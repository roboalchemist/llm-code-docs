# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdLoaderDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADUnifiedNativeAdLoaderDelegate

    protocol GADUnifiedNativeAdLoaderDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.html

The delegate of a GADAdLoader object implements this protocol to receive GADUnifiedNativeAd ads.
- `


  ### [adLoader(_:didReceive:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdLoaderDelegate#/c:objc(pl)GADUnifiedNativeAdLoaderDelegate(im)adLoader:didReceiveUnifiedNativeAd:)


  ` Called when a unified native ad is received.

  #### Declaration

  Swift

      func adLoader(_ adLoader: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader.html, didReceive nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.html)