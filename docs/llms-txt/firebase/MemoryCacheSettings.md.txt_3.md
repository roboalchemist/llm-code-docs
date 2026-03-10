# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryCacheSettings.md.txt

# FirebaseFirestore Framework Reference

# MemoryCacheSettings

    class MemoryCacheSettings : NSObject, NSCopying, https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/c:objc(pl)FIRLocalCacheSettings

Configures the SDK to use a memory cache. Firestore documents and mutations are NOT persisted
across App restart.

To use, create an instance using one of the initializer, then set the instance to
`https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings.html#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings`, and use `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings.html` instance to configure Firestore
SDK.
- `


  ### [init()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryCacheSettings#/c:objc(cs)FIRMemoryCacheSettings(im)init)


  ` Creates an instance of `MemoryCacheSettings`.

  #### Declaration

  Swift

      init()

- `


  ### [init(garbageCollectorSettings:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryCacheSettings#/c:objc(cs)FIRMemoryCacheSettings(im)initWithGarbageCollectorSettings:)


  ` Creates an instance of `MemoryCacheSettings` with given `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/c:objc(pl)FIRMemoryGarbageCollectorSettings` to
  custom the garbage collector.

  #### Declaration

  Swift

      init(garbageCollectorSettings settings: any NSObjectProtocol & https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/c:objc(pl)FIRMemoryGarbageCollectorSettings)