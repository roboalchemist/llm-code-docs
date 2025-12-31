# Source: https://firebase.google.com/docs/reference/js/ai.videometadata.md.txt

# VideoMetadata interface

Describes the input video content.

**Signature:**  

    export interface VideoMetadata 

## Properties

|                                                 Property                                                  |  Type  |                                                                                    Description                                                                                    |
|-----------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [endOffset](https://firebase.google.com/docs/reference/js/ai.videometadata.md#videometadataendoffset)     | string | The end offset of the video in protobuf [Duration](https://cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1/latest/Google-Protobuf-Duration#json-mapping) format.   |
| [startOffset](https://firebase.google.com/docs/reference/js/ai.videometadata.md#videometadatastartoffset) | string | The start offset of the video in protobuf [Duration](https://cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1/latest/Google-Protobuf-Duration#json-mapping) format. |

## VideoMetadata.endOffset

The end offset of the video in protobuf [Duration](https://cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1/latest/Google-Protobuf-Duration#json-mapping) format.

**Signature:**  

    endOffset: string;

## VideoMetadata.startOffset

The start offset of the video in protobuf [Duration](https://cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1/latest/Google-Protobuf-Duration#json-mapping) format.

**Signature:**  

    startOffset: string;