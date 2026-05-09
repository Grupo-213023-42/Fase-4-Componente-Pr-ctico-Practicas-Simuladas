from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError
class Servicio(ABC):
    def _init_(self, nombre: str, descripcion_base: str):
        self.nombre = nombre
        self.descripcion_base = descripcion_base
    @abstractmethod
    def calcular_costo(self, duracion: float, impuesto: float = 0.19, descuento: float = 0.0, **kwargs) -> float:
        pass
    @abstractmethod
    def describir(self) -> str:
        pass
    @abstractmethod
    def validar_parametros(self, duracion: float) -> bool:
        pass
    def _str_(self):
        return self.nombre
class ReservaSala(Servicio):
    def _init_(self):
        super()._init_("Reserva de Sala", "Sala de reuniones equipada con proyector y wifi")
    def calcular_costo(self, duracion: float, impuesto: float = 0.19, descuento: float = 0.0, **kwargs) -> float:
        if not self.validar_parametros(duracion):
            raise ValueError("Duración inválida para sala")
        base = 50000 * duracion
        return round(base * (1 + impuesto) - (base * descuento), 2)
    def describir(self) -> str:
        return f"{self.descripcion_base} - Tarifa por hora: $50.000 COP"
    def validar_parametros(self, duracion: float) -> bool:
        return 0.5 <= duracion <= 24
class AlquilerEquipo(Servicio):
    def _init_(self):
        super()._init_("Alquiler de Equipo", "Equipos de cómputo y audiovisuales")
    def calcular_costo(self, duracion: float, impuesto: float = 0.19, descuento: float = 0.0, **kwargs) -> float:
        if not self.validar_parametros(duracion):
            raise ValueError("Duración inválida para alquiler")
        dias = duracion / 24
        base = 200000 * dias
        return round(base * (1 + impuesto) - (base * descuento), 2)
    def describir(self) -> str:
        return f"{self.descripcion_base} - Tarifa por día: $200.000 COP"
    def validar_parametros(self, duracion: float) -> bool:
        return duracion >= 4
class AsesoriaEspecializada(Servicio):
    def _init_(self):
        super()._init_("Asesoría Especializada", "Consultoría técnica personalizada")
    def calcular_costo(self, duracion: float, impuesto: float = 0.19, descuento: float = 0.0, **kwargs) -> float:
        if not self.validar_parametros(duracion):
            raise ValueError("Duración inválida para asesoría")
        base = 80000 * duracion + 150000
        return round(base * (1 + impuesto) - (base * descuento), 2)
    def describir(self) -> str:
        return f"{self.descripcion_base} - Tarifa por hora + cargo fijo"
    def validar_parametros(self, duracion: float) -> bool:
        return 0.5 <= duracion <= 8
