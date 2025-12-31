# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeContentAdLoaderDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeContentAdLoaderDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADNativeContentAdLoaderDelegate

    protocol GADNativeContentAdLoaderDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.html

The delegate of a GADAdLoader object implements this protocol to receive GADNativeContentAd ads.
- `
  ``
  ``
  `

  ### [adLoader(_:didReceive:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeContentAdLoaderDelegate#/c:objc(pl)GADNativeContentAdLoaderDelegate(im)adLoader:didReceiveNativeContentAd:)

  `
  `  
  Called when native content is received.  

  #### Declaration

  Swift  

      func adLoader(_ adLoader: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader.html, didReceive nativeContentAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd.html)