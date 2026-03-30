# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# Classes

The following classes are available globally.
- `


  ### [InAppMessagingDefaultDisplayImpl](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDefaultDisplayImpl)


  ` Public class for displaying fiam messages. Most apps should not use it since its instance
  would be instantiated upon SDK start-up automatically. It's exposed in public interface
  to help UI Testing app access the UI layer directly.

  #### Declaration

  Swift

      class InAppMessagingDefaultDisplayImpl : NSObject, https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Protocols/InAppMessagingDisplay

- `


  ### [InAppMessagingActionButton](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingActionButton)


  ` Contains the display information for an action button.

  #### Declaration

  Swift

      class InAppMessagingActionButton : NSObject

- `


  ### [InAppMessagingImageData](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingImageData)


  ` Contain display data for an image for a fiam message.

  #### Declaration

  Swift

      class InAppMessagingImageData : NSObject

- `


  ### [FIRInAppMessagingCampaignInfo](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCampaignInfo)


  ` Defines the metadata for the campaign to which a FIAM message belongs.

  #### Declaration

  Swift

      class FIRInAppMessagingCampaignInfo : NSObject

- `


  ### [InAppMessagingAction](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingAction)


  ` Defines the metadata for a FIAM action.

  #### Declaration

  Swift

      class InAppMessagingAction : NSObject

- `


  ### [InAppMessagingDisplayMessage](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage)


  ` Base class representing a FIAM message to be displayed. Don't create instance
  of this class directly. Instantiate one of its subclasses instead.

  #### Declaration

  Swift

      class InAppMessagingDisplayMessage : NSObject

- `


  ### [InAppMessagingCardDisplay](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingCardDisplay)


  ` Undocumented

  #### Declaration

  Swift

      class InAppMessagingCardDisplay : https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage

- `


  ### [InAppMessagingModalDisplay](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingModalDisplay)


  ` Class for defining a modal message for display.

  #### Declaration

  Swift

      class InAppMessagingModalDisplay : https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage

- `


  ### [InAppMessagingBannerDisplay](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingBannerDisplay)


  ` Class for defining a banner message for display.

  #### Declaration

  Swift

      class InAppMessagingBannerDisplay : https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage

- `


  ### [InAppMessagingImageOnlyDisplay](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingImageOnlyDisplay)


  ` Class for defining a image-only message for display.

  #### Declaration

  Swift

      class InAppMessagingImageOnlyDisplay : https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage