genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
participants = {'Max'}
owner = 'Max'


def hash_block(block):
    return '-'.join(str([block[key] for key in block]))


def get_balance(participant):
    tx_sender = [[txn['amount'] for txn in block['transactions'] if txn['sender'] == participant] for block in blockchain]
    sent_amount = 0
    for tx in tx_sender:
        if len(tx) > 0:
            sent_amount += tx[0]

    tx_sender = [[txn['amount'] for txn in block['transactions'] if txn['recipient'] == participant] for block in
                 blockchain]
    recieved_amount = 0
    for tx in tx_sender:
        if len(tx) > 0:
            recieved_amount += tx[0]

    return recieved_amount - sent_amount


def get_last_blockchain_value():
    """Returns the last value of current blockchain"""
    if len(blockchain) < 1:
        return None;
    return blockchain[-1]


def add_transaction(recipient, sender = owner, amount = 1.0):
    """

    :type amount: object
    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)
    block = {'previous_hash': hashed_block,
             'index':len(blockchain),
             'transactions':open_transactions}
    blockchain.append(block)
    return True


def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Enter your transaction amount please: '))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input('Your Choice:')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting block')
        print(block)


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


while True:
    print('Please choose:')
    print('1:Add a new transaction value')
    print('2:Mine a new block ')
    print('3:Outputting the blockchain blocks')
    print('4:Display participants')
    print('h:Manipulate the blockchain')
    print('q:Quit')
    user_choice=get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []

    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice=='4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '',
                             'index': 0,
                             'transactions': {'sender': 'Chris', 'recipient': 'Max', 'amount': 20}}
    elif user_choice == 'q':
        break

    else:
        print('Input was invalid, please pick a value from list')

    if not verify_chain():
        print('Invalid blockchain')
        break

    print(get_balance('Max'))
