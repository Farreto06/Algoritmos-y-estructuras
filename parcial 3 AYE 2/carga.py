import datetime as dt
from clases import *
import json

def cargar_datos_desde_json(nombre_archivo):
    proyectos = []
    with open(nombre_archivo, "r") as archivo:
        datos = json.load(archivo)
        for proyecto_data in datos["proyectos"]:
            proyecto = Proyecto(
                proyecto_data["identificador"],
                proyecto_data["titulo"],
                proyecto_data["detalles"],
                dt.datetime.strptime(proyecto_data["inicio"], "%Y-%m-%d"),
                dt.datetime.strptime(proyecto_data["vencimiento"], "%Y-%m-%d"),
                proyecto_data["condicion"],
                proyecto_data["organizacion"],
                proyecto_data["responsable"],
                proyecto_data["grupo"]
            )
            for tarea_data in proyecto_data["tareas"]:
                tarea = Tarea(
                    tarea_data["identificador"],
                    tarea_data["titulo"],
                    tarea_data["cliente"],
                    tarea_data["detalles"],
                    dt.datetime.strptime(tarea_data["inicio"], "%Y-%m-%d"),
                    dt.datetime.strptime(tarea_data["vencimiento"], "%Y-%m-%d"),
                    tarea_data["condicion"],
                    tarea_data["avance"]
                )
                for subtarea_data in tarea_data.get("subtareas", []):
                    subtarea = Subtarea(
                        subtarea_data["identificador"],
                        subtarea_data["titulo"],
                        subtarea_data["detalles"],
                        subtarea_data["condicion"]
                    )
                    tarea.agregar_subtarea(subtarea)
                proyecto.agregar_tarea(tarea)
            proyectos.append(proyecto)
    return proyectos