# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Enums/GenerateContentError.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/GenerateContentError.md.txt

# FirebaseAI Framework Reference

# GenerateContentError

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public enum GenerateContentError : Error

Errors that occur when generating content from a model.
- `
  ``
  ``
  `

  ### [internalError(underlying:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/GenerateContentError#/s:10FirebaseAI20GenerateContentErrorO08internalE0yACs0E0_p_tcACmF)

  `
  `  
  An internal error occurred. See the underlying error for more context.  

  #### Declaration

  Swift  

      case internalError(underlying: Error)

- `
  ``
  ``
  `

  ### [promptImageContentError(underlying:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/GenerateContentError#/s:10FirebaseAI20GenerateContentErrorO011promptImagedE0yACs0E0_p_tcACmF)

  `
  `  
  An error occurred when constructing the prompt. Examine the related error for details.  

  #### Declaration

  Swift  

      case promptImageContentError(underlying: Error)

- `
  ``
  ``
  `

  ### [promptBlocked(response:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/GenerateContentError#/s:10FirebaseAI20GenerateContentErrorO13promptBlockedyAcA0cD8ResponseV_tcACmF)

  `
  `  
  A prompt was blocked. See the response's `promptFeedback.blockReason` for more information.  

  #### Declaration

  Swift  

      case promptBlocked(response: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GenerateContentResponse.html)

- `
  ``
  ``
  `

  ### [responseStoppedEarly(reason:response:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/GenerateContentError#/s:10FirebaseAI20GenerateContentErrorO20responseStoppedEarlyyAcA12FinishReasonV_AA0cD8ResponseVtcACmF)

  `
  `  
  A response didn't fully complete. See the [FinishReason](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FinishReason.html) for more information.  

  #### Declaration

  Swift  

      case responseStoppedEarly(reason: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FinishReason.html, response: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GenerateContentResponse.html)