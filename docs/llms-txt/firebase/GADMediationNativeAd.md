# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationNativeAd.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationNativeAd.md.txt

# GoogleMobileAds Framework Reference

# GADMediationNativeAd

    @protocol GADMediationNativeAd <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADMediationAd, https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html>

Rendered native ad.
- `
  ``
  ``
  `

  ### [-handlesUserClicks](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationNativeAd#/c:objc(pl)GADMediationNativeAd(im)handlesUserClicks)

  `
  `  
  Indicates whether the ad handles user clicks. If this method returns YES, the ad must handle
  user clicks and notify the Google Mobile Ads SDK of clicks using
  -\[GADMediationAdEventDelegate reportClick:\]. If this method returns NO, the Google Mobile Ads
  SDK handles user clicks and notifies the ad of clicks using -\[GADMediationNativeAd
  didRecordClickOnAssetWithName:view:viewController:\].  

  #### Declaration

  Objective-C  

      - (BOOL)handlesUserClicks;

- `
  ``
  ``
  `

  ### [-handlesUserImpressions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationNativeAd#/c:objc(pl)GADMediationNativeAd(im)handlesUserImpressions)

  `
  `  
  Indicates whether the ad handles user impressions tracking. If this method returns YES, the
  Google Mobile Ads SDK will not track user impressions and the ad must notify the
  Google Mobile Ads SDK of impressions using -\[GADMediationAdEventDelegate
  reportImpression:\]. If this method returns NO, the Google Mobile Ads SDK tracks user impressions
  and notifies the ad of impressions using -\[GADMediationNativeAd didRecordImpression:\].  

  #### Declaration

  Objective-C  

      - (BOOL)handlesUserImpressions;