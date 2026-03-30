# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata/URLRetrievalStatus.md.txt

# FirebaseAILogic Framework Reference

# URLRetrievalStatus

    public struct URLRetrievalStatus : DecodableProtoEnum, Hashable

Status of the URL retrieval.
- `


  ### [success](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata/URLRetrievalStatus#/s:15FirebaseAILogic11URLMetadataV18URLRetrievalStatusV7successAEvpZ)


  ` The URL retrieval was successful.

  #### Declaration

  Swift

      public static let success: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata.html.URLRetrievalStatus

- `


  ### [error](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata/URLRetrievalStatus#/s:15FirebaseAILogic11URLMetadataV18URLRetrievalStatusV5errorAEvpZ)


  ` The URL retrieval failed.

  #### Declaration

  Swift

      public static let error: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata.html.URLRetrievalStatus

- `


  ### [paywall](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata/URLRetrievalStatus#/s:15FirebaseAILogic11URLMetadataV18URLRetrievalStatusV7paywallAEvpZ)


  ` The URL retrieval failed because the content is behind a paywall.

  #### Declaration

  Swift

      public static let paywall: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata.html.URLRetrievalStatus

- `


  ### [unsafe](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata/URLRetrievalStatus#/s:15FirebaseAILogic11URLMetadataV18URLRetrievalStatusV6unsafeAEvpZ)


  ` The URL retrieval failed because the content is unsafe.

  #### Declaration

  Swift

      public static let unsafe: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata.html.URLRetrievalStatus

- `


  ### [rawValue](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata/URLRetrievalStatus#/s:15FirebaseAILogic11URLMetadataV18URLRetrievalStatusV8rawValueSSvp)


  ` Returns the raw string representation of the `URLRetrievalStatus` value.

  #### Declaration

  Swift

      public let rawValue: String