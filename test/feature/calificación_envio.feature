# Created by TOSHIBA at 1/9/2024
#language: es
Característica: Calificar trabajo final de verificiacion
  Como profesor
  Quiero calificar el trabajo final de mis estudiantes estrictamente
  Para aprobar a los estudiantes demuestran el conocimiento de la materia

  Esquema del escenario: :Profesor califica personalente
    Dado que un alumno ha entregado su trabajo final <tipo_entrega>
    Cuando asigno una calificación de <nota_trabajo> sobre <nota_maxima> basado en una
    Entonces el estudiante obtendrá <estado_alumno> de acuerdo a la nota de aprobación
    Ejemplos:
      | tipo_entrega | nota_maxima | nota_trabajo | estado_alumno
      | a tiempo     | 10          | 7            | Aprobado
      | con retraso  | 8           | 7            | Aprobado
      | adelantado   | 10          | 6            | Aprobado
      | con permiso  | 10          | 6            | Aprobado