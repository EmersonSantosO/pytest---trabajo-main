import pytest
from src.main import ingresardatos, clientes, idcliente
import builtins


def setup_function():
    global clientes, idcliente
    clientes = {}
    idcliente = 0


def simular_input(monkeypatch, inputs):
    input_iter = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda _: next(input_iter))


def verificar_cliente(
    cliente,
    id_cliente,
    run,
    nombre,
    apellido,
    direccion,
    fono,
    correo,
    tipo,
    monto,
    deuda=0,
):
    assert cliente[0] == id_cliente  # ID del cliente
    assert cliente[1] == run
    assert cliente[2] == nombre
    assert cliente[3] == apellido
    assert cliente[4] == direccion
    assert cliente[5] == fono
    assert cliente[6] == correo
    assert cliente[7] == tipo
    assert cliente[8] == monto
    assert cliente[9] == deuda


def test_crear_cliente(monkeypatch):
    setup_function()
    # Datos de prueba
    datos_predefinidos = [
        "12345678-9",  # run
        "Juan",  # nombre
        "Perez",  # apellido
        "Calle Falsa 123",  # direccion
        "987654321",  # fono
        "juan.perez@example.com",  # correo
        "101",  # tipo
        "10000",  # monto
    ]

    # Simular inputs del usuario
    simular_input(monkeypatch, datos_predefinidos)

    # Ejecutar la función
    ingresardatos()

    # Verificaciones
    assert 1 in clientes, "El cliente no se ha agregado al diccionario."
    cliente = clientes[1]
    verificar_cliente(cliente, 1, *datos_predefinidos)


def test_crear_clientes_multiple(monkeypatch):
    setup_function()
    # Datos de prueba para el primer cliente
    datos_predefinidos1 = [
        "12345678-9",
        "Juan",
        "Perez",
        "Calle Falsa 123",
        "987654321",
        "juan.perez@example.com",
        "101",
        "10000",
    ]

    # Datos de prueba para el segundo cliente
    datos_predefinidos2 = [
        "98765432-1",
        "Maria",
        "Gomez",
        "Avenida Siempreviva 742",
        "123456789",
        "maria.gomez@example.com",
        "102",
        "20000",
    ]

    # Simular inputs del usuario para el primer cliente
    simular_input(monkeypatch, datos_predefinidos1)
    ingresardatos()

    # Simular inputs del usuario para el segundo cliente
    simular_input(monkeypatch, datos_predefinidos2)
    ingresardatos()

    # Verificar que ambos clientes se hayan agregado al diccionario
    assert 1 in clientes, "El primer cliente no se ha agregado al diccionario."
    assert 2 in clientes, "El segundo cliente no se ha agregado al diccionario."

    # Verificar el primer cliente
    cliente1 = clientes[1]
    verificar_cliente(cliente1, 1, *datos_predefinidos1)

    # Verificar el segundo cliente
    cliente2 = clientes[2]
    verificar_cliente(cliente2, 2, *datos_predefinidos2)


@pytest.mark.parametrize(
    "cliente_invalid_datos",
    [
        [
            "",
            "Juan",
            "Perez",
            "Calle Falsa 123",
            "987654321",
            "juan.perez@example.com",
            "101",
            "10000",
        ],
        [
            "12345678-9",
            "",
            "Perez",
            "Calle Falsa 123",
            "987654321",
            "juan.perez@example.com",
            "101",
            "10000",
        ],
        [
            "12345678-9",
            "Juan",
            "",
            "Calle Falsa 123",
            "987654321",
            "juan.perez@example.com",
            "101",
            "10000",
        ],
        [
            "12345678-9",
            "Juan",
            "Perez",
            "",
            "987654321",
            "juan.perez@example.com",
            "101",
            "10000",
        ],
        [
            "12345678-9",
            "Juan",
            "Perez",
            "Calle Falsa 123",
            "",
            "juan.perez@example.com",
            "101",
            "10000",
        ],
        [
            "12345678-9",
            "Juan",
            "Perez",
            "Calle Falsa 123",
            "987654321",
            "",
            "101",
            "10000",
        ],
        [
            "12345678-9",
            "Juan",
            "Perez",
            "Calle Falsa 123",
            "987654321",
            "juan.perez@example.com",
            "",
            "10000",
        ],
        [
            "12345678-9",
            "Juan",
            "Perez",
            "Calle Falsa 123",
            "987654321",
            "juan.perez@example.com",
            "101",
            "",
        ],
    ],
)
def test_crear_cliente_invalid_data(monkeypatch, cliente_invalid_datos):
    setup_function()
    # Simular inputs del usuario
    simular_input(monkeypatch, cliente_invalid_datos)
    ingresardatos()

    # Verificar que no se ha agregado ningún cliente al diccionario
    assert len(clientes) == 0, "No se debería agregar un cliente con datos inválidos."
