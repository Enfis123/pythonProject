class Alumno:
    def __init__(self, nombre):
        self.trabajo_final = None
        self.nombre = nombre
        self.tarea = True
        self.calificacion = None  # Agregamos un atributo para almacenar la calificación
        self.apruebaMateria

    def entregar_trabajo_final(self, actividad_final):
        self.trabajo_final = actividad_final
        return True

    def asignar_calificacion(self, calificacion):
        self.calificacion = calificacion

    def apruebaMateria(self):
        self.apruebaMateria = True

    def repruebaMateria(self):
        self.apruebaMateria = False


class Actividad:
    def __init__(self, actividad_final):
        self.actividad_final = actividad_final

    def esta_entregado_a_tiempo_el_trabajo(self, trabajo_final):
        return True


class Rubrica:
    def __init__(self):
        self.criterios = {}  # Diccionario para almacenar los criterios de evaluación

    def agregar_criterio(self, nombre, peso):
        """Agrega un criterio a la rúbrica con un peso específico."""
        self.criterios[nombre] = peso

    def ponderar_actividad_final(self, actividad_final):
        puntosCalificados = sum(self.criterios.values())

        calificacion_ponderada = puntosCalificados
        return calificacion_ponderada


class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

    def calificar_actividad_final(self, alumno, actividad_final, rubrica):
        # Calificar el proyecto utilizando la rúbrica
        calificacion = rubrica.ponderar_actividad_final(actividad_final)

        # Asignar la calificación al atributo de la clase Alumno
        alumno.asignar_calificacion(calificacion)
        return True

    def verificar_puntos_totales_Aprobar(self, alumno):
        if alumno.calificacion >= 7:
            alumno.apruebaMateria()
            return True

    def verificar_puntos_totales_Reprueba(self, alumno):
        if alumno.calificacion < 7:
            alumno.repruebaMateria()
            return True
