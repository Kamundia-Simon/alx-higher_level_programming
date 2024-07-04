#!/usr/bin/python3
"""
add Louisiana
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    ses = Session()

    louisiana = State(name="Louisiana")
    ses.add(louisiana)
    ses.commit()
    print(louisiana.id)
