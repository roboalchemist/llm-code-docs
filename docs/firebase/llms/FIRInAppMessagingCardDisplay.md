# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay.md.txt

# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay.md.txt

# FirebaseInAppMessaging Framework Reference

# FIRInAppMessagingCardDisplay


    @interface FIRInAppMessagingCardDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage.html

A displayable in-app card message.
This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [title](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)title)

  `
  `  
  Gets the title text for a card FIAM message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) NSString *title;

- `
  ``
  ``
  `

  ### [body](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)body)

  `
  `  
  Gets the body text for a card FIAM message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *body;

- `
  ``
  ``
  `

  ### [textColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)textColor)

  `
  `  
  Gets the color for text in card FIAM message. It applies to both title and body text.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) UIColor *textColor;

- `
  ``
  ``
  `

  ### [portraitImageData](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)portraitImageData)

  `
  `  
  Image data for the supplied portrait image for a card FIAM messasge.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData.html *portraitImageData;

- `
  ``
  ``
  `

  ### [landscapeImageData](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)landscapeImageData)

  `
  `  
  Image data for the supplied landscape image for a card FIAM message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData.html *landscapeImageData;

- `
  ``
  ``
  `

  ### [displayBackgroundColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)displayBackgroundColor)

  `
  `  
  The background color for a card FIAM message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) UIColor *displayBackgroundColor;

- `
  ``
  ``
  `

  ### [primaryActionButton](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)primaryActionButton)

  `
  `  
  Metadata for a card FIAM message's primary action button.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nonnull) https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingActionButton.html *primaryActionButton;

- `
  ``
  ``
  `

  ### [primaryActionURL](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)primaryActionURL)

  `
  `  
  The action URL for a card FIAM message's primary action button.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSURL *primaryActionURL;

- `
  ``
  ``
  `

  ### [secondaryActionButton](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)secondaryActionButton)

  `
  `  
  Metadata for a card FIAM message's secondary action button.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingActionButton.html *secondaryActionButton;

- `
  ``
  ``
  `

  ### [secondaryActionURL](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)secondaryActionURL)

  `
  `  
  The action URL for a card FIAM message's secondary action button.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSURL *secondaryActionURL;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(im)init)

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

  ### [-initWithCampaignName:titleText:bodyText:textColor:portraitImageData:landscapeImageData:backgroundColor:primaryActionButton:secondaryActionButton:primaryActionURL:secondaryActionURL:appData:](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(im)initWithCampaignName:titleText:bodyText:textColor:portraitImageData:landscapeImageData:backgroundColor:primaryActionButton:secondaryActionButton:primaryActionURL:secondaryActionURL:appData:)

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
              portraitImageData:
                  (nonnull https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData.html *)portraitImageData
             landscapeImageData:
                 (nullable https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData.html *)landscapeImageData
                backgroundColor:(nonnull UIColor *)backgroundColor
            primaryActionButton:
                (nonnull https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingActionButton.html *)primaryActionButton
          secondaryActionButton:
              (nullable https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingActionButton.html *)secondaryActionButton
               primaryActionURL:(nullable NSURL *)primaryActionURL
             secondaryActionURL:(nullable NSURL *)secondaryActionURL
                        appData:(nullable NSDictionary *)appData;