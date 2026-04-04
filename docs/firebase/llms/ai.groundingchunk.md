# Source: https://firebase.google.com/docs/reference/js/ai.groundingchunk.md.txt

# GroundingChunk interface

Represents a chunk of retrieved data that supports a claim in the model's response. This is part of the grounding information provided when grounding is enabled.

**Signature:**  

    export interface GroundingChunk 

## Properties

|                                          Property                                           |                                                          Type                                                          |                          Description                          |
|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| [web](https://firebase.google.com/docs/reference/js/ai.groundingchunk.md#groundingchunkweb) | [WebGroundingChunk](https://firebase.google.com/docs/reference/js/ai.webgroundingchunk.md#webgroundingchunk_interface) | Contains details if the grounding chunk is from a web source. |

## GroundingChunk.web

Contains details if the grounding chunk is from a web source.

**Signature:**  

    web?: WebGroundingChunk;