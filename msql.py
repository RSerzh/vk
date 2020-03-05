import sys
sys.path.append(r"C:\Program Files\Python38\Lib\site-packages")
import pymysql

def sql(db_name,sql_text):
    try:
        con = pymysql.connect(
            'localhost',
            'root',
            '',
            db_name,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        with con:
            cur = con.cursor()
            rez = cur.execute(sql_text)
            return cur.fetchall()

    except Exception as e:
        print( e )

def create_table(tname,flds):
    try:
        con = pymysql.connect('localhost', 'root','','vk')
        with con:
            cur = con.cursor()

            sql = 'DROP TABLE IF EXISTS ' + tname
            rez = cur.execute(sql)
            print(rez)

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

def edit_column(tname,mode,col_name):
    try:
        con = pymysql.connect('localhost', 'root','','vk')
        with con:
            cur = con.cursor()
            if mode=='add':
                sql = 'ALTER TABLE ' + tname + ' ADD COLUMN ' + col_name

            if mode=='del':
                # col_name - может быть как именем колонки, так и списком имён колонок через запятую
                sql = 'ALTER TABLE ' + tname
                if col_name.find(',') > 0:
                    mas_col = col_name.split(',')
                    txt_col = ''
                    for i in mas_col:
                        if txt_col != '':
                            txt_col += ','
                        txt_col += ' DROP COLUMN ' + i
                    sql += txt_col
                else:
                    sql += ' DROP COLUMN ' + col_name

            print( 'SQL executed: ',sql )
            rez = cur.execute(sql)
            print(rez)

    except Exception as e:
        print( e )

# Функция для теста работы с sql на хостинге
def web_sql( params , sql_text ):
    print(params)
    print(sql_text)
    try:
        con = pymysql.connect(
            params['ip'],
            params['login'],
            params['pass'],
            params['dbname'],
            port=3307,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        with con:
            cur = con.cursor()
            rez = cur.execute(sql_text)
            return cur.fetchall()

    except Exception as e:
        print( 'Exepction =',e )

groups_flds = {
    'name':'VARCHAR(255)',
    'gid' : 'INT(11)'
}

posts_flds = {
    'text':'TEXT',
    'gid' : 'INT(11)',
    'pid' : 'INT(11)',
    'dt'  : 'DATETIME'
}

#create_table('groups',groups_flds)
#create_table( 'posts' , posts_flds )

#edit_column('posts','add','dt DATETIME NOT NULL')
#edit_column('posts','del','dt')
#edit_column('posts','del','st1,st2')
