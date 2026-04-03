# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPInterstitial.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPInterstitial.md.txt

# GoogleMobileAds Framework Reference

# DFPInterstitial

    class DFPInterstitial : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInterstitial.html

Google Ad Manager interstitial ad, a full-screen advertisement shown at natural
transition points in your application such as between game levels or news stories.
- `
  ``
  ``
  `

  ### [init(adUnitID:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPInterstitial#/c:objc(cs)DFPInterstitial(im)initWithAdUnitID:)

  `
  `  
  Initializes an interstitial with an ad unit created on the Ad Manager website. Create a new ad
  unit for every unique placement of an ad in your application. Set this to the ID assigned for
  this placement. Ad units are important for targeting and statistics.

  Example Ad Manager ad unit ID: @/6499/example/interstitial  

  #### Declaration

  Swift  

      init(adUnitID: String)

- `
  ``
  ``
  `

  ### [correlator](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPInterstitial#/c:objc(cs)DFPInterstitial(py)correlator)

  `
  `  
  Correlator object for correlating this object to other ad objects.  

  #### Declaration

  Swift  

      var correlator: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCorrelator.html? { get set }

- `
  ``
  ``
  `

  ### [appEventDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPInterstitial#/c:objc(cs)DFPInterstitial(py)appEventDelegate)

  `
  `  
  Optional delegate that is notified when creatives send app events.  

  #### Declaration

  Swift  

      weak var appEventDelegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAppEventDelegate.html? { get set }

- `
  ``
  ``
  `

  ### [customRenderedInterstitialDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPInterstitial#/c:objc(cs)DFPInterstitial(py)customRenderedInterstitialDelegate)

  `
  `  
  Optional delegate object for custom rendered ads.  

  #### Declaration

  Swift  

      weak var customRenderedInterstitialDelegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/DFPCustomRenderedInterstitialDelegate.html? { get set }