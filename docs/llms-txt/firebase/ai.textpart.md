# Source: https://firebase.google.com/docs/reference/js/ai.textpart.md.txt

Content part interface if the part represents a text string.

**Signature:**  

    export interface TextPart 

## Properties

|                                                    Property                                                     |  Type   | Description |
|-----------------------------------------------------------------------------------------------------------------|---------|-------------|
| [codeExecutionResult](https://firebase.google.com/docs/reference/js/ai.textpart.md#textpartcodeexecutionresult) | never   |             |
| [executableCode](https://firebase.google.com/docs/reference/js/ai.textpart.md#textpartexecutablecode)           | never   |             |
| [functionCall](https://firebase.google.com/docs/reference/js/ai.textpart.md#textpartfunctioncall)               | never   |             |
| [functionResponse](https://firebase.google.com/docs/reference/js/ai.textpart.md#textpartfunctionresponse)       | never   |             |
| [inlineData](https://firebase.google.com/docs/reference/js/ai.textpart.md#textpartinlinedata)                   | never   |             |
| [text](https://firebase.google.com/docs/reference/js/ai.textpart.md#textparttext)                               | string  |             |
| [thought](https://firebase.google.com/docs/reference/js/ai.textpart.md#textpartthought)                         | boolean |             |

## TextPart.codeExecutionResult

**Signature:**  

    codeExecutionResult?: never;

## TextPart.executableCode

**Signature:**  

    executableCode?: never;

## TextPart.functionCall

**Signature:**  

    functionCall?: never;

## TextPart.functionResponse

**Signature:**  

    functionResponse?: never;

## TextPart.inlineData

**Signature:**  

    inlineData?: never;

## TextPart.text

**Signature:**  

    text: string;

## TextPart.thought

**Signature:**  

    thought?: boolean;