# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeContentAdLoaderDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADNativeContentAdLoaderDelegate

    @protocol GADNativeContentAdLoaderDelegate <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.html>

The delegate of a GADAdLoader object implements this protocol to receive GADNativeContentAd ads.
- `


  ### [-adLoader:didReceiveNativeContentAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeContentAdLoaderDelegate#/c:objc(pl)GADNativeContentAdLoaderDelegate(im)adLoader:didReceiveNativeContentAd:)


  ` Called when native content is received.

  #### Declaration

  Objective-C

      - (void)adLoader:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader.html *)adLoader
          didReceiveNativeContentAd:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAd.html *)nativeContentAd;