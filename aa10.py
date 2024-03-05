import queue
import time
import threading
class Table:
    def __init__(self, id):
        self.id = id
        self.is_busy = False
class Cafe:
    def __init__(self, queue, tables):
        self.queue = queue
        self.tables = tables
    def customer_arrival(self):
        for cust in range(1, 9):
            print(f'Посетитель номер {cust} прибыл')
            self.serve_customer(cust)
            time.sleep(1)

    def serve_customer(self, cust):
        flag = False
        for table in self.tables:
            if table.is_busy == False:
                custom = Customer(cust, self, table)
                table.is_busy = True
                custom.start()
                flag = True
                break
        if flag == False:
            print(f'Посетитель номер {cust} ожидает свободный стол.')
            self.queue.put(cust)
class Customer(threading.Thread):
    def __init__(self, id, cafe, table, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.cafe = cafe
        self.table = table

    def run(self):
        self.table.is_busy = True
        print(f'Посетитель номер {self.id} сел за стол {self.table.id}')
        time.sleep(5)
        print(f'Посетитель номер {self.id} покушал и и ушел')
        self.table.is_busy = False
        if self.cafe.queue.qsize() > 0:
            self.cafe.serve_customer(self.cafe.queue.get())

tables = [Table(i) for i in range(1,4)]
queue = queue.Queue()
cafe = Cafe(queue, tables)
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()

