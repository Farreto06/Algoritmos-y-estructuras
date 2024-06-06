import datetime as dt
import message

#Definicion de las clases
class Proyecto:
    def __init__(self,identificador=int,titulo=str,detalles=str,inicio=dt.datetime,vencimiento=dt.datetime,condicion=str,organizacion=str,responsable=str,grupo=[],tareas=[]):
        self.identificador=identificador
        self.titulo=titulo
        self.detalles=detalles
        self.inicio=inicio
        self.vencimiento=vencimiento
        self.condicion=condicion
        self.organizacion=organizacion
        self.responsable=responsable
        self.grupo=grupo
        self.tareas=tareas
        self.cant_subtarea_p=0

    def agregar_tarea(self,tarea):
        self.tareas.append(tarea)

    def get_cant_subtarea_p(self):
        return self.cant_subtarea_p

class Tarea:
    def __init__(self,identificador=int,titulo=str,cliente=str,detalles=str,inicio=dt.datetime,vencimiento=dt.datetime,condicion=str,avance=int,subtarea=[]):
        self.identificador = identificador
        self.titulo=titulo
        self.cliente=cliente
        self.detalles=detalles
        self.inicio=inicio
        self.vencimiento=vencimiento
        self.condicion=condicion
        self.avance=avance
        self.sub_tareas=subtarea
        self.cant_subtarea=len(self.sub_tareas)

    def agregar_subtarea(self,subtareas):
        self.sub_tareas.append(subtareas)

    def get_vencimiento(self):
        return self.vencimiento
    
    def get_avacnce(self):
        return self.avance
        
class Subtarea:
    def __init__(self,identificador=int,titulo=str,detalles=str,condicion=str):
        self.identificador=identificador
        self.titulo=titulo
        self.detalles=detalles
        self.condicion=condicion

class Reporte:
    def __init__(self,proyectos: list[Proyecto]):
        self.proyectos=proyectos

    def interfaz(self):
        while True:
            i=int(input(message.menu))
            if i==1:
                Reporte.a_find_tarea_estado_espcifico(self)
            elif i==2:
                Reporte.b_find_proyecto_nombre(self)
            elif i==3:
                pass
            elif i==4:
                Reporte.d_sort_proyectos_cant(self)
            elif i==5:
                pass
            elif i==6:
                pass
            elif i==7:
                break
        
        print(message.end)
        
    def a_find_tarea_estado_espcifico(self):
        #Pedir estado
        est=input("Introduce el estado de las tareas a consultar: ")
        tarea_select=[]
        tarea_sort=[]

        for proyecto in self.proyectos:
            for tarea in proyecto.tareas:
                if tarea.condicion==est:
                    tarea_select.append(tarea)
        tarea_sort=Reporte.quicksort_tareas(tarea_select)

        for i in tarea_sort:
            print(Tarea.get_avacnce(i))


    @staticmethod
    def quicksort_tareas(tareas):
        if len(tareas) <= 1:
            return tareas
        else:
            pivote = tareas[-1]
            mayores = [tarea for tarea in tareas[:-1] if tarea.avance >= pivote.avance]
            menores = [tarea for tarea in tareas[:-1] if tarea.avance < pivote.avance]
            return Reporte.quicksort_tareas(mayores) + [pivote] + Reporte.quicksort_tareas(menores)

    def d_sort_proyectos_cant(self):
        num = 0
        for proyecto in self.proyectos:
            x = proyecto
            num = 0
            for tarea in x.tareas:
                if len(tarea.sub_tareas) <=0 :
                    pass
                else:
                    print("Chequeando")
                    num += 1
                    print(num)
                proyecto.cant_subtarea_p=num
            

        lista_ordenada=[]
        lista_ordenada=Reporte.merge_sort_d(self.proyectos)

        for i in lista_ordenada:
            print(Proyecto.get_cant_subtarea_p(i))

    @staticmethod
    def merge_sort_d(lista):
        if len(lista) <= 1:
            return lista

        # Dividir la lista en dos mitades
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        # Ordenar cada mitad recursivamente
        izquierda = Reporte.merge_sort_d(izquierda)
        derecha = Reporte.merge_sort_d(derecha)

        # Combinar las dos mitades ordenadas
        return Reporte.merge_d(izquierda, derecha)

    @staticmethod
    def merge_d(izquierda, derecha):
        resultado = []
        i = j = 0

        # Combinar las dos listas ordenadas en una sola lista ordenada
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i].cant_subtarea_p <= derecha[j].cant_subtarea_p:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        # Agregar los elementos restantes de la lista izquierda
        while i < len(izquierda):
            resultado.append(izquierda[i])
            i += 1

        # Agregar los elementos restantes de la lista derecha
        while j < len(derecha):
            resultado.append(derecha[j])
            j += 1

        return resultado
    
    def b_find_proyecto_nombre(self):
        select_proyect=[]
        lista_ordenada=[]
        p=input("Introduzca la palabara a contener el titulo del proyetco: ")

        for proyecto in self.proyectos:
            if p in proyecto.titulo:
                select_proyect.append(proyecto)

        lista_ordenada=Reporte.merge_sort_b(select_proyect)
        for i in lista_ordenada:
            print(i.inicio)

    @staticmethod
    def merge_sort_b(lista):
        if len(lista) <= 1:
            return lista

        # Dividir la lista en dos mitades
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        # Ordenar cada mitad recursivamente
        izquierda = Reporte.merge_sort_b(izquierda)
        derecha = Reporte.merge_sort_b(derecha)

        # Combinar las dos mitades ordenadas
        return Reporte.merge_b(izquierda, derecha)

    @staticmethod
    def merge_b(izquierda, derecha):
        resultado = []
        i = j = 0

        # Combinar las dos listas ordenadas en una sola lista ordenada
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i].inicio <= derecha[j].inicio:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        # Agregar los elementos restantes de la lista izquierda
        while i < len(izquierda):
            resultado.append(izquierda[i])
            i += 1

        # Agregar los elementos restantes de la lista derecha
        while j < len(derecha):
            resultado.append(derecha[j])
            j += 1

        return resultado

    def c(self):#Ejercicio c
        id=int(input("Introduzca identificador del proyecto a revisar: "))
        for proyecto in self.proyectos:
            if proyecto.identificador==id:
                pass