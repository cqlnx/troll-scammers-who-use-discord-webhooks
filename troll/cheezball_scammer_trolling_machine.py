#shit is hella slow but i mean it works
#pls only use this to troll scammers who use discord webhooks
import string, json, requests, random
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep
system ('cls')

system("title " + "Cheezballs Scammer Trolling Machine")

print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter ("pls only use this to troll scammer and hackers press enter to continue")))
input ("")
system ('cls')
print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter("continuing in 3")))
sleep (1)
system ('cls')
print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter ("2")))
sleep (1)
system ('cls')
print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter ("1")))
sleep(1)

system('cls')
neeger1 = True
neeger2 = True
sent_count = 1

def send_message(webhook_url):
    global sent_count
    username_base = "cheesballs spammer on top"
    random_numbers = ''.join(random.choices(string.digits, k=3))
    username = f"{username_base} {random_numbers}"
    message = "@everyone FUCKED BY CHEEZBALLS WEBHOOK SPAMMER https://media.discordapp.net/attachments/1153758480868581387/1190043957305028679/togif-3.gif?ex=65c547cd&is=65b2d2cd&hm=ad455c71dba6ceddea80ad3cdb9d3e844133da4412fbd12b7385784d21555d53& "
    avatar = "https://cdn.discordapp.com/attachments/1154878697870995499/1201264583013302302/COOL_KASS.png?ex=65c92fd3&is=65b6bad3&hm=faaf0ba96ab98056cffcb6385e4f31c0bce24c07c7a26bee060b5104ba3c50eb&".format(random.randint(1, 500))
    data = {
        "content": message,
        "username": username,
        "avatar_url": avatar,
        "tts": False
    }

    header = {
        "content-type": "application/json"
    }

    response = requests.post(webhook_url, json=data, headers=header)

    if response.ok:
        system('cls')
        print(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(webhooktext)))
        print(Colorate.Horizontal(Colors.blue_to_green, f"[+] Message sent! [ {sent_count} ]"))
        return True
    elif response.status_code == 429:
        system('cls')
        print(Colorate.Horizontal(Colors.black_to_red, Center.XCenter(webhooktext)))
        print(Colorate.Horizontal(Colors.black_to_red, "[/] Rate limit exceeded..."))
        sleep(2)
        return False
    else:
        system('cls')
        print(Colorate.Horizontal(Colors.black_to_red, Center.XCenter(webhooktext)))
        print(Colorate.Horizontal(Colors.black_to_red, "[!] Failed to send message !"))
        sleep(15)
        return False

CHEEZBALLS = ("""
 ██████╗██╗  ██╗███████╗███████╗███████╗██████╗  █████╗ ██╗     ██╗     ███████╗
██╔════╝██║  ██║██╔════╝██╔════╝╚══███╔╝██╔══██╗██╔══██╗██║     ██║     ██╔════╝
██║     ███████║█████╗  █████╗    ███╔╝ ██████╔╝███████║██║     ██║     ███████╗
██║     ██╔══██║██╔══╝  ██╔══╝   ███╔╝  ██╔══██╗██╔══██║██║     ██║     ╚════██║
╚██████╗██║  ██║███████╗███████╗███████╗██████╔╝██║  ██║███████╗███████╗███████║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ """)
SCAMMER = ("""
███████╗ ██████╗ █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
███████╗██║     ███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
╚════██║██║     ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝""")

TROLLING = ("""
████████╗██████╗  ██████╗ ██╗     ██╗     ██╗███╗   ██╗ ██████╗ 
╚══██╔══╝██╔══██╗██╔═══██╗██║     ██║     ██║████╗  ██║██╔════╝ 
   ██║   ██████╔╝██║   ██║██║     ██║     ██║██╔██╗ ██║██║  ███╗
   ██║   ██╔══██╗██║   ██║██║     ██║     ██║██║╚██╗██║██║   ██║
   ██║   ██║  ██║╚██████╔╝███████╗███████╗██║██║ ╚████║╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝""")

MACHINE = ("""
███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
""")

TROLL = ("""
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQWQQQQQWWWBBBHHHHHHHHHBWWWQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQD!`__ssaaaaaaaaaass_ass_s____.  -~""??9VWQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQP'_wmQQQWWBWV?GwwwmmWQmwwwwwgmZUVVHAqwaaaac,"?9$QQQQQQQQQQQQQQ
QQQQQQQQQQQW! aQWQQQQW?qw#TTSgwawwggywawwpY?T?TYTYTXmwwgZ$ma/-?4QQQQQQQQQQQ
QQQQQQQQQQW' jQQQQWTqwDYauT9mmwwawww?WWWWQQQQQ@TT?TVTT9HQQQQQQw,-4QQQQQQQQQ
QQQQQQQQQQ[ jQQQQQyWVw2$wWWQQQWWQWWWW7WQQQQQQQQPWWQQQWQQw7WQQQWWc)WWQQQQQQQ
QQQQQQQQQf jQQQQQWWmWmmQWU???????9WWQmWQQQQQQQWjWQQQQQQQWQmQQQQWL 4QQQQQQQQ
QQQQQQQP'.yQQQQQQQQQQQP"       <wa,.!4WQQQQQQQWdWP??!"??4WWQQQWQQc ?QWQQQQQ
QQQQQP'_a.<aamQQQW!<yF "!` ..  "??$Qa "WQQQWTVP'    "??' =QQmWWV?46/ ?QQQQQ
QQQP'sdyWQP?!`.-"?46mQQQQQQT!mQQgaa. <wWQQWQaa _aawmWWQQQQQQQQQWP4a7g -WWQQ
QQ[ j@mQP'adQQP4ga, -????" <jQQQQQWQQQQQQQQQWW;)WQWWWW9QQP?"`  -?QzQ7L ]QQQ
QW jQkQ@ jWQQD'-?$QQQQQQQQQQQQQQQQQWWQWQQQWQQQc "4QQQQa   .QP4QQQQfWkl jQQQ
QE ]QkQk $D?`  waa "?9WWQQQP??T?47`_aamQQQQQQWWQw,-?QWWQQQQQ`"QQQD\Qf(.QWQQ
QQ,-Qm4Q/-QmQ6 "WWQma/  "??QQQQQQL 4W"- -?$QQQQWP`s,awT$QQQ@  "QW@?$:.yQQQQ
QQm/-4wTQgQWQQ,  ?4WWk 4waac -???$waQQQQQQQQF??'<mWWWWWQW?^  ` ]6QQ' yQQQQQ
QQQQw,-?QmWQQQQw  a,    ?QWWQQQw _.  "????9VWaamQWV???"  a j/  ]QQf jQQQQQQ
QQQQQQw,"4QQQQQQm,-$Qa     ???4F jQQQQQwc <aaas _aaaaa 4QW ]E  )WQ`=QQQQQQQ
QQQQQQWQ/ $QQQQQQQa ?H ]Wwa,     ???9WWWh dQWWW,=QWWU?  ?!     )WQ ]QQQQQQQ
QQQQQQQQQc-QWQQQQQW6,  QWQWQQQk <c                             jWQ ]QQQQQQQ
QQQQQQQQQQ,"$WQQWQQQQg,."?QQQQ'.mQQQmaa,.,                . .; QWQ.]QQQQQQQ
QQQQQQQQQWQa ?$WQQWQQQQQa,."?( mQQQQQQW[:QQQQm[ ammF jy! j( } jQQQ(:QQQQQQQ
QQQQQQQQQQWWma "9gw?9gdB?QQwa, -??T$WQQ;:QQQWQ ]WWD _Qf +?! _jQQQWf QQQQQQQ
QQQQQQQQQQQQQQQws "Tqau?9maZ?WQmaas,,    --~-- ---  . _ssawmQQQQQQk 3QQQQWQ
QQQQQQQQQQQQQQQQWQga,-?9mwad?1wdT9WQQQQQWVVTTYY?YTVWQQQQWWD5mQQPQQQ ]QQQQQQ
QQQQQQQWQQQQQQQQQQQWQQwa,-??$QwadV}<wBHHVHWWBHHUWWBVTTTV5awBQQD6QQQ ]QQQQQQ
QQQQQQQQQQQQQQQQQQQQQQWWQQga,-"9$WQQmmwwmBUUHTTVWBWQQQQWVT?96aQWQQQ ]QQQQQQ
QQQQQQQQQQWQQQQWQQQQQQQQQQQWQQma,-?9$QQWWQQQQQQQWmQmmmmmQWQQQQWQQW(.yQQQQQW
QQQQQQQQQQQQQWQQQQQQWQQQQQQQQQQQQQga%,.  -??9$QQQQQQQQQQQWQQWQQV? sWQQQQQQQ
QQQQQQQQQWQQQQQQQQQQQQQQWQQQQQQQQQQQWQQQQmywaa,;~^"!???????!^`_saQWWQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQWWWWQQQQQmwywwwwwwmQQWQQQQQQQQQQQ
QQQQQQQWQQQWQQQQQQWQQQWQQQQQWQQQQQQQQQQQQQQQQWQQQQQWQQQWWWQQQQQQQQQQQQQQQWQ""") #funny troll face


print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(CHEEZBALLS)))
sleep(1)
system('cls')
print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(SCAMMER)))
sleep(1)
system('cls')
print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(TROLLING)))
sleep(1)
system('cls')
print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(MACHINE)))
sleep(1)
system('cls')
print(Colors.red, Center.XCenter (TROLL))
sleep(1)
system('cls')

webhooktext = """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝"""

print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(webhooktext)))
print(Colorate.Horizontal(Colors.yellow_to_red, "[-] The webhook ur gonna be putting in here is gonna be used later on"))
print(Colorate.Horizontal(Colors.yellow_to_red, "[-] Enter a Webhook URL ↓"))
webhook_url = input("")
system ("cls")

print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(webhooktext)))
def main():
    global neeger1, sent_count, neeger2
    print(Colorate.Horizontal(Colors.red_to_yellow,"1. Delete Webhook URL | 2. Spamm Webhook URL"))
    print(Colorate.Horizontal(Colors.red_to_yellow,"Enter your choice ↓"))
    choice = input("")

    if choice == '1':
        print(Colorate.Horizontal(Colors.red_to_yellow, "[!] Are you sure that you want to delete the webhook URL? Press enter to delete it (also if u get a error that means that the webhook is not right)"))
        input("")                        
        requests.delete(webhook_url)
        sleep(1)
        print(Colorate.Horizontal(Colors.red_to_yellow, "[!]Webhook deleted"))

    elif choice == '2':
        while neeger1:
            if webhook_url.startswith("https://discord.com/api/webhooks/"):
                neeger1 = False
                system('cls')
            else:
                system('cls')
                print(Colorate.Horizontal(Colors.black_to_red, Center.XCenter(webhooktext)))
                print(Colorate.Horizontal(Colors.black_to_red, "[!] Error valid link !"))
                sleep(2)
                system('cls')

        while neeger2:
            if send_message(webhook_url):
              sent_count += 1
            else:
                print("Error sending message")

if __name__ == "__main__":
    main()