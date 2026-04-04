# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView.md.txt

# GoogleMobileAds Framework Reference

# DFPBannerView

    @interface DFPBannerView : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADBannerView.html

The view that displays Ad Manager banner ads.

To request this ad type using GADAdLoader, you need to pass kGADAdLoaderAdTypeDFPBanner (see
GADAdLoaderAdTypes.h) to the \|adTypes\| parameter in GADAdLoader's initializer method. If you
request this ad type, your delegate must conform to the DFPBannerAdLoaderDelegate protocol.
- `


  ### [adUnitID](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView#/c:objc(cs)DFPBannerView(py)adUnitID)


  ` Required value created on the Ad Manager website. Create a new ad unit for every unique
  placement of an ad in your application. Set this to the ID assigned for this placement. Ad units
  are important for targeting and statistics.

  Example Ad Manager ad unit ID: @/6499/example/banner

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *adUnitID;

- `


  ### [appEventDelegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView#/c:objc(cs)DFPBannerView(py)appEventDelegate)


  ` Optional delegate that is notified when creatives send app events.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAppEventDelegate.html>
          appEventDelegate;

- `


  ### [adSizeDelegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView#/c:objc(cs)DFPBannerView(py)adSizeDelegate)


  ` Optional delegate that is notified when creatives cause the banner to change size.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdSizeDelegate.html> adSizeDelegate;

- `


  ### [validAdSizes](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView#/c:objc(cs)DFPBannerView(py)validAdSizes)


  ` Optional array of NSValue encoded GADAdSize structs, specifying all valid sizes that are
  appropriate for this slot. Never create your own GADAdSize directly. Use one of the predefined
  standard ad sizes (such as kGADAdSizeBanner), or create one using the GADAdSizeFromCGSize
  method.

  Example:

  <br />

  ```
    NSArray *validSizes = @[
      NSValueFromGADAdSize(kGADAdSizeBanner),
      NSValueFromGADAdSize(kGADAdSizeLargeBanner)
    ];

  bannerView.validAdSizes = validSizes;
    
  ```

  <br />

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable)
          NSArray<NSValue *> *validAdSizes;

- `


  ### [correlator](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView#/c:objc(cs)DFPBannerView(py)correlator)


  ` Correlator object for correlating this object to other ad objects.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCorrelator.html *correlator;

- `


  ### [enableManualImpressions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView#/c:objc(cs)DFPBannerView(py)enableManualImpressions)


  ` Indicates that the publisher will record impressions manually when the ad becomes visible to the
  user.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL enableManualImpressions;

- `


  ### [customRenderedBannerViewDelegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView#/c:objc(cs)DFPBannerView(py)customRenderedBannerViewDelegate)


  ` Optional delegate object for custom rendered ads.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable)
          id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/DFPCustomRenderedBannerViewDelegate.html>
              customRenderedBannerViewDelegate;

- `


  ### [videoController](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView#/c:objc(cs)DFPBannerView(py)videoController)


  ` Video controller for controlling video rendered by this ad view.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nonnull) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController.html *videoController;

- `


  ### [-recordImpression](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView#/c:objc(cs)DFPBannerView(im)recordImpression)


  ` If you've set enableManualImpressions to YES, call this method when the ad is visible.

  #### Declaration

  Objective-C

      - (void)recordImpression;

- `


  ### [-resize:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView#/c:objc(cs)DFPBannerView(im)resize:)


  ` Use this function to resize the banner view without launching a new ad request.

  #### Declaration

  Objective-C

      - (void)resize:(https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize.html)size;

- `


  ### [-setAdOptions:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView#/c:objc(cs)DFPBannerView(im)setAdOptions:)


  ` Sets options that configure ad loading.

  #### Declaration

  Objective-C

      - (void)setAdOptions:(nonnull NSArray<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdLoaderOptions *> *)adOptions;

  #### Parameters

  |---|---|
  | ` adOptions ` | An array of GADAdLoaderOptions objects. The array is deep copied and option objects cannot be modified after calling this method. |

[## Deprecated](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView#/Deprecated)

- `


  ### [-setValidAdSizesWithSizes:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView#/c:objc(cs)DFPBannerView(im)setValidAdSizesWithSizes:)


  ` Deprecated. Use the validAdSizes property.
  Sets the receiver's valid ad sizes to the values pointed to by the provided NULL terminated list
  of GADAdSize pointers.

  Example:

  <br />

  ```
    GADAdSize size1 = kGADAdSizeBanner;
    GADAdSize size2 = kGADAdSizeLargeBanner;
    [bannerView setValidAdSizesWithSizes:&size1, &size2, nil];
    
  ```

  <br />

  #### Declaration

  Objective-C

      - (void)setValidAdSizesWithSizes:(nullable https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize.html *)firstSize, ...;