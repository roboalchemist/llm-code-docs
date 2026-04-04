# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigSettings.md.txt

# FirebaseRemoteConfig Framework Reference

# RemoteConfigSettings

    class RemoteConfigSettings : NSObject

Firebase Remote Config settings.
- `
  ``
  ``
  `

  ### [minimumFetchInterval](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigSettings#/c:objc(cs)FIRRemoteConfigSettings(py)minimumFetchInterval)

  `
  `  
  Indicates the default value in seconds to set for the minimum interval that needs to elapse
  before a fetch request can again be made to the Remote Config backend. After a fetch request to
  the backend has succeeded, no additional fetch requests to the backend will be allowed until the
  minimum fetch interval expires. Note that you can override this default on a per-fetch request
  basis using [RemoteConfig.fetch(withExpirationDuration:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig.html#/c:objc(cs)FIRRemoteConfig(im)fetchWithExpirationDuration:completionHandler:). For example, setting
  the expiration duration to 0 in the fetch request will override the `minimumFetchInterval` and
  allow the request to proceed.  

  #### Declaration

  Swift  

      var minimumFetchInterval: TimeInterval { get set }

- `
  ``
  ``
  `

  ### [fetchTimeout](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigSettings#/c:objc(cs)FIRRemoteConfigSettings(py)fetchTimeout)

  `
  `  
  Indicates the default value in seconds to abandon a pending fetch request made to the backend.
  This value is set for outgoing requests as the `timeoutIntervalForRequest` as well as the
  `timeoutIntervalForResource` on the `NSURLSession`'s configuration.  

  #### Declaration

  Swift  

      var fetchTimeout: TimeInterval { get set }