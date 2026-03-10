# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.md.txt

# FirebaseFirestore Framework Reference

# BooleanExpression

    public protocol BooleanExpression : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html

A `BooleanExpression` is an `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html` that evaluates to a boolean value.

It is used to construct conditional logic within Firestore pipelines, such as in `where`
clauses or `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/ConditionalExpression.html`. `BooleanExpression` instances can be combined using standard
logical operators (`&&`, `||`, `!`, `^`) to create complex conditions.

Example usage in a `where` clause:

    firestore.pipeline()
      .collection("products")
      .where(
        Field("price").greaterThan(100) &&
        (Field("category").equal("electronics") || Field("on_sale").equal(true))
      )

- `


  ### [countIf()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression#/s:17FirebaseFirestore17BooleanExpressionPAAE7countIfAA17AggregateFunctionCyF)


  ` Extension method Creates an aggregation that counts the number of documents for which this boolean expression
  evaluates to `true`.

  This is useful for counting documents that meet a specific condition without retrieving the
  documents themselves.

      // Count how many books were published after 1980
      let post1980Condition = Field("published").greaterThan(1980)
      firestore.pipeline()
        .collection("books")
        .aggregate([
          post1980Condition.countIf().as("modernBooksCount")
        ])

  #### Declaration

  Swift

      func countIf() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html

  #### Return Value

  An `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html` that performs the conditional count.
- `


  ### [then(_:else:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression#/s:17FirebaseFirestore17BooleanExpressionPAAE4then_4elseAA08FunctionD0CAA0D0_p_AaH_ptF)


  ` Extension method Creates a conditional expression that returns one of two specified expressions based on the
  result of this boolean expression.

  This is equivalent to a ternary operator (`condition ? then : else`).

      // Create a new field "status" based on the "rating" field.
      // If rating > 4.5, status is "top_rated", otherwise "regular".
      firestore.pipeline()
        .collection("products")
        .addFields([
          Field("rating").greaterThan(4.5)
            .then(Constant("top_rated"), else: Constant("regular"))
            .as("status")
        ])

  #### Declaration

  Swift

      func then(_ thenExpression: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html,
                else elseExpression: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` thenExpression ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html` to evaluate if this boolean expression is `true`. |
  | ` elseExpression ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html` to evaluate if this boolean expression is `false`. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the conditional logic.