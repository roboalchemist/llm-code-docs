# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADMediationAdEventDelegate

    protocol GADMediationAdEventDelegate : NSObjectProtocol

Reports information to the Google Mobile Ads SDK from the adapter. Adapters receive an ad event
delegate when they provide a GADMediationAd by calling a render completion handler.
- `
  ``
  ``
  `

  ### [reportImpression()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate#/c:objc(pl)GADMediationAdEventDelegate(im)reportImpression)

  `
  `  
  Notifies Google Mobile Ads SDK that an impression occurred on the GADMediationAd.  

  #### Declaration

  Swift  

      func reportImpression()

- `
  ``
  ``
  `

  ### [reportClick()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate#/c:objc(pl)GADMediationAdEventDelegate(im)reportClick)

  `
  `  
  Notifies Google Mobile Ads SDK that a click occurred on the GADMediationAd.  

  #### Declaration

  Swift  

      func reportClick()

- `
  ``
  ``
  `

  ### [willPresentFullScreenView()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate#/c:objc(pl)GADMediationAdEventDelegate(im)willPresentFullScreenView)

  `
  `  
  Notifies Google Mobile Ads SDK that the GADMediationAd will present a full screen modal view.  

  #### Declaration

  Swift  

      func willPresentFullScreenView()

- `
  ``
  ``
  `

  ### [didFailToPresentWithError(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate#/c:objc(pl)GADMediationAdEventDelegate(im)didFailToPresentWithError:)

  `
  `  
  Notifies Google Mobile Ads SDK that the GADMediationAd failed to present with an error.  

  #### Declaration

  Swift  

      func didFailToPresentWithError(_ error: Error)

- `
  ``
  ``
  `

  ### [willDismissFullScreenView()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate#/c:objc(pl)GADMediationAdEventDelegate(im)willDismissFullScreenView)

  `
  `  
  Notifies Google Mobile Ads SDK that the GADMediationAd will dismiss a full screen modal view.  

  #### Declaration

  Swift  

      func willDismissFullScreenView()

- `
  ``
  ``
  `

  ### [didDismissFullScreenView()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate#/c:objc(pl)GADMediationAdEventDelegate(im)didDismissFullScreenView)

  `
  `  
  Notifies Google Mobile Ads SDK that the GADMediationAd finished dismissing a full screen modal
  view.  

  #### Declaration

  Swift  

      func didDismissFullScreenView()