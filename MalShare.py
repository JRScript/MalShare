__author__= "Jithin Raj"

import requests
import json
import pandas as pd
import time
import openpyxl as op
import os
import shutil

def malshare():
    code = open('api.txt', 'r')
    api = code.read()
    response = requests.get("https://malshare.com//api.php?api_key="+api+"&action=getlist")
    result = response.json()
    res = open('result.json', 'w+')
    json.dump(result, res)
    code.close()
    res.close()
    data = pd.read_json('result.json')
    data.to_excel('MalShare IOC.xlsx')
    ex1 = op.load_workbook('MalShare IOC.xlsx')
    ws = ex1.active
    ws.delete_cols(1)  # deleting the columns
    cwd = os.getcwd()
    ex1.save(cwd + '//Results//MalShare IOC-' + time.strftime("%m-%d-%Y") + '.xlsx')
    os.remove("MalShare IOC.xlsx")
    print("Successfully generated MalShare IOC")

malshare()
