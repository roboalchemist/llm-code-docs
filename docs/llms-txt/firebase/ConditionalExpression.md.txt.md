# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/ConditionalExpression.md.txt

# FirebaseFirestore Framework Reference

# ConditionalExpression

    public class ConditionalExpression : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html, @unchecked Sendable

A `ConditionalExpression` is a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` that evaluates to one of two expressions
based on a boolean condition.

This is equivalent to a ternary operator (`condition ? then : else`).

Example of using `ConditionalExpression`:

    // Create a new field "status" based on the "rating" field.
    // If rating > 4.5, status is "top_rated", otherwise "regular".
    firestore.pipeline()
      .collection("products")
      .addFields([
        ConditionalExpression(
          Field("rating").greaterThan(4.5),
          then: Constant("top_rated"),
          else: Constant("regular")
        ).as("status")
      ])

- `


  ### [init(_:then:else:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/ConditionalExpression#/s:17FirebaseFirestore21ConditionalExpressionC_4then4elseAcA07BooleanD0_p_AA0D0_pAaG_ptcfc)


  ` Creates a new `ConditionalExpression`.

  #### Declaration

  Swift

      public init(_ expression: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html,
                  then thenExpression: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html,
                  else elseExpression: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html)

  #### Parameters

  |---|---|
  | ` expression ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` to evaluate. |
  | ` thenExpression ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html` to evaluate if the boolean expression is `true`. |
  | ` elseExpression ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html` to evaluate if the boolean expression is `false`. |