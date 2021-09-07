
import statistics
from datetime import date

class RepairOrders:
    def __init__(self, client, device, entry_date, error_type, departure_date, repair_cost, completed):
        self.client = client
        self.device = device
        self.entry_date = entry_date
        self.departure_date = departure_date
        self.error_type = error_type
        self.repair_cost = repair_cost
        self.completed = completed


    @staticmethod
    def read_orders(path):                        #lee el archivo pedidos.csv y crea una lista de objetos con los datos
        clients = []
        with open(path) as f:
            for line in f:
                data = line.strip().split(',')
                fields = dict(client=data[0], device=data[1], entry_date=data[2], error_type=data[3], departure_date=data[4], repair_cost=data[5], completed=data[6])
                obj = RepairOrders(**fields)
                clients.append(obj)
            return clients

    def __getitem__(self, key):                  #getter para obtener el nombre de cliente y el coste de la reparación
        if key == 0:
            return self.client
        elif key == 5:
            return self.repair_cost


    def set_update(self, date, cost, status):   #setter para actualizar los datos de fecha de entrega, coste de reparación y el estado
        self.departure_date = date
        self.repair_cost = cost
        self.completed = status

    @staticmethod
    def stats(orders):                         #calcula valores estadísticos de las reparaciones 
        orders = RepairOrders.read_orders('pedidos.csv')
        total_costs = 0
        mean_costs = []
        median_costs = []
        mode_costs = []
        for cost in orders:
            if cost[5] != '-':                  #ignora los objetos que todavía no han sido reparados
                mean_costs.append(float(cost[5]))
                median_costs.append(float(cost[5]))
                mode_costs.append(float(cost[5]))
                total_costs += float(cost[5])
            else:
                continue
        print(f'Los valores estadísticos del total de pedidos son:')
        print(f'coste medio: {statistics.mean(mean_costs):.2f}, mediana el coste: {statistics.median(median_costs):.2f}, moda del coste: {statistics.mode(mode_costs):.2f}. Coste total de las reraciones: {total_costs}€')


    @staticmethod                              #escribe con el formato determinado el archivo pedidos.csv
    def write_orders(orders, path):
        with open(path, 'w',) as f:
            for row in orders:
                print(row, file=f)

    @staticmethod
    def update(orders):                         #método que se encarga de buscar el objeto que queremos actualizar, solicita el dato del coste y actualiza los datos mediante el setter
        update_order = str(input('¿A nombre de quién está el pedido?: '))
        for client in orders:
            if update_order.lower().strip(' ') == client.__getitem__(0).lower():    #elimina posibles espacios en blanco y compara las dos cadenas del atributo client en minúsculas
                date_repair = date.today()
                cost = float(input('Introduzca el coste de la reparación: '))
                status = 'Terminado'
                client.set_update(date_repair, cost, status)
            else:
                continue
            break
        else:
            print('No se ha encontrado el pedido.\n')
        return orders

    def __str__(self):                          #método mágico para escribir con el formato que quiero en el csv
        return f'{self.client},{self.device},{self.entry_date},{self.error_type},{self.departure_date},{self.repair_cost},{self.completed}'
                