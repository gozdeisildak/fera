import MySQLdb


def connection():
    conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="gozo",
                           db="fera")
    c = conn.cursor()

    return c, conn
