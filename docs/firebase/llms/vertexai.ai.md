# Source: https://firebase.google.com/docs/reference/js/vertexai.ai.md.txt

# AI interface

An instance of the Firebase AI SDK.

Do not create this instance directly. Instead, use [getAI()](https://firebase.google.com/docs/reference/js/vertexai.md#getai_a94a413).

**Signature:**  

    export interface AI 

## Properties

|                                      Property                                       |                                                 Type                                                  |                                                                                                                                                                                                                                    Description                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/js/vertexai.ai.md#aiapp)           | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) this [AI](https://firebase.google.com/docs/reference/js/vertexai.ai.md#ai_interface) instance is associated with.                                                                                                                                                                                                                                                       |
| [backend](https://firebase.google.com/docs/reference/js/vertexai.ai.md#aibackend)   | [Backend](https://firebase.google.com/docs/reference/js/vertexai.backend.md#backend_class)            | A [Backend](https://firebase.google.com/docs/reference/js/vertexai.backend.md#backend_class) instance that specifies the configuration for the target backend, either the Gemini Developer API (using [GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)) or the Vertex AI Gemini API (using [VertexAIBackend](https://firebase.google.com/docs/reference/js/vertexai.vertexaibackend.md#vertexaibackend_class)). |
| [location](https://firebase.google.com/docs/reference/js/vertexai.ai.md#ailocation) | string                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## AI.app

The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) this [AI](https://firebase.google.com/docs/reference/js/vertexai.ai.md#ai_interface) instance is associated with.

**Signature:**  

    app: FirebaseApp;

## AI.backend

A [Backend](https://firebase.google.com/docs/reference/js/vertexai.backend.md#backend_class) instance that specifies the configuration for the target backend, either the Gemini Developer API (using [GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)) or the Vertex AI Gemini API (using [VertexAIBackend](https://firebase.google.com/docs/reference/js/vertexai.vertexaibackend.md#vertexaibackend_class)).

**Signature:**  

    backend: Backend;

## AI.location

> | **Warning:** This API is now obsolete.
>
> use `AI.backend.location` instead.
>
> The location configured for this AI service instance, relevant for Vertex AI backends.

**Signature:**  

    location: string;