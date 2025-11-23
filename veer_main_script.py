import requests
import json
import socket
import sys
import os 
from time import sleep

# --- [1] आपकी Telegram Bot की जानकारी यहाँ अपडेट करें ---
# 🚨 आपको BotFather से मिला हुआ "नया" Bot Token यहाँ पेस्ट करना है 🚨
BOT_TOKEN = "8299002678:AAFbGuQFSNg4fhjEISV66TKTMXHu-TQHPEw"  
CHAT_ID = "6795520561"                     # आपकी Chat ID
SCRIPT_OWNER = "VEER CHOUDHARY"            # आपका नाम
# --------------------------------------------------------

def send_telegram_message(message):
    """टेलीग्राम पर मैसेज भेजने का फंक्शन"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload, timeout=5)
    except:
        pass

def get_device_info():
    """डिवाइस और यूजर की जानकारी इकठ्ठा करना"""
    info = {}
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        info['Local_IP'] = s.getsockname()[0]
        s.close()
    except:
        info['Local_IP'] = 'N/A'

    info['User'] = os.environ.get('USER', 'Unknown User')
    info['Shell'] = os.environ.get('SHELL', 'N/A')
    info['OS'] = sys.platform
    
    return info

def check_approval():
    """अप्रूवल स्टेटस चेक करने का फंक्शन और मैसेज भेजना"""
    device_info = get_device_info()
    
    # यह मैसेज आपके Telegram पर जाएगा
    approval_message = (
        f"🚨 *NEW DEVICE ACCESS REQUEST* 🚨\n\n"
        f"Tool Name: Veer Fire Tool\n"
        f"Owner: {SCRIPT_OWNER}\n\n"
        f"Device Info:\n"
        f"  IP: `{device_info['Local_IP']}`\n"
        f"  User: `{device_info['User']}`\n"
        f"  OS: {device_info['OS']}\n\n"
        f"➡️ Tool has been locked for this device."
    )
    
    send_telegram_message(approval_message)
    
    sleep(3) 

    # यह मैसेज Termux चलाने वाले यूजर को दिखेगा
    print("\n--- ⚠️ ACCESS PENDING ⚠️ ---")
    print(f"Tool is locked. Approval request sent to {SCRIPT_OWNER}'s Telegram.")
    print("Please wait for owner's confirmation.")
    
    sys.exit(0)

# --- मुख्य फंक्शन ---
def start_veer_tool():
    # यह लाइनें Termux में आपका नाम डिस्प्ले करेंगी
    print(f"\n=========================================")
    print(f"       🔥 Welcome to {SCRIPT_OWNER}'s Tool 🔥")
    print(f"=========================================\n")
    
    check_approval() 
    
if __name__ == "__main__":
    start_veer_tool()
  
