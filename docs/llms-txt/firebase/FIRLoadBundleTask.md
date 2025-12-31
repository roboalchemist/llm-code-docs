# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTask.md.txt

# FirebaseFirestore Framework Reference

# FIRLoadBundleTask


    @interface FIRLoadBundleTask : NSObject

Represents the task of loading a Firestore bundle. Observers can be registered with this task to
observe the bundle loading progress, as well as task completion and error events.
- `
  ``
  ``
  `

  ### [-addObserver:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTask#/c:objc(cs)FIRLoadBundleTask(im)addObserver:)

  `
  `  
  Registers an observer to observe the progress updates, completion or error events.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Type-Definitions.html#/c:FIRLoadBundleTask.h@T@FIRLoadBundleObserverHandle)addObserver:
          (nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTaskProgress.html *_Nonnull))observer;

  #### Return Value

  A handle to the registered observer which can be used to remove the observer once it is
  no longer needed.
- `
  ``
  ``
  `

  ### [-removeObserverWithHandle:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTask#/c:objc(cs)FIRLoadBundleTask(im)removeObserverWithHandle:)

  `
  `  
  Removes a registered observer associated with the given handle. If no observer can be found, this
  will be a no-op.  

  #### Declaration

  Objective-C  

      - (void)removeObserverWithHandle:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Type-Definitions.html#/c:FIRLoadBundleTask.h@T@FIRLoadBundleObserverHandle)handle;

- `
  ``
  ``
  `

  ### [-removeAllObservers](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTask#/c:objc(cs)FIRLoadBundleTask(im)removeAllObservers)

  `
  `  
  Removes all registered observers for this task.  

  #### Declaration

  Objective-C  

      - (void)removeAllObservers;