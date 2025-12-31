# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADCustomEventBannerDelegate

    protocol GADCustomEventBannerDelegate : NSObjectProtocol

Call back to this delegate in your custom event. You must call customEventBanner:didReceiveAd:
when there is an ad to show, or customEventBanner:didFailAd: when there is no ad to show.
Otherwise, if enough time passed (several seconds) after the SDK called the requestBannerAd:
method of your custom event, the mediation SDK will consider the request timed out, and move on
to the next ad network.
- `
  ``
  ``
  `

  ### [-customEventBanner:didReceiveAd:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate#/c:objc(pl)GADCustomEventBannerDelegate(im)customEventBanner:didReceiveAd:)

  `
  `  
  Your Custom Event object must call this when it receives or creates an ad view.
- `
  ``
  ``
  `

  ### [-customEventBanner:didFailAd:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate#/c:objc(pl)GADCustomEventBannerDelegate(im)customEventBanner:didFailAd:)

  `
  `  
  Your Custom Event object must call this when it fails to receive or create the ad view. Pass
  along any error object sent from the ad network's SDK, or an NSError describing the error. Pass
  nil if not available.
- `
  ``
  ``
  `

  ### [-customEventBannerWasClicked:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate#/c:objc(pl)GADCustomEventBannerDelegate(im)customEventBannerWasClicked:)

  `
  `  
  Your Custom Event object should call this when the user touches or clicks the ad to initiate
  an action. When the SDK receives this callback, it reports the click back to the mediation
  server.
- `
  ``
  ``
  `

  ### [viewControllerForPresentingModalView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate#/c:objc(pl)GADCustomEventBannerDelegate(py)viewControllerForPresentingModalView)

  `
  `  
  The rootViewController that you set in GADBannerView. Use this UIViewController to show a modal
  view when a user taps on the ad.  

  #### Declaration

  Swift  

      var viewControllerForPresentingModalView: UIViewController { get }

- `
  ``
  ``
  `

  ### [-customEventBannerWillPresentModal:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate#/c:objc(pl)GADCustomEventBannerDelegate(im)customEventBannerWillPresentModal:)

  `
  `  
  Your Custom Event should call this when the user taps an ad and a modal view appears.
- `
  ``
  ``
  `

  ### [-customEventBannerWillDismissModal:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate#/c:objc(pl)GADCustomEventBannerDelegate(im)customEventBannerWillDismissModal:)

  `
  `  
  Your Custom Event should call this when the user dismisses the modal view and the modal view is
  about to go away.
- `
  ``
  ``
  `

  ### [-customEventBannerDidDismissModal:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate#/c:objc(pl)GADCustomEventBannerDelegate(im)customEventBannerDidDismissModal:)

  `
  `  
  Your Custom Event should call this when the user dismisses the modal view and the modal view has
  gone away.
- `
  ``
  ``
  `

  ### [-customEventBannerWillLeaveApplication:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate#/c:objc(pl)GADCustomEventBannerDelegate(im)customEventBannerWillLeaveApplication:)

  `
  `  
Your Custom Event should call this method when a user action will result in App switching.  
[## Deprecated](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate#/Deprecated)

- `
  ``
  ``
  `

  ### [-customEventBanner:clickDidOccurInAd:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate#/c:objc(pl)GADCustomEventBannerDelegate(im)customEventBanner:clickDidOccurInAd:)

  `
  `  
  Deprecated. Use customEventBannerWasClicked:.