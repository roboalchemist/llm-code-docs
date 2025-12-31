# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo.md.txt

# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCampaignInfo.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# FIRInAppMessagingCampaignInfo

    class FIRInAppMessagingCampaignInfo : NSObject

Defines the metadata for the campaign to which a FIAM message belongs.
- `
  ``
  ``
  `

  ### [messageID](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(py)messageID)

  `
  `  
  Identifier for the campaign for this message.  

  #### Declaration

  Swift  

      var messageID: String { get }

- `
  ``
  ``
  `

  ### [campaignName](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(py)campaignName)

  `
  `  
  The name of this campaign, as defined in the console on campaign creation.  

  #### Declaration

  Swift  

      var campaignName: String { get }

- `
  ``
  ``
  `

  ### [renderAsTestMessage](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(py)renderAsTestMessage)

  `
  `  
  Whether or not this message is being rendered in Test On Device mode.  

  #### Declaration

  Swift  

      var renderAsTestMessage: Bool { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(im)init)

  `
  `  
  Unavailable.
- `
  ``
  ``
  `

  ### [init(messageID:campaignName:renderAsTestMessage:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(im)initWithMessageID:campaignName:renderAsTestMessage:)

  `
  `  
  Deprecated, this class shouldn't be directly instantiated.  

  #### Declaration

  Swift  

      init(messageID: String, campaignName: String, renderAsTestMessage: Bool)