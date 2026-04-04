# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingModalDisplay.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingModalDisplay.md.txt

# FirebaseInAppMessaging Framework Reference

# InAppMessagingModalDisplay

    class InAppMessagingModalDisplay : https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage.html

Class for defining a modal message for display.
This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [title](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)title)

  `
  `  
  Gets the title for a modal fiam message.  

  #### Declaration

  Swift  

      var title: String { get }

- `
  ``
  ``
  `

  ### [imageData](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)imageData)

  `
  `  
  Gets the image data for a modal fiam message.  

  #### Declaration

  Swift  

      @NSCopying var imageData: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData.html? { get }

- `
  ``
  ``
  `

  ### [bodyText](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)bodyText)

  `
  `  
  Gets the body text for a modal fiam message.  

  #### Declaration

  Swift  

      var bodyText: String? { get }

- `
  ``
  ``
  `

  ### [actionButton](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)actionButton)

  `
  `  
  Gets the action button metadata for a modal fiam message.  

  #### Declaration

  Swift  

      var actionButton: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton.html? { get }

- `
  ``
  ``
  `

  ### [actionURL](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)actionURL)

  `
  `  
  Gets the action URL for a modal fiam message.  

  #### Declaration

  Swift  

      var actionURL: URL? { get }

- `
  ``
  ``
  `

  ### [displayBackgroundColor](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)displayBackgroundColor)

  `
  `  
  Gets the background color for a modal fiam message.  

  #### Declaration

  Swift  

      @NSCopying var displayBackgroundColor: UIColor { get }

- `
  ``
  ``
  `

  ### [textColor](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)textColor)

  `
  `  
  Gets the color for text in modal fiam message. It would apply to both title and body text.  

  #### Declaration

  Swift  

      @NSCopying var textColor: UIColor { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(im)init)

  `
  `  
  Unavailable  
  Unavailable.
- `
  ``
  ``
  `

  ### [init(campaignName:titleText:bodyText:textColor:backgroundColor:imageData:actionButton:actionURL:appData:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(im)initWithCampaignName:titleText:bodyText:textColor:backgroundColor:imageData:actionButton:actionURL:appData:)

  `
  `  
  Exposed for unit testing only, or for use in SwiftUI previews. Don't instantiate this in your
  app directly.  

  #### Declaration

  Swift  

      init(campaignName: String, titleText title: String, bodyText: String?, textColor: UIColor, backgroundColor: UIColor, imageData: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData.html?, actionButton: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton.html?, actionURL: URL?, appData: [AnyHashable : Any]?)