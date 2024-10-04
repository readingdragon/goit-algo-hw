from queue import Queue
import random

# Створити чергу заявок
queue4requsts = Queue()

def generate_request():
    print(f'One more request has arrived!')
    if not hasattr(generate_request, 'request_number'):
        generate_request.request_number = 1
    new_request = f"request_{generate_request.request_number}"# Створити нову заявку
    generate_request.request_number += 1
    queue4requsts.put(new_request) # Додати заявку до черги

def process_request():
    print(f'Queue requests: {queue4requsts.queue}')
    if not queue4requsts.empty():
        print(f"Handling request: {queue4requsts.queue[0]}") # Обробити заявку
        queue4requsts.get() # Видалити заявку з черги
    else:
        print('Congrats! The work is done, all requests are handled! You can go home now)') # Вивести повідомлення, що черга пуста

# Головний цикл програми:
def service_center_at_work():
    i = 1
    while i < 10:
        # Виконати generate_request() для створення нових заявок 
        # Виконати process_request() для обробки заявок
        random.choice([generate_request, process_request])()
        i += 1
    print(f'Requests for tomorrow: {queue4requsts.queue}')
    
service_center_at_work()
