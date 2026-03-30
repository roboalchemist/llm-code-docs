# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ResponseModality.md.txt

# FirebaseVertexAI Framework Reference

# ResponseModality

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct ResponseModality : EncodableProtoEnum, Sendable

Represents the different types, or modalities, of data that a model can produce as output.

To configure the desired output modalities for model requests, set the `responseModalities`
parameter when initializing a `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerationConfig.html`. See the [multimodal
responses](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal-response-generation)
documentation for more details.
Important

Support for each response modality, or combination of modalities, depends on the
model.
- `


  ### [text](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ResponseModality#/s:16FirebaseVertexAI16ResponseModalityV4textACvpZ)


  ` Specifies that the model should generate textual content.

  Use this modality when you need the model to produce written language, such as answers to
  questions, summaries, creative writing, code snippets, or structured data formats like JSON.

  #### Declaration

  Swift

      public static let text: ResponseModality

- `


  ### [image](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ResponseModality#/s:16FirebaseVertexAI16ResponseModalityV5imageACvpZ)


  ` **Public Experimental**: Specifies that the model should generate image data.

  Use this modality when you want the model to create visual content based on the provided input
  or prompts. The response might contain one or more generated images. See the [image
  generation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal-response-generation#image-generation)
  documentation for more details.
  Warning

  Image generation using Gemini 2.0 Flash is a **Public Experimental** feature, which
  means that it is not subject to any SLA or deprecation policy and could change in
  backwards-incompatible ways.

  #### Declaration

  Swift

      public static let image: ResponseModality