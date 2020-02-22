import sys
sys.path.append(r"C:\Program Files\Python38\Lib\site-packages")
import pymysql

def create_table(tname,flds):
    try:
        con = pymysql.connect('localhost', 'root','','vk')
        with con:
            cur = con.cursor()

            sql = 'CREATE TABLE IF NOT EXISTS '
            sql += tname + '(`id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT, '
            for k in flds:
                sql += ' `' + k + '` ' + flds[k] + ' NOT NULL,'
            sql += 'PRIMARY KEY(`id`))'

            print(sql)
            print('---')

            #sql = 'show tables like `' + tname + '`'
            rez = cur.execute(sql)
            print(rez)

            #rez = cur.execute(sql)


    except Exception as e:
        print( e )

flds = {
    'name':'VARCHAR(255)',
    'age' : 'INT',
    'dr' : 'DATETIME'
}

create_table('bg4',flds)

