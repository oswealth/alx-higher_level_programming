#!/usr/bin/python3
"""
print the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_to_search = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_username,
        mysql_password,
        database_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    state = session.query(State).filter(
            State.name == state_to_search).order_by(
                    State.id).first()

    if state:
        if state.name == state_to_search:
            print(f'{state.id}')
    else:
        print('Not found')

    session.close()
