# Source: https://firebase.google.com/docs/in-app-messaging/customize-messages.md.txt

<br />

iOS+AndroidFlutter  

<br />

Firebase In-App Messaging provides a useful set of preconfigured behaviors and message types with a default look and feel, but in some cases you may want to extend behaviors and message content. In-App Messaging allows you to add actions to messages and customize message look and feel.

## Add an action to your message

With actions you can use your in-app messages to direct users to a website or a specific screen in your app.

### Implement a deep link handler

Firebase In-App Messaginguses link handlers to process actions. The SDK is able to use a number of handlers, so if your app already has one,Firebase In-App Messagingcan use that without any further setup. If you don't yet have a handler, you can useFirebase Dynamic Links. To learn more, read[Create Dynamic Links on iOS](https://firebase.google.com/docs/dynamic-links/ios/create).

### Add the action to your message using theFirebaseconsole

Once your app has a link handler, you're ready to compose a campaign with an action. Open theFirebaseconsole to[Messaging](https://console.firebase.google.com/project/_/messaging), and start a new campaign or edit an existing campaign. In that campaign, provide a**Card** ,**Button text** and**Button action** , an**Image action** , or a**Banner action**, where the action is a relevant deep link.

The action's format depends on which message layout you choose. Modals get action buttons with customizable button text content, text color, and background color. Images and top banners, on the other hand, become interactive and invoke the specified action when tapped.

## Modify message look and feel

Firebase In-App Messaginglets you customize message displays to change the way your app renders messages' layout, font styles, button shapes, and other details. There are two ways to modify message displays: modify the defaultFirebase In-App Messagingdisplays or create your own message display library from scratch.  
**Note:**This product is not available on macOS, Mac Catalyst, App Clip or watchOS targets.

### Modify default displays

The most straightforward way customize your messages is to build off ofFirebase In-App Messaging's default message display code.

#### Clone the`firebase-ios-sdk`repo

To get started, clone the[latest release](https://github.com/firebase/firebase-ios-sdk/releases/latest)of the`firebase-ios-sdk`repo, and open the[InAppMessaging directory](https://github.com/firebase/firebase-ios-sdk/tree/master/FirebaseInAppMessaging).

#### Select message types to modify

With the repo cloned, you can modify any or all of theFirebase In-App Messagingmessage types:`Card`,`Modal`,`Banner`, and`ImageOnly`. Each type corresponds to a message layout in theFirebase In-App Messagingcampaign creation flow.

Accordingly, each type has access to a different set of data, determined by campaign customization options in theFirebaseconsole:

|   Type    | titleText | bodyText | textColor | backgroundColor | imageData | actionButton | secondaryActionButton |
|-----------|-----------|----------|-----------|-----------------|-----------|--------------|-----------------------|
| Card      | check     | check    | check     | check           | check     | check        | check                 |
| Modal     | check     | check    | check     | check           | check     | check        |                       |
| Banner    | check     | check    | check     | check           | check     |              |                       |
| ImageOnly |           |          |           |                 | check     |              |                       |

#### Modify the message display rendering code

With the message type limitations in mind, you're free to modify them however you'd like. You can create a banner that displays at the bottom of your app, move around the action button on a modal, embed the in-app message in a user's feed, or any other modification that would make the messages' look and feel fit your app.

There are two main things to pay attention to when modifying message displays:

- **Message type directories:** Each message type has a separate directory with files that determine that type's logic:
  - [`Card`](https://github.com/firebase/firebase-ios-sdk/tree/master/FirebaseInAppMessaging/Sources/DefaultUI/Card)
  - [`Modal`](https://github.com/firebase/firebase-ios-sdk/tree/master/FirebaseInAppMessaging/Sources/DefaultUI/Modal)
  - [`Banner`](https://github.com/firebase/firebase-ios-sdk/tree/master/FirebaseInAppMessaging/Sources/DefaultUI/Banner)
  - [`ImageOnly`](https://github.com/firebase/firebase-ios-sdk/tree/master/FirebaseInAppMessaging/Sources/DefaultUI/ImageOnly)
- **Storyboard:** The`InAppMessaging`library also has a`.storyboard`file that helps define the UI for all three message types:
  - [`FIRInAppMessageDisplayStoryboard.storyboard`](https://github.com/firebase/firebase-ios-sdk/tree/master/FirebaseInAppMessaging/iOS/Resources/)

Modify files in your preferred message types' directories and the corresponding sections of the`.storyboard`to create your custom message displays.

#### Update your podfile to use your modified`InAppMessaging`code

To getFirebase In-App Messagingto use your modified message displays instead of the default displays, update your podfile to use your customized`InAppMessaging`library:  

```scdoc
# Uncomment the next line to define a global platform for your project
# platform :ios, '9.0'

target 'YourProject' do
# Comment the next line if you're not using Swift and don't want to use dynamic frameworks
use_frameworks!

# Pods for YourProject
pod 'Firebase'

# Remove the default InAppMessaging pod:
# pod 'Firebase/InAppMessaging'

# Overwrite it with a version that points to your local copy:
pod `FirebaseInAppMessaging', :path => '<var translate="no">~/Path/To/The/Cloned/Repo/</var>'

end
```
With that done, you can update your pods, rebuild your app, and see your new, customized message displays.

<br />

### Create your own message display library

You're not limited to working from the`InAppMessaging`library to create a UI for displaying messages. You can also write your own code from scratch.

#### Build a class that implements the`InAppMessagingDisplay`protocol

| **Note:** In Objective-C, all types are prefixed with`FIR`to avoid class name collisions.

Firebase In-App Messaginguses the`InAppMessaging`class to handle communications between Firebase servers and your app. That class, in turn, uses the`InAppMessagingDisplay`protocol to display the messages it receives. To build your own display library, write a class that implements the protocol.

The protocol definition and documentation on how to conform to it are in the`FIRInAppMessagingDisplay.h`file of the`InAppMessaging`library.
| **Tip: Use the`InAppMessaging`code for reference.** Even if you're not building with it directly, you'll probably find it helpful to take a look at the defaultFirebase In-App Messagingmessage displays to get a feel for how they implement`InAppMessagingDisplay`. You can find them in the[Firebase Apple platforms SDK GitHub repo](https://github.com/firebase/firebase-ios-sdk/tree/master/FirebaseInAppMessaging/).

#### Set`messageDisplayComponent`to use your message display library

`InAppMessaging`uses its[`messageDisplayComponent`](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessaging#messagedisplaycomponent)property to determine which object to use when displaying messages. Set that property to an object of your custom message display class, soFirebase In-App Messagingknows to use your library to render messages:  

```text
InAppMessaging.inAppMessaging().messageDisplayComponent = yourInAppMessagingRenderingInstance
```