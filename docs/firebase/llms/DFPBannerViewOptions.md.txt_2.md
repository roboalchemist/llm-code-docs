# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerViewOptions.md.txt

# GoogleMobileAds Framework Reference

# DFPBannerViewOptions

    @interface DFPBannerViewOptions : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdLoaderOptions

Ad loader options for banner ads.
- `


  ### [appEventDelegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerViewOptions#/c:objc(cs)DFPBannerViewOptions(py)appEventDelegate)


  ` Optional delegate that is notified if the loaded banner sends app events.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAppEventDelegate.html>
          appEventDelegate;

- `


  ### [adSizeDelegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerViewOptions#/c:objc(cs)DFPBannerViewOptions(py)adSizeDelegate)


  ` Optional delegate that is notified if the loaded banner changes size.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdSizeDelegate.html> adSizeDelegate;

- `


  ### [enableManualImpressions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerViewOptions#/c:objc(cs)DFPBannerViewOptions(py)enableManualImpressions)


  ` Whether the publisher will record impressions manually when the ad becomes visible to the user.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL enableManualImpressions;