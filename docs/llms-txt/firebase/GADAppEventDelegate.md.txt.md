# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAppEventDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADAppEventDelegate

    protocol GADAppEventDelegate : NSObjectProtocol

Implement your app event within these methods. The delegate will be notified when the SDK
receives an app event message from the ad.
- `


  ### [adView(_:didReceiveAppEvent:withInfo:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAppEventDelegate#/c:objc(pl)GADAppEventDelegate(im)adView:didReceiveAppEvent:withInfo:)


  ` Called when the banner receives an app event.

  #### Declaration

  Swift

      optional func adView(_ banner: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView.html, didReceiveAppEvent name: String, withInfo info: String?)

- `


  ### [interstitial(_:didReceiveAppEvent:withInfo:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAppEventDelegate#/c:objc(pl)GADAppEventDelegate(im)interstitial:didReceiveAppEvent:withInfo:)


  ` Called when the interstitial receives an app event.

  #### Declaration

  Swift

      optional func interstitial(_ interstitial: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInterstitial.html, didReceiveAppEvent name: String, withInfo info: String?)