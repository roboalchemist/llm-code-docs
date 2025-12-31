# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADBannerView.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView.md.txt

# GoogleMobileAds Framework Reference

# GADBannerView

    class GADBannerView : UIView

The view that displays banner ads. A minimum implementation to get an ad from within a
UIViewController class is:

<br />

```
  // Create and setup the ad view, specifying the size and origin at {0, 0}.
  GADBannerView *adView = [[GADBannerView alloc] initWithAdSize:kGADAdSizeBanner];
  adView.rootViewController = self;
  adView.adUnitID = @ID created when registering your app;
  // Place the ad view onto the screen.
  [self.view addSubview:adView];
  // Request an ad without any additional targeting information.
  [adView loadRequest:[GADRequest request]];
  
```

<br />

[## Initialization](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/Initialization)

- `
  ``
  ``
  `

  ### [init(adSize:origin:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/c:objc(cs)GADBannerView(im)initWithAdSize:origin:)

  `
  `  
  Initializes and returns a banner view with the specified ad size and origin relative to the
  banner's superview.  

  #### Declaration

  Swift  

      init(adSize: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize.html, origin: CGPoint)

- `
  ``
  ``
  `

  ### [init(adSize:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/c:objc(cs)GADBannerView(im)initWithAdSize:)

  `
  `  
  Initializes and returns a banner view with the specified ad size placed at its superview's
  origin.  

  #### Declaration

  Swift  

      init(adSize: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize.html)

[## Pre-Request](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/Pre-Request)

- `
  ``
  ``
  `

  ### [adUnitID](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/c:objc(cs)GADBannerView(py)adUnitID)

  `
  `  
  Required value created on the AdMob website. Create a new ad unit for every unique placement of
  an ad in your application. Set this to the ID assigned for this placement. Ad units are
  important for targeting and statistics.

  Example AdMob ad unit ID: @ca-app-pub-0123456789012345/0123456789  

  #### Declaration

  Swift  

      var adUnitID: String? { get set }

- `
  ``
  ``
  `

  ### [rootViewController](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/c:objc(cs)GADBannerView(py)rootViewController)

  `
  `  
  Required reference to a root view controller that is used by the banner to present full screen
  content after the user interacts with the ad. The root view controller is most commonly the view
  controller displaying the banner.  

  #### Declaration

  Swift  

      @IBOutlet weak var rootViewController: UIViewController? { get set }

- `
  ``
  ``
  `

  ### [adSize](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/c:objc(cs)GADBannerView(py)adSize)

  `
  `  
  Required to set this banner view to a proper size. Never create your own GADAdSize directly.
  Use one of the predefined standard ad sizes (such as kGADAdSizeBanner), or create one using the
  GADAdSizeFromCGSize method. If not using mediation, then changing the adSize after an ad has
  been shown will cause a new request (for an ad of the new size) to be sent. If using mediation,
  then a new request may not be sent.  

  #### Declaration

  Swift  

      var adSize: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize.html { get set }

- `
  ``
  ``
  `

  ### [delegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/c:objc(cs)GADBannerView(py)delegate)

  `
  `  
  Optional delegate object that receives state change notifications from this GADBannerView.
  Typically this is a UIViewController.  

  #### Declaration

  Swift  

      @IBOutlet weak var delegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADBannerViewDelegate.html? { get set }

- `
  ``
  ``
  `

  ### [adSizeDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/c:objc(cs)GADBannerView(py)adSizeDelegate)

  `
  `  
  Optional delegate that is notified when creatives cause the banner to change size.  

  #### Declaration

  Swift  

      @IBOutlet weak var adSizeDelegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdSizeDelegate.html? { get set }

[## Making an Ad Request](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/Making%20an%20Ad%20Request)

- `
  ``
  ``
  `

  ### [load(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/c:objc(cs)GADBannerView(im)loadRequest:)

  `
  `  
  Requests an ad. The request object supplies targeting information.  

  #### Declaration

  Swift  

      func load(_ request: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest.html?)

- `
  ``
  ``
  `

  ### [isAutoloadEnabled](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/c:objc(cs)GADBannerView(py)autoloadEnabled)

  `
  `  
  A Boolean value that determines whether autoloading of ads in the receiver is enabled. If
  enabled, you do not need to call the loadRequest: method to load ads.  

  #### Declaration

  Swift  

      var isAutoloadEnabled: Bool { get set }

[## Mediation](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/Mediation)

- `
  ``
  ``
  `

  ### [adNetworkClassName](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/c:objc(cs)GADBannerView(py)adNetworkClassName)

  `
  `  
  The ad network class name that fetched the current ad. Returns nil while the latest ad request
  is in progress or if the latest ad request failed. For both standard and mediated Google AdMob
  ads, this property returns @GADMAdapterGoogleAdMobAds. For ads fetched via mediation custom
  events, this property returns @GADMAdapterCustomEvents.  

  #### Declaration

  Swift  

      var adNetworkClassName: String? { get }

[## Deprecated](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/Deprecated)

- `
  ``
  ``
  `

  ### [hasAutoRefreshed](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/c:objc(cs)GADBannerView(py)hasAutoRefreshed)

  `
  `  
  Indicates whether the currently displayed ad (or most recent failure) was a result of auto
  refreshing as specified on server. This property is set to NO after each loadRequest: method.  

  #### Declaration

  Swift  

      var hasAutoRefreshed: Bool { get }

- `
  ``
  ``
  `

  ### [inAppPurchaseDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/c:objc(cs)GADBannerView(py)inAppPurchaseDelegate)

  `
  `  
  Deprecated delegate. GADInAppPurchase is deprecated.  

  #### Declaration

  Swift  

      @IBOutlet weak var inAppPurchaseDelegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInAppPurchaseDelegate.html? { get set }

- `
  ``
  ``
  `

  ### [mediatedAdView](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView#/c:objc(cs)GADBannerView(py)mediatedAdView)

  `
  `  
  The mediated ad network's underlying ad view. You may use this property to read the ad's actual
  size and adjust this banner view's frame origin. However, modifying the banner view's frame size
  triggers the Mobile Ads SDK to request a new ad. Only update the banner view's frame origin.  

  #### Declaration

  Swift  

      weak var mediatedAdView: UIView? { get }