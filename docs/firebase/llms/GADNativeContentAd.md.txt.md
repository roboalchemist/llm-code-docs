# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd.md.txt

# GoogleMobileAds Framework Reference

# GADNativeContentAd


    @interface GADNativeContentAd : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd.html

Native content ad. To request this ad type, you need to pass kGADAdLoaderAdTypeNativeContent
(see GADAdLoaderAdTypes.h) to the \|adTypes\| parameter in GADAdLoader's initializer method. If
you request this ad type, your delegate must conform to the GADNativeContentAdLoaderDelegate
protocol.
[## Must be displayed](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd#/Must%20be%20displayed)

- `


  ### [headline](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)headline)


  ` Primary text headline.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *headline;

- `


  ### [body](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)body)


  ` Secondary text.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *body;

[## Recommended to display](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd#/Recommended%20to%20display)

- `


  ### [images](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)images)


  ` Large images.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable)
          NSArray<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.html *> *images;

- `


  ### [logo](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)logo)


  ` Small logo image.

  #### Declaration

  Objective-C

      @property (readonly, strong, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.html *logo;

- `


  ### [callToAction](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)callToAction)


  ` Text that encourages user to take some action with the ad.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *callToAction;

- `


  ### [advertiser](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)advertiser)


  ` Identifies the advertiser. For example, the advertiser's name or visible URL.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *advertiser;

- `


  ### [videoController](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(py)videoController)


  ` Video controller for controlling video playback in GADNativeContentAdView's mediaView.

  #### Declaration

  Objective-C

      @property (readonly, strong, nonatomic)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController.html *_Nonnull videoController;

- `


  ### [-registerAdView:assetViews:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(im)registerAdView:assetViews:)


  ` Registers ad view and asset views created with this native ad.

  #### Declaration

  Objective-C

      - (void)registerAdView:(nonnull UIView *)adView
                  assetViews:
                      (nonnull NSDictionary<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID, UIView *> *)
                          assetViews;

  #### Parameters

  |---|---|
  | ` assetViews ` | Dictionary of asset views keyed by asset IDs. |

- `


  ### [-registerAdView:clickableAssetViews:nonclickableAssetViews:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(im)registerAdView:clickableAssetViews:nonclickableAssetViews:)


  ` Registers ad view, clickable asset views, and nonclickable asset views with this native ad.
  Media view shouldn't be registered as clickable.

  #### Declaration

  Objective-C

      - (void)registerAdView:(nonnull UIView *)adView
             clickableAssetViews:
                 (nonnull NSDictionary<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID, UIView *> *)
                     clickableAssetViews
          nonclickableAssetViews:
              (nonnull NSDictionary<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADNativeContentAdAssetIDs.h@T@GADNativeContentAdAssetID, UIView *> *)
                  nonclickableAssetViews;

  #### Parameters

  |---|---|
  | ` clickableAssetViews ` | Dictionary of asset views that are clickable, keyed by asset IDs. |
  | ` nonclickableAssetViews ` | Dictionary of asset views that are not clickable, keyed by asset IDs. |

- `


  ### [-unregisterAdView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd#/c:objc(cs)GADNativeContentAd(im)unregisterAdView)


  ` Unregisters ad view from this native ad. The corresponding asset views will also be
  unregistered.

  #### Declaration

  Objective-C

      - (void)unregisterAdView;