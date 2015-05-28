# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()    
    c.execute("DELETE FROM matches")
    #Always commit after a DELETE
    DB.commit()     
    DB.close() 


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players")
    #Always commit after a DELETE
    DB.commit()         
    DB.close()
    

def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT count(id) FROM players")
    players_registered = c.fetchall()
    DB.close()
    #Returning only the first column, first row cell content of this query
    return players_registered[0][0]
    

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    #Inserting or entering the players names into the Players table
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    #Always commit after an INSERT
    DB.commit()    
    DB.close()
    

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    #Dropping or removing the following views if they already exist in the database
    c.execute("DROP VIEW IF EXISTS win CASCADE")
    c.execute("DROP VIEW IF EXISTS loss")
    c.execute("DROP VIEW IF EXISTS matchesplayed")
    c.execute("DROP VIEW IF EXISTS standings")
    
    #Creating view "win" to list the players that have won a match
    c.execute("CREATE VIEW win AS SELECT players.id, players.name, count(matches.winner) as wins FROM players LEFT JOIN matches ON players.id = matches.winner GROUP BY players.id ORDER BY wins DESC")
    #Creating view "loss" to list the players that have lost a match
    c.execute("CREATE VIEW loss AS SELECT players.id, players.name, count(matches.loser) as loses FROM players LEFT JOIN matches ON players.id = matches.loser GROUP BY players.id ORDER BY loses DESC")
    #Creating view "matchesplayed" to list the players wins and loses into one view table
    c.execute("CREATE VIEW matchesplayed AS SELECT win.id, win.name, win.wins, sum(win.wins + loss.loses) as played FROM win LEFT JOIN loss ON win.id = loss.id GROUP BY win.id, win.name, win.wins")
    #Creating view "standings" for the current round
    c.execute("CREATE VIEW standings AS SELECT players.id, players.name, matchesplayed.wins, matchesplayed.played as matches FROM players LEFT JOIN matchesplayed ON players.id = matchesplayed.id GROUP BY players.id, matchesplayed.wins, matchesplayed.played ORDER BY matchesplayed.wins DESC")
    #Running the view "standings" query
    c.execute("SELECT * FROM standings")
    #Pulling the "standings" query results and storing them in the players_standings object
    players_standings = c.fetchall()
    DB.commit()
    DB.close()
    #Returning the "standings" query results
    return players_standings    
    

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    #Inserting or entering the results of a match (winner and loser) into the "matches" table
    c.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s)", (winner,loser))
    #Always commit after an INSERT
    DB.commit()   
    DB.close()    
    
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = connect()
    c = DB.cursor()
    #Running a self joining query using the "standings" view query result to list the pairs of players for the next round
    c.execute("SELECT a.id AS id1, a.name AS name1, b.id AS id2, b.name AS name2 FROM standings AS a, standings AS b WHERE a.wins = b.wins AND a.id < b.id ORDER BY a.wins DESC")
    #Pulling the query results and storing them in the swiss_pairings object
    swiss_pairings = c.fetchall()
    DB.commit()   
    DB.close()
    #Returning the query results that were stored in the swiss_pairings object
    return swiss_pairings    



