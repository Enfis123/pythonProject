from behave import *
from modelos.modelos import *

use_step_matcher("re")


@step("que el alumno ha entregado su trabajo final a tiempo")
def step_impl(context):
    # Debe existir un alumno
    context.alumno = Alumno("nombre")
    context.actividad_final = Actividad("Proyecto Final")
    # El alumno debe tener un trabajo final
    context.alumno.entregar_trabajo_final(context.actividad_final)
    # Verifica si el alumno entregó a tiempo
    assert context.actividad_final.esta_entregado_a_tiempo_el_trabajo(
        context.alumno.trabajo_final), "El trabajo no fue entregado a tiempo"


@step("asigno una calificacion sobre 10 basado en una rubrica")
def step_impl(context):
    # Debe existir una rubrica
    context.rubrica = Rubrica()
    # Debe existir un profesor
    context.profesor = Profesor("Carlos")
    # Debe existir un Alumno
    context.alumno = Alumno("Alumno")
    # Debe existir un trabajo final de un alumno
    context.actividad_final = context.alumno.trabajo_final
    # Agregar criterios a la rúbrica
    context.rubrica.agregar_criterio("Creatividad", 5)
    context.rubrica.agregar_criterio("Complejidad", 3)
    context.rubrica.agregar_criterio("Presentación", 1)
    # Calificar un proyecto utilizando la rúbrica
    assert context.profesor.calificar_actividad_final(context.alumno, context.actividad_final, context.rubrica)


@step("apruebo al estudiante si la calificación es mayor o igual a 7")
def step_impl(context):
    # Debe existir un profesor
    context.profesor = Profesor("Carlos")
    # Debe existir un alumno
    context.alumno = Alumno("Alumno")
    context.alumno.asignar_calificacion(8)
    # si el estudiante tiene 7 sobre 10 o mas deber estar aprobado
    assert context.profesor.verificar_puntos_totales_Aprobar(context.alumno)
    pass

@step("si no cumple esa calificación, repruebo al estudiante")
def step_impl(context):
    # Debe existir un profesor
    context.profesor = Profesor("Carlos")
    # Debe existir un alumno
    context.alumno = Alumno("Alumno")
    context.alumno.asignar_calificacion(5)
    # si el estudiante tiene 7 sobre 10 o mas deber estar aprobado
    assert context.profesor.verificar_puntos_totales_Reprueba(context.alumno)

