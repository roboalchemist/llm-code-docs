# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols.md.txt

# GoogleMobileAds Framework Reference

# Protocols

The following protocols are available globally.
- `


  ### [DFPBannerAdLoaderDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/DFPBannerAdLoaderDelegate)


  ` The delegate of a GADAdLoader object must conform to this protocol to receive DFPBannerViews.

  #### Declaration

  Swift

      protocol DFPBannerAdLoaderDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate

- `


  ### [DFPCustomRenderedBannerViewDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/DFPCustomRenderedBannerViewDelegate)


  ` The DFPCustomRenderedAd banner view delegate protocol for notifying the delegate of changes to
  custom rendered banners.

  #### Declaration

  Swift

      protocol DFPCustomRenderedBannerViewDelegate : NSObjectProtocol

- `


  ### [DFPCustomRenderedInterstitialDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/DFPCustomRenderedInterstitialDelegate)


  ` The DFPCustomRenderedAd interstitial delegate protocol for notifying the delegate of changes to
  custom rendered interstitials.

  #### Declaration

  Swift

      protocol DFPCustomRenderedInterstitialDelegate : NSObjectProtocol

- `


  ### [GADAdLoaderDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate)


  ` Base ad loader delegate protocol. Ad types provide extended protocols that declare methods to
  handle successful ad loads.

  #### Declaration

  Swift

      protocol GADAdLoaderDelegate : NSObjectProtocol

- `


  ### [GADAdNetworkExtras](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols#/c:objc(pl)GADAdNetworkExtras)


  ` An object implementing this protocol contains information set by the publisher on the client
  device for a particular ad network.

  Ad networks should create an 'extras' object implementing this protocol for their publishers to
  use.

  #### Declaration

  Swift

      protocol GADAdNetworkExtras : NSObjectProtocol

- `


  ### [GADAdSizeDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdSizeDelegate)


  ` The class implementing this protocol will be notified when the GADBannerView's ad content
  changes size. Any views that may be affected by the banner size change will have time to adjust.

  #### Declaration

  Swift

      protocol GADAdSizeDelegate : NSObjectProtocol

- `


  ### [GADAppEventDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAppEventDelegate)


  ` Implement your app event within these methods. The delegate will be notified when the SDK
  receives an app event message from the ad.

  #### Declaration

  Swift

      protocol GADAppEventDelegate : NSObjectProtocol

- `


  ### [GADAudioVideoManagerDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAudioVideoManagerDelegate)


  ` A set of methods to inform the delegate of audio video manager events.

  #### Declaration

  Swift

      protocol GADAudioVideoManagerDelegate : NSObjectProtocol

- `


  ### [GADBannerViewDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADBannerViewDelegate)


  ` Delegate methods for receiving GADBannerView state change messages such as ad request status
  and ad click lifecycle.

  #### Declaration

  Swift

      protocol GADBannerViewDelegate : NSObjectProtocol

- `


  ### [GADCustomEventBanner](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBanner)


  ` The banner custom event protocol. Your banner custom event handler must implement this protocol.

  #### Declaration

  Swift

      protocol GADCustomEventBanner : NSObjectProtocol

- `


  ### [GADCustomEventBannerDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate)


  ` Call back to this delegate in your custom event. You must call customEventBanner:didReceiveAd:
  when there is an ad to show, or customEventBanner:didFailAd: when there is no ad to show.
  Otherwise, if enough time passed (several seconds) after the SDK called the requestBannerAd:
  method of your custom event, the mediation SDK will consider the request timed out, and move on
  to the next ad network.

  #### Declaration

  Swift

      protocol GADCustomEventBannerDelegate : NSObjectProtocol

- `


  ### [GADCustomEventInterstitial](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial)


  ` The interstitial custom event protocol. Your interstitial custom event handler must implement
  this protocol.

  #### Declaration

  Swift

      protocol GADCustomEventInterstitial : NSObjectProtocol

- `


  ### [GADCustomEventInterstitialDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate)


  ` Call back to this delegate in your custom event. You must call
  customEventInterstitialDidReceiveAd: when there is an ad to show, or
  customEventInterstitial:didFailAd: when there is no ad to show. Otherwise, if enough time passed
  (several seconds) after the SDK called the requestInterstitialAdWithParameter: method of your
  custom event, the mediation SDK will consider the request timed out, and move on to the next ad
  network.

  #### Declaration

  Swift

      protocol GADCustomEventInterstitialDelegate : NSObjectProtocol

- `


  ### [GADCustomEventNativeAd](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventNativeAd)


  ` Native ad custom event protocol. Your native ad custom event handler class must conform to this
  protocol.

  #### Declaration

  Swift

      protocol GADCustomEventNativeAd : NSObjectProtocol

- `


  ### [GADCustomEventNativeAdDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventNativeAdDelegate)


  ` The delegate of the GADCustomEventNativeAd object must adopt the GADCustomEventNativeAdDelegate
  protocol. Methods in this protocol are used for native ad's custom event communication with the
  Google Mobile Ads SDK.

  #### Declaration

  Swift

      protocol GADCustomEventNativeAdDelegate : NSObjectProtocol

- `


  ### [GADDebugOptionsViewControllerDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADDebugOptionsViewControllerDelegate)


  ` Delegate for the GADDebugOptionsViewController.

  #### Declaration

  Swift

      protocol GADDebugOptionsViewControllerDelegate : NSObjectProtocol

[## Default Purchase Flow](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols#/Default%20Purchase%20Flow)

- `


  ### [GADDefaultInAppPurchaseDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADDefaultInAppPurchaseDelegate)


  ` In-app purchase delegate protocol for default purchase handling. The delegate must deliver
  the purchased item then call the GADDefaultInAppPurchase object's finishTransaction method.

  #### Declaration

  Swift

      protocol GADDefaultInAppPurchaseDelegate : NSObjectProtocol

[## Custom Purchase Flow](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols#/Custom%20Purchase%20Flow)

- `


  ### [GADInAppPurchaseDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInAppPurchaseDelegate)


  ` In-app purchase delegate protocol for custom purchase handling. The delegate must handle the
  product purchase flow then call the GADInAppPurchase object's reportPurchaseStatus: method.

  #### Declaration

  Swift

      protocol GADInAppPurchaseDelegate : NSObjectProtocol

- `


  ### [GADInterstitialDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInterstitialDelegate)


  ` Delegate for receiving state change messages from a GADInterstitial such as interstitial ad
  requests succeeding/failing.

  #### Declaration

  Swift

      protocol GADInterstitialDelegate : NSObjectProtocol

- `


  ### [GADNativeAdDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeAdDelegate)


  ` Identifies native ad assets.

  #### Declaration

  Swift

      protocol GADNativeAdDelegate : NSObjectProtocol

[## Protocol and constants](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols#/Protocol%20and%20constants)

- `


  ### [GADNativeAppInstallAdLoaderDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeAppInstallAdLoaderDelegate)


  ` The delegate of a GADAdLoader object implements this protocol to receive GADNativeAppInstallAd
  ads.

  #### Declaration

  Swift

      protocol GADNativeAppInstallAdLoaderDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate

[## Protocol and constants](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols#/Protocol%20and%20constants2)

- `


  ### [GADNativeContentAdLoaderDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeContentAdLoaderDelegate)


  ` The delegate of a GADAdLoader object implements this protocol to receive GADNativeContentAd ads.

  #### Declaration

  Swift

      protocol GADNativeContentAdLoaderDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate

[## Loading Protocol](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols#/Loading%20Protocol)

- `


  ### [GADNativeCustomTemplateAdLoaderDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeCustomTemplateAdLoaderDelegate)


  ` The delegate of a GADAdLoader object implements this protocol to receive
  GADNativeCustomTemplateAd ads.

  #### Declaration

  Swift

      protocol GADNativeCustomTemplateAdLoaderDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate

- `


  ### [GADNativeExpressAdViewDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate)


  ` Delegate methods for receiving GADNativeExpressAdView state change messages such as ad request
  status and ad click lifecycle.

  #### Declaration

  Swift

      protocol GADNativeExpressAdViewDelegate : NSObjectProtocol

- `


  ### [GADRewardBasedVideoAdDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate)


  ` Delegate for receiving state change messages from a GADRewardBasedVideoAd such as ad requests
  succeeding/failing.

  #### Declaration

  Swift

      protocol GADRewardBasedVideoAdDelegate : NSObjectProtocol

- `


  ### [GADRewardedAdDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate)


  ` Delegate for receiving state change messages from a GADRewardedAd.

  #### Declaration

  Swift

      protocol GADRewardedAdDelegate : NSObjectProtocol

- `


  ### [GADRewardedAdMetadataDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardedAdMetadataDelegate)


  ` Delegate for receiving metadata change messages from a GADRewardedAd.

  #### Declaration

  Swift

      protocol GADRewardedAdMetadataDelegate : NSObjectProtocol

[## Protocol and constants](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols#/Protocol%20and%20constants3)

- `


  ### [GADUnifiedNativeAdLoaderDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdLoaderDelegate)


  ` The delegate of a GADAdLoader object implements this protocol to receive GADUnifiedNativeAd ads.

  #### Declaration

  Swift

      protocol GADUnifiedNativeAdLoaderDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate

- `


  ### [GADUnifiedNativeAdDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate)


  ` Identifies native ad assets.

  #### Declaration

  Swift

      protocol GADUnifiedNativeAdDelegate : NSObjectProtocol

- `


  ### [GADUnifiedNativeAdUnconfirmedClickDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdUnconfirmedClickDelegate)


  ` Delegate methods for handling unified native ad unconfirmed clicks.

  #### Declaration

  Swift

      protocol GADUnifiedNativeAdUnconfirmedClickDelegate : NSObjectProtocol

- `


  ### [GADVideoControllerDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate)


  ` The GADVideoControllerDelegate protocol defines methods that are called by the video controller
  object in response to the video events that occurred throughout the lifetime of the video
  rendered by an ad.

  #### Declaration

  Swift

      protocol GADVideoControllerDelegate : NSObjectProtocol

- `


  ### [GADMAdNetworkAdapter](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter)


  ` Ad network adapter protocol.

  #### Declaration

  Swift

      protocol GADMAdNetworkAdapter : NSObjectProtocol

- `


  ### [GADMAdNetworkConnector](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector)


  ` Ad network adapters interact with the mediation SDK using an object that implements the
  GADMAdNetworkConnector protocol. The connector object can be used to obtain necessary
  information for ad requests, and to call back to the mediation SDK on ad request returns and
  user interactions.

  #### Declaration

  Swift

      protocol GADMAdNetworkConnector : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest

- `


  ### [GADMRewardBasedVideoAdNetworkAdapter](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter)


  ` Your adapter must conform to this protocol to provide reward based video ads.

  #### Declaration

  Swift

      protocol GADMRewardBasedVideoAdNetworkAdapter : NSObjectProtocol

- `


  ### [GADMRewardBasedVideoAdNetworkConnector](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector)


  ` Reward based video ad network adapters interact with the mediation SDK using an object that
  conforms to the GADMRewardBasedVideoAdNetworkConnector protocol. The connector object can be
  used to obtain information for ad requests and to call back to the mediation SDK on ad responses
  and user interactions.

  #### Declaration

  Swift

      protocol GADMRewardBasedVideoAdNetworkConnector : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest

- `


  ### [GADMediatedNativeAd](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd)


  ` Base protocol for mediated native ads.

  #### Declaration

  Swift

      protocol GADMediatedNativeAd : NSObjectProtocol

- `


  ### [GADMediatedNativeAdDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAdDelegate)


  ` GADMediatedNativeAdDelegate objects handle mediated native ad events.

  #### Declaration

  Swift

      protocol GADMediatedNativeAdDelegate : NSObjectProtocol

- `


  ### [GADMediatedNativeAppInstallAd](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd)


  ` Provides methods used for constructing native app install ads. The adapter must return an object
  conforming to this protocol for native app install ad requests.

  #### Declaration

  Swift

      protocol GADMediatedNativeAppInstallAd : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd

- `


  ### [GADMediatedNativeContentAd](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd)


  ` Provides methods used for constructing native content ads.

  #### Declaration

  Swift

      protocol GADMediatedNativeContentAd : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd

- `


  ### [GADMediatedUnifiedNativeAd](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd)


  ` Provides methods used for constructing native ads. The adapter must return an object conforming
  to this protocol for native ad requests.

  #### Declaration

  Swift

      protocol GADMediatedUnifiedNativeAd : NSObjectProtocol

- `


  ### [GADMediationAd](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols#/c:objc(pl)GADMediationAd)


  ` Rendered ad. Objects conforming to this protocol are created by the adapter and returned to
  the Google Mobile Ads SDK via the adapter's render method completion handler.

  #### Declaration

  Swift

      protocol GADMediationAd : NSObjectProtocol

- `


  ### [GADMediationAdEventDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate)


  ` Reports information to the Google Mobile Ads SDK from the adapter. Adapters receive an ad event
  delegate when they provide a GADMediationAd by calling a render completion handler.

  #### Declaration

  Swift

      protocol GADMediationAdEventDelegate : NSObjectProtocol

- `


  ### [GADMediationBannerAdEventDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationBannerAdEventDelegate)


  ` Reports banner related information to the Google Mobile Ads SDK from the adapter.

  #### Declaration

  Swift

      protocol GADMediationBannerAdEventDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate

- `


  ### [GADMediationInterstitialAdEventDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationInterstitialAdEventDelegate)


  ` Reports interstitial related information to the Google Mobile Ads SDK from the adapter.

  #### Declaration

  Swift

      protocol GADMediationInterstitialAdEventDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate

- `


  ### [GADMediationNativeAdEventDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationNativeAdEventDelegate)


  ` Reports native related information to the Google Mobile Ads SDK from the adapter.

  #### Declaration

  Swift

      protocol GADMediationNativeAdEventDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate

- `


  ### [GADMediationRewardedAdEventDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationRewardedAdEventDelegate)


  ` Reports rewarded related information to the Google Mobile Ads SDK from the adapter.

  #### Declaration

  Swift

      protocol GADMediationRewardedAdEventDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate

- `


  ### [GADMediationAdRequest](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest)


  ` Provides information which can be used for making ad requests during mediation.

  #### Declaration

  Swift

      protocol GADMediationAdRequest : NSObjectProtocol

- `


  ### [GADMediationAdapter](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter)


  ` Receives messages and requests from the Google Mobile Ads SDK. Provides GMA to 3P SDK
  communication.

  Adapters are initialized on a background queue and should avoid using the main queue until
  load time.

  #### Declaration

  Swift

      protocol GADMediationAdapter : NSObjectProtocol

- `


  ### [GADMediationBannerAd](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationBannerAd)


  ` Rendered banner ad. Provides a single subview to add to the banner view's view hierarchy.

  #### Declaration

  Swift

      protocol GADMediationBannerAd : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols#/c:objc(pl)GADMediationAd

- `


  ### [GADMediationInterstitialAd](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationInterstitialAd)


  ` Rendered interstitial ad.

  #### Declaration

  Swift

      protocol GADMediationInterstitialAd : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols#/c:objc(pl)GADMediationAd

- `


  ### [GADMediationNativeAd](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationNativeAd)


  ` Rendered native ad.

  #### Declaration

  Swift

      protocol GADMediationNativeAd : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd, https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols#/c:objc(pl)GADMediationAd

- `


  ### [GADMediationRewardedAd](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationRewardedAd)


  ` Rendered rewarded ad.

  #### Declaration

  Swift

      protocol GADMediationRewardedAd : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols#/c:objc(pl)GADMediationAd

- `


  ### [GADRTBAdapter](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRTBAdapter)


  ` Adapter that provides signals to the Google Mobile Ads SDK to be included in an OpenRTB auction.

  #### Declaration

  Swift

      protocol GADRTBAdapter : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter