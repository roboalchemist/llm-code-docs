# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRMemoryEagerGCSettings.md.txt

# FirebaseFirestore Framework Reference

# FIRMemoryEagerGCSettings


    @interface FIRMemoryEagerGCSettings
        : NSObject <NSCopying, https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols.html#/c:objc(pl)FIRMemoryGarbageCollectorSettings>

Configures the SDK to use an eager garbage collector for memory cache.

Once configured, the SDK will remove any Firestore documents from memory as soon as they are not
used by any active queries.

To use, create an instance using the initializer, then initialize
`MemoryCacheSettings` with this instance. This is the default garbage collector, so alternatively
you can use the default initializer of `MemoryCacheSettings`.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRMemoryEagerGCSettings#/c:objc(cs)FIRMemoryEagerGCSettings(im)init)

  `
  `  
  Creates an instance of `MemoryEagerGCSettings`.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;