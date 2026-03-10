# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.md.txt

# FirebaseFirestore Framework Reference

# Expression

    public protocol Expression : Sendable

Undocumented
- `


  ### [asBoolean()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP9asBooleanAA0eC0_pyF)


  ` Default implementation Casts the expression to a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html`.

  #### Default Implementation

  #### Declaration

  Swift

      func asBoolean() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` representing the same expression.
- `


  ### [as(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP2asyAA07AliasedC0VSSF)


  ` Default implementation Assigns an alias to this expression.

  Aliases are useful for renaming fields in the output of a stage or for giving meaningful
  names to calculated values.

      // Calculate total price and alias it "totalPrice"
      Field("price").multiply(Field("quantity")).as("totalPrice")

  #### Default Implementation

  #### Declaration

  Swift

      func `as`(_ name: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs.html#/s:17FirebaseFirestore17AliasedExpressionV

  #### Parameters

  |---|---|
  | ` name ` | The alias to assign to this expression. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs.html#/s:17FirebaseFirestore17AliasedExpressionV` wrapping this expression with the alias.
- `


  ### [round()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP5roundAA08FunctionC0CyF)


  ` Default implementation Creates an expression that returns the value of self rounded to the nearest integer.

      // Get the value of the "amount" field rounded to the nearest integer.
      Field("amount").round()

  #### Default Implementation

  #### Declaration

  Swift

      func round() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the rounded number.
- `


  ### [sqrt()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP4sqrtAA08FunctionC0CyF)


  ` Default implementation Creates an expression that returns the square root of self.

      // Get the square root of the "area" field.
      Field("area").sqrt()

  #### Default Implementation

  #### Declaration

  Swift

      func sqrt() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the square root of the number.
- `


  ### [pow(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP3powyAA08FunctionC0Cs8Sendable_pF)


  ` Default implementation Creates an expression that returns the value of self raised to the power of self.

  Returns zero on underflow.

      // Get the value of the "amount" field raised to the power of 2.
      Field("amount").pow(2)

  #### Default Implementation

  #### Declaration

  Swift

      func pow(_ exponent: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` exponent ` | The exponent to raise self to. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the power of the number.
- `


  ### [pow(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP3powyAA08FunctionC0CAaB_pF)


  ` Default implementation Creates an expression that returns the value of self raised to the power of self.

  Returns zero on underflow.

      // Get the value of the "amount" field raised to the power of the "exponent" field.
      Field("amount").pow(Field("exponent"))

  #### Default Implementation

  #### Declaration

  Swift

      func pow(_ exponent: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` exponent ` | The exponent to raise self to. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the power of the number.
- `


  ### [ln()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP2lnAA08FunctionC0CyF)


  ` Default implementation Creates an expression that returns the natural logarithm of self.

      // Get the natural logarithm of the "amount" field.
      Field("amount").ln()

  #### Default Implementation

  #### Declaration

  Swift

      func ln() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the natural logarithm of the number.
- `


  ### [floor()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP5floorAA08FunctionC0CyF)


  ` Default implementation Creates an expression that returns the largest numeric value that isn't greater than self.

      // Get the floor of the "amount" field.
      Field("amount").floor()

  #### Default Implementation

  #### Declaration

  Swift

      func floor() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the floor of the number.
- `


  ### [exp()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP3expAA08FunctionC0CyF)


  ` Default implementation Creates an expression that returns e to the power of self.

  Returns zero on underflow and nil on overflow.

      // Get the exp of the "amount" field.
      Field("amount").exp()

  #### Default Implementation

  #### Declaration

  Swift

      func exp() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the exp of the number.
- `


  ### [ceil()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP4ceilAA08FunctionC0CyF)


  ` Default implementation Creates an expression that returns the smallest numeric value that isn't less than the number.

      // Get the ceiling of the "amount" field.
      Field("amount").ceil()

  #### Default Implementation

  #### Declaration

  Swift

      func ceil() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the ceiling of the number.
- `


  ### [abs()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP3absAA08FunctionC0CyF)


  ` Default implementation Creates an expression that returns the absolute value of the number.

      // Get the absolute value of the "amount" field.
      Field("amount").abs()

  #### Default Implementation

  #### Declaration

  Swift

      func abs() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the absolute value of the number.
- `


  ### [add(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP3addyAA08FunctionC0CAaB_pF)


  ` Default implementation Creates an expression that adds another expression to this expression.
  To add multiple expressions, chain calls to this method.
  Assumes `self` and the parameter evaluate to compatible types for addition (e.g., numbers, or
  string/array concatenation if supported by the specific "add" implementation).

      // Add the value of the "quantity" field and the "reserve" field.
      Field("quantity").add(Field("reserve"))

      // Add multiple numeric fields
      Field("subtotal").add(Field("tax")).add(Field("shipping"))

  #### Default Implementation

  #### Declaration

  Swift

      func add(_ value: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` value ` | An `Expression` to add. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the addition operation.
- `


  ### [add(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP3addyAA08FunctionC0Cs8Sendable_pF)


  ` Default implementation Creates an expression that adds a literal value to this expression.
  To add multiple literals, chain calls to this method.
  Assumes `self` and the parameter evaluate to compatible types for addition.

      // Add 5 to the "count" field
      Field("count").add(5)

      // Add multiple literal numbers
      Field("score").add(10).add(20).add(-5)

  #### Default Implementation

  #### Declaration

  Swift

      func add(_ value: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` value ` | A `Sendable` literal value to add. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the addition operation.
- `


  ### [subtract(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8subtractyAA08FunctionC0CAaB_pF)


  ` Default implementation Creates an expression that subtracts another expression from this expression.
  Assumes `self` and `other` evaluate to numeric types.

      // Subtract the "discount" field from the "price" field
      Field("price").subtract(Field("discount"))

  #### Default Implementation

  #### Declaration

  Swift

      func subtract(_ other: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The `Expression` (evaluating to a number) to subtract from this expression. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the subtraction operation.
- `


  ### [subtract(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8subtractyAA08FunctionC0Cs8Sendable_pF)


  ` Default implementation Creates an expression that subtracts a literal value from this expression.
  Assumes `self` evaluates to a numeric type.

      // Subtract 20 from the value of the "total" field
      Field("total").subtract(20)

  #### Default Implementation

  #### Declaration

  Swift

      func subtract(_ other: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The `Sendable` literal (numeric) value to subtract from this expression. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the subtraction operation.
- `


  ### [multiply(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8multiplyyAA08FunctionC0CAaB_pF)


  ` Default implementation Creates an expression that multiplies this expression by another expression.
  To multiply multiple expressions, chain calls to this method.
  Assumes `self` and the parameter evaluate to numeric types.

      // Multiply the "quantity" field by the "price" field
      Field("quantity").multiply(Field("price"))

      // Multiply "rate" by "time" and "conversionFactor" fields
      Field("rate").multiply(Field("time")).multiply(Field("conversionFactor"))

  #### Default Implementation

  #### Declaration

  Swift

      func multiply(_ value: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` value ` | An `Expression` to multiply by. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the multiplication operation.
- `


  ### [multiply(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8multiplyyAA08FunctionC0Cs8Sendable_pF)


  ` Default implementation Creates an expression that multiplies this expression by a literal value.
  To multiply multiple literals, chain calls to this method.
  Assumes `self` evaluates to a numeric type.

      // Multiply the "score" by 1.1
      Field("score").multiply(1.1)

      // Multiply "base" by 2 and then by 3.0
      Field("base").multiply(2).multiply(3.0)

  #### Default Implementation

  #### Declaration

  Swift

      func multiply(_ value: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` value ` | A `Sendable` literal value to multiply by. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the multiplication operation.
- `


  ### [divide(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP6divideyAA08FunctionC0CAaB_pF)


  ` Default implementation Creates an expression that divides this expression by another expression.
  Assumes `self` and `other` evaluate to numeric types.

      // Divide the "total" field by the "count" field
      Field("total").divide(Field("count"))

  #### Default Implementation

  #### Declaration

  Swift

      func divide(_ other: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The `Expression` (evaluating to a number) to divide by. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the division operation.
- `


  ### [divide(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP6divideyAA08FunctionC0Cs8Sendable_pF)


  ` Default implementation Creates an expression that divides this expression by a literal value.
  Assumes `self` evaluates to a numeric type.

      // Divide the "value" field by 10
      Field("value").divide(10)

  #### Default Implementation

  #### Declaration

  Swift

      func divide(_ other: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The `Sendable` literal (numeric) value to divide by. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the division operation.
- `


  ### [mod(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP3modyAA08FunctionC0CAaB_pF)


  ` Default implementation Creates an expression that calculates the modulo (remainder) of dividing this expression by
  another expression.
  Assumes `self` and `other` evaluate to numeric types.

      // Calculate the remainder of dividing the "value" field by the "divisor" field
      Field("value").mod(Field("divisor"))

  #### Default Implementation

  #### Declaration

  Swift

      func mod(_ other: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The `Expression` (evaluating to a number) to use as the divisor. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the modulo operation.
- `


  ### [mod(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP3modyAA08FunctionC0Cs8Sendable_pF)


  ` Default implementation Creates an expression that calculates the modulo (remainder) of dividing this expression by a
  literal value.
  Assumes `self` evaluates to a numeric type.

      // Calculate the remainder of dividing the "value" field by 10
      Field("value").mod(10)

  #### Default Implementation

  #### Declaration

  Swift

      func mod(_ other: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The `Sendable` literal (numeric) value to use as the divisor. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the modulo operation.
- `


  ### [arrayReverse()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP12arrayReverseAA08FunctionC0CyF)


  ` Default implementation Creates an expression that returns the `input` with elements in reverse order.

      // Reverse the "tags" array.
      Field("tags").arrayReverse()

  #### Default Implementation

  #### Declaration

  Swift

      func arrayReverse() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the reversed array.
- `


  ### [arrayConcat(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP11arrayConcatyAA08FunctionC0CSayAaB_pGF)


  ` Default implementation Creates an expression that concatenates an array expression (from `self`) with one or more
  other array expressions.
  Assumes `self` and all parameters evaluate to arrays.

      // Combine the "items" array with "otherItems" and "archiveItems" array fields.
      Field("items").arrayConcat(Field("otherItems"), Field("archiveItems"))

  #### Default Implementation

  #### Declaration

  Swift

      func arrayConcat(_ arrays: [Expression]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` arrays ` | An array of at least one `Expression` (evaluating to an array) to concatenate. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the concatenated array.
- `


  ### [arrayConcat(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP11arrayConcatyAA08FunctionC0CSaySays8Sendable_pGGF)


  ` Default implementation Creates an expression that concatenates an array expression (from `self`) with one or more
  array literals.
  Assumes `self` evaluates to an array.

      // Combine "tags" (an array field) with ["new", "featured"] and ["urgent"]
      Field("tags").arrayConcat(["new", "featured"], ["urgent"])

  #### Default Implementation

  #### Declaration

  Swift

      func arrayConcat(_ arrays: [[Sendable]]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` arrays ` | An array of at least one `Sendable` values to concatenate. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the concatenated array.
- `


  ### [arrayContains(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP13arrayContainsyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates an expression that checks if an array (from `self`) contains a specific element
  expression.
  Assumes `self` evaluates to an array.

      // Check if "sizes" contains the value from "selectedSize" field
      Field("sizes").arrayContains(Field("selectedSize"))

  #### Default Implementation

  #### Declaration

  Swift

      func arrayContains(_ element: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` element ` | The `Expression` representing the element to search for in the array. |

  #### Return Value

  A new `BooleanExpr` representing the "array_contains" comparison.
- `


  ### [arrayContains(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP13arrayContainsyAA07BooleanC0_ps8Sendable_pF)


  ` Default implementation Creates an expression that checks if an array (from `self`) contains a specific literal
  element.
  Assumes `self` evaluates to an array.

      // Check if "colors" array contains "red"
      Field("colors").arrayContains("red")

  #### Default Implementation

  #### Declaration

  Swift

      func arrayContains(_ element: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` element ` | The `Sendable` literal element to search for in the array. |

  #### Return Value

  A new `BooleanExpr` representing the "array_contains" comparison.
- `


  ### [arrayContainsAll(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP16arrayContainsAllyAA07BooleanC0_pSayAaB_pGF)


  ` Default implementation Creates an expression that checks if an array (from `self`) contains all the specified element
  expressions.
  Assumes `self` evaluates to an array.

      // Check if "candidateSkills" contains all skills from "requiredSkill1" and "requiredSkill2"
      fields
      Field("candidateSkills").arrayContainsAll([Field("requiredSkill1"), Field("requiredSkill2")])

  #### Default Implementation

  #### Declaration

  Swift

      func arrayContainsAll(_ values: [Expression]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` values ` | A list of `Expression` elements to check for in the array represented by `self`. |

  #### Return Value

  A new `BooleanExpr` representing the "array_contains_all" comparison.
- `


  ### [arrayContainsAll(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP16arrayContainsAllyAA07BooleanC0_pSays8Sendable_pGF)


  ` Default implementation Creates an expression that checks if an array (from `self`) contains all the specified literal
  elements.
  Assumes `self` evaluates to an array.

      // Check if "tags" contains both "urgent" and "review"
      Field("tags").arrayContainsAll(["urgent", "review"])

  #### Default Implementation

  #### Declaration

  Swift

      func arrayContainsAll(_ values: [Sendable]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` values ` | An array of at least one `Sendable` element to check for in the array. |

  #### Return Value

  A new `BooleanExpr` representing the "array_contains_all" comparison.
- `


  ### [arrayContainsAll(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP16arrayContainsAllyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates an expression that checks if an array (from `self`) contains all the specified element
  expressions.
  Assumes `self` evaluates to an array.

      // Check if the "tags" array contains "foo", "bar", and "baz"
      Field("tags").arrayContainsAll(Constant(["foo", "bar", "baz"]))

  #### Default Implementation

  #### Declaration

  Swift

      func arrayContainsAll(_ arrayExpression: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` values ` | An `Expression` elements evaluated to be array. |

  #### Return Value

  A new `BooleanExpr` representing the "array_contains_all" comparison.
- `


  ### [arrayContainsAny(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP16arrayContainsAnyyAA07BooleanC0_pSayAaB_pGF)


  ` Default implementation Creates an expression that checks if an array (from `self`) contains any of the specified
  element expressions.
  Assumes `self` evaluates to an array.

      // Check if "userGroups" contains any group from "allowedGroup1" or "allowedGroup2" fields
      Field("userGroups").arrayContainsAny([Field("allowedGroup1"), Field("allowedGroup2")])

  #### Default Implementation

  #### Declaration

  Swift

      func arrayContainsAny(_ values: [Expression]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` values ` | A list of `Expression` elements to check for in the array. |

  #### Return Value

  A new `BooleanExpr` representing the "array_contains_any" comparison.
- `


  ### [arrayContainsAny(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP16arrayContainsAnyyAA07BooleanC0_pSays8Sendable_pGF)


  ` Default implementation Creates an expression that checks if an array (from `self`) contains any of the specified
  literal elements.
  Assumes `self` evaluates to an array.

      // Check if "categories" contains either "electronics" or "books"
      Field("categories").arrayContainsAny(["electronics", "books"])

  #### Default Implementation

  #### Declaration

  Swift

      func arrayContainsAny(_ values: [Sendable]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` values ` | An array of at least one `Sendable` element to check for in the array. |

  #### Return Value

  A new `BooleanExpr` representing the "array_contains_any" comparison.
- `


  ### [arrayContainsAny(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP16arrayContainsAnyyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates an expression that checks if an array (from `self`) contains any of the specified
  element expressions.
  Assumes `self` evaluates to an array.

      // Check if "groups" array contains any of the values from the "userGroup" field
      Field("groups").arrayContainsAny(Field("userGroup"))

  #### Default Implementation

  #### Declaration

  Swift

      func arrayContainsAny(_ arrayExpression: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` arrayExpression ` | An `Expression` elements evaluated to be array. |

  #### Return Value

  A new `BooleanExpr` representing the "array_contains_any" comparison.
- `


  ### [arrayLength()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP11arrayLengthAA08FunctionC0CyF)


  ` Default implementation Creates an expression that calculates the length of an array.
  Assumes `self` evaluates to an array.

      // Get the number of items in the "cart" array
      Field("cart").arrayLength()

  #### Default Implementation

  #### Declaration

  Swift

      func arrayLength() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the length of the array.
- `


  ### [arrayGet(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8arrayGetyAA08FunctionC0CSiF)


  ` Default implementation Creates an expression that accesses an element in an array (from `self`) at the specified
  integer offset.
  A negative offset starts from the end. If the offset is out of bounds, an error may be
  returned during evaluation.
  Assumes `self` evaluates to an array.

      // Return the value in the "tags" field array at index 1.
      Field("tags").arrayGet(1)
      // Return the last element in the "tags" field array.
      Field("tags").arrayGet(-1)

  #### Default Implementation

  #### Declaration

  Swift

      func arrayGet(_ offset: Int) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` offset ` | The literal `Int` offset of the element to return. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the "arrayGet" operation.
- `


  ### [arrayGet(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8arrayGetyAA08FunctionC0CAaB_pF)


  ` Default implementation Creates an expression that accesses an element in an array (from `self`) at the offset
  specified by an expression.
  A negative offset starts from the end. If the offset is out of bounds, an error may be
  returned during evaluation.
  Assumes `self` evaluates to an array and `offsetExpr` evaluates to an integer.

      // Return the value in the tags field array at index specified by field "favoriteTagIndex".
      Field("tags").arrayGet(Field("favoriteTagIndex"))

  #### Default Implementation

  #### Declaration

  Swift

      func arrayGet(_ offsetExpression: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` offsetExpression ` | An `Expression` (evaluating to an Int) representing the offset of the element to return. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the "arrayGet" operation.
- `


  ### [arrayMaximum()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP12arrayMaximumAA08FunctionC0CyF)


  ` Default implementation Creates an expression that returns the maximum element of an array.

  Assumes `self` evaluates to an array.

      // Get the maximum value in the "scores" array.
      Field("scores").arrayMaximum()

  #### Default Implementation

  #### Declaration

  Swift

      func arrayMaximum() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the maximum element of the array.
- `


  ### [arrayMinimum()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP12arrayMinimumAA08FunctionC0CyF)


  ` Default implementation Creates an expression that returns the minimum element of an array.

  Assumes `self` evaluates to an array.

      // Get the minimum value in the "scores" array.
      Field("scores").arrayMinimum()

  #### Default Implementation

  #### Declaration

  Swift

      func arrayMinimum() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the minimum element of the array.
- `


  ### [greaterThan(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP11greaterThanyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that returns `true` if this expression is greater
  than the given expression.

  #### Default Implementation

  #### Declaration

  Swift

      func greaterThan(_ other: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The expression to compare against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [greaterThan(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP11greaterThanyAA07BooleanC0_ps8Sendable_pF)


  ` Default implementation Creates a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that returns `true` if this expression is greater
  than the given value.

  #### Default Implementation

  #### Declaration

  Swift

      func greaterThan(_ other: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The value to compare against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [greaterThanOrEqual(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP18greaterThanOrEqualyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that returns `true` if this expression is
  greater than or equal to the given expression.

  #### Default Implementation

  #### Declaration

  Swift

      func greaterThanOrEqual(_ other: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The expression to compare against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [greaterThanOrEqual(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP18greaterThanOrEqualyAA07BooleanC0_ps8Sendable_pF)


  ` Default implementation Creates a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that returns `true` if this expression is
  greater than or equal to the given value.

  #### Default Implementation

  #### Declaration

  Swift

      func greaterThanOrEqual(_ other: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The value to compare against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [lessThan(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8lessThanyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that returns `true` if this expression is less
  than the given expression.

  #### Default Implementation

  #### Declaration

  Swift

      func lessThan(_ other: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The expression to compare against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [lessThan(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8lessThanyAA07BooleanC0_ps8Sendable_pF)


  ` Default implementation Creates a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that returns `true` if this expression is less
  than the given value.

  #### Default Implementation

  #### Declaration

  Swift

      func lessThan(_ other: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The value to compare against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [lessThanOrEqual(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP15lessThanOrEqualyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that returns `true` if this expression is less
  than or equal to the given expression.

  #### Default Implementation

  #### Declaration

  Swift

      func lessThanOrEqual(_ other: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The expression to compare against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [lessThanOrEqual(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP15lessThanOrEqualyAA07BooleanC0_ps8Sendable_pF)


  ` Default implementation Creates a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that returns `true` if this expression is less
  than or equal to the given value.

  #### Default Implementation

  #### Declaration

  Swift

      func lessThanOrEqual(_ other: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The value to compare against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [equal(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP5equalyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that returns `true` if this expression is equal
  to the given expression.

  #### Default Implementation

  #### Declaration

  Swift

      func equal(_ other: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The expression to compare against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [equal(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP5equalyAA07BooleanC0_ps8Sendable_pF)


  ` Default implementation Creates a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that returns `true` if this expression is equal
  to the given value.

  #### Default Implementation

  #### Declaration

  Swift

      func equal(_ other: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The value to compare against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [notEqual(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8notEqualyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that returns `true` if this expression is not
  equal to the given expression.

  #### Default Implementation

  #### Declaration

  Swift

      func notEqual(_ other: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The expression to compare against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [notEqual(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8notEqualyAA07BooleanC0_ps8Sendable_pF)


  ` Default implementation Creates a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that returns `true` if this expression is not
  equal to the given value.

  #### Default Implementation

  #### Declaration

  Swift

      func notEqual(_ other: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` other ` | The value to compare against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [equalAny(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8equalAnyyAA07BooleanC0_pSayAaB_pGF)


  ` Default implementation Creates an expression that checks if this expression is equal to any of the provided
  expression values.

      // Check if "categoryID" field is equal to "featuredCategory" or "popularCategory" fields
      Field("categoryID").equalAny([Field("featuredCategory"), Field("popularCategory")])

  #### Default Implementation

  #### Declaration

  Swift

      func equalAny(_ others: [Expression]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` others ` | An array of at least one `Expression` value to check against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [equalAny(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8equalAnyyAA07BooleanC0_pSays8Sendable_pGF)


  ` Default implementation Creates an expression that checks if this expression is equal to any of the provided literal
  values.

      // Check if "category" is "Electronics", "Books", or "Home Goods"
      Field("category").equalAny(["Electronics", "Books", "Home Goods"])

  #### Default Implementation

  #### Declaration

  Swift

      func equalAny(_ others: [Sendable]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` others ` | An array of at least one `Sendable` literal value to check against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [equalAny(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8equalAnyyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates an expression that checks if this expression is equal to any of the provided
  expression values.

      // Check if "categoryID" field is equal to any of "categoryIDs" fields
      Field("categoryID").equalAny(Field("categoryIDs"))

  #### Default Implementation

  #### Declaration

  Swift

      func equalAny(_ arrayExpression: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` arrayExpression ` | An `Expression` elements evaluated to be array. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [notEqualAny(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP11notEqualAnyyAA07BooleanC0_pSayAaB_pGF)


  ` Default implementation Creates an expression that checks if this expression is not equal to any of the provided
  expression values.

      // Check if "statusValue" is not equal to "archivedStatus" or "deletedStatus" fields
      Field("statusValue").notEqualAny([Field("archivedStatus"), Field("deletedStatus")])

  #### Default Implementation

  #### Declaration

  Swift

      func notEqualAny(_ others: [Expression]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` others ` | An array of at least one `Expression` value to check against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [notEqualAny(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP11notEqualAnyyAA07BooleanC0_pSays8Sendable_pGF)


  ` Default implementation Creates an expression that checks if this expression is not equal to any of the provided
  literal values.

      // Check if "status" is neither "pending" nor "archived"
      Field("status").notEqualAny(["pending", "archived"])

  #### Default Implementation

  #### Declaration

  Swift

      func notEqualAny(_ others: [Sendable]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` others ` | An array of at least one `Sendable` literal value to check against. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [notEqualAny(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP11notEqualAnyyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates an expression that checks if this expression is equal to any of the provided
  expression values.

      // Check if "categoryID" field is not equal to any of "categoryIDs" fields
      Field("categoryID").equalAny(Field("categoryIDs"))

  #### Default Implementation

  #### Declaration

  Swift

      func notEqualAny(_ arrayExpression: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` arrayExpression ` | An `Expression` elements evaluated to be array. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` that can be used in a where stage, together with other
  boolean expressions.
- `


  ### [exists()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP6existsAA07BooleanC0_pyF)


  ` Default implementation Creates an expression that checks if a field exists in the document.

      // Check if the document has a field named "phoneNumber"
      Field("phoneNumber").exists()

  #### Default Implementation

  #### Declaration

  Swift

      func exists() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` representing the "exists" check.
- `


  ### [isError()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP7isErrorAA07BooleanC0_pyF)


  ` Default implementation Creates an expression that checks if this expression produces an error during evaluation.

      // Check if accessing a non-existent array index causes an error
      Field("myArray").arrayGet(100).isError()

  #### Default Implementation

  #### Declaration

  Swift

      func isError() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` representing the "isError" check.
- `


  ### [isAbsent()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8isAbsentAA07BooleanC0_pyF)


  ` Default implementation Creates an expression that returns `true` if the result of this expression
  is absent (e.g., a field does not exist in a map). Otherwise, returns `false`.

      // Check if the field `value` is absent.
      Field("value").isAbsent()

  #### Default Implementation

  #### Declaration

  Swift

      func isAbsent() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` representing the "isAbsent" check.
[## String Operations](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/String-Operations)

- `


  ### [join(delimiter:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP4join9delimiterAA08FunctionC0CSS_tF)


  ` Default implementation Creates an expression that joins the elements of an array of strings with a given separator.

  Assumes `self` evaluates to an array of strings.

      // Join the "tags" array with a ", " separator.
      Field("tags").join(separator: ", ")

  #### Default Implementation

  #### Declaration

  Swift

      func join(delimiter: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` delimiter ` | The string to use as a delimiter. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the joined string.
- `


  ### [split(delimiter:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP5split9delimiterAA08FunctionC0CSS_tF)


  ` Default implementation Creates an expression that splits a string into an array of substrings based on a delimiter.

  #### Default Implementation

  #### Declaration

  Swift

      func split(delimiter: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` delimiter ` | The string to split on. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the array of substrings.
- `


  ### [split(delimiter:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP5split9delimiterAA08FunctionC0CAaB_p_tF)


  ` Default implementation Creates an expression that splits a string into an array of substrings based on a delimiter.

  #### Default Implementation

  #### Declaration

  Swift

      func split(delimiter: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` delimiter ` | An expression that evaluates to a string or bytes to split on. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the array of substrings.
- `


  ### [length()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP6lengthAA08FunctionC0CyF)


  ` Default implementation Creates an expression that returns the length of a string.

      // Get the length of the "name" field.
      Field("name").length()

  #### Default Implementation

  #### Declaration

  Swift

      func length() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the length of the string.
- `


  ### [charLength()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP10charLengthAA08FunctionC0CyF)


  ` Default implementation Creates an expression that calculates the character length of a string in UTF-8.
  Assumes `self` evaluates to a string.

      // Get the character length of the "name" field in its UTF-8 form.
      Field("name").charLength()

  #### Default Implementation

  #### Declaration

  Swift

      func charLength() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the length of the string.
- `


  ### [like(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP4likeyAA07BooleanC0_pSSF)


  ` Default implementation Creates an expression that performs a case-sensitive string comparison using wildcards against
  a literal pattern.
  Assumes `self` evaluates to a string.

      // Check if the "title" field contains the word "guide" (case-sensitive)
      Field("title").like("%guide%")

  #### Default Implementation

  #### Declaration

  Swift

      func like(_ pattern: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` pattern ` | The literal string pattern to search for. Use "%" as a wildcard. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` representing the "like" comparison.
- `


  ### [like(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP4likeyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates an expression that performs a case-sensitive string comparison using wildcards against
  an expression pattern.
  Assumes `self` evaluates to a string, and `pattern` evaluates to a string.

      // Check if "filename" matches a pattern stored in "patternField"
      Field("filename").like(Field("patternField"))

  #### Default Implementation

  #### Declaration

  Swift

      func like(_ pattern: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` pattern ` | An `Expression` (evaluating to a string) representing the pattern to search for. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` representing the "like" comparison.
- `


  ### [regexContains(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP13regexContainsyAA07BooleanC0_pSSF)


  ` Default implementation Creates an expression that checks if a string (from `self`) contains a specified regular
  expression literal as a substring.
  Assumes `self` evaluates to a string.

      // Check if "description" contains "example" (case-insensitive)
      Field("description").regexContains("(?i)example")

  #### Default Implementation

  #### Declaration

  Swift

      func regexContains(_ pattern: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` pattern ` | The literal string regular expression to use for the search. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` representing the "regex_contains" comparison.
- `


  ### [regexContains(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP13regexContainsyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates an expression that checks if a string (from `self`) contains a specified regular
  expression (from an expression) as a substring.
  Assumes `self` evaluates to a string, and `pattern` evaluates to a string.

      // Check if "logEntry" contains a pattern from "errorPattern" field
      Field("logEntry").regexContains(Field("errorPattern"))

  #### Default Implementation

  #### Declaration

  Swift

      func regexContains(_ pattern: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` pattern ` | An `Expression` (evaluating to a string) representing the regular expression to use for the search. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` representing the "regex_contains" comparison.
- `


  ### [regexFind(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP9regexFindyAA08FunctionC0CSSF)


  ` Default implementation Creates an expression that returns the first substring of a string expression that matches
  a specified regular expression.
  Assumes `self` evaluates to a string.

      // Extract the domain name from an email field
      Field("email").regexFind("@[A-Za-z0-9.-]+")

  #### Default Implementation

  #### Declaration

  Swift

      func regexFind(_ pattern: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` pattern ` | The literal string regular expression to search for. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the regular expression find function.
- `


  ### [regexFind(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP9regexFindyAA08FunctionC0CAaB_pF)


  ` Default implementation Creates an expression that returns the first substring of a string expression that matches
  a specified regular expression.
  Assumes `self` evaluates to a string, and `pattern` evaluates to a string.

      // Extract a substring based on a dynamic pattern stored in another field
      Field("email").regexFind(Field("pattern"))

  #### Default Implementation

  #### Declaration

  Swift

      func regexFind(_ pattern: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` pattern ` | An `Expression` (evaluating to a string) representing the regular expression to search for. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the regular expression find function.
- `


  ### [regexFindAll(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP12regexFindAllyAA08FunctionC0CSSF)


  ` Default implementation Creates an expression that evaluates to a list of all substrings in a string expression that
  match a specified regular expression.
  Assumes `self` evaluates to a string.

      // Extract all hashtags from a post content field
      Field("content").regexFindAll("#[A-Za-z0-9_]+")

  #### Default Implementation

  #### Declaration

  Swift

      func regexFindAll(_ pattern: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` pattern ` | The literal string regular expression to search for. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` that evaluates to an array of matched substrings.
- `


  ### [regexFindAll(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP12regexFindAllyAA08FunctionC0CAaB_pF)


  ` Default implementation Creates an expression that evaluates to a list of all substrings in a string expression that
  match a specified regular expression.
  Assumes `self` evaluates to a string, and `pattern` evaluates to a string.

      // Extract all matches based on a dynamic pattern stored in another field
      Field("content").regexFindAll(Field("pattern"))

  #### Default Implementation

  #### Declaration

  Swift

      func regexFindAll(_ pattern: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` pattern ` | An `Expression` (evaluating to a string) representing the regular expression to search for. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` that evaluates to an array of matched substrings.
- `


  ### [regexMatch(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP10regexMatchyAA07BooleanC0_pSSF)


  ` Default implementation Creates an expression that checks if a string (from `self`) matches a specified regular
  expression literal entirely.
  Assumes `self` evaluates to a string.

      // Check if the "email" field matches a valid email pattern
      Field("email").regexMatch("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

  #### Default Implementation

  #### Declaration

  Swift

      func regexMatch(_ pattern: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` pattern ` | The literal string regular expression to use for the match. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` representing the regular expression match.
- `


  ### [regexMatch(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP10regexMatchyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates an expression that checks if a string (from `self`) matches a specified regular
  expression (from an expression) entirely.
  Assumes `self` evaluates to a string, and `pattern` evaluates to a string.

      // Check if "input" matches the regex stored in "validationRegex"
      Field("input").regexMatch(Field("validationRegex"))

  #### Default Implementation

  #### Declaration

  Swift

      func regexMatch(_ pattern: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` pattern ` | An `Expression` (evaluating to a string) representing the regular expression to use for the match. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` representing the regular expression match.
- `


  ### [stringContains(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP14stringContainsyAA07BooleanC0_pSSF)


  ` Default implementation Creates an expression that checks if a string (from `self`) contains a specified literal
  substring (case-sensitive).
  Assumes `self` evaluates to a string.

      // Check if the "description" field contains "example".
      Field("description").stringContains("example")

  #### Default Implementation

  #### Declaration

  Swift

      func stringContains(_ substring: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` substring ` | The literal string substring to search for. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` representing the "stringContains" comparison.
- `


  ### [stringContains(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP14stringContainsyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates an expression that checks if a string (from `self`) contains a specified substring
  from an expression (case-sensitive).
  Assumes `self` evaluates to a string, and `expression` evaluates to a string.

      // Check if the "message" field contains the value of the "keyword" field.
      Field("message").stringContains(Field("keyword"))

  #### Default Implementation

  #### Declaration

  Swift

      func stringContains(_ expression: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` expression ` | An `Expression` (evaluating to a string) representing the substring to search for. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` representing the "str_contains" comparison.
- `


  ### [startsWith(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP10startsWithyAA07BooleanC0_pSSF)


  ` Default implementation Creates an expression that checks if a string (from `self`) starts with a given literal prefix
  (case-sensitive).
  Assumes `self` evaluates to a string.

      // Check if the "name" field starts with "Mr."
      Field("name").startsWith("Mr.")

  #### Default Implementation

  #### Declaration

  Swift

      func startsWith(_ prefix: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` prefix ` | The literal string prefix to check for. |

  #### Return Value

  A new `BooleanExpr` representing the "starts_with" comparison.
- `


  ### [startsWith(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP10startsWithyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates an expression that checks if a string (from `self`) starts with a given prefix from an
  expression (case-sensitive).
  Assumes `self` evaluates to a string, and `prefix` evaluates to a string.

      // Check if "fullName" starts with the value of "firstName"
      Field("fullName").startsWith(Field("firstName"))

  #### Default Implementation

  #### Declaration

  Swift

      func startsWith(_ prefix: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` prefix ` | An `Expression` (evaluating to a string) representing the prefix to check for. |

  #### Return Value

  A new `BooleanExpr` representing the "starts_with" comparison.
- `


  ### [endsWith(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8endsWithyAA07BooleanC0_pSSF)


  ` Default implementation Creates an expression that checks if a string (from `self`) ends with a given literal suffix
  (case-sensitive).
  Assumes `self` evaluates to a string.

      // Check if the "filename" field ends with ".txt"
      Field("filename").endsWith(".txt")

  #### Default Implementation

  #### Declaration

  Swift

      func endsWith(_ suffix: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` suffix ` | The literal string suffix to check for. |

  #### Return Value

  A new `BooleanExpr` representing the "ends_with" comparison.
- `


  ### [endsWith(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8endsWithyAA07BooleanC0_pAaB_pF)


  ` Default implementation Creates an expression that checks if a string (from `self`) ends with a given suffix from an
  expression (case-sensitive).
  Assumes `self` evaluates to a string, and `suffix` evaluates to a string.

      // Check if "url" ends with the value of "extension" field
      Field("url").endsWith(Field("extension"))

  #### Default Implementation

  #### Declaration

  Swift

      func endsWith(_ suffix: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html

  #### Parameters

  |---|---|
  | ` suffix ` | An `Expression` (evaluating to a string) representing the suffix to check for. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` representing the "ends_with" comparison.
- `


  ### [toLower()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP7toLowerAA08FunctionC0CyF)


  ` Default implementation Creates an expression that converts a string (from `self`) to lowercase.
  Assumes `self` evaluates to a string.

      // Convert the "name" field to lowercase
      Field("name").toLower()

  #### Default Implementation

  #### Declaration

  Swift

      func toLower() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the lowercase string.
- `


  ### [toUpper()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP7toUpperAA08FunctionC0CyF)


  ` Default implementation Creates an expression that converts a string (from `self`) to uppercase.
  Assumes `self` evaluates to a string.

      // Convert the "title" field to uppercase
      Field("title").toUpper()

  #### Default Implementation

  #### Declaration

  Swift

      func toUpper() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the uppercase string.
- `


  ### [trim()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP4trimAA08FunctionC0CyF)


  ` Default implementation Creates an expression that removes leading and trailing whitespace from a string.

  Assumes `self` evaluates to a string.

      // Trim leading/trailing whitespace from the "comment" field.
      Field("comment").trim()

  #### Default Implementation

  #### Declaration

  Swift

      func trim() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the trimmed string.
- `


  ### [trim(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP4trimyAA08FunctionC0CSSF)


  ` Default implementation Creates an expression that removes leading and trailing occurrences of specified characters
  from a string (from `self`).
  Assumes `self` evaluates to a string, and `value` evaluates to a string.

      // Trim leading/trailing "xy" from field
      Field("code").trim(characters: "xy")

  #### Default Implementation

  #### Declaration

  Swift

      func trim(_ value: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` value ` | A `String` containing the characters to trim. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the trimmed string.
- `


  ### [trim(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP4trimyAA08FunctionC0CAaB_pF)


  ` Default implementation Creates an expression that removes leading and trailing occurrences of specified string
  (from an expression) from a string (from `self`).
  Assumes `self` evaluates to a string, and `value` evaluates to a string.

      // Trim characters specified by the "trimChars" field from "data"
      Field("data").trim(characters: Field("trimChars"))

  #### Default Implementation

  #### Declaration

  Swift

      func trim(_ value: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` value ` | An `Expression` (evaluating to a string) containing the characters to trim. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the trimmed string.
- `


  ### [stringConcat(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP12stringConcatyAA08FunctionC0CSays8Sendable_pGF)


  ` Default implementation Creates an expression that concatenates this string expression with other string expressions.
  Assumes `self` and all parameters evaluate to strings.

      // Combine "firstName", " ", and "lastName"
      Field("firstName").stringConcat([" ", Field("lastName")])

  #### Default Implementation

  #### Declaration

  Swift

      func stringConcat(_ strings: [Sendable]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` strings ` | An array of `Expression` or `String` to concatenate. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the concatenated string.
- `


  ### [stringConcat(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP12stringConcatyAA08FunctionC0CSayAaB_pGF)


  ` Default implementation Creates an expression that concatenates this string expression with other string expressions.
  Assumes `self` and all parameters evaluate to strings.

      // Combine "firstName", "middleName", and "lastName" fields
      Field("firstName").stringConcat(Field("middleName"), Field("lastName"))

  #### Default Implementation

  #### Declaration

  Swift

      func stringConcat(_ strings: [Expression]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` secondString ` | An `Expression` (evaluating to a string) to concatenate. |
  | ` otherStrings ` | Optional additional `Expression` (evaluating to strings) to concatenate. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the concatenated string.
- `


  ### [reverse()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP7reverseAA08FunctionC0CyF)


  ` Default implementation Creates an expression that reverses this expression.
  Assumes `self` evaluates to a string.

      // Reverse the value of the "myString" field.
      Field("myString").reverse()

  #### Default Implementation

  #### Declaration

  Swift

      func reverse() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the reversed string.
- `


  ### [stringReverse()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP13stringReverseAA08FunctionC0CyF)


  ` Default implementation Creates an expression that reverses this string expression.
  Assumes `self` evaluates to a string.

      // Reverse the value of the "myString" field.
      Field("myString").stringReverse()

  #### Default Implementation

  #### Declaration

  Swift

      func stringReverse() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the reversed string.
- `


  ### [byteLength()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP10byteLengthAA08FunctionC0CyF)


  ` Default implementation Creates an expression that calculates the length of this string or bytes expression in bytes.
  Assumes `self` evaluates to a string or bytes.

      // Calculate the length of the "myString" field in bytes.
      Field("myString").byteLength()

      // Calculate the size of the "avatar" (Data/Bytes) field.
      Field("avatar").byteLength()

  #### Default Implementation

  #### Declaration

  Swift

      func byteLength() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the length in bytes.
- `


  ### [substring(position:length:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP9substring8position6lengthAA08FunctionC0CSi_SiSgtF)


  ` Default implementation Creates an expression that returns a substring of this expression (String or Bytes) using
  literal integers for position and optional length.
  Indexing is 0-based. Assumes `self` evaluates to a string or bytes.

      // Get substring from index 5 with length 10
      Field("myString").substring(5, 10)

      // Get substring from "myString" starting at index 3 to the end
      Field("myString").substring(3) // Default nil

  #### Default Implementation

  #### Declaration

  Swift

      func substring(position: Int, length: Int?) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` position ` | Literal `Int` index of the first character/byte. |
  | ` length ` | Optional literal `Int` length of the substring. If `nil`, goes to the end. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the substring.
- `


  ### [substring(position:length:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP9substring8position6lengthAA08FunctionC0CAaB_p_AaB_pSgtF)


  ` Default implementation Creates an expression that returns a substring of this expression (String or Bytes) using
  expressions for position and optional length.
  Indexing is 0-based. Assumes `self` evaluates to a string or bytes, and parameters evaluate to
  integers.

      // Get substring from index calculated by Field("start") with length from Field("len")
      Field("myString").substring(Field("start"), Field("len"))

      // Get substring from index calculated by Field("start") to the end
      Field("myString").substring(Field("start")) // Default nil for optional Expression length

  #### Default Implementation

  #### Declaration

  Swift

      func substring(position: Expression, length: Expression?) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` position ` | An `Expression` (evaluating to an Int) for the index of the first character. |
  | ` length ` | Optional `Expression` (evaluating to an Int) for the length of the substring. If `nil`, goes to the end. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the substring.
[## Map Operations](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/Map-Operations)

- `


  ### [mapGet(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP6mapGetyAA08FunctionC0CSSF)


  ` Default implementation Accesses a value from a map (object) field using the provided literal string key.
  Assumes `self` evaluates to a Map.

      // Get the "city" value from the "address" map field
      Field("address").mapGet("city")

  #### Default Implementation

  #### Declaration

  Swift

      func mapGet(_ subfield: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` subfield ` | The literal string key to access in the map. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the value associated with the given key.
- `


  ### [mapRemove(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP9mapRemoveyAA08FunctionC0CSSF)


  ` Default implementation Creates an expression that removes a key (specified by a literal string) from the map produced
  by evaluating this expression.
  Assumes `self` evaluates to a Map.

      // Removes the key "baz" from the map held in field "myMap"
      Field("myMap").mapRemove("baz")

  #### Default Implementation

  #### Declaration

  Swift

      func mapRemove(_ key: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` key ` | The literal string key to remove from the map. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the "map_remove" operation.
- `


  ### [mapRemove(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP9mapRemoveyAA08FunctionC0CAaB_pF)


  ` Default implementation Creates an expression that removes a key (specified by an expression) from the map produced by
  evaluating this expression.
  Assumes `self` evaluates to a Map, and `keyExpression` evaluates to a string.

      // Removes the key specified by field "keyToRemove" from the map in "settings"
      Field("settings").mapRemove(Field("keyToRemove"))

  #### Default Implementation

  #### Declaration

  Swift

      func mapRemove(_ keyExpression: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` keyExpression ` | An `Expression` (evaluating to a string) representing the key to remove from the map. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the "map_remove" operation.
- `


  ### [mapMerge(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8mapMergeyAA08FunctionC0CSaySDySSs8Sendable_pGGF)


  ` Default implementation Creates an expression that merges this map with multiple other map literals.
  Assumes `self` evaluates to a Map. Later maps overwrite keys from earlier maps.

      // Merge "settings" field with { "enabled": true } and another map literal { "priority": 1 }
      Field("settings").mapMerge(["enabled": true], ["priority": 1])

  #### Default Implementation

  #### Declaration

  Swift

      func mapMerge(_ maps: [[String: Sendable]])
        -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` maps ` | Maps (dictionary literals with `Sendable` values) to merge. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the "map_merge" operation.
- `


  ### [mapMerge(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8mapMergeyAA08FunctionC0CSayAaB_pGF)


  ` Default implementation Creates an expression that merges this map with multiple other map expressions.
  Assumes `self` and other arguments evaluate to Maps. Later maps overwrite keys from earlier
  maps.

      // Merge "baseSettings" field with "userOverrides" field and "adminConfig" field
      Field("baseSettings").mapMerge(Field("userOverrides"), Field("adminConfig"))

  #### Default Implementation

  #### Declaration

  Swift

      func mapMerge(_ maps: [Expression]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` maps ` | Additional `Expression` (evaluating to Maps) to merge. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the "map_merge" operation.
[## Aggregations](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/Aggregations)

- `


  ### [countDistinct()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP13countDistinctAA17AggregateFunctionCyF)


  ` Default implementation Creates an aggregation that counts the number of distinct values of this expression.

      // Count the number of distinct categories.
      Field("category").countDistinct().as("distinctCategories")

  #### Default Implementation

  #### Declaration

  Swift

      func countDistinct() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html` representing the "count_distinct" aggregation.
- `


  ### [count()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP5countAA17AggregateFunctionCyF)


  ` Default implementation Creates an aggregation that counts the number of stage inputs where this expression evaluates
  to a valid, non-null value.

      // Count the total number of products with a "productId"
      Field("productId").count().alias("totalProducts")

  #### Default Implementation

  #### Declaration

  Swift

      func count() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html` representing the "count" aggregation on this expression.
- `


  ### [sum()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP3sumAA17AggregateFunctionCyF)


  ` Default implementation Creates an aggregation that calculates the sum of this numeric expression across multiple
  stage inputs.
  Assumes `self` evaluates to a numeric type.

      // Calculate the total revenue from a set of orders
      Field("orderAmount").sum().alias("totalRevenue")

  #### Default Implementation

  #### Declaration

  Swift

      func sum() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html` representing the "sum" aggregation.
- `


  ### [average()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP7averageAA17AggregateFunctionCyF)


  ` Default implementation Creates an aggregation that calculates the average (mean) of this numeric expression across
  multiple stage inputs.
  Assumes `self` evaluates to a numeric type.

      // Calculate the average age of users
      Field("age").average().as("averageAge")

  #### Default Implementation

  #### Declaration

  Swift

      func average() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html` representing the "average" aggregation.
- `


  ### [minimum()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP7minimumAA17AggregateFunctionCyF)


  ` Default implementation Creates an aggregation that finds the minimum value of this expression across multiple stage
  inputs.

      // Find the lowest price of all products
      Field("price").minimum().alias("lowestPrice")

  #### Default Implementation

  #### Declaration

  Swift

      func minimum() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html` representing the "min" aggregation.
- `


  ### [maximum()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP7maximumAA17AggregateFunctionCyF)


  ` Default implementation Creates an aggregation that finds the maximum value of this expression across multiple stage
  inputs.

      // Find the highest score in a leaderboard
      Field("score").maximum().alias("highestScore")

  #### Default Implementation

  #### Declaration

  Swift

      func maximum() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html` representing the "max" aggregation.
- `


  ### [logicalMaximum(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP14logicalMaximumyAA08FunctionC0CSayAaB_pGF)


  ` Default implementation Creates an expression that returns the larger value between this expression and other
  expressions, based on Firestore"s value type ordering.

      // Returns the largest of "val1", "val2", and "val3" fields
      Field("val1").logicalMaximum(Field("val2"), Field("val3"))

  #### Default Implementation

  #### Declaration

  Swift

      func logicalMaximum(_ expressions: [Expression]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` expressions ` | An array of at least one `Expression` to compare with. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the logical max operation.
- `


  ### [logicalMaximum(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP14logicalMaximumyAA08FunctionC0CSays8Sendable_pGF)


  ` Default implementation Creates an expression that returns the larger value between this expression and other literal
  values, based on Firestore"s value type ordering.

      // Returns the largest of "val1" (a field), 100, and 200.0
      Field("val1").logicalMaximum(100, 200.0)

  #### Default Implementation

  #### Declaration

  Swift

      func logicalMaximum(_ values: [Sendable]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` values ` | An array of at least one `Sendable` value to compare with. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the logical max operation.
- `


  ### [logicalMinimum(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP14logicalMinimumyAA08FunctionC0CSayAaB_pGF)


  ` Default implementation Creates an expression that returns the smaller value between this expression and other
  expressions, based on Firestore"s value type ordering.

      // Returns the smallest of "val1", "val2", and "val3" fields
      Field("val1").logicalMinimum(Field("val2"), Field("val3"))

  #### Default Implementation

  #### Declaration

  Swift

      func logicalMinimum(_ expressions: [Expression]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` expressions ` | An array of at least one `Expression` to compare with. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the logical min operation.
- `


  ### [logicalMinimum(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP14logicalMinimumyAA08FunctionC0CSays8Sendable_pGF)


  ` Default implementation Creates an expression that returns the smaller value between this expression and other literal
  values, based on Firestore"s value type ordering.

      // Returns the smallest of "val1" (a field), 0, and -5.5
      Field("val1").logicalMinimum(0, -5.5)

  #### Default Implementation

  #### Declaration

  Swift

      func logicalMinimum(_ values: [Sendable]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` values ` | An array of at least one `Sendable` value to compare with. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the logical min operation.
[## Vector Operations](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/Vector-Operations)

- `


  ### [vectorLength()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP12vectorLengthAA08FunctionC0CyF)


  ` Default implementation Creates an expression that calculates the length (number of dimensions) of this Firestore
  Vector expression.
  Assumes `self` evaluates to a Vector.

      // Get the vector length (dimension) of the field "embedding".
      Field("embedding").vectorLength()

  #### Default Implementation

  #### Declaration

  Swift

      func vectorLength() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the length of the vector.
- `


  ### [cosineDistance(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP14cosineDistanceyAA08FunctionC0CAaB_pF)


  ` Default implementation Calculates the cosine distance between this vector expression and another vector expression.
  Assumes both `self` and `other` evaluate to Vectors.

      // Cosine distance between "userVector" field and "itemVector" field
      Field("userVector").cosineDistance(Field("itemVector"))

  #### Default Implementation

  #### Declaration

  Swift

      func cosineDistance(_ expression: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` expression ` | The other vector as an `Expr` to compare against. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the cosine distance.
- `


  ### [cosineDistance(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP14cosineDistanceyAA08FunctionC0CSo14FIRVectorValueCF)


  ` Default implementation Calculates the cosine distance between this vector expression and another vector literal
  (`VectorValue`).
  Assumes `self` evaluates to a Vector.

      // Cosine distance with a VectorValue
      let targetVector = VectorValue(vector: [0.1, 0.2, 0.3])
      Field("docVector").cosineDistance(targetVector)

  #### Default Implementation

  #### Declaration

  Swift

      func cosineDistance(_ vector: VectorValue) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` vector ` | The other vector as a `VectorValue` to compare against. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the cosine distance.
- `


  ### [cosineDistance(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP14cosineDistanceyAA08FunctionC0CSaySdGF)


  ` Default implementation Calculates the cosine distance between this vector expression and another vector literal
  (`[Double]`).
  Assumes `self` evaluates to a Vector.

      // Cosine distance between "location" field and a target location
      Field("location").cosineDistance([37.7749, -122.4194])

  #### Default Implementation

  #### Declaration

  Swift

      func cosineDistance(_ vector: [Double]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` vector ` | The other vector as `[Double]` to compare against. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the cosine distance.
- `


  ### [dotProduct(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP10dotProductyAA08FunctionC0CAaB_pF)


  ` Default implementation Calculates the dot product between this vector expression and another vector expression.
  Assumes both `self` and `other` evaluate to Vectors.

      // Dot product between "vectorA" and "vectorB" fields
      Field("vectorA").dotProduct(Field("vectorB"))

  #### Default Implementation

  #### Declaration

  Swift

      func dotProduct(_ expression: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` expression ` | The other vector as an `Expr` to calculate with. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the dot product.
- `


  ### [dotProduct(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP10dotProductyAA08FunctionC0CSo14FIRVectorValueCF)


  ` Default implementation Calculates the dot product between this vector expression and another vector literal
  (`VectorValue`).
  Assumes `self` evaluates to a Vector.

      // Dot product with a VectorValue
      let weightVector = VectorValue(vector: [0.5, -0.5])
      Field("features").dotProduct(weightVector)

  #### Default Implementation

  #### Declaration

  Swift

      func dotProduct(_ vector: VectorValue) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` vector ` | The other vector as a `VectorValue` to calculate with. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the dot product.
- `


  ### [dotProduct(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP10dotProductyAA08FunctionC0CSaySdGF)


  ` Default implementation Calculates the dot product between this vector expression and another vector literal
  (`[Double]`).
  Assumes `self` evaluates to a Vector.

      // Dot product between a feature vector and a target vector literal
      Field("features").dotProduct([0.5, 0.8, 0.2])

  #### Default Implementation

  #### Declaration

  Swift

      func dotProduct(_ vector: [Double]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` vector ` | The other vector as `[Double]` to calculate with. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the dot product.
- `


  ### [euclideanDistance(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP17euclideanDistanceyAA08FunctionC0CAaB_pF)


  ` Default implementation Calculates the Euclidean distance between this vector expression and another vector
  expression.
  Assumes both `self` and `other` evaluate to Vectors.

      // Euclidean distance between "pointA" and "pointB" fields
      Field("pointA").euclideanDistance(Field("pointB"))

  #### Default Implementation

  #### Declaration

  Swift

      func euclideanDistance(_ expression: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` expression ` | The other vector as an `Expr` to compare against. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the Euclidean distance.
- `


  ### [euclideanDistance(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP17euclideanDistanceyAA08FunctionC0CSo14FIRVectorValueCF)


  ` Default implementation Calculates the Euclidean distance between this vector expression and another vector literal
  (`VectorValue`).
  Assumes `self` evaluates to a Vector.

      let targetPoint = VectorValue(vector: [1.0, 2.0])
      Field("currentLocation").euclideanDistance(targetPoint)

  #### Default Implementation

  #### Declaration

  Swift

      func euclideanDistance(_ vector: VectorValue) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` vector ` | The other vector as a `VectorValue` to compare against. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the Euclidean distance.
- `


  ### [euclideanDistance(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP17euclideanDistanceyAA08FunctionC0CSaySdGF)


  ` Default implementation Calculates the Euclidean distance between this vector expression and another vector literal
  (`[Double]`).
  Assumes `self` evaluates to a Vector.

      // Euclidean distance between "location" field and a target location literal
      Field("location").euclideanDistance([37.7749, -122.4194])

  #### Default Implementation

  #### Declaration

  Swift

      func euclideanDistance(_ vector: [Double]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` vector ` | The other vector as `[Double]` to compare against. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the Euclidean distance.
[## Timestamp operations](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/Timestamp-operations)

- `


  ### [unixMicrosToTimestamp()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP21unixMicrosToTimestampAA08FunctionC0CyF)


  ` Default implementation Creates an expression that interprets this expression (evaluating to a number) as microseconds
  since the Unix epoch and returns a timestamp.
  Assumes `self` evaluates to a number.

      // Interpret "microseconds" field as microseconds since epoch.
      Field("microseconds").unixMicrosToTimestamp()

  #### Default Implementation

  #### Declaration

  Swift

      func unixMicrosToTimestamp() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the timestamp.
- `


  ### [timestampToUnixMicros()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP21timestampToUnixMicrosAA08FunctionC0CyF)


  ` Default implementation Creates an expression that converts this timestamp expression to the number of microseconds
  since the Unix epoch. Assumes `self` evaluates to a Timestamp.

      // Convert "timestamp" field to microseconds since epoch.
      Field("timestamp").timestampToUnixMicros()

  #### Default Implementation

  #### Declaration

  Swift

      func timestampToUnixMicros() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the number of microseconds.
- `


  ### [unixMillisToTimestamp()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP21unixMillisToTimestampAA08FunctionC0CyF)


  ` Default implementation Creates an expression that interprets this expression (evaluating to a number) as milliseconds
  since the Unix epoch and returns a timestamp.
  Assumes `self` evaluates to a number.

      // Interpret "milliseconds" field as milliseconds since epoch.
      Field("milliseconds").unixMillisToTimestamp()

  #### Default Implementation

  #### Declaration

  Swift

      func unixMillisToTimestamp() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the timestamp.
- `


  ### [timestampToUnixMillis()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP21timestampToUnixMillisAA08FunctionC0CyF)


  ` Default implementation Creates an expression that converts this timestamp expression to the number of milliseconds
  since the Unix epoch. Assumes `self` evaluates to a Timestamp.

      // Convert "timestamp" field to milliseconds since epoch.
      Field("timestamp").timestampToUnixMillis()

  #### Default Implementation

  #### Declaration

  Swift

      func timestampToUnixMillis() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the number of milliseconds.
- `


  ### [unixSecondsToTimestamp()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP22unixSecondsToTimestampAA08FunctionC0CyF)


  ` Default implementation Creates an expression that interprets this expression (evaluating to a number) as seconds
  since the Unix epoch and returns a timestamp.
  Assumes `self` evaluates to a number.

      // Interpret "seconds" field as seconds since epoch.
      Field("seconds").unixSecondsToTimestamp()

  #### Default Implementation

  #### Declaration

  Swift

      func unixSecondsToTimestamp() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the timestamp.
- `


  ### [timestampToUnixSeconds()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP22timestampToUnixSecondsAA08FunctionC0CyF)


  ` Default implementation Creates an expression that converts this timestamp expression to the number of seconds
  since the Unix epoch. Assumes `self` evaluates to a Timestamp.

      // Convert "timestamp" field to seconds since epoch.
      Field("timestamp").timestampToUnixSeconds()

  #### Default Implementation

  #### Declaration

  Swift

      func timestampToUnixSeconds() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the number of seconds.
- `


  ### [timestampTruncate(granularity:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP17timestampTruncate11granularityAA08FunctionC0CAA15TimeGranularityV_tF)


  ` Default implementation Creates an expression that truncates a timestamp to a specified granularity.
  Assumes `self` evaluates to a Timestamp.

      // Truncate "timestamp" field to the nearest day.
      Field("timestamp").timestampTruncate(granularity: .day)

  #### Default Implementation

  #### Declaration

  Swift

      func timestampTruncate(granularity: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/TimeGranularity.html) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` granularity ` | A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/TimeGranularity.html` representing the truncation unit. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the truncated timestamp.
- `


  ### [timestampTruncate(granularity:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP17timestampTruncate11granularityAA08FunctionC0Cs8Sendable_p_tF)


  ` Default implementation Creates an expression that truncates a timestamp to a specified granularity.
  Assumes `self` evaluates to a Timestamp.

      // Truncate "timestamp" field to the nearest day using a literal string.
      Field("timestamp").timestampTruncate(granularity: "day")

      // Truncate "timestamp" field to the nearest day using an expression.
      Field("timestamp").timestampTruncate(granularity: Field("granularity_field"))

  #### Default Implementation

  #### Declaration

  Swift

      func timestampTruncate(granularity: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` granularity ` | A `Sendable` literal string or an `Expression` that evaluates to a string, specifying the truncation unit. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the truncated timestamp.
- `


  ### [timestampAdd(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP12timestampAddyAA08FunctionC0CSi_AA8TimeUnitVtF)


  ` Default implementation Creates an expression that adds a specified amount of time to this timestamp expression,
  where unit and amount are provided as literals.
  Assumes `self` evaluates to a Timestamp.

      // Add 1 day to the "timestamp" field.
      Field("timestamp").timestampAdd(1, .day)

  #### Default Implementation

  #### Declaration

  Swift

      func timestampAdd(_ amount: Int, _ unit: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/TimeUnit.html) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` unit ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/TimeUnit.html` enum representing the unit of time. |
  | ` amount ` | The literal `Int` amount of the unit to add. |

  #### Return Value

  A new "FunctionExpression" representing the resulting timestamp.
- `


  ### [timestampAdd(amount:unit:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP12timestampAdd6amount4unitAA08FunctionC0CAaB_p_s8Sendable_ptF)


  ` Default implementation Creates an expression that adds a specified amount of time to this timestamp expression,
  where unit and amount are provided as an expression for amount and a literal for unit.
  Assumes `self` evaluates to a Timestamp, `amount` evaluates to an integer, and `unit`
  evaluates to a string.

      // Add duration from "amountField" to "timestamp" with a literal unit "day".
      Field("timestamp").timestampAdd(amount: Field("amountField"), unit: "day")

  #### Default Implementation

  #### Declaration

  Swift

      func timestampAdd(amount: Expression, unit: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` unit ` | A `Sendable` literal string specifying the unit of time. Valid units are "microsecond", "millisecond", "second", "minute", "hour", "day". |
  | ` amount ` | An `Expression` evaluating to the amount (Int) of the unit to add. |

  #### Return Value

  A new "FunctionExpression" representing the resulting timestamp.
- `


  ### [timestampSubtract(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP17timestampSubtractyAA08FunctionC0CSi_AA8TimeUnitVtF)


  ` Default implementation Creates an expression that subtracts a specified amount of time from this timestamp
  expression, where unit and amount are provided as literals.
  Assumes `self` evaluates to a Timestamp.

      // Subtract 1 day from the "timestamp" field.
      Field("timestamp").timestampSubtract(1, .day)

  #### Default Implementation

  #### Declaration

  Swift

      func timestampSubtract(_ amount: Int, _ unit: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/TimeUnit.html) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` unit ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/TimeUnit.html` enum representing the unit of time. |
  | ` amount ` | The literal `Int` amount of the unit to subtract. |

  #### Return Value

  A new "FunctionExpression" representing the resulting timestamp.
- `


  ### [timestampSubtract(amount:unit:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP17timestampSubtract6amount4unitAA08FunctionC0CAaB_p_s8Sendable_ptF)


  ` Default implementation Creates an expression that subtracts a specified amount of time from this timestamp
  expression, where unit and amount are provided as an expression for amount and a literal for
  unit.
  Assumes `self` evaluates to a Timestamp, `amount` evaluates to an integer, and `unit`
  evaluates to a string.

      // Subtract duration from "amountField" from "timestamp" with a literal unit "day".
      Field("timestamp").timestampSubtract(amount: Field("amountField"), unit: "day")

  #### Default Implementation

  #### Declaration

  Swift

      func timestampSubtract(amount: Expression, unit: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` unit ` | A `Sendable` literal string specifying the unit of time. Valid units are "microsecond", "millisecond", "second", "minute", "hour", "day". |
  | ` amount ` | An `Expression` evaluating to the amount (Int) of the unit to subtract. |

  #### Return Value

  A new "FunctionExpression" representing the resulting timestamp.
- `


  ### [documentId()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP10documentIdAA08FunctionC0CyF)


  ` Default implementation Creates an expression that returns the document ID from a path.

      // Get the document ID from a path.
      Field(FieldPath.documentID()).documentId()

  #### Default Implementation

  #### Declaration

  Swift

      func documentId() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the documentId operation.
- `


  ### [collectionId()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP12collectionIdAA08FunctionC0CyF)


  ` Default implementation Gets the collection id (kind) of a given document (either an absolute or
  namespace relative reference). Throw error if the input is the
  root itself.

  #### Default Implementation

  #### Declaration

  Swift

      func collectionId() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

- `


  ### [ifError(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP7ifErroryAA08FunctionC0CAaB_pF)


  ` Default implementation Creates an expression that returns the result of `catchExpression` if this expression produces
  an error during evaluation, otherwise returns the result of this expression.

      // Try dividing "a" by "b", return field "fallbackValue" on error (e.g., division by zero)
      Field("a").divide(Field("b")).ifError(Field("fallbackValue"))

  #### Default Implementation

  #### Declaration

  Swift

      func ifError(_ catchExpression: Expression) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` catchExpression ` | The `Expression` to evaluate and return if this expression errors. |

  #### Return Value

  A new "FunctionExpression" representing the "ifError" operation.
- `


  ### [ifError(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP7ifErroryAA08FunctionC0Cs8Sendable_pF)


  ` Default implementation Creates an expression that returns the literal `catchValue` if this expression produces an
  error during evaluation, otherwise returns the result of this expression.

      // Get first item in "title" array, or return "Default Title" if error (e.g., empty array)
      Field("title").arrayGet(0).ifError("Default Title")

  #### Default Implementation

  #### Declaration

  Swift

      func ifError(_ catchValue: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` catchValue ` | The literal `Sendable` value to return if this expression errors. |

  #### Return Value

  A new "FunctionExpression" representing the "ifError" operation.
- `


  ### [ifAbsent(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP8ifAbsentyAA08FunctionC0Cs8Sendable_pF)


  ` Default implementation Creates an expression that returns the literal `defaultValue` if this expression is
  absent (e.g., a field does not exist in a map).
  Otherwise, returns the result of this expression.

      // If the "optionalField" is absent, return "default value".
      Field("optionalField").ifAbsent("default value")

  #### Default Implementation

  #### Declaration

  Swift

      func ifAbsent(_ defaultValue: Sendable) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` defaultValue ` | The literal `Sendable` value to return if this expression is absent. |

  #### Return Value

  A new "FunctionExpression" representing the "ifAbsent" operation.
[## Sorting](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/Sorting)

- `


  ### [ascending()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP9ascendingAA8OrderingVyF)


  ` Default implementation Creates an `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Ordering.html` object that sorts documents in ascending order based on this expression.

      // Sort documents by the "name" field in ascending order
      firestore.pipeline().collection("users")
        .sort(Field("name").ascending())

  #### Default Implementation

  #### Declaration

  Swift

      func ascending() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Ordering.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Ordering.html` instance for ascending sorting.
- `


  ### [descending()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP10descendingAA8OrderingVyF)


  ` Default implementation Creates an `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Ordering.html` object that sorts documents in descending order based on this
  expression.

      // Sort documents by the "createdAt" field in descending order
      firestore.pipeline().collection("users")
        .sort(Field("createdAt").descending())

  #### Default Implementation

  #### Declaration

  Swift

      func descending() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Ordering.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Ordering.html` instance for descending sorting.
- `


  ### [concat(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP6concatyAA08FunctionC0CSays8Sendable_pGF)


  ` Default implementation Creates an expression that concatenates multiple sequenceable types together.

      // Concatenate the firstName and lastName with a space in between.
      Field("firstName").concat([" ", Field("lastName")])

  #### Default Implementation

  #### Declaration

  Swift

      func concat(_ values: [Sendable]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Parameters

  |---|---|
  | ` values ` | The values to concatenate. |

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the concatenated result.
- `


  ### [type()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression#/s:17FirebaseFirestore10ExpressionP4typeAA08FunctionC0CyF)


  ` Default implementation Creates an expression that returns the type of the expression.

      // Get the type of the "rating" field.
      Field("rating").type()

  #### Default Implementation

  #### Declaration

  Swift

      func type() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html` representing the type of the expression as a string.