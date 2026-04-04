# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Type-Definitions.md.txt

# FirebaseFirestore Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [FIRDocumentSnapshotBlock](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Type-Definitions#/c:FIRDocumentReference.h@T@FIRDocumentSnapshotBlock)


  ` A block type used to handle snapshot updates.

  #### Declaration

  Objective-C

      typedef void (^FIRDocumentSnapshotBlock)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot *_Nullable,
                                               NSError *_Nullable)

- `


  ### [FIRLoadBundleObserverHandle](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Type-Definitions#/c:FIRLoadBundleTask.h@T@FIRLoadBundleObserverHandle)


  ` A handle associated with registered observers that can be used to remove them.

  #### Declaration

  Objective-C

      typedef NSInteger FIRLoadBundleObserverHandle

- `


  ### [FIRQuerySnapshotBlock](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Type-Definitions#/c:FIRQuery.h@T@FIRQuerySnapshotBlock)


  ` A block type used to handle failable snapshot method callbacks.

  #### Declaration

  Objective-C

      typedef void (^FIRQuerySnapshotBlock)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot *_Nullable,
                                            NSError *_Nullable)