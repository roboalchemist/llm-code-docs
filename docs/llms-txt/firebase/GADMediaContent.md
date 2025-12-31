# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaContent.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediaContent.md.txt

# GoogleMobileAds Framework Reference

# GADMediaContent

    class GADMediaContent : NSObject

Provides media content information. Interact with instances of this class on the main queue
only.
- `
  ``
  ``
  `

  ### [aspectRatio](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediaContent#/c:objc(cs)GADMediaContent(py)aspectRatio)

  `
  `  
  Media content aspect ratio (width/height). The value is 0 when there's no media content or the
  media content aspect ratio is unknown.  

  #### Declaration

  Swift  

      var aspectRatio: CGFloat { get }

- `
  ``
  ``
  `

  ### [mainImage](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediaContent#/c:objc(cs)GADMediaContent(py)mainImage)

  `
  `  
  The main image to be displayed when the media content doesn't contain video.  

  #### Declaration

  Swift  

      var mainImage: UIImage? { get set }