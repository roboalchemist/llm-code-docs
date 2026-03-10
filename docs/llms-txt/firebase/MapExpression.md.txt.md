# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MapExpression.md.txt

# FirebaseFirestore Framework Reference

# MapExpression

    public class MapExpression : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html, @unchecked Sendable

An expression that represents a map (or dictionary) of key-value pairs.

`MapExpression` is used to construct a map from a dictionary of `String` keys
and `Sendable` values. The values can be literals (like numbers and strings)
or other `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html` instances, allowing for the creation of dynamic nested
objects within a pipeline.

Example:

    MapExpression([
      "genre": Field("genre"),
      "rating": Field("rating").multiply(10),
      "nestedArray": ArrayExpression([Field("title")]),
      "nestedMap": MapExpression(["published": Field("published")]),
    ]).as("metadata")

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MapExpression#/s:17FirebaseFirestore13MapExpressionCyACSDySSs8Sendable_pGcfc)


  ` Undocumented

  #### Declaration

  Swift

      public init(_ elements: [String : Sendable])