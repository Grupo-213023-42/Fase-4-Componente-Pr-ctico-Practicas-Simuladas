import logging
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import DatosInvalidosError, ServicioNoDisponibleError, ReservaInvalidaError

logging.basicConfig(
    filename='eventos.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def simular_operaciones():
    print("🚀 Iniciando Sistema Integral Software FJ - Estructura Modular\n")
    clientes = []
    reservas = []

    # 1. Cliente válido
    try:
        c1 = Cliente("Alejandro Ruiz", "alejandro@ejemplo.com", "3101234567")
        clientes.append(c1)
        print("✅ Cliente 1 registrado")
    except Exception as e:
        print("❌", e)

    # 2. Cliente inválido (email)
    try:
        Cliente("María López", "maria_ejemplo_com", "3209876543")
    except DatosInvalidosError as e:
        print("✅ Excepción controlada (email):", e)

    # 3. Cliente inválido (teléfono)
    try:
        Cliente("Carlos Pérez", "carlos@ejemplo.com", "123")
    except DatosInvalidosError as e:
        print("✅ Excepción controlada (teléfono):", e)

    # 4. Crear servicios
    sala = ReservaSala()
    equipo = AlquilerEquipo()
    asesoria = AsesoriaEspecializada()
    print("✅ Servicios creados:", [s.nombre for s in [sala, equipo, asesoria]])

    # 5. Reserva exitosa
    try:
        r1 = Reserva(c1, sala, 3.0)
        r1.confirmar()
        reservas.append(r1)
        print("✅", r1)
    except Exception as e:
        print("❌", e)

    # 6. Reserva inválida (duración)
    try:
        r2 = Reserva(c1, sala, 30.0)
        r2.confirmar()
    except Exception as e:
        print("✅ Excepción controlada (duración):", e)

    # 7. Cálculo sobrecargado (impuesto y descuento)
    try:
        costo = asesoria.calcular_costo(2.0, impuesto=0.10, descuento=0.15)
        print(f"✅ Costo personalizado: ${costo}")
    except Exception as e:
        print("❌", e)

    # 8. Cancelación
    try:
        r1.cancelar()
        print("✅ Reserva cancelada")
    except Exception as e:
        print("❌", e)

    # 9. Servicio no disponible
    try:
        raise ServicioNoDisponibleError("Equipo temporalmente no disponible", "SERV_005")
    except ServicioNoDisponibleError as e:
        print("✅ Excepción controlada (servicio):", e)

    # 10. Try/Except/Else/Finally + encadenamiento de excepciones
    try:
        1 / 0
    except ZeroDivisionError as e:
        try:
            raise ReservaInvalidaError("Error durante procesamiento") from e
        except ReservaInvalidaError as inner:
            print("✅ Excepción encadenada capturada:", inner)
            print("   Causa:", inner.__cause__)
    finally:
        print("✅ Finally: sistema sigue estable")

    print("\n📊 RESUMEN: Sistema estable con manejo de excepciones")
    print(f"Clientes: {len(clientes)} | Reservas: {len(reservas)}")
    print("📁 Revisa eventos.log")

if __name__ == "__main__":
    simular_operaciones()
