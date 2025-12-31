# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/DFPCustomRenderedBannerViewDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/DFPCustomRenderedBannerViewDelegate.md.txt

# GoogleMobileAds Framework Reference

# DFPCustomRenderedBannerViewDelegate

    protocol DFPCustomRenderedBannerViewDelegate : NSObjectProtocol

The DFPCustomRenderedAd banner view delegate protocol for notifying the delegate of changes to
custom rendered banners.
- `
  ``
  ``
  `

  ### [bannerView(_:didReceive:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/DFPCustomRenderedBannerViewDelegate#/c:objc(pl)DFPCustomRenderedBannerViewDelegate(im)bannerView:didReceiveCustomRenderedAd:)

  `
  `  
  Called after ad data has been received. You must construct a banner from \|customRenderedAd\| and
  call the \|customRenderedAd\| object's finishedRenderingAdView: when the ad has been rendered.  

  #### Declaration

  Swift  

      func bannerView(_ bannerView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPBannerView.html, didReceive customRenderedAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPCustomRenderedAd.html)