from flask import Flask,redirect
import requests

app = Flask(__name__)

def bypass(url):
  payload = {"url": url,}
  r = requests.post("https://api.bypass.vip/", data=payload)
  return r.json()

@app.route('/')
def main():
    return 'hello world'

@app.route('/<int:number>/<name>/<int:count>')
def bp(number,name,count):
    link = f"https://linkvertise.com/{number}/{name}/{count}"
    bson = bypass(link)
    blink = bson['destination']
    return redirect(blink)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
    #app.run(host="0.0.0.0", port=443,ssl_context=('certificate', 'key')) HTTPS
