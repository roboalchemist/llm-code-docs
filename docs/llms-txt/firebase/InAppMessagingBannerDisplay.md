# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingBannerDisplay.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingBannerDisplay.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# InAppMessagingBannerDisplay

    class InAppMessagingBannerDisplay : https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage.html

Class for defining a banner message for display.
- `
  ``
  ``
  `

  ### [title](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)title)

  `
  `  
  Gets the title of a banner message.  

  #### Declaration

  Swift  

      var title: String { get }

- `
  ``
  ``
  `

  ### [imageData](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)imageData)

  `
  `  
  Gets the image data for a banner message.  

  #### Declaration

  Swift  

      @NSCopying var imageData: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingImageData.html? { get }

- `
  ``
  ``
  `

  ### [bodyText](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)bodyText)

  `
  `  
  Gets the body text for a banner message.  

  #### Declaration

  Swift  

      var bodyText: String? { get }

- `
  ``
  ``
  `

  ### [displayBackgroundColor](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)displayBackgroundColor)

  `
  `  
  Gets banner's background color  

  #### Declaration

  Swift  

      @NSCopying var displayBackgroundColor: UIColor { get }

- `
  ``
  ``
  `

  ### [textColor](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)textColor)

  `
  `  
  Gets the color for text in banner fiam message. It would apply to both title and body text.  

  #### Declaration

  Swift  

      @NSCopying var textColor: UIColor { get set }

- `
  ``
  ``
  `

  ### [actionURL](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)actionURL)

  `
  `  
  Gets the action URL for a banner fiam message.  

  #### Declaration

  Swift  

      var actionURL: URL? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(im)init)

  `
  `  
  Unavailable.
- `
  ``
  ``
  `

  ### [init(messageID:campaignName:renderAsTestMessage:triggerType:titleText:bodyText:textColor:backgroundColor:imageData:actionURL:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(im)initWithMessageID:campaignName:renderAsTestMessage:triggerType:titleText:bodyText:textColor:backgroundColor:imageData:actionURL:)

  `
  `  
  Deprecated, this class shouldn't be directly instantiated.  

  #### Declaration

  Swift  

      init(messageID: String, campaignName: String, renderAsTestMessage: Bool, triggerType: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDisplayTriggerType.html, titleText title: String, bodyText: String, textColor: UIColor, backgroundColor: UIColor, imageData: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingImageData.html?, actionURL: URL?)