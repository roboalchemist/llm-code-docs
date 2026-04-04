# Source: https://docs.asapp.com/agent-desk/integrations/chat-instead/ios.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# iOS

## Pre-requisites

* ASAPP iOS SDK 9.4.0 or later, correctly configured and initialized [see more here](/agent-desk/integrations/ios-sdk/ios-quick-start).

## Getting Started

Once you've successfully configured and initialized the ASAPP SDK, you can start using Chat Instead for iOS.

1. Create a New Instance.

   ```json  theme={null}
   let chatInsteadViewController =  ASAPPChatInsteadViewController(phoneNumber: phoneNumber, delegate: delegate, title: title, chatIcon: image)
   ```

   |                        |                                                                                                                                                                                                                                                                            |
   | :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | phoneNumber (required) | The phone number to call when the phone channel is selected. Must be a valid phone number. For more information, see Apple's documentation on [phone links](https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/PhoneLinks/PhoneLinks). |
   | delegate (required)    | An object that implements `ASAPPChannelDelegate`.                                                                                                                                                                                                                          |
   | title (optional)       | A title (also called the "Chat Instead header title") which is displayed at the top of the Chat Instead UI. (See [Customization](#customization "Customization"))                                                                                                          |
   | image (optional)       | A UI Image that will override the default image for the chat channel. (See [Customization](#customization "Customization"))                                                                                                                                                |

2. Implement two functions that the `ASAPPChannelDelegate` requires:

   ```json  theme={null}
   func channel(_ channel: ASAPPChannel, didFailToOpenWithErrorDescription errorDescription: String?)
   ```

   ASAPP calls this if an error occurs while trying to open a channel.

   ```json  theme={null}
   func didSelectASAPPChatChannel()
   ```

   This opens the ASAPP chat.

   You should use one of these methods:

   ```json  theme={null}
   ASAPP.createChatViewControllerForPresentingFromChatInstead()
   ```

   or

   ```json  theme={null}
   ASAPP.createChatViewControllerForPushingFromChatInstead()
   ```

   to present or push the view controller instance that ASAPP returned.

   This means that you must present/push the ASAPP chat view controller inside `didSelectASAPPChatChannel()`.

<Note>
  ASAPP highly recommends initializing `ASAPPChatInsteadViewController` as early as possible for the best user experience.
</Note>

Whenever a channel is selected, ASAPP handles everything by default (except for the chat channel), but you can also handle a channel by yourself by implementing `func shouldOpenChannel(_ channel: ASAPPChannel) -> Bool` and returning false.

3. Show the `chatInsteadViewController` instance by using:

   ```json  theme={null}
   present(chatInsteadViewController, animated: true)
   ```

<Note>
  Only presentation works. Pushing the `chatInsteadViewController` instance does not work and causes unexpected behavior.
</Note>

## Support for iPad

For the best user experience, you should configure popover mode, which is used on iPad.

Use the `.popover` presentation style and set both the [sourceView](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622313-sourceview) and [sourceRect](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622324-sourcerect) properties following Apple's conventions:

```json  theme={null}
chatInsteadViewController.modalPresentationStyle = .popover
chatInsteadViewController.popoverPresentationController?.sourceView = aView
chatInsteadViewController.popoverPresentationController?.sourceRect = aRect
```

This will only have an effect when your app is run on iPad.

<Note>
  If you set `modalPresentationStyle` to `.popover` and forget to set `sourceView` and `sourceRect`, the application will crash in runtime. So please be sure to set both if you're using the popover mode.
</Note>

## Customization

You can customize the Chat Instead header title and the chat icon when creating the `ASAPPChatInsteadViewController` instance. (See [Getting Started](#getting-started "iOS").

<Frame>
  <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe1fe0e0-a7e7-d065-110c-b3b24627847b.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=0e858cf47e3564c073af38f44cd814e5" data-og-width="1999" width="1999" data-og-height="929" height="929" data-path="image/uuid-fe1fe0e0-a7e7-d065-110c-b3b24627847b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe1fe0e0-a7e7-d065-110c-b3b24627847b.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=5441d2dc01ccb30932eb2cdd2d1e11c5 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe1fe0e0-a7e7-d065-110c-b3b24627847b.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=bdac0d4bb09e32d24f16d2b8948899a0 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe1fe0e0-a7e7-d065-110c-b3b24627847b.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=1818734cb2a32577a174a5c775ab6a1e 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe1fe0e0-a7e7-d065-110c-b3b24627847b.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=7c2fb887b0f256efb6ba84a4d57505c8 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe1fe0e0-a7e7-d065-110c-b3b24627847b.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=993228b8288c34bc9743e6a9ffb3126f 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe1fe0e0-a7e7-d065-110c-b3b24627847b.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=8e477172fdfe6a155b8f43948f833952 2500w" />
</Frame>

`ASAPPChatInsteadViewController` uses [ASAPPColors](https://docs-sdk.asapp.com/api/chatsdk/ios/latest/Classes/ASAPPColors.html) for styling, so it will automatically use the colors set there (e.g. `primary`, `background`, `onBackground`, etc.), which are the same colors used for customizing the ASAPP chat interface. There is no way to independently change the styling of the Chat Instead UI.

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59879767-4622-5d70-522e-12ca0b7a8f8f.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=0c52d5bf38b636aed26902db65152cf9" data-og-width="1999" width="1999" data-og-height="929" height="929" data-path="image/uuid-59879767-4622-5d70-522e-12ca0b7a8f8f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59879767-4622-5d70-522e-12ca0b7a8f8f.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=c949c29c71f6e558b845fc3b6fd2ad27 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59879767-4622-5d70-522e-12ca0b7a8f8f.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=ca386671d68afde373e3d4ab179a8acc 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59879767-4622-5d70-522e-12ca0b7a8f8f.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=a526653f4b9790315fda5c3fcac48287 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59879767-4622-5d70-522e-12ca0b7a8f8f.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=f7c326e4f927172ef9aaa028711aa3a3 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59879767-4622-5d70-522e-12ca0b7a8f8f.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1132e51b218110d78c81ee5d0649211b 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59879767-4622-5d70-522e-12ca0b7a8f8f.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=de3c18114971d113c3940f4e11e8333d 2500w" />
</Frame>

ASAPP supports [Dark Mode](../ios-sdk/customization#dark-mode-15935 "Dark Mode") by default as long as you enable it.

## Remote settings

When you create an instance of `ASAPPChatInsteadViewController`, it automatically fetches remote settings to indicate which channels to display. You can configure these settings.

<Note>
  These remote settings override local ones (i.e. the ones you pass in when creating the `ASAPPChatInsteadViewController` instance).
</Note>

If an error occurs while fetching the settings and no local values were set, the system uses the defaults.

## Cache

When fetching succeeds, the SDK caches the remote settings for a short period of time. This cache references in lieu of repeated fetches. The cache remains valid across multiple app sessions.
