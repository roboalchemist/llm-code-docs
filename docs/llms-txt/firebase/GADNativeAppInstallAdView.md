# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView.md.txt

# GoogleMobileAds Framework Reference

# GADNativeAppInstallAdView

    class GADNativeAppInstallAdView : UIView

Base class for app install ad views. Your app install ad view must be a subclass of this class
and must call superclass methods for all overriden methods.
- `
  ``
  ``
  `

  ### [nativeAppInstallAd](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)nativeAppInstallAd)

  `
  `  
  This property must point to the native app install ad object rendered by this ad view.  

  #### Declaration

  Swift  

      var nativeAppInstallAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAd.html? { get set }

- `
  ``
  ``
  `

  ### [headlineView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)headlineView)

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

  ### [callToActionView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)callToActionView)

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

  ### [iconView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)iconView)

  `
  `  
  Weak reference to your ad view's icon asset view.  

  #### Declaration

  Swift  

      @IBOutlet weak var iconView: UIView? { get set }

- `
  ``
  ``
  `

  ### [bodyView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)bodyView)

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

  ### [storeView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)storeView)

  `
  `  
  Weak reference to your ad view's store asset view.  

  #### Declaration

  Swift  

      @IBOutlet weak var storeView: UIView? { get set }

- `
  ``
  ``
  `

  ### [priceView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)priceView)

  `
  `  
  Weak reference to your ad view's price asset view.  

  #### Declaration

  Swift  

      @IBOutlet weak var priceView: UIView? { get set }

- `
  ``
  ``
  `

  ### [imageView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)imageView)

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

  ### [starRatingView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)starRatingView)

  `
  `  
  Weak reference to your ad view's star rating asset view.  

  #### Declaration

  Swift  

      @IBOutlet weak var starRatingView: UIView? { get set }

- `
  ``
  ``
  `

  ### [mediaView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)mediaView)

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

  ### [adChoicesView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAppInstallAdView#/c:objc(cs)GADNativeAppInstallAdView(py)adChoicesView)

  `
  `  
  Weak reference to your ad view's AdChoices view. Must set adChoicesView before setting
  nativeAppInstallAd, otherwise AdChoices will be rendered in the publisher's
  preferredAdChoicesPosition as defined in GADNativeAdViewAdOptions.  

  #### Declaration

  Swift  

      @IBOutlet weak var adChoicesView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdChoicesView? { get set }