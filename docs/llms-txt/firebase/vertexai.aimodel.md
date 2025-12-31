# Source: https://firebase.google.com/docs/reference/js/vertexai.aimodel.md.txt

# AIModel class

Base class for Firebase AI model APIs.

Instances of this class are associated with a specific Firebase AI [Backend](https://firebase.google.com/docs/reference/js/vertexai.backend.md#backend_class) and provide methods for interacting with the configured generative model.

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `AIModel` class.

**Signature:**  

    export declare abstract class AIModel 

## Properties

|                                        Property                                         | Modifiers |  Type  |                                                               Description                                                               |
|-----------------------------------------------------------------------------------------|-----------|--------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [model](https://firebase.google.com/docs/reference/js/vertexai.aimodel.md#aimodelmodel) |           | string | The fully qualified model resource name to use for generating images (for example, `publishers/google/models/imagen-3.0-generate-002`). |

## AIModel.model

The fully qualified model resource name to use for generating images (for example, `publishers/google/models/imagen-3.0-generate-002`).

**Signature:**  

    readonly model: string;