# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/DFPBannerAdLoaderDelegate.md.txt

# GoogleMobileAds Framework Reference

# DFPBannerAdLoaderDelegate

    @protocol DFPBannerAdLoaderDelegate <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.html>

The delegate of a GADAdLoader object must conform to this protocol to receive DFPBannerViews.
- `


  ### [-validBannerSizesForAdLoader:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/DFPBannerAdLoaderDelegate#/c:objc(pl)DFPBannerAdLoaderDelegate(im)validBannerSizesForAdLoader:)


  ` Asks the delegate which banner ad sizes should be requested.

  #### Declaration

  Objective-C

      - (nonnull NSArray<NSValue *> *)validBannerSizesForAdLoader:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader.html *)adLoader;

- `


  ### [-adLoader:didReceiveDFPBannerView:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/DFPBannerAdLoaderDelegate#/c:objc(pl)DFPBannerAdLoaderDelegate(im)adLoader:didReceiveDFPBannerView:)


  ` Tells the delegate that a Google Ad Manager banner ad was received.

  #### Declaration

  Objective-C

      - (void)adLoader:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader.html *)adLoader
          didReceiveDFPBannerView:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView.html *)bannerView;