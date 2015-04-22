#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():

    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname='postgres'")

def runACommand(CommandText):
    """This is a generic function that  helps in executing sql script without repeating the same procedures
        It helps me implement the DRY  policy """
    conn =connect()
    cursor =conn.cursor()
    cursor.execute(CommandText)
    conn.commit()
    conn.close()

def deleteMatches():
    """Remove all the match records from the database."""
    runACommand("DELETE FROM match ;")



def deletePlayers():
    """Remove all the player records from the database."""
    runACommand("DELETE FROM player;")


def countPlayers():
    """Returns the number of players currently registered."""
    conn =connect()
    cursor =conn.cursor()
    cursor.execute("select count(*) from player;")
    num = cursor.fetchone()
    conn.commit()
    conn.close()
    return num[0]

    
    


def registerPlayer(name,tournament_id = None):
            
    
    """Adds a player to the tournament database. We can register a player
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO player(name,tounament_id) values(%s , %s);", (name,tournament_id))
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
    cursor.execute("select k.id as id, k.name as name, (select count(*) from match as t where t.winner = k.id and draw = false) as wins,(select count(*) from match m where k.id = m.winner or k.id=m.loser) as matches from player as K order by wins desc;")
    results = cursor.fetchall()
    conn.close()
    return results
   

def reportMatch(winner, loser,draw=False):
                   
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
      draw : defaulted to false.If draw is equal to true there is no winner or loser

    """
    conn =connect()
    cursor =conn.cursor()
    cursor.execute("INSERT INTO match(winner,loser,draw) values (%s,%s,%s);",(winner,loser,draw))
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
    cursor.execute('Select t.id , t.name from  player t order by (select count(*) from match as k where k.winner = t.id and draw = False) desc;')
    results =cursor.fetchall()
    """ Break down the results set in odd and even index """
    even = results[0::2]
    odd =results[1::2]
    conn.close()
    final =zip(even,odd)
    """Put the results in pairs for display"""
    final_result = final[0][0]+final[0][1],final[1][0]+final[1][1]
    return final_result

