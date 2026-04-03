# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView.md.txt

# GoogleMobileAds Framework Reference

# GADUnifiedNativeAdView

    class GADUnifiedNativeAdView : UIView

Base class for native ad views. Your native ad view must be a subclass of this class and must
call superclass methods for all overridden methods.
- `
  ``
  ``
  `

  ### [nativeAd](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)nativeAd)

  `
  `  
  This property must point to the unified native ad object rendered by this ad view.  

  #### Declaration

  Swift  

      var nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.html? { get set }

- `
  ``
  ``
  `

  ### [headlineView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)headlineView)

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

  ### [callToActionView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)callToActionView)

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

  ### [iconView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)iconView)

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

  ### [bodyView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)bodyView)

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

  ### [storeView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)storeView)

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

  ### [priceView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)priceView)

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

  ### [imageView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)imageView)

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

  ### [starRatingView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)starRatingView)

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

  ### [advertiserView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)advertiserView)

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

  ### [mediaView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)mediaView)

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

  ### [adChoicesView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAdView#/c:objc(cs)GADUnifiedNativeAdView(py)adChoicesView)

  `
  `  
  Weak reference to your ad view's AdChoices view. Must set adChoicesView before setting
  nativeAd, otherwise AdChoices will be rendered according to the preferredAdChoicesPosition
  defined in GADNativeAdViewAdOptions.  

  #### Declaration

  Swift  

      @IBOutlet weak var adChoicesView: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdChoicesView? { get set }