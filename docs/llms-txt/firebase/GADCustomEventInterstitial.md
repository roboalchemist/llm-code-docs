# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial.md.txt

# GoogleMobileAds Framework Reference

# GADCustomEventInterstitial

    protocol GADCustomEventInterstitial : NSObjectProtocol

The interstitial custom event protocol. Your interstitial custom event handler must implement
this protocol.
- `
  ``
  ``
  `

  ### [delegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial#/c:objc(pl)GADCustomEventInterstitial(py)delegate)

  `
  `  
  Inform \|delegate\| with the custom event execution results to ensure mediation behaves correctly.

  In your class, define the -delegate and -setDelegate: methods or use @synthesize delegate. The
  Google Mobile Ads SDK sets this property on instances of your class.  

  #### Declaration

  Swift  

      weak var delegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate.html? { get set }

- `
  ``
  ``
  `

  ### [requestAd(withParameter:label:request:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial#/c:objc(pl)GADCustomEventInterstitial(im)requestInterstitialAdWithParameter:label:request:)

  `
  `  
  Called by mediation when your custom event is scheduled to be executed. Your implementation
  should start retrieving the interstitial ad. Report execution results to the delegate. You must
  wait until -presentFromRootViewController is called before displaying the interstitial ad.  

  #### Declaration

  Swift  

      func requestAd(withParameter serverParameter: String?, label serverLabel: String?, request: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCustomEventRequest.html)

  #### Parameters

  |-------------------------|-------------------------------------------|
  | ` `*serverParameter*` ` | Parameter configured in the mediation UI. |
  | ` `*serverLabel*` `     | Label configured in the mediation UI.     |
  | ` `*request*` `         | Contains ad request information.          |

- `
  ``
  ``
  `

  ### [present(fromRootViewController:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial#/c:objc(pl)GADCustomEventInterstitial(im)presentFromRootViewController:)

  `
  `  
  Present the interstitial ad as a modal view using the provided view controller. Called only
  after your class calls -customEventInterstitialDidReceiveAd: on its custom event delegate.  

  #### Declaration

  Swift  

      func present(fromRootViewController rootViewController: UIViewController)