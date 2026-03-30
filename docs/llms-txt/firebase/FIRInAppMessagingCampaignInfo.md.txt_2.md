# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# FIRInAppMessagingCampaignInfo

    @interface FIRInAppMessagingCampaignInfo : NSObject

Defines the metadata for the campaign to which a FIAM message belongs.
- `


  ### [messageID](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(py)messageID)


  ` Identifier for the campaign for this message.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull) NSString *messageID;

- `


  ### [campaignName](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(py)campaignName)


  ` The name of this campaign, as defined in the console on campaign creation.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull) NSString *campaignName;

- `


  ### [renderAsTestMessage](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(py)renderAsTestMessage)


  ` Whether or not this message is being rendered in Test On Device mode.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic) BOOL renderAsTestMessage;

- `


  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(im)init)


  ` Unavailable.

  #### Declaration

  Objective-C

      - (nonnull instancetype)init;

- `


  ### [-initWithMessageID:campaignName:renderAsTestMessage:](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo#/c:objc(cs)FIRInAppMessagingCampaignInfo(im)initWithMessageID:campaignName:renderAsTestMessage:)


  ` Deprecated, this class shouldn't be directly instantiated.

  #### Declaration

  Objective-C

      - (nonnull instancetype)initWithMessageID:(nonnull NSString *)messageID
                                   campaignName:(nonnull NSString *)campaignName
                            renderAsTestMessage:(BOOL)renderAsTestMessage;