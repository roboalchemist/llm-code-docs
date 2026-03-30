# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ExecutableCodePart.md.txt

# FirebaseAILogic Framework Reference

# ExecutableCodePart

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct ExecutableCodePart : https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html

A part containing code that was executed by the model.
- `


  ### [Language](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ExecutableCodePart/Language.html)


  ` The language of the code in an `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ExecutableCodePart.html`.

  #### Declaration

  Swift

      public struct Language : Sendable, Equatable, CustomStringConvertible

- `


  ### [language](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ExecutableCodePart#/s:15FirebaseAILogic18ExecutableCodePartV8languageAC8LanguageVvp)


  ` The language of the code.

  #### Declaration

  Swift

      public var language: ExecutableCodePart.https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ExecutableCodePart/Language.html { get }

- `


  ### [code](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ExecutableCodePart#/s:15FirebaseAILogic18ExecutableCodePartV4codeSSvp)


  ` The code that was executed.

  #### Declaration

  Swift

      public var code: String { get }

- `


  ### [isThought](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ExecutableCodePart#/s:15FirebaseAILogic4PartP9isThoughtSbvp)


  `

  #### Declaration

  Swift

      public var isThought: Bool { get }

- `


  ### [init(language:code:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ExecutableCodePart#/s:15FirebaseAILogic18ExecutableCodePartV8language4codeA2C8LanguageV_SStcfc)


  ` Undocumented

  #### Declaration

  Swift

      public init(language: ExecutableCodePart.https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ExecutableCodePart/Language.html, code: String)