# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTaskProgress.md.txt

# FirebaseFirestore Framework Reference

# FIRLoadBundleTaskProgress


    @interface FIRLoadBundleTaskProgress : NSObject

Represents a progress update or a final state from loading bundles.
- `
  ``
  ``
  `

  ### [documentsLoaded](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTaskProgress#/c:objc(cs)FIRLoadBundleTaskProgress(py)documentsLoaded)

  `
  `  
  How many documents have been loaded.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSInteger documentsLoaded;

- `
  ``
  ``
  `

  ### [totalDocuments](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTaskProgress#/c:objc(cs)FIRLoadBundleTaskProgress(py)totalDocuments)

  `
  `  
  The total number of documents in the bundle. 0 if the bundle failed to parse.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSInteger totalDocuments;

- `
  ``
  ``
  `

  ### [bytesLoaded](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTaskProgress#/c:objc(cs)FIRLoadBundleTaskProgress(py)bytesLoaded)

  `
  `  
  How many bytes have been loaded.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSInteger bytesLoaded;

- `
  ``
  ``
  `

  ### [totalBytes](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTaskProgress#/c:objc(cs)FIRLoadBundleTaskProgress(py)totalBytes)

  `
  `  
  The total number of bytes in the bundle. 0 if the bundle failed to parse.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSInteger totalBytes;

- `
  ``
  ``
  `

  ### [state](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTaskProgress#/c:objc(cs)FIRLoadBundleTaskProgress(py)state)

  `
  `  
  The current state of `LoadBundleTask`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRLoadBundleTaskState.html state;