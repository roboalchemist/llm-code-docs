# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.md.txt

# GoogleMobileAds Framework Reference

# GADUnifiedNativeAd

    @interface GADUnifiedNativeAd : NSObject

Unified native ad. To request this ad type, pass kGADAdLoaderAdTypeUnifiedNative
(see GADAdLoaderAdTypes.h) to the \|adTypes\| parameter in GADAdLoader's initializer method. If
you request this ad type, your delegate must conform to the GADUnifiedNativeAdLoaderDelegate
protocol.
[## Must be displayed if available](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/Must%20be%20displayed%20if%20available)

- `


  ### [headline](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)headline)


  ` Headline

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *headline;

[## Recommended to display](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/Recommended%20to%20display)

- `


  ### [callToAction](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)callToAction)


  ` Text that encourages user to take some action with the ad. For example Install.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *callToAction;

- `


  ### [icon](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)icon)


  ` Icon image.

  #### Declaration

  Objective-C

      @property (readonly, strong, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.html *icon;

- `


  ### [body](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)body)


  ` Description.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *body;

- `


  ### [images](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)images)


  ` Array of GADNativeAdImage objects.

  #### Declaration

  Objective-C

      @property (readonly, strong, nonatomic, nullable)
          NSArray<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.html *> *images;

- `


  ### [starRating](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)starRating)


  ` App store rating (0 to 5).

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSDecimalNumber *starRating;

- `


  ### [store](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)store)


  ` The app store name. For example, App Store.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *store;

- `


  ### [price](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)price)


  ` String representation of the app's price.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *price;

- `


  ### [advertiser](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)advertiser)


  ` Identifies the advertiser. For example, the advertiser's name or visible URL.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *advertiser;

- `


  ### [videoController](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)videoController)


  ` Video controller for controlling video playback in GADUnifiedNativeAdView's mediaView.

  #### Declaration

  Objective-C

      @property (readonly, strong, nonatomic, nullable)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController.html *videoController;

- `


  ### [delegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)delegate)


  ` Optional delegate to receive state change notifications.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate.html>
          delegate;

- `


  ### [rootViewController](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)rootViewController)


  ` Reference to a root view controller that is used by the ad to present full screen content after
  the user interacts with the ad. The root view controller is most commonly the view controller
  displaying the ad.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) UIViewController *rootViewController;

- `


  ### [extraAssets](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)extraAssets)


  ` Dictionary of assets which aren't processed by the receiver.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable)
          NSDictionary<NSString *, id> *extraAssets;

- `


  ### [adNetworkClassName](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)adNetworkClassName)


  ` The ad network class name that fetched the current ad. For both standard and mediated Google
  AdMob ads, this method returns @GADMAdapterGoogleAdMobAds. For ads fetched via mediation
  custom events, this method returns @GADMAdapterCustomEvents.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *adNetworkClassName;

- `


  ### [customMuteThisAdAvailable](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)customMuteThisAdAvailable)


  ` Indicates whether custom Mute This Ad is available for the native ad.

  #### Declaration

  Objective-C

      @property (readonly, getter=isCustomMuteThisAdAvailable, nonatomic)
          BOOL customMuteThisAdAvailable;

- `


  ### [muteThisAdReasons](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)muteThisAdReasons)


  ` An array of Mute This Ad reasons used to render customized mute ad survey. Use this array to
  implement your own Mute This Ad feature only when customMuteThisAdAvailable is YES.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nullable)
          NSArray<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMuteThisAdReason.html *> *muteThisAdReasons;

- `


  ### [mediaContent](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)mediaContent)


  ` Media content. Set the associated media view's mediaContent property to this object to display
  this content.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nonnull) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaContent.html *mediaContent;

- `


  ### [-registerAdView:clickableAssetViews:nonclickableAssetViews:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)registerAdView:clickableAssetViews:nonclickableAssetViews:)


  ` Registers ad view, clickable asset views, and nonclickable asset views with this native ad.
  Media view shouldn't be registered as clickable.

  #### Declaration

  Objective-C

      - (void)registerAdView:(nonnull UIView *)adView
             clickableAssetViews:
                 (nonnull NSDictionary<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier, UIView *> *)
                     clickableAssetViews
          nonclickableAssetViews:
              (nonnull NSDictionary<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier, UIView *> *)
                  nonclickableAssetViews;

  #### Parameters

  |---|---|
  | ` clickableAssetViews ` | Dictionary of asset views that are clickable, keyed by asset IDs. |
  | ` nonclickableAssetViews ` | Dictionary of asset views that are not clickable, keyed by asset IDs. |

- `


  ### [-unregisterAdView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)unregisterAdView)


  ` Unregisters ad view from this native ad. The corresponding asset views will also be
  unregistered.

  #### Declaration

  Objective-C

      - (void)unregisterAdView;

- `


  ### [-muteThisAdWithReason:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)muteThisAdWithReason:)


  ` Reports the mute event with the mute reason selected by user. Use nil if no reason was selected.
  Call this method only if customMuteThisAdAvailable is YES.

  #### Declaration

  Objective-C

      - (void)muteThisAdWithReason:(nullable https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMuteThisAdReason.html *)reason;

[## ConfirmedClick](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/ConfirmedClick)

- `


  ### [unconfirmedClickDelegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)unconfirmedClickDelegate)


  ` Unconfirmed click delegate.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable)
          id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdUnconfirmedClickDelegate.html>
              unconfirmedClickDelegate;

- `


  ### [-registerClickConfirmingView:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)registerClickConfirmingView:)


  ` Registers a view that will confirm the click.

  #### Declaration

  Objective-C

      - (void)registerClickConfirmingView:(nullable UIView *)view;

- `


  ### [-cancelUnconfirmedClick](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)cancelUnconfirmedClick)


  ` Cancels the unconfirmed click. Call this method when the user fails to confirm the click.
  Calling this method causes the SDK to stop tracking clicks on the registered click confirming
  view and invokes the -nativeAdDidCancelUnconfirmedClick: delegate method. If no unconfirmed
  click is in progress, this method has no effect.

  #### Declaration

  Objective-C

      - (void)cancelUnconfirmedClick;

[## CustomClickGesture](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/CustomClickGesture)

- `


  ### [customClickGestureEnabled](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(py)customClickGestureEnabled)


  ` Indicates whether the custom click gestures feature can be used.

  #### Declaration

  Objective-C

      @property (readonly, getter=isCustomClickGestureEnabled, nonatomic)
          BOOL customClickGestureEnabled;

- `


  ### [-enableCustomClickGestures](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)enableCustomClickGestures)


  ` Enables custom click gestures. Must be called before the ad is associated with an ad view.
  Available for whitelisted accounts only.

  #### Declaration

  Objective-C

      - (void)enableCustomClickGestures;

- `


  ### [-recordCustomClickGesture](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd#/c:objc(cs)GADUnifiedNativeAd(im)recordCustomClickGesture)


  ` Records a click triggered by a custom click gesture.

  #### Declaration

  Objective-C

      - (void)recordCustomClickGesture;