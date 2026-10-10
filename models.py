import os
import random
from datetime import datetime


class Persona:
    contador_id = 1

    def __init__(self, nombre, apellidos, fecha_nacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.id = Persona.contador_id
        Persona.contador_id += 1
        self.puntuacionTotal = 0

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getFecha_nacimiento(self):
        return self.fecha_nacimiento

    def getId(self):
        return self.id

    def getEdad(self):
        hoy = datetime.now().date()
        anios = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            anios -= 1
        return anios

class Villanos(Persona):
    def __init__(self, nombre, apellidos, fecha_nacimiento):
        super().__init__(nombre,apellidos, fecha_nacimiento)
        self.chagepeteador = random.randint(1,100)
        self.entregadorTardio = random.randint(1,100)
        self.ausencias = random.randint(1,100)
        self.hablador = random.randint(1,100)

    def getChagepeteador(self):
        return self.chagepeteador
    def getEntregadorTardio(self):
        return self.entregadorTardio
    def getAusencias(self):
        return self.ausencias
    def getHablador(self):
        return self.hablador

    def definirPuntuacionTotalVillano(self):
        puntuacionTotalVillano = (self.chagepeteador + self.entregadorTardio + self.ausencias + self.hablador) / 4
        return puntuacionTotalVillano

class Heroes(Persona):
    def __init__(self, nombre, apellidos, fecha_nacimiento):
        super().__init__(nombre, apellidos, fecha_nacimiento)
        self.codigoLimpio = random.randint(1,100)
        self.bienDocumentado = random.randint(1,100)
        self.gitGOD = random.randint(1,100)
        self.arquitecto = random.randint(1,100)
        self.detallista = random.randint(1,100)

    def getCodigoLimpio(self):
        return self.codigoLimpio
    def getBienDocumentado(self):
        return self.bienDocumentado
    def getGitGOD(self):
        return self.gitGOD
    def getArquitecto(self):
        return self.arquitecto
    def getDetallista(self):
        return self.detallista

    def definirPuntuacionTotalHeroe(self):
        puntuacionTotalHeroe = (self.codigoLimpio + self.bienDocumentado + self.gitGOD + self.arquitecto + self.detallista) / 5
        return puntuacionTotalHeroe

