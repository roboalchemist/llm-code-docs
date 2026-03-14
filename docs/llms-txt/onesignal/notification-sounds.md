# Source: https://documentation.onesignal.com/docs/en/notification-sounds.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Notification sounds

> Adding custom sounds to mobile notifications.

Custom sounds are a way to provide a more unique, branded experience for your app. You may add a custom sound with every notification you send, or you may add sounds to just certain types of notifications. For instance, a game like "Jewel Breaker" may wish to have a jewel-like sound always played when receiving notifications. Meanwhile, a social network may wish to only play sounds when the user receives a message from another user to differentiate those notifications from more generic system notifications.

<Warning>
  For mobile apps only. Custom sounds are not supported on web push.
</Warning>

## Setup

### Create sound files

Be sure to create sound files according to the following rules. If the device cannot find the file in question, or if the file is not in a supported format, it will fall back to the default system notification sound.

<Note>
  Keep sound filenames lowercase since some platforms ignore upper case letters for sound files. Instead of `AwesomeSound.wav` use `awesomesound.wav` or `awesome_sound.wav`.
</Note>

| Platform | Extensions            | Notes                                                                                                    |
| -------- | --------------------- | -------------------------------------------------------------------------------------------------------- |
| iOS      | `.wav` `.aiff` `.caf` | Sounds must be encoded as Linear PCM, MA4 (IMA/ADPCM), µLaw, or aLaw. Must be less than 30 seconds.      |
| Android  | `.wav` `.mp3` `.ogg`  | Recommended length less than 30 seconds. Keep file size small, large files may not play on some devices. |
| Huawei   | `.wav` `.mp3` `.wma`  | Recommended length less than 30 seconds. Keep file size small, large files may not play on some devices. |
| Amazon   | `.wav` `.mp3` `.ogg`  | Recommended length less than 30 seconds. Keep file size small, large files may not play on some devices. |

### Add sound files to app

To adds sounds to notifications, you must include the sound files as resources within your app. External URLs are not supported.

<Tabs>
  <Tab title="iOS">
    Add sound files to the appropriate location in your Xcode project depending on your SDK.

    | SDK            | Folder                                                                                                                                                      |
    | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | iOS Native     | Add files to the Xcode project root. Make sure **Add to targets** is selected when adding files so that they are automatically add to the bundle resources. |
    | Cordova, Ionic | Add files to `Resources` directory within the Xcode project in `<project-root>/platforms/ios/project-name.xcodeproj`.                                       |
    | Unity          | Add sounds anywhere in your Unity project, build your project, and then move those sounds to the Xcode project root.                                        |
  </Tab>

  <Tab title="Android, Huawei, and Amazon">
    Add sound files to the appropriate folder in your project depending on your SDK. **If the folder does not exist, create it.**

    | SDK                            | Folder                                                                                                                                                                    |
    | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Android, Huawei, Amazon Native | `res/raw`                                                                                                                                                                 |
    | React Native                   | `<project-root>/android/app/src/main/res/raw`                                                                                                                             |
    | Cordova                        | `<project-root>/platforms/android/res/raw/`                                                                                                                               |
    | Ionic                          | `/android/app/src/main/res/raw/`                                                                                                                                          |
    | Unity                          | `Assets/Plugins/Android/OneSignalConfig/res/raw` *NOTE: Your sound and icon file names must be lowercase and can't contain anything else except underscores and numbers.* |
    | Flutter                        | `main/res/raw`                                                                                                                                                            |
    | .NET                           | `<project-root>/Platforms/Android/Resources/raw/`                                                                                                                         |
  </Tab>
</Tabs>

### Send notifications

<Tabs>
  <Tab title="iOS">
    Add the file extension when referencing the sound resource. For instance, `explode_sound.wav`. Set in the dashboard when sending push messages or use the [Create Notification](/reference/create-message) API `ios_sound` property.

    For no sound, pass in `nil` to the **Sound** field.

    <Frame>
      <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/a05af7e-Screenshot_2023-02-28_at_3.16.55_PM.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=9d33c9837ac9f67b0d6c6a7a87d03212" width="423" height="606" data-path="images/docs/a05af7e-Screenshot_2023-02-28_at_3.16.55_PM.png" />
    </Frame>
  </Tab>

  <Tab title="Android, Huawei, and Amazon">
    Android 8+ introduced [Notification Categories](./android-notification-categories) which must be setup to customize notification sounds. OneSignal will use the sound set in the Notification Channel for all versions of Android.

    In **Settings > Push & In-App > Android Notification Channels** create the group and channel.

    <Frame caption="Create a notification channel">
      <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/8f39237-Screenshot_2023-02-28_at_3.11.52_PM.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=b18a97c1706dde194bd4e5c13cd9f593" width="877" height="487" data-path="images/docs/8f39237-Screenshot_2023-02-28_at_3.11.52_PM.png" />
    </Frame>

    * Set **Importance** to "Urgent" or "High" to play sound.
    * Set **Sound** to "Default" or "Custom" based on your needs. **Do not** add the file extension when referencing the sound resource. For instance, `cat_meow_sound`.
    * For no sound, set **Importance** to "Urgent" or "High" and **Sound** to "Off". Or you can set **Importance** to "Medium" or "Low" for no sound.

    <Frame caption="Set the sound for a notification channel">
      <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/f7950b6-Screenshot_2023-02-28_at_3.11.03_PM.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=88d88df41d360b190b4c083709e8119c" width="429" height="498" data-path="images/docs/f7950b6-Screenshot_2023-02-28_at_3.11.03_PM.png" />
    </Frame>

    You can then set the category name in the dashboard when sending push messages or use the [Create Notification](/reference/create-message) API `android_channel_id` and `huawei_channel_id` properties. The sound set in the category will work for all android versions.

    <Frame caption="Set the category name for a notification in the dashboard">
      <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/5e8625c-Screenshot_2023-02-28_at_3.15.19_PM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=c02f9a68fcb73b913a1de93e01d0f4aa" width="423" height="517" data-path="images/docs/5e8625c-Screenshot_2023-02-28_at_3.15.19_PM.png" />
    </Frame>
  </Tab>

  <Tab title="REST API">
    Instead of sending via the dashboard, you can send notifications with sounds in the REST API by using the appropriate parameter and file extension depending on your platform (see more in [Create notification REST API docs](/reference/push-notification)).

    | Platform | API Parameter                                                                                                                                                                                                       | Details                                                                                        |
    | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
    | iOS      | `ios_sound`                                                                                                                                                                                                         | Include File Extension. Example: `ios_sound : expload_sound.wav` No sound, pass `nil`.         |
    | Android  | `android_channel_id `- Use if you created channel in the OneSignal Dashboard [Notification Categories](./android-notification-categories). `existing_android_channel_id` - Use if you created the channel elsewhere | Highly recommended to use [Android Notification Categories](./android-notification-categories) |
    | Huawei   | `huawei_channel_id` - Use if you created channel in the OneSignal Dashboard [Notification Categories](./android-notification-categories). `huawei_existing_channel_id` - Use if you created the channel elsewhere   | Highly recommended to use [Android Notification Categories](./android-notification-categories) |
    | Amazon   | `adm_sound`                                                                                                                                                                                                         | Do Not Include File Extension. Example: `adm_sound : exploade_sound`                           |
  </Tab>
</Tabs>

<Warning>
  If you've very recently added a sound resource to your app, you may want to wait a few days before sending notifications using the sound. This is because it can take many days or even weeks for the majority of your users to update their apps to the latest version which contain your new sound resource.

  If a user has an older version of your app without the sound resource and receives a notification that references it, they will hear only the default system notification sound.
</Warning>

***

## FAQ

### Can I set a default sound?

Use a [Template](./templates) that references the sound and/or Android Notification Channel.

### Why is my notification not playing the custom sound file?

There are a few reasons why a sound may not play.

* Sound file has an incorrect file extension
* Sound file is not encoded in a supported format
* Sound file is in the incorrect location
* Sound file is too long

Currently OneSignal does not log the resource incorrect issues, we're working on adding this to your logs.

**iOS** - Read more in [Apple's documentation](https://developer.apple.com/documentation/usernotifications/unnotificationsound?language=objc) for tips on how to encode files and test them.

**Android** - Make sure that it is getting built into your APK by extracting it and making sure it is located in `res/raw/`.

If shrinking resources is enabled, you can protect sound files from being removed by creating keep.xml in res/raw/ with following code

```xml xml theme={null}
<resources xmlns:tools="http://schemas.android.com/tools"
tools:keep="@raw/sound_file"/>
```

### Why is my notification playing the default sound file?

Please make sure that you followed the setup instructions carefully and the sound file is in the correct location for the SDK.

### Why is the wrong sound playing?

On Android, notifications will get grouped together after a certain amount are received by the device without opening them. Grouped notifications play a default sound. You can set the sound with the [GROUPKEY](https://developer.android.com/training/notify-user/group) for all your notifications.

***

Built with [Mintlify](https://mintlify.com).
