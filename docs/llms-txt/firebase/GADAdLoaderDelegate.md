# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADAdLoaderDelegate

    protocol GADAdLoaderDelegate : NSObjectProtocol

Base ad loader delegate protocol. Ad types provide extended protocols that declare methods to
handle successful ad loads.
- `
  ``
  ``
  `

  ### [adLoader(_:didFailToReceiveAdWithError:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate#/c:objc(pl)GADAdLoaderDelegate(im)adLoader:didFailToReceiveAdWithError:)

  `
  `  
  Called when adLoader fails to load an ad.  

  #### Declaration

  Swift  

      func adLoader(_ adLoader: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader.html, didFailToReceiveAdWithError error: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADRequestError)

- `
  ``
  ``
  `

  ### [adLoaderDidFinishLoading(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate#/c:objc(pl)GADAdLoaderDelegate(im)adLoaderDidFinishLoading:)

  `
  `  
  Called after adLoader has finished loading.  

  #### Declaration

  Swift  

      optional func adLoaderDidFinishLoading(_ adLoader: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader.html)