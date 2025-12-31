# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchBannerView.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchBannerView.md.txt

# GoogleMobileAds Framework Reference

# GADSearchBannerView

    class GADSearchBannerView : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADBannerView.html

A view that displays search ads.
To show search ads:
1) Create a GADSearchBannerView and add it to your view controller's view hierarchy.
2) Create a GADSearchRequest ad request object to hold the search query and other search data.
3) Call GADSearchBannerView's -loadRequest: method with the GADSearchRequest object.
- `
  ``
  ``
  `

  ### [adSizeDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchBannerView#/c:objc(cs)GADSearchBannerView(py)adSizeDelegate)

  `
  `  
  If the banner view is initialized with kGADAdSizeFluid and the corresponding request is created
  with dynamic height parameters, this delegate will be called when the ad size changes.  

  #### Declaration

  Swift  

      @IBOutlet weak var adSizeDelegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdSizeDelegate.html? { get set }