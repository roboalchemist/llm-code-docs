# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingImageOnlyDisplay.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageOnlyDisplay.md.txt

# FirebaseInAppMessaging Framework Reference

# InAppMessagingImageOnlyDisplay

    class InAppMessagingImageOnlyDisplay : https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage.html

Class for defining a image-only message for display.
This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [imageData](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(py)imageData)

  `
  `  
  Gets the image for this message  

  #### Declaration

  Swift  

      @NSCopying var imageData: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData.html { get }

- `
  ``
  ``
  `

  ### [actionURL](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(py)actionURL)

  `
  `  
  Gets the action URL for an image-only fiam message.  

  #### Declaration

  Swift  

      var actionURL: URL? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(im)init)

  `
  `  
  Unavailable  
  Unavailable.
- `
  ``
  ``
  `

  ### [init(campaignName:imageData:actionURL:appData:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(im)initWithCampaignName:imageData:actionURL:appData:)

  `
  `  
  Exposed for unit testing only, or for use in SwiftUI previews. Don't instantiate this in your
  app directly.  

  #### Declaration

  Swift  

      init(campaignName: String, imageData: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData.html, actionURL: URL?, appData: [AnyHashable : Any]?)