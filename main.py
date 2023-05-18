import random

def generar_historia():
    personajes = ["un astronauta", "un pirata", "un mago", "un robot", "una princesa"]
    lugares = ["en un castillo encantado", "en una isla tropical", "en el espacio sideral", "en un bosque mágico", "en una ciudad futurista"]
    eventos = ["descubrió un tesoro oculto", "luchó contra monstruos gigantes", "realizó un hechizo poderoso", "construyó una máquina del tiempo", "organizó una fiesta épica"]
    acciones = ["saltó de alegría", "cantó una canción divertida", "bailó descontroladamente", "se rió a carcajadas", "hizo una mueca graciosa"]
    desenlaces = ["y vivieron felices para siempre", "y se convirtió en leyenda", "y aprendieron una valiosa lección", "y celebraron con una gran fiesta", "y prometieron nunca olvidar esta aventura"]
    
    personaje = random.choice(personajes)
    lugar = random.choice(lugares)
    evento = random.choice(eventos)
    accion = random.choice(acciones)
    desenlace = random.choice(desenlaces)
    
    historia = f"Había una vez {personaje} que vivía {lugar}. Un día, {personaje} {evento}. Después, {personaje} {accion}. Finalmente, {desenlace}."
    return historia

historias_divertidas = []
cantidad_historias = 1

for _ in range(cantidad_historias):
    historia = generar_historia()
    historias_divertidas.append(historia)

for historia in historias_divertidas:
    print(historia)
