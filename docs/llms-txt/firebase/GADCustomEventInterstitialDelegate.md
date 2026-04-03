# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADCustomEventInterstitialDelegate

    protocol GADCustomEventInterstitialDelegate : NSObjectProtocol

Call back to this delegate in your custom event. You must call
customEventInterstitialDidReceiveAd: when there is an ad to show, or
customEventInterstitial:didFailAd: when there is no ad to show. Otherwise, if enough time passed
(several seconds) after the SDK called the requestInterstitialAdWithParameter: method of your
custom event, the mediation SDK will consider the request timed out, and move on to the next ad
network.
- `
  ``
  ``
  `

  ### [-customEventInterstitialDidReceiveAd:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitialDidReceiveAd:)

  `
  `  
  Your Custom Event object must call this when it receives or creates an interstitial ad.
- `
  ``
  ``
  `

  ### [-customEventInterstitial:didFailAd:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitial:didFailAd:)

  `
  `  
  Your Custom Event object must call this when it fails to receive or create the ad. Pass along
  any error object sent from the ad network's SDK, or an NSError describing the error. Pass nil if
  not available.
- `
  ``
  ``
  `

  ### [-customEventInterstitialWasClicked:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitialWasClicked:)

  `
  `  
  Your Custom Event object should call this when the user touches or clicks the ad to initiate
  an action. When the SDK receives this callback, it reports the click back to the mediation
  server.
- `
  ``
  ``
  `

  ### [-customEventInterstitialWillPresent:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitialWillPresent:)

  `
  `  
  Your Custom Event should call this when the interstitial is being displayed.
- `
  ``
  ``
  `

  ### [-customEventInterstitialWillDismiss:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitialWillDismiss:)

  `
  `  
  Your Custom Event should call this when the interstitial is about to be dismissed.
- `
  ``
  ``
  `

  ### [-customEventInterstitialDidDismiss:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitialDidDismiss:)

  `
  `  
  Your Custom Event should call this when the interstitial has been dismissed.
- `
  ``
  ``
  `

  ### [-customEventInterstitialWillLeaveApplication:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitialWillLeaveApplication:)

  `
  `  
Your Custom Event should call this method when a user action will result in app switching.  
[## Deprecated](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/Deprecated)

- `
  ``
  ``
  `

  ### [-customEventInterstitial:didReceiveAd:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitial:didReceiveAd:)

  `
  `  
  Deprecated. Use customEventInterstitialDidReceiveAd:.