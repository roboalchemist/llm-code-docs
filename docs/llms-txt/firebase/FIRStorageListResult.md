# Source: https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageListResult.md.txt

# FirebaseStorage Framework Reference

# FIRStorageListResult


    @interface FIRStorageListResult : NSObject

Contains the prefixes and items returned by a `StorageReference.list()` call.
- `
  ``
  ``
  `

  ### [prefixes](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageListResult#/c:@M@FirebaseStorage@objc(cs)FIRStorageListResult(py)prefixes)

  `
  `  
  The prefixes (folders) returned by a `list()` operation.

  returns:
  A list of prefixes (folders).  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference.html *> *_Nonnull prefixes;

- `
  ``
  ``
  `

  ### [items](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageListResult#/c:@M@FirebaseStorage@objc(cs)FIRStorageListResult(py)items)

  `
  `  
  The objects (files) returned by a `list()` operation.

  returns:
  A page token if more results are available.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference.html *> *_Nonnull items;

- `
  ``
  ``
  `

  ### [pageToken](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageListResult#/c:@M@FirebaseStorage@objc(cs)FIRStorageListResult(py)pageToken)

  `
  `  
  Returns a token that can be used to resume a previous `list()` operation. `nil`
  indicates that there are no more results.

  returns:
  A page token if more results are available.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nullable pageToken;

- `
  ``
  ``
  `

  ### [-copy](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageListResult#/c:@M@FirebaseStorage@objc(cs)FIRStorageListResult(im)copy)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      - (id _Nonnull)copy SWIFT_WARN_UNUSED_RESULT;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageListResult#/c:@M@FirebaseStorage@objc(cs)FIRStorageListResult(im)init)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init SWIFT_UNAVAILABLE;

- `
  ``
  ``
  `

  ### [+new](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageListResult#/c:@M@FirebaseStorage@objc(cs)FIRStorageListResult(cm)new)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)new SWIFT_UNAVAILABLE_MSG("-init is unavailable");