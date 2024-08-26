import simpy

class InventorySystem:
    def __init__(self, env):
        self.env = env
        self.inventory = 10  # Inicialmente, hay 10 productos en el inventario
        self.out_of_stock_event = env.event()  # Evento de agotamiento de productos

    def generate_products(self, rate):
        while True:
            # Generar un producto cada 5 minutos
            yield self.env.timeout(5/rate)
            self.inventory += 1
            print(f"{self.env.now}: Generado un producto. Total en inventario: {self.inventory}")

    def check_out_of_stock(self):
        while True:
            # Verificar si el inventario se ha agotado cada minuto
            yield self.env.timeout(1)
            if self.inventory == 0:
                self.out_of_stock_event.succeed()  # Activar el evento de agotamiento de productos
                print(f"{self.env.now}: El producto se ha agotado.")
                exit()

    def process_orders(self, rate):
        while True:
            # Procesar un pedido cada 3 minutos
            yield self.env.timeout(3/rate)
            if self.inventory > 0:
                self.inventory -= 1
                print(f"{self.env.now}: Procesado un pedido. Total en inventario: {self.inventory}")
            else:
                print(f"{self.env.now}: No hay productos disponibles.")

    def run(self, rate):
        self.env.process(self.generate_products(rate))
        self.env.process(self.check_out_of_stock())
        self.env.process(self.process_orders(rate))
        self.env.run()

env = simpy.Environment()
inventory_system = InventorySystem(env)
inventory_system.run(1)  # Tasa de generación de productos por minuto
