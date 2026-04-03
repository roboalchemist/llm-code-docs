# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/Chat.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Chat.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Chat.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Chat.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Chat.md.txt

# FirebaseAI Framework Reference

# Chat

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public final class Chat : Sendable

An object that represents a back-and-forth chat with a model, capturing the history and saving
the context in memory between each message sent.
- `
  ``
  ``
  `

  ### [history](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Chat#/s:10FirebaseAI4ChatC7historySayAA12ModelContentVGvp)

  `
  `  
  The previous content from the chat that has been successfully sent and received from the
  model. This will be provided to the model for each message sent as context for the discussion.  

  #### Declaration

  Swift  

      public var history: [https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ModelContent.html] { get set }

- `
  ``
  ``
  `

  ### [sendMessage(_:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Chat#/s:10FirebaseAI4ChatC11sendMessageyAA23GenerateContentResponseVAA18PartsRepresentable_pd_tYaKF)

  `
  `  
  Sends a message using the existing history of this chat as context. If successful, the message
  and response will be added to the history. If unsuccessful, history will remain unchanged.  
  Throws
  A [GenerateContentError](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/GenerateContentError.html) if an error occurred.  

  #### Declaration

  Swift  

      public func sendMessage(_ parts: any https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Protocols/PartsRepresentable.html...) async throws
        -> https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GenerateContentResponse.html

  #### Parameters

  |---------------|---------------------------------------------------|
  | ` `*parts*` ` | The new content to send as a single chat message. |

  #### Return Value

  The model's response if no error occurred.
- `
  ``
  ``
  `

  ### [sendMessage(_:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Chat#/s:10FirebaseAI4ChatC11sendMessageyAA23GenerateContentResponseVSayAA05ModelG0VGYaKF)

  `
  `  
  Sends a message using the existing history of this chat as context. If successful, the message
  and response will be added to the history. If unsuccessful, history will remain unchanged.  
  Throws
  A [GenerateContentError](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/GenerateContentError.html) if an error occurred.  

  #### Declaration

  Swift  

      public func sendMessage(_ content: [https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ModelContent.html]) async throws
        -> https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GenerateContentResponse.html

  #### Parameters

  |-----------------|---------------------------------------------------|
  | ` `*content*` ` | The new content to send as a single chat message. |

  #### Return Value

  The model's response if no error occurred.
- `
  ``
  ``
  `

  ### [sendMessageStream(_:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Chat#/s:10FirebaseAI4ChatC17sendMessageStreamyScsyAA23GenerateContentResponseVs5Error_pGAA18PartsRepresentable_pd_tKF)

  `
  `  
  Sends a message using the existing history of this chat as context. If successful, the message
  and response will be added to the history. If unsuccessful, history will remain unchanged.  

  #### Declaration

  Swift  

      @available(macOS 12.0, *)
      public func sendMessageStream(_ parts: any https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Protocols/PartsRepresentable.html...) throws
        -> AsyncThrowingStream<https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GenerateContentResponse.html, Error>

  #### Parameters

  |---------------|---------------------------------------------------|
  | ` `*parts*` ` | The new content to send as a single chat message. |

  #### Return Value

  A stream containing the model's response or an error if an error occurred.
- `
  ``
  ``
  `

  ### [sendMessageStream(_:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Chat#/s:10FirebaseAI4ChatC17sendMessageStreamyScsyAA23GenerateContentResponseVs5Error_pGSayAA05ModelH0VGKF)

  `
  `  
  Sends a message using the existing history of this chat as context. If successful, the message
  and response will be added to the history. If unsuccessful, history will remain unchanged.  

  #### Declaration

  Swift  

      @available(macOS 12.0, *)
      public func sendMessageStream(_ content: [https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ModelContent.html]) throws
        -> AsyncThrowingStream<https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GenerateContentResponse.html, Error>

  #### Parameters

  |-----------------|---------------------------------------------------|
  | ` `*content*` ` | The new content to send as a single chat message. |

  #### Return Value

  A stream containing the model's response or an error if an error occurred.