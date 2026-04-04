# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationBannerAdEventDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationBannerAdEventDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADMediationBannerAdEventDelegate

    protocol GADMediationBannerAdEventDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate.html

Reports banner related information to the Google Mobile Ads SDK from the adapter.
- `
  ``
  ``
  `

  ### [willBackgroundApplication()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationBannerAdEventDelegate#/c:objc(pl)GADMediationBannerAdEventDelegate(im)willBackgroundApplication)

  `
  `  
  Notifies Google Mobile Ads SDK that an action on the GADMediationAd will cause the application
  to move into the background.  

  #### Declaration

  Swift  

      func willBackgroundApplication()