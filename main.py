from telethon.sync import TelegramClient
import platform


def inRange(number, a, b):
    return a <= number <= b


print(f"Running on {platform.system()}")
print("Authorization...")
api_id = 000000
api_hash = ''
client = TelegramClient('Telegram Purge', api_id, api_hash)
client.start()

print("Your chats: ")


def printChatList():
    chats_count = 0
    entities = []
    for dialog in client.iter_dialogs():
        chats_count += 1
        entities.append(dialog.entity)
        print(f'{chats_count})', dialog.name)
        # print(client.get_messages(entity=dialog.entity, limit=1).total)

    if chats_count == 0:
        print("You don't have any chats.")
        exit(0)

    # print(newline, '0) Delete all messages from all chats.')

    while True:
        selected = input('--> ')
        if selected.isnumeric() and inRange(int(selected), a=1, b=chats_count):
            return entities[int(selected) - 1]


def deleteMyMessages(entity):
    messages_ids = []
    for message in client.iter_messages(entity=entity, from_user=client.get_me().id, limit=2_147_483_648):
        print(message)
        messages_ids.append(message.id)
    client.delete_messages(entity=entity, message_ids=messages_ids, revoke=True)


selected_entity = printChatList()

print("Общее количество сообщений: ", client.get_messages(entity=selected_entity, limit=1).total)
deleteMyMessages(selected_entity)
