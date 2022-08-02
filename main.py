from flask import Flask,redirect,request,render_template
import requests

app = Flask(__name__)

def bypass(url):
  payload = {
    "url": url,
  }

  r = requests.post("https://api.bypass.vip/", data=payload)
  return r.json()


@app.route('/',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        id = request.form['URL']
        link = id
        bson = bypass(link)
        blink = bson['destination']
        return redirect(blink)
    else:
        return render_template("index.html")


@app.route('/<int:number>/<name>/<int:count>')
def bp(number,name,count):
    link = f"https://linkvertise.com/{number}/{name}/{count}"
    bson = bypass(link)
    blink = bson['destination']
    return redirect(blink)

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=80)
