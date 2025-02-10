from cassandra.cluster import Cluster

def count_firefox_accesses():

    cluster = Cluster(['10.254.3.108', '10.254.1.207', '10.254.2.126'])
    session = cluster.connect('log_keyspace')


    query = "SELECT user_agent FROM log_data_small_log;"
    rows = session.execute(query)

    # Count the occurrences of Firefox
    firefox_count = sum(1 for row in rows if 'Firefox' in row.user_agent)

    print(f"Number of accesses made by Firefox: {firefox_count}")
    cluster.shutdown()

if __name__ == '__main__':
    count_firefox_accesses()
