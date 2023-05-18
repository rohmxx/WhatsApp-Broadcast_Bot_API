messages = """this
messages
can
be
entered"""

your_contacts = {
    "name1": "number1",
    "name2": "number2",
}

import requests
import json

for name, number in your_contacts.items():
    url = "https://api.whatspie.com/messages"
    contact = "{}{}".format("62", number)
    payload = json.dumps({
      "device": "yournumber",
      "receiver": contact,
      "type": "chat",
      "message": messages,
      "simulate_typing": 1
    })
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ******'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
