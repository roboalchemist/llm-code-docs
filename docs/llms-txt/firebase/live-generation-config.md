# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-generation-config.md.txt

# Firebase.AI.LiveGenerationConfig

A struct defining model parameters to be used when generating live session content.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [LiveGenerationConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-generation-config#struct_firebase_1_1_a_i_1_1_live_generation_config_1a83d22c04d1d250459540ad680092e1c3)`(`[SpeechConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/speech-config#struct_firebase_1_1_a_i_1_1_speech_config)`? speechConfig, IEnumerable< `[ResponseModality](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i_1a852882073bf7c7a6bd1489ade4b7f51f)` > responseModalities, float? temperature, float? topP, float? topK, int? maxOutputTokens, float? presencePenalty, float? frequencyPenalty, `[AudioTranscriptionConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/audio-transcription-config#struct_firebase_1_1_a_i_1_1_audio_transcription_config)`? inputAudioTranscription, `[AudioTranscriptionConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/audio-transcription-config#struct_firebase_1_1_a_i_1_1_audio_transcription_config)`? outputAudioTranscription)` Creates a new[LiveGenerationConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-generation-config#struct_firebase_1_1_a_i_1_1_live_generation_config)value. ||

## Public functions

### LiveGenerationConfig

```c#
 Firebase::AI::LiveGenerationConfig::LiveGenerationConfig(
  SpeechConfig? speechConfig,
  IEnumerable< ResponseModality > responseModalities,
  float? temperature,
  float? topP,
  float? topK,
  int? maxOutputTokens,
  float? presencePenalty,
  float? frequencyPenalty,
  AudioTranscriptionConfig? inputAudioTranscription,
  AudioTranscriptionConfig? outputAudioTranscription
)
```  
Creates a new[LiveGenerationConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-generation-config#struct_firebase_1_1_a_i_1_1_live_generation_config)value.

See the[Configure model parameters](https://firebase.google.com/docs/vertex-ai/model-parameters)guide and the[Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig)for more details.

<br />

|                                                                                    Details                                                                                    ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------------|-------------------------------------------------------------| | `speechConfig` | The speech configuration to use if generating audio output. | |

<br />

|                                                                                                                                                               Details                                                                                                                                                               ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------------------|----------------------------------------------------------------------------------------------------------------------------------| | `responseModalities` | A list of response types to receive from the model. Note: Currently only supports being provided one type, despite being a list. | |

Note: A temperature of 0 means that the highest probability tokens are always selected. In this case, responses for a given prompt are mostly deterministic, but a small amount of variation is still possible.

|                                                                                                                                                                                                                                      Details                                                                                                                                                                                                                                      ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `temperature` | Controls the randomness of the language model's output. Higher values (for example, 1.0) make the text more random and creative, while lower values (for example, 0.1) make it more focused and deterministic. | |

Important: The range of supported temperature values depends on the model; see the[Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig)for more details.

The supported range is 0.0 to 1.0.

|                                                                                                                                                                        Details                                                                                                                                                                        ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------|---------------------------------------------------------------------------------------------------------------------------------------------------------| | `topP` | Controls diversity of generated text. Higher values (e.g., 0.9) produce more diverse text, while lower values (e.g., 0.5) make the output more focused. | |

Important: The default`topP`value depends on the model; see the[Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig)for more details.

The supported range is 1 to 40.

|                                                                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                                                                       ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `topK` | Limits the number of highest probability words the model considers when generating text. For example, a topK of 40 means only the 40 most likely words are considered for the next token. A higher value increases diversity, while a lower value makes the output more deterministic. | |

Important: Support for`topK`and the default value depends on the model; see the[Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig)for more details.

<br />

|                                                                                                                                                                                                                                                          Details                                                                                                                                                                                                                                                          ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `maxOutputTokens` | Maximum number of tokens that can be generated in the response. See the configure model parameters[documentation](https://firebase.google.com/docs/vertex-ai/model-parameters?platform=ios#max-output-tokens)for more details. | |

Note: While both`presencePenalty`and`frequencyPenalty`discourage repetition,`presencePenalty`applies the same penalty regardless of how many times the word/phrase has already appeared, whereas`frequencyPenalty`increases the penalty for*each*repetition of a word/phrase.

|                                                                                                                                                                                                             Details                                                                                                                                                                                                             ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `presencePenalty` | Controls the likelihood of repeating the same words or phrases already generated in the text. Higher values increase the penalty of repetition, resulting in more diverse output. | |

Important: The range of supported`presencePenalty`values depends on the model; see the[Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig)for more details.

Note: While both`frequencyPenalty`and`presencePenalty`discourage repetition,`frequencyPenalty`increases the penalty for*each* repetition of a word/phrase, whereas`presencePenalty`applies the same penalty regardless of how many times the word/phrase has already appeared.

|                                                                                                                                                                                                                        Details                                                                                                                                                                                                                        ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `frequencyPenalty` | Controls the likelihood of repeating words or phrases, with the penalty increasing for each repetition. Higher values increase the penalty of repetition, resulting in more diverse output. | |

Important: The range of supported`frequencyPenalty`values depends on the model; see the[Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig)for more details.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                                                                                                                 ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `stopSequences` | A set of up to 5`String`s that will stop output generation. If specified, the API will stop at the first appearance of a stop sequence. The stop sequence will not be included as part of the response. See the[Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig)for more details. | |