# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchStatus.md.txt

# FirebaseRemoteConfig Framework Reference

# RemoteConfigFetchStatus

    enum RemoteConfigFetchStatus : Int, @unchecked Sendable

Indicates whether updated data was successfully fetched.
- `
  ``
  ``
  `

  ### [noFetchYet](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchStatus#/c:@E@FIRRemoteConfigFetchStatus@FIRRemoteConfigFetchStatusNoFetchYet)

  `
  `  
  Config has never been fetched.  

  #### Declaration

  Swift  

      case noFetchYet = 0

- `
  ``
  ``
  `

  ### [success](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchStatus#/c:@E@FIRRemoteConfigFetchStatus@FIRRemoteConfigFetchStatusSuccess)

  `
  `  
  Config fetch succeeded.  

  #### Declaration

  Swift  

      case success = 1

- `
  ``
  ``
  `

  ### [failure](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchStatus#/c:@E@FIRRemoteConfigFetchStatus@FIRRemoteConfigFetchStatusFailure)

  `
  `  
  Config fetch failed.  

  #### Declaration

  Swift  

      case failure = 2

- `
  ``
  ``
  `

  ### [throttled](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchStatus#/c:@E@FIRRemoteConfigFetchStatus@FIRRemoteConfigFetchStatusThrottled)

  `
  `  
  Config fetch was throttled.  

  #### Declaration

  Swift  

      case throttled = 3