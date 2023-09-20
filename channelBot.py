import requests
import json
from config import TOKEN
# from utils.utils_api import tx

TOKEN = "6538289312:AAHLHWTIlwqJ8CpeyX8XFW4rIZge9tgbem4"
chat_id = "-1001841995638"
data = {
    "amount": 100
}

# Mock tx info
# api_url = "http://si8a1.asuscomm.com:8000/mock/"

# Real-Time tx info
api_url = "http://si8a1.asuscomm.com:8000/filter_amount/"
res = requests.post(api_url, json=data)

if res.status_code == 200:
    transaction_data = res.json()
    
    tx_id = transaction_data["tx_id"]
    block_id = transaction_data["block_id"]
    sender_address = transaction_data["sender_address"]
    receiver_address = transaction_data["receiver_address"]
    transaction_type = transaction_data["type"]
    amount = transaction_data["amount"]
    confirm_time = transaction_data["confirm_time"]
    
    notification = f"""
    **Large Transaction Alert**
    > Notification: A large transaction has been detected! 🚨
    > 
    > **Sender's Address**: *{sender_address}*
    > 
    > **Recipient's Address**: *{recipient_address}*
    > 
    > **Transaction Amount**: *{amount}* TON
    > 
    > **Transaction Time**: *{confirm_time}*
    > 
    > Please take note of this transaction for security and transparency.
    """
    
    message = {
            'chat_id': chat_id,
            'text': notification,
            'parse_mode': 'MarkdownV2'
        }
    
    # Send the message to the Telegram channel
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    response = requests.post(url, json=message)
        
    if response.status_code == 200:
            print('Message successfully sent to the Telegram channel!')
    else:
            print('Message sending failed. Status code:', response.status_code)
            print('Error message:', response.text)
else:
    print('API request failed. Status code:', res.status_code)



# def send_tx_announcement(tx:[tx]):
#     pass
    # address_queue = []
    # for amount in tx:
    #     if amount["amount"] > 100:
    #         #Previous Pause here
    #         pass





# requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=-1001841995638&text={notification}')



# def get_block_height():
#     paylaod = {"query": "{wcBlocks: blocks(workchain: 0, page_size: 1) { seqno }}"}
#     r = requests.post('https://dton.io/graphql/',data = paylaod )
#     data = json.loads(r.text)
#     blockheight = data['data']['wcBlocks'][0]['seqno']
#     return blockheight

# print(get_block_height())