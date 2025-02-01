class GestionClientes:
    def __init__(self, cliente_repository: ClienteRepository):
        self.cliente_repository = cliente_repository

    def crear_cliente(self, cliente: Cliente):
        self.cliente_repository.guardar_cliente(cliente)

    def modificar_cliente(self, cliente: Cliente):
        self.cliente_repository.guardar_cliente(cliente)

    def eliminar_cliente(self, id: int):
        # Implementación para eliminar un cliente
        pass