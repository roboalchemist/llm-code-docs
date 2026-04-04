# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes.md.txt

# FirebaseAILogic Framework Reference

# Classes

The following classes are available globally.
- `


  ### [Chat](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/Chat)


  ` An object that represents a back-and-forth chat with a model, capturing the history and saving
  the context in memory between each message sent.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public final class Chat : Sendable

- `


  ### [FirebaseAI](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/FirebaseAI)


  ` The Firebase AI SDK provides access to Gemini models directly from your app.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public final class FirebaseAI : Sendable

- `


  ### [GenerativeModel](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/GenerativeModel)


  ` A type that represents a remote multimodal model (like Gemini), with the ability to generate
  content based on various input types.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public final class GenerativeModel : Sendable

- `


  ### [TemplateGenerativeModel](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/TemplateGenerativeModel)


  ` A type that represents a remote multimodal model (like Gemini), with the ability to generate
  content based on various input types.

  **Public Preview**: This API is a public preview and may be subject to change.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public final class TemplateGenerativeModel : Sendable

- `


  ### [TemplateImagenModel](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/TemplateImagenModel)


  ` A type that represents a remote image generation model (like Imagen), with the ability to
  generate
  images based on various input types.

  **Public Preview**: This API is a public preview and may be subject to change.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public final class TemplateImagenModel : Sendable

- `


  ### [ImagenModel](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/ImagenModel)


  ` Represents a remote Imagen model with the ability to generate images using text prompts.

  See the [generate images
  documentation](https://firebase.google.com/docs/vertex-ai/generate-images-imagen?platform=ios)
  for more details about the image generation capabilities offered by the Imagen model in the
  Firebase AI SDK SDK.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public final class ImagenModel

- `


  ### [LiveGenerativeModel](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveGenerativeModel)


  ` A multimodal model (like Gemini) capable of real-time content generation based on
  various input types, supporting bidirectional streaming.

  You can create a new session via `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveGenerativeModel#/s:15FirebaseAILogic19LiveGenerativeModelC7connectAA0C7SessionCyYaKF`.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public final class LiveGenerativeModel

- `


  ### [LiveSession](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession)


  ` A live WebSocket session, capable of streaming content to and from the model.

  Messages are streamed through `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession#/s:15FirebaseAILogic11LiveSessionC9responsesScsyAA0C13ServerMessageVs5Error_pGvp`, and can be sent through either the
  dedicated realtime API function (such as `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession#/s:15FirebaseAILogic11LiveSessionC17sendAudioRealtimeyy10Foundation4DataVYaF` and
  `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession#/s:15FirebaseAILogic11LiveSessionC16sendTextRealtimeyySSYaF`), or through the incremental API (such as
  `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession#/s:15FirebaseAILogic11LiveSessionC11sendContent_12turnCompleteySayAA05ModelF0VG_SbtYaF`).

  To create an instance of this class, see `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveGenerativeModel`.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      @available(watchOS, unavailable)
      public final class LiveSession : Sendable

- `


  ### [Schema](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/Schema)


  ` A `Schema` object allows the definition of input and output data types.

  These types can be objects, but also primitives and arrays. Represents a select subset of an
  [OpenAPI 3.0 schema object](https://spec.openapis.org/oas/v3.0.3#schema).

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public final class Schema : Sendable

      extension Schema: Encodable