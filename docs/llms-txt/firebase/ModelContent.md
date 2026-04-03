# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ModelContent.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModelContent.md.txt

# FirebaseVertexAI Framework Reference

# ModelContent

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct ModelContent : Equatable, Sendable

    extension ModelContent: Codable

A type describing data in media formats interpretable by an AI model. Each generative AI
request or response contains an `Array` of `ModelContent`s, and each `ModelContent` value
may comprise multiple heterogeneous [Part](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part.html)s.
- `
  ``
  ``
  `

  ### [role](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModelContent#/s:16FirebaseVertexAI12ModelContentV4roleSSSgvp)

  `
  `  
  The role of the entity creating the `ModelContent`. For user-generated client requests,
  for example, the role is `user`.  

  #### Declaration

  Swift  

      public let role: String?

- `
  ``
  ``
  `

  ### [parts](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModelContent#/s:16FirebaseVertexAI12ModelContentV5partsSayAA4Part_pGvp)

  `
  `  
  The data parts comprising this `ModelContent` value.  

  #### Declaration

  Swift  

      public var parts: [any https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part.html] { get }

- `
  ``
  ``
  `

  ### [init(role:parts:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModelContent#/s:16FirebaseVertexAI12ModelContentV4role5partsACSSSg_SayAA4Part_pGtcfc)

  `
  `  
  Creates a new value from a list of [Part](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part.html)s.  

  #### Declaration

  Swift  

      public init(role: String? = "user", parts: [any https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part.html])

- `
  ``
  ``
  `

  ### [init(role:parts:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModelContent#/s:16FirebaseVertexAI12ModelContentV4role5partsACSSSg_AA18PartsRepresentable_pdtcfc)

  `
  `  
  Creates a new value from any data interpretable as a [Part](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part.html).
  See [PartsRepresentable](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/PartsRepresentable.html) for types that can be interpreted as [Part](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part.html)s.  

  #### Declaration

  Swift  

      public init(role: String? = "user", parts: any https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/PartsRepresentable.html...)