# Source: https://firebase.google.com/docs/reference/js/ai.safetysetting.md.txt

# SafetySetting interface

Safety setting that can be sent as part of request parameters.

**Signature:**  

    export interface SafetySetting 

## Properties

|                                               Property                                                |                                             Type                                             |                                                                                                                                                                                                                                        Description                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [category](https://firebase.google.com/docs/reference/js/ai.safetysetting.md#safetysettingcategory)   | [HarmCategory](https://firebase.google.com/docs/reference/js/ai.md#harmcategory)             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [method](https://firebase.google.com/docs/reference/js/ai.safetysetting.md#safetysettingmethod)       | [HarmBlockMethod](https://firebase.google.com/docs/reference/js/ai.md#harmblockmethod)       | The harm block method.This property is only supported in the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)), an [AIError](https://firebase.google.com/docs/reference/js/ai.aierror.md#aierror_class) will be thrown if this property is defined. |
| [threshold](https://firebase.google.com/docs/reference/js/ai.safetysetting.md#safetysettingthreshold) | [HarmBlockThreshold](https://firebase.google.com/docs/reference/js/ai.md#harmblockthreshold) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## SafetySetting.category

**Signature:**  

    category: HarmCategory;

## SafetySetting.method

The harm block method.

This property is only supported in the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)), an [AIError](https://firebase.google.com/docs/reference/js/ai.aierror.md#aierror_class) will be thrown if this property is defined.

**Signature:**  

    method?: HarmBlockMethod;

## SafetySetting.threshold

**Signature:**  

    threshold: HarmBlockThreshold;