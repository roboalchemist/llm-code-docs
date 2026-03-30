# Source: https://docs.enate.net/enate-help/espanol/apendice/comportamiento-del-sistema-para-determinar-la-persona-asignada-el-propietario-y-la-lista-de-tareas.md

# Comportamiento del sistema para determinar la Persona asignada, el Propietario y la Lista de tareas

Como parte de la gestión de Tickets, Casos y Acciones en sus flujos de trabajo en Enate, el sistema evaluará regularmente a quién se asigna la tarea, quién se establece como Propietario, y a qué Lista está enlazada la tarea. Hay un conjunto detallado de reglas que se siguen, en orden, al determinar esto. Antes de ver este conjunto detallado de reglas, es importante entender el patrón de nivel superior que se sigue para evaluar estas asignaciones de tareas, y de hecho, para saber cuándo se evalúan. Funciona de la siguiente manera:&#x20;

* En primer lugar, [determinamos CUÁNDO ocurren tales revaluaciones:](#determinar-cuando-ocurren-las-revaluaciones) fundamentalmente esto ocurre cuando algo cambia en la tarjeta de "Estado" de una tarea.
* Cuando el sistema determina que es necesario hacer una evaluación de este tipo, inicialmente utilizamos el estado o la situación de la tarea para [determinar cuáles de los valores de la Persona asignada, el Propietario y la Lista necesitan Establecerse, y cuáles necesitan Borrarse](#determinar-si-los-valores-de-la-persona-asignada-el-propietario-y-la-lista-deben-establecerse-o-borr) completamente.
* [Para aquellos que necesitan establecerse:](#como-establecer-la-persona-asignada-el-propietario-y-la-lista)
  * a. Si hay que establecer una Lista, es sencillo: solo hay que seleccionar la Lista a la que se hace referencia en la regla de asignación (solo hay dos tipos de regla de asignación de Lista que se puede seguir).
  * b. En el caso de la Persona asignada y el Propietario, hay más detalles: tenemos que repasar una serie de reglas para estos — detenerse cuando la regla se cumple y se selecciona un objetivo válido\*.

[\*Verificación de validez](#verificacion-de-validez) - Como parte de la verificación de la regla de asignación de personas asignadas/propietarios, tenemos que determinar si el objetivo es válido (hay una serie de reglas de verificación de validez que debe aprobar). Si no lo es, continuamos con las reglas de la parte 3 hasta encontrar un objetivo válido.

Ahora que se ha descrito el patrón de nivel superior en juego, podemos ir a ver cada conjunto de reglas que se ejecutan para las secciones 1 a 3 anteriores, y para las verificaciones de validez del objetivo.

## Determinar CUÁNDO ocurren las revaluaciones

El sistema revaluará el usuario asignado, el propietario y la lista siempre que la información en la tarjeta de Estado cambia, específicamente cuando:

* cambia el Estado;
* cambia el tipo de Espera;
* cambia la Fecha de seguimiento programado;
* cambia la fecha de Esperar más información;
* cambia la opción Esperando (solo para los Casos);
* cambia el Contexto del Ticket;
* cambia la Categoría del Ticket;
* cambia el estado de Revisión por compañeros;
* se recibe Nueva información sobre la tarea;
* un Caso se enfrenta a un problema.

## Determinar si los valores de la Persona asignada, el Propietario y la Lista deben establecerse o borrarse

Cuando el sistema determina que necesita hacer una evaluación de este tipo, inicialmente utilizamos el ESTADO de la tarea para determinar qué valores de la Persona asignada, el Propietario y la Lista necesitan Establecerse, y cuáles necesitan Borrarse completamente. Puede ver esta información en la siguiente tabla:

| Estado/Situación de la tarea                        | Persona asignada | Propietario      | Lista            |
| --------------------------------------------------- | ---------------- | ---------------- | ---------------- |
| Cerrado                                             | Borrar valor     | Borrar valor     | Borrar valor     |
| Borrador                                            | Establecer valor | Borrar valor     | Borrar valor     |
| Nueva información recibida                          | Establecer valor | Borrar valor     | Establecer valor |
| Necesita atención (solo relevante para un Caso)     | Establecer valor | Borrar valor     | Establecer valor |
| Por hacer o En progreso para una Acción o un Ticket | Establecer valor | Borrar valor     | Establecer valor |
| Por hacer o En progreso para un Caso                | Borrar valor     | Establecer valor | Borrar valor     |
| Resuelto o Esperando                                | Borrar valor     | Establecer valor | Borrar valor     |

## Cómo establecer la Persona asignada, el Propietario y la Lista

* **Listas:** Si hay que establecer una Lista, es muy sencillo hacerlo. Se ejecuta el [Método de Asignación de Lista](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours#setting-a-queue-method) configurado.&#x20;
* **Persona asignada y Propietario:** Si hay que establecer una Persona asignada o Propietario,  se deben tener en cuenta más detalles. Tenemos que repasar una serie de reglas, en orden, y detenernos cuando se cumpla la regla y se seleccione un [objetivo válido.](#verificacion-de-validez)&#x20;

Antes de ejecutar la lista de reglas, hay una verificación más: si actualmente hay establecida una Persona asignada o un Propietario, **no cambie la Persona asignada o el Propietario a menos que haya cambiado la Categoría del Ticket.**

De lo contrario, ejecute las siguientes reglas, en orden, y deténgase cuando identifique un objetivo válido:

1. Si en una tarea se ha establecido la opción "Mantener conmigo", la Persona asignada/el Propietario se establece como el usuario que ha seleccionado "Mantener conmigo". Si no es así o si el usuario resultante no es válido, entonces
2. Si el usuario Propietario no está en blanco, entonces establezca ese valor a la Persona asignada también. Si no es así o el usuario resultante no es válido, entonces,
3. Si la tarea es un Ticket y la Categoría del Ticket ha cambiado y el Tipo de espera ha cambiado o el estado es Resuelto, entonces la Persona asignada/Propietario se establece como el usuario que está actualizando actualmente el Ticket. Si no,
4. Si la tarea no es un Ticket O es un Ticket (en el que la Categoría del Ticket no ha cambiado Y tenemos más de 2 filas de historial de estado, es decir, no se encuentra en su primer estado de no borrador), entonces:
   1. Establezca la Persona asignada y el Propietario al último usuario/robot que actualizó la tarea. Si no hay ninguno o el usuario resultante no es válido, entonces
   2. Establezca la Persona asignada/el Propietario como (cualquiera) asignado previamente al usuario/robot en orden descendente de cuando fue asignado. Si no hay ninguno o el usuario resultante no es válido, entonces&#x20;
   3. Si la Acción fue iniciada por el Flujo de trabajo (es decir, no fue manual ad-hoc), entonces establezca la Persona asignada/el Propietario como el último usuario/robot que trabajó en la misma Acción previamente completada en el Caso (o la revisión por compañeros de la Acción si se encuentra en revisión por compañeros). Si no hay ninguno o el usuario resultante no es válido, entonces
5. Ejecute la [regla de asignación](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours) para esta tarea:
   1. Si la asignación *push* principal está configurada para un usuario específico, establezca la Persona asignada/el Propietario para ese usuario. Si no hay ninguno o el usuario resultante no es válido, entonces
   2. Si la asignación *push* secundaria está configurada para un usuario específico, configure la Persona asignada/el Propietario para ese usuario. Si no hay ninguno o el usuario resultante no es válido, entonces
   3. Si la asignación *push* principal está configurada en la Posición de los usuarios que ocupan esta posición, configure la Persona asignada/ el Propietario como el usuario con menos tareas en su bandeja de entrada. Si no hay ninguno o el usuario resultante no es válido, entonces
   4. Si la asignación *push* secundaria está configurada en la Posición de los usuarios que ocupan esta posición, configure la Persona asignada/el Propietario como el usuario con menos tareas en su bandeja de entrada. Si no hay ninguno o el usuario resultante no es válido, entonces
6. Si la tarea es un Caso, configure la Persona asignada/el Propietario como el usuario/robot que inició ese Caso.

## Verificación de validez

Como parte de la regla de verificación de la asignación de la Persona asignada/el Propietario, tenemos que determinar si el objetivo es válido. Para que sea válido, hay una serie de reglas de verificación de validez que debe cumplir. Si no es así, continuamos con las reglas de establecimiento de una Persona asignada/Propietario hasta que se encuentre un objetivo válido. Las verificaciones de validez que se realizan son las siguientes:

* Si el usuario/robot no está autorizado a trabajar en tareas de este tipo (es decir, Activo/Prueba) entonces se bloquea.
* Si el usuario/robot está retirado entonces se bloquea.
* Si el usuario no está autorizado entonces se bloquea (no se verifican los permisos de los robots).
* Si el robot está suspendido entonces se bloquea.
* Si el robot ha utilizado la función "Obtener más trabajo" más de 3 veces para esta tarea, se bloquea.
* Si el usuario seleccionado es un robot y la tarea es una Acción que está en la fase de revisión por compañeros, se bloquea (los robots no pueden realizar Revisiones por compañeros).
* Si el usuario seleccionado es un robot y la tarea es una Acción y no hay ninguna granja de robots configurada para la Acción, se bloquea.
* Si el usuario seleccionado es un robot y la tarea es una Acción y el robot no es miembro de la granja de robots configurada para la Acción, se bloquea.
* Si el usuario seleccionado es un robot y la tarea es un Caso, se bloquea (no se pueden asignar Casos a los robots).
* Si la tarea es un manual con una Acción de Revisión por compañeros que se encuentra en la etapa de Revisión por compañeros y el usuario realizó una o más actualizaciones mientras estaba en la etapa de Hacer entonces se bloquea (los usuarios no pueden someter a Revisión por compañeros su propio trabajo).
* Si la tarea es un manual con una Acción de Revisión por compañeros que se encuentra en la etapa de Revisión por compañeros y el usuario realizó una o más actualizaciones mientras estaba en la etapa de Revisión por compañeros entonces se bloquea (no se le puede pedir a los usuarios que hagan una tarea si la han sometido a Revisión por compañeros).
