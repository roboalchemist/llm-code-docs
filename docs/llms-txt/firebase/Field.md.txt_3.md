# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field.md.txt

# FirebaseFirestore Framework Reference

# Field

    public struct Field: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html, https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP, BridgeWrapper, SelectableWrapper,
      @unchecked Sendable

A `Field` is an `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html` that represents a field in a Firestore document.

It is a central component for building queries and transformations in Firestore pipelines.
A `Field` can be used to:

- Reference a document field by its name or `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.html`.
- Create complex `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html`s for filtering in a `where` clause.
- Perform mathematical operations on numeric fields.
- Manipulate string and array fields.

Example of creating a `Field` and using it in a `where` clause:

    // Reference the "price" field in a document
    let priceField = Field("price")

    // Create a query to find products where the price is greater than 100
    firestore.pipeline()
      .collection("products")
      .where(priceField.greaterThan(100))

- `


  ### [fieldName](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field#/s:17FirebaseFirestore5FieldV9fieldNameSSvp)


  ` The name of the field.

  #### Declaration

  Swift

      public let fieldName: String

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field#/s:17FirebaseFirestore5FieldVyACSScfc)


  ` Creates a new `Field` expression from a field name.

  #### Declaration

  Swift

      public init(_ name: String)

  #### Parameters

  |---|---|
  | ` name ` | The name of the field. |

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field#/s:17FirebaseFirestore5FieldVyACSo12FIRFieldPathCcfc)


  ` Creates a new `Field` expression from a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.html`.

  #### Declaration

  Swift

      public init(_ path: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.html)

  #### Parameters

  |---|---|
  | ` path ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.html` of the field. |