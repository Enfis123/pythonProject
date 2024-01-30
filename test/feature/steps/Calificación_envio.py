from behave import *

use_step_matcher("re")


@step("que el alumno ha entregado su trabajo final a tiempo")
def step_impl(context):
    #debe existir un alumno
    alumno= Alumno("nombre")
    actividad_final=Actividad("Proyecto Final")
    alumno.entregar_trabajo_final(actividad_final)
    actividad_final.contiene(alumno.trabajo_final)
    #el trabajo esta dentro de la fecha
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que el alumno ha entregado su trabajo final a tiempo')


@step("asigno una calificacion sobre 10 basado en una rubrica")
def step_impl(context):
    #debe existir una rubrica
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando asigno una calificacion sobre 10 basado en una rubrica')


@step("apruebo al estudiante si la calificación es mayor o igual a 7")
def step_impl(context):
    #si el estudiante tiene 7 sobre 10 o mas deber estar aprobado
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces apruebo al estudiante si la calificación es mayor o igual a 7')


@step("si no cumple esa calificación, repruebo al estudiante")
def step_impl(context):
    #si el estudiante tiene menos de 7 sobre 10 se reprueba
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Pero si no cumple esa calificación, repruebo al estudiante')