import requests

r = requests.get('https://pilares.cdmx.gob.mx/')

print(r.text)