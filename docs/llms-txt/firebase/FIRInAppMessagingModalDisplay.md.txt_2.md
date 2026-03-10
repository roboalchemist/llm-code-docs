# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingModalDisplay.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# FIRInAppMessagingModalDisplay


    @interface FIRInAppMessagingModalDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage.html

Class for defining a modal message for display.
- `


  ### [title](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)title)


  ` Gets the title for a modal fiam message.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull) NSString *title;

- `


  ### [imageData](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)imageData)


  ` Gets the image data for a modal fiam message.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable)
          https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageData.html *imageData;

- `


  ### [bodyText](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)bodyText)


  ` Gets the body text for a modal fiam message.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *bodyText;

- `


  ### [actionButton](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)actionButton)


  ` Gets the action button metadata for a modal fiam message.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nullable)
          https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingActionButton.html *actionButton;

- `


  ### [actionURL](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)actionURL)


  ` Gets the action URL for a modal fiam message.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nullable) NSURL *actionURL;

- `


  ### [displayBackgroundColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)displayBackgroundColor)


  ` Gets the background color for a modal fiam message.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nonnull) UIColor *displayBackgroundColor;

- `


  ### [textColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(py)textColor)


  ` Gets the color for text in modal fiam message. It would apply to both title and body text.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nonnull) UIColor *textColor;

- `


  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(im)init)


  ` Unavailable.

  #### Declaration

  Objective-C

      - (nonnull instancetype)init;

- `


  ### [-initWithMessageID:campaignName:renderAsTestMessage:triggerType:titleText:bodyText:textColor:backgroundColor:imageData:actionButton:actionURL:](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingModalDisplay#/c:objc(cs)FIRInAppMessagingModalDisplay(im)initWithMessageID:campaignName:renderAsTestMessage:triggerType:titleText:bodyText:textColor:backgroundColor:imageData:actionButton:actionURL:)


  ` Deprecated, this class shouldn't be directly instantiated.

  #### Declaration

  Objective-C

      - (nonnull instancetype)
            initWithMessageID:(nonnull NSString *)messageID
                 campaignName:(nonnull NSString *)campaignName
          renderAsTestMessage:(BOOL)renderAsTestMessage
                  triggerType:(https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDisplayTriggerType.html)triggerType
                    titleText:(nonnull NSString *)title
                     bodyText:(nonnull NSString *)bodyText
                    textColor:(nonnull UIColor *)textColor
              backgroundColor:(nonnull UIColor *)backgroundColor
                    imageData:(nullable https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageData.html *)imageData
                 actionButton:(nullable https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingActionButton.html *)actionButton
                    actionURL:(nullable NSURL *)actionURL;