# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeExpressAdView.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView.md.txt

# GoogleMobileAds Framework Reference

# GADNativeExpressAdView

    class GADNativeExpressAdView : UIView

The view that displays native ads. A minimum implementation to get an ad from within a
UIViewController class is:

<br />

```
  // Create and setup the ad view, specifying the size and origin at {0, 0}.
  GADNativeExpressAdView *adView =
      [[GADNativeExpressAdView alloc] initWithAdSize:kGADAdSizeBanner];
  adView.rootViewController = self;
  adView.adUnitID = @ID created when registering your app;
  // Place the ad view onto the screen.
  [self.view addSubview:adView];
  // Request an ad without any additional targeting information.
  [adView loadRequest:[GADRequest request]];
  
```

<br />

[## Initialization](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/Initialization)

- `
  ``
  ``
  `

  ### [init(adSize:origin:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/c:objc(cs)GADNativeExpressAdView(im)initWithAdSize:origin:)

  `
  `  
  Returns an initialized GADNativeExpressAdView instance set to \|adSize\| and positioned at
  \|origin\| relative to its superview bounds. Returns nil if \|adSize\| is an invalid ad size.  

  #### Declaration

  Swift  

      init?(adSize: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize.html, origin: CGPoint)

- `
  ``
  ``
  `

  ### [init(adSize:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/c:objc(cs)GADNativeExpressAdView(im)initWithAdSize:)

  `
  `  
  Returns an initialized GADNativeExpressAdView instance set to \|adSize\| and positioned at the
  top left of its superview. Returns nil if \|adSize\| is an invalid ad size.  

  #### Declaration

  Swift  

      init?(adSize: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize.html)

- `
  ``
  ``
  `

  ### [videoController](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/c:objc(cs)GADNativeExpressAdView(py)videoController)

  `
  `  
  Video controller for controlling video rendered by this native express ad view.  

  #### Declaration

  Swift  

      var videoController: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController.html { get }

[## Pre-Request](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/Pre-Request)

- `
  ``
  ``
  `

  ### [adUnitID](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/c:objc(cs)GADNativeExpressAdView(py)adUnitID)

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

  ### [rootViewController](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/c:objc(cs)GADNativeExpressAdView(py)rootViewController)

  `
  `  
  Required reference to the current root view controller. For example, the root view controller in
  a tab-based application would be the UITabViewController.  

  #### Declaration

  Swift  

      @IBOutlet weak var rootViewController: UIViewController? { get set }

- `
  ``
  ``
  `

  ### [adSize](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/c:objc(cs)GADNativeExpressAdView(py)adSize)

  `
  `  
  Required to set this native ad view to a proper size. Never create your own GADAdSize directly.
  Use one of the predefined standard ad sizes (such as kGADAdSizeBanner), or create one using the
  GADAdSizeFromCGSize method. If you are not using mediation, changing the adSize after an ad has
  been shown will cause a new request (for an ad of the new size) to be sent. If you are using
  mediation, then a new request may not be sent.  

  #### Declaration

  Swift  

      var adSize: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Structs/GADAdSize.html { get set }

- `
  ``
  ``
  `

  ### [delegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/c:objc(cs)GADNativeExpressAdView(py)delegate)

  `
  `  
  Optional delegate object that receives state change notifications from this
  GADNativeExpressAdView. Typically this is a UIViewController.  

  #### Declaration

  Swift  

      @IBOutlet weak var delegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate.html? { get set }

- `
  ``
  ``
  `

  ### [isAutoloadEnabled](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/c:objc(cs)GADNativeExpressAdView(py)autoloadEnabled)

  `
  `  
  A Boolean value that determines whether autoloading of ads in the receiver is enabled. If
  enabled, you do not need to call the loadRequest: method to load ads.  

  #### Declaration

  Swift  

      var isAutoloadEnabled: Bool { get set }

- `
  ``
  ``
  `

  ### [setAdOptions(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/c:objc(cs)GADNativeExpressAdView(im)setAdOptions:)

  `
  `  
  Sets options that configure ad loading.  

  #### Declaration

  Swift  

      func setAdOptions(_ adOptions: [Any])

  #### Parameters

  |-------------------|-----------------------------------------------------------------------------------------------------------------------------------|
  | ` `*adOptions*` ` | An array of GADAdLoaderOptions objects. The array is deep copied and option objects cannot be modified after calling this method. |

[## Making an Ad Request](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/Making%20an%20Ad%20Request)

- `
  ``
  ``
  `

  ### [load(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/c:objc(cs)GADNativeExpressAdView(im)loadRequest:)

  `
  `  
  Makes an ad request. The request object supplies targeting information.  

  #### Declaration

  Swift  

      func load(_ request: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest.html?)

[## Mediation](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/Mediation)

- `
  ``
  ``
  `

  ### [adNetworkClassName](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeExpressAdView#/c:objc(cs)GADNativeExpressAdView(py)adNetworkClassName)

  `
  `  
  The name of the ad network adapter class that fetched the current ad. Returns nil while the
  latest ad request is in progress or if the latest ad request failed. For both standard and
  mediated Google AdMob ads, this method returns @GADMAdapterGoogleAdMobAds. For ads fetched
  via mediation custom events, this method returns @GADMAdapterCustomEvents.  

  #### Declaration

  Swift  

      weak var adNetworkClassName: NSString? { get }