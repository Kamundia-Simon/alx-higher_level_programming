#!/usr/bin/python3

import sys
import MySQLdb


def list_states(username, password, dbname):
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passd=password,
            dbn=dbname,
            charset="utf8"
            )
    cr = conn.cursor()
    cr.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cr.fetchall():
        print(row)
        cr.close()
        conn.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
