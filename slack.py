import requests
import json

with open("./slack_webhook_url.txt")as f:
    SLACK_WEBHOOK_URL = f.read()

def send_message(message):
    data_dic = json.dumps({"text":message})
    requests.post(SLACK_WEBHOOK_URL, headers={'content-type':'application/json'}, data=data_dic)

def send_error_log(message):
    send_message(":no_entry_sign:" + message)

if __name__ == "__main__":
    send_message("test")