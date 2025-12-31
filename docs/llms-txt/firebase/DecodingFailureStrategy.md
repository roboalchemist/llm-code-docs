# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/DecodingFailureStrategy.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/DecodingFailureStrategy.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/DecodingFailureStrategy.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/DecodingFailureStrategy.md.txt

# FirebaseFirestore Framework Reference

# DecodingFailureStrategy

    public enum DecodingFailureStrategy

The strategy to use when an error occurs during mapping Firestore documents
to the target type of [FirestoreQuery](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/FirestoreQuery.html).
- `
  ``
  ``
  `

  ### [ignore](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/DecodingFailureStrategy#/s:17FirebaseFirestore23DecodingFailureStrategyO6ignoreyA2CmF)

  `
  `  
  Ignore any errors that occur when mapping Firestore documents.  

  #### Declaration

  Swift  

      case ignore

- `
  ``
  ``
  `

  ### [raise](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/DecodingFailureStrategy#/s:17FirebaseFirestore23DecodingFailureStrategyO5raiseyA2CmF)

  `
  `  
  Raise an error when mapping a Firestore document fails.  

  #### Declaration

  Swift  

      case raise