# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.md.txt

# GoogleMobileAds Framework Reference

# GADMediatedNativeAd

    @protocol GADMediatedNativeAd <NSObject>

Base protocol for mediated native ads.
- `


  ### [-mediatedNativeAdDelegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAd#/c:objc(pl)GADMediatedNativeAd(im)mediatedNativeAdDelegate)


  ` Returns a delegate object that receives state change notifications.

  #### Declaration

  Objective-C

      - (nullable id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAdDelegate.html>)mediatedNativeAdDelegate;

- `


  ### [-extraAssets](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAd#/c:objc(pl)GADMediatedNativeAd(im)extraAssets)


  ` Returns a dictionary of asset names and object pairs for assets that are not handled by
  properties of the GADMediatedNativeAd subclass.

  #### Declaration

  Objective-C

      - (nullable NSDictionary *)extraAssets;