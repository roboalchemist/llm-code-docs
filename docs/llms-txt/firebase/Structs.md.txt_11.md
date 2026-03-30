# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs.md.txt

# FirebaseVertexAI Framework Reference

# Structures

The following structures are available globally.
- `


  ### [FunctionDeclaration](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionDeclaration)


  ` Structured representation of a function declaration.

  This `FunctionDeclaration` is a representation of a block of code that can be used as a `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Tool`
  by the model and executed by the client.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct FunctionDeclaration : Sendable

      extension FunctionDeclaration: Encodable

- `


  ### [Tool](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Tool)


  ` A helper tool that the model may use when generating responses.

  A `Tool` is a piece of code that enables the system to interact with external systems to perform
  an action, or set of actions, outside of knowledge and scope of the model.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct Tool : Sendable

      extension Tool: Encodable

- `


  ### [FunctionCallingConfig](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallingConfig)


  ` Configuration for specifying function calling behavior.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct FunctionCallingConfig : Sendable

      extension FunctionCallingConfig: Encodable

- `


  ### [ToolConfig](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ToolConfig)


  ` Tool configuration for any `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Tool` specified in the request.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ToolConfig : Sendable

      extension ToolConfig: Encodable

- `


  ### [GenerateContentResponse](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse)


  ` The model's response to a generate content request.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct GenerateContentResponse : Sendable

      extension GenerateContentResponse: Decodable

- `


  ### [Candidate](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Candidate)


  ` A struct representing a possible reply to a content generation prompt. Each content generation
  prompt may produce multiple candidate responses.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct Candidate : Sendable

      extension Candidate: Decodable

- `


  ### [CitationMetadata](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CitationMetadata)


  ` A collection of source attributions for a piece of content.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct CitationMetadata : Sendable

      extension CitationMetadata: Decodable

- `


  ### [Citation](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Citation)


  ` A struct describing a source attribution.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct Citation : Sendable

      extension Citation: Decodable

- `


  ### [FinishReason](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FinishReason)


  ` A value enumerating possible reasons for a model to terminate a content generation request.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct FinishReason : DecodableProtoEnum, Hashable, Sendable

- `


  ### [PromptFeedback](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback)


  ` A metadata struct containing any feedback the model had on the prompt it was provided.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct PromptFeedback : Sendable

      extension PromptFeedback: Decodable

- `


  ### [GenerationConfig](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerationConfig)


  ` A struct defining model parameters to be used when sending generative AI
  requests to the backend model.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct GenerationConfig : Sendable

      extension GenerationConfig: Encodable

- `


  ### [RequestOptions](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/RequestOptions)


  ` Configuration parameters for sending requests to the backend.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct RequestOptions : Sendable

      extension RequestOptions: Equatable

- `


  ### [ModalityTokenCount](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModalityTokenCount)


  ` Represents token counting info for a single modality.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ModalityTokenCount : Sendable

      extension ModalityTokenCount: Decodable

- `


  ### [ContentModality](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ContentModality)


  ` Content part modality.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ContentModality : DecodableProtoEnum, Hashable, Sendable

- `


  ### [ModelContent](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModelContent)


  ` A type describing data in media formats interpretable by an AI model. Each generative AI
  request or response contains an `Array` of `ModelContent`s, and each `ModelContent` value
  may comprise multiple heterogeneous `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part`s.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ModelContent : Equatable, Sendable

      extension ModelContent: Codable

- `


  ### [SafetyRating](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating)


  ` A type defining potentially harmful media categories and their model-assigned ratings. A value
  of this type may be assigned to a category for every model-generated response, not just
  responses that exceed a certain threshold.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct SafetyRating : Equatable, Hashable, Sendable

      extension SafetyRating: Decodable

- `


  ### [SafetySetting](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting)


  ` A type used to specify a threshold for harmful content, beyond which the model will return a
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


  ### [HarmCategory](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/HarmCategory)


  ` Categories describing the potential harm a piece of content may pose.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct HarmCategory : CodableProtoEnum, Hashable, Sendable

- `


  ### [CountTokensResponse](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CountTokensResponse)


  ` The model's response to a count tokens request.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct CountTokensResponse

      extension CountTokensResponse: Decodable

- `


  ### [ImagenAspectRatio](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenAspectRatio)


  ` An aspect ratio for images generated by Imagen.

  To specify an aspect ratio for generated images, set `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig#/s:16FirebaseVertexAI22ImagenGenerationConfigV11aspectRatioAA0d6AspectH0VSgvp` in
  your `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig`. See the [Cloud
  documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#aspect-ratio)
  for more details and examples of the supported aspect ratios.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenAspectRatio : Sendable

- `


  ### [ImagenGenerationConfig](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig)


  ` Configuration options for generating images with Imagen.

  See [Parameters for Imagen
  models](https://firebase.google.com/docs/vertex-ai/model-parameters?platform=ios#imagen) to
  learn about parameters available for use with Imagen models, including how to configure them.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenGenerationConfig

- `


  ### [ImagenGenerationResponse](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationResponse)


  ` A response from a request to generate images with Imagen.

  The type placeholder `T` is an image type; this is currently always an `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenInlineImage`.

  This type is returned from:
  - `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/ImagenModel#/s:16FirebaseVertexAI11ImagenModelC14generateImages6promptAA0D18GenerationResponseVyAA0D11InlineImageVGSS_tYaKF` where `T` is `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenInlineImage`

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenGenerationResponse<T>

      extension ImagenGenerationResponse: Decodable where T: Decodable

- `


  ### [ImagenImageFormat](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenImageFormat)


  ` An image format for images generated by Imagen.

  To specify an image format for generated images, set `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig#/s:16FirebaseVertexAI22ImagenGenerationConfigV11imageFormatAA0d5ImageH0VSgvp` in
  your `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig`. See the [Cloud
  documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api#output-options)
  for more details.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenImageFormat

- `


  ### [ImagenImagesBlockedError](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenImagesBlockedError)


  ` An error that occurs when image generation fails due to all generated images being blocked.

  The images may have been blocked due to the specified `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenSafetyFilterLevel`, the
  `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenPersonFilterLevel`, or filtering included in the model. These filter levels may be
  adjusted in your `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenSafetySettings`. See the [Responsible AI and usage guidelines for
  Imagen](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen)
  for more details.

  #### Declaration

  Swift

      public struct ImagenImagesBlockedError : Error

      extension ImagenImagesBlockedError: CustomNSError

- `


  ### [ImagenInlineImage](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenInlineImage)


  ` An image generated by Imagen, represented as inline data.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenInlineImage

      extension ImagenInlineImage: Equatable

      extension ImagenInlineImage: Decodable

- `


  ### [ImagenPersonFilterLevel](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenPersonFilterLevel)


  ` A filter level controlling whether generation of images containing people or faces is allowed.

  See the
  [`personGeneration`](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api#parameter_list)
  documentation for more details.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenPersonFilterLevel : ProtoEnum

- `


  ### [ImagenSafetyFilterLevel](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenSafetyFilterLevel)


  ` A filter level controlling how aggressively to filter sensitive content.

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


  ### [ImagenSafetySettings](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenSafetySettings)


  ` Settings for controlling the aggressiveness of filtering out sensitive content.

  See the [Responsible AI and usage
  guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#config-safety-filters)
  for more details.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ImagenSafetySettings

- `


  ### [TextPart](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/TextPart)


  ` A text part containing a string value.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct TextPart : https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part

- `


  ### [InlineDataPart](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/InlineDataPart)


  ` A data part that is provided inline in requests.

  Data provided as an inline data part is encoded as base64 and included directly (inline) in the
  request. For large files, see `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FileDataPart` which references content by URI instead of
  including the data in the request.
  Important

  Only small files can be sent as inline data because of limits on total request
  sizes;
  see [input files and requirements](https://firebase.google.com/docs/vertex-ai/input-file-requirements#provide-file-as-inline-data)
  for more details and size limits.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct InlineDataPart : https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part

- `


  ### [FileDataPart](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FileDataPart)


  ` File data stored in Cloud Storage for Firebase, referenced by URI.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct FileDataPart : https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part

- `


  ### [FunctionCallPart](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallPart)


  ` A predicted function call returned from the model.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct FunctionCallPart : https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part

- `


  ### [FunctionResponsePart](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionResponsePart)


  ` Result output from a function call.

  Contains a string representing the `FunctionDeclaration.name` and a structured JSON object
  containing any output from the function is used as context to the model. This should contain the
  result of a `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallPart` made based on model prediction.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct FunctionResponsePart : https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part

- `


  ### [ResponseModality](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ResponseModality)


  ` Represents the different types, or modalities, of data that a model can produce as output.

  To configure the desired output modalities for model requests, set the `responseModalities`
  parameter when initializing a `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerationConfig`. See the [multimodal
  responses](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal-response-generation)
  documentation for more details.
  Important

  Support for each response modality, or combination of modalities, depends on the
  model.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct ResponseModality : EncodableProtoEnum, Sendable