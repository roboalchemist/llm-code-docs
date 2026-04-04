# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeCustomTemplateAdLoaderDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeCustomTemplateAdLoaderDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADNativeCustomTemplateAdLoaderDelegate

    protocol GADNativeCustomTemplateAdLoaderDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.html

The delegate of a GADAdLoader object implements this protocol to receive
GADNativeCustomTemplateAd ads.
- `
  ``
  ``
  `

  ### [nativeCustomTemplateIDs(for:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeCustomTemplateAdLoaderDelegate#/c:objc(pl)GADNativeCustomTemplateAdLoaderDelegate(im)nativeCustomTemplateIDsForAdLoader:)

  `
  `  
  Called when requesting an ad. Asks the delegate for an array of custom template ID strings.  

  #### Declaration

  Swift  

      func nativeCustomTemplateIDs(for adLoader: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader.html) -> [String]

- `
  ``
  ``
  `

  ### [adLoader(_:didReceive:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeCustomTemplateAdLoaderDelegate#/c:objc(pl)GADNativeCustomTemplateAdLoaderDelegate(im)adLoader:didReceiveNativeCustomTemplateAd:)

  `
  `  
  Tells the delegate that a native custom template ad was received.  

  #### Declaration

  Swift  

      func adLoader(_ adLoader: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader.html, didReceive nativeCustomTemplateAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd.html)