# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Citation.md.txt

# FirebaseAILogic Framework Reference

# Citation

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct Citation : Sendable, Equatable

    extension Citation: Decodable

A struct describing a source attribution.
- `


  ### [startIndex](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Citation#/s:15FirebaseAILogic8CitationV10startIndexSivp)


  ` The inclusive beginning of a sequence in a model response that derives from a cited source.

  #### Declaration

  Swift

      public let startIndex: Int

- `


  ### [endIndex](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Citation#/s:15FirebaseAILogic8CitationV8endIndexSivp)


  ` The exclusive end of a sequence in a model response that derives from a cited source.

  #### Declaration

  Swift

      public let endIndex: Int

- `


  ### [uri](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Citation#/s:15FirebaseAILogic8CitationV3uriSSSgvp)


  ` A link to the cited source, if available.

  #### Declaration

  Swift

      public let uri: String?

- `


  ### [title](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Citation#/s:15FirebaseAILogic8CitationV5titleSSSgvp)


  ` The title of the cited source, if available.

  #### Declaration

  Swift

      public let title: String?

- `


  ### [license](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Citation#/s:15FirebaseAILogic8CitationV7licenseSSSgvp)


  ` The license the cited source work is distributed under, if specified.

  #### Declaration

  Swift

      public let license: String?

- `


  ### [publicationDate](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Citation#/s:15FirebaseAILogic8CitationV15publicationDate10Foundation0E10ComponentsVSgvp)


  ` The publication date of the cited source, if available.
  Tip

  `DateComponents` can be converted to a `Date` using the `date` computed property.

  #### Declaration

  Swift

      public let publicationDate: DateComponents?

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Citation#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Citation#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: any Decoder) throws