import webhook
import cfscrape
import time
import requests
import re
import datetime


user = ""
link = ""
uid = ""
totalRegistered = ""
lastKnownLink = ""

webhookURL = ""
myBB = ''
cookie = requests.cookies.RequestsCookieJar()
cookie.set('mybbuser', value=myBB, domain='.v3rmillion.net', path='/')
scraper = cfscrape.create_scraper()
scraper.cookies = cookie

def func():
    global link
    global user
    global totalRegistered
    global lastKnownLink
    while True:
        body = scraper.get("https://v3rmillion.net").text
        if 'Please welcome our newest member, <b><a href=' in body:
            try:
                link = re.search(r'Please welcome our newest member, <b><a href="(.*?)">', body).group(1)
                link = re.sub('&amp;', '&', link)
                if lastKnownLink != link:
                    totalRegistered = re.search(r"We currently have (.*?) members registered.<br />", body).group(1)
                    user = re.search(r'">(.*?)</a></b><br', body).group(1)
                    uid = re.sub(r'https://v3rmillion.net/member.php\?action=profile&uid=', "", link)
                    print(uid)
                    print(f'{user}:{link}')
                    now = datetime.datetime.now()
                    webhook.post_data(url=webhookURL, desc="Found at " + now.strftime("%Y-%m-%d %H:%M"), user=user, link=link, UID=uid, tMembers=totalRegistered)
                    lastKnownLink = link
                    time.sleep(2)
            except Exception as oof:
                print(oof)
func()
