# Source: https://firebase.google.com/docs/reference/js/vertexai.inlinedatapart.md.txt

# InlineDataPart interface

Content part interface if the part represents an image.

**Signature:**  

    export interface InlineDataPart 

## Properties

|                                                          Property                                                           |                                                                   Type                                                                   |              Description               |
|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| [functionCall](https://firebase.google.com/docs/reference/js/vertexai.inlinedatapart.md#inlinedatapartfunctioncall)         | never                                                                                                                                    |                                        |
| [functionResponse](https://firebase.google.com/docs/reference/js/vertexai.inlinedatapart.md#inlinedatapartfunctionresponse) | never                                                                                                                                    |                                        |
| [inlineData](https://firebase.google.com/docs/reference/js/vertexai.inlinedatapart.md#inlinedatapartinlinedata)             | [GenerativeContentBlob](https://firebase.google.com/docs/reference/js/vertexai.generativecontentblob.md#generativecontentblob_interface) |                                        |
| [text](https://firebase.google.com/docs/reference/js/vertexai.inlinedatapart.md#inlinedataparttext)                         | never                                                                                                                                    |                                        |
| [videoMetadata](https://firebase.google.com/docs/reference/js/vertexai.inlinedatapart.md#inlinedatapartvideometadata)       | [VideoMetadata](https://firebase.google.com/docs/reference/js/vertexai.videometadata.md#videometadata_interface)                         | Applicable if `inlineData` is a video. |

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

## InlineDataPart.videoMetadata

Applicable if `inlineData` is a video.

**Signature:**  

    videoMetadata?: VideoMetadata;