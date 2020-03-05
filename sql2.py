import sys
sys.path.append(r"C:\Program Files\Python38\Lib\site-packages")
import mysql.connector

try:
    con = mysql.connector.connect(
        user='user',
        password='',
        host='mysql.user.myjino.ru',
        database='dbname')

    with con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM bids""")
        print(cur)
        for row in cur:
            print(row)

except Exception as e:
    print("Exception =" , e )
