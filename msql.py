import sys
sys.path.append(r"C:\Program Files\Python38\Lib\site-packages")
import pymysql

def sql(db_name,sql_text):
    try:
        con = pymysql.connect('localhost',
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

def get_gid_from_domain(domain):

    # if(len(rez)==0):
    #     txt = 'INSERT INTO groups(`name`,`g_id`) VALUES (\''+ domain +'\', \'156\' )'
    #     rez2 = sql('vk',txt)
    #     print(rez2)

    return 0

groups_flds = {
    'name':'VARCHAR(255)',
    'g_id' : 'INT(11)'
}

posts_flds = {
    'text':'TEXT',
    'g_id' : 'INT(11)',
    'p_id' : 'INT(11)'
}

#create_table('groups',groups_flds)
#create_table( 'posts' , posts_flds )

get_gid_from_domain('egais_v_1c')

