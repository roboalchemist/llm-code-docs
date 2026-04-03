# Source: https://firebase.google.com/docs/reference/js/ai.audioconversationcontroller.md.txt

# AudioConversationController interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

A controller for managing an active audio conversation.

**Signature:**  

    export interface AudioConversationController 

## Properties

|                                                        Property                                                         |          Type          |                                                                                Description                                                                                |
|-------------------------------------------------------------------------------------------------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [stop](https://firebase.google.com/docs/reference/js/ai.audioconversationcontroller.md#audioconversationcontrollerstop) | () =\> Promise\<void\> | ***(Public Preview)*** Stops the audio conversation, closes the microphone connection, and cleans up resources. Returns a promise that resolves when cleanup is complete. |

## AudioConversationController.stop

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Stops the audio conversation, closes the microphone connection, and cleans up resources. Returns a promise that resolves when cleanup is complete.

**Signature:**  

    stop: () => Promise<void>;