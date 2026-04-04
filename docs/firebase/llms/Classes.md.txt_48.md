# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.md.txt

# GoogleMobileAds Framework Reference

# Classes

The following classes are available globally.
- `


  ### [DFPBannerView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView)


  ` The view that displays Ad Manager banner ads.

  To request this ad type using GADAdLoader, you need to pass kGADAdLoaderAdTypeDFPBanner (see
  GADAdLoaderAdTypes.h) to the \|adTypes\| parameter in GADAdLoader's initializer method. If you
  request this ad type, your delegate must conform to the DFPBannerAdLoaderDelegate protocol.

  #### Declaration

  Objective-C

      @interface DFPBannerView : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADBannerView

- `


  ### [DFPBannerViewOptions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerViewOptions)


  ` Ad loader options for banner ads.

  #### Declaration

  Objective-C

      @interface DFPBannerViewOptions : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/c:objc(cs)GADAdLoaderOptions

- `


  ### [DFPCustomRenderedAd](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPCustomRenderedAd)


  ` Custom rendered ad. Your application renders the ad.

  #### Declaration

  Objective-C

      @interface DFPCustomRenderedAd : NSObject

- `


  ### [DFPInterstitial](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPInterstitial)


  ` Google Ad Manager interstitial ad, a full-screen advertisement shown at natural
  transition points in your application such as between game levels or news stories.

  #### Declaration

  Objective-C

      @interface DFPInterstitial : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial

- `


  ### [DFPRequest](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPRequest)


  ` Specifies optional parameters for ad requests.

  #### Declaration

  Objective-C

      @interface DFPRequest : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequest

- `


  ### [GADAdChoicesView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/c:objc(cs)GADAdChoicesView)


  ` Displays AdChoices content.

  If a GADAdChoicesView is set on GADNativeAppInstallAdView or GADNativeContentAdView prior to
  calling -setNativeAppInstallAd: or -setNativeContentAd:, AdChoices content will render inside
  the GADAdChoicesView. By default, AdChoices is placed in the top right corner of
  GADNativeAppInstallAdView and GADNativeContentAdView.

  #### Declaration

  Objective-C

      @interface GADAdChoicesView : UIView

- `


  ### [GADAdLoaderOptions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/c:objc(cs)GADAdLoaderOptions)


  ` Ad loader options base class. See each ad type's header for available GADAdLoaderOptions
  subclasses.

  #### Declaration

  Objective-C

      @interface GADAdLoaderOptions : NSObject

- `


  ### [GADAdLoader](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader)


  ` Loads ads. See GADAdLoaderAdTypes.h for available ad types.

  #### Declaration

  Objective-C

      @interface GADAdLoader : NSObject

- `


  ### [GADAdReward](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdReward)


  ` Reward information for GADRewardBasedVideoAd ads.

  #### Declaration

  Objective-C

      @interface GADAdReward : NSObject

- `


  ### [GADAudioVideoManager](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAudioVideoManager)


  ` Provides audio and video notifications and configurations management.

  Don't create an instance of this class and use the one available from GADMobileAds
  sharedInstace's audioVideoManager.

  #### Declaration

  Objective-C

      @interface GADAudioVideoManager : NSObject

- `


  ### [GADBannerView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADBannerView)


  ` The view that displays banner ads. A minimum implementation to get an ad from within a
  UIViewController class is:

  <br />

  ```
    // Create and setup the ad view, specifying the size and origin at {0, 0}.
    GADBannerView *adView = [[GADBannerView alloc] initWithAdSize:kGADAdSizeBanner];
    adView.rootViewController = self;
    adView.adUnitID = @ID created when registering your app;
    // Place the ad view onto the screen.
    [self.view addSubview:adView];
    // Request an ad without any additional targeting information.
    [adView loadRequest:[GADRequest request]];
    
  ```

  <br />

  #### Declaration

  Objective-C

      @interface GADBannerView : UIView

- `


  ### [GADCorrelator](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCorrelator)


  ` Represents a correlation between multiple ads. Set an instance of this object on multiple ads to
  indicate they are being used in a common context.

  #### Declaration

  Objective-C

      @interface GADCorrelator : NSObject

- `


  ### [GADCorrelatorAdLoaderOptions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCorrelatorAdLoaderOptions)


  ` Ad loader options for adding a correlator to a native ad request.

  #### Declaration

  Objective-C

      @interface GADCorrelatorAdLoaderOptions : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/c:objc(cs)GADAdLoaderOptions

- `


  ### [GADCustomEventExtras](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCustomEventExtras)


  ` Create an instance of this class to set additional parameters for each custom event object. The
  additional parameters for a custom event are keyed by the custom event label. These extras are
  passed to your implementation of GADCustomEventBanner or GADCustomEventInterstitial.

  #### Declaration

  Objective-C

      @interface GADCustomEventExtras : NSObject <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols#/c:objc(pl)GADAdNetworkExtras>

- `


  ### [GADCustomEventRequest](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCustomEventRequest)


  ` Specifies optional ad request targeting parameters that are provided by the publisher and are
  forwarded to custom events for purposes of populating an ad request to a 3rd party ad network.

  #### Declaration

  Objective-C

      @interface GADCustomEventRequest : NSObject

- `


  ### [GADDebugOptionsViewController](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDebugOptionsViewController)


  ` Displays debug options to the user.

  #### Declaration

  Objective-C

      @interface GADDebugOptionsViewController : UIViewController

- `


  ### [GADDynamicHeightSearchRequest](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDynamicHeightSearchRequest)


  ` Use to configure Custom Search Ad (CSA) ad requests. A dynamic height search banner can contain
  multiple ads and the height is set dynamically based on the ad contents. Please cross-reference
  the property sections and properties with the official reference document:
  <https://developers.google.com/custom-search-ads/docs/reference>

  #### Declaration

  Objective-C

      @interface GADDynamicHeightSearchRequest : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequest

- `


  ### [GADExtras](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADExtras)


  ` Ad network extras sent to Google networks.

  #### Declaration

  Objective-C

      @interface GADExtras : NSObject <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols#/c:objc(pl)GADAdNetworkExtras>

[## Default Purchase Flow](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/Default%20Purchase%20Flow)

- `


  ### [GADDefaultInAppPurchase](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDefaultInAppPurchase)


  ` The consumable in-app purchase item that has been purchased by the user. The purchase flow is
  handled by the Google Mobile Ads SDK.
  Instances of this class are created and passed to your in-app purchase delegate after the user
  has successfully paid for a product. Your code must correctly deliver the product to the user
  and then call the didCompletePurchase method to finish the transaction.

  #### Declaration

  Objective-C


      @interface GADDefaultInAppPurchase : NSObject

[## Custom Purchase Flow](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/Custom%20Purchase%20Flow)

- `


  ### [GADInAppPurchase](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInAppPurchase)


  ` The in-app purchase item to be purchased with the purchase flow handled by you, the
  application developer.
  Instances of this class are created and passed to your GADInAppPurchaseDelegate object when
  users click a buy button. It is important to report the result of the purchase back to the SDK
  in order to track metrics about the transaction.

  #### Declaration

  Objective-C


      @interface GADInAppPurchase : NSObject

- `


  ### [GADAdapterStatus](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdapterStatus)


  ` An immutable snapshot of a mediation adapter's initialization status.

  #### Declaration

  Objective-C

      @interface GADAdapterStatus : NSObject <NSCopying>

- `


  ### [GADInitializationStatus](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInitializationStatus)


  ` An immutable snapshot of the Google Mobile Ads SDK's initialization status, categorized by
  mediation adapter.

  #### Declaration

  Objective-C

      @interface GADInitializationStatus : NSObject <NSCopying>

- `


  ### [GADInterstitial](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial)


  ` An interstitial ad. This is a full-screen advertisement shown at natural transition points in
  your application such as between game levels or news stories.

  #### Declaration

  Objective-C

      @interface GADInterstitial : NSObject

- `


  ### [GADMediaContent](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaContent)


  ` Provides media content information. Interact with instances of this class on the main queue
  only.

  #### Declaration

  Objective-C

      @interface GADMediaContent : NSObject

- `


  ### [GADMediaView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaView)


  ` Displays native ad media content.

  To display media content in GADUnifiedNativeAdView instances, add a GADMediaView subview,
  assign the native ad view's mediaView property, and set the native ad's mediaContent property to
  the media view.

  If the native ad contains video content, the media view displays the video content.

  If the native ad doesn't have video content and image loading is enabled, the media view
  displays the first image from the native ad's \|images\| property.

  If the native ad doesn't have video content and image loading is disabled, the media view is
  empty.

  #### Declaration

  Objective-C

      @interface GADMediaView : UIView

- `


  ### [GADMobileAds](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMobileAds)


  ` Google Mobile Ads SDK settings.

  #### Declaration

  Objective-C

      @interface GADMobileAds : NSObject

- `


  ### [GADMultipleAdsAdLoaderOptions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMultipleAdsAdLoaderOptions)


  ` Ad loader options for requesting multiple ads. Requesting multiple ads in a single request is
  currently only available for native app install ads and native content ads.

  #### Declaration

  Objective-C

      @interface GADMultipleAdsAdLoaderOptions : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/c:objc(cs)GADAdLoaderOptions

- `


  ### [GADMuteThisAdReason](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMuteThisAdReason)


  ` Reason for muting the ad.

  #### Declaration

  Objective-C

      @interface GADMuteThisAdReason : NSObject

- `


  ### [GADNativeAd](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd)


  ` Native ad base class. All native ad types are subclasses of this class.

  #### Declaration

  Objective-C

      @interface GADNativeAd : NSObject

- `


  ### [GADNativeAdImage](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage)


  ` Native ad image.

  #### Declaration

  Objective-C

      @interface GADNativeAdImage : NSObject

- `


  ### [GADNativeAdImageAdLoaderOptions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImageAdLoaderOptions)


  ` Ad loader options for native ad image settings.

  #### Declaration

  Objective-C

      @interface GADNativeAdImageAdLoaderOptions : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/c:objc(cs)GADAdLoaderOptions

- `


  ### [GADNativeAdViewAdOptions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdViewAdOptions)


  ` Ad loader options for configuring the view of native ads.

  #### Declaration

  Objective-C

      @interface GADNativeAdViewAdOptions : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/c:objc(cs)GADAdLoaderOptions

- `


  ### [GADNativeAppInstallAd](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd)


  ` Native app install ad. To request this ad type, you need to pass
  kGADAdLoaderAdTypeNativeAppInstall (see GADAdLoaderAdTypes.h) to the \|adTypes\| parameter in
  GADAdLoader's initializer method. If you request this ad type, your delegate must conform to
  the GADNativeAppInstallAdLoaderDelegate protocol.

  #### Declaration

  Objective-C


      @interface GADNativeAppInstallAd : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd

[## Native App Install Ad View](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/Native%20App%20Install%20Ad%20View)

- `


  ### [GADNativeAppInstallAdView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView)


  ` Base class for app install ad views. Your app install ad view must be a subclass of this class
  and must call superclass methods for all overriden methods.

  #### Declaration

  Objective-C


      @interface GADNativeAppInstallAdView : UIView

[## Native Content Ad Assets](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/Native%20Content%20Ad%20Assets)

- `


  ### [GADNativeContentAd](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd)


  ` Native content ad. To request this ad type, you need to pass kGADAdLoaderAdTypeNativeContent
  (see GADAdLoaderAdTypes.h) to the \|adTypes\| parameter in GADAdLoader's initializer method. If
  you request this ad type, your delegate must conform to the GADNativeContentAdLoaderDelegate
  protocol.

  #### Declaration

  Objective-C


      @interface GADNativeContentAd : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd

[## Native Content Ad View](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/Native%20Content%20Ad%20View)

- `


  ### [GADNativeContentAdView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAdView)


  ` Base class for content ad views. Your content ad view must be a subclass of this class and must
  call superclass methods for all overriden methods.

  #### Declaration

  Objective-C


      @interface GADNativeContentAdView : UIView

- `


  ### [GADNativeCustomTemplateAd](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd)


  ` Native custom template ad. To request this ad type, you need to pass
  kGADAdLoaderAdTypeNativeCustomTemplate (see GADAdLoaderAdTypes.h) to the \|adTypes\| parameter
  in GADAdLoader's initializer method. If you request this ad type, your delegate must conform to
  the GADNativeCustomTemplateAdLoaderDelegate protocol.

  #### Declaration

  Objective-C

      @interface GADNativeCustomTemplateAd : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd

- `


  ### [GADNativeExpressAdView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeExpressAdView)


  ` The view that displays native ads. A minimum implementation to get an ad from within a
  UIViewController class is:

  <br />

  ```
    // Create and setup the ad view, specifying the size and origin at {0, 0}.
    GADNativeExpressAdView *adView =
        [[GADNativeExpressAdView alloc] initWithAdSize:kGADAdSizeBanner];
    adView.rootViewController = self;
    adView.adUnitID = @ID created when registering your app;
    // Place the ad view onto the screen.
    [self.view addSubview:adView];
    // Request an ad without any additional targeting information.
    [adView loadRequest:[GADRequest request]];
    
  ```

  <br />

  #### Declaration

  Objective-C


      @interface GADNativeExpressAdView : UIView

- `


  ### [GADNativeMuteThisAdLoaderOptions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeMuteThisAdLoaderOptions)


  ` Mute This Ad options.

  #### Declaration

  Objective-C

      @interface GADNativeMuteThisAdLoaderOptions : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/c:objc(cs)GADAdLoaderOptions

- `


  ### [GADRequest](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequest)


  ` Specifies optional parameters for ad requests.

  #### Declaration

  Objective-C

      @interface GADRequest : NSObject <NSCopying>

- `


  ### [GADRequestConfiguration](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequestConfiguration)


  ` Request configuration. The settings in this class will apply to all ad requests.

  #### Declaration

  Objective-C

      @interface GADRequestConfiguration : NSObject

- `


  ### [GADRequestError](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/c:objc(cs)GADRequestError)


  ` Represents the error generated due to invalid request parameters.

  #### Declaration

  Objective-C

      @interface GADRequestError : NSError

- `


  ### [GADRewardBasedVideoAd](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd)


  ` The GADRewardBasedVideoAd class is used for requesting and presenting a reward based video ad.
  This class isn't thread safe.

  #### Declaration

  Objective-C

      @interface GADRewardBasedVideoAd : NSObject

- `


  ### [GADRewardedAd](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd)


  ` The GADRewardedAd class is used for requesting and presenting a rewarded ad.

  #### Declaration

  Objective-C

      @interface GADRewardedAd : NSObject

- `


  ### [GADSearchBannerView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchBannerView)


  ` A view that displays search ads.
  To show search ads:
  1) Create a GADSearchBannerView and add it to your view controller's view hierarchy.
  2) Create a GADSearchRequest ad request object to hold the search query and other search data.
  3) Call GADSearchBannerView's -loadRequest: method with the GADSearchRequest object.

  #### Declaration

  Objective-C

      @interface GADSearchBannerView : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADBannerView

- `


  ### [GADSearchRequest](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest)


  ` Specifies parameters for search ads.

  #### Declaration

  Objective-C

      @interface GADSearchRequest : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequest

- `


  ### [GADServerSideVerificationOptions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADServerSideVerificationOptions)


  ` Options for server-to-server verification callbacks for a rewarded ad.

  #### Declaration

  Objective-C

      @interface GADServerSideVerificationOptions : NSObject <NSCopying>

- `


  ### [GADUnifiedNativeAd](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd)


  ` Unified native ad. To request this ad type, pass kGADAdLoaderAdTypeUnifiedNative
  (see GADAdLoaderAdTypes.h) to the \|adTypes\| parameter in GADAdLoader's initializer method. If
  you request this ad type, your delegate must conform to the GADUnifiedNativeAdLoaderDelegate
  protocol.

  #### Declaration

  Objective-C

      @interface GADUnifiedNativeAd : NSObject

[## Unified Native Ad View](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/Unified%20Native%20Ad%20View)

- `


  ### [GADUnifiedNativeAdView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView)


  ` Base class for native ad views. Your native ad view must be a subclass of this class and must
  call superclass methods for all overridden methods.

  #### Declaration

  Objective-C

      @interface GADUnifiedNativeAdView : UIView

- `


  ### [GADVideoController](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController)


  ` The video controller class provides a way to get the video metadata and also manages video
  content of the ad rendered by the Google Mobile Ads SDK. You don't need to create an instance of
  this class. When the ad rendered by the Google Mobile Ads SDK loads video content, you may be
  able to get an instance of this class from the rendered ad object.

  #### Declaration

  Objective-C

      @interface GADVideoController : NSObject

- `


  ### [GADVideoOptions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoOptions)


  ` Video ad options.

  #### Declaration

  Objective-C

      @interface GADVideoOptions : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/c:objc(cs)GADAdLoaderOptions

- `


  ### [GADMediatedNativeAdNotificationSource](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedNativeAdNotificationSource)


  ` Notifies the Google Mobile Ads SDK about the events performed by adapters. Adapters may perform
  some action (e.g. opening an in app browser or opening the iTunes store) when handling callbacks
  from GADMediatedNativeAdDelegate. Adapters in such case should notify the Google Mobile Ads SDK
  by calling the relevant methods from this class.

  #### Declaration

  Objective-C

      @interface GADMediatedNativeAdNotificationSource : NSObject

- `


  ### [GADMediatedUnifiedNativeAdNotificationSource](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource)


  ` Notifies the Google Mobile Ads SDK about the events performed by adapters. Adapters may perform
  some action (e.g. opening an in app browser or opening the iTunes store) when handling methods
  in GADMediatedUnifiedNativeAd. Adapters in such case should notify the Google Mobile Ads SDK by
  calling the relevant methods from this class.

  #### Declaration

  Objective-C

      @interface GADMediatedUnifiedNativeAdNotificationSource : NSObject

- `


  ### [GADMediationAdConfiguration](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration)


  ` Provided by the Google Mobile Ads SDK for the adapter to render the ad. Contains 3PAS and other
  ad configuration information.

  #### Declaration

  Objective-C

      @interface GADMediationAdConfiguration : NSObject

- `


  ### [GADMediationBannerAdConfiguration](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationBannerAdConfiguration)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface GADMediationBannerAdConfiguration : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration

- `


  ### [GADMediationInterstitialAdConfiguration](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/c:objc(cs)GADMediationInterstitialAdConfiguration)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface GADMediationInterstitialAdConfiguration : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration

- `


  ### [GADMediationNativeAdConfiguration](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationNativeAdConfiguration)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface GADMediationNativeAdConfiguration : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration

- `


  ### [GADMediationRewardedAdConfiguration](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes#/c:objc(cs)GADMediationRewardedAdConfiguration)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface GADMediationRewardedAdConfiguration : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationAdConfiguration

- `


  ### [GADMediationCredentials](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationCredentials)


  ` Mediation configuration set by the publisher on the AdMob UI.

  #### Declaration

  Objective-C

      @interface GADMediationCredentials : NSObject

- `


  ### [GADMediationServerConfiguration](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediationServerConfiguration)


  ` Third party SDK configuration.

  #### Declaration

  Objective-C

      @interface GADMediationServerConfiguration : NSObject

- `


  ### [GADRTBRequestParameters](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRTBRequestParameters)


  ` Request parameters provided by the publisher and Google Mobile Ads SDK.

  #### Declaration

  Objective-C

      @interface GADRTBRequestParameters : NSObject