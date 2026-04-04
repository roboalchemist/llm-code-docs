# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Functions.md.txt

# FirebaseFirestore Framework Reference

# Functions

The following functions are available globally.
- `


  ### [\&\&(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Functions#/s:17FirebaseFirestore2aaoiyAA17BooleanExpression_pAaC_p_AaC_pyKXKtKF)


  ` Combines two boolean expressions with a logical AND (`&&`).

  The resulting expression is `true` only if both the left-hand side (`lhs`) and the right-hand
  side (`rhs`) are `true`.

      // Find books in the "Fantasy" genre with a rating greater than 4.5
      firestore.pipeline()
        .collection("books")
        .where(
          Field("genre").equal("Fantasy") && Field("rating").greaterThan(4.5)
        )

  #### Declaration

  Swift

      public func && (lhs: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression,
                      rhs: @autoclosure () throws -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression) rethrows -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression

  #### Parameters

  |---|---|
  | ` lhs ` | The left-hand boolean expression. |
  | ` rhs ` | The right-hand boolean expression. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression` representing the logical AND.
- `


  ### [\|\|(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Functions#/s:17FirebaseFirestore2oooiyAA17BooleanExpression_pAaC_p_AaC_pyKXKtKF)


  ` Combines two boolean expressions with a logical OR (`||`).

  The resulting expression is `true` if either the left-hand side (`lhs`) or the right-hand
  side (`rhs`) is `true`.

      // Find books that are either in the "Romance" genre or were published before 1900
      firestore.pipeline()
        .collection("books")
        .where(
          Field("genre").equal("Romance") || Field("published").lessThan(1900)
        )

  #### Declaration

  Swift

      public func || (lhs: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression,
                      rhs: @autoclosure () throws -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression) rethrows -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression

  #### Parameters

  |---|---|
  | ` lhs ` | The left-hand boolean expression. |
  | ` rhs ` | The right-hand boolean expression. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression` representing the logical OR.
- `


  ### [\^(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Functions#/s:17FirebaseFirestore1xoiyAA17BooleanExpression_pAaC_p_AaC_pyKXKtKF)


  ` Combines two boolean expressions with a logical XOR (`^`).

  The resulting expression is `true` if the left-hand side (`lhs`) and the right-hand side
  (`rhs`) have different boolean values.

      // Find books that are in the "Dystopian" genre OR have a rating of 5.0, but not both.
      firestore.pipeline()
        .collection("books")
        .where(
          Field("genre").equal("Dystopian") ^ Field("rating").equal(5.0)
        )

  #### Declaration

  Swift

      public func ^ (lhs: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression,
                     rhs: @autoclosure () throws -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression) rethrows -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression

  #### Parameters

  |---|---|
  | ` lhs ` | The left-hand boolean expression. |
  | ` rhs ` | The right-hand boolean expression. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression` representing the logical XOR.
- `


  ### [!(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Functions#/s:17FirebaseFirestore1nopyAA17BooleanExpression_pAaC_pF)


  ` Negates a boolean expression with a logical NOT (`!`).

  The resulting expression is `true` if the original expression is `false`, and vice versa.

      // Find books that are NOT in the "Science Fiction" genre
      firestore.pipeline()
        .collection("books")
        .where(!Field("genre").equal("Science Fiction"))

  #### Declaration

  Swift

      public prefix func ! (lhs: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression

  #### Parameters

  |---|---|
  | ` lhs ` | The boolean expression to negate. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression` representing the logical NOT.