# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCorrelatorAdLoaderOptions.md.txt

# GoogleMobileAds Framework Reference

# GADCorrelatorAdLoaderOptions

    @interface GADCorrelatorAdLoaderOptions : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdLoaderOptions

Ad loader options for adding a correlator to a native ad request.
- `


  ### [correlator](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCorrelatorAdLoaderOptions#/c:objc(cs)GADCorrelatorAdLoaderOptions(py)correlator)


  ` Correlator object for correlating ads loaded by an ad loader to other ad objects.

  #### Declaration

  Objective-C

      @property (readwrite, strong, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCorrelator.html *correlator;