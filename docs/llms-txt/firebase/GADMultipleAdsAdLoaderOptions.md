# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMultipleAdsAdLoaderOptions.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMultipleAdsAdLoaderOptions.md.txt

# GoogleMobileAds Framework Reference

# GADMultipleAdsAdLoaderOptions

    class GADMultipleAdsAdLoaderOptions : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdLoaderOptions

Ad loader options for requesting multiple ads. Requesting multiple ads in a single request is
currently only available for native app install ads and native content ads.
- `
  ``
  ``
  `

  ### [numberOfAds](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMultipleAdsAdLoaderOptions#/c:objc(cs)GADMultipleAdsAdLoaderOptions(py)numberOfAds)

  `
  `  
  Number of ads the GADAdLoader should attempt to return for the request. By default, numberOfAds
  is one. Requests are invalid and will fail if numberOfAds is less than one. If numberOfAds
  exceeds the maximum limit (5), only the maximum number of ads are requested.

  The ad loader makes at least one and up to numberOfAds calls to the ad received and
  -didFailToReceiveAdWithError: methods found in GADAdLoaderDelegate and its extensions, followed
  by a single call to -adLoaderDidFinishLoading: once loading is finished.  

  #### Declaration

  Swift  

      var numberOfAds: Int { get set }