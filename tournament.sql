-- Table definitions for this Swiss-System-Tournament project.

-- Creating database
CREATE DATABASE tournament;

-- Connecting to database tournament;
\c tournament;

-- Creating tables for players and matches
CREATE TABLE players (name text, id serial primary key);
CREATE TABLE matches (winner integer references players(id), loser integer references players(id));

















