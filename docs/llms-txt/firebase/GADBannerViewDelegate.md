# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADBannerViewDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADBannerViewDelegate

    protocol GADBannerViewDelegate : NSObjectProtocol

Delegate methods for receiving GADBannerView state change messages such as ad request status
and ad click lifecycle.
[## Ad Request Lifecycle Notifications](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/Ad%20Request%20Lifecycle%20Notifications)

- `
  ``
  ``
  `

  ### [adViewDidReceiveAd(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/c:objc(pl)GADBannerViewDelegate(im)adViewDidReceiveAd:)

  `
  `  
  Tells the delegate that an ad request successfully received an ad. The delegate may want to add
  the banner view to the view hierarchy if it hasn't been added yet.  

  #### Declaration

  Swift  

      optional func adViewDidReceiveAd(_ bannerView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView.html)

- `
  ``
  ``
  `

  ### [adView(_:didFailToReceiveAdWithError:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/c:objc(pl)GADBannerViewDelegate(im)adView:didFailToReceiveAdWithError:)

  `
  `  
  Tells the delegate that an ad request failed. The failure is normally due to network
  connectivity or ad availablility (i.e., no fill).  

  #### Declaration

  Swift  

      optional func adView(_ bannerView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView.html, didFailToReceiveAdWithError error: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADRequestError)

[## Click-Time Lifecycle Notifications](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/Click-Time%20Lifecycle%20Notifications)

- `
  ``
  ``
  `

  ### [adViewWillPresentScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/c:objc(pl)GADBannerViewDelegate(im)adViewWillPresentScreen:)

  `
  `  
  Tells the delegate that a full screen view will be presented in response to the user clicking on
  an ad. The delegate may want to pause animations and time sensitive interactions.  

  #### Declaration

  Swift  

      optional func adViewWillPresentScreen(_ bannerView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView.html)

- `
  ``
  ``
  `

  ### [adViewWillDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/c:objc(pl)GADBannerViewDelegate(im)adViewWillDismissScreen:)

  `
  `  
  Tells the delegate that the full screen view will be dismissed.  

  #### Declaration

  Swift  

      optional func adViewWillDismissScreen(_ bannerView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView.html)

- `
  ``
  ``
  `

  ### [adViewDidDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/c:objc(pl)GADBannerViewDelegate(im)adViewDidDismissScreen:)

  `
  `  
  Tells the delegate that the full screen view has been dismissed. The delegate should restart
  anything paused while handling adViewWillPresentScreen:.  

  #### Declaration

  Swift  

      optional func adViewDidDismissScreen(_ bannerView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView.html)

- `
  ``
  ``
  `

  ### [adViewWillLeaveApplication(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/c:objc(pl)GADBannerViewDelegate(im)adViewWillLeaveApplication:)

  `
  `  
  Tells the delegate that the user click will open another app, backgrounding the current
  application. The standard UIApplicationDelegate methods, like applicationDidEnterBackground:,
  are called immediately before this method is called.  

  #### Declaration

  Swift  

      optional func adViewWillLeaveApplication(_ bannerView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView.html)