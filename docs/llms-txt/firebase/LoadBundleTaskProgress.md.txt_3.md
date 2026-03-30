# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTaskProgress.md.txt

# FirebaseFirestore Framework Reference

# LoadBundleTaskProgress

    class LoadBundleTaskProgress : NSObject, @unchecked Sendable

Represents a progress update or a final state from loading bundles.
- `


  ### [documentsLoaded](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTaskProgress#/c:objc(cs)FIRLoadBundleTaskProgress(py)documentsLoaded)


  ` How many documents have been loaded.

  #### Declaration

  Swift

      var documentsLoaded: Int { get }

- `


  ### [totalDocuments](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTaskProgress#/c:objc(cs)FIRLoadBundleTaskProgress(py)totalDocuments)


  ` The total number of documents in the bundle. 0 if the bundle failed to parse.

  #### Declaration

  Swift

      var totalDocuments: Int { get }

- `


  ### [bytesLoaded](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTaskProgress#/c:objc(cs)FIRLoadBundleTaskProgress(py)bytesLoaded)


  ` How many bytes have been loaded.

  #### Declaration

  Swift

      var bytesLoaded: Int { get }

- `


  ### [totalBytes](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTaskProgress#/c:objc(cs)FIRLoadBundleTaskProgress(py)totalBytes)


  ` The total number of bytes in the bundle. 0 if the bundle failed to parse.

  #### Declaration

  Swift

      var totalBytes: Int { get }

- `


  ### [state](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTaskProgress#/c:objc(cs)FIRLoadBundleTaskProgress(py)state)


  ` The current state of `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTask.html`.

  #### Declaration

  Swift

      var state: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/LoadBundleTaskState.html { get }