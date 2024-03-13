from multiprocessing import Process, Pipe
class WarehouseManager(Process):
    def __init__(self, request, conn, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.data = {}
        self.conn = conn

    def process_request(self):
        x = self.request
        if x[1] == 'receipt':
            self.data[x[0]] = x[2]
        if x[1] == 'shipment':
            if self.data[x[0]] >= x[2]:
                self.data[x[0]] -= x[2]
            else:
                self.data[x[0]] = 0
        self.conn.send(self.data)
        self.conn.close()

    def run(self):
        for self.request in requests:
            p = Process(target=self.process_request)
            p.start()
            self.data = parent_conn.recv()
            p.join()



if __name__ == '__main__':
    requests = [("product1", "receipt", 100),
                ("product2", "receipt", 150),
                ("product1", "shipment", 30),
                ("product3", "receipt", 200),
                ("product2", "shipment", 50)]
    parent_conn, child_conn = Pipe()
    manager = WarehouseManager(requests, child_conn)
    data = {}
    manager.run()
    print(manager.data)



















