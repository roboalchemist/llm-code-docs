# Source: https://firebase.google.com/docs/reference/js/vertexai.safetysetting.md.txt

# SafetySetting interface

Safety setting that can be sent as part of request parameters.

**Signature:**  

    export interface SafetySetting 

## Properties

|                                                  Property                                                   |                                                Type                                                |                                                                                                                                                                                                                                                 Description                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [category](https://firebase.google.com/docs/reference/js/vertexai.safetysetting.md#safetysettingcategory)   | [HarmCategory](https://firebase.google.com/docs/reference/js/vertexai.md#harmcategory)             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [method](https://firebase.google.com/docs/reference/js/vertexai.safetysetting.md#safetysettingmethod)       | [HarmBlockMethod](https://firebase.google.com/docs/reference/js/vertexai.md#harmblockmethod)       | The harm block method.This property is only supported in the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/vertexai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), an [AIError](https://firebase.google.com/docs/reference/js/vertexai.aierror.md#aierror_class) will be thrown if this property is defined. |
| [threshold](https://firebase.google.com/docs/reference/js/vertexai.safetysetting.md#safetysettingthreshold) | [HarmBlockThreshold](https://firebase.google.com/docs/reference/js/vertexai.md#harmblockthreshold) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## SafetySetting.category

**Signature:**  

    category: HarmCategory;

## SafetySetting.method

The harm block method.

This property is only supported in the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/vertexai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), an [AIError](https://firebase.google.com/docs/reference/js/vertexai.aierror.md#aierror_class) will be thrown if this property is defined.

**Signature:**  

    method?: HarmBlockMethod;

## SafetySetting.threshold

**Signature:**  

    threshold: HarmBlockThreshold;