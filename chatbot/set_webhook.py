from decouple import config

import requests

token=config("TOKEN")
api_url = f"https://api.telegram.org/bot{token}"

set_webhook_url=f"{api_url}/setWebhook?url=https://leegj93.pythonanywhere.com/929907754:AAHPa5k-tn2PU6I4P2JiJAhFwhgLH4epKsk"

response= requests.get(set_webhook_url)
print(response.text)