# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdUnconfirmedClickDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdUnconfirmedClickDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADUnifiedNativeAdUnconfirmedClickDelegate

    protocol GADUnifiedNativeAdUnconfirmedClickDelegate : NSObjectProtocol

Delegate methods for handling unified native ad unconfirmed clicks.
- `
  ``
  ``
  `

  ### [nativeAd(_:didReceiveUnconfirmedClickOnAssetID:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdUnconfirmedClickDelegate#/c:objc(pl)GADUnifiedNativeAdUnconfirmedClickDelegate(im)nativeAd:didReceiveUnconfirmedClickOnAssetID:)

  `
  `  
  Tells the delegate that native ad receives an unconfirmed click on view with asset ID. You
  should update user interface and ask user to confirm the click once this message is received.
  Use the -registerClickConfirmingView: method in GADUnifiedNativeAd+ConfirmedClick.h to register
  a view that will confirm the click. Only called for Google ads and is not supported for mediated
  ads.  

  #### Declaration

  Swift  

      func nativeAd(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.html, didReceiveUnconfirmedClickOnAssetID assetID: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADUnifiedNativeAdAssetIdentifiers.h@T@GADUnifiedNativeAssetIdentifier)

- `
  ``
  ``
  `

  ### [nativeAdDidCancelUnconfirmedClick(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdUnconfirmedClickDelegate#/c:objc(pl)GADUnifiedNativeAdUnconfirmedClickDelegate(im)nativeAdDidCancelUnconfirmedClick:)

  `
  `  
  Tells the delegate that the unconfirmed click is cancelled. You should revert the user interface
  change once this message is received. Only called for Google ads and is not supported for
  mediated ads.  

  #### Declaration

  Swift  

      func nativeAdDidCancelUnconfirmedClick(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.html)