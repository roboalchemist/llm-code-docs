# Source: https://support.anydesk.com/docs/anydesk-for-android

**AnyDesk for Android** offers a powerful and mobile way to connect to and control remote desktops. This guide helps you get started and troubleshoot common issues.

> ::: blockquote-title
> 🚨 [**IMPORTANT**]
> :::
>
> As of Android 10 and depending on the smartphone provider, 8 and 9, users will get an Android security prompt regarding casting when connecting to the Android device. For most, this message is unskippable and requires the end user to manually accept the prompt before the connecting user is able to establish the session.
>
> ![](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/image(109).png)

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![AnyDesk - Google Play](https://f.hubspotusercontent40.net/hubfs/7940397/Help%20Center/AnyDesk%20for%20Android/Available_GooglePlay-55dc42.svg)](https://play.google.com/store/apps/details?id=com.anydesk.anydeskandroid)   [![AnyDesk - AppGallery](https://f.hubspotusercontent40.net/hubfs/7940397/Help%20Center/AnyDesk%20for%20Android/Available_Huawei-7b3d39.svg)](https://appgallery.huawei.com/#/app/C100140863)   [![AnyDesk - Galaxy Store](https://f.hubspotusercontent40.net/hubfs/7940397/Help%20Center/AnyDesk%20for%20Android/Available_GalaxyStore-cf156b.svg)](https://galaxystore.samsung.com/detail/com.anydesk.anydeskandroid)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## System requirements 

-   **Android**

    -   Remote control features require **Android 7.0 or higher**.

    -   Many Android devices require an additional **control plugin** to enable full input control. When you launch AnyDesk for the first time, the application will automatically prompt you to install the appropriate plugin.

    > 🚨[[ ]][**IMPORTANT**]
    >
    > Some devices may require manually enabling the plugin under **Settings \> Accessibility** after installation.

-   **ChromeOS**

    -   [**Only remote screen viewing** (without input control) is **available on ChromeOS,** due to vendor restrictions.]

------------------------------------------------------------------------

## Getting started with control plugins 

Instead of choosing a plugin manually, rely on the **Plugin available** prompt when launching AnyDesk or using **Menu \> About AnyDesk**. This ensures the correct plugin for your device is selected, and it also guides you through the activation process.

If your device still lacks a plugin, the generic `ad1` plugin is installed, though it may only support basic functions like mouse control. For full compatibility, contact your device manufacturer to cooperate with AnyDesk on a dedicated plugin.

Control plugins enable remote control of Android devices using the AnyDesk Android app. You can view the complete plugin list on the [Android Control Plugins](/v1/docs/android-control-plugins) page.

------------------------------------------------------------------------

## Register license key 

To register a license key on Android:

-   Download or configure a **custom AnyDesk APK** with the **Assign to license** option enabled.

-   Upon installation, you will see an app labeled **AnyDesk custom** linked to your license, offering features like the Address Book and Session Logging.

------------------------------------------------------------------------

## Permission management 

Starting with AnyDesk 7.2.0 for Android, a **Setup Checklist** guides you to enable necessary permissions.

![](https://7940397.fs1.hubspotusercontent-na1.net/hubfs/7940397/image-png-Nov-14-2024-04-15-31-5423-PM.png)

-   Launch the checklist manually from the main menu if dismissed initially.\
    ![](https://7940397.fs1.hubspotusercontent-na1.net/hubfs/7940397/image-png-Nov-14-2024-04-16-14-8754-PM.png)

-   Tap any item to see how the permission is used and quickly jump to the relevant Android settings page to allow it.\
    ![](https://7940397.fs1.hubspotusercontent-na1.net/hubfs/7940397/image-png-Nov-14-2024-04-18-03-9978-PM.png)

------------------------------------------------------------------------

## Session controls 

During a session, you can open the **Session Menu** by long-pressing the AnyDesk logo. Move the logo by double-tapping and dragging it anywhere on the screen.

You can use the menu during the session to:

-   End the session

-   Adjust transmission quality

-   Toggle input control, clipboard sync, and privacy screen

-   Manage audio and display settings

-   Start/stop VPN or session recording

-   Send CTRL+ALT+DEL or request elevation

If the connected device has multiple displays, users can switch between the various displays from here as well as enable and disable fullscreen mode on Android.

![](https://f.hubspotusercontent40.net/hubfs/7940397/Knowledge%20Base%20Import/Open_Menu_3rd_Entry.png)

### Supported gestures 

When using **mouse** or **touchpad** mode inside a session:

-   Single-finger swipe - move the cursor

-   Two-finger pinch - zoom in/out

-   Three-finger swipe - scroll

-   Tap - left-click

-   Hold - right-click

-   Three-finger tap - middle-click

------------------------------------------------------------------------

## Hotkeys 

When connecting to an Android device from Windows, AnyDesk offers keyboard shortcuts to Android navigation buttons. Hold **CTRL+ALT+SHIFT** and then press one of the following keys:

  ------------------------------------------------------------- ------------------------------------------------------------------------
  [**Key**]   [**Android action**]
  **F5**                                                        Back
  **F6**                                                        Home
  **F7**                                                        Recent apps
  **F8**                                                        App menu
  **F9**                                                        Power
  **F11**                                                       Volume down
  **F12**                                                       Volume up
  **End**                                                       OK button
  ------------------------------------------------------------- ------------------------------------------------------------------------

------------------------------------------------------------------------

## Mobile device management (MDM) 

Since version 6.1.10, AnyDesk for Android supports integration with third-party MDM platforms like Microsoft Intune, currently available only for the standard client from the Google Play Store. MDM consoles can detect available options and show brief descriptions of each feature.

### Remote control in work profiles 

To control a device with a non-Personal (Work) profile, you must pair the `ad1` control plugin across profiles:

To pair the plugin:

1.  Install the `ad1` plugin in the **Personal profile.**

2.  Enable it in **Accessibility settings.**

3.  Open `ad1` in the **non‑Personal profile.**

4.  In the plugin menu, select **Choose Plugin.**

5.  In the **Personal** tab, select AD1 (format may vary on Android 8.1--10).

6.  Accept the configuration request.

7.  To initiate pairing, click **OK**.

If the above fails, reverse the setup order. Also, cross-profile communication may need to be enabled via your MDM. Manufacturer-specific plugins often bypass the pairing requirement.

------------------------------------------------------------------------

## Custom client 

### Installation 

AnyDesk is available as a **Custom Client APK**. To install it:

-   Enable installation from **untrusted sources** (preferably for a file explorer app, not a browser).\
    ![212px-Android_unknown_allowed (1)](https://f.hubspotusercontent40.net/hubfs/7940397/Help%20Center/AnyDesk%20for%20Android/212px-Android_unknown_allowed%20(1).png)

-   Menu names may vary by Android version or device manufacturer.

#### Auto Blocker and Android 14 restrictions 

Starting with Android 14, Google and some device manufacturers introduced new security features that block the installation of APKs including custom AnyDesk clients.

If these protections are active, the installation may fail with a message such as:

![](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/image(110).png)

**To turn it off:**

**On Samsung Galaxy devices (One UI 6 or newer):**

1.  Open Settings › Security and privacy › Additional security settings › Auto Blocker

2.  Turn Auto Blocker off

3.  Retry installing the custom AnyDesk APK

**On stock Android 16 devices (Pixel and others):**

1.  Go to Settings › Security and privacy › Advanced Protection / Device Protection\
    [**Note:** Menu names and locations may vary by manufacturer or Android version.]

2.  Disable the protection mode

3.  Retry installing the custom AnyDesk APK

### Custom package name 

If you wish to upload your custom AnyDesk client to your private app store for easy deployment across your managed devices, simply set a custom package name for it.

To deploy through a private app store:

1.  In custom client configuration, enable **Android Package Name Suffix**.

2.  Enter a suffix that:

    -   Starts with a letter

    -   Is 3--16 characters long

    -   Uses only lowercase Latin letters, no symbols

3.  Save and upload the generated custom client to your app store.

------------------------------------------------------------------------

## Android API 

AnyDesk provides an Android API similar to the Windows CLI. Access is limited to system apps, and detailed documentation is available via support.

### API features 

-   **Returns** - version, connection status, ID, alias, user name.

-   **Checks** - whether unattended access is active, if any incoming session occurred, and if a custom user image exists.

-   **Sets** - unattended access password, connection behavior, Discovery status, user name, and custom image.

------------------------------------------------------------------------

## Troubleshooting 

### Plugin not activating 

Some Android devices require a **reboot** for the control plugin to function properly.

### Control plugin disabled on Android TV 

If **Accessibility** settings are disabled:

-   Only remote view is available.

-   A workaround (without warranty) is to enable control via **ADB shell**:

``` 
adb shell settings put secure enabled_accessibility_services com.anydesk.adcontrol.ad1/com.anydesk.adcontrol.AccService
```

Refer to the official [ADB documentation](https://developer.android.com/studio/command-line/adb) for details.

### Screen recording prompt (Android 10+) 

Android requires user consent to start screen recording. To bypass with ADB (use at your own risk):

-   **Standard Client**:

    ``` 
    adb shell appops set com.anydesk.anydeskandroid PROJECT_MEDIA allow
    ```

-   **Custom Client**:

    ``` 
    adb shell appops set com.anydesk.anydeskandroid.custom PROJECT_MEDIA allow
    ```

### Android battery optimization 

Android includes a feature called **Battery Optimization**, which is designed to preserve battery life by limiting background activity. However, when enabled for AnyDesk, this feature may interfere with remote sessions by automatically closing the application after 30 to 60 seconds in the background. This behavior disrupts active remote control sessions, resulting in unexpected session termination.

To maintain a stable connection when remotely controlling an Android device, you should exclude AnyDesk and its control plugin from Battery Optimization.

#### Google Pixel devices 

1.  Open the **Settings** app.

2.  Navigate to **Apps** \> **AnyDesk** \> **Battery**.

3.  Tap **Unrestricted** to allow full background activity.

4.  Repeat Steps 2--3 for the **AnyDesk plugin**.

#### Motorola devices 

1.  Open the **Settings** app.

2.  Go to **Battery** \> **Battery Optimization**.

3.  Tap **Not optimized** and switch to **All apps**.

4.  Locate **AnyDesk**, then select **Don\'t optimize**.

5.  Repeat Steps 3--4 for the **AnyDesk plugin**.

#### General guidelines for other devices 

If your Android device differs from the examples provided:

-   Search for *Battery Optimization* or *App battery usage* in the Settings search bar.

-   Ensure that both AnyDesk and any installed plugin (e.g., `ad1`) are set to *Unrestricted* or *Not optimized*.

-   Refer to your device's user manual or support website for precise instructions.

------------------------------------------------------------------------

## Send support information 

If AnyDesk crashes or encounters errors, you can send trace files and a detailed description.

On the Android device:

1.  Open the menu in the main AnyDesk window.

2.  Tap **About AnyDesk**.

3.  Select **Send Support Information**.

4.  Enter details and tap **Send Email**.

If no email client is present:

1.  Connect from a desktop AnyDesk to the Android device.

2.  Ensure the desktop client has permission to:

    -   Control the device

    -   Access the clipboard

    -   Transfer files

3.  In the **Accept Window**, tap the three-dot menu and select **Send AnyDesk trace file**.\
    ![](https://7940397.fs1.hubspotusercontent-na1.net/hubfs/7940397/Screenshot%202024-10-14%20at%204-12-03%E2%80%AFPM-png.png)

4.  On the desktop, paste the trace using **CTRL+V** or right-click paste.

As of AnyDesk 7.2.0 (Android), you can also open, filter, and copy trace logs via:\
**Main Menu \> About AnyDesk \> Open AnyDesk Log**.

![](https://7940397.fs1.hubspotusercontent-na1.net/hubfs/7940397/image-png-Nov-14-2024-04-21-50-0803-PM.png)