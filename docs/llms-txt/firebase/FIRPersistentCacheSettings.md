# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRPersistentCacheSettings.md.txt

# FirebaseFirestore Framework Reference

# FIRPersistentCacheSettings


    @interface FIRPersistentCacheSettings
        : NSObject <NSCopying, https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols.html#/c:objc(pl)FIRLocalCacheSettings>

Configures the SDK to use a persistent cache. Firestore documents and mutations are persisted
across App restart.

This is the default cache type unless explicitly specified otherwise.

To use, create an instance using one of the initializers, then set the instance to
`FirestoreSettings.cacheSettings`, and use `FirestoreSettings` instance to configure Firestore
SDK.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRPersistentCacheSettings#/c:objc(cs)FIRPersistentCacheSettings(im)init)

  `
  `  
  Creates `PersistentCacheSettings` with default cache size: 100MB.

  The cache size is not a hard limit, but a target for the SDK's garbage collector to work towards.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-initWithSizeBytes:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRPersistentCacheSettings#/c:objc(cs)FIRPersistentCacheSettings(im)initWithSizeBytes:)

  `
  `  
  Creates `PersistentCacheSettings` with a custom cache size in bytes.

  The cache size is not a hard limit, but a target for the SDK's garbage collector to work towards.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithSizeBytes:(nonnull NSNumber *)size;