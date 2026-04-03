# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMobileAds.md.txt

# GoogleMobileAds Framework Reference

# GADMobileAds

    class GADMobileAds : NSObject

Google Mobile Ads SDK settings.
- `
  ``
  ``
  `

  ### [sharedInstance()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(cm)sharedInstance)

  `
  `  
  Returns the shared GADMobileAds instance.  

  #### Declaration

  Swift  

      class func sharedInstance() -> GADMobileAds

- `
  ``
  ``
  `

  ### [disableAutomatedInAppPurchaseReporting()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(cm)disableAutomatedInAppPurchaseReporting)

  `
  `  
  Disables automated in app purchase (IAP) reporting. Must be called before any IAP transaction is
  initiated. IAP reporting is used to track IAP ad conversions. Do not disable reporting if you
  use IAP ads.  

  #### Declaration

  Swift  

      class func disableAutomatedInAppPurchaseReporting()

- `
  ``
  ``
  `

  ### [disableSDKCrashReporting()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(cm)disableSDKCrashReporting)

  `
  `  
  Disables automated SDK crash reporting. If not called, the SDK records the original exception
  handler if available and registers a new exception handler. The new exception handler only
  reports SDK related exceptions and calls the recorded original exception handler.  

  #### Declaration

  Swift  

      class func disableSDKCrashReporting()

- `
  ``
  ``
  `

  ### [applicationVolume](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(py)applicationVolume)

  `
  `  
  The application's audio volume. Affects audio volumes of all ads relative to other audio output.
  Valid ad volume values range from 0.0 (silent) to 1.0 (current device volume). Use this method
  only if your application has its own volume controls (e.g., custom music or sound effect
  volumes). Defaults to 1.0.  

  #### Declaration

  Swift  

      var applicationVolume: Float { get set }

- `
  ``
  ``
  `

  ### [applicationMuted](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(py)applicationMuted)

  `
  `  
  Indicates whether the application's audio is muted. Affects initial mute state for all ads. Use
  this method only if your application has its own volume controls (e.g., custom music or sound
  effect muting). Defaults to NO.  

  #### Declaration

  Swift  

      var applicationMuted: Bool { get set }

- `
  ``
  ``
  `

  ### [audioVideoManager](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(py)audioVideoManager)

  `
  `  
  Manages the Google Mobile Ads SDK's audio and video settings.  

  #### Declaration

  Swift  

      var audioVideoManager: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAudioVideoManager.html { get }

- `
  ``
  ``
  `

  ### [requestConfiguration](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(py)requestConfiguration)

  `
  `  
  Request configuration that is common to all requests.  

  #### Declaration

  Swift  

      var requestConfiguration: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequestConfiguration.html { get }

- `
  ``
  ``
  `

  ### [initializationStatus](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(py)initializationStatus)

  `
  `  
  Initialization status of the ad networks available to the Google Mobile Ads SDK.  

  #### Declaration

  Swift  

      var initializationStatus: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInitializationStatus.html { get }

- `
  ``
  ``
  `

  ### [isSDKVersion(atLeastMajor:minor:patch:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(im)isSDKVersionAtLeastMajor:minor:patch:)

  `
  `  
  Returns YES if the current SDK version is at least \|major\|.\|minor\|.\|patch\|. This method can be
  used by libraries that depend on a specific minimum version of the Google Mobile Ads SDK to warn
  developers if they have an incompatible version.

  Available in Google Mobile Ads SDK 7.10 and onwards. Before calling this method check if the
  GADMobileAds's shared instance responds to this method. Calling this method on a Google Mobile
  Ads SDK lower than 7.10 can crash the app.  

  #### Declaration

  Swift  

      func isSDKVersion(atLeastMajor major: Int, minor: Int, patch: Int) -> Bool

- `
  ``
  ``
  `

  ### [start(completionHandler:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(im)startWithCompletionHandler:)

  `
  `  
  Starts the Google Mobile Ads SDK. Call this method as early as possible to reduce latency on the
  session's first ad request. Calls completionHandler when the GMA SDK and all mediation networks
  are fully set up or if set-up times out. The Google Mobile Ads SDK starts on the first ad
  request if this method is not called.  

  #### Declaration

  Swift  

      func start(completionHandler: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADMobileAds.h@T@GADInitializationCompletionHandler? = nil)

[## Deprecated](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMobileAds#/Deprecated)

- `
  ``
  ``
  `

  ### [configure(withApplicationID:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(cm)configureWithApplicationID:)

  `
  `  
  Configures the SDK using the settings associated with the given application ID.  

  #### Declaration

  Swift  

      class func configure(withApplicationID applicationID: String)