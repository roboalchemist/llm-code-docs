# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveGenerationConfig.md.txt

# FirebaseAILogic Framework Reference

# LiveGenerationConfig

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
    @available(watchOS, unavailable)
    public struct LiveGenerationConfig : Sendable

Configuration options for live content generation.
- `


  ### [init(temperature:topP:topK:candidateCount:maxOutputTokens:presencePenalty:frequencyPenalty:responseModalities:speech:inputAudioTranscription:outputAudioTranscription:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveGenerationConfig#/s:15FirebaseAILogic20LiveGenerationConfigV11temperature4topP0G1K14candidateCount15maxOutputTokens15presencePenalty09frequencyN018responseModalities6speech23inputAudioTranscription06outputtU0ACSfSg_AOSiSgA2p2OSayAA16ResponseModalityVGSgAA06SpeechE0VSgAA0tuE0VSgAZtcfc)


  ` Creates a new `LiveGenerationConfig` value.

  See the
  [Configure model parameters](https://firebase.google.com/docs/vertex-ai/model-parameters)
  guide and the
  [Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig)
  for more details.

  #### Declaration

  Swift

      public init(temperature: Float? = nil, topP: Float? = nil, topK: Int? = nil,
                  candidateCount: Int? = nil, maxOutputTokens: Int? = nil,
                  presencePenalty: Float? = nil, frequencyPenalty: Float? = nil,
                  responseModalities: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ResponseModality.html]? = nil,
                  speech: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SpeechConfig.html? = nil,
                  inputAudioTranscription: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/AudioTranscriptionConfig.html? = nil,
                  outputAudioTranscription: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/AudioTranscriptionConfig.html? = nil)

  #### Parameters

  |---|---|
  | ` temperature ` | Controls the randomness of the language model's output. Higher values (for example, 1.0) make the text more random and creative, while lower values (for example, 0.1) make it more focused and deterministic. |
  | ` topP ` | Controls diversity of generated text. Higher values (e.g., 0.9) produce more diverse text, while lower values (e.g., 0.5) make the output more focused. |
  | ` topK ` | Limits the number of highest probability words the model considers when generating text. For example, a topK of 40 means only the 40 most likely words are considered for the next token. A higher value increases diversity, while a lower value makes the output more deterministic. |
  | ` candidateCount ` | The number of response variations to return; defaults to 1 if not set. Support for multiple candidates depends on the model; see the [Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig) for more details. |
  | ` maxOutputTokens ` | Maximum number of tokens that can be generated in the response. See the configure model parameters [documentation](https://firebase.google.com/docs/vertex-ai/model-parameters?platform=ios#max-output-tokens) for more details. |
  | ` presencePenalty ` | Controls the likelihood of repeating the same words or phrases already generated in the text. Higher values increase the penalty of repetition, resulting in more diverse output. |
  | ` frequencyPenalty ` | Controls the likelihood of repeating words or phrases, with the penalty increasing for each repetition. Higher values increase the penalty of repetition, resulting in more diverse output. |
  | ` responseModalities ` | The data types (modalities) that may be returned in model responses. |
  | ` speech ` | Controls the voice of the model, when streaming `audio` via `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ResponseModality.html`. |
  | ` inputAudioTranscription ` | Configures (and enables) input transcriptions when streaming to the model. |
  | ` outputAudioTranscription ` | Configures (and enables) output transcriptions when streaming to the model. |