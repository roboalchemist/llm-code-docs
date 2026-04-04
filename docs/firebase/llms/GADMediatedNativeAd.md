# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.md.txt

# GoogleMobileAds Framework Reference

# GADMediatedNativeAd

    protocol GADMediatedNativeAd : NSObjectProtocol

Base protocol for mediated native ads.
- `
  ``
  ``
  `

  ### [mediatedNativeAdDelegate()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd#/c:objc(pl)GADMediatedNativeAd(im)mediatedNativeAdDelegate)

  `
  `  
  Returns a delegate object that receives state change notifications.  

  #### Declaration

  Swift  

      func mediatedNativeAdDelegate() -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAdDelegate.html?

- `
  ``
  ``
  `

  ### [extraAssets()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd#/c:objc(pl)GADMediatedNativeAd(im)extraAssets)

  `
  `  
  Returns a dictionary of asset names and object pairs for assets that are not handled by
  properties of the GADMediatedNativeAd subclass.  

  #### Declaration

  Swift  

      func extraAssets() -> [AnyHashable : Any]?