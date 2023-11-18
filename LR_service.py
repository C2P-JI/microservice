import csv
import rpyc
'''
    log nutritional data
    retrieve nutritional data
        see what was previously ate

'''
class LRservice(rpyc.Service):
    def on_connect(self, conn):
        print("Client connected")
    
    def on_disconnect(self, conn):
        print("Client disconnected")

    def exposed_log(self, name, servings, log):
        items = [name, servings, log[0], log[1], log[2], log[3], log[4], log[5], log[6]]
        with open("food_log.csv", 'a', newline='') as csv_file:
            csv_write = csv.writer(csv_file)
            csv_write.writerow(items)

    def exposed_get_logged(self):
        pass

    def exposed_total_nutrition(slef):
        pass
        


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(LRservice, port=18866)
    server.start()