# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTask.md.txt

# FirebaseFirestore Framework Reference

# LoadBundleTask

    class LoadBundleTask : NSObject

Represents the task of loading a Firestore bundle. Observers can be registered with this task to
observe the bundle loading progress, as well as task completion and error events.
- `


  ### [addObserver(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTask#/c:objc(cs)FIRLoadBundleTask(im)addObserver:)


  ` Registers an observer to observe the progress updates, completion or error events.

  #### Declaration

  Swift

      func addObserver(_ observer: @escaping (https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTaskProgress.html) -> Void) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Type-Definitions.html#/c:FIRLoadBundleTask.h@T@FIRLoadBundleObserverHandle

  #### Return Value

  A handle to the registered observer which can be used to remove the observer once it is
  no longer needed.
- `


  ### [removeObserverWith(handle:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTask#/c:objc(cs)FIRLoadBundleTask(im)removeObserverWithHandle:)


  ` Removes a registered observer associated with the given handle. If no observer can be found, this
  will be a no-op.

  #### Declaration

  Swift

      func removeObserverWith(handle: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Type-Definitions.html#/c:FIRLoadBundleTask.h@T@FIRLoadBundleObserverHandle)

- `


  ### [removeAllObservers()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTask#/c:objc(cs)FIRLoadBundleTask(im)removeAllObservers)


  ` Removes all registered observers for this task.

  #### Declaration

  Swift

      func removeAllObservers()