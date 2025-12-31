# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery/Configuration.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/FirestoreQuery/Configuration.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery/Configuration.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/FirestoreQuery/Configuration.md.txt

# FirebaseFirestore Framework Reference

# Configuration

    public struct Configuration

The query's configurable properties.
- `
  ``
  ``
  `

  ### [path](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/FirestoreQuery/Configuration#/s:17FirebaseFirestore0B5QueryV13ConfigurationV4pathSSvp)

  `
  `  
  The query's collection path.  

  #### Declaration

  Swift  

      public var path: String

- `
  ``
  ``
  `

  ### [predicates](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/FirestoreQuery/Configuration#/s:17FirebaseFirestore0B5QueryV13ConfigurationV10predicatesSayAA0C9PredicateOGvp)

  `
  `  
  The query's predicates.  

  #### Declaration

  Swift  

      public var predicates: [https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate.html]

- `
  ``
  ``
  `

  ### [decodingFailureStrategy](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/FirestoreQuery/Configuration#/s:17FirebaseFirestore0B5QueryV13ConfigurationV23decodingFailureStrategyAA08DecodingfG0Ovp)

  `
  `  
  The strategy to use in case there was a problem during the decoding phase.  

  #### Declaration

  Swift  

      public var decodingFailureStrategy: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/DecodingFailureStrategy.html

- `
  ``
  ``
  `

  ### [error](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/FirestoreQuery/Configuration#/s:17FirebaseFirestore0B5QueryV13ConfigurationV5errors5Error_pSgvp)

  `
  `  
  If any errors occurred, they will be exposed here as well.  

  #### Declaration

  Swift  

      public var error: Error?

- `
  ``
  ``
  `

  ### [animation](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/FirestoreQuery/Configuration#/s:17FirebaseFirestore0B5QueryV13ConfigurationV9animation7SwiftUI9AnimationVSgvp)

  `
  `  
  The type of animation to apply when updating the view. If this is omitted then no
  animations are fired.  

  #### Declaration

  Swift  

      public var animation: Animation?