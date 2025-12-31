# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchAndActivateStatus.md.txt

# FirebaseRemoteConfig Framework Reference

# RemoteConfigFetchAndActivateStatus

    enum RemoteConfigFetchAndActivateStatus : Int, @unchecked Sendable

Indicates whether updated data was successfully fetched and activated.
- `
  ``
  ``
  `

  ### [successFetchedFromRemote](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchAndActivateStatus#/c:@E@FIRRemoteConfigFetchAndActivateStatus@FIRRemoteConfigFetchAndActivateStatusSuccessFetchedFromRemote)

  `
  `  
  The remote fetch succeeded and fetched data was activated.  

  #### Declaration

  Swift  

      case successFetchedFromRemote = 0

- `
  ``
  ``
  `

  ### [successUsingPreFetchedData](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchAndActivateStatus#/c:@E@FIRRemoteConfigFetchAndActivateStatus@FIRRemoteConfigFetchAndActivateStatusSuccessUsingPreFetchedData)

  `
  `  
  The fetch and activate succeeded from already fetched but yet unexpired config data. You can
  control this using minimumFetchInterval property in FIRRemoteConfigSettings.  

  #### Declaration

  Swift  

      case successUsingPreFetchedData = 1

- `
  ``
  ``
  `

  ### [error](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchAndActivateStatus#/c:@E@FIRRemoteConfigFetchAndActivateStatus@FIRRemoteConfigFetchAndActivateStatusError)

  `
  `  
  The fetch and activate failed.  

  #### Declaration

  Swift  

      case error = 2