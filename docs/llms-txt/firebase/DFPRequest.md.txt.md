# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPRequest.md.txt

# GoogleMobileAds Framework Reference

# DFPRequest

    @interface DFPRequest : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequest.html

Specifies optional parameters for ad requests.
- `


  ### [publisherProvidedID](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPRequest#/c:objc(cs)DFPRequest(py)publisherProvidedID)


  ` Publisher provided user ID.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *publisherProvidedID;

- `


  ### [categoryExclusions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPRequest#/c:objc(cs)DFPRequest(py)categoryExclusions)


  ` Array of strings used to exclude specified categories in ad results.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSArray *categoryExclusions;

- `


  ### [customTargeting](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPRequest#/c:objc(cs)DFPRequest(py)customTargeting)


  ` Key-value pairs used for custom targeting.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSDictionary *customTargeting;

- `


  ### [+updateCorrelator](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPRequest#/c:objc(cs)DFPRequest(cm)updateCorrelator)


  ` This API is deprecated and has no effect. Use an instance of GADCorrelator with DFPInterstitial
  or DFPBannerView objects to correlate requests.

  #### Declaration

  Objective-C

      + (void)updateCorrelator;