# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdapter.md.txt

# GoogleMobileAds Framework Reference

# GADMediationAdapter

    @protocol GADMediationAdapter <NSObject>

Receives messages and requests from the Google Mobile Ads SDK. Provides GMA to 3P SDK
communication.

Adapters are initialized on a background queue and should avoid using the main queue until
load time.
- `


  ### [+version](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(cm)version)


  ` Returns the adapter version.

  #### Declaration

  Objective-C

      + (https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions/GADVersionNumber.html)version;

- `


  ### [+adSDKVersion](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(cm)adSDKVersion)


  ` Returns the ad SDK version.

  #### Declaration

  Objective-C

      + (https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions/GADVersionNumber.html)adSDKVersion;

- `


  ### [+networkExtrasClass](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(cm)networkExtrasClass)


  ` The extras class that is used to specify additional parameters for a request to this ad network.
  Returns Nil if the network doesn't have publisher provided extras.

  #### Declaration

  Objective-C

      + (nullable Class<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras>)networkExtrasClass;

- `


  ### [+setUpWithConfiguration:completionHandler:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(cm)setUpWithConfiguration:completionHandler:)


  ` Tells the adapter to set up its underlying ad network SDK and perform any necessary prefetching
  or configuration work. The adapter must call completionHandler once the adapter can service ad
  requests, or if it encounters an error while setting up.

  #### Declaration

  Objective-C

      + (void)setUpWithConfiguration:
                  (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationServerConfiguration.html *)configuration
                   completionHandler:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADMediationAdapter.h@T@GADMediationAdapterSetUpCompletionBlock)
                                         completionHandler;

- `


  ### [-loadBannerForAdConfiguration:completionHandler:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(im)loadBannerForAdConfiguration:completionHandler:)


  ` Asks the adapter to load a banner ad with the provided ad configuration. The adapter must call
  back completionHandler with the loaded ad, or it may call back with an error. This method is
  called on the main thread, and completionHandler must be called back on the main thread.

  #### Declaration

  Objective-C

      - (void)loadBannerForAdConfiguration:
                  (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationBannerAdConfiguration.html *)adConfiguration
                         completionHandler:
                             (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADMediationAdapter.h@T@GADMediationBannerLoadCompletionHandler)
                                 completionHandler;

- `


  ### [-loadInterstitialForAdConfiguration:completionHandler:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(im)loadInterstitialForAdConfiguration:completionHandler:)


  ` Asks the adapter to load an interstitial ad with the provided ad configuration. The adapter
  must call back completionHandler with the loaded ad, or it may call back with an error. This
  method is called on the main thread, and completionHandler must be called back on the main
  thread.

  #### Declaration

  Objective-C

      - (void)
          loadInterstitialForAdConfiguration:
              (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADMediationInterstitialAdConfiguration *)adConfiguration
                           completionHandler:
                               (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADMediationAdapter.h@T@GADMediationInterstitialLoadCompletionHandler)
                                   completionHandler;

- `


  ### [-loadNativeAdForAdConfiguration:completionHandler:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(im)loadNativeAdForAdConfiguration:completionHandler:)


  ` Asks the adapter to load a native ad with the provided ad configuration. The adapter must call
  back completionHandler with the loaded ad, or it may call back with an error. This method is
  called on the main thread, and completionHandler must be called back on the main thread.

  #### Declaration

  Objective-C

      - (void)loadNativeAdForAdConfiguration:
                  (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationNativeAdConfiguration.html *)adConfiguration
                           completionHandler:
                               (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADMediationAdapter.h@T@GADMediationNativeLoadCompletionHandler)
                                   completionHandler;

- `


  ### [-loadRewardedAdForAdConfiguration:completionHandler:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(im)loadRewardedAdForAdConfiguration:completionHandler:)


  ` Asks the adapter to load a rewarded ad with the provided ad configuration. The adapter must
  call back completionHandler with the loaded ad, or it may call back with an error. This method
  is called on the main thread, and completionHandler must be called back on the main thread.

  #### Declaration

  Objective-C

      - (void)loadRewardedAdForAdConfiguration:
                  (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADMediationRewardedAdConfiguration *)adConfiguration
                             completionHandler:
                                 (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADMediationAdapter.h@T@GADMediationRewardedLoadCompletionHandler)
                                     completionHandler;

- `


  ### [+setUp](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(cm)setUp)


  ` Deprecated. To be removed before launch. Use setUpWithConfiguration:completionHandler:.

  #### Declaration

  Objective-C

      + (void)setUp;

- `


  ### [+updateConfiguration:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdapter#/c:objc(pl)GADMediationAdapter(cm)updateConfiguration:)


  ` Deprecated. To be removed before launch. Use setUpWithConfiguration:completionHandler:.

  #### Declaration

  Objective-C

      + (void)updateConfiguration:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationServerConfiguration.html *)configuration;