import time
import hmac
import hashlib
import urllib.parse
import base64
import json


def send_to_dd(msg):
    timestamp = str(round(time.time() * 1000))
    secret = ""
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

    access_token = ""
    url = f"https://oapi.dingtalk.com/robot/send?access_token={access_token}&sign={sign}&timestamp={timestamp}"

    header = {"Content-Type": "application/json", "Charset": "UTF-8"}
    data = {
        "msgtype": "text",
        "text": {"content": msg},
        "at": {"isAtAll": False},
    }
    sendData = json.dumps(data)
    sendData = sendData.encode("utf-8")
    request = urllib.request.Request(url=url, data=sendData, headers=header)
    opener = urllib.request.urlopen(request)
