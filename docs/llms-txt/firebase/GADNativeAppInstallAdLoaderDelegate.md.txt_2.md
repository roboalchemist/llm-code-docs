# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeAppInstallAdLoaderDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADNativeAppInstallAdLoaderDelegate

    @protocol GADNativeAppInstallAdLoaderDelegate <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.html>

The delegate of a GADAdLoader object implements this protocol to receive GADNativeAppInstallAd
ads.
- `


  ### [-adLoader:didReceiveNativeAppInstallAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeAppInstallAdLoaderDelegate#/c:objc(pl)GADNativeAppInstallAdLoaderDelegate(im)adLoader:didReceiveNativeAppInstallAd:)


  ` Called when a native app install ad is received.

  #### Declaration

  Objective-C

      - (void)adLoader:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader.html *)adLoader
          didReceiveNativeAppInstallAd:
              (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAd.html *)nativeAppInstallAd;