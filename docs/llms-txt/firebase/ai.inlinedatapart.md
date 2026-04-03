# Source: https://firebase.google.com/docs/reference/js/ai.inlinedatapart.md.txt

Content part interface if the part represents an image.

**Signature:**  

    export interface InlineDataPart 

## Properties

|                                                          Property                                                           |                                                                Type                                                                |              Description               |
|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| [codeExecutionResult](https://firebase.google.com/docs/reference/js/ai.inlinedatapart.md#inlinedatapartcodeexecutionresult) | never                                                                                                                              |                                        |
| [executableCode](https://firebase.google.com/docs/reference/js/ai.inlinedatapart.md#inlinedatapartexecutablecode)           | never                                                                                                                              |                                        |
| [functionCall](https://firebase.google.com/docs/reference/js/ai.inlinedatapart.md#inlinedatapartfunctioncall)               | never                                                                                                                              |                                        |
| [functionResponse](https://firebase.google.com/docs/reference/js/ai.inlinedatapart.md#inlinedatapartfunctionresponse)       | never                                                                                                                              |                                        |
| [inlineData](https://firebase.google.com/docs/reference/js/ai.inlinedatapart.md#inlinedatapartinlinedata)                   | [GenerativeContentBlob](https://firebase.google.com/docs/reference/js/ai.generativecontentblob.md#generativecontentblob_interface) |                                        |
| [text](https://firebase.google.com/docs/reference/js/ai.inlinedatapart.md#inlinedataparttext)                               | never                                                                                                                              |                                        |
| [thought](https://firebase.google.com/docs/reference/js/ai.inlinedatapart.md#inlinedatapartthought)                         | boolean                                                                                                                            |                                        |
| [videoMetadata](https://firebase.google.com/docs/reference/js/ai.inlinedatapart.md#inlinedatapartvideometadata)             | [VideoMetadata](https://firebase.google.com/docs/reference/js/ai.videometadata.md#videometadata_interface)                         | Applicable if `inlineData` is a video. |

## InlineDataPart.codeExecutionResult

**Signature:**  

    codeExecutionResult?: never;

## InlineDataPart.executableCode

**Signature:**  

    executableCode?: never;

## InlineDataPart.functionCall

**Signature:**  

    functionCall?: never;

## InlineDataPart.functionResponse

**Signature:**  

    functionResponse?: never;

## InlineDataPart.inlineData

**Signature:**  

    inlineData: GenerativeContentBlob;

## InlineDataPart.text

**Signature:**  

    text?: never;

## InlineDataPart.thought

**Signature:**  

    thought?: boolean;

## InlineDataPart.videoMetadata

Applicable if `inlineData` is a video.

**Signature:**  

    videoMetadata?: VideoMetadata;