import requests
def post_data(url, desc, user, link, UID):
    post = {
        "username": "User notifier!",
        "avatar_url": "https://i.boring.host/J66Eot2.png",
        "embeds": [
        {
            "author": {
            "name": "Vaporwave30",
            "url": "https://v3rmillion.net/member.php?action=profile&uid=393343",
            "icon_url": "https://i.boring.host/J679G0m.png"
        },
            "title": "Another new user has signed up to this site!",
            "description": desc,
            "color": 3843043,
            "fields": [
            {
                "name": "Username:",
                "value": user,
                "inline": True
            },
            {
                "name": "Link:",
                "value": link,
                "inline": True
            },
            {
                "name": "UserID:",
                "value": UID,
                "inline": False
            },
        ],
            "footer": {
             "text": "Made by Vaporwave30 ",
                "icon_url": "https://i.boring.host/JDZiDf5.png"
            }
        }
        ]
    }
    a = requests.post(url, json=post)
    print(a.status_code)

