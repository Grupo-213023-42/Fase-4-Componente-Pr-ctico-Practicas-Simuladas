import logging
from cliente import Cliente
from servicio import Servicio
from excepciones import ReservaInvalidaError

class Reserva:
    def __init__(self, cliente: Cliente, servicio: Servicio, duracion: float):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"
        self.costo = 0.0
        logging.info(f"Reserva creada (pendiente): {cliente.nombre} - {servicio.nombre}")

    def confirmar(self):
        try:
            if self.estado != "pendiente":
                raise ReservaInvalidaError("La reserva ya fue procesada", "RES_003")
            self.servicio.validar_parametros(self.duracion)
            self.costo = self.servicio.calcular_costo(self.duracion)
            self.estado = "confirmada"
            logging.info(f"Reserva CONFIRMADA - Costo: ${self.costo}")
        except Exception as e:
            logging.error(f"Error al confirmar reserva: {e}")
            raise

    def cancelar(self):
        if self.estado == "confirmada":
            self.estado = "cancelada"
            logging.info("Reserva CANCELADA")
        else:
            raise ReservaInvalidaError("Solo se pueden cancelar reservas confirmadas", "RES_004")

    def __str__(self):
        return f"Reserva {self.estado.upper()} | Cliente: {self.cliente.nombre} | Servicio: {self.servicio} | Duración: {self.duracion}h | Costo: ${self.costo}"
