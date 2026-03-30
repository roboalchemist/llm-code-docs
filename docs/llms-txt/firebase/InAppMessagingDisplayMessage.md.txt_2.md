# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# InAppMessagingDisplayMessage

    class InAppMessagingDisplayMessage : NSObject

Base class representing a FIAM message to be displayed. Don't create instance
of this class directly. Instantiate one of its subclasses instead.
- `


  ### [campaignInfo](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)campaignInfo)


  ` Metadata for the campaign to which this message belongs.

  #### Declaration

  Swift

      @NSCopying var campaignInfo: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo.html { get }

- `


  ### [type](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)type)


  ` The type and UI style of this message.

  #### Declaration

  Swift

      var type: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDisplayMessageType.html { get }

- `


  ### [triggerType](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)triggerType)


  ` How this message should be triggered.

  #### Declaration

  Swift

      var triggerType: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDisplayTriggerType.html { get }

- `


  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(im)init)


  ` Unavailable.
- `


  ### [init(messageID:campaignName:renderAsTestMessage:messageType:triggerType:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(im)initWithMessageID:campaignName:renderAsTestMessage:messageType:triggerType:)


  ` Deprecated, this class shouldn't be directly instantiated.

  #### Declaration

  Swift

      init(messageID: String, campaignName: String, renderAsTestMessage: Bool, messageType: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDisplayMessageType.html, triggerType: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDisplayTriggerType.html)