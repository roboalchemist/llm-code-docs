# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/ios-quick-start.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# iOS Quick Start

If you want to start fast, follow these steps:

1. [Gather Required Information](#1-gather-required-information "1. Gather Required Information")
2. [Download the SDK](#2-download-the-sdk "2. Download the SDK")
3. [Install the SDK](#3-install-the-sdk "3. Install the SDK")
4. [Configure the SDK](#4-configure-the-sdk "4. Configure the SDK")
5. [Open Chat](#5-open-chat "5. Open Chat")

## 1. Gather Required Information

Before downloading and installing the SDK, please make sure you have the following information. Contact your Implementation Manager at ASAPP if you have any questions.

| App ID               | Also known as the "Company Marker", assigned by ASAPP.                                                                                                                                                                              |
| :------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API Host Name        | The fully-qualified domain name used by the SDK to communicate with ASAPP's API. Provided by ASAPP and subject to change based on the stage of implementation.                                                                      |
| Region Code          | The ISO 3166-1 alpha-2 code for the region of the implementation, provided by ASAPP.                                                                                                                                                |
| Supported Languages  | Your app's supported languages, in order of preference, as an array of language tag strings. Strings can be in the format `{ISO 639-1 Code}-{ISO 3166-1 Code}` or `{ISO 639-1 Code}`, such as "en-us" or "en". Defaults to \["en"]. |
| Client Secret        | This can be an empty or random string\* until otherwise notified by ASAPP.                                                                                                                                                          |
| User Identifier      | A username or similar value used to identify and authenticate the customer, provided by the Customer Company.                                                                                                                       |
| Authentication Token | A password-equivalent value, which may or may not expire, used to authenticate the customer that is provided by the Customer Company.                                                                                               |

\* In the future, the ASAPP-provided client secret will be a string that authorizes the integrated SDK to call the ASAPP API in production. ASAPP recommends fetching this string from a server and storing it securely using Secure Storage; however, as it is one of many layers of security, you can hard-code the client secret.

## 2. Download the SDK

Download the iOS SDK from the [ASAPP iOS SDK releases page on GitHub](https://github.com/asappinc/chat-sdk-ios-release/releases).

## 3. Install the SDK

ASAPP provides the SDK as an `.xcframework` with and without bitcode in dynamic and static flavors. If in doubt, ASAPP recommends that you use the dynamic `.xcframework` with bitcode.

Add your chosen flavor of the framework to the "Frameworks, Libraries, and Embedded Content" section of your target's "General" settings.

### Include SDK Resources When Using the Static Framework

Add the provided `ASAPPResources.bundle` to your target's "Frameworks, Libraries, and Embedded Content" and then include it in your target's "Copy Bundle Resources" build phase.

The SDK allows customers to take and upload photos, [unless you disable these features through configuration](https://docs-sdk.asapp.com/api/chatsdk/ios/latest/Classes/ASAPP.html#/Permissions). Since iOS 10, Apple requires descriptions for why your app uses the photo library and/or camera, which Apple displays to the customer. If you haven't already, you'll need to add these descriptions to your app's `Info.plist`.

* If you access `Info.plist` via Xcode's plist editor, the description keys are "Privacy - Camera Usage Description" and "Privacy - Photo Library Usage Description".
* If you access `Info.plist` via a text editor, the keys are "NSPhotoLibraryUsageDescription" and "NSCameraUsageDescription".

### Validate iOS SDK Authenticity

ASAPP uses GPG (GNU Privacy Guard) for creating digital signatures. To install on macOS:

1. Using [Homebrew](https://brew.sh), install gpg:
   `brew install gpg`
2. Download the [ASAPP SDK Team public key](https://docs-sdk.asapp.com/api/chatsdk/ios/security/asapp_public.gpg).
3. Add the key to GPG:
   `gpg --import asapp_public.gpg`

Optionally, you can also validate the public key. Please refer to the [GPG documentation](https://www.gnupg.org/documentation/manuals.html) for more information.

Then, you can verify the signature using:

`gpg --verify <-sdk-filename>.sig <sdk-filename>`

ASAPP provides the signature alongside the SDK in each release.

## 4. Configure the SDK

Use the code below to create a config, initialize the SDK with the config, and set an anonymous user. Refer to the aforementioned [Required Information](#1-gather-required-information-15931 "1. Gather Required Information") for more details. ASAPP recommends that you initialize the SDK on launch in `application(_:didFinishLaunchingWithOptions…)`. Please see the [User Authentication](/agent-desk/integrations/ios-sdk/user-authentication "User Authentication") section for details about how to authenticate an identified user.

```json  theme={null}
import ASAPPSDK
let config = ASAPPConfig(appId: appId,
                         apiHostName: apiHostName,
                         clientSecret: clientSecret,
                         regionCode: regionCode)
ASAPP.initialize(with: config)
ASAPP.user = ASAPPUser(nil, requestContextProvider: { _ in return [:] })
```

## 5. Open Chat

Once the SDK has been initialized with a config and a user has been set, you can create a chat view controller that can then be pushed onto the navigation stack. ASAPP recommends doing so when a navigation bar button is tapped.

```json  theme={null}
let chatViewController =
ASAPP.createChatViewControllerForPushing(fromNotificationWith: nil)!
navigationController?.pushViewController(chatViewController, animated: true)
```

If you prefer to present the chat view controller as a modal, use the `ForPresenting` method instead:

```json  theme={null}
let chatViewController =
ASAPP.createChatViewControllerForPresenting(fromNotificationWith: nil)!
present(chatViewController, animated: true, completion: nil)
```

Once the chat interface is open, you should see an initial state similar to the one below:

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-862d403d-e7b8-5ed0-d8aa-bc4726b65a4b.svg?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=170863c2489010e23bdec67f00f3ceb8" data-og-width="881" width="881" data-og-height="1156" height="1156" data-path="image/uuid-862d403d-e7b8-5ed0-d8aa-bc4726b65a4b.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-862d403d-e7b8-5ed0-d8aa-bc4726b65a4b.svg?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=4a0cc8b6f0083b629f334d0f74cd8f35 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-862d403d-e7b8-5ed0-d8aa-bc4726b65a4b.svg?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=b7778434a4c32ed43292533d801648b8 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-862d403d-e7b8-5ed0-d8aa-bc4726b65a4b.svg?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=ae9088919e8d64bf60c2b8e0b01621d8 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-862d403d-e7b8-5ed0-d8aa-bc4726b65a4b.svg?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=19ce1507a7e4f9b4f2da60e5c8bb9312 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-862d403d-e7b8-5ed0-d8aa-bc4726b65a4b.svg?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e1c2717a897d52e2b3675590b9ffe587 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-862d403d-e7b8-5ed0-d8aa-bc4726b65a4b.svg?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=ad692beaab7710ab1109ddb610359916 2500w" />
</Frame>
