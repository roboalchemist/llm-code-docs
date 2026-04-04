# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes.md.txt

# FirebaseVertexAI Framework Reference

# Classes

The following classes are available globally.
- `


  ### [Chat](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Chat)


  ` An object that represents a back-and-forth chat with a model, capturing the history and saving
  the context in memory between each message sent.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public final class Chat : Sendable

- `


  ### [GenerativeModel](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/GenerativeModel)


  ` A type that represents a remote multimodal model (like Gemini), with the ability to generate
  content based on various input types.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public final class GenerativeModel : Sendable

- `


  ### [ImagenModel](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/ImagenModel)


  ` Represents a remote Imagen model with the ability to generate images using text prompts.

  See the [generate images
  documentation](https://firebase.google.com/docs/vertex-ai/generate-images-imagen?platform=ios)
  for more details about the image generation capabilities offered by the Imagen model in the
  Vertex AI in Firebase SDK.
  Warning

  For Vertex AI in Firebase, image generation using Imagen 3 models is in Public
  Preview, which means that the feature is not subject to any SLA or deprecation policy and
  could change in backwards-incompatible ways.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public final class ImagenModel

- `


  ### [Schema](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema)


  ` A `Schema` object allows the definition of input and output data types.

  These types can be objects, but also primitives and arrays. Represents a select subset of an
  [OpenAPI 3.0 schema object](https://spec.openapis.org/oas/v3.0.3#schema).

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public final class Schema : Sendable

      extension Schema: Encodable

- `


  ### [VertexAI](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/VertexAI)


  ` The Vertex AI for Firebase SDK provides access to Gemini models directly from your app.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public class VertexAI