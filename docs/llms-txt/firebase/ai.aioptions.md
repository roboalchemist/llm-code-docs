# Source: https://firebase.google.com/docs/reference/js/ai.aioptions.md.txt

# AIOptions interface

Options for initializing the AI service using [getAI()](https://firebase.google.com/docs/reference/js/ai.md#getai_a94a413). This allows specifying which backend to use (Vertex AI Gemini API or Gemini Developer API) and configuring its specific options (like location for Vertex AI).

**Signature:**  

    export interface AIOptions 

## Properties

|                                                             Property                                                              |                                         Type                                         |                                                                                                        Description                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [backend](https://firebase.google.com/docs/reference/js/ai.aioptions.md#aioptionsbackend)                                         | [Backend](https://firebase.google.com/docs/reference/js/ai.backend.md#backend_class) | The backend configuration to use for the AI service instance. Defaults to the Gemini Developer API backend ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)). |
| [useLimitedUseAppCheckTokens](https://firebase.google.com/docs/reference/js/ai.aioptions.md#aioptionsuselimiteduseappchecktokens) | boolean                                                                              | Whether to use App Check limited use tokens. Defaults to false.                                                                                                                                                            |

## AIOptions.backend

The backend configuration to use for the AI service instance. Defaults to the Gemini Developer API backend ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)).

**Signature:**  

    backend?: Backend;

## AIOptions.useLimitedUseAppCheckTokens

Whether to use App Check limited use tokens. Defaults to false.

**Signature:**  

    useLimitedUseAppCheckTokens?: boolean;