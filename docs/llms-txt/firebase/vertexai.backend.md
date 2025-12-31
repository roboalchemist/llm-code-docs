# Source: https://firebase.google.com/docs/reference/js/vertexai.backend.md.txt

# Backend class

Abstract base class representing the configuration for an AI service backend. This class should not be instantiated directly. Use its subclasses; [GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class) for the Gemini Developer API (via [Google AI](https://ai.google/)), and [VertexAIBackend](https://firebase.google.com/docs/reference/js/vertexai.vertexaibackend.md#vertexaibackend_class) for the Vertex AI Gemini API.

**Signature:**  

    export declare abstract class Backend 

## Constructors

|                                                 Constructor                                                 | Modifiers |                 Description                  |
|-------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------|
| [(constructor)(type)](https://firebase.google.com/docs/reference/js/vertexai.backend.md#backendconstructor) |           | Protected constructor for use by subclasses. |

## Properties

|                                              Property                                               | Modifiers |                                         Type                                         |         Description         |
|-----------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------|-----------------------------|
| [backendType](https://firebase.google.com/docs/reference/js/vertexai.backend.md#backendbackendtype) |           | [BackendType](https://firebase.google.com/docs/reference/js/vertexai.md#backendtype) | Specifies the backend type. |

## Backend.(constructor)

Protected constructor for use by subclasses.

**Signature:**  

    protected constructor(type: BackendType);

#### Parameters

| Parameter |                                         Type                                         |    Description    |
|-----------|--------------------------------------------------------------------------------------|-------------------|
| type      | [BackendType](https://firebase.google.com/docs/reference/js/vertexai.md#backendtype) | The backend type. |

## Backend.backendType

Specifies the backend type.

**Signature:**  

    readonly backendType: BackendType;