# Source: https://firebase.google.com/docs/reference/js/ai.functionresponsepart.md.txt

Content part interface if the part represents [FunctionResponse](https://firebase.google.com/docs/reference/js/ai.functionresponse.md#functionresponse_interface).

**Signature:**  

    export interface FunctionResponsePart 

## Properties

|                                                                Property                                                                 |                                                        Type                                                         | Description |
|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-------------|
| [codeExecutionResult](https://firebase.google.com/docs/reference/js/ai.functionresponsepart.md#functionresponsepartcodeexecutionresult) | never                                                                                                               |             |
| [executableCode](https://firebase.google.com/docs/reference/js/ai.functionresponsepart.md#functionresponsepartexecutablecode)           | never                                                                                                               |             |
| [functionCall](https://firebase.google.com/docs/reference/js/ai.functionresponsepart.md#functionresponsepartfunctioncall)               | never                                                                                                               |             |
| [functionResponse](https://firebase.google.com/docs/reference/js/ai.functionresponsepart.md#functionresponsepartfunctionresponse)       | [FunctionResponse](https://firebase.google.com/docs/reference/js/ai.functionresponse.md#functionresponse_interface) |             |
| [inlineData](https://firebase.google.com/docs/reference/js/ai.functionresponsepart.md#functionresponsepartinlinedata)                   | never                                                                                                               |             |
| [text](https://firebase.google.com/docs/reference/js/ai.functionresponsepart.md#functionresponseparttext)                               | never                                                                                                               |             |
| [thought](https://firebase.google.com/docs/reference/js/ai.functionresponsepart.md#functionresponsepartthought)                         | boolean                                                                                                             |             |

## FunctionResponsePart.codeExecutionResult

**Signature:**  

    codeExecutionResult?: never;

## FunctionResponsePart.executableCode

**Signature:**  

    executableCode?: never;

## FunctionResponsePart.functionCall

**Signature:**  

    functionCall?: never;

## FunctionResponsePart.functionResponse

**Signature:**  

    functionResponse: FunctionResponse;

## FunctionResponsePart.inlineData

**Signature:**  

    inlineData?: never;

## FunctionResponsePart.text

**Signature:**  

    text?: never;

## FunctionResponsePart.thought

**Signature:**  

    thought?: boolean;