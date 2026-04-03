# Source: https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigFetchAndActivateStatus.md.txt

# FirebaseRemoteConfig Framework Reference

# FIRRemoteConfigFetchAndActivateStatus

    enum FIRRemoteConfigFetchAndActivateStatus : NSInteger {}

Indicates whether updated data was successfully fetched and activated.
- `
  ``
  ``
  `

  ### [FIRRemoteConfigFetchAndActivateStatusSuccessFetchedFromRemote](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigFetchAndActivateStatus#/c:@E@FIRRemoteConfigFetchAndActivateStatus@FIRRemoteConfigFetchAndActivateStatusSuccessFetchedFromRemote)

  `
  `  
  The remote fetch succeeded and fetched data was activated.  

  #### Declaration

  Objective-C  

      FIRRemoteConfigFetchAndActivateStatusSuccessFetchedFromRemote

- `
  ``
  ``
  `

  ### [FIRRemoteConfigFetchAndActivateStatusSuccessUsingPreFetchedData](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigFetchAndActivateStatus#/c:@E@FIRRemoteConfigFetchAndActivateStatus@FIRRemoteConfigFetchAndActivateStatusSuccessUsingPreFetchedData)

  `
  `  
  The fetch and activate succeeded from already fetched but yet unexpired config data. You can
  control this using minimumFetchInterval property in FIRRemoteConfigSettings.  

  #### Declaration

  Objective-C  

      FIRRemoteConfigFetchAndActivateStatusSuccessUsingPreFetchedData

- `
  ``
  ``
  `

  ### [FIRRemoteConfigFetchAndActivateStatusError](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigFetchAndActivateStatus#/c:@E@FIRRemoteConfigFetchAndActivateStatus@FIRRemoteConfigFetchAndActivateStatusError)

  `
  `  
  The fetch and activate failed.  

  #### Declaration

  Objective-C  

      FIRRemoteConfigFetchAndActivateStatusError