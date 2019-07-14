from time import sleep
from datetime import datetime
import os
import requests


def post_to_discord(msg):
	from discord_endpoint import discord_endpoint
    data = { "content": msg}
    requests.post(discord_endpoint, json = data)

bIsBuilding = False
while 1:   
    PROCNAME = "UnrealLightmass.exe"
    output = os.popen('tasklist /FI "IMAGENAME eq ' + PROCNAME + '"').read()
    # For Mac: output = os.popen('ps -ax | grep "' + PROCNAME + '"').read()   
    if not bIsBuilding and (len(output.split('\n'))>3):
        bIsBuilding = True
        post_to_discord("Your process started at {}. I am watching it for you!".format(datetime.now().strftime("%m/%d/%Y %H:%M:%S")))
    elif bIsBuilding and not (len(output.split('\n'))>3):
        bIsBuilding = False
        post_to_discord("Your process ended at {}. All done!".format(datetime.now().strftime("%m/%d/%Y %H:%M:%S")))
    sleep(1)
