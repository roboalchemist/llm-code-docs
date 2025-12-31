# Source: https://firebase.google.com/docs/reference/js/vertexai.vertexaimodel.md.txt

# VertexAIModel class

Base class for Vertex AI in Firebase model APIs.

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `VertexAIModel` class.

**Signature:**  

    export declare abstract class VertexAIModel 

## Properties

|                                              Property                                               | Modifiers |  Type  |                                                               Description                                                               |
|-----------------------------------------------------------------------------------------------------|-----------|--------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [model](https://firebase.google.com/docs/reference/js/vertexai.vertexaimodel.md#vertexaimodelmodel) |           | string | The fully qualified model resource name to use for generating images (for example, `publishers/google/models/imagen-3.0-generate-002`). |

## Methods

|                                                                  Method                                                                  | Modifiers |                                Description                                |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------|
| [normalizeModelName(modelName)](https://firebase.google.com/docs/reference/js/vertexai.vertexaimodel.md#vertexaimodelnormalizemodelname) | `static`  | Normalizes the given model name to a fully qualified model resource name. |

## VertexAIModel.model

The fully qualified model resource name to use for generating images (for example, `publishers/google/models/imagen-3.0-generate-002`).

**Signature:**  

    readonly model: string;

## VertexAIModel.normalizeModelName()

Normalizes the given model name to a fully qualified model resource name.

**Signature:**  

    static normalizeModelName(modelName: string): string;

#### Parameters

| Parameter |  Type  |         Description          |
|-----------|--------|------------------------------|
| modelName | string | The model name to normalize. |

**Returns:**

string

The fully qualified model resource name.