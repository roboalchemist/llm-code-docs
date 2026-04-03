# Source: https://firebase.google.com/docs/reference/js/ai.startaudioconversationoptions.md.txt

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options for [startAudioConversation()](https://firebase.google.com/docs/reference/js/ai.md#startaudioconversation_01c8e7f).

**Signature:**  

    export interface StartAudioConversationOptions 

## Properties

|                                                                            Property                                                                             |                                                                                                                              Type                                                                                                                               |                                                                                                             Description                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [functionCallingHandler](https://firebase.google.com/docs/reference/js/ai.startaudioconversationoptions.md#startaudioconversationoptionsfunctioncallinghandler) | (functionCalls: [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface)\[\]) =\> Promise\<[FunctionResponse](https://firebase.google.com/docs/reference/js/ai.functionresponse.md#functionresponse_interface)\> | ***(Public Preview)*** An async handler that is called when the model requests a function to be executed. The handler should perform the function call and return the result as a `Part`, which will then be sent back to the model. |

## StartAudioConversationOptions.functionCallingHandler

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

An async handler that is called when the model requests a function to be executed. The handler should perform the function call and return the result as a `Part`, which will then be sent back to the model.

**Signature:**  

    functionCallingHandler?: (functionCalls: FunctionCall[]) => Promise<FunctionResponse>;