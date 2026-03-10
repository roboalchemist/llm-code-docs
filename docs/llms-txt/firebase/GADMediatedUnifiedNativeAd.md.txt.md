# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.md.txt

# GoogleMobileAds Framework Reference

# GADMediatedUnifiedNativeAd

    @protocol GADMediatedUnifiedNativeAd <NSObject>

Provides methods used for constructing native ads. The adapter must return an object conforming
to this protocol for native ad requests.
- `


  ### [headline](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)headline)


  ` Headline.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *headline;

- `


  ### [images](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)images)


  ` Array of GADNativeAdImage objects.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nullable) NSArray<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.html *> *images;

- `


  ### [body](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)body)


  ` Description.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *body;

- `


  ### [icon](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)icon)


  ` Icon image.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.html *icon;

- `


  ### [callToAction](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)callToAction)


  ` Text that encourages user to take some action with the ad. For example Install.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *callToAction;

- `


  ### [starRating](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)starRating)


  ` App store rating (0 to 5).

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSDecimalNumber *starRating;

- `


  ### [store](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)store)


  ` The app store name. For example, App Store.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *store;

- `


  ### [price](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)price)


  ` String representation of the app's price.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *price;

- `


  ### [advertiser](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)advertiser)


  ` Identifies the advertiser. For example, the advertiser's name or visible URL.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *advertiser;

- `


  ### [extraAssets](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)extraAssets)


  ` Returns a dictionary of asset names and object pairs for assets that are not handled by
  properties of the GADMediatedUnifiedNativeAd.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable)
          NSDictionary<NSString *, id> *extraAssets;

- `


  ### [adChoicesView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)adChoicesView)


  ` AdChoices view.

  #### Declaration

  Objective-C

      @optional
      @property (readonly, nonatomic, nullable) UIView *adChoicesView;

- `


  ### [mediaView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)mediaView)


  ` Media view.

  #### Declaration

  Objective-C

      @optional
      @property (readonly, nonatomic, nullable) UIView *mediaView;

- `


  ### [hasVideoContent](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)hasVideoContent)


  ` Indicates whether the ad has video content.

  #### Declaration

  Objective-C

      @optional
      @property (readonly, nonatomic) BOOL hasVideoContent;

- `


  ### [mediaContentAspectRatio](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(py)mediaContentAspectRatio)


  ` Media content aspect ratio (width/height) or 0 if there's no media content.

  #### Declaration

  Objective-C

      @optional
      @property (readonly, nonatomic) CGFloat mediaContentAspectRatio;

- `


  ### [-didRenderInView:clickableAssetViews:nonclickableAssetViews:viewController:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(im)didRenderInView:clickableAssetViews:nonclickableAssetViews:viewController:)


  ` Tells the receiver that it has been rendered in \|view\| with clickable asset views and
  nonclickable asset views. viewController should be used to present modal views for the ad.

  #### Declaration

  Objective-C

      - (void)didRenderInView:(nonnull UIView *)view
             clickableAssetViews:
                 (nonnull NSDictionary<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier, UIView *> *)
                     clickableAssetViews
          nonclickableAssetViews:
              (nonnull NSDictionary<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier, UIView *> *)
                  nonclickableAssetViews
                  viewController:(nonnull UIViewController *)viewController;

- `


  ### [-didRecordImpression](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(im)didRecordImpression)


  ` Tells the receiver that an impression is recorded. This method is called only once per mediated
  native ad.

  #### Declaration

  Objective-C

      - (void)didRecordImpression;

- `


  ### [-didRecordClickOnAssetWithName:view:viewController:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(im)didRecordClickOnAssetWithName:view:viewController:)


  ` Tells the receiver that a user click is recorded on the asset named \|assetName\|. Full screen
  actions should be presented from viewController. This method is called only if
  -\[GADMAdNetworkAdapter handlesUserClicks\] returns NO.

  #### Declaration

  Objective-C

      - (void)didRecordClickOnAssetWithName:
                  (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier)assetName
                                       view:(nonnull UIView *)view
                             viewController:
                                 (nonnull UIViewController *)viewController;

- `


  ### [-didUntrackView:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd#/c:objc(pl)GADMediatedUnifiedNativeAd(im)didUntrackView:)


  ` Tells the receiver that it has untracked \|view\|. This method is called when the mediated native
  ad is no longer rendered in the provided view and the delegate should stop tracking the view's
  impressions and clicks. The method may also be called with a nil view when the view in which the
  mediated native ad has rendered is deallocated.

  #### Declaration

  Objective-C

      - (void)didUntrackView:(nullable UIView *)view;