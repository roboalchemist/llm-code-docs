# Source: https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigSettings.md.txt

# FirebaseRemoteConfig Framework Reference

# FIRRemoteConfigSettings


    @interface FIRRemoteConfigSettings : NSObject

Firebase Remote Config settings.
- `
  ``
  ``
  `

  ### [minimumFetchInterval](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigSettings#/c:objc(cs)FIRRemoteConfigSettings(py)minimumFetchInterval)

  `
  `  
  Indicates the default value in seconds to set for the minimum interval that needs to elapse
  before a fetch request can again be made to the Remote Config backend. After a fetch request to
  the backend has succeeded, no additional fetch requests to the backend will be allowed until the
  minimum fetch interval expires. Note that you can override this default on a per-fetch request
  basis using `RemoteConfig.fetch(withExpirationDuration:)`. For example, setting
  the expiration duration to 0 in the fetch request will override the `minimumFetchInterval` and
  allow the request to proceed.  

  #### Declaration

  Objective-C  

      @property (nonatomic) NSTimeInterval minimumFetchInterval;

- `
  ``
  ``
  `

  ### [fetchTimeout](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigSettings#/c:objc(cs)FIRRemoteConfigSettings(py)fetchTimeout)

  `
  `  
  Indicates the default value in seconds to abandon a pending fetch request made to the backend.
  This value is set for outgoing requests as the `timeoutIntervalForRequest` as well as the
  `timeoutIntervalForResource` on the `NSURLSession`'s configuration.  

  #### Declaration

  Objective-C  

      @property (nonatomic) NSTimeInterval fetchTimeout;