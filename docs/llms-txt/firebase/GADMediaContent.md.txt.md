# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaContent.md.txt

# GoogleMobileAds Framework Reference

# GADMediaContent

    @interface GADMediaContent : NSObject

Provides media content information. Interact with instances of this class on the main queue
only.
- `


  ### [aspectRatio](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaContent#/c:objc(cs)GADMediaContent(py)aspectRatio)


  ` Media content aspect ratio (width/height). The value is 0 when there's no media content or the
  media content aspect ratio is unknown.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic) CGFloat aspectRatio;

- `


  ### [mainImage](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaContent#/c:objc(cs)GADMediaContent(py)mainImage)


  ` The main image to be displayed when the media content doesn't contain video.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic, nullable) UIImage *mainImage;