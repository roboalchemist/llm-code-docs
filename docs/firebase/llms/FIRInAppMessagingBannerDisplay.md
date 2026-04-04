# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingBannerDisplay.md.txt

# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingBannerDisplay.md.txt

# FirebaseInAppMessaging Framework Reference

# FIRInAppMessagingBannerDisplay


    @interface FIRInAppMessagingBannerDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage.html

Class for defining a banner message for display.
This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [title](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)title)

  `
  `  
  Gets the title of a banner message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) NSString *title;

- `
  ``
  ``
  `

  ### [imageData](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)imageData)

  `
  `  
  Gets the image data for a banner message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData.html *imageData;

- `
  ``
  ``
  `

  ### [bodyText](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)bodyText)

  `
  `  
  Gets the body text for a banner message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *bodyText;

- `
  ``
  ``
  `

  ### [displayBackgroundColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)displayBackgroundColor)

  `
  `  
  Gets banner's background color  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) UIColor *displayBackgroundColor;

- `
  ``
  ``
  `

  ### [textColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)textColor)

  `
  `  
  Gets the color for text in banner fiam message. It would apply to both title and body text.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) UIColor *textColor;

- `
  ``
  ``
  `

  ### [actionURL](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)actionURL)

  `
  `  
  Gets the action URL for a banner fiam message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSURL *actionURL;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(im)init)

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

  ### [-initWithCampaignName:titleText:bodyText:textColor:backgroundColor:imageData:actionURL:appData:](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(im)initWithCampaignName:titleText:bodyText:textColor:backgroundColor:imageData:actionURL:appData:)

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
                     actionURL:(nullable NSURL *)actionURL
                       appData:(nullable NSDictionary *)appData;