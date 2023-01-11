import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests
from bs4 import BeautifulSoup
from datetime import date
from glob import *


mydict = {
    "FC Bayern München" : "1-FC+Bayern+München",
    "Borussia Dortmund" : "5-Borussia+Dortmund",
    "Bayer Leverkusen" : "8-Bayer+04+Leverkusen",
    "RB Leipzig" : "92-RB+Leipzig",
    "FC Union Berlin" : "109-1.+FC+Union+Berlin",
    "SC Freiburg" : "21-Sport-Club+Freiburg",
    "FC Köln" : "13-1.+FC+Köln",
    "FSV Mainz 05" : "18-1.+FSV+Mainz+05",
    "TSG Hoffenheim" : "62-TSG+Hoffenheim",
    "Borussioa M'Gladbach" : "3-Borussia+M'gladbach",
    "Eintrach Frankfurt" : "9-Eintracht+Frankfurt",
    "VfL Wolfsburg" : "12-VfL+Wolfsburg",
    "VfL Bochum" : "15-VfL+Bochum",
    "FC Augsburg" : "68-FC+Augsburg",
    "VfB Stuttgart" : "14-VfB+Stuttgart",
    "Hertha BSC" : "7-Hertha+BSC",
    "FC Schalke 04" : "10-FC+Schalke+04",
    "SV Werder Bremen" : "6-SV+Werder+Bremen"
}

global playerid, playername, position, punkte, pps, passq, zweikampf, marktwert, verein

playerid = []
playername = []
position = []
punkte = []
pps = []
passq = []
zweikampf = []
marktwert= []
verein = []
datum = []

def scrap(scripts, team):
    for i in range(9,len(scripts)-13):
        playerid.append(str(scripts[i]).split('data-playerid="')[1].split('">')[0])
        playername.append(str(scripts[i]).split('"_blank">')[1].split('</a><')[0])
        position.append(str(scripts[i]).split('title="')[1].split('"/><')[0])
        punkte.append(str(scripts[i]).split('<td class="base"')[1].split('<td>')[1].split('</td>')[0])
        pps.append(str(scripts[i]).split('<td class="base"')[1].split('td class="extended">')[2].split('</td>')[0])
        passq.append(str(scripts[i]).split('<td class="base"')[1].split('td class="extended">')[4].split('</td>')[0])
        zweikampf.append(str(scripts[i]).split('<td class="base"')[1].split('td class="extended">')[5].split('</td>')[0])
        marktwert.append(str(scripts[i]).split('data-value="')[1].split('"><span')[0])
        verein.append(team)
        datum.append(date.today().strftime("%d/%m/%Y"))

for x in mydict:
    team = x


base_url = 'https://stats.comunio.de/squad/' + mydict[x]
res = requests.get(base_url)
soup = BeautifulSoup(res.content, 'lxml')
scripts = soup.find_all('tr')
scrap(scripts, team)

df = pd.DataFrame(playerid, columns=['Playerid'])
df['Datum'] = pd.Series(datum)
df['Verein'] = pd.Series(verein)
df['Name'] = pd.Series(playername)
df['Position'] = pd.Series(position)
df['Punkte'] = pd.Series(punkte)
df['Punkte pro Spiel'] = pd.Series(pps)
df['Passquote'] = pd.Series(passq)
df['Zweikampf'] = pd.Series(zweikampf)
df['Marktwert'] = pd.Series(marktwert)

tag = date.today().strftime('%d/%m/%Y')
tag = tag.replace("/", "_")

df.to_csv(str(tag) + ".csv", index=False)