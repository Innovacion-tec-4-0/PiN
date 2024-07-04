import random
import time
from datetime import datetime


class Dispositivo:
    # Clase base para los dispositivos.
    def __init__(self, id_dispositivo):
        self.id_dispositivo = id_dispositivo

    def leer_datos(self):
        pass

    def enviar_datos(self):
        pass

    def recibir_datos(self):
        pass


class PiN(Dispositivo):
    # Clase para el dispositivo PiN que incluye varios sensores.
    def __init__(self, id_dispositivo, nombre_mascota):
        super().__init__(id_dispositivo)
        self.nombre_mascota = nombre_mascota
        self.sensores = {
            'gps': None,
            'ritmo_cardiaco': None,
            'acelerometro': None,
            'temperatura_por_infrarrojo': None,
            'proximidad': None
        }

    def leer_datos(self):
        for sensor in self.sensores.values():
            if sensor:
                sensor.leer_datos()

    def enviar_datos(self):
        for sensor in self.sensores.values():
            if sensor:
                sensor.enviar_datos()


class SensorGPS(Dispositivo):
    # Clase para el sensor GPS.
    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.ubicacion = {}

    def leer_datos(self):
        self.ubicacion = self.leer_gps()
        print(f"Ubicación GPS leída: {self.ubicacion}")

    def enviar_datos(self):
        print(f"Enviando datos de ubicación GPS: {self.ubicacion}")

    def leer_gps(self):
        return {
            'latitud': random.uniform(-90, 90),
            'longitud': random.uniform(-180, 180)
        }


class SensorRitmoCardiaco(Dispositivo):
    # Clase para el sensor de ritmo cardíaco.
    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.frecuencia_cardiaca = None

    def leer_datos(self):
        self.frecuencia_cardiaca = self.leer_ritmo_cardiaco()
        print(f"Frecuencia cardíaca leída: {self.frecuencia_cardiaca} BPM")

    def enviar_datos(self):
        print(f"Enviando datos de frecuencia cardíaca: {
              self.frecuencia_cardiaca} BPM")

    def leer_ritmo_cardiaco(self):
        return random.randint(60, 140)


class SensorAcelerometro(Dispositivo):
    # Clase para el sensor de acelerómetro.
    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.aceleracion = {}

    def leer_datos(self):
        self.aceleracion = self.leer_acelerometro()
        print(f"Datos de aceleración leídos: {self.aceleracion}")

    def enviar_datos(self):
        print(f"Enviando datos de aceleración: {self.aceleracion}")

    def leer_acelerometro(self):
        return {
            'x': random.uniform(-2, 2),
            'y': random.uniform(-2, 2),
            'z': random.uniform(-2, 2)
        }


class SensorTemperaturaInfrarrojo(Dispositivo):
    # Clase para el sensor de temperatura por infrarrojo.
    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.temperatura = None

    def leer_datos(self):
        self.temperatura = self.leer_temperatura_por_infrarrojo()
        print(f"Temperatura por infrarrojo leída: {self.temperatura} °C")

    def enviar_datos(self):
        print(f"Enviando datos de temperatura por infrarrojo: {
              self.temperatura} °C")

    def leer_temperatura_por_infrarrojo(self):
        return random.uniform(35.0, 40.0)


class SensorProximidad(Dispositivo):
    # Clase para el sensor de proximidad.
    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.proximidad = None

    def leer_datos(self):
        self.proximidad = self.leer_proximidad()
        print(f"Proximidad leída: {self.proximidad} m")
        if self.proximidad > 2:  # Umbral de proximidad para aviso
            print("Alerta: ¡Un objeto está demasiado cerca!")

    def enviar_datos(self):
        print(f"Enviando datos de proximidad: {self.proximidad} m")

    def leer_proximidad(self):
        return random.uniform(0, 5)


class RedIoT:
    # Clase para la red IoT que gestiona múltiples dispositivos.
    def __init__(self):
        self.dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def leer_todos_los_datos(self):
        for dispositivo in self.dispositivos:
            dispositivo.leer_datos()

    def enviar_todos_los_datos(self):
        for dispositivo in self.dispositivos:
            dispositivo.enviar_datos()


# Ejemplo de uso
if __name__ == "__main__":
    # Solicitar nombre de la mascota
    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    print("------------------------------------------------")
    print(f'Hola {nombre_mascota}, aquí tienes todos tus datos monitoreados.')
    print("------------------------------------------------")

    # Crear una red IoT
    red_iot = RedIoT()

    # Crear dispositivo PiN y sensores
    pin = PiN(id_dispositivo=1, nombre_mascota=nombre_mascota)
    pin.sensores['gps'] = SensorGPS(id_dispositivo=2)
    pin.sensores['ritmo_cardiaco'] = SensorRitmoCardiaco(id_dispositivo=3)
    pin.sensores['acelerometro'] = SensorAcelerometro(id_dispositivo=4)
    pin.sensores['temperatura_por_infrarrojo'] = SensorTemperaturaInfrarrojo(
        id_dispositivo=5)
    pin.sensores['proximidad'] = SensorProximidad(id_dispositivo=6)

    # Agregar dispositivos a la red IoT
    red_iot.agregar_dispositivo(pin)
    red_iot.agregar_dispositivo(pin.sensores['gps'])
    red_iot.agregar_dispositivo(pin.sensores['ritmo_cardiaco'])
    red_iot.agregar_dispositivo(pin.sensores['acelerometro'])
    red_iot.agregar_dispositivo(pin.sensores['temperatura_por_infrarrojo'])
    red_iot.agregar_dispositivo(pin.sensores['proximidad'])

    # Leer y enviar todos los datos
    red_iot.leer_todos_los_datos()
    red_iot.enviar_todos_los_datos()

    # Simulación adicional para leer todos los sensores en intervalos regulares
    iteraciones = 0
    while True:
        tiempo_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            ritmo_cardiaco_dato = pin.sensores['ritmo_cardiaco'].leer_ritmo_cardiaco(
            )
            aceleracion_dato = pin.sensores['acelerometro'].leer_acelerometro()
            ubicacion_gps_dato = pin.sensores['gps'].leer_gps()
            temperatura_por_infrarrojo_dato = pin.sensores['temperatura_por_infrarrojo'].leer_temperatura_por_infrarrojo(
            )
            proximidad_dato = pin.sensores['proximidad'].leer_proximidad()

            print("------------------------------------------------")
            print(f"Fecha y Hora: {tiempo_actual}")
            print(f"Ritmo cardíaco: {ritmo_cardiaco_dato} BPM")
            print(f"Acelerómetro X={aceleracion_dato['x']:.2f}, Y={
                  aceleracion_dato['y']:.2f}, Z={aceleracion_dato['z']:.2f}")
            print(f"Ubicación GPS Latitud={ubicacion_gps_dato['latitud']:.5f}, Longitud={
                  ubicacion_gps_dato['longitud']:.5f}")
            print(f"Temperatura por infrarrojo: {
                  temperatura_por_infrarrojo_dato:.2f} °C")
            print(f"Proximidad: {proximidad_dato:.2f} m")

            time.sleep(5)
            iteraciones += 1

            if iteraciones == 3:
                continuar = input("¿Desea continuar? (s/n): ")
                if continuar.lower() != 's':
                    break
        except Exception as e:
            print(f"Error: {e}")
            break
