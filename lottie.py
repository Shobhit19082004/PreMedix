import json 
import requests
import streamlit
from streamlit_lottie import st_lottie

def get (path:str):
    with open(path) as p:
        return json.load(p)
    
path=get('Animation - 1736172441933.json')
st_lottie(path)

def get_url(url:str):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

url=get_url('https://lottie.host/fe8971d2-7c1d-43b9-a177-179a15419c05/4q3blcmuaL.lottie')
st_lottie