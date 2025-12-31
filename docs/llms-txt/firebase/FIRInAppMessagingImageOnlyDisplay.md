# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageOnlyDisplay.md.txt

# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageOnlyDisplay.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# FIRInAppMessagingImageOnlyDisplay


    @interface FIRInAppMessagingImageOnlyDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage.html

Class for defining a image-only message for display.
- `
  ``
  ``
  `

  ### [imageData](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(py)imageData)

  `
  `  
  Gets the image for this message  

  #### Declaration

  Objective-C  

      @property (readonly, copy, nonatomic, nonnull)
          https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageData.html *imageData;

- `
  ``
  ``
  `

  ### [actionURL](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(py)actionURL)

  `
  `  
  Gets the action URL for an image-only fiam message.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic, nullable) NSURL *actionURL;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-initWithMessageID:campaignName:renderAsTestMessage:triggerType:imageData:actionURL:](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(im)initWithMessageID:campaignName:renderAsTestMessage:triggerType:imageData:actionURL:)

  `
  `  
  Deprecated, this class shouldn't be directly instantiated.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)
            initWithMessageID:(nonnull NSString *)messageID
                 campaignName:(nonnull NSString *)campaignName
          renderAsTestMessage:(BOOL)renderAsTestMessage
                  triggerType:(https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDisplayTriggerType.html)triggerType
                    imageData:(nullable https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageData.html *)imageData
                    actionURL:(nullable NSURL *)actionURL;