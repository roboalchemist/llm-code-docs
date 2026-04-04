# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery/Configuration.md.txt

# FirebaseFirestoreSwift Framework Reference

# Configuration

    public struct Configuration

The query's configurable properties.
- `


  ### [path](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery/Configuration#/s:22FirebaseFirestoreSwift0B5QueryV13ConfigurationV4pathSSvp)


  ` The query's collection path.

  #### Declaration

  Swift

      public var path: String

- `


  ### [predicates](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery/Configuration#/s:22FirebaseFirestoreSwift0B5QueryV13ConfigurationV10predicatesSayAA0D9PredicateOGvp)


  ` The query's predicates.

  #### Declaration

  Swift

      public var predicates: [https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/QueryPredicate.html]

- `


  ### [decodingFailureStrategy](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery/Configuration#/s:22FirebaseFirestoreSwift0B5QueryV13ConfigurationV23decodingFailureStrategyAA08DecodinggH0Ovp)


  ` Undocumented

  #### Declaration

  Swift

      public var decodingFailureStrategy: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/DecodingFailureStrategy.html

- `


  ### [error](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery/Configuration#/s:22FirebaseFirestoreSwift0B5QueryV13ConfigurationV5errors5Error_pSgvp)


  ` If any errors occurred, they will be exposed here as well.

  #### Declaration

  Swift

      public var error: Error?