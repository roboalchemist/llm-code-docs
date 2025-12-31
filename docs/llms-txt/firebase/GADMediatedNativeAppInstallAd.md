# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd.md.txt

# GoogleMobileAds Framework Reference

# GADMediatedNativeAppInstallAd

    protocol GADMediatedNativeAppInstallAd : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html

Provides methods used for constructing native app install ads. The adapter must return an object
conforming to this protocol for native app install ad requests.
- `
  ``
  ``
  `

  ### [headline()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)headline)

  `
  `  
  App title.  

  #### Declaration

  Swift  

      func headline() -> String?

- `
  ``
  ``
  `

  ### [images()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)images)

  `
  `  
  Array of GADNativeAdImage objects related to the advertised application.  

  #### Declaration

  Swift  

      func images() -> [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage.html]?

- `
  ``
  ``
  `

  ### [body()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)body)

  `
  `  
  App description.  

  #### Declaration

  Swift  

      func body() -> String?

- `
  ``
  ``
  `

  ### [icon()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)icon)

  `
  `  
  Application icon.  

  #### Declaration

  Swift  

      func icon() -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage.html?

- `
  ``
  ``
  `

  ### [callToAction()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)callToAction)

  `
  `  
  Text that encourages user to take some action with the ad. For example Install.  

  #### Declaration

  Swift  

      func callToAction() -> String?

- `
  ``
  ``
  `

  ### [starRating()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)starRating)

  `
  `  
  App store rating (0 to 5).  

  #### Declaration

  Swift  

      func starRating() -> NSDecimalNumber?

- `
  ``
  ``
  `

  ### [store()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)store)

  `
  `  
  The app store name. For example, App Store.  

  #### Declaration

  Swift  

      func store() -> String?

- `
  ``
  ``
  `

  ### [price()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)price)

  `
  `  
  String representation of the app's price.  

  #### Declaration

  Swift  

      func price() -> String?

- `
  ``
  ``
  `

  ### [adChoicesView()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)adChoicesView)

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

  ### [mediaView()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)mediaView)

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

  ### [hasVideoContent()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)hasVideoContent)

  `
  `  
  Indicates whether the ad has video content.  

  #### Declaration

  Swift  

      optional func hasVideoContent() -> Bool