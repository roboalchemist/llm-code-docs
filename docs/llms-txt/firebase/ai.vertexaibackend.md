# Source: https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md.txt

# VertexAIBackend class

Configuration class for the Vertex AI Gemini API.

Use this with [AIOptions](https://firebase.google.com/docs/reference/js/ai.aioptions.md#aioptions_interface) when initializing the AI service via [getAI()](https://firebase.google.com/docs/reference/js/ai.md#getai_a94a413) to specify the Vertex AI Gemini API as the backend.

**Signature:**  

    export declare class VertexAIBackend extends Backend 

**Extends:** [Backend](https://firebase.google.com/docs/reference/js/ai.backend.md#backend_class)

## Constructors

|                                                        Constructor                                                        | Modifiers |                        Description                        |
|---------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------|
| [(constructor)(location)](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackendconstructor) |           | Creates a configuration object for the Vertex AI backend. |

## Properties

|                                                Property                                                 | Modifiers |  Type  |                                                                          Description                                                                          |
|---------------------------------------------------------------------------------------------------------|-----------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [location](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackendlocation) |           | string | The region identifier. See [Vertex AI locations](https://firebase.google.com/docs/vertex-ai/locations#available-locations) for a list of supported locations. |

## VertexAIBackend.(constructor)

Creates a configuration object for the Vertex AI backend.

**Signature:**  

    constructor(location?: string);

#### Parameters

| Parameter |  Type  |                                                                                        Description                                                                                         |
|-----------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| location  | string | The region identifier, defaulting to `us-central1`; see [Vertex AI locations](https://firebase.google.com/docs/vertex-ai/locations#available-locations) for a list of supported locations. |

## VertexAIBackend.location

The region identifier. See [Vertex AI locations](https://firebase.google.com/docs/vertex-ai/locations#available-locations) for a list of supported locations.

**Signature:**  

    readonly location: string;