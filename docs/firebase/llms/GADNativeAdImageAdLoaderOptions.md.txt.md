# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImageAdLoaderOptions.md.txt

# GoogleMobileAds Framework Reference

# GADNativeAdImageAdLoaderOptions

    @interface GADNativeAdImageAdLoaderOptions : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdLoaderOptions

Ad loader options for native ad image settings.
- `


  ### [disableImageLoading](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImageAdLoaderOptions#/c:objc(cs)GADNativeAdImageAdLoaderOptions(py)disableImageLoading)


  ` Indicates whether image asset content should be loaded by the SDK. If set to YES, the SDK will
  not load image asset content and native ad image URLs can be used to fetch content. Defaults to
  NO, image assets are loaded by the SDK.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL disableImageLoading;

- `


  ### [shouldRequestMultipleImages](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImageAdLoaderOptions#/c:objc(cs)GADNativeAdImageAdLoaderOptions(py)shouldRequestMultipleImages)


  ` Indicates whether multiple images should be loaded for each asset. Defaults to NO.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL shouldRequestMultipleImages;

- `


  ### [preferredImageOrientation](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImageAdLoaderOptions#/c:objc(cs)GADNativeAdImageAdLoaderOptions(py)preferredImageOrientation)


  ` Indicates preferred image orientation. Defaults to
  GADNativeAdImageAdLoaderOptionsOrientationAny.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADNativeAdImageAdLoaderOptionsOrientation.html preferredImageOrientation;