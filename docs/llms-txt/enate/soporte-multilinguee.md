# Source: https://docs.enate.net/enate-help/espanol/soporte-multilinguee.md

# Soporte Multilingüe

Enate admite los siguientes idiomas:

1. inglés
2. portugués (Brasil)
3. español
4. rumano
5. húngaro
6. polaco
7. ruso
8. francés
9. alemán

El entorno de operaciones en el que los usuarios finales prestan el servicio admitirá varios idiomas y cada usuario podrá elegir su idioma preferido junto con el patrón de fecha y hora deseado en la configuración del perfil de usuario.

El menú desplegable Idioma preferido mostrará la lista de idiomas admitidos por Enate.

![](https://gblobscdn.gitbook.com/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZCCjQMZrIXW_c-JAut%2F-MZCWE2H20vuRKMcEY_D%2FChange-Language.gif?alt=media\&token=112e24b6-1177-4eba-8d46-043d1fae0317)

La pantalla y los elementos/etiquetas de la IU aparecerán en el idioma preferido del usuario; esto se logra al agregar un "paquete de idioma" en **Enate**. Cada paquete de idioma tendrá un mapeo para un idioma específico del usuario como el Portugués, por ejemplo, "Lista" será "Fila" y "Acción" será "Açao" en portugués.

Aquí está la lista de elementos de la interfaz de usuario que estarán disponibles en el idioma preferido del usuario conectado:

| Elemento                      | Detalles                                                                                                                                                                                                  |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Página de Inicio              | <ol><li>Filtro RAG</li><li>Mi Equipo</li><li>Granja de Bots</li><li>Lista</li><li>Gráfico</li><li>Ajustes de Casillas y Columnas</li></ol><p>Mismo comportamiento en la página de Bandeja de entrada.</p> |
| Búsqueda Rápida               | Búsqueda de Personas, Comentarios y Tareas                                                                                                                                                                |
| Página de Lista               |                                                                                                                                                                                                           |
| Enlaces de Navegación         | Enlaces a Builder, Página de Lista o Tareas accedidas recientemente, etc.                                                                                                                                 |
| Página de Perfil de Usuario   | Aquí el Usuario también puede cambiar el Idioma preferido, así como el patrón horario.                                                                                                                    |
| Página de Gestión de Llamadas | Esta página muestra todas las comunicaciones y Tareas relativas a los usuarios individuales.                                                                                                              |
| IU Tarea                      | Etiquetas y Botones como Selector de Categoría, Estado, etc.                                                                                                                                              |

{% hint style="info" %}
Nota – los nombres reales, como los nombres de los clientes y los nombres de usuario, se mantendrán en el idioma original, tal como lo ingresaron los configuradores en Builder.
{% endhint %}

## Datos ingresados por los usuarios finales de *Work Manager* <a href="#datos-ingresados-por-los-usuarios-finales-de-work-manager" id="datos-ingresados-por-los-usuarios-finales-de-work-manager"></a>

Enate admitirá completamente el idioma preferido de un usuario en la pantalla del Administrador de trabajo y los elementos de la interfaz de usuario, incluidas etiquetas, enlaces y botones, sin embargo, todo lo que agregue el usuario permanecerá en el mismo idioma en el que el usuario lo ingresó originalmente y no se traducirá automáticamente a ningún otro idioma cuando es visto por otros usuarios con un idioma preferido diferente.

Por ejemplo, si un usuario brasileño agrega una nota a un Caso en Portugués, Enate guardará la nota en Portugués en la base de datos y solo mostrará la nota en Portugués tal como la ingresó el usuario.

Aquí hay una lista completa de los elementos dependientes de los datos introducidos del usuario y que **NO** serán traducidos automáticamente por el producto.

| Elemento              | Detalles                                                                                                                                                                                                                                                                                                                                            |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Caso                  | <p></p><ol><li>Notas</li><li>Correos electrónicos</li><li>Caso - descripción breve/ título</li><li>Instrucción de anulación de Acción de una Acción nueva lanzada por el usuario final</li></ol>                                                                                                                                                    |
| Acción                | <p></p><ol><li>Notas</li><li>Correos electrónicos</li><li>Comentarios de listas de Verificación</li><li>Estado de la Acción - texto de razón 'No se puede completar'</li><li>Instrucción de anulación de Acción de una Acción nueva lanzada por el usuario final</li><li>Nota de Revisión por pares de la Acción ingresada por el revisor</li></ol> |
| Ticket                | <p></p><ol><li>Título y Descripción de nuevos Tickets secundarios</li><li>Nombre de nueva Acción lanzada por usuario</li><li>Nombre del nuevo Caso lanzado por usuario</li></ol>                                                                                                                                                                    |
| Contacto              | Detalles sobre el Contacto como la dirección                                                                                                                                                                                                                                                                                                        |
| Archivos              | Nombre del archivo y nota sobre el Archivo                                                                                                                                                                                                                                                                                                          |
| Defecto               | Descripción del Defecto                                                                                                                                                                                                                                                                                                                             |
| Notas de Reasignación | Texto ingresado por el usuario mientras reasigna una parte de trabajo a otro compañero de equipo                                                                                                                                                                                                                                                    |

### Datos y Tarjetas personalizados <a href="#datos-y-tarjetas-personalizados" id="datos-y-tarjetas-personalizados"></a>

La versión inicial con la funcionalidad multilingüe no admitirá configuradores que definan varios idiomas al crear datos personalizados y *Tarjetas inteligentes* en *Builder*. Se necesitarían varias tarjetas y elementos de datos para esto.

### Notificaciones en la aplicación <a href="#notificaciones-en-la-aplicacion" id="notificaciones-en-la-aplicacion"></a>

En la versión inicial con funcionalidad multilingüe las notificaciones se mantendrán en inglés.
