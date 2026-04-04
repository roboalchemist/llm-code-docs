# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage.md.txt

# GoogleMobileAds Framework Reference

# GADNativeAdImage

    class GADNativeAdImage : NSObject

Native ad image.
- `
  ``
  ``
  `

  ### [image](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage#/c:objc(cs)GADNativeAdImage(py)image)

  `
  `  
  The image. If image autoloading is disabled, this property will be nil.  

  #### Declaration

  Swift  

      var image: UIImage? { get }

- `
  ``
  ``
  `

  ### [imageURL](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage#/c:objc(cs)GADNativeAdImage(py)imageURL)

  `
  `  
  The image's URL.  

  #### Declaration

  Swift  

      var imageURL: URL? { get }

- `
  ``
  ``
  `

  ### [scale](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage#/c:objc(cs)GADNativeAdImage(py)scale)

  `
  `  
  The image's scale.  

  #### Declaration

  Swift  

      var scale: CGFloat { get }

[## MediationAdditions](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage#/MediationAdditions)

- `
  ``
  ``
  `

  ### [init(image:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage#/c:objc(cs)GADNativeAdImage(im)initWithImage:)

  `
  `  
  Initializes and returns a native ad image object with the provided image.  

  #### Declaration

  Swift  

      init(image: UIImage)

- `
  ``
  ``
  `

  ### [init(url:scale:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAdImage#/c:objc(cs)GADNativeAdImage(im)initWithURL:scale:)

  `
  `  
  Initializes and returns a native ad image object with the provided image URL and image scale.  

  #### Declaration

  Swift  

      init(url URL: URL, scale: CGFloat)