# Source: https://firebase.google.com/docs/reference/js/vertexai.aioptions.md.txt

# AIOptions interface

Options for initializing the AI service using [getAI()](https://firebase.google.com/docs/reference/js/vertexai.md#getai_a94a413). This allows specifying which backend to use (Vertex AI Gemini API or Gemini Developer API) and configuring its specific options (like location for Vertex AI).

**Signature:**  

    export interface AIOptions 

## Properties

|                                            Property                                             |                                            Type                                            |                          Description                          |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| [backend](https://firebase.google.com/docs/reference/js/vertexai.aioptions.md#aioptionsbackend) | [Backend](https://firebase.google.com/docs/reference/js/vertexai.backend.md#backend_class) | The backend configuration to use for the AI service instance. |

## AIOptions.backend

The backend configuration to use for the AI service instance.

**Signature:**  

    backend: Backend;