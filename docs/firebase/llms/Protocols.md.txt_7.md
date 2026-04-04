# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols.md.txt

# FirebaseFirestore Framework Reference

# Protocols

The following protocols are available globally.
- `


  ### [FIRListenerRegistration](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols/FIRListenerRegistration)


  ` Represents a listener that can be removed by calling remove.

  #### Declaration

  Objective-C

      @protocol FIRListenerRegistration <NSObject>

- `


  ### [FIRLocalCacheSettings](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols#/c:objc(pl)FIRLocalCacheSettings)


  ` Marker protocol implemented by all supported cache settings.

  The two cache types supported are `PersistentCacheSettings` and `MemoryCacheSettings`. Custom
  implementation is not supported.

  #### Declaration

  Objective-C

      @protocol FIRLocalCacheSettings

- `


  ### [FIRMemoryGarbageCollectorSettings](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols#/c:objc(pl)FIRMemoryGarbageCollectorSettings)


  ` Marker protocol implemented by all supported garbage collector settings.

  The two cache types supported are `MemoryEagerGCSettings` and `MemoryLRUGCSettings`. Custom
  implementation is not supported.

  #### Declaration

  Objective-C

      @protocol FIRMemoryGarbageCollectorSettings