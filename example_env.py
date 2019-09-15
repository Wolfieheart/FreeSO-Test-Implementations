from flask import current_app
from flask import request
from pathlib import Path

import requests
import datetime
import json

def main():
    print("Starting FreeSO Functions")

    # * Get the API URL for the FreeSO API
    configPath = "D:/xMake/Documents/FreeSO-API-Test/configs"
    print("Reading Directory {0} for config attempt...".format(configPath))
    configPath_dir = Path(configPath)

    if configPath_dir.is_dir():
        print("{0} is a VALID directory. Continuing....".format(configPath_dir))
    else:
        print("{0} is an INVALID directory. Stopping....".format(configPath_dir))

    # * Attempt to read API_URL File
    try:
        apiURLFile = configPath_dir / 'API_URI'
        apiurl = apiURLFile.read_text()
    except:
        print("Unable to read API URL file(s) for configuration")
        # ! Error: Config File is missing
        return (json.dumps({'error': 'Config File Missing'}), 500, {'Content-Type': 'application/json'})
    else:
        print("API_URL Value is: {0}".format(apiurl))     

    #! No Oauth or API Key currently required
    print("Building a Response... Please wait....")

    # * All Code to get City.json from API
    response = getCity(apiurl) #! Method to be depreciated in the userapi

    #TODO: Make all of these in seperate files
    # * All Code for Avatars API
    #response = getAvatarInfo(apiurl)
    #response = getOnlineAvatars(apiurl)
    
    # * All Code for LotsAPI
    #response = getLotsInfo(apiurl)
    #response = getOnlineLots(apiurl)

    # * Code to get Lot Thumbnail
    #response = getLotThumbnail(apiurl)

    # * All Code for Top 100 API
    #response = getAllTop100(apiurl)  
    #response = getTop100ByCategory(apiurl)

    # * All code for Neighborhoods API
    #response = getNeighborhoods(apiurl)  

    # * Return the Response
    print("Sending response: {0}".format(json.dumps(response)))
    return (json.dumps(response, indent=4), 200, {'Content-Type': 'application/json'})

def apiQuery(apiurl):
    try:
        print("Requesting {0} ... ".format(apiurl))
        # * APIKey = Personal Access Token from GitLab
        response = requests.get(apiurl, headers={'Content-Type':'application/json'})
    except Exception as e:
        print("Could not read url {0}".format(apiurl))
        print(type(e))
        current_app.logger.error(e.args)
        current_app.logger.error(e)
    return response.json()

def getCity(apiurl):
    response = {}
    print("TODO")
    return response