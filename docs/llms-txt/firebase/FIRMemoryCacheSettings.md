# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRMemoryCacheSettings.md.txt

# FirebaseFirestore Framework Reference

# FIRMemoryCacheSettings


    @interface FIRMemoryCacheSettings : NSObject <NSCopying, https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols.html#/c:objc(pl)FIRLocalCacheSettings>

Configures the SDK to use a memory cache. Firestore documents and mutations are NOT persisted
across App restart.

To use, create an instance using one of the initializer, then set the instance to
`FirestoreSettings.cacheSettings`, and use `FirestoreSettings` instance to configure Firestore
SDK.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRMemoryCacheSettings#/c:objc(cs)FIRMemoryCacheSettings(im)init)

  `
  `  
  Creates an instance of `MemoryCacheSettings`.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-initWithGarbageCollectorSettings:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRMemoryCacheSettings#/c:objc(cs)FIRMemoryCacheSettings(im)initWithGarbageCollectorSettings:)

  `
  `  
  Creates an instance of `MemoryCacheSettings` with given `MemoryGarbageCollectorSettings` to
  custom the garbage collector.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithGarbageCollectorSettings:
          (nonnull id<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols.html#/c:objc(pl)FIRMemoryGarbageCollectorSettings, NSObject>)settings;