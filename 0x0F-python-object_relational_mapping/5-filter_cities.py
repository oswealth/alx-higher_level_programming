#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=mysql_username,
                           passwd=mysql_password,
                           db=database_name)
    cur = conn.cursor()
    query = "SELECT cities.name\
             FROM cities\
             INNER JOIN states\
             WHERE cities.state_id = states.id\
             AND states.name = %s\
             ORDER BY cities.id ASC;"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    rows = [row[0] for row in rows]
    print(", ".join(rows))
    conn.close()
