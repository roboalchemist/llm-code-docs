# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingBannerDisplay.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# FIRInAppMessagingBannerDisplay


    @interface FIRInAppMessagingBannerDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage.html

Class for defining a banner message for display.
- `


  ### [title](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)title)


  ` Gets the title of a banner message.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull) NSString *title;

- `


  ### [imageData](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)imageData)


  ` Gets the image data for a banner message.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable)
          https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageData.html *imageData;

- `


  ### [bodyText](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)bodyText)


  ` Gets the body text for a banner message.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *bodyText;

- `


  ### [displayBackgroundColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)displayBackgroundColor)


  ` Gets banner's background color

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull) UIColor *displayBackgroundColor;

- `


  ### [textColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)textColor)


  ` Gets the color for text in banner fiam message. It would apply to both title and body text.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nonnull) UIColor *textColor;

- `


  ### [actionURL](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(py)actionURL)


  ` Gets the action URL for a banner fiam message.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nullable) NSURL *actionURL;

- `


  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(im)init)


  ` Unavailable.

  #### Declaration

  Objective-C

      - (nonnull instancetype)init;

- `


  ### [-initWithMessageID:campaignName:renderAsTestMessage:triggerType:titleText:bodyText:textColor:backgroundColor:imageData:actionURL:](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingBannerDisplay#/c:objc(cs)FIRInAppMessagingBannerDisplay(im)initWithMessageID:campaignName:renderAsTestMessage:triggerType:titleText:bodyText:textColor:backgroundColor:imageData:actionURL:)


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
                    actionURL:(nullable NSURL *)actionURL;