# Source: https://docs.enate.net/enate-help/espanol/correos-electronicos/correos-electronicos-no-controlados/mas-detalles-sobre-los-correos-electronicos-sin-procesar.md

# Más detalles sobre los correos electrónicos sin procesar

### ¿Cuándo aparecen los correos electrónicos en la vista de Correos electrónicos sin procesar?

Los correos electrónicos aparecerán en la vista de Correos electrónicos sin procesar de su vista de "Bandeja de entrada de correo electrónico" en Work Manager si cumplen con una de las siguientes condiciones:

1. Ninguna de las direcciones de correo electrónico Para y/o CC tiene una ruta de correo electrónico que coincida.
2. Solo hay direcciones CCO en un correo electrónico, no hay direcciones Para o CC.

Consulte la tabla siguiente para obtener información más detallada sobre cómo se gestionan los correos electrónicos que llegan a Enate, en función de las combinaciones de direcciones de correo electrónico relevantes para Enate que pueden aparecer en los campos Para, CC o CCO.

| Situación                                                                                                                                                                        | Cantidad de tareas creadas                            | ¿Aparecerán en la vista sin procesar?                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Un correo electrónico que llega a una sola dirección de correo electrónico en el campo Para o CC.                                                                                | 1                                                     | <mark style="color:orange;">No</mark>                                                          |
| Un correo electrónico que llega a dos o más direcciones de correo electrónico en los campos Para o CC.                                                                           | 2 o más                                               | <mark style="color:orange;">No</mark>                                                          |
| Un correo electrónico que llega a una dirección de correo electrónico en el campo Para, otra en el campo CC y otra en el campo CCO.                                              | 1 para cada dirección Para y CC                       | <mark style="color:orange;">No</mark>                                                          |
| \*Un correo electrónico que llega a una dirección de correo electrónico en el campo Para y otra en el campo CCO.                                                                 | 1 para el campo Para                                  | <mark style="color:orange;">No</mark>                                                          |
| Un correo electrónico que llega a una o más direcciones de correo electrónico solo en CCO. Nada en los campos Para o CC.                                                         | 0                                                     | <mark style="color:green;">Sí - para el buzón de correo electrónico CCO.</mark>                |
| Un correo electrónico que llega a una sola dirección de correo electrónico que no está configurado correctamente en Enate.                                                       | 0                                                     | <mark style="color:green;">Sí - para la dirección de correo electrónico no configurada.</mark> |
| Un correo electrónico que llega a una dirección de correo electrónico que no está configurada correctamente en Enate y una dirección de correo electrónico configurada en Enate. | 1 para la dirección de correo electrónico configurada | <mark style="color:orange;">No</mark>                                                          |
