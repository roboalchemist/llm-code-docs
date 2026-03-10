# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationBannerAd.md.txt

# GoogleMobileAds Framework Reference

# GADMediationBannerAd

    protocol GADMediationBannerAd : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADMediationAd

Rendered banner ad. Provides a single subview to add to the banner view's view hierarchy.
- `


  ### [view](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationBannerAd#/c:objc(pl)GADMediationBannerAd(py)view)


  ` Undocumented

  #### Declaration

  Swift

      var view: UIView { get }

- `


  ### [changeSize(to:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationBannerAd#/c:objc(pl)GADMediationBannerAd(im)changeAdSizeTo:)


  ` Tells the ad to resize the banner. Implement if banner content is resizable.

  #### Declaration

  Swift

      optional func changeSize(to adSize: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize.html)