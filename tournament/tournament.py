#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname='tournament' ")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    cursor =conn.cursor()
    cursor.execute("DELETE FROM match ;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn =connect()
    cursor =conn.cursor()
    cursor.execute("DELETE FROM player;")
    conn.commit()
    conn.close


def countPlayers():
    """Returns the number of players currently registered."""
    conn =connect()
    cursor =conn.cursor()
    cursor.execute("select count(*) from player;")
    num = cursor.fetchone()
    conn.commit()
    conn.close()
    return num[0]

    
    


def registerPlayer(name):
            
    
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO player(name) values(%s);", (name,))
    conn.commit()
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
    cursor.execute("select k.id as id, k.name as name, (select count(*) from match as t where t.winner = k.id) as wins,(select count(*) from match m where k.id = m.playerid1 or k.id=m.playerid2) as matches from player as K order by wins desc;")
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
    cursor.execute("INSERT INTO match(playerid1,playerid2,winner,loser,draw) values (%s,%s,%s,%s,%s);",(winner,loser,winner,loser,False))
    conn.commit()
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
    cursor.execute('Select t.id , t.name from  player t order by (select count(*) from match as k where k.winner = t.id) desc;')
    results =cursor.fetchall()
    xalass  =()
    xalass2=()
    for row in results[0:2]:
        xalass +=row[0:2]
    for row in results[2:4]:
        xalass2 +=row[0:2]
    conn.close()
    return xalass,xalass2

