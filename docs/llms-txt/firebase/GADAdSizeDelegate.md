# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdSizeDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdSizeDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADAdSizeDelegate

    @protocol GADAdSizeDelegate <NSObject>

The class implementing this protocol will be notified when the GADBannerView's ad content
changes size. Any views that may be affected by the banner size change will have time to adjust.
- `
  ``
  ``
  `

  ### [-adView:willChangeAdSizeTo:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdSizeDelegate#/c:objc(pl)GADAdSizeDelegate(im)adView:willChangeAdSizeTo:)

  `
  `  
  Called before the ad view changes to the new size.  

  #### Declaration

  Objective-C  

      - (void)adView:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADBannerView.html *)bannerView
          willChangeAdSizeTo:(https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize.html)size;