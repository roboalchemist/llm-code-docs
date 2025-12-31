# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingModalDisplay.md.txt

# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingModalDisplay.md.txt

# FirebaseInAppMessaging Framework Reference

# FIRInAppMessagingModalDisplay


    @interface FIRInAppMessagingModalDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage.html

Class for defining a modal message for display.
This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [title](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)title)

  `
  `  
  Gets the title for a modal fiam message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) NSString *title;

- `
  ``
  ``
  `

  ### [imageData](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)imageData)

  `
  `  
  Gets the image data for a modal fiam message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData.html *imageData;

- `
  ``
  ``
  `

  ### [bodyText](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)bodyText)

  `
  `  
  Gets the body text for a modal fiam message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *bodyText;

- `
  ``
  ``
  `

  ### [actionButton](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)actionButton)

  `
  `  
  Gets the action button metadata for a modal fiam message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingActionButton.html *actionButton;

- `
  ``
  ``
  `

  ### [actionURL](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)actionURL)

  `
  `  
  Gets the action URL for a modal fiam message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSURL *actionURL;

- `
  ``
  ``
  `

  ### [displayBackgroundColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)displayBackgroundColor)

  `
  `  
  Gets the background color for a modal fiam message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) UIColor *displayBackgroundColor;

- `
  ``
  ``
  `

  ### [textColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)textColor)

  `
  `  
  Gets the color for text in modal fiam message. It would apply to both title and body text.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) UIColor *textColor;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(im)init)

  `
  `  
  Unavailable  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-initWithCampaignName:titleText:bodyText:textColor:backgroundColor:imageData:actionButton:actionURL:appData:](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(im)initWithCampaignName:titleText:bodyText:textColor:backgroundColor:imageData:actionButton:actionURL:appData:)

  `
  `  
  Exposed for unit testing only, or for use in SwiftUI previews. Don't instantiate this in your
  app directly.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)
          initWithCampaignName:(nonnull NSString *)campaignName
                     titleText:(nonnull NSString *)title
                      bodyText:(nullable NSString *)bodyText
                     textColor:(nonnull UIColor *)textColor
               backgroundColor:(nonnull UIColor *)backgroundColor
                     imageData:(nullable https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData.html *)imageData
                  actionButton:(nullable https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingActionButton.html *)actionButton
                     actionURL:(nullable NSURL *)actionURL
                       appData:(nullable NSDictionary *)appData;