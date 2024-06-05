import datetime as dt
from metodos import *
import message

#Definicion de las clases
class Proyecto:
    def __init__(self,id=int,nom=str,desc=str,f_ini=dt.datetime,f_fin=dt.datetime,estado=str,empresa=str,gerente=str,equipo=[]):
        self.id=id
        self.nom=nom
        self.desc=desc
        self.f_ini=f_ini
        self.f_fin=f_fin
        self.estado=estado
        self.empresa=empresa
        self.gerente=gerente
        self.equipo=equipo
        self.tareas= []

    def agregar_tarea(self,tarea):
        self.tareas.append(tarea)

class Tarea:
    def __init__(self,id=int,nom=str,empresa_cliente=str,descripcion=str,f_ini=dt.datetime,f_fin=dt.datetime,estado=str,porcentaje=int):
        self.id=id
        self.nom=nom
        self.empresa_cliente=empresa_cliente
        self.descripcion=descripcion
        self.f_ini=f_ini
        self.f_fin=f_fin
        self.estado=estado
        self.procetanje=porcentaje
        self.sub_tareas=[]

    def agregar_subtarea(self,subtareas):
        self.sub_tareas.append(subtareas)

    def get_f_fin(self):
        return self.f_fin
        
class Subtarea:
    def __init__(self,id=int,nom=str,descripcion=str,estado=str):
        self.id=id
        self.nom=nom
        self.descripcion=descripcion
        self.estado=estado

class Reporte:
    def __init__(self,proyectos: list[Proyecto]):
        self.proyectos=proyectos

    def interfaz(self):
        while True:
            i=int(input(message.menu))
            if i==1:
                Reporte.find_tareas_rango_quicksort(self)
            elif i==2:
                Reporte.sort_proyectos_empresa_mergesort(self)
            elif i==3:
                Reporte.sort_proyectos_progreso_heapsort(self)
            elif i==4:
                Reporte.sort_proyecto_equipo_shellsort(self)
            elif i==5:
                Reporte.sort_tareas_proyecto_hashing(self)
            elif i==6:
                Reporte.sort_proyectos_duracion_heapsort(self)
            elif i==7:
                break
        
        print(message.end)
        
    def find_tareas_rango_quicksort(self):
        #Pedir rango de fechas
        f_min=dt.datetime.strptime(input("Introduzca la fecha minima A-M-D: "),"%Y-%m-%d")
        f_max=dt.datetime.strptime(input("Introduzca la fecha maxima A-M-D: "),"%Y-%m-%d")

        select_tarea=[]
        for proyecto in self.proyectos:
            for tarea in proyecto.tareas:
                if f_min <= tarea.f_ini <= f_max:
                    select_tarea.append(tarea)
   
        Reporte.quicksort(select_tarea,0,len(select_tarea)-1)
        for i in select_tarea:
            print(Tarea.get_f_fin(i))

    @staticmethod
    def partition(arr, low, high):
        pivot = arr[low].f_fin
        left = low + 1
        right = high

        done = False
        while not done:
            while left <= right and arr[left].f_fin <= pivot:
                left = left + 1
            while arr[right].f_fin >= pivot and right >= left:
                right = right - 1
            if right < left:
                done = True
            else:
                arr[left], arr[right] = arr[right], arr[left]

        arr[low], arr[right] = arr[right], arr[low]

        return right

    @staticmethod
    def quicksort(arr, low, high):
        if low < high:
            pi = Reporte.partition(arr, low, high)
            Reporte.quicksort(arr, low, pi - 1)
            Reporte.quicksort(arr, pi + 1, high)

    def sort_proyectos_empresa_mergesort(self):
        pass

    def sort_proyectos_progreso_heapsort(self):
        pass

    def sort_proyecto_equipo_shellsort(self):
        pass

    def sort_tareas_proyecto_hashing(self):
        pass

    def sort_proyectos_duracion_heapsort(self):
        pass