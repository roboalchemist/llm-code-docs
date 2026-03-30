# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdSizeDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADAdSizeDelegate

    protocol GADAdSizeDelegate : NSObjectProtocol

The class implementing this protocol will be notified when the GADBannerView's ad content
changes size. Any views that may be affected by the banner size change will have time to adjust.
- `


  ### [adView(_:willChangeAdSizeTo:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdSizeDelegate#/c:objc(pl)GADAdSizeDelegate(im)adView:willChangeAdSizeTo:)


  ` Called before the ad view changes to the new size.

  #### Declaration

  Swift

      func adView(_ bannerView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView.html, willChangeAdSizeTo size: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize.html)