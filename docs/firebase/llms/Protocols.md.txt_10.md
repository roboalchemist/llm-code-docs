# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.md.txt

# FirebaseFirestore Framework Reference

# Protocols

The following protocols are available globally.
- `


  ### [ListenerRegistration](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ListenerRegistration)


  ` Represents a listener that can be removed by calling remove.

  #### Declaration

  Swift

      protocol ListenerRegistration : NSObjectProtocol

- `


  ### [LocalCacheSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols#/c:objc(pl)FIRLocalCacheSettings)


  ` Marker protocol implemented by all supported cache settings.

  The two cache types supported are `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/PersistentCacheSettings` and `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryCacheSettings`. Custom
  implementation is not supported.

  #### Declaration

  Swift

      protocol LocalCacheSettings

- `


  ### [MemoryGarbageCollectorSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols#/c:objc(pl)FIRMemoryGarbageCollectorSettings)


  ` Marker protocol implemented by all supported garbage collector settings.

  The two cache types supported are `MemoryEagerGCSettings` and `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryLRUGCSettings`. Custom
  implementation is not supported.

  #### Declaration

  Swift

      protocol MemoryGarbageCollectorSettings

- `


  ### [DocumentIDWrappable](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/DocumentIDWrappable)


  ` A type that can initialize itself from a Firestore `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference`,
  which makes it suitable for use with the `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DocumentID` property wrapper.

  Firestore includes extensions that make `String` and `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference`
  conform to `DocumentIDWrappable`.

  Note that Firestore ignores fields annotated with `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DocumentID` when writing
  so there is no requirement to convert from the wrapped type back to a
  `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference`.

  #### Declaration

  Swift

      public protocol DocumentIDWrappable

- `


  ### [ServerTimestampWrappable](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ServerTimestampWrappable)


  ` A type that can initialize itself from a Firestore Timestamp, which makes
  it suitable for use with the `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ServerTimestamp` property wrapper.

  Firestore includes extensions that make `Timestamp` and `Date` conform to
  `ServerTimestampWrappable`.

  #### Declaration

  Swift

      public protocol ServerTimestampWrappable

- `


  ### [Expression](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression)


  ` Undocumented

  #### Declaration

  Swift

      public protocol Expression : Sendable

- `


  ### [BooleanExpression](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression)


  ` A `BooleanExpression` is an `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression` that evaluates to a boolean value.

  It is used to construct conditional logic within Firestore pipelines, such as in `where`
  clauses or `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/ConditionalExpression`. `BooleanExpression` instances can be combined using standard
  logical operators (`&&`, `||`, `!`, `^`) to create complex conditions.

  Example usage in a `where` clause:

      firestore.pipeline()
        .collection("products")
        .where(
          Field("price").greaterThan(100) &&
          (Field("category").equal("electronics") || Field("on_sale").equal(true))
        )

  #### Declaration

  Swift

      public protocol BooleanExpression : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression

- `


  ### [Selectable](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols#/s:17FirebaseFirestore10SelectableP)


  ` A protocol for expressions that have a name.

  `Selectable` is adopted by expressions that can be used in pipeline stages where a named output
  is required, such as `select` and `distinct`.

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field` is a `Selectable` where the name is the field path.

  An expression can be made `Selectable` by giving it an alias using the `.as()` method.

  #### Declaration

  Swift

      public protocol Selectable : Sendable