# Source: https://docs.enate.net/enate-help/espanol/procesando-una-accion/envia-email-y-envia-email-y-espera-acciones.md

# Acciones de "Enviar correo electrónico" y "Enviar correo electrónico y esperar"

## Descripción general

Las Acciones de "Enviar correo electrónico" implican el envío automático de un correo electrónico por parte de Enate y luego la Acción se cerrará inmediatamente. Los usuarios de Work Manager no deberían tener que hacer ningún trabajo en este tipo de Acción.&#x20;

Las Acciones de "Enviar correo electrónico y esperar" implican el envío automático de un correo electrónico por parte de Enate. Luego, la Acción pasará a un estado de En espera hasta recibir una respuesta. Una vez que se reciba una respuesta, la Acción pasará a un estado de Por hacer para su procesamiento posterior.

La dirección Para y las direcciones CC o CCO del correo electrónico se configuran en Builder - consulte este artículo sobre cómo configurar Acciones de "Enviar correo electrónico" en Builder.

{% embed url="<https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/email-action-info-tab>" %}

Una vez que se haya enviado el correo electrónico, aparecerá una entrada en la cronología que muestre cuándo se envió, quién lo envió, cualquier dirección CC o CCO, el asunto, y si hace clic para expandir, el cuerpo del correo electrónico.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FeZjfXc39SYj8IOFOuUXg%2Fimage.png?alt=media&#x26;token=32223d18-d584-440f-bd37-af1d11934b2f" alt=""><figcaption></figcaption></figure>

## Excepciones

Si se utiliza una dirección de correo electrónico Para, CC o CCO no válida, el correo electrónico para la Acción Enviar correo electrónico/Enviar correo electrónico y esperar no se enviará automáticamente y la Acción pasará nuevamente a su Lista.

En la cronología aparecerá una advertencia:

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FOGmhhaVDlDFrBKu6LLvU%2Fimage.png?alt=media&#x26;token=55b8283e-9352-4c14-95a7-365e385e86a7" alt=""><figcaption></figcaption></figure>

El propietario del Caso puede entonces decidir si desea enviar manualmente el correo electrónico y tendrá que corregir la dirección de correo electrónico y añadir manualmente el cuerpo del mensaje. También debe ponerse en contacto con el administrador del sistema para avisarle y que pueda corregir la dirección de correo electrónico y evitar futuros errores.
