import sys
sys.path.append(r"C:\Program Files\Python38\Lib\site-packages")
import requests
import time

token = '4bdb3528b751be13b6df2d41fcdc28823a7e9457cedb19ffecfdc0b4de0685f8d0c9590c103dac70421ae'

def get_my_format_time(sec):
    return time.strftime("%d.%m.%y %H:%M:%S",time.localtime(sec))

def scan_domain(domain):
    cnt_posts = get_cnt_posts(domain)
    print("Постов",cnt_posts)

    debug=True

    if(debug):
        arr_p = get_posts(domain,1,0)
        items = arr_p['items']
        print( items )
    if(debug):
        return

    for i in range(0,cnt_posts,100):
        arr_p = get_posts(domain,100,i)
        items = arr_p['items']
        time.sleep(1)
        for j in items:
            print( 'id=', j['id'] , 'date=', get_my_format_time(j['date']) )
            if 'text' in j:
                print( 'text=' , j['text'])
            if 'attachments' in j:
                print( j['attachments']['title'] )
        print('---Step---',i,'items=',len(items))


def get_posts(domain,cnt=1,offset=0):
    params={'access_token': token,'v': '5.103','domain':domain,'count':cnt,'offset':offset }
    url = 'https://api.vk.com/method/wall.get'
    r = requests.get(url,params)
    return r.json()['response']

def get_cnt_posts(domain):
    params={'access_token': token,'v': '5.103','domain':domain,'count':1 }
    url = 'https://api.vk.com/method/wall.get'
    r = requests.get(url,params)
    return r.json()['response']['count']

# Для метода groups.getById
params={
    'access_token': '4bdb3528b751be13b6df2d41fcdc28823a7e9457cedb19ffecfdc0b4de0685f8d0c9590c103dac70421ae',
    'v': '5.103',
    'group_ids':'the_riddler_2k17',
    'fields':'can_upload_doc,city,city,place,members_count,status,wall'
}

# Для метода wall.get
#url = 'https://api.vk.com/method/groups.getById'
#url = 'https://api.vk.com/method/wall.get'

scan_domain('the_riddler_2k17')
