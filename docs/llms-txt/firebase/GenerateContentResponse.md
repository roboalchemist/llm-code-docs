# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GenerateContentResponse.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse.md.txt

# FirebaseVertexAI Framework Reference

# GenerateContentResponse

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct GenerateContentResponse : Sendable

    extension GenerateContentResponse: Decodable

The model's response to a generate content request.
- `
  ``
  ``
  `

  ### [UsageMetadata](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse/UsageMetadata.html)

  `
  `  
  Token usage metadata for processing the generate content request.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct UsageMetadata : Sendable

      extension https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse.html.UsageMetadata: Decodable

- `
  ``
  ``
  `

  ### [candidates](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse#/s:16FirebaseVertexAI23GenerateContentResponseV10candidatesSayAA9CandidateVGvp)

  `
  `  
  A list of candidate response content, ordered from best to worst.  

  #### Declaration

  Swift  

      public let candidates: [https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Candidate.html]

- `
  ``
  ``
  `

  ### [promptFeedback](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse#/s:16FirebaseVertexAI23GenerateContentResponseV14promptFeedbackAA06PromptH0VSgvp)

  `
  `  
  A value containing the safety ratings for the response, or, if the request was blocked, a
  reason for blocking the request.  

  #### Declaration

  Swift  

      public let promptFeedback: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback.html?

- `
  ``
  ``
  `

  ### [usageMetadata](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse#/s:16FirebaseVertexAI23GenerateContentResponseV13usageMetadataAC05UsageH0VSgvp)

  `
  `  
  Token usage metadata for processing the generate content request.  

  #### Declaration

  Swift  

      public let usageMetadata: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse/UsageMetadata.html?

- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse#/s:16FirebaseVertexAI23GenerateContentResponseV4textSSSgvp)

  `
  `  
  The response's content as text, if it exists.  

  #### Declaration

  Swift  

      public var text: String? { get }

- `
  ``
  ``
  `

  ### [functionCalls](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse#/s:16FirebaseVertexAI23GenerateContentResponseV13functionCallsSayAA16FunctionCallPartVGvp)

  `
  `  
  Returns function calls found in any [Part](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part.html)s of the first candidate of the response, if any.  

  #### Declaration

  Swift  

      public var functionCalls: [https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallPart.html] { get }

- `
  ``
  ``
  `

  ### [init(candidates:promptFeedback:usageMetadata:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse#/s:16FirebaseVertexAI23GenerateContentResponseV10candidates14promptFeedback13usageMetadataACSayAA9CandidateVG_AA06PromptI0VSgAC05UsageK0VSgtcfc)

  `
  `  
  Initializer for SwiftUI previews or tests.  

  #### Declaration

  Swift  

      public init(candidates: [https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Candidate.html], promptFeedback: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback.html? = nil,
                  usageMetadata: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse/UsageMetadata.html? = nil)

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse#/Codable-Conformances)

- `
  ``
  ``
  `

  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse#/s:Se4fromxs7Decoder_p_tKcfc)

  `
  `  

  #### Declaration

  Swift  

      public init(from decoder: Decoder) throws