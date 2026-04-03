# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/DFPCustomRenderedInterstitialDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/DFPCustomRenderedInterstitialDelegate.md.txt

# GoogleMobileAds Framework Reference

# DFPCustomRenderedInterstitialDelegate

    protocol DFPCustomRenderedInterstitialDelegate : NSObjectProtocol

The DFPCustomRenderedAd interstitial delegate protocol for notifying the delegate of changes to
custom rendered interstitials.
- `
  ``
  ``
  `

  ### [interstitial(_:didReceive:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/DFPCustomRenderedInterstitialDelegate#/c:objc(pl)DFPCustomRenderedInterstitialDelegate(im)interstitial:didReceiveCustomRenderedAd:)

  `
  `  
  Called after ad data has been received. You must construct an interstitial from
  \|customRenderedAd\| and call the \|customRenderedAd\| object's finishedRenderingAdView: method when
  the ad has been rendered.  

  #### Declaration

  Swift  

      func interstitial(_ interstitial: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPInterstitial.html, didReceive customRenderedAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPCustomRenderedAd.html)