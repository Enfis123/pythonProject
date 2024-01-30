# Created by TOSHIBA at 1/9/2024
#language: es
Característica: Calificar trabajo final de verificiacion
  Como profesor
  Quiero calificar el trabajo final de mis estudiantes estrictamente
  Para aprobar a los estudiantes demuestran el conocimiento de la materia
  Escenario:Profesor califica personalente
    Dado que el alumno ha entregado su trabajo final a tiempo
    Cuando asigno una calificacion sobre 10 basado en una rubrica
    Entonces apruebo al estudiante si la calificación es mayor o igual a 7
    Pero si no cumple esa calificación, repruebo al estudiante
