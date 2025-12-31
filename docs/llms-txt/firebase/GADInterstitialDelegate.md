# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADInterstitialDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInterstitialDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADInterstitialDelegate

    protocol GADInterstitialDelegate : NSObjectProtocol

Delegate for receiving state change messages from a GADInterstitial such as interstitial ad
requests succeeding/failing.
[## Ad Request Lifecycle Notifications](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInterstitialDelegate#/Ad%20Request%20Lifecycle%20Notifications)

- `
  ``
  ``
  `

  ### [interstitialDidReceiveAd(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInterstitialDelegate#/c:objc(pl)GADInterstitialDelegate(im)interstitialDidReceiveAd:)

  `
  `  
  Called when an interstitial ad request succeeded. Show it at the next transition point in your
  application such as when transitioning between view controllers.  

  #### Declaration

  Swift  

      optional func interstitialDidReceiveAd(_ ad: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInterstitial.html)

- `
  ``
  ``
  `

  ### [interstitial(_:didFailToReceiveAdWithError:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInterstitialDelegate#/c:objc(pl)GADInterstitialDelegate(im)interstitial:didFailToReceiveAdWithError:)

  `
  `  
  Called when an interstitial ad request completed without an interstitial to
  show. This is common since interstitials are shown sparingly to users.  

  #### Declaration

  Swift  

      optional func interstitial(_ ad: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInterstitial.html, didFailToReceiveAdWithError error: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADRequestError)

[## Display-Time Lifecycle Notifications](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInterstitialDelegate#/Display-Time%20Lifecycle%20Notifications)

- `
  ``
  ``
  `

  ### [interstitialWillPresentScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInterstitialDelegate#/c:objc(pl)GADInterstitialDelegate(im)interstitialWillPresentScreen:)

  `
  `  
  Called just before presenting an interstitial. After this method finishes the interstitial will
  animate onto the screen. Use this opportunity to stop animations and save the state of your
  application in case the user leaves while the interstitial is on screen (e.g. to visit the App
  Store from a link on the interstitial).  

  #### Declaration

  Swift  

      optional func interstitialWillPresentScreen(_ ad: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInterstitial.html)

- `
  ``
  ``
  `

  ### [interstitialDidFail(toPresentScreen:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInterstitialDelegate#/c:objc(pl)GADInterstitialDelegate(im)interstitialDidFailToPresentScreen:)

  `
  `  
  Called when \|ad\| fails to present.  

  #### Declaration

  Swift  

      optional func interstitialDidFail(toPresentScreen ad: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInterstitial.html)

- `
  ``
  ``
  `

  ### [interstitialWillDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInterstitialDelegate#/c:objc(pl)GADInterstitialDelegate(im)interstitialWillDismissScreen:)

  `
  `  
  Called before the interstitial is to be animated off the screen.  

  #### Declaration

  Swift  

      optional func interstitialWillDismissScreen(_ ad: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInterstitial.html)

- `
  ``
  ``
  `

  ### [interstitialDidDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInterstitialDelegate#/c:objc(pl)GADInterstitialDelegate(im)interstitialDidDismissScreen:)

  `
  `  
  Called just after dismissing an interstitial and it has animated off the screen.  

  #### Declaration

  Swift  

      optional func interstitialDidDismissScreen(_ ad: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInterstitial.html)

- `
  ``
  ``
  `

  ### [interstitialWillLeaveApplication(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInterstitialDelegate#/c:objc(pl)GADInterstitialDelegate(im)interstitialWillLeaveApplication:)

  `
  `  
  Called just before the application will background or terminate because the user clicked on an
  ad that will launch another application (such as the App Store). The normal
  UIApplicationDelegate methods, like applicationDidEnterBackground:, will be called immediately
  before this.  

  #### Declaration

  Swift  

      optional func interstitialWillLeaveApplication(_ ad: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInterstitial.html)