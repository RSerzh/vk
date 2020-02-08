import sys
sys.path.append(r"C:\Program Files\Python38\Lib\site-packages")
import requests

token = '4bdb3528b751be13b6df2d41fcdc28823a7e9457cedb19ffecfdc0b4de0685f8d0c9590c103dac70421ae'

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

get_cnt_posts("the_riddler_2k17")
