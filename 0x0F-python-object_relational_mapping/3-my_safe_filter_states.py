#!/usr/bin/python3

"""
SQL injection
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Displays all values in the states table of the database

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
