#!/usr/bin/python3
"""
print the first State object from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_username,
        mysql_password,
        database_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).first()

    if not first:
        print("Nothing")
    else:
        print(f'{first.id}: {first.name}')

    session.close()
