# Source: https://firebase.google.com/docs/reference/js/ai.functioncallpart.md.txt

Content part interface if the part represents a [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface).

**Signature:**  

    export interface FunctionCallPart 

## Properties

|                                                            Property                                                             |                                                  Type                                                   | Description |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------|
| [codeExecutionResult](https://firebase.google.com/docs/reference/js/ai.functioncallpart.md#functioncallpartcodeexecutionresult) | never                                                                                                   |             |
| [executableCode](https://firebase.google.com/docs/reference/js/ai.functioncallpart.md#functioncallpartexecutablecode)           | never                                                                                                   |             |
| [functionCall](https://firebase.google.com/docs/reference/js/ai.functioncallpart.md#functioncallpartfunctioncall)               | [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface) |             |
| [functionResponse](https://firebase.google.com/docs/reference/js/ai.functioncallpart.md#functioncallpartfunctionresponse)       | never                                                                                                   |             |
| [inlineData](https://firebase.google.com/docs/reference/js/ai.functioncallpart.md#functioncallpartinlinedata)                   | never                                                                                                   |             |
| [text](https://firebase.google.com/docs/reference/js/ai.functioncallpart.md#functioncallparttext)                               | never                                                                                                   |             |
| [thought](https://firebase.google.com/docs/reference/js/ai.functioncallpart.md#functioncallpartthought)                         | boolean                                                                                                 |             |

## FunctionCallPart.codeExecutionResult

**Signature:**  

    codeExecutionResult?: never;

## FunctionCallPart.executableCode

**Signature:**  

    executableCode?: never;

## FunctionCallPart.functionCall

**Signature:**  

    functionCall: FunctionCall;

## FunctionCallPart.functionResponse

**Signature:**  

    functionResponse?: never;

## FunctionCallPart.inlineData

**Signature:**  

    inlineData?: never;

## FunctionCallPart.text

**Signature:**  

    text?: never;

## FunctionCallPart.thought

**Signature:**  

    thought?: boolean;