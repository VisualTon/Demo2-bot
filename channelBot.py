import requests
import json
from config import TOKEN
#  from utils.utils_api import tx


#Database realtime tx alert

sender_address = "Sender's address here"
recipient_address = "Recipient's address here"
transaction_amount = "Transaction amount here"
transaction_time = "Transaction time here"

notification = f"""
**Large Transaction Alert**
> Notification: A large transaction has been detected! 🚨
> 
> **Sender's Address**: *{sender_address}*
> 
> **Recipient's Address**: *{recipient_address}*
> 
> **Transaction Amount**: *{transaction_amount}* TON
> 
> **Transaction Time**: *{transaction_time}*
> 
> Please take note of this transaction for security and transparency.
"""


def send_tx_announcement(tx:[tx]):
    pass
    # address_queue = []
    # for amount in tx:
    #     if amount["amount"] > 100:
    #         #Previous Pause here
    #         pass





requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=-1001841995638&text={notification}')







# def get_block_height():
#     paylaod = {"query": "{wcBlocks: blocks(workchain: 0, page_size: 1) { seqno }}"}
#     r = requests.post('https://dton.io/graphql/',data = paylaod )
#     data = json.loads(r.text)
#     blockheight = data['data']['wcBlocks'][0]['seqno']
#     return blockheight

# print(get_block_height())

