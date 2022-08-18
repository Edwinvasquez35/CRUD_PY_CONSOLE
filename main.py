import csv

import os

CLIENT_TABLE = 'clients.csv'

CLIENT_SCHEMA = ['name', 'company', 'email', 'position']

clients = []

def _initialize_clients_from_storange():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames= CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
	tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
	with open(tmp_table_name, mode='w') as f:
		writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
		writer.writerows(clients)

		os.remove(CLIENT_TABLE)
	os.rename(tmp_table_name, CLIENT_TABLE)

def create_client(client_name):
    global clients

    if client_name not in clients: # operador de pertenencia
        clients.append(client_name)
    else:
        print('Client already is in the client\'s list')

def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))

def update_client(client_id, update_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = update_client
    else:
        print('Client not in client\'s list')

def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break

    

def search_client(client_name):
    
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('what is the client {}? '.format(field_name))
    
    return field

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client

def _print_welcome():
    print("WELCOME TO PLATZI VENTAS")
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')


if __name__ == '__main__':
    _initialize_clients_from_storange()

    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()

        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))

        delete_client(client_id)
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')

    _save_clients_to_storage()

