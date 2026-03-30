# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerationConfig.md.txt

# FirebaseVertexAI Framework Reference

# GenerationConfig

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct GenerationConfig : Sendable

    extension GenerationConfig: Encodable

A struct defining model parameters to be used when sending generative AI
requests to the backend model.
- `


  ### [init(temperature:topP:topK:candidateCount:maxOutputTokens:presencePenalty:frequencyPenalty:stopSequences:responseMIMEType:responseSchema:responseModalities:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerationConfig#/s:16FirebaseVertexAI16GenerationConfigV11temperature4topP0G1K14candidateCount15maxOutputTokens15presencePenalty09frequencyN013stopSequences16responseMIMEType0R6Schema0R10ModalitiesACSfSg_AOSiSgA2p2OSaySSGSgSSSgAA0T0CSgSayAA16ResponseModalityVGSgtcfc)


  ` Creates a new `GenerationConfig` value.

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
                  stopSequences: [String]? = nil, responseMIMEType: String? = nil,
                  responseSchema: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html? = nil, responseModalities: [https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ResponseModality.html]? = nil)

  #### Parameters

  |---|---|
  | ` temperature ` | Controls the randomness of the language model's output. Higher values (for example, 1.0) make the text more random and creative, while lower values (for example, 0.1) make it more focused and deterministic. |
  | ` topP ` | Controls diversity of generated text. Higher values (e.g., 0.9) produce more diverse text, while lower values (e.g., 0.5) make the output more focused. |
  | ` topK ` | Limits the number of highest probability words the model considers when generating text. For example, a topK of 40 means only the 40 most likely words are considered for the next token. A higher value increases diversity, while a lower value makes the output more deterministic. |
  | ` candidateCount ` | The number of response variations to return; defaults to 1 if not set. Support for multiple candidates depends on the model; see the [Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig) for more details. |
  | ` maxOutputTokens ` | Maximum number of tokens that can be generated in the response. See the configure model parameters [documentation](https://firebase.google.com/docs/vertex-ai/model-parameters?platform=ios#max-output-tokens) for more details. |
  | ` presencePenalty ` | Controls the likelihood of repeating the same words or phrases already generated in the text. Higher values increase the penalty of repetition, resulting in more diverse output. |
  | ` frequencyPenalty ` | Controls the likelihood of repeating words or phrases, with the penalty increasing for each repetition. Higher values increase the penalty of repetition, resulting in more diverse output. |
  | ` stopSequences ` | A set of up to 5 `String`s that will stop output generation. If specified, the API will stop at the first appearance of a stop sequence. The stop sequence will not be included as part of the response. See the [Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig) for more details. |
  | ` responseMIMEType ` | Output response MIME type of the generated candidate text. |
  | ` responseSchema ` | Output schema of the generated candidate text. If set, a compatible `responseMIMEType` must also be set. |
  | ` responseModalities ` | The data types (modalities) that may be returned in model responses. |