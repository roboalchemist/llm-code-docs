# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingImageData.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData.md.txt

# FirebaseInAppMessaging Framework Reference

# InAppMessagingImageData

    class InAppMessagingImageData : NSObject

Contain display data for an image for a fiam message.

- This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [imageURL](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData#/c:objc(cs)FIRInAppMessagingImageData(py)imageURL)

  `
  `  
  Gets the image URL from image data.  

  #### Declaration

  Swift  

      var imageURL: String { get }

- `
  ``
  ``
  `

  ### [imageRawData](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData#/c:objc(cs)FIRInAppMessagingImageData(py)imageRawData)

  `
  `  
  Gets the downloaded image data. It can be null if headless component fails to load it.  

  #### Declaration

  Swift  

      var imageRawData: Data? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData#/c:objc(cs)FIRInAppMessagingImageData(im)init)

  `
  `  
  Unavailable  
  Unavailable.
- `
  ``
  ``
  `

  ### [init(imageURL:imageData:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData#/c:objc(cs)FIRInAppMessagingImageData(im)initWithImageURL:imageData:)

  `
  `  
  Exposed for unit testing only, or for use in SwiftUI previews. Don't instantiate this in your
  app directly.  

  #### Declaration

  Swift  

      init(imageURL: String, imageData: Data)