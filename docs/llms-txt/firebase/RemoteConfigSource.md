# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigSource.md.txt

# FirebaseRemoteConfig Framework Reference

# RemoteConfigSource

    enum RemoteConfigSource : Int, @unchecked Sendable

Enumerated value that indicates the source of Remote Config data. Data can come from
the Remote Config service, the DefaultConfig that is available when the app is first installed,
or a static initialized value if data is not available from the service or DefaultConfig.
- `
  ``
  ``
  `

  ### [remote](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigSource#/c:@E@FIRRemoteConfigSource@FIRRemoteConfigSourceRemote)

  `
  `  
  \< The data source is the Remote Config service.  

  #### Declaration

  Swift  

      case remote = 0

- `
  ``
  ``
  `

  ### [default](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigSource#/c:@E@FIRRemoteConfigSource@FIRRemoteConfigSourceDefault)

  `
  `  
  \< The data source is the DefaultConfig defined for this app.  

  #### Declaration

  Swift  

      case `default` = 1

- `
  ``
  ``
  `

  ### [static](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigSource#/c:@E@FIRRemoteConfigSource@FIRRemoteConfigSourceStatic)

  `
  `  
  \< The data doesn't exist, return a static initialized value.  

  #### Declaration

  Swift  

      case `static` = 2