# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.md.txt

# GoogleMobileAds Framework Reference

# GADNativeAdImage

    @interface GADNativeAdImage : NSObject

Native ad image.
- `


  ### [image](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage#/c:objc(cs)GADNativeAdImage(py)image)


  ` The image. If image autoloading is disabled, this property will be nil.

  #### Declaration

  Objective-C

      @property (readonly, strong, nonatomic, nullable) UIImage *image;

- `


  ### [imageURL](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage#/c:objc(cs)GADNativeAdImage(py)imageURL)


  ` The image's URL.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSURL *imageURL;

- `


  ### [scale](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage#/c:objc(cs)GADNativeAdImage(py)scale)


  ` The image's scale.

  #### Declaration

  Objective-C

      @property (readonly, assign, nonatomic) CGFloat scale;

[## MediationAdditions](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage#/MediationAdditions)

- `


  ### [-initWithImage:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage#/c:objc(cs)GADNativeAdImage(im)initWithImage:)


  ` Initializes and returns a native ad image object with the provided image.

  #### Declaration

  Objective-C

      - (nonnull instancetype)initWithImage:(nonnull UIImage *)image;

- `


  ### [-initWithURL:scale:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage#/c:objc(cs)GADNativeAdImage(im)initWithURL:scale:)


  ` Initializes and returns a native ad image object with the provided image URL and image scale.

  #### Declaration

  Objective-C

      - (nonnull instancetype)initWithURL:(nonnull NSURL *)URL scale:(CGFloat)scale;