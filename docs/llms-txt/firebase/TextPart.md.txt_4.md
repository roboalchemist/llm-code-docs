# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/TextPart.md.txt

# FirebaseAILogic Framework Reference

# TextPart

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct TextPart : https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html

A text part containing a string value.
- `


  ### [text](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/TextPart#/s:15FirebaseAILogic8TextPartV4textSSvp)


  ` Text value.

  #### Declaration

  Swift

      public let text: String

- `


  ### [isThought](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/TextPart#/s:15FirebaseAILogic4PartP9isThoughtSbvp)


  `

  #### Declaration

  Swift

      public var isThought: Bool { get }

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/TextPart#/s:15FirebaseAILogic8TextPartVyACSScfc)


  ` Undocumented

  #### Declaration

  Swift

      public init(_ text: String)