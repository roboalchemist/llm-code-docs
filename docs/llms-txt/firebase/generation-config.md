# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generation-config.md.txt

# Firebase.AI.GenerationConfig Struct Reference

# Firebase.AI.GenerationConfig

A struct defining model parameters to be used when sending generative [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) requests to the backend model.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [GenerationConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generation-config#struct_firebase_1_1_a_i_1_1_generation_config_1aa16543b83555901239466ab20e084c48)`(float? temperature, float? topP, float? topK, int? candidateCount, int? maxOutputTokens, float? presencePenalty, float? frequencyPenalty, string[] stopSequences, string responseMimeType, `[Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema)` responseSchema, IEnumerable< `[ResponseModality](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i_1a852882073bf7c7a6bd1489ade4b7f51f)` > responseModalities, `[ThinkingConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config)`? thinkingConfig)` Creates a new [GenerationConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generation-config#struct_firebase_1_1_a_i_1_1_generation_config) value. ||

## Public functions

### GenerationConfig

```c#
 Firebase::AI::GenerationConfig::GenerationConfig(
  float? temperature,
  float? topP,
  float? topK,
  int? candidateCount,
  int? maxOutputTokens,
  float? presencePenalty,
  float? frequencyPenalty,
  string[] stopSequences,
  string responseMimeType,
  Schema responseSchema,
  IEnumerable< ResponseModality > responseModalities,
  ThinkingConfig? thinkingConfig
)
```  
Creates a new [GenerationConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generation-config#struct_firebase_1_1_a_i_1_1_generation_config) value.

See the [Configure model parameters](https://firebase.google.com/docs/vertex-ai/model-parameters) guide and the [Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig) for more details.

Note: A temperature of 0 means that the highest probability tokens are always selected. In this case, responses for a given prompt are mostly deterministic, but a small amount of variation is still possible.

|                                                                                                                                                                                                                                      Details                                                                                                                                                                                                                                      ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `temperature` | Controls the randomness of the language model's output. Higher values (for example, 1.0) make the text more random and creative, while lower values (for example, 0.1) make it more focused and deterministic. | |

Important: The range of supported temperature values depends on the model; see the [Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig) for more details.


The supported range is 0.0 to 1.0.

|                                                                                                                                                                        Details                                                                                                                                                                        ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------|---------------------------------------------------------------------------------------------------------------------------------------------------------| | `topP` | Controls diversity of generated text. Higher values (e.g., 0.9) produce more diverse text, while lower values (e.g., 0.5) make the output more focused. | |

Important: The default `topP` value depends on the model; see the [Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig) for more details.


The supported range is 1 to 40.

|                                                                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                                                                       ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `topK` | Limits the number of highest probability words the model considers when generating text. For example, a topK of 40 means only the 40 most likely words are considered for the next token. A higher value increases diversity, while a lower value makes the output more deterministic. | |

Important: Support for `topK` and the default value depends on the model; see the [Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig) for more details.

<br />

|                                                                                                                                                                                                                                                                                                         Details                                                                                                                                                                                                                                                                                                         ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `candidateCount` | The number of response variations to return; defaults to 1 if not set. Support for multiple candidates depends on the model; see the [Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig) for more details. | |

<br />

|                                                                                                                                                                                                                                                            Details                                                                                                                                                                                                                                                            ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `maxOutputTokens` | Maximum number of tokens that can be generated in the response. See the configure model parameters [documentation](https://firebase.google.com/docs/vertex-ai/model-parameters?platform=ios#max-output-tokens) for more details. | |

Note: While both `presencePenalty` and `frequencyPenalty` discourage repetition, `presencePenalty` applies the same penalty regardless of how many times the word/phrase has already appeared, whereas `frequencyPenalty` increases the penalty for *each* repetition of a word/phrase.

|                                                                                                                                                                                                             Details                                                                                                                                                                                                             ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `presencePenalty` | Controls the likelihood of repeating the same words or phrases already generated in the text. Higher values increase the penalty of repetition, resulting in more diverse output. | |

Important: The range of supported `presencePenalty` values depends on the model; see the [Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig) for more details.

Note: While both `frequencyPenalty` and `presencePenalty` discourage repetition, `frequencyPenalty` increases the penalty for *each* repetition of a word/phrase, whereas `presencePenalty` applies the same penalty regardless of how many times the word/phrase has already appeared.

|                                                                                                                                                                                                                        Details                                                                                                                                                                                                                        ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `frequencyPenalty` | Controls the likelihood of repeating words or phrases, with the penalty increasing for each repetition. Higher values increase the penalty of repetition, resulting in more diverse output. | |

Important: The range of supported `frequencyPenalty` values depends on the model; see the [Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig) for more details.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                    Details                                                                                                                                                                                                                                                                                                                                                                                    ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `stopSequences` | A set of up to 5 `String`s that will stop output generation. If specified, the API will stop at the first appearance of a stop sequence. The stop sequence will not be included as part of the response. See the [Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig) for more details. | |


Supported MIME types:

- `text/plain`: Text output; the default behavior if unspecified.
- `application/json`: JSON response in the candidates.
- `text/x.enum`: For classification tasks, output an enum value as defined in the `responseSchema`.

<br />

|                                                                                       Details                                                                                       ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------------|------------------------------------------------------------| | `responseMimeType` | Output response MIME type of the generated candidate text. | |


Compatible MIME types:

- `application/json`: [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for JSON response.

<br />

|                                                                                                                                   Details                                                                                                                                   ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------|----------------------------------------------------------------------------------------------------------| | `responseSchema` | Output schema of the generated candidate text. If set, a compatible `responseMimeType` must also be set. | |

Refer to the [Control generated output](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output) guide for more details.


See the [multimodal responses](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal-response-generation) documentation for more details.

|                                                                                                   Details                                                                                                   ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------------------|----------------------------------------------------------------------| | `responseModalities` | The data types (modalities) that may be returned in model responses. | |


An error will be returned if this field is set for models that don't support thinking.

|                                                                                                                                                                                                                                                                                      Details                                                                                                                                                                                                                                                                                      ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `thinkingConfig` | Configuration for controlling the "thinking" behavior of compatible Gemini models; see [ThinkingConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config) for more details. | |