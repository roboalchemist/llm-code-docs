# Source: https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageObservableTask.md.txt

# FirebaseStorage Framework Reference

# FIRStorageObservableTask


    @interface FIRStorageObservableTask : https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTask.html

An extended `StorageTask` providing observable semantics that can be used for responding to changes
in task state.
Observers produce a `StorageHandle`, which is used to keep track of and remove specific
observers at a later date.
- `
  ``
  ``
  `

  ### [-observeStatus:handler:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageObservableTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageObservableTask(im)observeStatus:handler:)

  `
  `  
  Observes changes in the upload status: Resume, Pause, Progress, Success, and Failure.
  \\param status The `StorageTaskStatus` change to observe.

  \\param handler A callback that fires every time the status event occurs,
  containing a `StorageTaskSnapshot` describing task state.

  returns:
  A task handle that can be used to remove the observer at a later date.  

  #### Declaration

  Objective-C  

      - (NSString *_Nonnull)
          observeStatus:(enum https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Enums/FIRStorageTaskStatus.html)status
                handler:(void (^_Nonnull)(https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTaskSnapshot.html *_Nonnull))handler;

- `
  ``
  ``
  `

  ### [-removeObserverWithHandle:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageObservableTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageObservableTask(im)removeObserverWithHandle:)

  `
  `  
  Removes the single observer with the provided handle.
  \\param handle The handle of the task to remove.  

  #### Declaration

  Objective-C  

      - (void)removeObserverWithHandle:(NSString *_Nonnull)handle;

- `
  ``
  ``
  `

  ### [-removeAllObserversForStatus:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageObservableTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageObservableTask(im)removeAllObserversForStatus:)

  `
  `  
  Removes all observers for a single status.
  \\param status A `StorageTaskStatus` to remove all listeners for.  

  #### Declaration

  Objective-C  

      - (void)removeAllObserversForStatus:(enum https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Enums/FIRStorageTaskStatus.html)status;

- `
  ``
  ``
  `

  ### [-removeAllObservers](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageObservableTask#/c:@M@FirebaseStorage@objc(cs)FIRStorageObservableTask(im)removeAllObservers)

  `
  `  
  Removes all observers.  

  #### Declaration

  Objective-C  

      - (void)removeAllObservers;