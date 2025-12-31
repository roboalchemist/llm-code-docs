# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/DFPBannerAdLoaderDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/DFPBannerAdLoaderDelegate.md.txt

# GoogleMobileAds Framework Reference

# DFPBannerAdLoaderDelegate

    protocol DFPBannerAdLoaderDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.html

The delegate of a GADAdLoader object must conform to this protocol to receive DFPBannerViews.
- `
  ``
  ``
  `

  ### [validBannerSizes(for:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/DFPBannerAdLoaderDelegate#/c:objc(pl)DFPBannerAdLoaderDelegate(im)validBannerSizesForAdLoader:)

  `
  `  
  Asks the delegate which banner ad sizes should be requested.  

  #### Declaration

  Swift  

      func validBannerSizes(for adLoader: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader.html) -> [NSValue]

- `
  ``
  ``
  `

  ### [adLoader(_:didReceive:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/DFPBannerAdLoaderDelegate#/c:objc(pl)DFPBannerAdLoaderDelegate(im)adLoader:didReceiveDFPBannerView:)

  `
  `  
  Tells the delegate that a Google Ad Manager banner ad was received.  

  #### Declaration

  Swift  

      func adLoader(_ adLoader: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader.html, didReceive bannerView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPBannerView.html)