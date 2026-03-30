# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeCustomTemplateAdLoaderDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADNativeCustomTemplateAdLoaderDelegate

    @protocol GADNativeCustomTemplateAdLoaderDelegate <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.html>

The delegate of a GADAdLoader object implements this protocol to receive
GADNativeCustomTemplateAd ads.
- `


  ### [-nativeCustomTemplateIDsForAdLoader:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeCustomTemplateAdLoaderDelegate#/c:objc(pl)GADNativeCustomTemplateAdLoaderDelegate(im)nativeCustomTemplateIDsForAdLoader:)


  ` Called when requesting an ad. Asks the delegate for an array of custom template ID strings.

  #### Declaration

  Objective-C

      - (nonnull NSArray<NSString *> *)nativeCustomTemplateIDsForAdLoader:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader.html *)adLoader;

- `


  ### [-adLoader:didReceiveNativeCustomTemplateAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeCustomTemplateAdLoaderDelegate#/c:objc(pl)GADNativeCustomTemplateAdLoaderDelegate(im)adLoader:didReceiveNativeCustomTemplateAd:)


  ` Tells the delegate that a native custom template ad was received.

  #### Declaration

  Objective-C

      - (void)adLoader:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader.html *)adLoader
          didReceiveNativeCustomTemplateAd:
              (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd.html *)nativeCustomTemplateAd;