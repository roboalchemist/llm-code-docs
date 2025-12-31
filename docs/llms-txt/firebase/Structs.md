# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Structs.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs.md.txt

# Structures

The following structures are available globally.
- `
  ``
  ``
  `

  ### [GenerateContentResponse](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GenerateContentResponse)

  `
  `  
  The model's response to a generate content request.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct GenerateContentResponse : Sendable

      extension GenerateContentResponse: Decodable

- `
  ``
  ``
  `

  ### [Candidate](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Candidate)

  `
  `  
  A struct representing a possible reply to a content generation prompt. Each content generation
  prompt may produce multiple candidate responses.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct Candidate : Sendable

      extension Candidate: Decodable

- `
  ``
  ``
  `

  ### [CitationMetadata](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/CitationMetadata)

  `
  `  
  A collection of source attributions for a piece of content.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct CitationMetadata : Sendable

      extension CitationMetadata: Decodable

- `
  ``
  ``
  `

  ### [Citation](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Citation)

  `
  `  
  A struct describing a source attribution.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct Citation : Sendable, Equatable

      extension Citation: Decodable

- `
  ``
  ``
  `

  ### [FinishReason](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FinishReason)

  `
  `  
  A value enumerating possible reasons for a model to terminate a content generation request.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct FinishReason : DecodableProtoEnum, Hashable, Sendable

- `
  ``
  ``
  `

  ### [PromptFeedback](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/PromptFeedback)

  `
  `  
  A metadata struct containing any feedback the model had on the prompt it was provided.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct PromptFeedback : Sendable

      extension PromptFeedback: Decodable

- `
  ``
  ``
  `

  ### [GroundingMetadata](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GroundingMetadata)

  `
  `  
  Metadata returned to the client when grounding is enabled.  
  Important

  If using Grounding with Google Search, you are required to comply with the
  "Grounding with Google Search" usage requirements for your chosen API provider:
  [Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search)
  or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms)
  section within the Service Specific Terms).  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct GroundingMetadata : Sendable, Equatable, Hashable

      extension GroundingMetadata: Decodable

- `
  ``
  ``
  `

  ### [Segment](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Segment)

  `
  `  
  Represents a specific segment within a [ModelContent](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ModelContent) struct, often used to pinpoint the
  exact location of text or data that grounding information refers to.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct Segment : Sendable, Equatable, Hashable

      extension Segment: Decodable

- `
  ``
  ``
  `

  ### [GenerationConfig](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GenerationConfig)

  `
  `  
  A struct defining model parameters to be used when sending generative AI
  requests to the backend model.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct GenerationConfig : Sendable

      extension GenerationConfig: Encodable

- `
  ``
  ``
  `

  ### [RequestOptions](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/RequestOptions)

  `
  `  
  Configuration parameters for sending requests to the backend.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct RequestOptions : Sendable

      extension RequestOptions: Equatable

- `
  ``
  ``
  `

  ### [ModalityTokenCount](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ModalityTokenCount)

  `
  `  
  Represents token counting info for a single modality.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ModalityTokenCount : Sendable

      extension ModalityTokenCount: Decodable

- `
  ``
  ``
  `

  ### [ContentModality](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ContentModality)

  `
  `  
  Content part modality.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ContentModality : DecodableProtoEnum, Hashable, Sendable

- `
  ``
  ``
  `

  ### [ModelContent](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ModelContent)

  `
  `  
  A type describing data in media formats interpretable by an AI model. Each generative AI
  request or response contains an `Array` of `ModelContent`s, and each `ModelContent` value
  may comprise multiple heterogeneous [Part](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Protocols/Part)s.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ModelContent : Equatable, Sendable

      extension ModelContent: Codable

- `
  ``
  ``
  `

  ### [SafetyRating](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetyRating)

  `
  `  
  A type defining potentially harmful media categories and their model-assigned ratings. A value
  of this type may be assigned to a category for every model-generated response, not just
  responses that exceed a certain threshold.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct SafetyRating : Equatable, Hashable, Sendable

      extension SafetyRating: Decodable

- `
  ``
  ``
  `

  ### [SafetySetting](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetySetting)

  `
  `  
  A type used to specify a threshold for harmful content, beyond which the model will return a
  fallback response instead of generated content.

  See [safety settings for Gemini
  models](https://firebase.google.com/docs/vertex-ai/safety-settings?platform=ios#gemini) for
  more details.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct SafetySetting : Sendable

      extension SafetySetting: Encodable

- `
  ``
  ``
  `

  ### [HarmCategory](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/HarmCategory)

  `
  `  
  Categories describing the potential harm a piece of content may pose.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct HarmCategory : CodableProtoEnum, Hashable, Sendable

- `
  ``
  ``
  `

  ### [FunctionDeclaration](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionDeclaration)

  `
  `  
  Structured representation of a function declaration.

  This `FunctionDeclaration` is a representation of a block of code that can be used as a [Tool](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Tool)
  by the model and executed by the client.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct FunctionDeclaration : Sendable

      extension FunctionDeclaration: Encodable

- `
  ``
  ``
  `

  ### [GoogleSearch](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GoogleSearch)

  `
  `  
  A tool that allows the generative model to connect to Google Search to access and incorporate
  up-to-date information from the web into its responses.  
  Important

  When using this feature, you are required to comply with the
  "Grounding with Google Search" usage requirements for your chosen API provider:
  [Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search)
  or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms)
  section within the Service Specific Terms).  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct GoogleSearch : Sendable

      extension GoogleSearch: Encodable

- `
  ``
  ``
  `

  ### [Tool](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Tool)

  `
  `  
  A helper tool that the model may use when generating responses.

  A `Tool` is a piece of code that enables the system to interact with external systems to perform
  an action, or set of actions, outside of knowledge and scope of the model.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct Tool : Sendable

      extension Tool: Encodable

- `
  ``
  ``
  `

  ### [FunctionCallingConfig](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionCallingConfig)

  `
  `  
  Configuration for specifying function calling behavior.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct FunctionCallingConfig : Sendable

      extension FunctionCallingConfig: Encodable

- `
  ``
  ``
  `

  ### [ToolConfig](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ToolConfig)

  `
  `  
  Tool configuration for any [Tool](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Tool) specified in the request.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ToolConfig : Sendable

      extension ToolConfig: Encodable

- `
  ``
  ``
  `

  ### [CountTokensResponse](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/CountTokensResponse)

  `
  `  
  The model's response to a count tokens request.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct CountTokensResponse : Sendable

      extension CountTokensResponse: Decodable

- `
  ``
  ``
  `

  ### [Backend](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Backend)

  `
  `  
  Represents available backend APIs for the Firebase AI SDK.  

  #### Declaration

  Swift  

      public struct Backend

- `
  ``
  ``
  `

  ### [ImagenAspectRatio](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenAspectRatio)

  `
  `  
  An aspect ratio for images generated by Imagen.

  To specify an aspect ratio for generated images, set [aspectRatio](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenGenerationConfig#/s:10FirebaseAI22ImagenGenerationConfigV11aspectRatioAA0c6AspectG0VSgvp) in
  your [ImagenGenerationConfig](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenGenerationConfig). See the [Cloud
  documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#aspect-ratio)
  for more details and examples of the supported aspect ratios.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenAspectRatio : Sendable

- `
  ``
  ``
  `

  ### [ImagenGenerationConfig](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenGenerationConfig)

  `
  `  
  Configuration options for generating images with Imagen.

  See [Parameters for Imagen
  models](https://firebase.google.com/docs/vertex-ai/model-parameters?platform=ios#imagen) to
  learn about parameters available for use with Imagen models, including how to configure them.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenGenerationConfig

- `
  ``
  ``
  `

  ### [ImagenGenerationResponse](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenGenerationResponse)

  `
  `  
  A response from a request to generate images with Imagen.

  The type placeholder `T` is an image type; this is currently always an [ImagenInlineImage](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenInlineImage).

  This type is returned from:
  - [generateImages(prompt:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/ImagenModel#/s:10FirebaseAI11ImagenModelC14generateImages6promptAA0C18GenerationResponseVyAA0C11InlineImageVGSS_tYaKF) where `T` is [ImagenInlineImage](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenInlineImage)  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenGenerationResponse<T> : Sendable where T : Sendable

      extension ImagenGenerationResponse: Decodable where T: Decodable

- `
  ``
  ``
  `

  ### [ImagenImageFormat](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenImageFormat)

  `
  `  
  An image format for images generated by Imagen.

  To specify an image format for generated images, set [imageFormat](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenGenerationConfig#/s:10FirebaseAI22ImagenGenerationConfigV11imageFormatAA0c5ImageG0VSgvp) in
  your [ImagenGenerationConfig](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenGenerationConfig). See the [Cloud
  documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api#output-options)
  for more details.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenImageFormat

- `
  ``
  ``
  `

  ### [ImagenImagesBlockedError](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenImagesBlockedError)

  `
  `  
  An error that occurs when image generation fails due to all generated images being blocked.

  The images may have been blocked due to the specified [ImagenSafetyFilterLevel](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenSafetyFilterLevel), the
  [ImagenPersonFilterLevel](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenPersonFilterLevel), or filtering included in the model. These filter levels may be
  adjusted in your [ImagenSafetySettings](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenSafetySettings). See the [Responsible AI and usage guidelines for
  Imagen](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen)
  for more details.  

  #### Declaration

  Swift  

      public struct ImagenImagesBlockedError : Error

      extension ImagenImagesBlockedError: CustomNSError

- `
  ``
  ``
  `

  ### [ImagenInlineImage](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenInlineImage)

  `
  `  
  An image generated by Imagen, represented as inline data.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenInlineImage : Sendable

      extension ImagenInlineImage: Equatable

      extension ImagenInlineImage: Decodable

- `
  ``
  ``
  `

  ### [ImagenPersonFilterLevel](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenPersonFilterLevel)

  `
  `  
  A filter level controlling whether generation of images containing people or faces is allowed.

  See the
  [`personGeneration`](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api#parameter_list)
  documentation for more details.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenPersonFilterLevel : ProtoEnum

- `
  ``
  ``
  `

  ### [ImagenSafetyFilterLevel](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenSafetyFilterLevel)

  `
  `  
  A filter level controlling how aggressively to filter sensitive content.

  Text prompts provided as inputs and images (generated or uploaded) through Imagen on Vertex AI
  are assessed against a list of safety filters, which include 'harmful categories' (for example,
  `violence`, `sexual`, `derogatory`, and `toxic`). This filter level controls how aggressively to
  filter out potentially harmful content from responses. See the
  [`safetySetting`](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api#parameter_list)
  documentation and the [Responsible AI and usage
  guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#safety-filters)
  for more details.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenSafetyFilterLevel : ProtoEnum, Sendable

- `
  ``
  ``
  `

  ### [ImagenSafetySettings](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenSafetySettings)

  `
  `  
  Settings for controlling the aggressiveness of filtering out sensitive content.

  See the [Responsible AI and usage
  guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#config-safety-filters)
  for more details.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenSafetySettings

- `
  ``
  ``
  `

  ### [AudioTranscriptionConfig](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/AudioTranscriptionConfig)

  `
  `  
  Configuration options for audio transcriptions when communicating with a model that supports the
  Gemini Live API.

  While there are not currently any options, this will likely change in the future. For now, just
  providing an instance of this struct will enable audio transcriptions for the corresponding
  input or output fields.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public struct AudioTranscriptionConfig : Sendable

- `
  ``
  ``
  `

  ### [LiveAudioTranscription](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveAudioTranscription)

  `
  `  
  Text transcription of some audio form during a live interaction with the model.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public struct LiveAudioTranscription : Sendable

- `
  ``
  ``
  `

  ### [LiveGenerationConfig](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveGenerationConfig)

  `
  `  
  Configuration options for live content generation.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public struct LiveGenerationConfig : Sendable

- `
  ``
  ``
  `

  ### [LiveServerContent](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveServerContent)

  `
  `  
  Incremental server update generated by the model in response to client
  messages.

  Content is generated as quickly as possible, and not in realtime. Clients
  may choose to buffer and play it out in realtime.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public struct LiveServerContent : Sendable

- `
  ``
  ``
  `

  ### [LiveServerGoingAwayNotice](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveServerGoingAwayNotice)

  `
  `  
  Server will not be able to service client soon.

  To learn more about session limits, see the docs on [Maximum session duration](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live#maximum-session-duration).  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public struct LiveServerGoingAwayNotice : Sendable

- `
  ``
  ``
  `

  ### [LiveServerMessage](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveServerMessage)

  `
  `  
  Update from the server, generated from the model in response to client messages.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public struct LiveServerMessage : Sendable

- `
  ``
  ``
  `

  ### [LiveServerToolCall](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveServerToolCall)

  `
  `  
  Request for the client to execute the provided `functionCalls`.

  The client should return matching [FunctionResponsePart](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionResponsePart), where the
  [functionId](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionResponsePart#/s:10FirebaseAI20FunctionResponsePartV10functionIdSSSgvp) fields correspond to individual [FunctionCallPart](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionCallPart)s.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      @available(watchOS, unavailable)
      public struct LiveServerToolCall : Sendable

- `
  ``
  ``
  `

  ### [LiveServerToolCallCancellation](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveServerToolCallCancellation)

  `
  `  
  Notification for the client to cancel a previous function call from [LiveServerToolCall](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveServerToolCall).

  The client does not need to send [FunctionResponsePart](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionResponsePart)s for the cancelled
  [FunctionCallPart](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionCallPart)s.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public struct LiveServerToolCallCancellation : Sendable

- `
  ``
  ``
  `

  ### [LiveSessionUnsupportedMessageError](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveSessionUnsupportedMessageError)

  `
  `  
  The model sent a message that the SDK failed to parse.

  This may indicate that the SDK version needs updating, a model is too old for the current SDK
  version, or that the model is just
  not supported.

  Check the `NSUnderlyingErrorKey` entry in [errorUserInfo](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveSessionUnsupportedMessageError#/s:10Foundation13CustomNSErrorP13errorUserInfoSDySSypGvp)
  for the error that caused this.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public struct LiveSessionUnsupportedMessageError : Error, Sendable, CustomNSError

- `
  ``
  ``
  `

  ### [LiveSessionLostConnectionError](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveSessionLostConnectionError)

  `
  `  
  The live session was closed, because the network connection was lost.

  Check the `NSUnderlyingErrorKey` entry in [errorUserInfo](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveSessionLostConnectionError#/s:10Foundation13CustomNSErrorP13errorUserInfoSDySSypGvp) for
  the error that caused this.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public struct LiveSessionLostConnectionError : Error, Sendable, CustomNSError

- `
  ``
  ``
  `

  ### [LiveSessionUnexpectedClosureError](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveSessionUnexpectedClosureError)

  `
  `  
  The live session was closed, but not for a reason the SDK expected.

  Check the `NSUnderlyingErrorKey` entry in [errorUserInfo](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveSessionUnexpectedClosureError#/s:10Foundation13CustomNSErrorP13errorUserInfoSDySSypGvp)
  for the error that caused this.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public struct LiveSessionUnexpectedClosureError : Error, Sendable, CustomNSError

- `
  ``
  ``
  `

  ### [LiveSessionSetupError](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveSessionSetupError)

  `
  `  
  The model refused our request to setup a live session.

  This can occur due to the model not supporting the requested response modalities, the project
  not having access to the model, the model being invalid, or some internal error.

  Check the `NSUnderlyingErrorKey` entry in [errorUserInfo](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveSessionSetupError#/s:10Foundation13CustomNSErrorP13errorUserInfoSDySSypGvp) for the error
  that caused this.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public struct LiveSessionSetupError : Error, Sendable, CustomNSError

- `
  ``
  ``
  `

  ### [SpeechConfig](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SpeechConfig)

  `
  `  
  Configuration for controlling the voice of the model during conversation.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public struct SpeechConfig : Sendable

- `
  ``
  ``
  `

  ### [TextPart](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/TextPart)

  `
  `  
  A text part containing a string value.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct TextPart : https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Protocols/Part

- `
  ``
  ``
  `

  ### [InlineDataPart](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/InlineDataPart)

  `
  `  
  A data part that is provided inline in requests.

  Data provided as an inline data part is encoded as base64 and included directly (inline) in the
  request. For large files, see [FileDataPart](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FileDataPart) which references content by URI instead of
  including the data in the request.  
  Important

  Only small files can be sent as inline data because of limits on total request
  sizes;
  see [input files and requirements](https://firebase.google.com/docs/vertex-ai/input-file-requirements#provide-file-as-inline-data)
  for more details and size limits.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct InlineDataPart : https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Protocols/Part

- `
  ``
  ``
  `

  ### [FileDataPart](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FileDataPart)

  `
  `  
  File data stored in Cloud Storage for Firebase, referenced by URI.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct FileDataPart : https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Protocols/Part

- `
  ``
  ``
  `

  ### [FunctionCallPart](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionCallPart)

  `
  `  
  A predicted function call returned from the model.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct FunctionCallPart : https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Protocols/Part

- `
  ``
  ``
  `

  ### [FunctionResponsePart](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionResponsePart)

  `
  `  
  Result output from a function call.

  Contains a string representing the `FunctionDeclaration.name` and a structured JSON object
  containing any output from the function is used as context to the model. This should contain the
  result of a [FunctionCallPart](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionCallPart) made based on model prediction.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct FunctionResponsePart : https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Protocols/Part

- `
  ``
  ``
  `

  ### [ExecutableCodePart](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ExecutableCodePart)

  `
  `  
  A part containing code that was executed by the model.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ExecutableCodePart : https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Protocols/Part

- `
  ``
  ``
  `

  ### [CodeExecutionResultPart](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/CodeExecutionResultPart)

  `
  `  
  The result of executing code.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct CodeExecutionResultPart : https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Protocols/Part

- `
  ``
  ``
  `

  ### [ResponseModality](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ResponseModality)

  `
  `  
  Represents the different types, or modalities, of data that a model can produce as output.

  To configure the desired output modalities for model requests, set the `responseModalities`
  parameter when initializing a [GenerationConfig](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GenerationConfig). See the [multimodal
  responses](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal-response-generation)
  documentation for more details.  
  Important

  Support for each response modality, or combination of modalities, depends on the
  model.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ResponseModality : EncodableProtoEnum, Sendable

- `
  ``
  ``
  `

  ### [ThinkingConfig](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ThinkingConfig)

  `
  `  
  Configuration for controlling the "thinking" behavior of compatible Gemini models.

  Certain models, like Gemini 2.5 Flash and Pro, utilize a thinking process before generating a
  response. This allows them to reason through complex problems and plan a more coherent and
  accurate answer.  

  #### Declaration

  Swift  

      public struct ThinkingConfig : Sendable

      extension ThinkingConfig: Encodable

- `
  ``
  ``
  `

  ### [CodeExecution](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs#/s:10FirebaseAI13CodeExecutionV)

  `
  `  
  A tool that allows the model to execute code.

  This tool can be used to solve complex problems, for example, by generating and executing Python
  code to solve a math problem.  

  #### Declaration

  Swift  

      public struct CodeExecution : Sendable, Encodable

- `
  ``
  ``
  `

  ### [URLContextMetadata](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/URLContextMetadata)

  `
  `  
  Metadata related to the [urlContext()](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Tool#/s:10FirebaseAI4ToolV10urlContextACyFZ) tool.  
  Warning

  URL context is a **Public Preview** feature, which means that it is not subject to
  any SLA or deprecation policy and could change in backwards-incompatible ways.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct URLContextMetadata : Sendable, Hashable

      extension URLContextMetadata: Decodable

- `
  ``
  ``
  `

  ### [URLMetadata](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/URLMetadata)

  `
  `  
  Metadata for a single URL retrieved by the [urlContext()](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Tool#/s:10FirebaseAI4ToolV10urlContextACyFZ) tool.  
  Warning

  URL context is a **Public Preview** feature, which means that it is not subject to
  any SLA or deprecation policy and could change in backwards-incompatible ways.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct URLMetadata : Sendable, Hashable

      extension URLMetadata: Decodable