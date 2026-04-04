# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# FIRInAppMessagingDisplayMessage


    @interface FIRInAppMessagingDisplayMessage : NSObject

Base class representing a FIAM message to be displayed. Don't create instance
of this class directly. Instantiate one of its subclasses instead.
- `


  ### [campaignInfo](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)campaignInfo)


  ` Metadata for the campaign to which this message belongs.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull)
          https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo.html *campaignInfo;

- `


  ### [type](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)type)


  ` The type and UI style of this message.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic) https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDisplayMessageType.html type;

- `


  ### [triggerType](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)triggerType)


  ` How this message should be triggered.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic) https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDisplayTriggerType.html triggerType;

- `


  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(im)init)


  ` Unavailable.

  #### Declaration

  Objective-C

      - (nonnull instancetype)init;

- `


  ### [-initWithMessageID:campaignName:renderAsTestMessage:messageType:triggerType:](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(im)initWithMessageID:campaignName:renderAsTestMessage:messageType:triggerType:)


  ` Deprecated, this class shouldn't be directly instantiated.

  #### Declaration

  Objective-C

      - (nonnull instancetype)
            initWithMessageID:(nonnull NSString *)messageID
                 campaignName:(nonnull NSString *)campaignName
          renderAsTestMessage:(BOOL)renderAsTestMessage
                  messageType:(https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDisplayMessageType.html)messageType
                  triggerType:(https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDisplayTriggerType.html)triggerType;