# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk.md

# Android SDK Overview

> Learn how to integrate the ASAPP Android SDK into your application.

You can integrate ASAPP's Android SDK into your application to provide a seamless messaging experience for your Android customers.

### Android Requirements

ASAPP supports Android 5.0 (API level 21) and up. The SDK currently targets API level 30.

ASAPP distributes the library via a Maven repository and you can import it with Gradle. ASAPP wrote the SDK in Kotlin. You can also use it if you developed your application in Java.

## Getting Started

To get started with Android SDK, you need to:

1. [Gather Required Information](#1-gather-required-information "1. Gather Required Information")
2. [Install the SDK](#2-install-the-sdk "2. Install the SDK")
3. [Configure the SDK](#3-configure-the-sdk "3. Configure the SDK")
4. [Open Chat](#4-open-chat "4. Open Chat")

### 1. Gather Required Information

Before downloading and installing the SDK, please make sure you have the following information. Contact your Implementation Manager at ASAPP if you have any questions.

|                      |                                                                                                                                                                                                                                        |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| App ID               | Also known as the "Company Marker", assigned by ASAPP.                                                                                                                                                                                 |
| API Host Name        | The fully-qualified domain name used by the SDK to communicate with ASAPP's API. Provided by ASAPP and subject to change based on the stage of implementation.                                                                         |
| Region Code          | The ISO 3166-1 alpha-2 code for the region of the implementation, provided by ASAPP.                                                                                                                                                   |
| Supported Languages  | Your app's supported languages, in order of preference, as an array of language tag strings. Strings can be in the format "\{ISO 639-1 Code}-\{ISO 3166-1 Code}" or "\{ISO 639-1 Code}", such as "en-us" or "en". Defaults to \["en"]. |
| Client Secret        | This can be an empty or random string\* until otherwise notified by ASAPP.                                                                                                                                                             |
| User Identifier      | A username or similar value used to identify and authenticate the customer, provided by the Customer Company.                                                                                                                          |
| Authentication Token | A password-equivalent value, which may or may not expire, used to authenticate the customer that is provided by the Customer Company.                                                                                                  |

\* In the future, the ASAPP-provided client secret will be a string that authorizes the integrated SDK to call the ASAPP API in production. ASAPP recommends fetching this string from a server and storing it securely using Secure Storage; however, as it is one of many layers of security, you can hard-code the client secret.

### 2. Install the SDK

ASAPP distributes the library via a Maven repository and you can import it with Gradle. First, add the ASAPP Maven repository to the top-level `build.gradle` file of your project:

```groovy  theme={null}
repositories {
    maven {
        url  "https://packages.asapp.com/chat/sdk/android"
    }
}
```

Then, add the SDK to your application dependencies:

`implementation 'com.asapp.chatsdk:chat-sdk:<version>'`

Please check the latest Chat SDK version in the [repository](https://gitlab.com/asappinc/public/mobile-sdk/android/-/packages) or [release notes](https://docs-sdk.asapp.com/api/chatsdk/android/releasenotes/).

At this point, sync and rebuild your project to make sure all dependencies are imported successfully. You can also validate the authenticity of the downloaded dependency by following these steps.

### Validate Android SDK Authenticity

You can verify the authenticity of the SDK and make sure that ASAPP generated the binary. The GPG signature is the standard way ASAPP handles Java binaries when this is a requirement.

#### Setup

First, download the ASAPP public key [from here](https://docs-sdk.asapp.com/api/chatsdk/android/security/asapp_public.gpg).

```json  theme={null}
wget -O asapp_public_key.asc https://docs-sdk.asapp.com/api/chatsdk/android/security/asapp_public.gpg
```

#### Verify File Signature

Use the console GPG command to import the key:

```json  theme={null}
gpg --import asapp_public_key.asc
```

You can verify that the public key was imported via `gpg --list-keys`.

Download the ASC file directly from [our repository](https://gitlab.com/asappinc/public/mobile-sdk/android/-/packages). Finally, you can verify the Chat SDK AAR and associated ASC files like so:

```json  theme={null}
gpg --verify chat-sdk-<version>.aar.asc chat-sdk-<version>.aar
```

### 3. Configure the SDK

Use the code below to create a configuration, and initialize the SDK with it. You must pass your `Application` instance.

Refer to the aforementioned [required information](/agent-desk/integrations/ios-sdk/ios-quick-start). ASAPP recommends you initialize the SDK in your `Application.onCreate`.

```json  theme={null}
import com.asapp.chatsdk.ASAPP
import com.asapp.chatsdk.ASAPPConfig
val asappConfig = ASAPPConfig(
   appId = "my-app-id",
   apiHostName = "my-hostname.test.asapp.com",
   clientSecret = "my-secret",
   enableSDKCrashlytics = true)
ASAPP.init(application = this, config = asappConfig)
```

<Note>
  In case, you are facing compile issue after setting enableSDKCrashlytics to true, perform the following steps

  1. Add (if not present) the following plugins to your app module's build.gradle.kts or build.gradle:
     * id("com.google.gms.google-services")
     * id("com.google.firebase.crashlytics")
  2. Add (if not present) the Firebase BOM to your app's dependencies block:"
     * implementation(platform("com.google.firebase:firebase-bom:29.0.0"))
  3. Create a dummy google-services.json and place it in location: \$APP\_DIR/google-services.json.
</Note>

<Note>
  The SDK should only be initialized once and it is possible to update the configuration at runtime.
</Note>

### 4. Open Chat

Once the SDK has been configured and initialized, you can open chat. To do so, use the `openChat(context: Context)` function which will start a new Activity:

```kotlin  theme={null}
ASAPP.instance.openChat(context = this)
```

Once the chat interface is open, you should see an initial state similar to the one below:

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-22b1ac55-782d-e734-1a48-114b7f0e8a88.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=fb2fe0fba2e5d127050a4a4aad1366a0" data-og-width="621" width="621" data-og-height="783" height="783" data-path="image/uuid-22b1ac55-782d-e734-1a48-114b7f0e8a88.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-22b1ac55-782d-e734-1a48-114b7f0e8a88.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=0cc09aa335fccfe520a582cf523f80ec 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-22b1ac55-782d-e734-1a48-114b7f0e8a88.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=1e3038aca624f9b981885dd3a733f01d 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-22b1ac55-782d-e734-1a48-114b7f0e8a88.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=d19c1ce3296348044cc3f6ada00acdd6 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-22b1ac55-782d-e734-1a48-114b7f0e8a88.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=e297bb897bceb87994dc1a64e3ef5b19 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-22b1ac55-782d-e734-1a48-114b7f0e8a88.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=5722575aacd81ff6c73d120a952a97e7 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-22b1ac55-782d-e734-1a48-114b7f0e8a88.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=ce434a87454178d1182eddce8f878808 2500w" />
</Frame>

## Next Steps

<CardGroup>
  <Card title="Customization" href="/agent-desk/integrations/android-sdk/customization" />

  <Card title="User Authentication" href="/agent-desk/integrations/android-sdk/user-authentication" />

  <Card title="Miscellaneous APIs" href="/agent-desk/integrations/android-sdk/miscellaneous-apis" />

  <Card title="Deep Links and Web Links" href="/agent-desk/integrations/android-sdk/deep-links-and-web-links" />

  <Card title="Notifications" href="/agent-desk/integrations/android-sdk/notifications" />
</CardGroup>
