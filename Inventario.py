from datetime import date
from claseInventario import RepairOrders


if __name__ == '__main__':
    path = 'pedidos.csv'
    orders_list = []
    modif_orders = []


    salir = False
    option = 0
    while not salir:                                        #Menu de opciones
        orders_list = RepairOrders.read_orders(path)
        print('1.- Añadir un nuevo pedido.')
        print('2.- Modificar un pedido.')
        print('3.- Ver estadísticas de los pedidos.')
        print('4.- Salir.')
        option = int(input('Elije una opción: '))

        if option == 1:                                     #coge por teclado los datos necesarios, crea un nuevo objeto, lee el csv y guarda el nuevo pedido al final del csv
            name = str(input('Introduce el nombre del cliente: '))
            device = str(input('Introduce el dispositivo: '))
            entry_date = date.today()
            error_type = str(input('Descipción del error: '))
            new_order = RepairOrders(name.strip(' '), device, entry_date, error_type,'-', '-', 'En proceso')
            orders_list.append(new_order)
            RepairOrders.write_orders(orders_list, path)

        elif option == 2:                                   #crea una lista modificada donde guarda los objetos modificados y luego manda esa lista a write.orders para guardarla en el csv
            modif_orders = RepairOrders.update(orders_list)
            RepairOrders.write_orders(modif_orders, path)

        elif option == 3:                                   #llama a stats para calcular los datos estadísticos de los pedidos.
            RepairOrders.stats(orders_list)

        elif option == 4:                                   #finaliza el programa
            salir = True
        else:
            print('Introduce un numero entre 1 y 3.\n')