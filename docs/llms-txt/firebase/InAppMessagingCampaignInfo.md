# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCampaignInfo.md.txt

# FirebaseInAppMessaging Framework Reference

# InAppMessagingCampaignInfo

    class InAppMessagingCampaignInfo : NSObject

Defines the metadata for the campaign to which a FIAM message belongs.

- This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [messageID](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(py)messageID)

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

  ### [campaignName](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(py)campaignName)

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

  ### [renderAsTestMessage](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(py)renderAsTestMessage)

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

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(im)init)

  `
  `  
  Unavailable  
  Unavailable.