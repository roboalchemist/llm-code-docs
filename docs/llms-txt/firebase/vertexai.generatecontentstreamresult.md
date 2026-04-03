# Source: https://firebase.google.com/docs/reference/js/vertexai.generatecontentstreamresult.md.txt

# GenerateContentStreamResult interface

Result object returned from [GenerativeModel.generateContentStream()](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelgeneratecontentstream) call. Iterate over `stream` to get chunks as they come in and/or use the `response` promise to get the aggregated response when the stream is done.

**Signature:**  

    export interface GenerateContentStreamResult 

## Properties

|                                                               Property                                                                |                                                                                           Type                                                                                           | Description |
|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [response](https://firebase.google.com/docs/reference/js/vertexai.generatecontentstreamresult.md#generatecontentstreamresultresponse) | Promise\<[EnhancedGenerateContentResponse](https://firebase.google.com/docs/reference/js/vertexai.enhancedgeneratecontentresponse.md#enhancedgeneratecontentresponse_interface)\>        |             |
| [stream](https://firebase.google.com/docs/reference/js/vertexai.generatecontentstreamresult.md#generatecontentstreamresultstream)     | AsyncGenerator\<[EnhancedGenerateContentResponse](https://firebase.google.com/docs/reference/js/vertexai.enhancedgeneratecontentresponse.md#enhancedgeneratecontentresponse_interface)\> |             |

## GenerateContentStreamResult.response

**Signature:**  

    response: Promise<EnhancedGenerateContentResponse>;

## GenerateContentStreamResult.stream

**Signature:**  

    stream: AsyncGenerator<EnhancedGenerateContentResponse>;