# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventNativeAd.md.txt

# GoogleMobileAds Framework Reference

# GADCustomEventNativeAd

    @protocol GADCustomEventNativeAd <NSObject>

Native ad custom event protocol. Your native ad custom event handler class must conform to this
protocol.
- `


  ### [-requestNativeAdWithParameter:request:adTypes:options:rootViewController:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventNativeAd#/c:objc(pl)GADCustomEventNativeAd(im)requestNativeAdWithParameter:request:adTypes:options:rootViewController:)


  ` Called when the custom event is scheduled to be executed.

  #### Declaration

  Objective-C

      - (void)requestNativeAdWithParameter:(nonnull NSString *)serverParameter
                                   request:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCustomEventRequest.html *)request
                                   adTypes:(nonnull NSArray *)adTypes
                                   options:(nonnull NSArray *)options
                        rootViewController:
                            (nonnull UIViewController *)rootViewController;

  #### Parameters

  |---|---|
  | ` serverParameter ` | A value configured in the mediation UI for the custom event. |
  | ` request ` | Ad targeting information. |
  | ` adTypes ` | List of requested native ad types. See GADAdLoaderAdTypes.h for available ad types. |
  | ` options ` | Additional options configured by the publisher for requesting a native ad. See GADNativeAdImageAdLoaderOptions.h for available image options. |
  | ` rootViewController ` | Publisher-provided view controller. |

- `


  ### [-handlesUserClicks](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventNativeAd#/c:objc(pl)GADCustomEventNativeAd(im)handlesUserClicks)


  ` Indicates whether the custom event handles user clicks. Return YES if the custom event should
  handle user clicks. In this case, the Google Mobile Ads SDK doesn't track user clicks and the
  custom event must notify the Google Mobile Ads SDK of clicks using
  +\[GADMediatedNativeAdNotificationSource mediatedNativeAdDidRecordClick:\]. Return NO if the
  custom event doesn't handles user clicks. In this case, the Google Mobile Ads SDK tracks user
  clicks itself and the custom event is notified of user clicks via -\[GADMediatedNativeAdDelegate
  mediatedNativeAd:didRecordClickOnAssetWithName:view:viewController:\].

  #### Declaration

  Objective-C

      - (BOOL)handlesUserClicks;

- `


  ### [-handlesUserImpressions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventNativeAd#/c:objc(pl)GADCustomEventNativeAd(im)handlesUserImpressions)


  ` Indicates whether the custom event handles user impressions tracking. If this method returns
  YES, the Google Mobile Ads SDK will not track user impressions and the custom event must notify
  the Google Mobile Ads SDK of impressions using +\[GADMediatedNativeAdNotificationSource
  mediatedNativeAdDidRecordImpression:\]. If this method returns NO, the Google Mobile Ads SDK
  tracks user impressions and notifies the custom event of impressions using
  -\[GADMediatedNativeAdDelegate mediatedNativeAdDidRecordImpression:\].

  #### Declaration

  Objective-C

      - (BOOL)handlesUserImpressions;

- `


  ### [delegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventNativeAd#/c:objc(pl)GADCustomEventNativeAd(py)delegate)


  ` Delegate object used for receiving custom native ad load request progress.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventNativeAdDelegate.html>
          delegate;