# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds.md.txt

# GoogleMobileAds Framework Reference

# GADMobileAds

    @interface GADMobileAds : NSObject

Google Mobile Ads SDK settings.
- `


  ### [+sharedInstance](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(cm)sharedInstance)


  ` Returns the shared GADMobileAds instance.

  #### Declaration

  Objective-C

      + (nonnull GADMobileAds *)sharedInstance;

- `


  ### [+disableAutomatedInAppPurchaseReporting](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(cm)disableAutomatedInAppPurchaseReporting)


  ` Disables automated in app purchase (IAP) reporting. Must be called before any IAP transaction is
  initiated. IAP reporting is used to track IAP ad conversions. Do not disable reporting if you
  use IAP ads.

  #### Declaration

  Objective-C

      + (void)disableAutomatedInAppPurchaseReporting;

- `


  ### [+disableSDKCrashReporting](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(cm)disableSDKCrashReporting)


  ` Disables automated SDK crash reporting. If not called, the SDK records the original exception
  handler if available and registers a new exception handler. The new exception handler only
  reports SDK related exceptions and calls the recorded original exception handler.

  #### Declaration

  Objective-C

      + (void)disableSDKCrashReporting;

- `


  ### [applicationVolume](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(py)applicationVolume)


  ` The application's audio volume. Affects audio volumes of all ads relative to other audio output.
  Valid ad volume values range from 0.0 (silent) to 1.0 (current device volume). Use this method
  only if your application has its own volume controls (e.g., custom music or sound effect
  volumes). Defaults to 1.0.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) float applicationVolume;

- `


  ### [applicationMuted](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(py)applicationMuted)


  ` Indicates whether the application's audio is muted. Affects initial mute state for all ads. Use
  this method only if your application has its own volume controls (e.g., custom music or sound
  effect muting). Defaults to NO.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL applicationMuted;

- `


  ### [audioVideoManager](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(py)audioVideoManager)


  ` Manages the Google Mobile Ads SDK's audio and video settings.

  #### Declaration

  Objective-C

      @property (readonly, strong, nonatomic, nonnull)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAudioVideoManager.html *audioVideoManager;

- `


  ### [requestConfiguration](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(py)requestConfiguration)


  ` Request configuration that is common to all requests.

  #### Declaration

  Objective-C

      @property (readonly, strong, nonatomic, nonnull)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequestConfiguration.html *requestConfiguration;

- `


  ### [initializationStatus](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(py)initializationStatus)


  ` Initialization status of the ad networks available to the Google Mobile Ads SDK.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nonnull)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInitializationStatus.html *initializationStatus;

- `


  ### [-isSDKVersionAtLeastMajor:minor:patch:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(im)isSDKVersionAtLeastMajor:minor:patch:)


  ` Returns YES if the current SDK version is at least \|major\|.\|minor\|.\|patch\|. This method can be
  used by libraries that depend on a specific minimum version of the Google Mobile Ads SDK to warn
  developers if they have an incompatible version.

  Available in Google Mobile Ads SDK 7.10 and onwards. Before calling this method check if the
  GADMobileAds's shared instance responds to this method. Calling this method on a Google Mobile
  Ads SDK lower than 7.10 can crash the app.

  #### Declaration

  Objective-C

      - (BOOL)isSDKVersionAtLeastMajor:(NSInteger)major
                                 minor:(NSInteger)minor
                                 patch:(NSInteger)patch;

- `


  ### [-startWithCompletionHandler:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(im)startWithCompletionHandler:)


  ` Starts the Google Mobile Ads SDK. Call this method as early as possible to reduce latency on the
  session's first ad request. Calls completionHandler when the GMA SDK and all mediation networks
  are fully set up or if set-up times out. The Google Mobile Ads SDK starts on the first ad
  request if this method is not called.

  #### Declaration

  Objective-C

      - (void)startWithCompletionHandler:
          (nullable https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADMobileAds.h@T@GADInitializationCompletionHandler)completionHandler;

[## Deprecated](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds#/Deprecated)

- `


  ### [+configureWithApplicationID:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds#/c:objc(cs)GADMobileAds(cm)configureWithApplicationID:)


  ` Configures the SDK using the settings associated with the given application ID.

  #### Declaration

  Objective-C

      + (void)configureWithApplicationID:(nonnull NSString *)applicationID;