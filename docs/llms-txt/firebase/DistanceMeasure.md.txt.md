# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DistanceMeasure.md.txt

# FirebaseFirestore Framework Reference

# DistanceMeasure

    public struct DistanceMeasure : Sendable, Equatable, Hashable

Represents the distance measure to be used in a vector similarity search.
- `


  ### [euclidean](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DistanceMeasure#/s:17FirebaseFirestore15DistanceMeasureV9euclideanACvpZ)


  ` The Euclidean distance measure.

  #### Declaration

  Swift

      public static let euclidean: DistanceMeasure

- `


  ### [cosine](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DistanceMeasure#/s:17FirebaseFirestore15DistanceMeasureV6cosineACvpZ)


  ` The Cosine distance measure.

  #### Declaration

  Swift

      public static let cosine: DistanceMeasure

- `


  ### [dotProduct](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DistanceMeasure#/s:17FirebaseFirestore15DistanceMeasureV10dotProductACvpZ)


  ` The Dot Product distance measure.

  #### Declaration

  Swift

      public static let dotProduct: DistanceMeasure