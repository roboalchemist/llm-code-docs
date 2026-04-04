# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage.md.txt

# FirebaseInAppMessaging Framework Reference

# InAppMessagingDisplayMessage

    class InAppMessagingDisplayMessage : NSObject

Base class representing a FIAM message to be displayed. Don't create instance
of this class directly. Instantiate one of its subclasses instead.
This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [campaignInfo](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)campaignInfo)

  `
  `  
  Metadata for the campaign to which this message belongs.  

  #### Declaration

  Swift  

      @NSCopying var campaignInfo: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCampaignInfo.html { get }

- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)type)

  `
  `  
  The type and UI style of this message.  

  #### Declaration

  Swift  

      var type: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingDisplayMessageType.html { get }

- `
  ``
  ``
  `

  ### [triggerType](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)triggerType)

  `
  `  
  How this message should be triggered.  

  #### Declaration

  Swift  

      var triggerType: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingDisplayTriggerType.html { get }

- `
  ``
  ``
  `

  ### [appData](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(py)appData)

  `
  `  
  Extra key-value dictionary data that can be sent along with the message  

  #### Declaration

  Swift  

      var appData: [AnyHashable : Any]? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(im)init)

  `
  `  
  Unavailable  
  Unavailable.
- `
  ``
  ``
  `

  ### [init(messageID:campaignName:renderAsTestMessage:messageType:triggerType:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage#/c:objc(cs)FIRInAppMessagingDisplayMessage(im)initWithMessageID:campaignName:renderAsTestMessage:messageType:triggerType:)

  `
  `  
  Exposed for unit testing only. Don't instantiate this in your app directly.  

  #### Declaration

  Swift  

      init(messageID: String, campaignName: String, renderAsTestMessage: Bool, messageType: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingDisplayMessageType.html, triggerType: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingDisplayTriggerType.html)