public = "4nk45di67zb5zgaic6jz7hujuj21de"
secret=  "ndvlpezqoy197xs3wkl8d582ss43e5"

from twitchAPI.twitch import Twitch
import json

twitch = Twitch(public, secret)

next = None
loop=0
def get_str(next, loop):
    resposta = twitch.get_streams(language="ca", after=next)
    print(len(resposta["data"]))
    with open(f'{loop}.json', 'w', encoding='utf-8') as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)
    try:
        next = resposta["pagination"]["cursor"]
        print("hi ha nova pàgina")
        loop = loop+1
        get_str(next, loop)
    except:
        print("final")
        pass
get_str(next, loop)
