# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPCustomRenderedAd.md.txt

# GoogleMobileAds Framework Reference

# DFPCustomRenderedAd

    @interface DFPCustomRenderedAd : NSObject

Custom rendered ad. Your application renders the ad.
- `


  ### [adHTML](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPCustomRenderedAd#/c:objc(cs)DFPCustomRenderedAd(py)adHTML)


  ` The ad's HTML.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nonnull) NSString *adHTML;

- `


  ### [adBaseURL](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPCustomRenderedAd#/c:objc(cs)DFPCustomRenderedAd(py)adBaseURL)


  ` The base URL of the ad's HTML.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nonnull) NSURL *adBaseURL;

- `


  ### [-recordClick](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPCustomRenderedAd#/c:objc(cs)DFPCustomRenderedAd(im)recordClick)


  ` Call this method when the user clicks the ad.

  #### Declaration

  Objective-C

      - (void)recordClick;

- `


  ### [-recordImpression](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPCustomRenderedAd#/c:objc(cs)DFPCustomRenderedAd(im)recordImpression)


  ` Call this method when the ad is visible to the user.

  #### Declaration

  Objective-C

      - (void)recordImpression;

- `


  ### [-finishedRenderingAdView:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPCustomRenderedAd#/c:objc(cs)DFPCustomRenderedAd(im)finishedRenderingAdView:)


  ` Call this method after the ad has been rendered in a UIView object.

  #### Declaration

  Objective-C

      - (void)finishedRenderingAdView:(nonnull UIView *)view;