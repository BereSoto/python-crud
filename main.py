import sys

clients = ['Pablo', 'Ricardo']

def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients.append(client_name)
        
    else:
        print('Client already is in the client\'s list')

def list_clients():
    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client))

def update_client(client_name, update_client_name):
    global clients

    if clients in clients:
        index = clients.index(client_name)
        clients[index] = update_client_name
    else:
        print('client is not in client list')

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Clients is not in clients list')

def search_client(client_name):
    
    for client in clients:
        if client != client_name:
            continue
        else: 
            return True


def _get_client_name():
    client_name = None

    while not client_name:
        client_name =  input('what is the client name?')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _print_welcome():
    print('welcome to platzi ventas')
    print('*' * 50)
    print('what would you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()

    elif command == 'L':
        list_clients()
        
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input ( 'whats is the update client name')
        update_client(client_name, update_client_name)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('the client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid commad')
    