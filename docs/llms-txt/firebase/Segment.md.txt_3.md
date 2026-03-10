# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Segment.md.txt

# FirebaseAILogic Framework Reference

# Segment

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct Segment : Sendable, Equatable, Hashable

    extension Segment: Decodable

Represents a specific segment within a `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent.html` struct, often used to pinpoint the
exact location of text or data that grounding information refers to.
- `


  ### [partIndex](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Segment#/s:15FirebaseAILogic7SegmentV9partIndexSivp)


  ` The zero-based index of the `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html` object within the `parts` array of its parent
  `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent.html` object. This identifies which part of the content the segment belongs to.

  #### Declaration

  Swift

      public let partIndex: Int

- `


  ### [startIndex](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Segment#/s:15FirebaseAILogic7SegmentV10startIndexSivp)


  ` The zero-based start index of the segment within the specified `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html`, measured in UTF-8
  bytes. This offset is inclusive, starting from 0 at the beginning of the part's content.

  #### Declaration

  Swift

      public let startIndex: Int

- `


  ### [endIndex](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Segment#/s:15FirebaseAILogic7SegmentV8endIndexSivp)


  ` The zero-based end index of the segment within the specified `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html`, measured in UTF-8
  bytes. This offset is exclusive, meaning the character at this index is not included in the
  segment.

  #### Declaration

  Swift

      public let endIndex: Int

- `


  ### [text](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Segment#/s:15FirebaseAILogic7SegmentV4textSSvp)


  ` The text corresponding to the segment from the response.

  #### Declaration

  Swift

      public let text: String

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Segment#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Segment#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: Decoder) throws