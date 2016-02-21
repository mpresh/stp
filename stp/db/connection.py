import MySQLdb

CURSOR = None

def get_cursor():
    global CURSOR
    if CURSOR is None:
        db = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="",
                             db="stp")
        CURSOR = db.cursor()
        
    return CURSOR
    
def main():
    cursor =  get_cursor()
    cursor.execute("SELECT * FROM stocks")
    for row in cursor.fetchall():
        print row[0]
        db.close()

    
if __name__ == "__main__":
    main()
