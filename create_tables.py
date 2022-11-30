from cassandra.cluster import Cluster
from sql_queries import create_table_queries, drop_table_queries

def create_cluster():

    cluster = Cluster()

    session = cluster.connect()

    session.execute("DROP KEYSPACE IF EXISTS udacity")
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS udacity 
        WITH REPLICATION = 
        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
    """
    ) 

    session.set_keyspace('udacity')

    return cluster, session

def drop_tables(session):
    
    for query in drop_table_queries:
        session.execute(query)

def create_tables(session):

    for query in create_table_queries:
        session.execute(query)

def main():

    cluster, session = create_cluster()

    drop_tables(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    main()