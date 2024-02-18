#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import sessionmaker

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_username,
        mysql_password,
        database_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    states = session.query(State).order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
