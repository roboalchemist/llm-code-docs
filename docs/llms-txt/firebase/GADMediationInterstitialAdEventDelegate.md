# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationInterstitialAdEventDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationInterstitialAdEventDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADMediationInterstitialAdEventDelegate

    protocol GADMediationInterstitialAdEventDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate.html

Reports interstitial related information to the Google Mobile Ads SDK from the adapter.
- `
  ``
  ``
  `

  ### [willBackgroundApplication()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationInterstitialAdEventDelegate#/c:objc(pl)GADMediationInterstitialAdEventDelegate(im)willBackgroundApplication)

  `
  `  
  Notifies Google Mobile Ads SDK that an action on the GADMediationAd will cause the application
  to move into the background.  

  #### Declaration

  Swift  

      func willBackgroundApplication()