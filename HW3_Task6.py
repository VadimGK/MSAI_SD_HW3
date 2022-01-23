DB = {
    'user1':
        {
            'login': 'qwe',
            'chats': ['ch1', 'ch2'],
            'messages': ['yes', 'no', 'tank']
        },
    'user2':
        {
            'login': 'asd',
            'chats': ['ch1', 'ch3'],
            'messages': ['yes', 'good', 'T-34']
        },
}

# Solution:

def add(user, chat):
        DB[user]['chats'].append(chat)
        print(f'{user} added in {chat}')

add('user2', 'chat2')
user2 added in chat2

# Find
def find(words):
    temp = []
    for user, dbi  in DB.items():
        for message in dbi['messages']:
            if words in message:
                temp.append(message)
    print(temp)

find('yes')
['yes', 'yes']

def shared_chats(*args):
    r = set(DB[args[0]]['chats'])
    for user in args[1:]:
        r = r.intersection(DB[user]['chats'])
    print(r)

shared_chats('user1', 'user2')
{'ch1'}
