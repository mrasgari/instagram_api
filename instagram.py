from requests import get,cookies
from json import loads
import configparser

configParser = configparser.RawConfigParser()   
configFilePath = r'./config.txt'
configParser.read(configFilePath)


jar = cookies.RequestsCookieJar()
jar.set('csrftoken', configParser.get('your-config', 'csrftoken') , domain='.instagram.com', path='/')
jar.set('ds_user_id', configParser.get('your-config', 'ds_user_id'), domain='.instagram.com', path='/')
jar.set('fbm_124024574287414', 'base_domain=.instagram.com', domain='.instagram.com', path='/')
jar.set('mid', configParser.get('your-config', 'mid') , domain='.instagram.com', path='/')
jar.set('rur', 'FRC', domain='.instagram.com', path='/')
jar.set('sessionid',configParser.get('your-config', 'sessionid') , domain='.instagram.com', path='/')
jar.set('shbid', configParser.get('your-config', 'shbid') , domain='.instagram.com', path='/')
jar.set('mcd', '3', domain='.instagram.com', path='/')
jar.set('shbts', configParser.get('your-config', 'shbts'), domain='.instagram.com', path='/')

def UserAccount(username):
   
    url='https://www.instagram.com/'+username+'/?__a=1'

    response=get(url,cookies=jar)
    if response.status_code == 200:
        if response.headers['content-type'] == 'application/json; charset=utf-8':
            json_data=loads(response.text)
        else:
            json_data=False
    else:
        json_data=False    
    return (json_data)

def Hashtag(hashtag):
   
    url='https://www.instagram.com/explore/tags/'+hashtag+'/?__a=1'

    response=get(url,cookies=jar)
    if response.status_code == 200:
        if response.headers['content-type'] == 'application/json; charset=utf-8':
            json_data=loads(response.text)
        else:
            json_data=False
    else:
        json_data=False    
    return (json_data)  

def Location(location_id):
   
    url='https://www.instagram.com/explore/tags/'+location_id+'/?__a=1'

    response=get(url,cookies=jar)
    if response.status_code == 200:
        if response.headers['content-type'] == 'application/json; charset=utf-8':
            json_data=loads(response.text)
        else:
            json_data=False
    else:
        json_data=False    
    return (json_data) 

def Post(post_shortcode):
    url='https://www.instagram.com/p/'+post_shortcode+'/?__a=1'
    response=get(url,cookies=jar)
    if response.status_code == 200:
        if response.headers['content-type'] == 'application/json; charset=utf-8':
            json_data=loads(response.text)
        else:
            json_data=False
    else:
        json_data=False    
    return (json_data) 


 


   


    