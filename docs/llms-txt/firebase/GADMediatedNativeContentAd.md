# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd.md.txt

# GoogleMobileAds Framework Reference

# GADMediatedNativeContentAd

    protocol GADMediatedNativeContentAd : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html

Provides methods used for constructing native content ads.
- `
  ``
  ``
  `

  ### [headline()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)headline)

  `
  `  
  Primary text headline.  

  #### Declaration

  Swift  

      func headline() -> String?

- `
  ``
  ``
  `

  ### [body()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)body)

  `
  `  
  Secondary text.  

  #### Declaration

  Swift  

      func body() -> String?

- `
  ``
  ``
  `

  ### [images()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)images)

  `
  `  
  List of large images. Each object is an instance of GADNativeAdImage.  

  #### Declaration

  Swift  

      func images() -> [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage.html]?

- `
  ``
  ``
  `

  ### [logo()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)logo)

  `
  `  
  Small logo image.  

  #### Declaration

  Swift  

      func logo() -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage.html?

- `
  ``
  ``
  `

  ### [callToAction()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)callToAction)

  `
  `  
  Text that encourages user to take some action with the ad.  

  #### Declaration

  Swift  

      func callToAction() -> String?

- `
  ``
  ``
  `

  ### [advertiser()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)advertiser)

  `
  `  
  Identifies the advertiser. For example, the advertiser's name or visible URL.  

  #### Declaration

  Swift  

      func advertiser() -> String?

- `
  ``
  ``
  `

  ### [adChoicesView()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)adChoicesView)

  `
  `  
  AdChoices view.  

  #### Declaration

  Swift  

      optional func adChoicesView() -> UIView?

- `
  ``
  ``
  `

  ### [mediaView()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)mediaView)

  `
  `  
  Media view.  

  #### Declaration

  Swift  

      optional func mediaView() -> UIView?

- `
  ``
  ``
  `

  ### [hasVideoContent()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)hasVideoContent)

  `
  `  
  Indicates whether the ad has video content.  

  #### Declaration

  Swift  

      optional func hasVideoContent() -> Bool