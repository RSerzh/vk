import sys
sys.path.append(r"C:\Program Files\Python38\Lib\site-packages")
import requests
import time
from pprint import pprint
import msql

token = '4bdb3528b751be13b6df2d41fcdc28823a7e9457cedb19ffecfdc0b4de0685f8d0c9590c103dac70421ae'

def get_my_format_time(sec):
    return time.strftime("%d.%m.%y %H:%M:%S",time.localtime(sec))

# Функция для анализ массива постов сообщества
def get_post_list(domain,cnt):
    cnt = 5
    arr_p = get_posts(domain,cnt,0)

    items = arr_p['items']
    #pprint( arr_p , depth=2 )
    for i in items:
        dt = '(' + get_my_format_time( i['date'] ) + ')'
        txt = str(i['id']) + ' ' + dt + ' ' + str(len(i['text'])) + ' Att='
        if 'attachments' in i:
            txt = txt + str(len(i['attachments']))
        if 'copy_history' in i:
            txt += ' ch= ' + i['copy_history']

        print( txt )
        print(i['text'])

# Функция сканирует сообщество и подсчитывает какие поля 1-го уровня сколько раз
# использовались
def scan_domain_fields(domain):
    cnt_posts = get_cnt_posts(domain)
    print("Постов",cnt_posts)

    fld1 = {}
    start = time.time()
    qst = 0
    for i in range(0,cnt_posts,100):
        arr_p = get_posts(domain,100,i)
        qst += 1
        items = arr_p['items']
        time.sleep(0.5)
        for j in items:
            for k in j:
                if k in fld1:
                    fld1[k] += 1
                else:
                    fld1[k]=1

        print(i,'-', end='')
    print('')
    print(fld1,end='\n')
    print("Время работы", round( time.time()-start , 3) ,'сек. Запросов:',qst)

def set_group_cur(domain):
    txt = 'SELECT name,gid FROM groups WHERE name=\''+domain+'\''
    rez = msql.sql('vk',txt)
    print('Selection=',rez)
    if(len(rez)==0):
        gpinfo = get_group_info(domain)
        gid = gpinfo[0]['id']
        txt = 'INSERT INTO groups(`name`,`gid`) VALUES (\''+ domain +'\', \'' + str(gid) + '\' )'
        rez = msql.sql('vk',txt)
        print('Insertion=',rez)
    else:
        gid = rez[0]['gid']
    return gid

# Обработка поста. Если есть в базе, то провряем на изменения и если отличаются правим
# Если нет в базе заносим
def proceccing_post(params):
    pid = params['pid']
    gid = params['gid']
    text = params['text']
    date = params['date']

    txt = 'SELECT * FROM posts WHERE pid=' + str(pid)
    rez = msql.sql('vk',txt)
    if(len(rez)>0):
        print(rez)
    else:
        txt = 'INSERT INTO posts(gid,pid,dt,text) VALUES (\'' + str(gid) + '\',\'' + str(pid)
        txt += '\',\'' + date + '\',\'' + text + '\' )'
        msql.sql('vk',txt)
        print(date)
        print('ins ' + str(pid))


def date_convert(dt):
    if(dt.find('-')>0):
        print('MySQL',dt)
    else:
        print('myFormat',dt)

def scan_domain(domain):
    dt = '02.03.20 10:26:11'
    msqldt = '2020-03-02 10:26:11'
    date_convert(msqldt)
    return

    gid = set_group_cur(domain)
    print(gid)
    cnt_posts = get_cnt_posts(domain)
    print('Группа = ' + domain , "ID = " + str(gid)  ,'Постов',cnt_posts)
    time.sleep(0.5)
    arr_p = get_posts(domain,2,0)
    items = arr_p['items']
    time.sleep(0.5)

    params = {}
    params['gid'] = gid

    for j in items:

        pid = j['id']
        text = j['text']
        date = get_my_format_time(j['date'])

        params['pid'] = pid
        params['date'] = date
        params['text'] = text

        proceccing_post(params)

        #print( 'id=', pid , 'date=', date )
        #print( 'text=' , text )

    return False

    start = time.time()
    qst = 0
    for i in range(0,cnt_posts,100):
        arr_p = get_posts(domain,100,i)
        qst += 1
        items = arr_p['items']
        time.sleep(0.5)
        for j in items:
            #print( 'id=', j['id'] , 'date=', get_my_format_time(j['date']) )
            #print( 'text=' , j['text'])
            #if 'text' in j:
            #print( 'text=' , j['text'])
            #if 'attachments' in j:
            #print( j['attachments']['title'] )
            if 'copy_history' in j:
                print('-CPH-')

        print('---Step---',i,'items=',len(items))

    print("Время работы", round( time.time()-start , 3) ,'сек. Запросов:',qst)

def get_posts(domain,cnt=1,offset=0):
    params={'access_token': token,'v': '5.103','domain':domain,'count':cnt,'offset':offset }
    url = 'https://api.vk.com/method/wall.get'
    r = requests.get(url,params)
    return r.json()['response']

def get_cnt_posts(domain):
    params={'access_token': token,'v': '5.103','domain':domain,'count':1 }
    url = 'https://api.vk.com/method/wall.get'
    r = requests.get(url,params)
    r = r.json()
    return r['response']['count']

# Возвращает массив информации о сообществе
def get_group_info(domain):
    flds = 'activity,age_limits,can_create_topic,can_message,can_post,can_see_all_posts,can_upload_doc,can_upload_video,city,contacts,counters,country,description,fixed_post,links,member_status,members_count,place,site,status,trending,verified,wall,start_date'
    params={'access_token': token,'v': '5.103','group_id':domain,'fields':flds }
    url = 'https://api.vk.com/method/groups.getById'
    r = requests.get(url,params)
    return r.json()['response']

# Для метода groups.getById
params={
    #'access_token': '4bdb3528b751be13b6df2d41fcdc28823a7e9457cedb19ffecfdc0b4de0685f8d0c9590c103dac70421ae',
    'v': '5.103',
    'group_ids':'the_riddler_2k17',
    'fields':'can_upload_doc,city,city,place,members_count,status,wall'
}

# Для метода wall.get
#url = 'https://api.vk.com/method/groups.getById'
#url = 'https://api.vk.com/method/wall.get'
# space_engineers , the_riddler_2k17

#dmn = 'the_riddler_2k17'
#dmn = 'egais_v_1c'
dmn = 'space_engineers'

scan_domain(dmn)

#scan_domain(dmn)
#scan_domain_fields(dmn)
#get_post_list(dmn,25)


