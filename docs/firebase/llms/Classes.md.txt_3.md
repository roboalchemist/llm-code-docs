# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes.md.txt

# FirebaseInAppMessaging Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRInAppMessaging](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessaging)


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

  Objective-C


      @interface FIRInAppMessaging : NSObject

- `


  ### [FIRInAppMessagingActionButton](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingActionButton)


  ` Contains the display information for an action button. This class is unavailable on macOS,
  - macOS Catalyst, and watchOS.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingActionButton : NSObject

- `


  ### [FIRInAppMessagingImageData](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData)


  ` Contain display data for an image for a fiam message.
  - This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingImageData : NSObject

- `


  ### [FIRInAppMessagingCampaignInfo](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCampaignInfo)


  ` Defines the metadata for the campaign to which a FIAM message belongs.
  - This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingCampaignInfo : NSObject

- `


  ### [FIRInAppMessagingAction](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingAction)


  ` Defines the metadata for a FIAM action.
  - This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingAction : NSObject

- `


  ### [FIRInAppMessagingDisplayMessage](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage)


  ` Base class representing a FIAM message to be displayed. Don't create instance
  of this class directly. Instantiate one of its subclasses instead.
  This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingDisplayMessage : NSObject

- `


  ### [FIRInAppMessagingCardDisplay](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingCardDisplay)


  ` A displayable in-app card message.
  This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingCardDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage

- `


  ### [FIRInAppMessagingModalDisplay](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingModalDisplay)


  ` Class for defining a modal message for display.
  This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingModalDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage

- `


  ### [FIRInAppMessagingBannerDisplay](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingBannerDisplay)


  ` Class for defining a banner message for display.
  This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingBannerDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage

- `


  ### [FIRInAppMessagingImageOnlyDisplay](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageOnlyDisplay)


  ` Class for defining a image-only message for display.
  This class is unavailable on macOS, macOS Catalyst, and watchOS.

  #### Declaration

  Objective-C


      @interface FIRInAppMessagingImageOnlyDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage