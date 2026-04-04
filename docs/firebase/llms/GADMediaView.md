# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediaView.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaView.md.txt

# GoogleMobileAds Framework Reference

# GADMediaView

    @interface GADMediaView : UIView

Displays native ad media content.

To display media content in GADUnifiedNativeAdView instances, add a GADMediaView subview,
assign the native ad view's mediaView property, and set the native ad's mediaContent property to
the media view.

If the native ad contains video content, the media view displays the video content.

If the native ad doesn't have video content and image loading is enabled, the media view
displays the first image from the native ad's \|images\| property.

If the native ad doesn't have video content and image loading is disabled, the media view is
empty.
- `
  ``
  ``
  `

  ### [mediaContent](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaView#/c:objc(cs)GADMediaView(py)mediaContent)

  `
  `  
  The media content displayed in the media view.  

  #### Declaration

  Objective-C  

      @property (assign, readwrite, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaContent.html *mediaContent;