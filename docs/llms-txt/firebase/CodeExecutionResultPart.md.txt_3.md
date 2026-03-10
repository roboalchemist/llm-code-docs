# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart.md.txt

# FirebaseAILogic Framework Reference

# CodeExecutionResultPart

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct CodeExecutionResultPart : https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html

The result of executing code.
- `


  ### [Outcome](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart/Outcome.html)


  ` The outcome of a code execution.

  #### Declaration

  Swift

      public struct Outcome : Sendable, Equatable, CustomStringConvertible

- `


  ### [outcome](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart#/s:15FirebaseAILogic23CodeExecutionResultPartV7outcomeAC7OutcomeVvp)


  ` The outcome of the code execution.

  #### Declaration

  Swift

      public var outcome: CodeExecutionResultPart.https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart/Outcome.html { get }

- `


  ### [output](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart#/s:15FirebaseAILogic23CodeExecutionResultPartV6outputSSSgvp)


  ` The output of the code execution.

  #### Declaration

  Swift

      public var output: String? { get }

- `


  ### [isThought](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart#/s:15FirebaseAILogic4PartP9isThoughtSbvp)


  `

  #### Declaration

  Swift

      public var isThought: Bool { get }

- `


  ### [init(outcome:output:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart#/s:15FirebaseAILogic23CodeExecutionResultPartV7outcome6outputA2C7OutcomeV_SStcfc)


  ` Undocumented

  #### Declaration

  Swift

      public init(outcome: CodeExecutionResultPart.https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart/Outcome.html, output: String)