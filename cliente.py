import re
import logging
from excepciones import DatosInvalidosError
from abc import ABC, abstractmethod

class Entidad(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Cliente(Entidad):
    def __init__(self, nombre: str, email: str, telefono: str):
        self._nombre = nombre
        self.email = email
        self.telefono = telefono
        logging.info(f"Cliente registrado: {self}")

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", valor):
            raise DatosInvalidosError("Email inválido", "EMAIL_001")
        self._email = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):
        if not valor.isdigit() or len(valor) < 7:
            raise DatosInvalidosError("Teléfono inválido (mínimo 7 dígitos)", "TEL_002")
        self._telefono = valor

    def __str__(self):
        return f"Cliente: {self.nombre} | Email: {self.email} | Tel: {self.telefono}"
