from telethon.sync import TelegramClient
import platform


def in_range(number, a, b):
    return a <= number <= b


print(f"Running on {platform.system()}")
print("Authorization...")

# Configure it with your data
api_id = 123456
api_hash = "1234567890abcdefghijklmnopqrstuv"
client = TelegramClient("Telegram Purge", api_id, api_hash)

client.start()
user_id = client.get_me().id


def main():
    print("Your chats: ")
    chats_count = 0
    entities = []
    for dialog in client.iter_dialogs():
        chats_count += 1
        entities.append(dialog.entity)
        print(f'{chats_count})', dialog.name)

    if chats_count == 0:
        print("You don't have any chats.")
        exit(0)

    print()
    print('D) Delete all messages from all chats.')
    print('0) Exit.')
    print()

    while True:
        selected = input('--> ').lower()
        if selected.isnumeric() and in_range(int(selected), a=1, b=chats_count):
            print("[Question]: Do you really want to delete all your messages in this chat?'")
            confirm_input = input("[Confirm? (Yes / No)]: ")
            if confirm_input.lower() == "yes":
                delete_my_messages([entities[int(selected) - 1]])
            break
        elif selected == 'd':
            print("[Warning]: !!!THIS WILL DELETE ALL YOUR MESSAGES IN ALL CHATS!!!")
            confirm_input = input("[Confirm? (Yes / No)]: ")
            if confirm_input.lower() == "yes":
                delete_my_messages(entities)
            break
        elif selected == '0':
            print("Bye. Have a nice day/night.")
            exit(0)

    main()


def delete_my_messages(entities):
    entities_length = len(entities)
    for index, entity in enumerate(entities, start=1):
        if entities_length > 1:
            print(f"[Chat №{index}]")

        print("[Info]: Total number of all messages in this chat: ", client.get_messages(entity=entity, limit=1).total)
        print("[Deleting]")

        messages_ids = []
        for message in client.iter_messages(entity=entity, from_user=user_id):
            print(message)
            messages_ids.append(message.id)
        client.delete_messages(entity=entity, message_ids=messages_ids, revoke=True)


main()
