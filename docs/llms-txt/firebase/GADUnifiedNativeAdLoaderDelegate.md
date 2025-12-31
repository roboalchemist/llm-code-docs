# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdLoaderDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdLoaderDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADUnifiedNativeAdLoaderDelegate

    @protocol GADUnifiedNativeAdLoaderDelegate <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.html>

The delegate of a GADAdLoader object implements this protocol to receive GADUnifiedNativeAd ads.
- `
  ``
  ``
  `

  ### [-adLoader:didReceiveUnifiedNativeAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdLoaderDelegate#/c:objc(pl)GADUnifiedNativeAdLoaderDelegate(im)adLoader:didReceiveUnifiedNativeAd:)

  `
  `  
  Called when a unified native ad is received.  

  #### Declaration

  Objective-C  

      - (void)adLoader:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader.html *)adLoader
          didReceiveUnifiedNativeAd:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.html *)nativeAd;