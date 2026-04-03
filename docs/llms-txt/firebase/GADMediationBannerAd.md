# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationBannerAd.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationBannerAd.md.txt

# GoogleMobileAds Framework Reference

# GADMediationBannerAd

    @protocol GADMediationBannerAd <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADMediationAd>

Rendered banner ad. Provides a single subview to add to the banner view's view hierarchy.
- `
  ``
  ``
  `

  ### [view](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationBannerAd#/c:objc(pl)GADMediationBannerAd(py)view)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      @property(nonatomic, readonly, nonnull) UIView *view

- `
  ``
  ``
  `

  ### [-changeAdSizeTo:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationBannerAd#/c:objc(pl)GADMediationBannerAd(im)changeAdSizeTo:)

  `
  `  
  Tells the ad to resize the banner. Implement if banner content is resizable.  

  #### Declaration

  Objective-C  

      - (void)changeAdSizeTo:(https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize.html)adSize;