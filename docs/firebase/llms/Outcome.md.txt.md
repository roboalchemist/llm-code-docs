# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart/Outcome.md.txt

# FirebaseAILogic Framework Reference

# Outcome

    public struct Outcome : Sendable, Equatable, CustomStringConvertible

The outcome of a code execution.
- `


  ### [ok](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart/Outcome#/s:15FirebaseAILogic23CodeExecutionResultPartV7OutcomeV2okAEvpZ)


  ` The code executed without errors.

  #### Declaration

  Swift

      public static let ok: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart.html.Outcome

- `


  ### [failed](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart/Outcome#/s:15FirebaseAILogic23CodeExecutionResultPartV7OutcomeV6failedAEvpZ)


  ` The code failed to execute.

  #### Declaration

  Swift

      public static let failed: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart.html.Outcome

- `


  ### [deadlineExceeded](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart/Outcome#/s:15FirebaseAILogic23CodeExecutionResultPartV7OutcomeV16deadlineExceededAEvpZ)


  ` The code took too long to execute.

  #### Declaration

  Swift

      public static let deadlineExceeded: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart.html.Outcome

- `


  ### [description](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CodeExecutionResultPart/Outcome#/s:s23CustomStringConvertibleP11descriptionSSvp)


  `

  #### Declaration

  Swift

      public var description: String { get }