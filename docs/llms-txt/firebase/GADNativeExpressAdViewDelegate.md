# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADNativeExpressAdViewDelegate

    protocol GADNativeExpressAdViewDelegate : NSObjectProtocol

Delegate methods for receiving GADNativeExpressAdView state change messages such as ad request
status and ad click lifecycle.
[## Ad Request Lifecycle Notifications](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/Ad%20Request%20Lifecycle%20Notifications)

- `
  ``
  ``
  `

  ### [nativeExpressAdViewDidReceiveAd(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/c:objc(pl)GADNativeExpressAdViewDelegate(im)nativeExpressAdViewDidReceiveAd:)

  `
  `  
  Tells the delegate that the native express ad view successfully received an ad. The delegate may
  want to add the native express ad view to the view hierarchy if it hasn't been added yet.  

  #### Declaration

  Swift  

      optional func nativeExpressAdViewDidReceiveAd(_ nativeExpressAdView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView.html)

- `
  ``
  ``
  `

  ### [nativeExpressAdView(_:didFailToReceiveAdWithError:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/c:objc(pl)GADNativeExpressAdViewDelegate(im)nativeExpressAdView:didFailToReceiveAdWithError:)

  `
  `  
  Tells the delegate that an ad request failed. The failure is normally due to network
  connectivity or ad availablility (i.e., no fill).  

  #### Declaration

  Swift  

      optional func nativeExpressAdView(_ nativeExpressAdView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView.html, didFailToReceiveAdWithError error: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADRequestError)

[## Click-Time Lifecycle Notifications](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/Click-Time%20Lifecycle%20Notifications)

- `
  ``
  ``
  `

  ### [nativeExpressAdViewWillPresentScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/c:objc(pl)GADNativeExpressAdViewDelegate(im)nativeExpressAdViewWillPresentScreen:)

  `
  `  
  Tells the delegate that a full screen view will be presented in response to the user clicking on
  an ad. The delegate may want to pause animations and time sensitive interactions.  

  #### Declaration

  Swift  

      optional func nativeExpressAdViewWillPresentScreen(_ nativeExpressAdView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView.html)

- `
  ``
  ``
  `

  ### [nativeExpressAdViewWillDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/c:objc(pl)GADNativeExpressAdViewDelegate(im)nativeExpressAdViewWillDismissScreen:)

  `
  `  
  Tells the delegate that the full screen view will be dismissed.  

  #### Declaration

  Swift  

      optional func nativeExpressAdViewWillDismissScreen(_ nativeExpressAdView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView.html)

- `
  ``
  ``
  `

  ### [nativeExpressAdViewDidDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/c:objc(pl)GADNativeExpressAdViewDelegate(im)nativeExpressAdViewDidDismissScreen:)

  `
  `  
  Tells the delegate that the full screen view has been dismissed. The delegate should restart
  anything paused while handling adViewWillPresentScreen:.  

  #### Declaration

  Swift  

      optional func nativeExpressAdViewDidDismissScreen(_ nativeExpressAdView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView.html)

- `
  ``
  ``
  `

  ### [nativeExpressAdViewWillLeaveApplication(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/c:objc(pl)GADNativeExpressAdViewDelegate(im)nativeExpressAdViewWillLeaveApplication:)

  `
  `  
  Tells the delegate that the user click will open another app, backgrounding the current
  application. The standard UIApplicationDelegate methods, like applicationDidEnterBackground:,
  are called immediately before this method is called.  

  #### Declaration

  Swift  

      optional func nativeExpressAdViewWillLeaveApplication(_ nativeExpressAdView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView.html)