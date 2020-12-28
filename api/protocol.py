import random, string, requests, json

from base64 import b64encode
from hashlib import sha256
from urllib.parse import urlencode

URL = json.load(open('./link/link.json', 'r')) # ./link/link.json

def get_app_check():
    return requests.get(URL["auth"]["app_check"]).json()

def get_client_token():
    randomString = string.ascii_letters
    result = ""

    for i in range(11):
        result += random.choice(randomString)

    result += ":APA91bFMI-0d1b0wJmlIWoDPVa_V5Nv0OWnAefN7fGLegy6D76TN_CRo5RSUO-6V7Wnq44t7Rzx0A4kICVZ7wX-hJd3mrczE5NnLud722k5c-XRjIxYGVM9yZBScqE3oh4xbJOe2AvDe"

    return result

def get_app_id(token):
    app_key = f"dcArdchk_{get_app_check()[0]['date']}"
    app_key = sha256(app_key.encode("ascii")).hexdigest()

    data = {
        "value_token": app_key,
        "signature": "ReOo4u96nnv8Njd7707KpYiIVYQ3FlcKHDJE046Pg6s=",
        "client_token": token
    }

    return session.post(URL["auth"]["app_id"], data=data).json()[0][
        "app_id"]

def redirect(url):
    hash = b64encode(bytes(url.encode("utf8")))
    url = "http://m.dcinside.com/api/redirect.php?hash={}".format(hash.decode("utf8"))
    return url

def get(api, body):
    params = "{}?{}".format(api, urlencode(body))
    return session.get(redirect(params))

def post(api, body):
    return session.post(api, body)

session = requests.session()
session.headers = {
    "User-Agent": "dcinside.app",
    "Referer": "http://m.dcinside.com",
    "Content-Type": "application/x-www-form-urlencoded"
}

token = get_client_token()
app_id = get_app_id(token)
