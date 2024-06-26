#!/usr/bin/python3
"""
Lists all states from the db hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # creat connection to db

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
