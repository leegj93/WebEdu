from decouple import config
from flask import Flask, request, render_template, jsonify
import requests
import random

app=Flask(__name__)


token = config("TOKEN")
api_url = f"https://api.telegram.org/bot{token}"
update_url=f"{api_url}/getUpdates"

google_key=config("GOOGLE_API_KEY")
google_url="https://translation.googleapis.com/language/translate/v2"

# response = requests.get(update_url).json()
# chat_id= response["result"][0]["message"]["chat"]["id"]



#메세지에 로또 번호 6개 뽑아서 보내주기
# message= random.sample(range (1,46),6)
# message_url=f"{api_url}/sendMessage?chat_id={chat_id}&text={message}"

# response = requests.get(message_url).json()

# print(response)

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    message= request.args.get("message")
    message_url=f"{api_url}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(message_url)
    return "메세지 전송 완료"


@app.route(f'/{token}', methods=["POST"])
def telegram():
    message= request.get_json()
    dialog_flow=message["originalDetectIntentRequest"]["payload"]

    print(dialog_flow)
    text = dialog_flow["text"]

    # chat_id=message["message"]["chat"]["id"]
    # text=message["message"]["text"]


    if text == "로또":
        reply= random.sample(range(1, 46), 6)
        
        reply= ' '.join(str(e) for e in reply)
        print(reply)
    elif text[0:3] == "/번역":
        data={
            'q': text[4:],
            'source':'ko',
            'target': 'en'

        }
        response=requests.post(f'{google_url}?key={google_key}',data).json()
        # print(response)
        reply= response["data"]["translations"][0]["translatedText"]

    # else:
    #     reply=text

    # message_url=f"{api_url}/sendMessage?chat_id={chat_id}&text={reply}"
    # requests.get(message_url)
    # return '', 200
    result={'fulfillmentText': reply}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
    