# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/DecodingFailureStrategy.md.txt

# FirebaseFirestoreSwift Framework Reference

# DecodingFailureStrategy

    public enum DecodingFailureStrategy

The strategy to use when an error occurs during mapping Firestore documents
to the target type of `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery.html`.
- `


  ### [ignore](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/DecodingFailureStrategy#/s:22FirebaseFirestoreSwift23DecodingFailureStrategyO6ignoreyA2CmF)


  ` Ignore any errors that occur when mapping Firestore documents.

  #### Declaration

  Swift

      case ignore

- `


  ### [raise](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/DecodingFailureStrategy#/s:22FirebaseFirestoreSwift23DecodingFailureStrategyO5raiseyA2CmF)


  ` Raise an error when mapping a Firestore document fails.

  #### Declaration

  Swift

      case raise