from telethon import TelegramClient, events
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import InviteHashExpiredError, InviteHashInvalidError
import re
import asyncio
from config import api_id, api_hash, phone_number

# Initialize Telegram Client
client = TelegramClient('bot_session', api_id, api_hash)

# Function to join group using invite link
async def join_group(link):
    try:
        if 'joinchat' in link or '+' in link:
            # Private invite link
            invite_hash = link.split('/')[-1]
            print(f"Using invite hash: {invite_hash}")
            await client(ImportChatInviteRequest(invite_hash))
            print(f"Successfully joined group: {link}")
        else:
            # Public invite link
            await JoinChannel(client, link.split('/')[-1])
            print(f"Successfully joined group: {link}")
    except InviteHashExpiredError:
        print(f"Error while joining group: The invite link {link} has expired.")
    except InviteHashInvalidError:
        print(f"Error while joining group: The invite link {link} is not valid.")
    except Exception as e:
        print(f"Error while joining group: {e}")

# Event handler for new messages
@client.on(events.NewMessage)
async def handler(event):
    message = event.message.message
    # Regex pattern to match both public and private Telegram invite links
    match = re.findall(r'https:\/\/t\.me\/(?:joinchat\/|[A-Za-z0-9_-]{5,50})', message)
    if match:
        for link in match:
            print(f"Detected join link: {link}")
            try:
                await join_group(link)
            except Exception as e:
                print(f"Error while joining group: {e}")

def JoinChannel(client, channel):
    # Your implementation here
    pass

# Start the client and listen for messages
async def main():
    async with TelegramClient(phone_number, api_id, api_hash) as client:
        print("Client created. Connecting to Telegram...")
        await client.start()
        print("Connected to Telegram!")
        print("Bot is now listening for Telegram group join links...")
        await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())