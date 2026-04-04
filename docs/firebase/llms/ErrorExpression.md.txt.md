# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/ErrorExpression.md.txt

# FirebaseFirestore Framework Reference

# ErrorExpression

    public class ErrorExpression : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html, @unchecked Sendable

An expression that produces an error with a custom error message.
This is primarily used for debugging purposes.

Example:

    ErrorExpression("This is a custom error message").as("errorResult")

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/ErrorExpression#/s:17FirebaseFirestore15ErrorExpressionCyACSScfc)


  ` Undocumented

  #### Declaration

  Swift

      public init(_ errorMessage: String)