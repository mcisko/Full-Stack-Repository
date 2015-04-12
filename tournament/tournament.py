#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    cursor =conn.cursor()
    cursor.execute('DELETE from match;')
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn =connect()
    cursor =conn.cursor()
    cursor.execute('DELETE FROM PLAYER;')
    conn.close


def countPlayers():
    """Returns the number of players currently registered."""
    conn =connect()
    cursor =conn.cursor()
    Count_number_of_players =cursor.execute('select count(*) from player;')
    conn.close()
    return Count_number_of_players
    
    


def registerPlayer(name):
            
    
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = coonect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO player(name) values ('Mamadou');")
    conn.close()
    


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
    conn = connect()
    cursor =conn.cursor()
    cursor.execute("select k.id, k.name, (select count(*) from match as t where t.winner = k.id)as match_won,(select count(*) from match m where k.id = m.playerid1 or k.id=m.playerid2) as Number_matches_played from player as K order by match_won desc;")
    results = cursor.fetchall()
    conn.close()
    return results
   

def reportMatch(winner, loser):
                   
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn =connect()
    cursor =conn.cursor()
    cursor.execute("INSERT INTO match value(winner,loser,winner,loser,FALSE );")
    conn.close()

 
 
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
    conn =connect()
    cursor =conn.cursor()
    cursor.execute('Select t.id , t.name, k.id,k.name from  player as t,player as k where t.id > k.id;')
    results =cursor.fetchall()
    conn.close()
    return results

