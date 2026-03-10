# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter.md.txt

# GoogleMobileAds Framework Reference

# GADMRewardBasedVideoAdNetworkAdapter

    @protocol GADMRewardBasedVideoAdNetworkAdapter <NSObject>

Your adapter must conform to this protocol to provide reward based video ads.
- `


  ### [+adapterVersion](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter#/c:objc(pl)GADMRewardBasedVideoAdNetworkAdapter(cm)adapterVersion)


  ` Returns a version string for the adapter. It can be any string that uniquely identifies the
  version of your adapter. For example, 1.0, or simply a date such as 20110915.

  #### Declaration

  Objective-C

      + (NSString *)adapterVersion;

- `


  ### [+networkExtrasClass](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter#/c:objc(pl)GADMRewardBasedVideoAdNetworkAdapter(cm)networkExtrasClass)


  ` The extras class that is used to specify additional parameters for a request to this ad network.
  Returns Nil if the network does not have extra settings for publishers to send.

  #### Declaration

  Objective-C

      + (Class<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras>)networkExtrasClass;

- `


  ### [-initWithRewardBasedVideoAdNetworkConnector:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter#/c:objc(pl)GADMRewardBasedVideoAdNetworkAdapter(im)initWithRewardBasedVideoAdNetworkConnector:)


  ` Returns an initialized instance of the adapter when mediation ad requests come in. The adapter
  must only maintain a weak reference to the provided connector.

  #### Declaration

  Objective-C

      - (instancetype)initWithRewardBasedVideoAdNetworkConnector:
          (id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector.html>)connector;

- `


  ### [-setUp](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter#/c:objc(pl)GADMRewardBasedVideoAdNetworkAdapter(im)setUp)


  ` Tells the adapter to set up reward based video ads. The adapter should notify the Google Mobile
  Ads SDK whether set up has succeeded or failed using callbacks provided in the connector. When
  set up fails, the Google Mobile Ads SDK may try to set up the adapter again.

  #### Declaration

  Objective-C

      - (void)setUp;

- `


  ### [-requestRewardBasedVideoAd](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter#/c:objc(pl)GADMRewardBasedVideoAdNetworkAdapter(im)requestRewardBasedVideoAd)


  ` Tells the adapter to request a reward based video ad. This method is called after the adapter
  has been set up. The adapter should notify the Google Mobile Ads SDK if the request succeeds or
  fails using callbacks provided in the connector.

  #### Declaration

  Objective-C

      - (void)requestRewardBasedVideoAd;

- `


  ### [-presentRewardBasedVideoAdWithRootViewController:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter#/c:objc(pl)GADMRewardBasedVideoAdNetworkAdapter(im)presentRewardBasedVideoAdWithRootViewController:)


  ` Tells the adapter to present the reward based video ad with the provided view controller. This
  method is only called after the adapter successfully requested an ad.

  #### Declaration

  Objective-C

      - (void)presentRewardBasedVideoAdWithRootViewController:
          (UIViewController *)viewController;

- `


  ### [-stopBeingDelegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter#/c:objc(pl)GADMRewardBasedVideoAdNetworkAdapter(im)stopBeingDelegate)


  ` Tells the adapter to remove itself as a delegate or notification observer from the underlying ad
  network SDK.

  #### Declaration

  Objective-C

      - (void)stopBeingDelegate;

- `


  ### [-initWithRewardBasedVideoAdNetworkConnector:credentials:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter#/c:objc(pl)GADMRewardBasedVideoAdNetworkAdapter(im)initWithRewardBasedVideoAdNetworkConnector:credentials:)


  ` Adapters that want to be initialized as early as possible should implement this method to
  opt-into initialization when the publisher initializes the Google Mobile Ads SDK. If not
  implemented, initWithRewardBasedVideoAdNetworkConnector: gets called the first time the
  publisher loads a rewarded video ad.

  #### Declaration

  Objective-C

      - (instancetype)initWithRewardBasedVideoAdNetworkConnector:
                          (id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector.html>)connector
                                                     credentials:
                                                         (NSArray<NSDictionary *> *)
                                                             credentials;

- `


  ### [-initWithGADMAdNetworkConnector:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter#/c:objc(pl)GADMRewardBasedVideoAdNetworkAdapter(im)initWithGADMAdNetworkConnector:)


  ` Returns an initialized instance of the adapter. The adapter must only maintain a weak reference
  to the provided connector.

  #### Declaration

  Objective-C

      - (instancetype)initWithGADMAdNetworkConnector:
          (id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector.html>)connector;

- `


  ### [-setUpWithUserID:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter#/c:objc(pl)GADMRewardBasedVideoAdNetworkAdapter(im)setUpWithUserID:)


  ` Tells the adapter to set up reward based video ads with the provided user ID. The adapter should
  notify the Google Mobile Ads SDK whether set up has succeeded or failed using callbacks provided
  in the connector. When set up fails, the Google Mobile Ads SDK may try to set up the adapter
  again.

  #### Declaration

  Objective-C

      - (void)setUpWithUserID:(NSString *)userID;