# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent.md.txt

# FirebaseAILogic Framework Reference

# ModelContent

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct ModelContent : Equatable, Sendable

    extension ModelContent: Codable

A type describing data in media formats interpretable by an AI model. Each generative AI
request or response contains an `Array` of `ModelContent`s, and each `ModelContent` value
may comprise multiple heterogeneous `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html`s.
- `


  ### [role](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent#/s:15FirebaseAILogic12ModelContentV4roleSSSgvp)


  ` The role of the entity creating the `ModelContent`. For user-generated client requests,
  for example, the role is `user`.

  #### Declaration

  Swift

      public let role: String?

- `


  ### [parts](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent#/s:15FirebaseAILogic12ModelContentV5partsSayAA4Part_pGvp)


  ` The data parts comprising this `ModelContent` value.

  #### Declaration

  Swift

      public var parts: [any https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html] { get }

- `


  ### [init(role:parts:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent#/s:15FirebaseAILogic12ModelContentV4role5partsACSSSg_SayAA4Part_pGtcfc)


  ` Creates a new value from a list of `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html`s.

  #### Declaration

  Swift

      public init(role: String? = "user", parts: [any https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html])

- `


  ### [init(role:parts:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent#/s:15FirebaseAILogic12ModelContentV4role5partsACSSSg_AA18PartsRepresentable_pdtcfc)


  ` Creates a new value from any data interpretable as a `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html`.
  See `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/PartsRepresentable.html` for types that can be interpreted as `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html`s.

  #### Declaration

  Swift

      public init(role: String? = "user", parts: any https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/PartsRepresentable.html...)

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: any Decoder) throws