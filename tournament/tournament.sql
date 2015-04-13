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

-- Creating Table Player

CREATE TABLE player(Id SERIAl PRIMARY KEY,
                    name TEXT

                    );
-- Creating Table tournament
Create TABLE tournament(Id serial PRIMARY KEY , 
                        name TEXT
                        );

-- Creating tabe match
Create TABLE match(id SERIAl PRIMARY KEY ,
                  tournament_id INTEGER REFERENCES tournament(Id),
                  playerID1 Integer references player(Id) on DELETE CASCADE on UPDATE CASCADE ,
                  playerID2 INTEGER references player(Id) on DELETE CASCADE on UPDATE CASCADE ,
                  Winner  INTEGER REFERENCES player(Id)on DELETE CASCADE on UPDATE CASCADE,
                  Loser INTEGER REFERENCES player(Id) on DELETE CASCADE on UPDATE CASCADE,
                  draw Boolean,
                  match_date DATE DEFAULT now()
                  );



