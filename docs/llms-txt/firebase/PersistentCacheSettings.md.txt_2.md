# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/PersistentCacheSettings.md.txt

# FirebaseFirestore Framework Reference

# PersistentCacheSettings

    class PersistentCacheSettings : NSObject, NSCopying, https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/c:objc(pl)FIRLocalCacheSettings

Configures the SDK to use a persistent cache. Firestore documents and mutations are persisted
across App restart.

This is the default cache type unless explicitly specified otherwise.

To use, create an instance using one of the initializers, then set the instance to
`https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings.html#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings`, and use `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings.html` instance to configure Firestore
SDK.
- `


  ### [init()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/PersistentCacheSettings#/c:objc(cs)FIRPersistentCacheSettings(im)init)


  ` Creates `PersistentCacheSettings` with default cache size: 100MB.

  The cache size is not a hard limit, but a target for the SDK's garbage collector to work towards.

  #### Declaration

  Swift

      init()

- `


  ### [init(sizeBytes:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/PersistentCacheSettings#/c:objc(cs)FIRPersistentCacheSettings(im)initWithSizeBytes:)


  ` Creates `PersistentCacheSettings` with a custom cache size in bytes.

  The cache size is not a hard limit, but a target for the SDK's garbage collector to work towards.

  #### Declaration

  Swift

      init(sizeBytes size: NSNumber)