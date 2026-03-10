# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession.md.txt

# FirebaseAILogic Framework Reference

# LiveSession

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    @available(watchOS, unavailable)
    public final class LiveSession : Sendable

A live WebSocket session, capable of streaming content to and from the model.

Messages are streamed through `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession.html#/s:15FirebaseAILogic11LiveSessionC9responsesScsyAA0C13ServerMessageVs5Error_pGvp`, and can be sent through either the
dedicated realtime API function (such as `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession.html#/s:15FirebaseAILogic11LiveSessionC17sendAudioRealtimeyy10Foundation4DataVYaF` and
`https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession.html#/s:15FirebaseAILogic11LiveSessionC16sendTextRealtimeyySSYaF`), or through the incremental API (such as
`https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession.html#/s:15FirebaseAILogic11LiveSessionC11sendContent_12turnCompleteySayAA05ModelF0VG_SbtYaF`).

To create an instance of this class, see `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveGenerativeModel.html`.
- `


  ### [responses](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession#/s:15FirebaseAILogic11LiveSessionC9responsesScsyAA0C13ServerMessageVs5Error_pGvp)


  ` An asynchronous stream of messages from the server.

  These messages from the incremental updates from the model, for the current conversation.

  #### Declaration

  Swift

      public var responses: AsyncThrowingStream<https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerMessage.html, Error> { get }

- `


  ### [sendFunctionResponses(_:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession#/s:15FirebaseAILogic11LiveSessionC21sendFunctionResponsesyySayAA0F12ResponsePartVGYaF)


  ` Response to a `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerToolCall.html` received from the server.

  This method is used both for the realtime API and the incremental API.

  #### Declaration

  Swift

      public func sendFunctionResponses(_ responses: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart.html]) async

  #### Parameters

  |---|---|
  | ` responses ` | Client generated function results, matched to their respective `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.html` by the `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.html#/s:15FirebaseAILogic16FunctionCallPartV10functionIdSSSgvp` field. |

- `


  ### [sendAudioRealtime(_:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession#/s:15FirebaseAILogic11LiveSessionC17sendAudioRealtimeyy10Foundation4DataVYaF)


  ` Sends an audio input stream to the model, using the realtime API.

  To learn more about audio formats, and the required state they should be provided in, see the
  docs on
  [Supported audio formats](https://cloud.google.com/vertex-ai/generative-ai/docs/live-api#supported-audio-formats).

  #### Declaration

  Swift

      public func sendAudioRealtime(_ audio: Data) async

  #### Parameters

  |---|---|
  | ` audio ` | Raw 16-bit PCM audio at 16Hz, used to update the model on the client's conversation. |

- `


  ### [sendVideoRealtime(_:mimeType:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession#/s:15FirebaseAILogic11LiveSessionC17sendVideoRealtime_8mimeTypey10Foundation4DataV_SStYaF)


  ` Sends a video frame to the model, using the realtime API.

  Instead of raw video data, the model expects individual frames of the video,
  sent as images.

  If your video has audio, send it separately through `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession.html#/s:15FirebaseAILogic11LiveSessionC17sendAudioRealtimeyy10Foundation4DataVYaF`.

  For better performance, frames can also be sent at a lower rate than the video;
  even as low as 1 frame per second.

  #### Declaration

  Swift

      public func sendVideoRealtime(_ video: Data, mimeType: String) async

  #### Parameters

  |---|---|
  | ` video ` | Encoded image data extracted from a frame of the video, used to update the model on the client's conversation. |
  | ` mimeType ` | The IANA standard MIME type of the video frame data (eg; `images/png`, `images/jpeg`etc.,). |

- `


  ### [sendTextRealtime(_:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession#/s:15FirebaseAILogic11LiveSessionC16sendTextRealtimeyySSYaF)


  ` Sends a text input stream to the model, using the realtime API.

  #### Declaration

  Swift

      public func sendTextRealtime(_ text: String) async

  #### Parameters

  |---|---|
  | ` text ` | Text content to append to the current client's conversation. |

- `


  ### [sendContent(_:turnComplete:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession#/s:15FirebaseAILogic11LiveSessionC11sendContent_12turnCompleteySayAA05ModelF0VG_SbtYaF)


  ` Incremental update of the current conversation.

  The content is unconditionally appended to the conversation history and used as part of the
  prompt to the model to generate content.

  Sending this message will also cause an interruption, if the server is actively generating
  content.

  #### Declaration

  Swift

      public func sendContent(_ content: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent.html], turnComplete: Bool = false) async

  #### Parameters

  |---|---|
  | ` content ` | Content to append to the current conversation with the model. |
  | ` turnComplete ` | Whether the server should start generating content with the currently accumulated prompt, or await additional messages before starting generation. By default, the server will await additional messages. |

- `


  ### [sendContent(_:turnComplete:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession#/s:15FirebaseAILogic11LiveSessionC11sendContent_12turnCompleteyAA18PartsRepresentable_pd_SbtYaF)


  ` Incremental update of the current conversation.

  The content is unconditionally appended to the conversation history and used as part of the
  prompt to the model to generate content.

  Sending this message will also cause an interruption, if the server is actively generating
  content.

  #### Declaration

  Swift

      public func sendContent(_ parts: any https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/PartsRepresentable.html...,
                              turnComplete: Bool = false) async

  #### Parameters

  |---|---|
  | ` content ` | Content to append to the current conversation with the model (see `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/PartsRepresentable.html` for conforming types). |
  | ` turnComplete ` | Whether the server should start generating content with the currently accumulated prompt, or await additional messages before starting generation. By default, the server will await additional messages. |

- `


  ### [close()](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveSession#/s:15FirebaseAILogic11LiveSessionC5closeyyYaF)


  ` Permanently stop the conversation with the model, and close the connection to the server

  This method will be called automatically when the `LiveSession` is deinitialized, but this
  method can be called manually to explicitly end the session.

  Attempting to receive content from a closed session will cause a
  `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveSessionUnexpectedClosureError.html` error to be thrown.

  #### Declaration

  Swift

      public func close() async