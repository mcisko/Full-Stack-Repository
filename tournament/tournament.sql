-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Creating the project database

CREATE DATABASE tournament;

-- Connect to the database tournament

\c tournament

-- Creating Table tournament
Create TABLE tournament(Id serial PRIMARY KEY ,
                        name TEXT
                        );

-- Creating Table Player
-- I have added a foreign key referencing the tournament table.Using that model I can differentiate
--  between a regular player from a player registered in a tournament

CREATE TABLE player(Id SERIAl PRIMARY KEY,
                    name TEXT,
                    tounament_Id INTEGER  REFERENCES tournament(Id)

                    );

-- Creating table match
-- I have created winner and loser referencing players who have won or lost. The win or loss is valid
-- only if draw = false; if draw  =true then winner and loser will just indicated the players
-- competing


Create TABLE match(id SERIAl PRIMARY KEY ,
                  Winner  INTEGER REFERENCES player(Id)on DELETE CASCADE on UPDATE CASCADE,
                  Loser INTEGER REFERENCES player(Id) on DELETE CASCADE on UPDATE CASCADE,
                  draw boolean,
                  match_date DATE DEFAULT now()
                  );



