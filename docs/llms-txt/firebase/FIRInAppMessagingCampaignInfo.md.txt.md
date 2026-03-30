# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCampaignInfo.md.txt

# FirebaseInAppMessaging Framework Reference

# FIRInAppMessagingCampaignInfo


    @interface FIRInAppMessagingCampaignInfo : NSObject

Defines the metadata for the campaign to which a FIAM message belongs.

- This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `


  ### [messageID](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(py)messageID)


  ` Identifier for the campaign for this message.

  #### Declaration

  Objective-C

      @property (nonatomic, copy, readonly, nonnull) NSString *messageID;

- `


  ### [campaignName](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(py)campaignName)


  ` The name of this campaign, as defined in the console on campaign creation.

  #### Declaration

  Objective-C

      @property (nonatomic, copy, readonly, nonnull) NSString *campaignName;

- `


  ### [renderAsTestMessage](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(py)renderAsTestMessage)


  ` Whether or not this message is being rendered in Test On Device mode.

  #### Declaration

  Objective-C

      @property (nonatomic, readonly) BOOL renderAsTestMessage;

- `


  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(im)init)


  ` Unavailable
  Unavailable.

  #### Declaration

  Objective-C

      - (nonnull instancetype)init;