# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRIAMDefaultDisplayImpl](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRIAMDefaultDisplayImpl)


  ` Public class for displaying fiam messages. Most apps should not use it since its instance
  would be instantiated upon SDK start-up automatically. It's exposed in public interface
  to help UI Testing app access the UI layer directly.

  #### Declaration

  Objective-C


      @interface FIRIAMDefaultDisplayImpl : NSObject <https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Protocols/FIRInAppMessagingDisplay>

- `


  ### [FIRInAppMessagingActionButton](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingActionButton)


  ` Contains the display information for an action button.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingActionButton : NSObject

- `


  ### [FIRInAppMessagingImageData](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageData)


  ` Contain display data for an image for a fiam message.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingImageData : NSObject

- `


  ### [FIRInAppMessagingCampaignInfo](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo)


  ` Defines the metadata for the campaign to which a FIAM message belongs.

  #### Declaration

  Objective-C

      @interface FIRInAppMessagingCampaignInfo : NSObject

- `


  ### [FIRInAppMessagingAction](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingAction)


  ` Defines the metadata for a FIAM action.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingAction : NSObject

- `


  ### [FIRInAppMessagingDisplayMessage](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage)


  ` Base class representing a FIAM message to be displayed. Don't create instance
  of this class directly. Instantiate one of its subclasses instead.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingDisplayMessage : NSObject

- `


  ### [FIRInAppMessagingCardDisplay](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay)


  ` Undocumented

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingCardDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage

- `


  ### [FIRInAppMessagingModalDisplay](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingModalDisplay)


  ` Class for defining a modal message for display.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingModalDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage

- `


  ### [FIRInAppMessagingBannerDisplay](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingBannerDisplay)


  ` Class for defining a banner message for display.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingBannerDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage

- `


  ### [FIRInAppMessagingImageOnlyDisplay](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageOnlyDisplay)


  ` Class for defining a image-only message for display.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingImageOnlyDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage