# Source: https://docs.ntfy.sh/subscribe/phone/

# Subscribe from your phone[¶](#subscribe-from-your-phone "Permanent link")

You can use the ntfy [Android App](https://play.google.com/store/apps/details?id=io.heckel.ntfy) or [iOS app](https://apps.apple.com/us/app/ntfy/id1625396347) to receive notifications directly on your phone. Just like the server, this app is also open source, and the code is available on GitHub ([Android](https://github.com/binwiederhier/ntfy-android), [iOS](https://github.com/binwiederhier/ntfy-ios)). Feel free to contribute, or [build your own](../../develop/).

[![](../../static/img/badge-googleplay.png)](https://play.google.com/store/apps/details?id=io.heckel.ntfy) [![](../../static/img/badge-fdroid.png)](https://f-droid.org/en/packages/io.heckel.ntfy/) [![](../../static/img/badge-appstore.png)](https://apps.apple.com/us/app/ntfy/id1625396347)

You can get the Android app from [Google Play](https://play.google.com/store/apps/details?id=io.heckel.ntfy), [F-Droid](https://f-droid.org/en/packages/io.heckel.ntfy/), or via the APKs from [GitHub Releases](https://github.com/binwiederhier/ntfy-android/releases). The Google Play and F-Droid releases are largely identical, with the one exception that the F-Droid flavor does not use Firebase. The iOS app can be downloaded from the [App Store](https://apps.apple.com/us/app/ntfy/id1625396347).

Alternatively, you may also want to consider using the **[progressive web app (PWA)](../pwa/)** instead of the native app. The PWA is a website that you can add to your home screen, and it will behave just like a native app.

If you\'re downloading the APKs from [GitHub](https://github.com/binwiederhier/ntfy-android/releases), they are signed with a certificate with the following SHA-256 fingerprint: `6e145d7ae685eff75468e5067e03a6c3645453343e4e181dac8b6b17ff67489d`. You can also query the DNS TXT records for `ntfy.sh` to find this fingerprint.

## Overview[¶](#overview "Permanent link")

A picture is worth a thousand words. Here are a few screenshots showing what the app looks like. It\'s all pretty straight forward. You can add topics and as soon as you add them, you can [publish messages](../../publish/) to them.

[![](../../static/img/android-screenshot-main.png)](../../static/img/android-screenshot-main.png) [![](../../static/img/android-screenshot-detail.png)](../../static/img/android-screenshot-detail.png) [![](../../static/img/android-screenshot-pause.png)](../../static/img/android-screenshot-pause.png) [![](../../static/img/android-screenshot-add.png)](../../static/img/android-screenshot-add.png) [![](../../static/img/android-screenshot-add-instant.png)](../../static/img/android-screenshot-add-instant.png) [![](../../static/img/android-screenshot-add-other.png)](../../static/img/android-screenshot-add-other.png)

If those screenshots are still not enough, here\'s a video:

<figure>

<figcaption>Sending push notifications to your Android phone</figcaption>
</figure>

## Message priority[¶](#message-priority "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)] [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE4LjcxIDE5LjVjLS44MyAxLjI0LTEuNzEgMi40NS0zLjA1IDIuNDctMS4zNC4wMy0xLjc3LS43OS0zLjI5LS43OS0xLjUzIDAtMiAuNzctMy4yNy44Mi0xLjMxLjA1LTIuMy0xLjMyLTMuMTQtMi41M0M0LjI1IDE3IDIuOTQgMTIuNDUgNC43IDkuMzljLjg3LTEuNTIgMi40My0yLjQ4IDQuMTItMi41MSAxLjI4LS4wMiAyLjUuODcgMy4yOS44Ny43OCAwIDIuMjYtMS4wNyAzLjgxLS45MS42NS4wMyAyLjQ3LjI2IDMuNjQgMS45OC0uMDkuMDYtMi4xNyAxLjI4LTIuMTUgMy44MS4wMyAzLjAyIDIuNjUgNC4wMyAyLjY4IDQuMDQtLjAzLjA3LS40MiAxLjQ0LTEuMzggMi44M00xMyAzLjVjLjczLS44MyAxLjk0LTEuNDYgMi45NC0xLjUuMTMgMS4xNy0uMzQgMi4zNS0xLjA0IDMuMTktLjY5Ljg1LTEuODMgMS41MS0yLjk1IDEuNDItLjE1LTEuMTUuNDEtMi4zNSAxLjA1LTMuMTEiIC8+PC9zdmc+)]

When you [publish messages](../../publish/#message-priority) to a topic, you can **define a priority**. This priority defines how urgently Android will notify you about the notification, and whether they make a sound and/or vibrate.

By default, messages with default priority or higher (\>= 3) will vibrate and make a sound. Messages with high or urgent priority (\>= 4) will also show as pop-over, like so:

<figure>
<p><img src="../../static/img/priority-notification.png" width="500" alt="priority notification" /></p>
<figcaption>High and urgent notifications show as pop-over</figcaption>
</figure>

You can change these settings in Android by long-pressing on the app, and tapping \"Notifications\", or from the \"Settings\" menu under \"Channel settings\". There is one notification channel for each priority:

<figure>
<p><img src="../../static/img/android-screenshot-notification-settings.png" width="500" alt="notification settings" /></p>
<figcaption>Per-priority channels</figcaption>
</figure>

Per notification channel, you can configure a **channel-specific sound**, whether to **override the Do Not Disturb (DND)** setting, and other settings such as popover or notification dot:

<figure>
<p><img src="../../static/img/android-screenshot-notification-details.jpg" width="500" alt="channel details" /></p>
<figcaption>Per-priority sound/vibration settings</figcaption>
</figure>

## Instant delivery[¶](#instant-delivery "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)]

Instant delivery allows you to receive messages on your phone instantly, **even when your phone is in doze mode**, i.e. when the screen turns off, and you leave it on the desk for a while. This is achieved with a foreground service, which you\'ll see as a permanent notification that looks like this:

<figure>
<p><img src="../../static/img/foreground-service.png" width="500" alt="foreground service" /></p>
<figcaption>Instant delivery foreground notification</figcaption>
</figure>

Android does not allow you to dismiss this notification, unless you turn off the notification channel in the settings. To do so, long-press on the foreground notification (screenshot above) and navigate to the settings. Then toggle the \"Subscription Service\" off:

<figure>
<p><img src="../../static/img/notification-settings.png" width="500" alt="foreground service" /></p>
<figcaption>Turning off the persistent instant delivery notification</figcaption>
</figure>

**Limitations without instant delivery**: Without instant delivery, **messages may arrive with a significant delay** (sometimes many minutes, or even hours later). If you\'ve ever picked up your phone and suddenly had 10 messages that were sent long before you know what I\'m talking about.

The reason for this is [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging). FCM is the *only* Google approved way to send push messages to Android devices, and it\'s what pretty much all apps use to deliver push notifications. Firebase is overall pretty bad at delivering messages in time, but on Android, most apps are stuck with it.

The ntfy Android app uses Firebase only for the main host `ntfy.sh`, and only in the Google Play flavor of the app. It won\'t use Firebase for any self-hosted servers, and not at all in the the F-Droid flavor.

## Share to topic[¶](#share-to-topic "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)]

You can share files to a topic using Android\'s \"Share\" feature. This works in almost any app that supports sharing files or text, and it\'s useful for sending yourself links, files or other things. The feature remembers a few of the last topics you shared content to and lists them at the bottom.

The feature is pretty self-explanatory, and one picture says more than a thousand words. So here are two pictures:

[![](../../static/img/android-screenshot-share-1.jpg)](../../static/img/android-screenshot-share-1.jpg) [![](../../static/img/android-screenshot-share-2.jpg)](../../static/img/android-screenshot-share-2.jpg)

## ntfy:// links[¶](#ntfy-links "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)]

The ntfy Android app supports deep linking directly to topics. This is useful when integrating with [automation apps](#automation-apps) such as [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) or [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm), or to simply directly link to a topic from a mobile website.

Info

Android deep linking of http/https links is very brittle and limited, which is why something like `https://<host>/<topic>/subscribe` is **not possible**, and instead `ntfy://` links have to be used. More details in [issue #20](https://github.com/binwiederhier/ntfy/issues/20).

**Supported link formats:**

  Link format                                                           Example                                     Description
  --------------------------------------------------------------------- ------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`ntfy://<host>/<topic>`]                `ntfy://ntfy.sh/mytopic`                    Directly opens the Android app detail view for the given topic and server. Subscribes to the topic if not already subscribed. This is equivalent to the web view `https://ntfy.sh/mytopic` (HTTPS!)
  [`ntfy://<host>/<topic>?secure=false`]   `ntfy://example.com/mytopic?secure=false`   Same as above, except that this will use HTTP instead of HTTPS as topic URL. This is equivalent to the web view `http://example.com/mytopic` (HTTP!)

## Integrations[¶](#integrations "Permanent link")

### UnifiedPush[¶](#unifiedpush "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)]

[UnifiedPush](https://unifiedpush.org) is a standard for receiving push notifications without using the Google-owned [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging) service. It puts push notifications in the control of the user. ntfy can act as a **UnifiedPush distributor**, forwarding messages to apps that support it.

To use ntfy as a distributor, simply select it in one of the [supported apps](https://unifiedpush.org/users/apps/). That\'s it. It\'s a one-step installation 😀. If desired, you can select your own [selfhosted ntfy server](../../install/) to handle messages. Here\'s an example with [FluffyChat](https://fluffychat.im/):

[![](../../static/img/android-screenshot-unifiedpush-fluffychat.jpg)](../../static/img/android-screenshot-unifiedpush-fluffychat.jpg) [![](../../static/img/android-screenshot-unifiedpush-subscription.jpg)](../../static/img/android-screenshot-unifiedpush-subscription.jpg) [![](../../static/img/android-screenshot-unifiedpush-settings.jpg)](../../static/img/android-screenshot-unifiedpush-settings.jpg)

### Automation apps[¶](#automation-apps "Permanent link")

*Supported on:* [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2LjYxIDE1LjE1Yy0uNDYgMC0uODQtLjM3LS44NC0uODNzLjM4LS44Mi44NC0uODIuODQuMzYuODQuODItLjM4LjgzLS44NC44M20tOS4yIDBjLS40NiAwLS44NC0uMzctLjg0LS44M3MuMzgtLjgyLjg0LS44Mi44My4zNi44My44Mi0uMzcuODMtLjgzLjgzbTkuNS01LjAxIDEuNjctMi44OGMuMDktLjE3LjAzLS4zOC0uMTMtLjQ3LS4xNy0uMS0uMzgtLjA0LS40NS4xM2wtMS43MSAyLjkxQTEwLjE1IDEwLjE1IDAgMCAwIDEyIDguOTFjLTEuNTMgMC0zIC4zMy00LjI3LjkxTDYuMDQgNi45MWEuMzM0LjMzNCAwIDAgMC0uNDctLjEzYy0uMTcuMDktLjIyLjMtLjEzLjQ3bDEuNjYgMi44OEM0LjI1IDExLjY5IDIuMjkgMTQuNTggMiAxOGgyMGMtLjI4LTMuNDEtMi4yMy02LjMtNS4wOS03Ljg2IiAvPjwvc3ZnPg==)]

The ntfy Android app integrates nicely with automation apps such as [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) or [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm). Using Android intents, you can **react to incoming messages**, as well as **send messages**.

#### React to incoming messages[¶](#react-to-incoming-messages "Permanent link")

To react on incoming notifications, you have to register to intents with the `io.heckel.ntfy.MESSAGE_RECEIVED` action (see [code for details](https://github.com/binwiederhier/ntfy-android/blob/main/app/src/main/java/io/heckel/ntfy/msg/BroadcastService.kt)). Here\'s an example using [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) and [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm), but any app that can catch broadcasts is supported:

[![](../../static/img/android-screenshot-macrodroid-overview.png)](../../static/img/android-screenshot-macrodroid-overview.png) [![](../../static/img/android-screenshot-macrodroid-trigger.png)](../../static/img/android-screenshot-macrodroid-trigger.png) [![](../../static/img/android-screenshot-macrodroid-action.png)](../../static/img/android-screenshot-macrodroid-action.png) [![](../../static/img/android-screenshot-tasker-profiles.png)](../../static/img/android-screenshot-tasker-profiles.png) [![](../../static/img/android-screenshot-tasker-event-edit.png)](../../static/img/android-screenshot-tasker-event-edit.png) [![](../../static/img/android-screenshot-tasker-task-edit.png)](../../static/img/android-screenshot-tasker-task-edit.png) [![](../../static/img/android-screenshot-tasker-action-edit.png)](../../static/img/android-screenshot-tasker-action-edit.png)

For MacroDroid, be sure to type in the package name `io.heckel.ntfy`, otherwise intents may be silently swallowed. If you\'re using topics to drive automation, you\'ll likely want to mute the topic in the ntfy app. This will prevent notification popups:

<figure>
<p><img src="../../static/img/android-screenshot-muted.png" width="500" alt="muted subscription" /></p>
<figcaption>Muting notifications to prevent popups</figcaption>
</figure>

Here\'s a list of extras you can access. Most likely, you\'ll want to filter for `topic` and react on `message`:

  Extra name             Type                           Example                                    Description
  ---------------------- ------------------------------ ------------------------------------------ -------------------------------------------------------------------------------------
  `id`                   *String*                       `bP8dMjO8ig`                               Randomly chosen message identifier (likely not very useful for task automation)
  `base_url`             *String*                       `https://ntfy.sh`                          Root URL of the ntfy server this message came from
  `topic` ❤️             *String*                       `mytopic`                                  Topic name; **you\'ll likely want to filter for a specific topic**
  `muted`                *Boolean*                      `true`                                     Indicates whether the subscription was muted in the app
  `muted_str`            *String (`true` or `false`)*   `true`                                     Same as `muted`, but as string `true` or `false`
  `time`                 *Int*                          `1635528741`                               Message date time, as Unix time stamp
  `title`                *String*                       `Some title`                               Message [title](../../publish/#message-title); may be empty if not set
  `message` ❤️           *String*                       `Some message`                             Message body; **this is likely what you\'re interested in**
  `message_bytes`        *ByteArray*                    `(binary data)`                            Message body as binary data
  `encoding`️             *String*                       \-                                         Message encoding (empty or \"base64\")
  `tags`                 *String*                       `tag1,tag2,..`                             Comma-separated list of [tags](../../publish/#tags-emojis)
  `tags_map`             *String*                       `0=tag1,1=tag2,..`                         Map of tags to make it easier to map first, second, \... tag
  `priority`             *Int (between 1-5)*            `4`                                        Message [priority](../../publish/#message-priority) with 1=min, 3=default and 5=max
  `click`                *String*                       `https://google.com`                       [Click action](../../publish/#click-action) URL, or empty if not set
  `attachment_name`      *String*                       `attachment.jpg`                           Filename of the attachment; may be empty if not set
  `attachment_type`      *String*                       `image/jpeg`                               Mime type of the attachment; may be empty if not set
  `attachment_size`      *Long*                         `9923111`                                  Size in bytes of the attachment; may be zero if not set
  `attachment_expires`   *Long*                         `1655514244`                               Expiry date as Unix timestamp of the attachment URL; may be zero if not set
  `attachment_url`       *String*                       `https://ntfy.sh/file/afUbjadfl7ErP.jpg`   URL of the attachment; may be empty if not set

#### Send messages using intents[¶](#send-messages-using-intents "Permanent link")

To send messages from other apps (such as [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) and [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm)), you can broadcast an intent with the `io.heckel.ntfy.SEND_MESSAGE` action. The ntfy Android app will forward the intent as a HTTP POST request to [publish a message](../../publish/). This is primarily useful for apps that do not support HTTP POST/PUT (like MacroDroid). In Tasker, you can simply use the \"HTTP Request\" action, which is a little easier and also works if ntfy is not installed.

Here\'s what that looks like:

[![](../../static/img/android-screenshot-macrodroid-send-macro.png)](../../static/img/android-screenshot-macrodroid-send-macro.png) [![](../../static/img/android-screenshot-macrodroid-send-action.png)](../../static/img/android-screenshot-macrodroid-send-action.png) [![](../../static/img/android-screenshot-tasker-profile-send.png)](../../static/img/android-screenshot-tasker-profile-send.png) [![](../../static/img/android-screenshot-tasker-task-edit-post.png)](../../static/img/android-screenshot-tasker-task-edit-post.png) [![](../../static/img/android-screenshot-tasker-action-http-post.png)](../../static/img/android-screenshot-tasker-action-http-post.png)

The following intent extras are supported when for the intent with the `io.heckel.ntfy.SEND_MESSAGE` action:

  Extra name     Required   Type                            Example             Description
  -------------- ---------- ------------------------------- ------------------- -------------------------------------------------------------------------------------
  `base_url`     \-         *String*                        `https://ntfy.sh`   Root URL of the ntfy server this message came from, defaults to `https://ntfy.sh`
  `topic` ❤️     ✔          *String*                        `mytopic`           Topic name; **you must set this**
  `title`        \-         *String*                        `Some title`        Message [title](../../publish/#message-title); may be empty if not set
  `message` ❤️   ✔          *String*                        `Some message`      Message body; **you must set this**
  `tags`         \-         *String*                        `tag1,tag2,..`      Comma-separated list of [tags](../../publish/#tags-emojis)
  `priority`     \-         *String or Int (between 1-5)*   `4`                 Message [priority](../../publish/#message-priority) with 1=min, 3=default and 5=max