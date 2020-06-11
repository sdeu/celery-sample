import requests
import os
from .worker import app

STORAGE_HOST = os.getenv('STORAGE_HOST')
STORAGE_PORT = os.getenv('STORAGE_PORT')

@app.task(name="render")
def render():
    url = f'http://{STORAGE_HOST}:{STORAGE_PORT}/{render.request.id}'
    x = requests.post(url, files=dict(file=render.request.id))
    return render.request.id

@app.task(name="combine")
def combine(files):
    data = []
    for f in files:
        url = f'http://{STORAGE_HOST}:{STORAGE_PORT}/{f}'
        r = requests.get(url)
        content = r.content
        data.append(str(content))
    
    url = f'http://{STORAGE_HOST}:{STORAGE_PORT}/combined_{combine.request.id}'
    x = requests.post(url, files=dict(file=os.linesep.join(data)))
