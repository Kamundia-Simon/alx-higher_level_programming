#!/usr/bin/python3
"""
Displays all cities of a given state from states table
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Displays all cities of a given state from states table
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in cur.fetchall() if ct[4] == sys.argv[4]]))
