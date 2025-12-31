# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd.md.txt

# GoogleMobileAds Framework Reference

# GADNativeAppInstallAd


    @interface GADNativeAppInstallAd : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd.html

Native app install ad. To request this ad type, you need to pass
kGADAdLoaderAdTypeNativeAppInstall (see GADAdLoaderAdTypes.h) to the \|adTypes\| parameter in
GADAdLoader's initializer method. If you request this ad type, your delegate must conform to
the GADNativeAppInstallAdLoaderDelegate protocol.
[## Must be displayed](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/Must%20be%20displayed)

- `
  ``
  ``
  `

  ### [headline](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)headline)

  `
  `  
  App title.  

  #### Declaration

  Objective-C  

      @property (readonly, copy, nonatomic, nullable) NSString *headline;

- `
  ``
  ``
  `

  ### [callToAction](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)callToAction)

  `
  `  
  Text that encourages user to take some action with the ad. For example Install.  

  #### Declaration

  Objective-C  

      @property (readonly, copy, nonatomic, nullable) NSString *callToAction;

- `
  ``
  ``
  `

  ### [icon](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)icon)

  `
  `  
  Application icon.  

  #### Declaration

  Objective-C  

      @property (readonly, strong, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.html *icon;

[## Recommended to display](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/Recommended%20to%20display)

- `
  ``
  ``
  `

  ### [body](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)body)

  `
  `  
  App description.  

  #### Declaration

  Objective-C  

      @property (readonly, copy, nonatomic, nullable) NSString *body;

- `
  ``
  ``
  `

  ### [store](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)store)

  `
  `  
  The app store name. For example, App Store.  

  #### Declaration

  Objective-C  

      @property (readonly, copy, nonatomic, nullable) NSString *store;

- `
  ``
  ``
  `

  ### [price](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)price)

  `
  `  
  String representation of the app's price.  

  #### Declaration

  Objective-C  

      @property (readonly, copy, nonatomic, nullable) NSString *price;

- `
  ``
  ``
  `

  ### [images](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)images)

  `
  `  
  Array of GADNativeAdImage objects related to the advertised application.  

  #### Declaration

  Objective-C  

      @property (readonly, strong, nonatomic, nullable)
          NSArray<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.html *> *images;

- `
  ``
  ``
  `

  ### [starRating](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)starRating)

  `
  `  
  App store rating (0 to 5).  

  #### Declaration

  Objective-C  

      @property (readonly, copy, nonatomic, nullable) NSDecimalNumber *starRating;

- `
  ``
  ``
  `

  ### [videoController](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(py)videoController)

  `
  `  
  Video controller for controlling video playback in GADNativeAppInstallAdView's mediaView.  

  #### Declaration

  Objective-C  

      @property (readonly, strong, nonatomic)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController.html *_Nonnull videoController;

- `
  ``
  ``
  `

  ### [-registerAdView:assetViews:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(im)registerAdView:assetViews:)

  `
  `  
  Registers ad view and asset views with this native ad.  

  #### Declaration

  Objective-C  

      - (void)registerAdView:(nonnull UIView *)adView
                  assetViews:
                      (nonnull NSDictionary<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID, UIView *> *)
                          assetViews;

  #### Parameters

  |--------------------|-----------------------------------------------|
  | ` `*assetViews*` ` | Dictionary of asset views keyed by asset IDs. |

- `
  ``
  ``
  `

  ### [-registerAdView:clickableAssetViews:nonclickableAssetViews:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(im)registerAdView:clickableAssetViews:nonclickableAssetViews:)

  `
  `  
  Registers ad view, clickable asset views, and nonclickable asset views with this native ad.
  Media view shouldn't be registered as clickable.  

  #### Declaration

  Objective-C  

      - (void)registerAdView:(nonnull UIView *)adView
             clickableAssetViews:
                 (nonnull NSDictionary<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID, UIView *> *)
                     clickableAssetViews
          nonclickableAssetViews:
              (nonnull NSDictionary<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADNativeAppInstallAdAssetIDs.h@T@GADNativeAppInstallAssetID, UIView *> *)
                  nonclickableAssetViews;

  #### Parameters

  |--------------------------------|-----------------------------------------------------------------------|
  | ` `*clickableAssetViews*` `    | Dictionary of asset views that are clickable, keyed by asset IDs.     |
  | ` `*nonclickableAssetViews*` ` | Dictionary of asset views that are not clickable, keyed by asset IDs. |

- `
  ``
  ``
  `

  ### [-unregisterAdView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd#/c:objc(cs)GADNativeAppInstallAd(im)unregisterAdView)

  `
  `  
  Unregisters ad view from this native ad. The corresponding asset views will also be
  unregistered.  

  #### Declaration

  Objective-C  

      - (void)unregisterAdView;