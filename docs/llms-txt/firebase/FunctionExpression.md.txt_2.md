# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.md.txt

# FirebaseFirestore Framework Reference

# FunctionExpression

    public class FunctionExpression : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html, BridgeWrapper, @unchecked Sendable

Represents a function call in a pipeline.

A `FunctionExpression` is an expression that represents a function call with a given name and
arguments.

`FunctionExpression`s are typically used to perform operations on data in a pipeline, such as
mathematical calculations, string manipulations, or array operations.
- `


  ### [init(functionName:args:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression#/s:17FirebaseFirestore18FunctionExpressionC12functionName4argsACSS_SayAA0D0_pGtcfc)


  ` Creates a new `FunctionExpression`.

  #### Declaration

  Swift

      public init(functionName: String, args: [https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html])

  #### Parameters

  |---|---|
  | ` functionName ` | The name of the function. |
  | ` args ` | The arguments to the function. |