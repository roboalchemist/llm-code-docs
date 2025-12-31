# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage.md.txt

# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage.md.txt

# FirebaseInAppMessaging Framework Reference

# FIRInAppMessagingDisplayMessage


    @interface FIRInAppMessagingDisplayMessage : NSObject

Base class representing a FIAM message to be displayed. Don't create instance
of this class directly. Instantiate one of its subclasses instead.
This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [campaignInfo](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)campaignInfo)

  `
  `  
  Metadata for the campaign to which this message belongs.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCampaignInfo.html *campaignInfo;

- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)type)

  `
  `  
  The type and UI style of this message.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Enums/FIRInAppMessagingDisplayMessageType.html type;

- `
  ``
  ``
  `

  ### [triggerType](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)triggerType)

  `
  `  
  How this message should be triggered.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Enums/FIRInAppMessagingDisplayTriggerType.html triggerType;

- `
  ``
  ``
  `

  ### [appData](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)appData)

  `
  `  
  Extra key-value dictionary data that can be sent along with the message  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSDictionary *appData;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(im)init)

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

  ### [-initWithMessageID:campaignName:renderAsTestMessage:messageType:triggerType:](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(im)initWithMessageID:campaignName:renderAsTestMessage:messageType:triggerType:)

  `
  `  
  Exposed for unit testing only. Don't instantiate this in your app directly.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)
            initWithMessageID:(nonnull NSString *)messageID
                 campaignName:(nonnull NSString *)campaignName
          renderAsTestMessage:(BOOL)renderAsTestMessage
                  messageType:(https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Enums/FIRInAppMessagingDisplayMessageType.html)messageType
                  triggerType:(https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Enums/FIRInAppMessagingDisplayTriggerType.html)triggerType;