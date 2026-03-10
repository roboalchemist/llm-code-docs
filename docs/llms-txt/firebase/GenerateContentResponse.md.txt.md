# Source: https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse.md.txt

# GenerateContentResponse

Response from the model supporting multiple candidate responses.

Safety ratings and content filtering are reported for both prompt in `GenerateContentResponse.prompt_feedback` and for each candidate in `finishReason` and in `safetyRatings`. The API: - Returns either all requested candidates or none of them - Returns no candidates at all only if there was something wrong with the prompt (check `promptFeedback`) - Reports feedback on each candidate in `finishReason` and `safetyRatings`.

| JSON representation |
|---|
| ``` { "candidates": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Candidate`) } ], "promptFeedback": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#PromptFeedback`) }, "usageMetadata": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#UsageMetadata`) }, "modelVersion": string, "responseId": string } ``` |

| Fields ||
|---|---|
| `candidates[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Candidate`)`` Candidate responses from the model. |
| `promptFeedback` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#PromptFeedback`)`` Returns the prompt's feedback related to the content filters. |
| `usageMetadata` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#UsageMetadata`)`` Output only. Metadata on the generation requests' token usage. |
| `modelVersion` | `string` Output only. The model version used to generate the response. |
| `responseId` | `string` Output only. responseId is used to identify each response. |

## Candidate

A response candidate generated from the model.

| JSON representation |
|---|
| ``` { "content": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Content`) }, "finishReason": enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#FinishReason`), "safetyRatings": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#SafetyRating`) } ], "citationMetadata": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#CitationMetadata`) }, "tokenCount": integer, "groundingAttributions": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#GroundingAttribution`) } ], "groundingMetadata": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#GroundingMetadata`) }, "avgLogprobs": number, "logprobsResult": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#LogprobsResult`) }, "urlContextMetadata": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#UrlContextMetadata`) }, "index": integer, "finishMessage": string } ``` |

| Fields ||
|---|---|
| `content` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Content`)`` Output only. Generated content returned from the model. |
| `finishReason` | ``enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#FinishReason`)`` Optional. Output only. The reason why the model stopped generating tokens. If empty, the model has not stopped generating tokens. |
| `safetyRatings[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#SafetyRating`)`` List of ratings for the safety of a response candidate. There is at most one rating per category. |
| `citationMetadata` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#CitationMetadata`)`` Output only. Citation information for model-generated candidate. This field may be populated with recitation information for any text included in the `content`. These are passages that are "recited" from copyrighted material in the foundational LLM's training data. |
| `tokenCount` | `integer` Output only. Token count for this candidate. |
| `groundingAttributions[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#GroundingAttribution`)`` Output only. Attribution information for sources that contributed to a grounded answer. This field is populated for `models.generateAnswer` calls. |
| `groundingMetadata` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#GroundingMetadata`)`` Output only. Grounding metadata for the candidate. This field is populated for `GenerateContent` calls. |
| `avgLogprobs` | `number` Output only. Average log probability score of the candidate. |
| `logprobsResult` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#LogprobsResult`)`` Output only. Log-likelihood scores for the response tokens and top tokens |
| `urlContextMetadata` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#UrlContextMetadata`)`` Output only. Metadata related to url context retrieval tool. |
| `index` | `integer` Output only. Index of the candidate in the list of response candidates. |
| `finishMessage` | `string` Optional. Output only. Details the reason why the model stopped generating tokens. This is populated only when `finishReason` is set. |

## Content

The base structured datatype containing multi-part content of a message.

A `Content` includes a `role` field designating the producer of the `Content` and a `parts` field containing multi-part data that contains the content of the message turn.

| JSON representation |
|---|
| ``` { "parts": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Part`) } ], "role": string } ``` |

| Fields ||
|---|---|
| `parts[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Part`)`` Ordered `Parts` that constitute a single message. Parts may have different MIME types. |
| `role` | `string` Optional. The producer of the content. Must be either 'user' or 'model'. Useful to set for multi-turn conversations, otherwise can be left blank or unset. |

## Part

A datatype containing media that is part of a multi-part `Content` message.

A `Part` consists of data which has an associated datatype. A `Part` can only contain one of the accepted types in `Part.data`.

A `Part` must have a fixed IANA MIME type identifying the type and subtype of the media if the `inlineData` field is filled with raw bytes.

| JSON representation |
|---|
| ``` { "thought": boolean, "thoughtSignature": string, "partMetadata": { object }, // Union field `data` can be only one of the following: "text": string, "inlineData": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Blob`) }, "functionCall": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#FunctionCall`) }, "functionResponse": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#FunctionResponse`) }, "fileData": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#FileData`) }, "executableCode": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#ExecutableCode`) }, "codeExecutionResult": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#CodeExecutionResult`) } // End of list of possible types for union field `data`. // Union field `metadata` can be only one of the following: "videoMetadata": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#VideoMetadata`) } // End of list of possible types for union field `metadata`. } ``` |

| Fields ||
|---|---|
| `thought` | `boolean` Optional. Indicates if the part is thought from the model. |
| `thoughtSignature` | `string (https://developers.google.com/discovery/v1/type-format format)` Optional. An opaque signature for the thought so it can be reused in subsequent requests. A base64-encoded string. |
| `partMetadata` | ``object (`https://protobuf.dev/reference/protobuf/google.protobuf#struct` format)`` Custom metadata associated with the Part. Agents using genai.Part as content representation may need to keep track of the additional information. For example it can be name of a file/source from which the Part originates or a way to multiplex multiple Part streams. |
| Union field `data`. `data` can be only one of the following: ||
| `text` | `string` Inline text. |
| `inlineData` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Blob`)`` Inline media bytes. |
| `functionCall` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#FunctionCall`)`` A predicted `FunctionCall` returned from the model that contains a string representing the `FunctionDeclaration.name` with the arguments and their values. |
| `functionResponse` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#FunctionResponse`)`` The result output of a `FunctionCall` that contains a string representing the `FunctionDeclaration.name` and a structured JSON object containing any output from the function is used as context to the model. |
| `fileData` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#FileData`)`` URI based data. |
| `executableCode` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#ExecutableCode`)`` Code generated by the model that is meant to be executed. |
| `codeExecutionResult` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#CodeExecutionResult`)`` Result of executing the `ExecutableCode`. |
| Union field `metadata`. Controls extra preprocessing of data. `metadata` can be only one of the following: ||
| `videoMetadata` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#VideoMetadata`)`` Optional. Video metadata. The metadata should only be specified while the video data is presented in inlineData or fileData. |

## Blob

Raw media bytes.

Text should not be sent as raw bytes, use the 'text' field.

| JSON representation |
|---|
| ``` { "mimeType": string, "data": string } ``` |

| Fields ||
|---|---|
| `mimeType` | `string` The IANA standard MIME type of the source data. Examples: - image/png - image/jpeg If an unsupported MIME type is provided, an error will be returned. For a complete list of supported types, see [Supported file formats](https://ai.google.dev/gemini-api/docs/prompting_with_media#supported_file_formats). |
| `data` | `string (https://developers.google.com/discovery/v1/type-format format)` Raw bytes for media formats. A base64-encoded string. |

## FunctionCall

A predicted `FunctionCall` returned from the model that contains a string representing the `FunctionDeclaration.name` with the arguments and their values.

| JSON representation |
|---|
| ``` { "id": string, "name": string, "args": { object } } ``` |

| Fields ||
|---|---|
| `id` | `string` Optional. The unique id of the function call. If populated, the client to execute the `functionCall` and return the response with the matching `id`. |
| `name` | `string` Required. The name of the function to call. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. |
| `args` | ``object (`https://protobuf.dev/reference/protobuf/google.protobuf#struct` format)`` Optional. The function parameters and values in JSON object format. |

## FunctionResponse

The result output from a `FunctionCall` that contains a string representing the `FunctionDeclaration.name` and a structured JSON object containing any output from the function is used as context to the model. This should contain the result of a`FunctionCall` made based on model prediction.

| JSON representation |
|---|
| ``` { "id": string, "name": string, "response": { object }, "parts": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#FunctionResponsePart`) } ], "willContinue": boolean, "scheduling": enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Scheduling`) } ``` |

| Fields ||
|---|---|
| `id` | `string` Optional. The id of the function call this response is for. Populated by the client to match the corresponding function call `id`. |
| `name` | `string` Required. The name of the function to call. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. |
| `response` | ``object (`https://protobuf.dev/reference/protobuf/google.protobuf#struct` format)`` Required. The function response in JSON object format. Callers can use any keys of their choice that fit the function's syntax to return the function output, e.g. "output", "result", etc. In particular, if the function call failed to execute, the response can have an "error" key to return error details to the model. |
| `parts[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#FunctionResponsePart`)`` Optional. Ordered `Parts` that constitute a function response. Parts may have different IANA MIME types. |
| `willContinue` | `boolean` Optional. Signals that function call continues, and more responses will be returned, turning the function call into a generator. Is only applicable to NON_BLOCKING function calls, is ignored otherwise. If set to false, future responses will not be considered. It is allowed to return empty `response` with `willContinue=False` to signal that the function call is finished. This may still trigger the model generation. To avoid triggering the generation and finish the function call, additionally set `scheduling` to `SILENT`. |
| `scheduling` | ``enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Scheduling`)`` Optional. Specifies how the response should be scheduled in the conversation. Only applicable to NON_BLOCKING function calls, is ignored otherwise. Defaults to WHEN_IDLE. |

## FunctionResponsePart

A datatype containing media that is part of a `FunctionResponse` message.

A `FunctionResponsePart` consists of data which has an associated datatype. A `FunctionResponsePart` can only contain one of the accepted types in `FunctionResponsePart.data`.

A `FunctionResponsePart` must have a fixed IANA MIME type identifying the type and subtype of the media if the `inlineData` field is filled with raw bytes.

| JSON representation |
|---|
| ``` { // Union field `data` can be only one of the following: "inlineData": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#FunctionResponseBlob`) } // End of list of possible types for union field `data`. } ``` |

| Fields ||
|---|---|
| Union field `data`. The data of the function response part. `data` can be only one of the following: ||
| `inlineData` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#FunctionResponseBlob`)`` Inline media bytes. |

## FunctionResponseBlob

Raw media bytes for function response.

Text should not be sent as raw bytes, use the 'FunctionResponse.response' field.

| JSON representation |
|---|
| ``` { "mimeType": string, "data": string } ``` |

| Fields ||
|---|---|
| `mimeType` | `string` The IANA standard MIME type of the source data. Examples: - image/png - image/jpeg If an unsupported MIME type is provided, an error will be returned. For a complete list of supported types, see [Supported file formats](https://ai.google.dev/gemini-api/docs/prompting_with_media#supported_file_formats). |
| `data` | `string (https://developers.google.com/discovery/v1/type-format format)` Raw bytes for media formats. A base64-encoded string. |

## Scheduling

Specifies how the response should be scheduled in the conversation.

| Enums ||
|---|---|
| `SCHEDULING_UNSPECIFIED` | This value is unused. |
| `SILENT` | Only add the result to the conversation context, do not interrupt or trigger generation. |
| `WHEN_IDLE` | Add the result to the conversation context, and prompt to generate output without interrupting ongoing generation. |
| `INTERRUPT` | Add the result to the conversation context, interrupt ongoing generation and prompt to generate output. |

## FileData

URI based data.

| JSON representation |
|---|
| ``` { "mimeType": string, "fileUri": string } ``` |

| Fields ||
|---|---|
| `mimeType` | `string` Optional. The IANA standard MIME type of the source data. |
| `fileUri` | `string` Required. URI. |

## ExecutableCode

Code generated by the model that is meant to be executed, and the result returned to the model.

Only generated when using the `CodeExecution` tool, in which the code will be automatically executed, and a corresponding `CodeExecutionResult` will also be generated.

| JSON representation |
|---|
| ``` { "language": enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Language`), "code": string } ``` |

| Fields ||
|---|---|
| `language` | ``enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Language`)`` Required. Programming language of the `code`. |
| `code` | `string` Required. The code to be executed. |

## Language

Supported programming languages for the generated code.

| Enums ||
|---|---|
| `LANGUAGE_UNSPECIFIED` | Unspecified language. This value should not be used. |
| `PYTHON` | Python \>= 3.10, with numpy and simpy available. Python is the default language. |

## CodeExecutionResult

Result of executing the `ExecutableCode`.

Only generated when using the `CodeExecution`, and always follows a `part` containing the `ExecutableCode`.

| JSON representation |
|---|
| ``` { "outcome": enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Outcome`), "output": string } ``` |

| Fields ||
|---|---|
| `outcome` | ``enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Outcome`)`` Required. Outcome of the code execution. |
| `output` | `string` Optional. Contains stdout when code execution is successful, stderr or other description otherwise. |

## Outcome

Enumeration of possible outcomes of the code execution.

| Enums ||
|---|---|
| `OUTCOME_UNSPECIFIED` | Unspecified status. This value should not be used. |
| `OUTCOME_OK` | Code execution completed successfully. |
| `OUTCOME_FAILED` | Code execution finished but with a failure. `stderr` should contain the reason. |
| `OUTCOME_DEADLINE_EXCEEDED` | Code execution ran for too long, and was cancelled. There may or may not be a partial output present. |

## VideoMetadata

Metadata describes the input video content.

| JSON representation |
|---|
| ``` { "startOffset": string, "endOffset": string, "fps": number } ``` |

| Fields ||
|---|---|
| `startOffset` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#duration` format)`` Optional. The start offset of the video. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |
| `endOffset` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#duration` format)`` Optional. The end offset of the video. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |
| `fps` | `number` Optional. The frame rate of the video sent to the model. If not specified, the default value will be 1.0. The fps range is (0.0, 24.0\]. |

## FinishReason

Defines the reason why the model stopped generating tokens.

| Enums ||
|---|---|
| `FINISH_REASON_UNSPECIFIED` | Default value. This value is unused. |
| `STOP` | Natural stop point of the model or provided stop sequence. |
| `MAX_TOKENS` | The maximum number of tokens as specified in the request was reached. |
| `SAFETY` | The response candidate content was flagged for safety reasons. |
| `RECITATION` | The response candidate content was flagged for recitation reasons. |
| `LANGUAGE` | The response candidate content was flagged for using an unsupported language. |
| `OTHER` | Unknown reason. |
| `BLOCKLIST` | Token generation stopped because the content contains forbidden terms. |
| `PROHIBITED_CONTENT` | Token generation stopped for potentially containing prohibited content. |
| `SPII` | Token generation stopped because the content potentially contains Sensitive Personally Identifiable Information (SPII). |
| `MALFORMED_FUNCTION_CALL` | The function call generated by the model is invalid. |
| `IMAGE_SAFETY` | Token generation stopped because generated images contain safety violations. |
| `IMAGE_PROHIBITED_CONTENT` | Image generation stopped because generated images has other prohibited content. |
| `IMAGE_OTHER` | Image generation stopped because of other miscellaneous issue. |
| `NO_IMAGE` | The model was expected to generate an image, but none was generated. |
| `IMAGE_RECITATION` | Image generation stopped due to recitation. |
| `UNEXPECTED_TOOL_CALL` | Model generated a tool call but no tools were enabled in the request. |
| `TOO_MANY_TOOL_CALLS` | Model called too many tools consecutively, thus the system exited execution. |

## SafetyRating

Safety rating for a piece of content.

The safety rating contains the category of harm and the harm probability level in that category for a piece of content. Content is classified for safety across a number of harm categories and the probability of the harm classification is included here.

| JSON representation |
|---|
| ``` { "category": enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#HarmCategory`), "probability": enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#HarmProbability`), "blocked": boolean } ``` |

| Fields ||
|---|---|
| `category` | ``enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#HarmCategory`)`` Required. The category for this rating. |
| `probability` | ``enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#HarmProbability`)`` Required. The probability of harm for this content. |
| `blocked` | `boolean` Was this content blocked because of this rating? |

## HarmCategory

The category of a rating.

These categories cover various kinds of harms that developers may wish to adjust.

| Enums ||
|---|---|
| `HARM_CATEGORY_UNSPECIFIED` | Category is unspecified. |
| `HARM_CATEGORY_DEROGATORY` | **PaLM** - Negative or harmful comments targeting identity and/or protected attribute. |
| `HARM_CATEGORY_TOXICITY` | **PaLM** - Content that is rude, disrespectful, or profane. |
| `HARM_CATEGORY_VIOLENCE` | **PaLM** - Describes scenarios depicting violence against an individual or group, or general descriptions of gore. |
| `HARM_CATEGORY_SEXUAL` | **PaLM** - Contains references to sexual acts or other lewd content. |
| `HARM_CATEGORY_MEDICAL` | **PaLM** - Promotes unchecked medical advice. |
| `HARM_CATEGORY_DANGEROUS` | **PaLM** - Dangerous content that promotes, facilitates, or encourages harmful acts. |
| `HARM_CATEGORY_HARASSMENT` | **Gemini** - Harassment content. |
| `HARM_CATEGORY_HATE_SPEECH` | **Gemini** - Hate speech and content. |
| `HARM_CATEGORY_SEXUALLY_EXPLICIT` | **Gemini** - Sexually explicit content. |
| `HARM_CATEGORY_DANGEROUS_CONTENT` | **Gemini** - Dangerous content. |
| `HARM_CATEGORY_CIVIC_INTEGRITY` | **Gemini** - Content that may be used to harm civic integrity. DEPRECATED: use enableEnhancedCivicAnswers instead. > [!WARNING] > This item is deprecated! |

## HarmProbability

The probability that a piece of content is harmful.

The classification system gives the probability of the content being unsafe. This does not indicate the severity of harm for a piece of content.

| Enums ||
|---|---|
| `HARM_PROBABILITY_UNSPECIFIED` | Probability is unspecified. |
| `NEGLIGIBLE` | Content has a negligible chance of being unsafe. |
| `LOW` | Content has a low chance of being unsafe. |
| `MEDIUM` | Content has a medium chance of being unsafe. |
| `HIGH` | Content has a high chance of being unsafe. |

## CitationMetadata

A collection of source attributions for a piece of content.

| JSON representation |
|---|
| ``` { "citationSources": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#CitationSource`) } ] } ``` |

| Fields ||
|---|---|
| `citationSources[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#CitationSource`)`` Citations to sources for a specific response. |

## CitationSource

A citation to a source for a portion of a specific response.

| JSON representation |
|---|
| ``` { "startIndex": integer, "endIndex": integer, "uri": string, "license": string } ``` |

| Fields ||
|---|---|
| `startIndex` | `integer` Optional. Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes. |
| `endIndex` | `integer` Optional. End of the attributed segment, exclusive. |
| `uri` | `string` Optional. URI that is attributed as a source for a portion of the text. |
| `license` | `string` Optional. License for the GitHub project that is attributed as a source for segment. License info is required for code citations. |

## GroundingAttribution

Attribution for a source that contributed to an answer.

| JSON representation |
|---|
| ``` { "sourceId": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#AttributionSourceId`) }, "content": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Content`) } } ``` |

| Fields ||
|---|---|
| `sourceId` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#AttributionSourceId`)`` Output only. Identifier for the source contributing to this attribution. |
| `content` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Content`)`` Grounding source content that makes up this attribution. |

## AttributionSourceId

Identifier for the source contributing to this attribution.

| JSON representation |
|---|
| ``` { // Union field `source` can be only one of the following: "groundingPassage": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#GroundingPassageId`) }, "semanticRetrieverChunk": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#SemanticRetrieverChunk`) } // End of list of possible types for union field `source`. } ``` |

| Fields ||
|---|---|
| Union field `source`. `source` can be only one of the following: ||
| `groundingPassage` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#GroundingPassageId`)`` Identifier for an inline passage. |
| `semanticRetrieverChunk` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#SemanticRetrieverChunk`)`` Identifier for a `Chunk` fetched via Semantic Retriever. |

## GroundingPassageId

Identifier for a part within a `GroundingPassage`.

| JSON representation |
|---|
| ``` { "passageId": string, "partIndex": integer } ``` |

| Fields ||
|---|---|
| `passageId` | `string` Output only. ID of the passage matching the `GenerateAnswerRequest`'s `GroundingPassage.id`. |
| `partIndex` | `integer` Output only. Index of the part within the `GenerateAnswerRequest`'s `GroundingPassage.content`. |

## SemanticRetrieverChunk

Identifier for a `Chunk` retrieved via Semantic Retriever specified in the `GenerateAnswerRequest` using `SemanticRetrieverConfig`.

| JSON representation |
|---|
| ``` { "source": string, "chunk": string } ``` |

| Fields ||
|---|---|
| `source` | `string` Output only. Name of the source matching the request's `SemanticRetrieverConfig.source`. Example: `corpora/123` or `corpora/123/documents/abc` |
| `chunk` | `string` Output only. Name of the `Chunk` containing the attributed text. Example: `corpora/123/documents/abc/chunks/xyz` |

## GroundingMetadata

Metadata returned to client when grounding is enabled.

| JSON representation |
|---|
| ``` { "groundingChunks": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#GroundingChunk`) } ], "groundingSupports": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#GroundingSupport`) } ], "webSearchQueries": [ string ], "searchEntryPoint": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#SearchEntryPoint`) }, "retrievalMetadata": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#RetrievalMetadata`) }, "googleMapsWidgetContextToken": string } ``` |

| Fields ||
|---|---|
| `groundingChunks[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#GroundingChunk`)`` List of supporting references retrieved from specified grounding source. |
| `groundingSupports[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#GroundingSupport`)`` List of grounding support. |
| `webSearchQueries[]` | `string` Web search queries for the following-up web search. |
| `searchEntryPoint` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#SearchEntryPoint`)`` Optional. Google search entry for the following-up web searches. |
| `retrievalMetadata` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#RetrievalMetadata`)`` Metadata related to retrieval in the grounding flow. |
| `googleMapsWidgetContextToken` | `string` Optional. Resource name of the Google Maps widget context token that can be used with the PlacesContextElement widget in order to render contextual data. Only populated in the case that grounding with Google Maps is enabled. |

## SearchEntryPoint

Google search entry point.

| JSON representation |
|---|
| ``` { "renderedContent": string, "sdkBlob": string } ``` |

| Fields ||
|---|---|
| `renderedContent` | `string` Optional. Web content snippet that can be embedded in a web page or an app webview. |
| `sdkBlob` | `string (https://developers.google.com/discovery/v1/type-format format)` Optional. Base64 encoded JSON representing array of \<search term, search url\> tuple. A base64-encoded string. |

## GroundingChunk

Grounding chunk.

| JSON representation |
|---|
| ``` { // Union field `chunk_type` can be only one of the following: "web": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Web`) }, "retrievedContext": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#RetrievedContext`) }, "maps": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Maps`) } // End of list of possible types for union field `chunk_type`. } ``` |

| Fields ||
|---|---|
| Union field `chunk_type`. Chunk type. `chunk_type` can be only one of the following: ||
| `web` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Web`)`` Grounding chunk from the web. |
| `retrievedContext` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#RetrievedContext`)`` Optional. Grounding chunk from context retrieved by the file search tool. |
| `maps` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Maps`)`` Optional. Grounding chunk from Google Maps. |

## Web

Chunk from the web.

| JSON representation |
|---|
| ``` { "uri": string, "title": string } ``` |

| Fields ||
|---|---|
| `uri` | `string` URI reference of the chunk. |
| `title` | `string` Title of the chunk. |

## RetrievedContext

Chunk from context retrieved by the file search tool.

| JSON representation |
|---|
| ``` { "uri": string, "title": string, "text": string, "fileSearchStore": string } ``` |

| Fields ||
|---|---|
| `uri` | `string` Optional. URI reference of the semantic retrieval document. |
| `title` | `string` Optional. Title of the document. |
| `text` | `string` Optional. Text of the chunk. |
| `fileSearchStore` | `string` Optional. Name of the `FileSearchStore` containing the document. Example: `fileSearchStores/123` |

## Maps

A grounding chunk from Google Maps. A Maps chunk corresponds to a single place.

| JSON representation |
|---|
| ``` { "uri": string, "title": string, "text": string, "placeId": string, "placeAnswerSources": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#PlaceAnswerSources`) } } ``` |

| Fields ||
|---|---|
| `uri` | `string` URI reference of the place. |
| `title` | `string` Title of the place. |
| `text` | `string` Text description of the place answer. |
| `placeId` | `string` This ID of the place, in `places/{placeId}` format. A user can use this ID to look up that place. |
| `placeAnswerSources` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#PlaceAnswerSources`)`` Sources that provide answers about the features of a given place in Google Maps. |

## PlaceAnswerSources

Collection of sources that provide answers about the features of a given place in Google Maps. Each PlaceAnswerSources message corresponds to a specific place in Google Maps. The Google Maps tool used these sources in order to answer questions about features of the place (e.g: "does Bar Foo have Wifi" or "is Foo Bar wheelchair accessible?"). Currently we only support review snippets as sources.

| JSON representation |
|---|
| ``` { "reviewSnippets": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#ReviewSnippet`) } ] } ``` |

| Fields ||
|---|---|
| `reviewSnippets[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#ReviewSnippet`)`` Snippets of reviews that are used to generate answers about the features of a given place in Google Maps. |

## ReviewSnippet

Encapsulates a snippet of a user review that answers a question about the features of a specific place in Google Maps.

| JSON representation |
|---|
| ``` { "reviewId": string, "googleMapsUri": string, "title": string } ``` |

| Fields ||
|---|---|
| `reviewId` | `string` The ID of the review snippet. |
| `googleMapsUri` | `string` A link that corresponds to the user review on Google Maps. |
| `title` | `string` Title of the review. |

## GroundingSupport

Grounding support.

| JSON representation |
|---|
| ``` { "groundingChunkIndices": [ integer ], "confidenceScores": [ number ], "segment": { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Segment`) } } ``` |

| Fields ||
|---|---|
| `groundingChunkIndices[]` | `integer` A list of indices (into 'grounding_chunk') specifying the citations associated with the claim. For instance \[1,3,4\] means that grounding_chunk\[1\], grounding_chunk\[3\], grounding_chunk\[4\] are the retrieved content attributed to the claim. |
| `confidenceScores[]` | `number` Confidence score of the support references. Ranges from 0 to 1. 1 is the most confident. This list must have the same size as the groundingChunkIndices. |
| `segment` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Segment`)`` Segment of the content this support belongs to. |

## Segment

Segment of the content.

| JSON representation |
|---|
| ``` { "partIndex": integer, "startIndex": integer, "endIndex": integer, "text": string } ``` |

| Fields ||
|---|---|
| `partIndex` | `integer` Output only. The index of a Part object within its parent Content object. |
| `startIndex` | `integer` Output only. Start index in the given Part, measured in bytes. Offset from the start of the Part, inclusive, starting at zero. |
| `endIndex` | `integer` Output only. End index in the given Part, measured in bytes. Offset from the start of the Part, exclusive, starting at zero. |
| `text` | `string` Output only. The text corresponding to the segment from the response. |

## RetrievalMetadata

Metadata related to retrieval in the grounding flow.

| JSON representation |
|---|
| ``` { "googleSearchDynamicRetrievalScore": number } ``` |

| Fields ||
|---|---|
| `googleSearchDynamicRetrievalScore` | `number` Optional. Score indicating how likely information from google search could help answer the prompt. The score is in the range \[0, 1\], where 0 is the least likely and 1 is the most likely. This score is only populated when google search grounding and dynamic retrieval is enabled. It will be compared to the threshold to determine whether to trigger google search. |

## LogprobsResult

Logprobs Result

| JSON representation |
|---|
| ``` { "topCandidates": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#TopCandidates`) } ], "chosenCandidates": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Candidate_1`) } ], "logProbabilitySum": number } ``` |

| Fields ||
|---|---|
| `topCandidates[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#TopCandidates`)`` Length = total number of decoding steps. |
| `chosenCandidates[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Candidate_1`)`` Length = total number of decoding steps. The chosen candidates may or may not be in topCandidates. |
| `logProbabilitySum` | `number` Sum of log probabilities for all tokens. |

## TopCandidates

Candidates with top log probabilities at each decoding step.

| JSON representation |
|---|
| ``` { "candidates": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Candidate_1`) } ] } ``` |

| Fields ||
|---|---|
| `candidates[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Candidate_1`)`` Sorted by log probability in descending order. |

## Candidate

Candidate for the logprobs token and score.

| JSON representation |
|---|
| ``` { "token": string, "tokenId": integer, "logProbability": number } ``` |

| Fields ||
|---|---|
| `token` | `string` The candidate's token string value. |
| `tokenId` | `integer` The candidate's token id value. |
| `logProbability` | `number` The candidate's log probability. |

## UrlContextMetadata

Metadata related to url context retrieval tool.

| JSON representation |
|---|
| ``` { "urlMetadata": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#UrlMetadata`) } ] } ``` |

| Fields ||
|---|---|
| `urlMetadata[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#UrlMetadata`)`` List of url context. |

## UrlMetadata

Context of the a single url retrieval.

| JSON representation |
|---|
| ``` { "retrievedUrl": string, "urlRetrievalStatus": enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#UrlRetrievalStatus`) } ``` |

| Fields ||
|---|---|
| `retrievedUrl` | `string` Retrieved url by the tool. |
| `urlRetrievalStatus` | ``enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#UrlRetrievalStatus`)`` Status of the url retrieval. |

## UrlRetrievalStatus

Status of the url retrieval.

| Enums ||
|---|---|
| `URL_RETRIEVAL_STATUS_UNSPECIFIED` | Default value. This value is unused. |
| `URL_RETRIEVAL_STATUS_SUCCESS` | Url retrieval is successful. |
| `URL_RETRIEVAL_STATUS_ERROR` | Url retrieval is failed due to error. |
| `URL_RETRIEVAL_STATUS_PAYWALL` | Url retrieval is failed because the content is behind paywall. |
| `URL_RETRIEVAL_STATUS_UNSAFE` | Url retrieval is failed because the content is unsafe. |

## PromptFeedback

A set of the feedback metadata the prompt specified in `GenerateContentRequest.content`.

| JSON representation |
|---|
| ``` { "blockReason": enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#BlockReason`), "safetyRatings": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#SafetyRating`) } ] } ``` |

| Fields ||
|---|---|
| `blockReason` | ``enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#BlockReason`)`` Optional. If set, the prompt was blocked and no candidates are returned. Rephrase the prompt. |
| `safetyRatings[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#SafetyRating`)`` Ratings for safety of the prompt. There is at most one rating per category. |

## BlockReason

Specifies the reason why the prompt was blocked.

| Enums ||
|---|---|
| `BLOCK_REASON_UNSPECIFIED` | Default value. This value is unused. |
| `SAFETY` | Prompt was blocked due to safety reasons. Inspect `safetyRatings` to understand which safety category blocked it. |
| `OTHER` | Prompt was blocked due to unknown reasons. |
| `BLOCKLIST` | Prompt was blocked due to the terms which are included from the terminology blocklist. |
| `PROHIBITED_CONTENT` | Prompt was blocked due to prohibited content. |
| `IMAGE_SAFETY` | Candidates blocked due to unsafe image generation content. |

## UsageMetadata

Metadata on the generation request's token usage.

| JSON representation |
|---|
| ``` { "promptTokenCount": integer, "cachedContentTokenCount": integer, "candidatesTokenCount": integer, "toolUsePromptTokenCount": integer, "thoughtsTokenCount": integer, "totalTokenCount": integer, "promptTokensDetails": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#ModalityTokenCount`) } ], "cacheTokensDetails": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#ModalityTokenCount`) } ], "candidatesTokensDetails": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#ModalityTokenCount`) } ], "toolUsePromptTokensDetails": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#ModalityTokenCount`) } ] } ``` |

| Fields ||
|---|---|
| `promptTokenCount` | `integer` Number of tokens in the prompt. When `cachedContent` is set, this is still the total effective prompt size meaning this includes the number of tokens in the cached content. |
| `cachedContentTokenCount` | `integer` Number of tokens in the cached part of the prompt (the cached content) |
| `candidatesTokenCount` | `integer` Total number of tokens across all the generated response candidates. |
| `toolUsePromptTokenCount` | `integer` Output only. Number of tokens present in tool-use prompt(s). |
| `thoughtsTokenCount` | `integer` Output only. Number of tokens of thoughts for thinking models. |
| `totalTokenCount` | `integer` Total token count for the generation request (prompt + response candidates). |
| `promptTokensDetails[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#ModalityTokenCount`)`` Output only. List of modalities that were processed in the request input. |
| `cacheTokensDetails[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#ModalityTokenCount`)`` Output only. List of modalities of the cached content in the request input. |
| `candidatesTokensDetails[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#ModalityTokenCount`)`` Output only. List of modalities that were returned in the response. |
| `toolUsePromptTokensDetails[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#ModalityTokenCount`)`` Output only. List of modalities that were processed for tool-use request inputs. |

## ModalityTokenCount

Represents token counting info for a single modality.

| JSON representation |
|---|
| ``` { "modality": enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Modality`), "tokenCount": integer } ``` |

| Fields ||
|---|---|
| `modality` | ``enum (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/GenerateContentResponse#Modality`)`` The modality associated with this token count. |
| `tokenCount` | `integer` Number of tokens. |

## Modality

Content Part modality

| Enums ||
|---|---|
| `MODALITY_UNSPECIFIED` | Unspecified modality. |
| `TEXT` | Plain text. |
| `IMAGE` | Image. |
| `VIDEO` | Video. |
| `AUDIO` | Audio. |
| `DOCUMENT` | Document, e.g. PDF. |