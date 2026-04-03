# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeContentAdView.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAdView.md.txt

# GoogleMobileAds Framework Reference

# GADNativeContentAdView

    class GADNativeContentAdView : UIView

Base class for content ad views. Your content ad view must be a subclass of this class and must
call superclass methods for all overriden methods.
- `
  ``
  ``
  `

  ### [nativeContentAd](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)nativeContentAd)

  `
  `  
  This property must point to the native content ad object rendered by this ad view.  

  #### Declaration

  Swift  

      var nativeContentAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAd.html? { get set }

- `
  ``
  ``
  `

  ### [headlineView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)headlineView)

  `
  `  
  Weak reference to your ad view's headline asset view.  

  #### Declaration

  Swift  

      @IBOutlet weak var headlineView: UIView? { get set }

- `
  ``
  ``
  `

  ### [bodyView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)bodyView)

  `
  `  
  Weak reference to your ad view's body asset view.  

  #### Declaration

  Swift  

      @IBOutlet weak var bodyView: UIView? { get set }

- `
  ``
  ``
  `

  ### [imageView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)imageView)

  `
  `  
  Weak reference to your ad view's image asset view.  

  #### Declaration

  Swift  

      @IBOutlet weak var imageView: UIView? { get set }

- `
  ``
  ``
  `

  ### [logoView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)logoView)

  `
  `  
  Weak reference to your ad view's logo asset view.  

  #### Declaration

  Swift  

      @IBOutlet weak var logoView: UIView? { get set }

- `
  ``
  ``
  `

  ### [callToActionView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)callToActionView)

  `
  `  
  Weak reference to your ad view's call to action asset view.  

  #### Declaration

  Swift  

      @IBOutlet weak var callToActionView: UIView? { get set }

- `
  ``
  ``
  `

  ### [advertiserView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)advertiserView)

  `
  `  
  Weak reference to your ad view's advertiser asset view.  

  #### Declaration

  Swift  

      @IBOutlet weak var advertiserView: UIView? { get set }

- `
  ``
  ``
  `

  ### [mediaView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)mediaView)

  `
  `  
  Weak reference to your ad view's media asset view.  

  #### Declaration

  Swift  

      @IBOutlet weak var mediaView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediaView.html? { get set }

- `
  ``
  ``
  `

  ### [adChoicesView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeContentAdView#/c:objc(cs)GADNativeContentAdView(py)adChoicesView)

  `
  `  
  Weak reference to your ad view's AdChoices view. Must set adChoicesView before setting
  nativeContentAd, otherwise AdChoices will be rendered in the publisher's
  preferredAdChoicesPosition as defined in GADNativeAdViewAdOptions.  

  #### Declaration

  Swift  

      @IBOutlet weak var adChoicesView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdChoicesView? { get set }