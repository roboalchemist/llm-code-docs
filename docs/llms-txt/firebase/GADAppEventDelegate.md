# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAppEventDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAppEventDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADAppEventDelegate

    @protocol GADAppEventDelegate <NSObject>

Implement your app event within these methods. The delegate will be notified when the SDK
receives an app event message from the ad.
- `
  ``
  ``
  `

  ### [-adView:didReceiveAppEvent:withInfo:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAppEventDelegate#/c:objc(pl)GADAppEventDelegate(im)adView:didReceiveAppEvent:withInfo:)

  `
  `  
  Called when the banner receives an app event.  

  #### Declaration

  Objective-C  

      - (void)adView:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADBannerView.html *)banner
          didReceiveAppEvent:(nonnull NSString *)name
                    withInfo:(nullable NSString *)info;

- `
  ``
  ``
  `

  ### [-interstitial:didReceiveAppEvent:withInfo:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAppEventDelegate#/c:objc(pl)GADAppEventDelegate(im)interstitial:didReceiveAppEvent:withInfo:)

  `
  `  
  Called when the interstitial receives an app event.  

  #### Declaration

  Objective-C  

      - (void)interstitial:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInterstitial.html *)interstitial
          didReceiveAppEvent:(nonnull NSString *)name
                    withInfo:(nullable NSString *)info;