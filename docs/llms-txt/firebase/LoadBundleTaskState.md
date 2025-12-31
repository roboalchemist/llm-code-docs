# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/LoadBundleTaskState.md.txt

# FirebaseFirestore Framework Reference

# LoadBundleTaskState

    enum LoadBundleTaskState : Int, @unchecked Sendable

Represents the state of bundle loading tasks.

Both `error` and `inProgress` are final states: the task will be in either an aborted or
completed state and there will be no more subsequent updates.
- `
  ``
  ``
  `

  ### [error](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/LoadBundleTaskState#/c:@E@FIRLoadBundleTaskState@FIRLoadBundleTaskStateError)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case error = 0

- `
  ``
  ``
  `

  ### [inProgress](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/LoadBundleTaskState#/c:@E@FIRLoadBundleTaskState@FIRLoadBundleTaskStateInProgress)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case inProgress = 1

- `
  ``
  ``
  `

  ### [success](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/LoadBundleTaskState#/c:@E@FIRLoadBundleTaskState@FIRLoadBundleTaskStateSuccess)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case success = 2