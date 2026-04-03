# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImageAdLoaderOptions.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImageAdLoaderOptions.md.txt

# GoogleMobileAds Framework Reference

# GADNativeAdImageAdLoaderOptions

    class GADNativeAdImageAdLoaderOptions : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdLoaderOptions

Ad loader options for native ad image settings.
- `
  ``
  ``
  `

  ### [disableImageLoading](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImageAdLoaderOptions#/c:objc(cs)GADNativeAdImageAdLoaderOptions(py)disableImageLoading)

  `
  `  
  Indicates whether image asset content should be loaded by the SDK. If set to YES, the SDK will
  not load image asset content and native ad image URLs can be used to fetch content. Defaults to
  NO, image assets are loaded by the SDK.  

  #### Declaration

  Swift  

      var disableImageLoading: Bool { get set }

- `
  ``
  ``
  `

  ### [shouldRequestMultipleImages](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImageAdLoaderOptions#/c:objc(cs)GADNativeAdImageAdLoaderOptions(py)shouldRequestMultipleImages)

  `
  `  
  Indicates whether multiple images should be loaded for each asset. Defaults to NO.  

  #### Declaration

  Swift  

      var shouldRequestMultipleImages: Bool { get set }

- `
  ``
  ``
  `

  ### [preferredImageOrientation](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImageAdLoaderOptions#/c:objc(cs)GADNativeAdImageAdLoaderOptions(py)preferredImageOrientation)

  `
  `  
  Indicates preferred image orientation. Defaults to
  GADNativeAdImageAdLoaderOptionsOrientationAny.  

  #### Declaration

  Swift  

      var preferredImageOrientation: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADNativeAdImageAdLoaderOptionsOrientation.html { get set }