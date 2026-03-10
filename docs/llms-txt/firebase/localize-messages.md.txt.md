# Source: https://firebase.google.com/docs/cloud-messaging/customize-messages/localize-messages.md.txt

This documentation outlines the use of FCM localization fields
(`*_loc_key` and `*_loc_args`) to deliver notifications that automatically adapt
to a user's language settings on Android and iOS. This lets your server send a
single, language-agnostic payload, delegating the translation to the client
device.

## FCM Localization Overview

To localize your app, you can send a key that corresponds to a string resource
entry inside the user's application. The device's operating system (OS) handles
the lookup and insertion of dynamic arguments.

> [!NOTE]
> **Note:** See [`AndroidNotification`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification) and [`ApnsConfig`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#apnsconfig) in the [HTTP v1 reference
> documentation](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages) for complete detail on the keys available in platform-specific blocks in the message body. For keys supported by APNS, see Apple's [Payload Key
> Reference](https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification#Payload-key-reference).

| FCM Field | Description | Client Action |
|---|---|---|
| `title_loc_key` | The key for the title string in the client app's string resources. | The OS finds the corresponding string in the app's localized files. |
| `body_loc_key` | The key for the body string in the client app's string resources. | The OS finds the corresponding string in the app's localized files. |
| `title_loc_args` | An array of dynamic string values to be substituted into the `title_loc_key` string. | The OS inserts these arguments into the localized string's format specifiers. |
| `body_loc_args` | An array of dynamic string values to be substituted into the `body_loc_key` string. | The OS inserts these arguments into the localized string's format specifiers. |

## Step 1: Define localized string resources in your apps

To get started with FCM localization, it is important to make sure that you have the necessary
translations available in your Android and iOS projects.

### Android Setup

**Define string resources** : Enter your default language strings in `res/values/strings.xml`.
Use format specifiers (`%1$s`, `%2$d`, etc.) for any dynamic values you plan to
pass in the `*_loc_args`.

Default (`res/values/strings.xml`):

    <resources>
        <string name="welcome_title">Welcome, %1$s!</string>
        <string name="new_message_body">You have %1$d new message(s) from %2$s.</string>
    </resources>

**Add translations** : Create language-specific directories using the ISO language
codes (e.g., `values-fr` for French, `values-es` for Spanish) and translate the keys.

French (`res/values-fr/strings.xml`):

    <resources>
        <string name="welcome_title">Bienvenue, %1$s!</string>
        <string name="new_message_body">Vous avez %1$d nouveau(x) message(s) de %2$s.</string>
    </resources>

For more information, use the following documentation:

- [String resources - Android Developers](https://developer.android.com/guide/topics/resources/string-resource)

- [Localize your app - Android Developers](https://developer.android.com/training/basics/supporting-devices/languages)

### iOS Setup

**Define string resources** : Define your base strings in the `Localizable.strings`
file (typically in the `Base.lproj` folder or a String Catalog). Use format
specifiers (`%@`, `%ld`, etc.) for dynamic values. Keys are often defined in
all capital letters for convention.

Default (English `Localizable.strings`):

    "WELCOME_TITLE" = "Welcome, %@!";
    "NEW_MESSAGE_BODY" = "You have %ld new message(s) from %@.";

**Add translations** : Create language-specific `.lproj` folders (or add
localizations using a String Catalog) and translate the keys.

French (`fr.lproj/Localizable.strings`):

    "WELCOME_TITLE" = "Bienvenue, %@!";
    "NEW_MESSAGE_BODY" = "Vous avez %ld nouveau(x) message(s) de %@.";

For more information, use the following documentation:

- [Localization - Apple Developer Documentation](https://developer.apple.com/localization)

- [String resources - Apple Developer
  Documentation](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Strings/Strings.html)

## Step 2: Construct the FCM message payload

When sending the notification using the FCM HTTP v1 API, your server
constructs a single payload that uses the resource keys (`*_loc_key`) and the
dynamic data (`*_loc_args`) as an array of strings.

### Example FCM HTTP v1 Payload

The localization keys are placed within the platform-specific override blocks
(`android.notification` and `apns.payload.aps.alert`).

    {
      "message": {
        "token": "DEVICE_REGISTRATION_TOKEN",

        "android": {
          "notification": {
            // Android keys match strings.xml resource names
            "title_loc_key": "welcome_title",
            "title_loc_args": ["Alice"],
            "body_loc_key": "new_message_body",
            "body_loc_args": ["3", "Bob"]
          }
        },

        "apns": {
          "payload": {
            "aps": {
              "alert": {
                // iOS uses 'title-loc-key' and 'loc-key' (for the body)
                "title-loc-key": "WELCOME_TITLE",
                "title-loc-args": ["Alice"],
                "loc-key": "NEW_MESSAGE_BODY",
                "loc-args": ["3", "Bob"]
              }
            }
          }
        }
      }
    }

### Key considerations for payload arguments

- **Order matters** : The strings in `*_loc_args` must be in the exact order
  required by the placeholders in the string resource file (e.g., `%1$s`, `%2$s`).

- **Strings only** : All elements in the `*_loc_args` array must be strings, even
  if they represent numbers (like `"3"` in the example). The client OS's string
  formatter handles the final type conversion based on the format specifier
  (`%ld` or `%1$d`).

## Step 3: Client processing and display

When the device receives the notification, the following steps occur automatically:

1. **Language check**: The device identifies the user's primary locale (e.g.,
   German, Italian).

2. **Key lookup** : The OS uses the `*_loc_key` value (`welcome_title`) to look up
   the corresponding translated string in the app's resource files for the
   device's locale.

3. **Argument insertion** : The OS takes the array from `*_loc_args` (`["Alice"]`)
   and inserts the values into the localized string, respecting the locale's
   formatting rules (punctuation, word order, etc.).

| Device Locale | `title_loc_key`: welcome_title | `title_loc_args`: \["Alice"\] | Final Title Display |
|---|---|---|---|
| English | `"Welcome, %1$s!"` | Alice | `"Welcome, Alice!"` |
| French | `"Bienvenue, %1$s!"` | Alice | `"Bienvenue, Alice!"` |
| German | `"Willkommen, %1$s!"` | Alice | `"Willkommen, Alice!"` |

This process makes sure that every user receives a message tailored to their
language preferences, using the correct linguistic structure, all while
maintaining a standardized payload from your server.

## Example: notification message with localization options

The following example send request sends a notification to the `Tech` topic,
including localization options for the client to display localized messages.
Here's an example of the visual effect on a user's device:

![Simple drawing of two devices displaying text in English and Spanish](https://firebase.google.com/static/docs/cloud-messaging/images/Localization_v2.png)

### Node.js

    var topicName = 'industry-tech';

    var message = {
      android: {
        ttl: 3600000,
        notification: {
          bodyLocKey: 'STOCK_NOTIFICATION_BODY',
          bodyLocArgs: ['FooCorp', '11.80', '835.67', '1.43']
        }
      },
      apns: {
        payload: {
          aps: {
            alert: {
              locKey: 'STOCK_NOTIFICATION_BODY',
              locArgs: ['FooCorp', '11.80', '835.67', '1.43']
            }
          }
        }
      },
      topic: topicName,
    };

    getMessaging().send(message)
      .then((response) => {
        // Response is a message ID string.
        console.log('Successfully sent message:', response);
      })
      .catch((error) => {
        console.log('Error sending message:', error);
      });

### REST

    POST https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send HTTP/1.1

    Content-Type: application/json
    Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA
    {
      "message": {
        "topic":"Tech",
        "android": {
          "ttl":"3600s",
          "notification": {
            "body_loc_key": "STOCK_NOTIFICATION_BODY",
            "body_loc_args": ["FooCorp", "11.80", "835.67", "1.43"]
          }
        },
        "apns": {
          "payload": {
            "aps": {
              "alert": {
                "loc-key": "STOCK_NOTIFICATION_BODY",
                "loc-args": ["FooCorp", "11.80", "835.67", "1.43"]
              }
            }
          }
        }
      }
    }'

To learn more, see
[`AndroidNotification`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification)
and
[`ApnsConfig`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#apnsconfig)
in the [HTTP v1 reference
documentation](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages)
for complete detail on the keys available in platform-specific blocks in the
message body. For keys supported by APNS, see Apple's [Payload Key
Reference](https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification#Payload-key-reference).