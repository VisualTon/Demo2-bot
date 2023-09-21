import requests
import json
from config import TOKEN
from datetime import datetime
import time
# from utils.utils_api import tx

TOKEN = "6538289312:AAHLHWTIlwqJ8CpeyX8XFW4rIZge9tgbem4"
chat_id = "-1001841995638"
sent_transactions_file = "sent_transactions.txt"

try:
    with open(sent_transactions_file, "r") as file:
        sent_transactions = file.read().splitlines()
except FileNotFoundError:
    sent_transactions = []


# Mock tx info
# api_url = "http://si8a1.asuscomm.com:8000/mock/"
# res = requests.get(api_url)

# if res.status_code == 200:
#     transaction_data = res.json()
#     notifications = []

#     for transaction in transaction_data:
#         tx_id = transaction["tx_id"]
#         sender_address = transaction["sender_address"]
#         receiver_address = transaction["receiver_address"]
#         transaction_type = transaction["type"]
#         amount = transaction["amount"]
#         confirm_time = datetime.utcfromtimestamp(transaction["confirm_time"]).strftime('%Y-%m-%d %H:%M:%S')
        
#         if tx_id not in sent_transactions:
#             notification = f"""
#             🚨 *LARGE TRANSACTION ALERT* 🚨

# *Sender's Address*: {sender_address}
# *Recipient's Address*: {receiver_address}
# *Transaction Amount*: {amount} TON
# *Transaction Time*: {confirm_time} UTC

# ⚠️ Please take note of this transaction for security and transparency ⚠️
#             """
#             notifications.append(notification)
    
#     for notification in notifications:
#         message = {
#                 'chat_id': chat_id,
#                 'text': notification,
#                 'parse_mode': 'Markdown'
#             }    
            
#         # Send the message to the Telegram channel
#         url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
#         response = requests.post(url, json=message)
                
#         if response.status_code == 200:
#                 print('Message successfully sent to the Telegram channel!')
#         else:
#                 print('Message sending failed. Status code:', response.status_code)
#                 print('Error message:', response.text)

# elif res.status_code == 429:
#         retry_after = int(res.headers.get('Retry-After', 60))
#         print(f"Rate limited. Waiting for {retry_after} seconds before retrying...")
#         time.sleep(retry_after)

# else:
#     print('API request failed. Status code:', res.status_code)


# Real-Time tx info
while True:
    api_url = "http://si8a1.asuscomm.com:8000/filteredNodes/?amount=10000"
    res = requests.get(api_url)

    if res.status_code == 200:
        transaction_data = res.json()
        notifications = []

        for transaction in transaction_data:
            tx_id = transaction["Transaction_id"]
            # block_id = transaction["Block_id"]
            sender_address = transaction["Sender_address"]
            receiver_address = transaction["Receiver_address"]
            transaction_type = transaction["Type"]
            amount = transaction["Amount"]
            confirm_time = datetime.utcfromtimestamp(transaction["Confirm_time"]).strftime('%Y-%m-%d %H:%M:%S')
            
            if tx_id not in sent_transactions:
                notification = f"""
                🚨 *LARGE TRANSACTION ALERT* 🚨

*Sender's Address*: {sender_address}
*Recipient's Address*: {receiver_address}
*Transaction Amount*: {amount} TON
*Transaction Time*: {confirm_time} UTC

⚠️ Please take note of this transaction for security and transparency ⚠️
                """
                notifications.append(notification)
                sent_transactions.append(tx_id)
        
        for notification in notifications:
            message = {
                    'chat_id': chat_id,
                    'text': notification,
                    'parse_mode': 'Markdown'
                }    
                
            # Send the message to the Telegram channel
            url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
            response = requests.post(url, json=message)
                    
            if response.status_code == 200:
                    print('Message successfully sent to the Telegram channel!')
            else:
                    print('Message sending failed. Status code:', response.status_code)
                    print('Error message:', response.text)

    elif res.status_code == 429:
        retry_after = int(res.headers.get('Retry-After', 60))
        print(f"Rate limited. Waiting for {retry_after} seconds before retrying...")
        time.sleep(retry_after)

    else:
        print('API request failed. Status code:', res.status_code)

    with open(sent_transactions_file, "w") as file:
        file.write("\n".join(sent_transactions))

    time.sleep(60)



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