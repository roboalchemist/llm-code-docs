# Source: https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigSource.md.txt

# FirebaseRemoteConfig Framework Reference

# FIRRemoteConfigSource

    enum FIRRemoteConfigSource : NSInteger {}

Enumerated value that indicates the source of Remote Config data. Data can come from
the Remote Config service, the DefaultConfig that is available when the app is first installed,
or a static initialized value if data is not available from the service or DefaultConfig.
- `
  ``
  ``
  `

  ### [FIRRemoteConfigSourceRemote](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigSource#/c:@E@FIRRemoteConfigSource@FIRRemoteConfigSourceRemote)

  `
  `  
  \< The data source is the Remote Config service.  

  #### Declaration

  Objective-C  

      FIRRemoteConfigSourceRemote

- `
  ``
  ``
  `

  ### [FIRRemoteConfigSourceDefault](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigSource#/c:@E@FIRRemoteConfigSource@FIRRemoteConfigSourceDefault)

  `
  `  
  \< The data source is the DefaultConfig defined for this app.  

  #### Declaration

  Objective-C  

      FIRRemoteConfigSourceDefault

- `
  ``
  ``
  `

  ### [FIRRemoteConfigSourceStatic](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigSource#/c:@E@FIRRemoteConfigSource@FIRRemoteConfigSourceStatic)

  `
  `  
  \< The data doesn't exist, return a static initialized value.  

  #### Declaration

  Objective-C  

      FIRRemoteConfigSourceStatic