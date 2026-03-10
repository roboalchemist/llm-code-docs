# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes.md.txt

# FirebaseInAppMessaging Framework Reference

# Classes

The following classes are available globally.
- `


  ### [InAppMessaging](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessaging)


  ` The root object for in-app messaging iOS SDK.

  Note: Firebase In-App Messaging depends on using a Firebase Installation ID and token pair to be
  able to retrieve messages defined for the current app instance. By default, the Firebase In-App
  Messaging SDK will obtain the ID and token pair on app/SDK startup. In its default configuration
  the in-app messaging SDK will send some device and client data (linked to the installation ID)
  to the Firebase backend periodically.

  The app can tune the default data collection behavior via certain controls. They are listed in
  descending order below. If a higher-priority setting exists, lower level settings are ignored.
  1. Dynamically turning on or off data collection behavior by setting the `automaticDataCollectionEnabled` property on the `InAppMessaging` instance to true or false.
  2. Setting `FirebaseInAppMessagingAutomaticDataCollectionEnabled` to false in the app's plist file.
  3. Disabling data collection via the global Firebase data collection setting.

  This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Swift

      class InAppMessaging : NSObject

- `


  ### [InAppMessagingActionButton](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton)


  ` Contains the display information for an action button. This class is unavailable on macOS,
  - macOS Catalyst, and watchOS.

  #### Declaration

  Swift

      class InAppMessagingActionButton : NSObject

- `


  ### [InAppMessagingImageData](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData)


  ` Contain display data for an image for a fiam message.
  - This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Swift

      class InAppMessagingImageData : NSObject

- `


  ### [InAppMessagingCampaignInfo](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCampaignInfo)


  ` Defines the metadata for the campaign to which a FIAM message belongs.
  - This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Swift

      class InAppMessagingCampaignInfo : NSObject

- `


  ### [InAppMessagingAction](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingAction)


  ` Defines the metadata for a FIAM action.
  - This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Swift

      class InAppMessagingAction : NSObject

- `


  ### [InAppMessagingDisplayMessage](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage)


  ` Base class representing a FIAM message to be displayed. Don't create instance
  of this class directly. Instantiate one of its subclasses instead.
  This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Swift

      class InAppMessagingDisplayMessage : NSObject

- `


  ### [InAppMessagingCardDisplay](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay)


  ` A displayable in-app card message.
  This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Swift

      class InAppMessagingCardDisplay : https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage

- `


  ### [InAppMessagingModalDisplay](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingModalDisplay)


  ` Class for defining a modal message for display.
  This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Swift

      class InAppMessagingModalDisplay : https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage

- `


  ### [InAppMessagingBannerDisplay](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingBannerDisplay)


  ` Class for defining a banner message for display.
  This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Swift

      class InAppMessagingBannerDisplay : https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage

- `


  ### [InAppMessagingImageOnlyDisplay](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageOnlyDisplay)


  ` Class for defining a image-only message for display.
  This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Swift

      class InAppMessagingImageOnlyDisplay : https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage