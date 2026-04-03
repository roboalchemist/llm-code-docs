# Source: https://firebase.google.com/docs/reference/js/ai.liveservercontent.md.txt

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

An incremental content update from the model.

**Signature:**  

    export interface LiveServerContent 

## Properties

|                                                             Property                                                              |                                                    Type                                                    |                                                                                                            Description                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [inputTranscription](https://firebase.google.com/docs/reference/js/ai.liveservercontent.md#liveservercontentinputtranscription)   | [Transcription](https://firebase.google.com/docs/reference/js/ai.transcription.md#transcription_interface) | ***(Public Preview)***Transcription of the audio that was input to the model.                                                                                                                                                     |
| [interrupted](https://firebase.google.com/docs/reference/js/ai.liveservercontent.md#liveservercontentinterrupted)                 | boolean                                                                                                    | ***(Public Preview)*** Indicates whether the model was interrupted by the client. An interruption occurs when the client sends a message before the model finishes it's turn. This is`undefined`if the model was not interrupted. |
| [modelTurn](https://firebase.google.com/docs/reference/js/ai.liveservercontent.md#liveservercontentmodelturn)                     | [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface)                   | ***(Public Preview)***The content that the model has generated as part of the current conversation with the user.                                                                                                                 |
| [outputTranscription](https://firebase.google.com/docs/reference/js/ai.liveservercontent.md#liveservercontentoutputtranscription) | [Transcription](https://firebase.google.com/docs/reference/js/ai.transcription.md#transcription_interface) | ***(Public Preview)***Transcription of the audio output from the model.                                                                                                                                                           |
| [turnComplete](https://firebase.google.com/docs/reference/js/ai.liveservercontent.md#liveservercontentturncomplete)               | boolean                                                                                                    | ***(Public Preview)*** Indicates whether the turn is complete. This is`undefined`if the turn is not complete.                                                                                                                     |
| [type](https://firebase.google.com/docs/reference/js/ai.liveservercontent.md#liveservercontenttype)                               | 'serverContent'                                                                                            | ***(Public Preview)***                                                                                                                                                                                                            |

## LiveServerContent.inputTranscription

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Transcription of the audio that was input to the model.

**Signature:**  

    inputTranscription?: Transcription;

## LiveServerContent.interrupted

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Indicates whether the model was interrupted by the client. An interruption occurs when the client sends a message before the model finishes it's turn. This is`undefined`if the model was not interrupted.

**Signature:**  

    interrupted?: boolean;

## LiveServerContent.modelTurn

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The content that the model has generated as part of the current conversation with the user.

**Signature:**  

    modelTurn?: Content;

## LiveServerContent.outputTranscription

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Transcription of the audio output from the model.

**Signature:**  

    outputTranscription?: Transcription;

## LiveServerContent.turnComplete

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Indicates whether the turn is complete. This is`undefined`if the turn is not complete.

**Signature:**  

    turnComplete?: boolean;

## LiveServerContent.type

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    type: 'serverContent';