# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/ArrayExpression.md.txt

# FirebaseFirestore Framework Reference

# ArrayExpression

    public class ArrayExpression : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html, @unchecked Sendable

An expression that represents an array of values.

`ArrayExpression` is used to construct an array from a list of `Sendable`
values, which can include literals (like numbers and strings) as well as other
`https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html` instances. This allows for the creation of dynamic arrays within
a pipeline.

Example:

    ArrayExpression([
      1,
      2,
      Field("genre"),
      Field("rating").multiply(10),
      ArrayExpression([Field("title")]),
      MapExpression(["published": Field("published")]),
    ]).as("metadataArray")

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/ArrayExpression#/s:17FirebaseFirestore15ArrayExpressionCyACSays8Sendable_pGcfc)


  ` Undocumented

  #### Declaration

  Swift

      public init(_ elements: [Sendable])