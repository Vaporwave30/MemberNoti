import webhook
import cfscrape
import time
import requests
import re
import datetime


user = ""
link = ""
uid = ""
lastKnownLink = ""

webhookURL = "https://discordapp.com/api/webhooks/518375280042311684/SxL5GzPoTzuamS61b_WHc1Y6qhZwLmTY5ftW7uLMGitciB-Y9gRidLh0lqOcXLyWaOer"
myBB = '393343_ZuuYc55ZirZAVfPEmhxXupyOPSoj5huEOERLdQr1ZydqaH5Fa0'
cookie = requests.cookies.RequestsCookieJar()
cookie.set('mybbuser', value=myBB, domain='.v3rmillion.net', path='/')
scraper = cfscrape.create_scraper()
scraper.cookies = cookie
now = datetime.datetime.now()

def func():
    global link
    global user
    global lastKnownLink
    while True:
        body = scraper.get("https://v3rmillion.net").text
        if 'Please welcome our newest member, <b><a href=' in body:
            try:
                link = re.search(r'Please welcome our newest member, <b><a href="(.*?)">', body).group(1)
                link = re.sub('&amp;', '&', link)
                if lastKnownLink != link:
                    user = re.search(r'">(.*?)</a></b><br', body).group(1)
                    uid = re.sub(r'https://v3rmillion.net/member.php\?action=profile&uid=', "", link)
                    print(uid)
                    print(f'{user}:{link}')
                    webhook.post_data(url=webhookURL, desc="Newest user:", user=user, link=link, UID=uid)
                    lastKnownLink = link
                    time.sleep(2)
            except Exception as oof:
                print(oof)
func()
