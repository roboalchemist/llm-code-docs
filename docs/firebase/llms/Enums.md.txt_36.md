# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums.md.txt

# FirebaseFirestoreSwift Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [FirestoreDecodingError](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/FirestoreDecodingError)


  ` Undocumented

  #### Declaration

  Swift

      public enum FirestoreDecodingError : Error

- `


  ### [FirestoreEncodingError](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/FirestoreEncodingError)


  ` Undocumented

  #### Declaration

  Swift

      public enum FirestoreEncodingError : Error

- `


  ### [DecodingFailureStrategy](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/DecodingFailureStrategy)


  ` The strategy to use when an error occurs during mapping Firestore documents
  to the target type of `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery`.

  #### Declaration

  Swift

      public enum DecodingFailureStrategy

- `


  ### [QueryPredicate](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/QueryPredicate)


  ` Query predicates that can be used to filter results fetched by `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery`.

  Construct predicates using one of the following ways:

      let onlyFavourites: QueryPredicate = .whereField("isFavourite", isEqualTo: true)
      let onlyFavourites2: QueryPredicate = .isEqualTo("isFavourite", true)
      let onlyFavourites3: QueryPredicate = .where("isFavourite", isEqualTo: true)

  #### Declaration

  Swift

      public enum QueryPredicate