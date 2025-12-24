# Source: https://help.realvnc.com/hc/en-us/articles/360002253138-Release-Notes-v7-7-13-1-and-earlier

# Release Notes (v7 - 7.13.1 and earlier) 

[Follow](/hc/en-us/articles/360002253138-Release-Notes-v7-7-13-1-and-earlier/subscription.html "Opens a sign-in dialog")

![Avatar](https://help.realvnc.com/system/photos/360077753378/Jack_Naisbett_Professional_Headshot_for_web_-_Copy.jpg)

**[Jack N RealVNC](/hc/en-us/profiles/364261730191-Jack-N-RealVNC)**

Updated September 08, 2025 13:19

#### RealVNC Connect v8 

To read the release notes for the [new version of RealVNC Connect (v8), please click here](https://help.realvnc.com/hc/en-us/sections/26441433034013-RealVNC-Connect-v8).

This page records changes made to RealVNC Connect v7.13.1 and earlier.

To read the release notes for RealVNC Connect 7.14.0 and later, please refer to the [dedicated release pages here](https://help.realvnc.com/hc/en-us/sections/26441349091101-RealVNC-Connect-v7).

RealVNC Connect v7 consists of a RealVNC Server app for computers you want to control, a RealVNC Viewer app for devices you want to control from, and an online management portal. Where helpful, changes are identified by these categories.

# Where can I download the latest version? 

## Updating all RealVNC Connect apps (all versions) 

The quickest way to update your RealVNC Connect apps is to download and run the RealVNC Connect Installer which will update all RealVNC Connect apps:

  ------------------------------------------------------------------------------------------------------------------------
  [Download](https://www.realvnc.com/en/connect/download/)
  ------------------------------------------------------------------------------------------------------------------------

## Updating RealVNC Server and RealVNC Viewer individually (v7 only) 

If you are using RealVNC Connect v7 and want to download the latest version of RealVNC Viewer or RealVNC Server, please use the appropriate link below for the app you want to update:

  ----------------------------------------------------------------------------------------------------------------------------------------------
  [Download RealVNC Server](https://www.realvnc.com/en/connect/download/vnc/)
  [Download RealVNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)
  ----------------------------------------------------------------------------------------------------------------------------------------------

# December 2024 

## RealVNC Server 7.13.1 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   FIXED: An issue preventing concurrent session tracking from working reliably on newly installed and licensed RealVNC Servers has been resolved.

-   FIXED: RealVNC Server for Windows now correctly enforces policy settings when a policy-applied license key is reloaded. This was introduced in RealVNC Server 7.13.0.

## RealVNC Viewer 7.13.1 for desktop computers 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   FIXED: Active session icons are no longer shown for teams that are not billed per concurrent session.

# November 2024 

## RealVNC Server 7.13.0 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** RealVNC Server for macOS now supports audio playback when accessed from RealVNC Viewer on Windows, macOS and Linux. Requires macOS 13 or later.
-   IMPROVED: RealVNC Server's Information Center now shows a message when it detects the device it is running on is set to sleep automatically, which would prevent users from connecting to it.
-   IMPROVED: The hostname of the device is now displayed in the Diagnostics section of RealVNC Server's Information Center.
-   IMPROVED: The JOINCLOUD property for the RealVNC Server for Windows MSI installer no longer creates a duplicate entry for an already cloud-joined RealVNC Server.
-   IMPROVED: When using the -joincloud command to deploy a cloud connectivity token to RealVNC Server, it will check if it is already joined to the same team that the cloud connectivity token belongs to, to prevent duplicate entries being registered.
-   FIXED: An issue causing copy/paste (clipboard sharing) in RealVNC Viewer/Server to not work reliably has been resolved.
-   FIXED: When using the Chat feature, chat text no longer shows as light grey during an active connection.
-   FIXED: An issue causing RealVNC Server in User Mode to crash in rare cases has been resolved.
-   FIXED: Remote Printing is once again available when running RealVNC Connect on macOS Sonoma and later.
-   FIXED: An issue that caused RealVNC Server to crash when trying to check a CRL over HTTP with RealVNC Server's Certificate Authentication feature.

## RealVNC Viewer 7.13.0 for desktop computers 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW:** Shared Device Lists -- Create custom lists of devices that appear in RealVNC Viewer when using RealVNC Connect in an offline deployment. [Read more here](https://help.realvnc.com/hc/en-us/articles/360003502672-How-do-I-create-a-shared-device-list-in-RealVNC-Viewer).
-   **NEW:** When trialling RealVNC Connect, you can now request that On-Demand Assist is activated as part of your trial experience.
-   FIXED: An issue causing copy/paste (clipboard sharing) in RealVNC Viewer/Server to not work reliably has been resolved.
-   FIXED: The Online/Offline since column used by Presence once again updates correctly.
-   FIXED: RealVNC Viewer for macOS no longer closes unexpectedly when cycling through remote monitors when using RealVNC Viewer in fullscreen mode.
-   FIXED: Remote Printing is once again available when running RealVNC Connect on macOS Sonoma and later.
-   FIXED: When signing in to RealVNC Viewer, a dialog for SSO Sign-in would be shown incorrectly.
-   FIXED: File Transfer and Chat within an On-Demand Assist session are once again accessible after selecting a monitor.
-   FIXED: File sizes are now reported with more accuracy in the File Manager (e.g. 1.90GB is now shown as 1.90GB and not 1GB)
-   FIXED: An issue that would cause multi-window mode windows to open at an unexpected size has been resolved.

# September 2024 

## RealVNC Viewer for Android 4.9.2 

This is a release of RealVNC Viewer for Android devices you want to control from. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android).

-   FIXED: RealVNC Viewer correctly requests the Notifications permission to show a persistent notification while a connection to a VNC Server is in progress.
-   Updated SDK to target Android 14

## RealVNC Viewer for iOS 4.9.3 

This is a release of RealVNC Viewer for iOS devices, used to control remote devices running a VNC Server. [Get the app in the App Store](https://apps.apple.com/us/app/vnc-viewer/id352019548).

-   **NEW:** Added support for iOS/iPadOS 18, including support for Bluetooth keyboards.
-   FIXED: RealVNC Viewer will no longer unexpectedly close or sign users out when signed in using RealVNC Account SSO.

## RealVNC Server for Android 2.8.1 

This is a release of RealVNC Server for Android devices, to allow you to securely share your mobile device\'s screen with your IT technician or system administrator. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.server).

-   Updated SDK to target Android 14

# August 2024 

## RealVNC Server 7.12.1 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   IMPROVED: It is now possible to [configure the number of attempts RealVNC Server makes to contact a RADIUS Server](https://help.realvnc.com/hc/en-us/articles/360002253538-Setting-up-RADIUS-Authentication) before failing with 2 new parameters, `RadiusRequestPackets` and `RadiusPacketInterval`. This can be useful if your RADIUS Server is slow to respond to access requests.

## RealVNC Viewer 7.12.1 for desktop computers 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   FIXED: [Certificate authentication](https://help.realvnc.com/hc/en-us/articles/360002250377-Setting-up-Smartcard-Certificate-Store-Authentication) no longer fails when using RealVNC Viewer for macOS with certain certificate/smartcard combinations.

# July 2024 

## RealVNC Server for iOS 2.8.0 

This is a release of RealVNC Server for iOS devices, to allow you to securely share your mobile device\'s screen with your IT technician or system administrator. [Get the app in the App Store](https://apps.apple.com/gb/app/vnc-server/id1616886311).

-   **NEW:** Users receiving remote support can now see additional information about the technician connecting to their device to help verify the technician's identity.

-   **NEW:** Users can now report suspicious technicians to RealVNC by tapping the 'Report this user' button in the app.

-   FIXED: Bug fixes, security and stability improvements.

## RealVNC Server for Android 2.8.0 

This is a release of RealVNC Server for Android devices, to allow you to securely share your mobile device\'s screen with your IT technician or system administrator. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.server).

-   **NEW:** Users receiving remote support can now see additional information about the technician connecting to their device to help verify the technician's identity.

-   **NEW:** Users can now report suspicious technicians to RealVNC by tapping the 'Report this user' button in the app.

-   FIXED: Bug fixes, security and stability improvements.

# June 2024 

## RealVNC Server 7.12.0 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** You can now limit the maximum number of concurrent Virtual Mode sessions on a RealVNC Server host using the MaxDesktops parameter.
-   **NEW:** You can now retrieve a list of connected VNC Viewer users in RealVNC Server with the -getconnections argument. For example, on Windows, "C:\\Program Files\\RealVNC\\VNC Server\\vncserver.exe" -service -getconnections
-   IMPROVED: The RealVNC Server Diagnostics now show a specific message if direct connections have been disabled.

## RealVNC Viewer 7.12.0 for desktop computers 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW:** You can now drag application windows between RealVNC Viewer windows when using [Multi-Window mode](https://help.realvnc.com/hc/en-us/articles/360006483577-Working-with-multiple-monitors-in-RealVNC-Connect#viewing-multiple-monitors-multi-window-mode--0-2).
-   **NEW**: The toolbar that is displayed during a remote access session can now be pinned in place using the ToolbarPin parameter, found in the Expert section of RealVNC Viewer's Preferences.
-   **NEW**: It is now possible to send the clipboard content as keystrokes to a RealVNC Server. This is useful to "paste" text where standard clipboard pasting is unavailable, such as on the Windows logon screen. This feature is accessible via the F8 menu and can be configured using the ClipboardKeystrokesEnable parameter.
-   IMPROVED: The Session Information dialog now clearly shows whether a cloud connection is peer-to-peer or relayed.
-   IMPROVED: When connecting to a RealVNC Server configured to use [Interactive System Authentication](https://help.realvnc.com/hc/en-us/articles/360002250217-Setting-up-Interactive-System-Authentication), RealVNC Viewer will now correctly focus the appropriate button.
-   IMPROVED: Keyboard shortcuts for the menu items on the "F8 Menu", accessible during a remote access session, work correctly in all [supported locales](https://help.realvnc.com/hc/en-us/articles/7793055632541-Which-languages-are-supported-in-RealVNC-Connect).
-   FIXED: Resolved an issue where On-Demand Assist sessions could end unexpectedly while signed in to RealVNC Viewer with SSO.
-   FIXED: Address Book connections for a cloud-joined RealVNC Server no longer appear multiple times [in a group](https://help.realvnc.com/hc/en-us/articles/360005031717-Organizing-RealVNC-Viewer-connections#using-computer-groups-0-0).

## RealVNC Connect Setup 2.3.0 

This is a release of the RealVNC Connect Setup application. [Download](https://www.realvnc.com/en/connect/download/combined/).

-   FIXED: Resolved an issue that could cause a crash when clicking Launch at the end of the setup process.

 

# May 2024 

## RealVNC Server 7.11.1 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   FIXED: Resolved an issue that affected users running RealVNC Server 7.11.0 on macOS 12 (Monterey) where a black screen would display when connecting to RealVNC Server.

We're retiring RealVNC Connect Home subscriptions soon. [Click here to learn more](https://help.realvnc.com/hc/en-us/articles/17445613281309-RealVNC-Connect-Home-Subscriptions-Important-Information) about how this affects you.

## RealVNC Viewer 7.11.1 for desktop computers 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   FIXED: Resolved an issue where RealVNC Viewer could crash while signing in to your RealVNC Account using SSO.

We're retiring RealVNC Connect Home subscriptions soon. Click the \'Learn More\' link on the in-app banner to find out how this affects you.

## RealVNC Viewer for Android 4.9.1 

This is a release of RealVNC Viewer for Android devices you want to control from. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android).

We\'re retiring RealVNC Connect Home subscriptions soon. Click the \'Learn More\' link on the in-app banner to find out how this affects you.

## RealVNC Viewer for iOS 4.9.2 

This is a release of RealVNC Viewer for iOS devices, used to control remote devices running a VNC Server. [Get the app in the App Store](https://apps.apple.com/us/app/vnc-viewer/id352019548).

We\'re retiring RealVNC Connect Home subscriptions soon. Click the \'Learn More\' link on the in-app banner to find out how this affects you.

# April 2024 

## RealVNC Server 7.11.0 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** RealVNC Server for macOS now supports use of Apple's ScreenCaptureKit API for desktop capture, on macOS 13 and later.

-   **NEW:** RealVNC Server can now prevent the built-in Windows On-Screen Keyboard from being displayed to connected RealVNC Viewers. This can be enabled using the new Expert parameter `HideOSKWindow`.

-   **NEW:** The connection notification banner is now movable. Configure the banner's behaviour using the new parameter `ConnNotifyStyle` in the Expert section of RealVNC Server.

-   IMPROVED: The `-cloudstatus` command now includes the ID of the team that RealVNC Server is joined to.

-   IMPROVED: Re-introduced support for Windows Server 2012 following Microsoft's announcement to make Extended Security Updates (ESUs) available.

-   IMPROVED: `AlterShiftWithMods` is now available to be set in the Expert section of RealVNC Server's Options.

-   FIXED: The installation package for macOS now reports correct version information for patch/software management systems.

## RealVNC Viewer 7.11.0 for desktop computers 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW:** Added support for SSO sign-in (Entra ID/Azure AD) using your email address instead of an OIDC identifier.

-   **NEW:** Multi-Window Mode is now available on RealVNC Viewer for macOS. When connecting to devices with multiple monitors, you can now pop out each remote monitor into its own window in RealVNC Viewer.

-   IMPROVED: Screen recording in multi-window mode now only records the screen(s) that are being shown.

-   IMPROVED: Re-introduced support for Windows Server 2012 following Microsoft's announcement to make Extended Security Updates (ESUs) available.

-   FIXED: Resolved an issue with large groups of computers failing to load correctly.

-   FIXED: The installation package for macOS now reports correct version information for patch/software management systems.

## RealVNC Connect Setup 2.2.2 

This is a release of the RealVNC Connect Setup application. [Download](https://www.realvnc.com/en/connect/download/combined/).

-   FIXED: Resolved an issue that could cause a crash when clicking Launch at the end of the setup process.

## RealVNC Connect Portal 

We\'ve made the following improvements to the [RealVNC Connect Portal](https://manage.realvnc.com):

-   **NEW:** Customers with RealVNC Account SSO enabled can now [sign-in using the SSO button](https://help.realvnc.com/hc/en-us/articles/17984619082013-Signing-in-to-RealVNC-Connect-with-an-SSO-provider#realvnc-connect-portal-0-1) on the portal sign-in page.

# March 2024 

## RealVNC Viewer for Android 4.9.0 

This is a release of RealVNC Viewer for Android devices you want to control from. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android).

-   **NEW:** Added support for SSO sign-in using your email address instead of an OIDC identifier.\
    Please note, if you are currently signed in to RealVNC Viewer with an SSO account, you will need to sign-in again.

*KNOWN ISSUE: We are aware of an issue with SSO sign-in when using RealVNC Viewer in a Work Profile where if a web browser app is not available then the app will close. If you use a Work Profile and want to sign in using SSO, please ensure a web browser app is installed to the Work Profile.*

## RealVNC Viewer for iOS 4.9.0 

This is a release of RealVNC Viewer for iOS devices, used to control remote devices running a VNC Server. [Get the app in the App Store](https://apps.apple.com/us/app/vnc-viewer/id352019548).

-   NEW: Added support for SSO sign-in using your email address instead of an OIDC identifier.
-   FIXED: Bug fixes and stability improvements.\
    Please note, if you are currently signed in to RealVNC Viewer with an SSO account, you will need to sign-in again after updating to this version.

# February 2024 

## RealVNC Server 7.10.0 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW: Multi-Window Mode for Multi-Monitor Support**. When connected to a RealVNC Server with multiple monitors, you can now activate Multi-Window Mode in RealVNC Viewer on Windows and Linux. This lets you show each remote monitor in its own window, so you're free to arrange remote monitors to your liking, including displayed individually on connected local monitors. [Read more here](/hc/en-us/articles/360006483577#viewing-multiple-monitors-multi-window-mode--0-2). Note, if you license RealVNC Server offline, you will need to [apply an updated offline license](/hc/en-us/articles/360029797672) to enable this feature.
-   IMPROVED: Prevent file transfers from occurring at the lock screen in RealVNC Server for Windows. To enable this, use the DisableFileTransferAtLockScreen parameter found in the Expert section of RealVNC Server's Options.
-   FIXED: Resolved an issue in RealVNC Server for Linux that caused the PixelBuffer to be recreated continuously.
-   FIXED: RealVNC Server now runs correctly on 32-bit versions of Raspberry Pi OS Bookworm. Please note, this version removes the deprecated experimental "direct capture" option in RealVNC Server as Raspberry Pi OS no longer includes the libraries that made it possible.

## RealVNC Viewer 7.10.0 for desktop computers 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW: Multi-Window Mode for Multi-Monitor Support**. When connected to a RealVNC Server with multiple monitors, you can now activate Multi-Window Mode in RealVNC Viewer on Windows and Linux. This lets you show each remote monitor in its own window, so you're free to arrange remote monitors to your liking, including displayed individually on connected local monitors. [Read more here](/hc/en-us/articles/360006483577#viewing-multiple-monitors-multi-window-mode--0-2). Note, if you license RealVNC Server offline, you will need to [apply an updated offline license](/hc/en-us/articles/360029797672) to enable this feature.
-   FIXED: Resolved an issue preventing entry of your organisation\'s OIDC identifier for Azure AD SSO if an invalid OIDC identifier was set previously.

## RealVNC Server for iOS 2.7.0 

This is a release of RealVNC Server for iOS devices, to allow you to securely share your mobile device\'s screen with your IT technician or system administrator. [Get the app in the App Store](https://apps.apple.com/gb/app/vnc-server/id1616886311).

-   IMPROVED: Getting connected to a technician is easier than ever with a refreshed app design
-   FIXED: Bug fixes, security and stability improvements.

## RealVNC Server for Android 2.7.0 

This is a release of RealVNC Server for Android devices, to allow you to securely share your mobile device\'s screen with your IT technician or system administrator. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.server).

-   IMPROVED: Getting connected to a technician is easier than ever with a refreshed app design
-   IMPROVED: RealVNC Server for Android is now compatible with 32-bit Android devices
-   FIXED: Using the in-app copy button no longer causes the app to crash in some circumstances
-   FIXED: Bug fixes, security and stability improvements.

## RealVNC Viewer for Android 4.8.0 

This is a release of RealVNC Viewer for Android devices you want to control from. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android).

-   FIXED: Bug fixes, security hardening and stability improvements.

This version removes support for Android 7.

## RealVNC Viewer for iOS 4.8.0 

This is a release of RealVNC Viewer for iOS devices, used to control remote devices running a VNC Server. [Get the app in the App Store](https://apps.apple.com/us/app/vnc-viewer/id352019548).

-   FIXED: Bug fixes, security hardening and stability improvements.

# January 2024 

## RealVNC Server 7.9.0 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** File Manager - File Transfer now has a completely new look and a new name. The two-pane window in File Manager makes it easier than ever to transfer files and folders to and from remote devices, and you can even rename and delete files on your remote devices. [Read more here](https://help.realvnc.com/hc/en-us/articles/360002250477#using-file-manager-0-1).
-   **NEW:** RealVNC Server in Virtual Mode can now be started with session specific locations for configuration files, using the `VNC_PROFILE` and `VNC_CONFIG_PROFILE` environment variables. [Read more here](https://help.realvnc.com/hc/en-us/articles/360004324217#using-session-specific-configuration-0-4).
-   **NEW:** Added support for macOS Sonoma. Please note, there is a [known issue with the remote printing feature](/hc/en-us/articles/13986719562909) on macOS Sonoma.
-   IMPROVED: A new parameter, `KeyEventMethod`, has been added to RealVNC Server for macOS to allow RealVNC Server to use an alternate key injection method. This is only required if you see issues with key modifiers, such as Shift, not being passed through to macOS applications, like UTM.\
    Note, we are aware of an issue with the `IOHIDPostEvent` value not passing any key input to the login screen in macOS Sonoma and we are actively investigating.
-   IMPROVED: The MSI installers for RealVNC Server for Windows now support the MSI Properties `JOINCLOUD`, `JOINGROUP` and `JOINNAME` to join RealVNC Server to the cloud as part of the installation process. [Read more here](https://help.realvnc.com/hc/en-us/articles/360002250657#realvnc-server-0-5).

## RealVNC Viewer 7.9.0 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW:** File Manager - File Transfer now has a completely new look and a new name. The two-pane window in File Manager makes it easier than ever to transfer files and folders to and from remote devices, and you can even rename and delete files on your remote devices. [Read more here](https://help.realvnc.com/hc/en-us/articles/360002250477#using-file-manager-0-1).
-   **NEW:** Added support for macOS Sonoma. Please note, there is a [known issue with the remote printing feature](/hc/en-us/articles/13986719562909) on macOS Sonoma.
-   IMPROVED: A new parameter, `ColorSpaceRGB`, has been added to RealVNC Viewer for macOS to allow users to customise the color space used to render a remote computer\'s desktop.
-   IMPROVED: An updated splash screen is shown on first run after installing RealVNC Viewer using the RealVNC Connect Setup app.
-   FIXED: When using RealVNC Viewer with Azure AD SSO users will no longer see erroneous \"Access denied; please sign in\" messages intermittently when trying to connect to remote devices.
-   FIXED: RealVNC Viewer no longer crashes during an Azure AD SSO sign-in attempt if login.microsoftonline.com cannot be reached.
-   FIXED: RealVNC Viewer for macOS now correctly removes whitespace and newline characters from the connection address bar.
-   FIXED: Azure AD SSO now works correctly when using Firefox with RealVNC Viewer on Ubuntu.

# December 2023 

## RealVNC Connect API Gateway Service 

We\'ve made the following improvements to the [RealVNC API Gateway Service](https://docs.realvnc.com/api-access.html):

-   **NEW:** User Management - API endpoints have been added to allow you to invite and remove people from your Team, change Team member roles and update People Group membership.

## RealVNC Server for iOS 2.6.0 

This is a release of RealVNC Server for iOS devices, to allow you to securely share your mobile device\'s screen with your IT technician or system administrator. [Get the app in the App Store](https://apps.apple.com/gb/app/vnc-server/id1616886311).

-   **NEW:** Session Logging - Cloud connections made to RealVNC Server are now logged to the [RealVNC Connect Audit service](https://help.realvnc.com/hc/en-us/articles/10386546139805) and can be reviewed in the [RealVNC Connect portal](https://manage.realvnc.com/) and through [API Access](https://help.realvnc.com/hc/en-us/articles/6521249110685). *If you do not see Session Log information for your devices, please *[*contact our Sales team*](https://www.realvnc.com/en/contact-us/)* to discuss enabling it for your subscription.*
-   **NEW:** Added support for iOS 17.
-   IMPROVED: Improved MDM device management and device naming with the addition of the joinName parameter.
-   FIXED: Bug fixes and stability improvements

# November 2023 

## RealVNC Server for Android 2.6.0 

This is a release of RealVNC Server for Android devices, to allow you to securely share your mobile device\'s screen with your IT technician or system administrator. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.server).

-   **NEW:** RealVNC Server for Android now supports remote control! While a RealVNC Viewer is connected, tap the \"Enable RealVNC remote control\" button and follow the on-screen instructions. (Accessibility service required)
-   **NEW:** Session Logging - Cloud connections made to RealVNC Server are now logged to the [RealVNC Connect Audit service](https://help.realvnc.com/hc/en-us/articles/10386546139805) and can be reviewed in the [RealVNC Connect portal](https://manage.realvnc.com/) and through [API Access](https://help.realvnc.com/hc/en-us/articles/6521249110685). *If you do not see Session Log information for your devices, please *[*contact our Sales team*](https://www.realvnc.com/en/contact-us/)* to discuss enabling it for your subscription.*
-   **NEW:** Added support for Android 14.
-   CHANGED: The \"Disconnect all\" button that is displayed in the notification tray while a RealVNC Viewer is connected no longer asks for confirmation before disconnecting RealVNC Viewers.
-   IMPROVED: Improved MDM device management and device naming with the addition of the joinName parameter.
-   FIXED: Bug fixes and stability improvements.

## RealVNC Server 7.8.0 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** Session Logging - Cloud connections made to RealVNC Server are now logged to the [RealVNC Connect Audit service](https://help.realvnc.com/hc/en-us/articles/10386546139805) and can be reviewed in the [RealVNC Connect portal](https://manage.realvnc.com/) and through [API Access](https://help.realvnc.com/hc/en-us/articles/6521249110685). *If you do not see Session Log information for your devices, please *[*contact our Sales team*](https://www.realvnc.com/en/contact-us/)* to discuss enabling it for your subscription.*

## RealVNC Viewer 7.8.0 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   [IMPROVED: General bug fixes and performance improvements]

## RealVNC Connect Portal 

We\'ve made the following improvements to the [RealVNC Connect portal](https://manage.realvnc.com):

-   **NEW:** Session Logging - Cloud connections made to RealVNC Server are now logged to the [RealVNC Connect Audit service](https://help.realvnc.com/hc/en-us/articles/10386546139805) and can be reviewed in the [RealVNC Connect portal](https://manage.realvnc.com/) and through [API Access](https://help.realvnc.com/hc/en-us/articles/6521249110685). *If you do not see Session Log information for your devices, please *[*contact our Sales team*](https://www.realvnc.com/en/contact-us/)* to discuss enabling it for your subscription.*
-   IMPROVED: Additional page navigation controls (Next/Back) have been added to the Computers and People pages, and the page will now scroll back to the top after navigating.

# October 2023 

## RealVNC Connect Setup 2.2.1 

This is a release of the RealVNC Connect Setup application. [Download](https://www.realvnc.com/en/connect/download/combined/).

-   FIXED: The sign-in/sign-up process now works correctly when using Firefox on Ubuntu.

## RealVNC Connect Setup 2.2.0 

This is a release of the RealVNC Connect Setup application. [Download](https://www.realvnc.com/en/connect/download/combined/).

-   **NEW:** Improved sign-in and sign-up experience for first-time users that makes it easier than ever to get started. On initial install of RealVNC Connect, you can choose to sign into an existing account or sign up for a new one. After signing up/in, RealVNC Viewer and RealVNC Server will be automatically joined to your RealVNC Connect Team.

## RealVNC Server 7.7.0 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   IMPROVED: Behind the scenes changes to enable support for the RealVNC Connect Setup app\'s new online sign-in option.

Please note that this version removes support for Windows Server 2012 and Windows Server 2012 R2.

## RealVNC Viewer 7.7.0 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   IMPROVED: Behind the scenes changes to enable support for the RealVNC Connect Setup app\'s new online sign-in option.

Please note that this version removes support for Windows Server 2012 and Windows Server 2012 R2.

## RealVNC Viewer for Android 4.7.0 

This is a release of RealVNC Viewer for Android devices you want to control from. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android).

-   **NEW:** Added support for Android 14.
-   [IMPROVED: Performance improvements and bug fixes.]

## RealVNC Viewer for iOS 4.7.2 

This is a release of RealVNC Viewer for iOS devices, used to control remote devices running a VNC Server. [Get the app in the App Store](https://apps.apple.com/us/app/vnc-viewer/id352019548).

-   FIXED: Launching connections to remote devices via a link/URI no longer causes the app to close

## RealVNC Viewer for iOS 4.7.1 

This is a release of RealVNC Viewer for iOS devices, used to control remote devices running a VNC Server. [Get the app in the App Store](https://apps.apple.com/us/app/vnc-viewer/id352019548).

-   **NEW: **Added support for iOS 17.
-   FIXED: Issues searching for address book entries in large teams - this now requires you to hit \"search\" on the keyboard before a search is executed.
-   FIXED: Potential crashes with large teams in address book view.
-   FIXED: Potential crash on disconnect.
-   IMPROVED: Performance improvements and bug fixes.

Please note that this version removes support for iOS 13.

# September 2023 

## RealVNC Server 7.6.1 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   FIXED: RealVNC Viewer will no longer erroneously show the message \"VNC Viewer is not licensed to connect to this VNC Server\" when connecting to a RealVNC Server licensed with a Per User subscription plan.

-   IMPROVED: The RealVNC Server Licensing Wizard now includes the subscription plan type when multiple teams are available for the RealVNC Server to be joined to.

## RealVNC Viewer 7.6.1 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   FIXED: RealVNC Viewer will no longer erroneously show the message \"VNC Viewer is not licensed to connect to this VNC Server\" when connecting to a RealVNC Server licensed with a Per User subscription plan.

-   FIXED: RealVNC Viewer will no longer crash if your organisation\'s [Azure AD SSO](https://help.realvnc.com/hc/en-us/articles/5459490226333) OIDC identifier changes.

-   FIXED: Sorting of columns in the Address Book and other views is remembered between RealVNC Viewer application launches.

-   CHANGED: MaxServersToList is now available as an Expert parameter in RealVNC Viewer for easier configuration when using [RealVNC Viewer\'s Computer Group organisation feature](https://help.realvnc.com/hc/en-us/articles/360005031717#using-computer-groups-0-0).

# August 2023 

## RealVNC Server 7.6.0 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** Support for dynamic resolutions in Virtual Mode sessions, which allows RealVNC Server to dynamically change resolution to match the size of the connected RealVNC Viewer window.\
    Note that this feature also requires use of RealVNC Viewer 7.6.0 or later, and if [SystemXorg mode](https://help.realvnc.com/hc/en-us/articles/360003474752) is enabled, the [RealVNC dummy driver](https://help.realvnc.com/hc/en-us/articles/360016058212#realvnc-dummy-driver-0-3) must be installed.

-   IMPROVED: Application icons in RealVNC Connect for Windows are no longer blurry on devices using display scaling set above 100%.

-   FIXED: RealVNC Server for macOS no longer prompts to install Rosetta on M1/M2 macOS devices.

-   FIXED: It is possible to remove all access to RealVNC Server using the Remove button in RealVNC Server\'s Users & Permissions, instead of automatically reverting to the default access list (Administrators only).

-   FIXED: Configuring RealVNC Server to lock the screen when the last user disconnects now functions correctly on macOS Ventura.

## RealVNC Viewer 7.6.0 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW: **Presence status for [cloud-connected] RealVNC Servers is now available in RealVNC Viewer. Presence allows users to easily see the status of their devices, letting them know if they're online or not, before starting a connection to them.\
    *Please note that this feature is only available on certain subscription [plans]. If you do not see P[resence] information for your devices, please [contact our Sales team](https://www.realvnc.com/en/contact-us/) to discuss adding Presence to your subscription.*

-   **NEW:** RealVNC Viewer now shows cloud-connected RealVNC Servers in their groups, as configured in the [RealVNC Connect Portal].  For more information about this feature, [click here](https://help.realvnc.com/hc/en-us/articles/360005031717#using-computer-groups-0-0).

-   **NEW:** Support for dynamic resolutions in Virtual Mode sessions, which allows RealVNC Server to dynamically change resolution to match the size of the connected RealVNC Viewer window. Note that this feature also requires use of RealVNC Server 7.6.0 or later, and if [SystemXorg mode](https://help.realvnc.com/hc/en-us/articles/360003474752) is enabled, the [RealVNC dummy driver](https://help.realvnc.com/hc/en-us/articles/360016058212#realvnc-dummy-driver-0-3) must be installed.

-   IMPROVED: Application icons in RealVNC Connect for Windows are no longer blurry on devices using display scaling set above 100%.

-   IMPROVED: RealVNC Viewer now resumes active sessions faster when resuming from sleep/hibernation.

## RealVNC Connect Setup 2.1.0 

This is a release of the RealVNC Connect Setup application. [Download](https://www.realvnc.com/en/connect/download/combined/).

-   **IMPROVED:** RealVNC Connect Setup for Mac has a refreshed UI and user experience to provide a smoother installation of RealVNC Connect applications.

# July 2023 

## RealVNC Viewer for Android 4.6.1 

This is a release of RealVNC Viewer for Android devices you want to control from. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android).

-   **FIXED:** Bluetooth keyboard NumPad keys now work when using GBoard as the device\'s keyboard
-   IMPROVED: The toolbar can now be moved to a different corner of your device\'s screen
-   IMPROVED: The toolbar will fade if not interacted with after a short period
-   IMPROVED: Various improvements to enhance the stability of the app

This release also restores support for 32-bit Android devices.

## RealVNC Viewer for iOS 4.6.0 

This is a release of RealVNC Viewer for iOS devices, used to control remote devices running a VNC Server. [Get the app in the App Store](https://apps.apple.com/us/app/vnc-viewer/id352019548).

-   **NEW:** RealVNC Viewer will now respect the permission given by \"Paste from Other Apps\" permission dialog, on devices running iOS 16.1 onwards
-   FIXED: Click-and-drag events no longer accelerate desktop bump scrolling
-   FIXED: Restored mouse cursor inertia when controlling a desktop
-   IMPROVED: Improvements to enhance the stability of the app

# June 2023 

## RealVNC Server 7.5.1 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   FIXED: Users and groups can now be selected and managed again using the Users & Permissions section of VNC Server\'s Option UI.
-   FIXED: Individual custom permission check boxes can be toggled again in the Users & Permissions section of VNC Server\'s Option UI.

## RealVNC Viewer 7.5.1 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   FIXED: Resolved an issue that could cause issues in some areas of VNC Viewer\'s UI in rare cases.

## RealVNC Viewer for iOS 4.5.0 

This is a release of RealVNC Viewer for iOS devices, used to control remote devices running a VNC Server. [Get the app in the App Store](https://apps.apple.com/us/app/vnc-viewer/id352019548).

-   **CHANGED: **VNC Viewer has a new app name, RealVNC Viewer, as well as a new icon!
-   FIXED: The \"Forget OIDC identifier\" option now works correctly when signed in with an Azure AD SSO account
-   IMPROVED: Various improvements to enhance the stability of the app

## RealVNC Viewer for Android 4.5.0 

This is a release of RealVNC Viewer for Android devices you want to control from. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android).

-   **CHANGED:** VNC Viewer has a new name, RealVNC Viewer, as well as a new icon!
-   FIXED: Pressing backspace no longer sends double backspace events to the connected server, when using certain keyboard apps
-   FIXED: Zooming out no longer results in a zoomed-in, pixelated desktop
-   FIXED: The \"Forget OIDC\" option now works correctly when signed in with an Azure AD SSO account
-   IMPROVED: Various improvements to enhance the stability of the app

## RealVNC Server for iOS 2.5.0 

This is a release of RealVNC Server for iOS devices, to allow you to securely share your mobile device\'s screen with your IT technician or system administrator. [Get the app in the App Store](https://apps.apple.com/gb/app/vnc-server/id1616886311).

-   **CHANGED: **VNC Server has a new name, RealVNC Server, as well as a new icon!

## RealVNC Server for Android 2.5.0 

This is a release of RealVNC Server for Android devices, to allow you to securely share your mobile device\'s screen with your IT technician or system administrator. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.server).

-   **CHANGED: **VNC Server has a new name, RealVNC Server, as well as a new icon!

# May 2023 

## RealVNC Server 7.5.0 

This is a release of RealVNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **CHANGED:** VNC Server has a new name, RealVNC Server, as well as a new icon!
-   FIXED: Offline licenses applied by the License Wizard in RealVNC Server for Linux now have the correct file permissions.
-   FIXED: Applying an offline license file from a network share is now correctly processed by the Licensing Wizard.
-   FIXED: VNC Server on MacOS will now use system proxies that use a PAC file.

## RealVNC Viewer 7.5.0 

This is a release of RealVNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **CHANGED:** VNC Viewer has a new name, RealVNC Viewer, as well as a new icon!

## RealVNC Connect Setup 2.0.0 

This is a release of the RealVNC Connect Setup application. [Download](https://www.realvnc.com/en/connect/download/combined/).

-   **CHANGED:** The \"single installer\" for VNC Connect has a new name, RealVNC Connect Setup, as well as a new icon!
-   **IMPROVED:** RealVNC Connect Setup for Windows has a refreshed UI and user experience to provide a smoother installation of RealVNC Connect applications.

## VNC Server 7.2.0 - VNC Server 7.4.0 

Non-public releases

## VNC Viewer 7.2.0 - VNC Viewer 7.4.0 

Non-public releases

# April 2023 

## VNC Connect Portal 

We\'ve made the following improvements to the [VNC Connect portal](https://manage.realvnc.com):

-   **NEW:** The Audit feature in VNC Connect provides comprehensive logging for key events regarding your VNC Connect team, such as when users are added or removed from your team, and when [cloud connectivity tokens](/hc/en-us/articles/360005474138) are created or revoked. If your [subscription does not include Audit as standard](https://www.realvnc.com/en/connect/pricing), please [contact our Sales team](https://www.realvnc.com/en/contact-us/) to discuss adding it.\
    For more information about Audit, [click here](https://help.realvnc.com/hc/en-us/articles/10386546139805).
-   IMPROVED: Capacity information is now available on the Computers and People pages.

## VNC Server 7.1.0 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** VNC Server can now authenticate with Duo directly, with the new native Duo authentication scheme. To read more about this feature, [click here](https://help.realvnc.com/hc/en-us/articles/9730756848285).\
    Please note that this feature is only available on certain subscription types. If you do not see an option for Duo authentication in the Authentication dropdown in VNC Server\'s Options, [please contact our Sales team](https://www.realvnc.com/en/contact-us/) to discuss adding native Duo to your subscription.
-   **NEW**: A new parameter (SystemSleepBehavior) is available in VNC Server for macOS to control whether VNC Server prevents macOS from sleeping or not.
-   **NEW:** It is now possible to require the end user to accept screen recording attempts, using the RecordQuery parameter.
-   **FIXED**: VNC Server now correctly detects changes to connected monitors to update the [available monitor list](https://help.realvnc.com/hc/en-us/articles/360006483577) in VNC Viewer.
-   **FIXED**: The VNC Server tray icon is now hidden correctly for customers with the applicable license.
-   **IMPROVED:** VNC Server now returns a more specific error message when licensed with a per user subscription to older VNC Viewers that do not support this subscription model.
-   **CHANGED**: The Direct Capture option has been hidden on Raspberry Pi platforms that do not support it.
-   **REMOVED: **The **vncserver** symbolic link (symlink) will no longer be available by default. To launch Virtual Mode sessions, you will instead need to run the command, **vncserver-virtual**. [Learn more here](https://help.realvnc.com/hc/en-us/articles/10006324531741).

Please note that this version removes support for Windows 7, 8 and 8.1.

## VNC Viewer 7.1.0 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW**:  Monitor selection is now available using the VNC Viewer toolbar. See [this guide](https://help.realvnc.com/hc/en-us/articles/360006483577) for more information.
-   **FIXED**: An invalid offline license could prevent VNC Viewer from connecting to VNC Servers in some cases.
-   **IMPROVED: **The icons on the VNC Viewer session toolbar have been visually refreshed.

Please note that this version removes support for Windows 7, 8 and 8.1.

[March 2023]

## VNC Connect Portal 

We\'ve made the following improvements to the [VNC Connect portal](https://manage.realvnc.com):

-   **NEW:** Team Managers, Admins and Owners can now launch connections to computers from the Computers page. For more information, please see [this guide](https://help.realvnc.com/hc/en-us/articles/9987343661469).\
    Note: this feature requires VNC Viewer 6.22.826 or later.
-   CHANGED: The Account, Profile and Security pages have been moved from the left menu of the VNC Connect Portal and can now be accessed by using the person/profile icon in the top right.

## VNC Viewer for iOS 4.1.1 released 

This is a release of VNC Viewer for iOS devices, used to control remote devices running a VNC Server. [Get the app in the App Store](https://apps.apple.com/us/app/vnc-viewer/id352019548).

-   **NEW:** Support for Apple-branded and third-party bluetooth mice and trackpads.
-   FIXED: Improved performance when searching in large teams.
-   FIXED: Issues that could lead the app to crash have been resolved.

# February 2023 

## VNC Viewer for Android 4.1.0 released 

This is a release of VNC Viewer for Android devices you want to control from. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android).

-   **NEW:** The toolbar available during a remote access session has been replaced by a floating toolbar.
-   FIXED: Issues that could lead the app to crash have been resolved.
-   SECURITY: Improved security hardening

## VNC Server 7.0.1 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **FIXED: **[Monitor selection](https://help.realvnc.com/hc/en-us/articles/360006483577) is now possible again for Professional and Enterprise subscription holders.

## VNC Viewer 7.0.1 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **FIXED:** VNC Viewer no longer crashes on startup if the AllowSignIn parameter is disabled.

# January 2023 

## VNC Server 7.0.0 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **CHANGED:** VNC Server now uses a new format for offline licensing. VNC Server 7.x will continue to work with your VNC Server 6.x offline license key, up until the expiry date of the key. After this, you will need to apply the new format offline license. [Click here](https://help.realvnc.com/hc/en-us/articles/360029797672) to learn more.
-   **CHANGED:** VNC Server 7.x will not enforce a policy-applied VNC Server 6.x offline license key. To enforce licensing through policy, you must deploy the new format VNC 7.x offline license. [Click here](https://help.realvnc.com/hc/en-us/articles/360002250797) to learn more.
-   **CHANGED:** \'Instant Support\' is now \'On-Demand Assist\'. [Click here](https://help.realvnc.com/hc/en-us/articles/8702708653213) to learn more.
-   **CHANGED:** The VNC® Connect Home plan has been replaced with our new VNC® Connect Lite plan. It\'s still free, but you now get up to 256-bit encryption as well as high-speed streaming, for up to 3 devices.
-   **NEW:** VNC Server is now available as a Universal app on macOS, with native support for M1/M2 Macs.
-   FIXED: Audio is now available again when connecting to Ubuntu 22.04.1 (all modes) and CentOS/RHEL 7/8 (Virtual Mode).
-   FIXED: Chat text not visible when using Dark Mode on macOS.
-   FIXED: RADIUS authentication is now possible without mapping to system accounts, by enabling the [advanced parameter](https://help.realvnc.com/hc/en-us/articles/360002253878), RadiusAllowNonSystemUser. Note, this bypasses VNC Server\'s Users & Permissions feature and passes responsibility of required user authentication and verification to your RADIUS implementation.
-   REMOVED: Legacy ADM templates are no longer provided for VNC Server. ADMX templates continue to be available on the [Download page of the RealVNC website](https://www.realvnc.com/en/connect/download/vnc/).

Please note that this version removes support for macOS Catalina (10.15) and 32-bit Linux (x86).

## VNC Viewer 7.0.0 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **CHANGED:** \'Instant Support\' is now \'On-Demand Assist\'. [Click here](https://help.realvnc.com/hc/en-us/articles/8702708653213) to learn more.

-   **CHANGED:** The VNC® Connect Home plan has been replaced with our new VNC® Connect Lite plan. It\'s still free, but you now get up to 256-bit encryption as well as high-speed streaming, for up to 3 devices.

-   **NEW:** Users on *per user* priced plans will need to license VNC Viewer. This can be achieved by signing in or applying an offline license. [Click here](https://help.realvnc.com/hc/en-us/articles/360002249677) to learn more.

-   **NEW**: VNC Viewer is now available as a Universal app on macOS, with native support for M1/M2 Macs.

-    **NEW**: Added a button to save Session Information dialog to a text file.

-    FIXED**:** Ability to use Ctrl-Click as a \"right-click\" to access the sidebar context menu fixed on Ubuntu 22.04 and Mac M1.

-    FIXED: The sign-in dropdown menu no longer remains visible when moving the VNC Viewer application window.

-    FIXED: \'Top\' and \'Bottom\' options on the scrollbar \"right-click\" menu now move the position of the scrollbar as expected.

-   REMOVED**:** Legacy ADM templates are no longer provided for VNC Viewer. ADMX templates continue to be available on the [Download page of the RealVNC website](https://www.realvnc.com/en/connect/download/viewer/).

Please note that this version removes support for macOS Catalina (10.15) and 32-bit Linux (x86).

## VNC Viewer for iOS 4.0.1 released 

This is a release of VNC Viewer for iOS devices, used to control remote devices running a VNC Server. [Get the app in the App Store](https://apps.apple.com/us/app/vnc-viewer/id352019548).

-   CHANGED: \'Instant Support\' is now \'On-Demand Assist\'. [Click here](https://help.realvnc.com/hc/en-us/articles/8702708653213) to learn more.
-   CHANGED: The VNC® Connect Home plan has been replaced with our new VNC® Connect Lite plan.
-   FIXED: Accessibility - Application responds to the user\'s text size preferences.

Please note that this version removes support for iOS 9, iOS 10 and iOS 11.

## VNC Viewer for Android 4.0.1 released 

This is a release of VNC Viewer for Android devices you want to control from. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android).

-   CHANGED: \'Instant Support\' is now \'On-Demand Assist\'. [Click here](https://help.realvnc.com/hc/en-us/articles/8702708653213) to learn more.
-   CHANGED: The VNC® Connect Home plan has been replaced with our new VNC® Connect Lite plan.

## VNC Server for iOS 2.0.1 released 

This is a release of VNC Server for iOS devices, to allow you to securely share your mobile device\'s screen with your IT technician or system administrator. [Get the app in the App Store](https://apps.apple.com/gb/app/vnc-server/id1616886311).

-   CHANGED: \'Instant Support\' is now \'On-Demand Assist\'. [Click here](https://help.realvnc.com/hc/en-us/articles/8702708653213) to learn more.
-   CHANGED: The VNC® Connect Home plan has been replaced with our new VNC® Connect Lite plan.
-   FIXED: Accessibility - Application responds to the user\'s text size preferences.

## VNC Server for Android 2.0.1 released 

This is a release of VNC Server for Android devices, to allow you to securely share your mobile device\'s screen with your IT technician or system administrator. [Get the app in the Play Store](https://play.google.com/store/apps/details?id=com.realvnc.server).

-   CHANGED: \'Instant Support\' is now \'On-Demand Assist\'. [Click here](https://help.realvnc.com/hc/en-us/articles/8702708653213) to learn more.
-   CHANGED: The VNC® Connect Home plan has been replaced with our new VNC® Connect Lite plan.

# November 2022 

## VNC Viewer for iOS 3.10.0 released 

This is a release of VNC Viewer for iOS devices, used to control remote devices running a VNC Server. Search "RealVNC" in the App Store.

-   **NEW:** Sign-in with your Azure AD organisation: VNC Viewer for Mobile now supports VNC Connect\'s Azure AD SSO. [Contact us to find out more!](https://www.realvnc.com/en/contact-us/)
-   **NEW:** Added support for iOS/iPadOS 16.
-   FIXED: VNC Viewer now correctly uses UK layout on soft keyboard instead of US layouts when the device is configured to use a UK keyboard layout.
-   SECURITY: Improved security hardening and internal dependency updates.

## VNC Viewer for Android 3.8.0 released 

This is a release of VNC Viewer for Android devices you want to control from. Search 'RealVNC' in the Play Store.

-   **NEW:** Sign-in with your Azure AD organisation: VNC Viewer for Mobile now supports VNC Connect\'s Azure AD SSO. [Contact us to find out more!](https://www.realvnc.com/en/contact-us/)
-   **NEW:** Added support for Android 13.
-   FIXED: Logs are now attached correctly when using the \"Email technical support\" option on Android 11 and later.
-   FIXED: A grid overlay is no longer visible on high resolution devices running Android 12 and later.
-   IMPROVED: Bluetooth/physical keyboards can now be used to search for computers in the Address Book.
-   CHANGED - URI handlers have been changed to improve security, to prevent snooping. URI handlers no longer accept credentials (username/password).
-   SECURITY: Improved security hardening and internal dependency updates.

Please note that this version removes support for Android 6, as well as 32-bit Android devices.

# September 2022 

## VNC Server 6.11.0 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** Software screen blanking support for Windows 10 build 2004 onwards, including a new privacy mode status indicator and per-user screen blanking. Find out more here: [Can I blank the screen of a remote computer while I\'m connected to it?](/hc/en-us/articles/360016511452)

-   **NEW:** -cloudstatus command line parameter to fetch the cloud connectivity status of VNC Server.

-   **NEW:** Added the AlwaysShowCursor parameter to VNC Server for Windows. Enable this parameter to display a mouse cursor icon in VNC Viewer rather than a dot for systems where no mouse is detected.

-   IMPROVED: The \"Create a debug log file\" option in VNC Server\'s Options - Troubleshooting section now continues to log important events, such as connections, separately to EventLog (Windows) and syslog (MacOS and Linux).

-   FIXED: The VNC Server License Wizard now starts correctly when VNC Server is installed in a Remote Desktop (RDP) session.

-   FIXED: Windows 11 is now reported correctly in the VNC Server Diagnostics and log files.

-   FIXED: [QueryConnect](https://help.realvnc.com/hc/en-us/articles/360002250457) now works correctly when the remote Linux computer is at the login screen.

-   SECURITY: Fixed a local privilege escalation in Windows caused by MSI installer Repair mode.

-   SECURITY: VNC Passwords are now stored as an irreversible salted hash, where available.

-   SECURITY: Updated internal dependencies.

Please note that this version removes support for MacOS 10.14 Mojave.

## VNC Viewer 6.22.826 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW:** URI schema support for automatically launching and starting Viewer connections to Servers. Find out more here: [Can I launch VNC Viewer from a web page or program using URIs?](/hc/en-us/articles/6449870411037)

-   **NEW:** Screen recording is now available in VNC Viewer for Raspberry Pi.

-   IMPROVED: VNC Viewer now correctly scales the image when connecting to device with a large resolution portrait display.

-   FIXED: A timeout during an SSO login attempt could cause VNC Viewer to crash.

-   FIXED: VNC Viewer now shows an appropriate message for SSO accounts that have an expired token e.g. when using periodic re-authentication through Azure Conditional Access.

-   SECURITY: Fixed a local privilege escalation in Windows caused by MSI installer Repair mode.

Please note that this version removes support for MacOS 10.14 Mojave.

# August 2022 

## VNC Server for Mobile now available in VNC Connect! 

The VNC® Server mobile app from RealVNC® lets you securely share your mobile device's screen with your IT technician or system administrator in just a few taps. The app is available for Android and iOS/iPadOS. Read the FAQs here: [VNC Server for Mobile - FAQs](/hc/en-us/articles/5518809415453)

There are two ways to start a remote session:

-   INSTANT SUPPORT lets you set up a session in a flash using a secure one-time code that's unique to your session. This option is available on VNC® Connect Professional and Enterprise Instant Support plans.
-   DEVICE ACCESS lets IT teams pre-license a managed mobile device against their VNC Connect account. A session can be started without a session code, but the device holder still needs to authenticate the session. This option is available only on VNC® Connect Enterprise Device Access plans.

### Key Features 

-   Privacy with end-to-end encryption on all remote sessions.
-   Fast, effortless connections using RealVNC's secure cloud service.
-   Protection from unwanted access with end-user connection approval.
-   Free, paid and trial VNC Connect subscriptions available.

## VNC Server 6.10.1 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   FIXED: VNC Server started in User Mode and Virtual Mode used the [default permissions](https://help.realvnc.com/hc/en-us/articles/360002253618#understanding-pre-registered-user-accounts-and-groups-0-0) for Service Mode. This has been corrected to only allow access from the user account that started the VNC Server by default.

# June 2022 

## VNC Server 6.10.0 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** Added support for Ubuntu 22.04, RHEL/CentOS 9 and Windows Server 2022.

-   IMPROVED: VNC Server better handles resuming from hibernation/low power states and re-establishes cloud connectivity in a shorter time.

-   IMPROVED: VNC Server on Windows can accept an increased number of simultaneous connections from audio-enabled VNC Viewers.

-   IMPROVED: Diagnostics now lists detected audio devices.

-   FIXED: CREATOR OWNER account now works correctly when added to VNC Server\'s Users and Permissions.

-   FIXED: Running VNC Server in User Mode could prevent subsequent use of Service Mode.

-   FIXED: Group Policy refreshes/updates could interrupt active connections from VNC Viewers.

-   REMOVED: \"Test Direct Connection\" functionality from VNC Server\'s Diagnostics. RealVNC strongly recommend using [VNC Connect\'s cloud connectivity](https://help.realvnc.com/hc/en-us/articles/360002249737) for connections over the Internet.

-   SECURITY: Improved security hardening and internal dependency updates.

Please note that this version removes support for Ubuntu 16.04.

## VNC Viewer 6.22.515 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW:** Sign-in with your Azure AD organisation - VNC Connect now supports federated authentication for RealVNC accounts. [Contact us to find out more!](https://www.realvnc.com/en/contact-us/)

-   **NEW:** Added support for Ubuntu 22.04, RHEL/CentOS 9 and Windows Server 2022.

-   IMPROVED: The Preferences window now defaults to the Privacy tab.

-   IMPROVED: AudioVolume now available for control via policy.

-   SECURITY: Improved security hardening and internal dependency updates.

Please note that this version removes support for Ubuntu 16.04.

# April 2022 

## VNC Server 6.9.1 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   SECURITY: Fixed a local privilege escalation via MSI installer on Windows.

## VNC Viewer 6.22.315 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   FIXED: Saved passwords and the Master Password feature were not working correctly for some users after upgrading to VNC Viewer 6.22.207 from an earlier version of VNC Viewer.

# March 2022 

## VNC Server 6.9.0 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW**: Added support for Raspberry Pi OS Bullseye, 32-bit and 64-bit.
-   IMPROVED: VNC Server\'s License Wizard has been updated to allow users to configure essential settings during first time setup including Authentication, Encryption and Access Control.
-   IMPROVED: Specific events are now logged to Event Viewer/syslog when screen recording is started and stopped during a remote access session.
-   FIXED: VNC Server will now automatically use polling when DirectX failures are detected with portrait displays on Windows 11.
-   FIXED: DisconnectAction now works as expected when running VNC Server on macOS Big Sur and Monterey.
-   FIXED: Multiple keyboard layouts were not detected when running VNC Server 6.8.0 on Linux.
-   CHANGED: Default permissions for VNC Server have been changed from \"Administrative\" to \"Normal\".\
    **Please note that when upgrading, if you have enabled [QueryConnect](https://help.realvnc.com/hc/en-us/articles/360002250457) and have not changed your VNC Server\'s Permissions from the default value, your connections will now be required to be accepted by an end user on the remote computer.**
-   SECURITY: Fixed a local privilege escalation security issue affecting VNC Server installations on Linux.

Please note that this version removes support for Raspberry Pi OS (formerly Raspbian) Stretch 9.

## VNC Viewer 6.22.207 released 

**This version has been replaced by VNC Viewer 6.22.315.**

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW**: Added support for Raspberry Pi OS Bullseye, 32-bit and 64-bit.
-   **NEW**: Screen recording can now be started and stopped using the F8 menu in VNC Viewer.
-   **NEW**: New parameter for session recording, SessionRecordNewFileOnIncrease. This controls whether a new video file should be started when the screen resolution increases or not.
-   IMPROVED: The splash screen shown when running VNC Viewer for the first time has been updated.

Please note that this version removes support for Raspberry Pi OS (formerly Raspbian) Stretch 9.

# November 2021 

## VNC Viewer 6.21.1109 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   FIXED: Opening the chat window to send messages to a user on the server could prevent any control of the remote computer desktop.

## VNC Viewer for iOS 3.9.4 released 

This is a release of VNC Viewer for iOS devices, used to control remote devices running a VNC Server. Search "RealVNC" in the App Store.

-   FIXED: Bluetooth keyboards not working with VNC Viewer on iOS 15.

# October 2021 

## VNC Server 6.8.0 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** Screen Recording for computers running VNC Server 6.8.0+ and VNC Viewer 6.21.920+ with a Professional or Enterprise subscription.
-   **NEW:** Added support for Windows 11, MacOS Monterey and SUSE Linux Enterprise 15.
-   **NEW:** Dark mode support for MacOS.
-   **NEW:** VNC Viewer can now send the connection password to a VNC Server on Windows that is at the login screen. This is useful for users that are using System Authentication to authenticate to VNC Server and saves typing in the password again, after connecting. This feature is accessible via the F8 menu for the first 30 seconds of the session.
-   **NEW:** WinSSOAccountCheck parameter added to VNC Server on Windows to allow relaxing of Windows account status checks when authenticating via SSO. This may be useful if connecting VNC Viewer users are experiencing problems authenticating to VNC Server.
-   FIXED: VNC Server attempted to bind to invalid subnets for UDP TURN, causing VNC Server to log \"TurnDgram: Received ChannelBind error (code=403)\". This error will now only appear for unexpected TURN channel bind errors.
-   FIXED: Users would receive an \"Access is Denied\" error when they are part of the BuiltIn\\Adminstrators group when NTLogonAsInteractive is enabled.
-   IMPROVED: Removed extra logging that was printed to stdout when starting a Virtual Mode VNC Server on Linux with SystemXorg enabled.

Please note that this version removes support for MacOS High Sierra (10.13.x) and earlier, RHEL 6.x and CentOS 6.x.

## VNC Viewer 6.21.920 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW:** Screen Recording for computers running VNC Server 6.8.0+ and VNC Viewer 6.21.920+ with a Professional or Enterprise subscription.
-   **NEW:** Added support for Windows 11, MacOS Monterey and SUSE Linux Enterprise 15.
-   **NEW:** Dark mode support for MacOS.
-   **NEW:** VNC Viewer can now send the connection password to a VNC Server on Windows that is at the login screen. This is useful for users that are using System Authentication to authenticate to VNC Server and saves typing in the password again, after connecting. This feature is accessible via the F8 menu for the first 30 seconds of the session.
-   **NEW:** Added support for middle button press from laptops.

Please note that this version removes support for MacOS High Sierra (10.13.x) and earlier, RHEL 6.x and CentOS 6.x.

# May 2021 

## VNC Viewer 6.21.406 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. 

-   **NEW:** Added ability to sort connections using the Label column in Details View, so you can easily find servers that you have not yet labelled.
-   **NEW:** Added access to the context menu for search results. This can be shown by right clicking on a search result and allows you to change connection properties and add labels.

# March 2021 

## VNC Server 6.7.4 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/en/connect/download/vnc/).

-   **NEW:** Added ProxyAutoConfig parameter to specify a proxy-auto configuration (PAC) script on Windows.
-   **NEW**: Added support for MacOS Big Sur.
-   FIXED: Potential crashes when using new 10-bit color depth displays on Mac.

## VNC Viewer for Android 3.7.1 released 

This is a release of VNC Viewer for Android devices you want to control from. Search 'RealVNC' in the Play Store.

-   FIXED: When searching for servers in a large team the search results may have been incomplete.
-   CHANGED: You must now press the Search/Enter button on your keyboard after typing your search term to perform the search.

<div>

-    

</div>

# February 2021 

## VNC Viewer for Android 3.7.0 released 

This is a release of VNC Viewer for Android devices you want to control from. Search 'RealVNC' in the Play Store.

-   NEW: Added support for Android 10 (Android Q).
-   FIXED: Searching by name for computers in your Teams.

Please note that this version removes support for Android 5.x and earlier.

# January 2021 

## VNC Viewer 6.21.118 released 

This is a release of VNC Viewer for Mac computers you want to exercise control from. [[Download](https://www.realvnc.com/en/connect/download/viewer/ "https://www.realvnc.com/en/connect/download/viewer/")].

-   **NEW**: Added support for MacOS Big Sur.
-   FIXED: Possible VNC Viewer crashes on Macbook Air M1 and Macbook Pro M1 when connecting to other computers. 

# December 2020 

## VNC Server 6.7.3 released 

Non-public release.

# November 2020 

## VNC Viewer for iOS 3.9.3 released 

<div>

This is a release of VNC Viewer for iOS devices, used to control remote devices running a VNC Server. Search "RealVNC" in the App Store.

-   **NEW**: You will see a prompt on your screen to help VNC Viewer discover VNC services through the local network. This access will allow you to connect to VNC Servers.
-   FIXED: Bluetooth keyboards not working with VNC Viewer on iOS 14.
-   FIXED: Potential crashes during account login on iOS 14.
-   IMPROVED: Added support for dark mode on iOS 13+.

</div>

# August 2020 

## VNC Viewer 6.20.817 released 

This is a release of VNC Viewer for Mac computers you want to exercise control from. [[Download](https://www.realvnc.com/connect/download/viewer/ "https://www.realvnc.com/connect/download/viewer/")].

-   FIXED: an issue with the VNC Viewer showing a black screen on MacOS Big Sur.

# June 2020 

## VNC Server 6.7.2 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/en/connect/download/vnc/).

-   **NEW: **DxBadFormat parameter to allow working around misreported DirectX desktop duplication format.
-   FIXED: an issue preventing connections to VNC Server in some circumstances with audio enabled.
-   FIXED: Networking issue which can cause fallback to TCP connections.

## VNC Viewer 6.20.529 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   FIXED: Possible crashes on Linux when SendPrimary parameter is set.
-   FIXED: High-speed streaming and audio connections failures under certain networking conditions.

# April 2020 

## VNC Connect Portal 

We\'ve made the following usability improvements to the VNC Connect portal:

-   The **People** and **Computer** lists are now paginated with Next and Back buttons
-   Both **People** and **Computer** *groups* now appear on their own page under the **People** and **Computer** navigation bar items
-   A search box has been added to the **Computers** and **People** page if there are over 150 objects in the list
-   Bulk team invites - up to 250 email addresses can be invited to a team (and optionally added to a group) at once

## Cloud Services 

To best support VNC Connect customers worldwide and accommodate new growth and demand, we\'re making the following change to our cloud services:

-   small increase in the polling interval for the Directory service

This will mean changes to team computers (addition, removal, rename) and synchronized address books may appear in VNC Viewer a little slower.\
\
This change will be rolled out to clients over the next 28 days.

We do not expect these changes to have significant impact on the end user experience but wanted to make you aware.

# February 2020  

## VNC Server 6.7.1 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/en/connect/download/vnc/).

-   FIXED**:** Potential Server crash when using multiple monitors.

# January 2020  

## VNC Server 6.7.0 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/en/connect/download/vnc/).

-   **NEW**: Use VNC Viewer to control which monitor is displayed. (requires VNC Viewer 6.20.113 or later). Press F8 while connected to your VNC Server to access the \"Select monitor\" menu.
-   **NEW**: Support for High Speed Streaming and Audio when connecting to Virtual Mode sessions via the Virtual Mode Daemon (vncserver-virtuald).
-   **NEW**: Added support for Windows Server 2019 and CentOS/RHEL 8.
-   **NEW**: VNC Server will now additionally log to a file at info level (30) by default, in addition to EventLog/syslog logging at audit level (10).
-   **NEW**: Add a button to test/refresh connectivity between VNC Server and RealVNC\'s Cloud.
-   **NEW**: Advanced parameters can now be set via the Expert tab in VNC Server\'s Options*.* This will typically be used with instruction from RealVNC Support when troubleshooting an issue.
-   IMPROVED: Better setup experience for users when remotely installing VNC Server on Windows
-   IMPROVED: VNC Server will recommend testing screen blanking before it is enabled​.

## VNC Viewer 6.20.113 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW**: Use VNC Viewer to control which remote monitor is displayed by VNC Server (requires VNC Server 6.7.0 or later). Press F8 while connected to your VNC Server to access the \"Select monitor\" menu.
-   **NEW**: Added support for Windows Server 2019 and CentOS/RHEL 8.
-   **NEW**: VNC Viewer will now log to a file at info level (30) by default, in addition to EventLog/syslog logging at audit level (10).
-   **NEW**: Advanced parameters can now be set via the Expert tab in VNC Server\'s Options*.* This will typically be used with instruction from RealVNC Support when troubleshooting an issue.
-   FIXED: Desktop toolbar should no longer keep focus when interacting with it.
-   FIXED: A silent crash could occur on Windows 10 when launching connections from the address book.
-   FIXED: A silent crash could occur on Windows 10 launching instant support sessions.
-   FIXED: Crash on connection to AMX touch panel from Linux.

# November 2019 

<div>

## VNC Connect Portal updated 

<div>

-   The correct customer reference number of a subscription is now displayed following reactivation.
-   When purchasing a new subscription, customers are now prompted if they have existing trials or recently (within 30 days) expired teams.
-   Improved Address Verification System error handling when adding a credit card to a subscription. 
-   Improvements to the Team switcher:
    -   Picker reduced to 5 teams with a \"show more\" button
    -   Team status (Active, Expired, Cancelled) displayed in the \"Your teams\" list 
    -   Recently expired (within 30 days) teams are highlighted
-   Allow self-service payment method removal.

</div>

</div>

## VNC Viewer 6.19.1115 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   FIXED: Out of order UDP packets causing "assertion failed" error

# October 2019 

## VNC Viewer for iOS 3.8.1 released 

This is a release of VNC Viewer for iOS devices you want to control from. Search 'RealVNC' in the App Store.

-   FIXED: Various crash fixes and backgrounding behavior affecting iOS 13
-   FIXED: IPv6 domain resolution for RealVNC Cloud Services for affected ISPs
-   IMPROVED: Help menu now redirects to: help.realvnc.com

## VNC Viewer for Android 3.6.1 released 

This is a release of VNC Viewer for Android devices you want to control from. Search 'RealVNC' in the Play Store.

-   FIXED: IPv6 domain resolution for RealVNC Cloud Services for affected ISPs
-   IMPROVED: Help menu now redirects to: help.realvnc.com

# September 2019 

## VNC Server 6.6.0 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** High-quality audio streaming for computers running VNC Server 6.6.0+ with a Professional or Enterprise subscription, for a fully immersive remote access experience.
-   Added support for MacOS Catalina.

## VNC Viewer 6.19.923 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW:** High-quality audio streaming for devices running VNC Server 6.6.0+ with a Professional or Enterprise subscription, for a fully immersive remote access experience.
-   Added support for MacOS Catalina.

[]

# August 2019 

## VNC Server 6.5.0 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** Support High-speed streaming even when peer-to-peer connectivity is not available via a new UDP relay service.
-   Improve reliability of connection establishment.
-   Improve performance particularly in scenarios with high packet loss and latency.
-   Improve detection of display capture failures on Windows, switching to an alternative capture method where possible.
-   Improve styling of the menu bar icon on Mac to better match the system theme.
-   Add the ability to limit display capture to a single monitor on Linux using the "Monitor" parameter.

## VNC Viewer 6.19.715 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW**: Support for High-speed streaming even when peer-to-peer connectivity is not available via a new UDP relay service.
-   Improve reliability of connection establishment.
-   Improve performance particularly in scenarios with high packet loss and latency.

[]

# April 2019 

## VNC Viewer 6.19.325 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   In order to connect to remote computers, you must enter two separate sets of credentials; your RealVNC account email address and password to sign in, and then the system (username and) password expected by VNC Server to authenticate. It should now be clearer which set you have to enter when.
-   FIXED: Usernames that contain [`$`] are now saved correctly.
-   FIXED: Holding down SHIFT or CTRL while pressing a mouse button now affects remote Linux computers running the Gnome 3 desktop environment correctly.
-   FIXED: Under Windows, VNC Viewer no longer captures mouse movements when it is not the active desktop window.

[]

# March 2019 

## VNC Server 6.4.1 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   The License Wizard user interface has changed, to make licensing by signing in to your RealVNC account more prominent. If you have an Enterprise subscription and want to enter a license key via the Wizard, click the **Register offline** button. [More information](https://help.realvnc.com/hc/en-us/articles/360002249677).
-   The [`ShowCloudHints`] VNC Server parameter has been deprecated. You can remove sign in links from the VNC Server status dialog by setting [AllowCloudRfb](https://help.realvnc.com/hc/en-us/articles/360002251297) to [`FALSE`] instead.

## VNC Viewer for Android 3.5.0 released 

This is a release of VNC Viewer for Android devices you want to control from. Search 'RealVNC' in the Play Store.

-   **NEW:** High-speed streaming for connections to computers running VNC Server 6.4+ with a Professional or Enterprise subscription, for up to four times the screen refresh rate without compromising on picture quality.
-   **NEW:** Establish a direct connection to a remote computer using the URI syntax [`vnc://username:password@host:port`]. If the username and password are omitted, the connecting user is prompted to supply credentials.
-   In order to connect to remote computers, you must enter two separate sets of credentials; your RealVNC account email address and password to sign in, and then the system (username and) password expected by VNC Server to actually authenticate. It should now be clearer which set you have to enter when.
-   FIXED: Usernames that contain [`$`] are now saved correctly.

## VNC Viewer for iOS 3.7.0 released 

This is a release of VNC Viewer for iOS devices you want to control from. Search 'RealVNC' in the App Store.

-   **NEW:** High-speed streaming for connections to computers running VNC Server 6.4+ with a Professional or Enterprise subscription, for up to four times the screen refresh rate without compromising on picture quality.
-   **NEW:** A floating, flickable toolbar is available on all devices.
-   In order to connect to remote computers, you must enter two separate sets of credentials; your RealVNC account email address and password to sign in, and then the system (username and) password expected by VNC Server to actually authenticate. It should now be clearer which set you have to enter when.
-   FIXED: Usernames that contain [`$`] are now saved correctly.

------------------------------------------------------------------------

[]

# January 2019 

## VNC Server 6.4.0 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** High-speed streaming (first release) \
    If you have a Professional or Enterprise subscription, benefit from a significant performance improvement without compromising on picture quality, especially for graphically-intensive operations over slow links. [More information](https://www.realvnc.com/connect/performance).
-   **NEW:** Ensure cloud connections are all peer-to-peer, so no session data is sent via the cloud. [More information](https://help.realvnc.com/hc/en-us/articles/360002251297).
-   **NEW:** Join a computer to a team (that is, enable cloud connectivity) at the command line using a JSON file instead of a large token. [More information](https://help.realvnc.com/hc/en-us/articles/360002249737).
-   Setting the [IpClientAddresses](https://help.realvnc.com/hc/en-us/articles/360002251297) parameter (formerly [`hosts`]) to filter incoming direct connections now allows connecting users to specify IPv6 addresses.

### Windows 

-   Disable audit logging to the *domain* Windows Event Log by setting the [`LogSessionToDomainEventLog`] advanced parameter to [`FALSE`], which might speed up connection time. Audit logging to the local Windows Event Log continues.

### Linux 

-   Start VNC Server in Service Mode from a desktop shortcut, and stop it from the app menu, instead of [running commands](https://help.realvnc.com/hc/en-us/articles/360002253218).
-   Specify the screen capture technology used on a Raspberry Pi (hardware or software) separately from the preferred encoding using the [CaptureTech](https://help.realvnc.com/hc/en-us/articles/360002251297) parameter.
-   Use regular expressions in conjunction with the [`CertificateUserName`] advanced parameter, to match user names more flexibly.

### Mac 

-   FIXED: The [LeftOptKey](https://help.realvnc.com/hc/en-us/articles/360002251297), [LeftCmdKey](https://help.realvnc.com/hc/en-us/articles/360002251297), [RightOptKey ](https://help.realvnc.com/hc/en-us/articles/360002251297)and [RightCmdKey ](https://help.realvnc.com/hc/en-us/articles/360002251297)parameters now map received keysyms correctly.

## VNC Viewer 6.19.107 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to exercise control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW:** Support for high-speed streaming in conjunction with VNC Server 6.4.0, above.
-   Share the clipboard contents with the remote computer on session start by setting the [SendInitialClipboard](https://help.realvnc.com/hc/en-us/articles/360002254618) parameter to [`TRUE`].

------------------------------------------------------------------------

[]

# October 2018 

## Mandatory 2-step verification for team members 

If you have an Enterprise subscription, you can mandate that all team members must enable 2-step verification (2FA, using TOTP codes) on their own RealVNC accounts. Failure to comply prevents them remotely accessing team computers. [See how to set this up](https://help.realvnc.com/hc/en-us/articles/360002250077).

## VNC Server 6.3.2 released 

This is a release of VNC Server and supporting programs for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** Provide a comprehensive multi-factor authentication scheme for Mac and Linux computers using [interactive system authentication](https://help.realvnc.com/hc/en-us/articles/360002250217) to integrate with your choice of PAM authentication modules.
-   **NEW:** Blank the screens of Windows 8 and 10 computers in addition to Windows 7 and earlier computers. Note screen blanking is only likely to be effective for monitors attached to desktop computers, and not laptop displays. Test your system in advance using the tool provided on VNC Server's **Options \> Privacy** page. [More information](https://help.realvnc.com/hc/en-us/articles/360016511452).
-   Remove a computer from your team (that is, prevent discovery by RealVNC's cloud service) at the command line using [`-leavecloud`]. [More information](https://help.realvnc.com/hc/en-us/articles/360002249697).
-   Specify a friendly name for a computer whilst adding it to your team at the command line using [`-joinname`]. [More information](https://help.realvnc.com/hc/en-us/articles/360002249737).
-   FIXED: Connecting users supplying Active Directory credentials should find authenticating to VNC Server on Windows is quicker.
-   FIXED: VNC Server is now more integrated with LDAP when the [smartcard/certificate store authentication scheme](https://help.realvnc.com/hc/en-us/articles/360002250377) is selected.
-   FIXED: Users should experience fewer blank screens when connected to Windows computers with the screen saver enabled, or Intel Ready Mode Technology installed.
-   FIXED: Connected users with a left-hand mouse or with mouse buttons switched can now interact remotely in the expected way.

## VNC Viewer for Android 3.4.3 released 

This is a release of VNC Viewer for Android devices you want to control from. Search 'RealVNC' in the Play Store.

-   FIXED: VNC Viewer no longer crashes when connecting directly to a computer that has spaces in its hostname.

## VNC Viewer for iOS 3.6.0 released 

This is a release of VNC Viewer for iOS devices you want to control from. Search 'RealVNC' in the App Store.

-   Improved Bluetooth keyboard support for iOS 12.
-   FIXED: Speech recognition input when dealing with large quantities of text no longer suffers from performance issues.

------------------------------------------------------------------------

[]

# September 2018 

## VNC Viewer for Android 3.4.1 and 3.4.2 released 

These patch releases fixed issues with cursors and app crashes on certain devices found in VNC Viewer for Android 3.4.0, below.

## VNC Viewer 6.18.907 released 

This is a patch release of VNC Viewer for Windows, Mac and Linux computers you want to control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   FIXED: VNC Viewer now starts on macOS even if an invalid URL has been entered into the Mac's **System Preferences \> Network \> Advanced... \> Proxies \> Automatic Proxy Configuration \> Proxy Configuration File URL** field, for either Ethernet or Wi-Fi.

## VNC Viewer for Android 3.4.0 released 

This is a release of VNC Viewer for Android devices you want to control from. Search 'RealVNC' in the Play Store.

-   **NEW:** Support for Android Oreo and Pie, and arm64 processors for improved performance.
-   FIXED: Address books with more than 30 computers now synchronize correctly between all your devices.

------------------------------------------------------------------------

[]

# July 2018 

## VNC Server 6.3.1 released 

This is a patch release of VNC Server and supporting programs, for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   FIXED: Under Linux and macOS, VNC Server now accepts domain license keys once more.
-   FIXED: Under macOS, the VNC Server postflight installation script no longer kills the [`loginwindow`] process, so other service operations continue without interruption.
-   FIXED: VNC Server now attempts to use both system and user proxy server settings (in that order) when communicating with RealVNC services in order to license the software.
-   FIXED: Under Windows, VNC Server should now start in circumstances where Windows Firewall fails to respond properly.

## VNC Viewer 6.18.625 released 

This is a release of VNC Viewer for Windows, Mac and Linux computers you want to control from. [Download](https://www.realvnc.com/connect/download/viewer/).

-   **NEW:** A new encoding, ZRLE2, is now the default, which means that most users should experience better performance in conjunction with VNC Connect 6.3.0, below.
-   VNC Viewer can now log to a centralized logging facility such as [syslog or Event Log](https://help.realvnc.com/hc/en-us/articles/360002254618).
-   On Windows, VNC Viewer now supports high contrast mode.

------------------------------------------------------------------------

[]

# June 2018 

## VNC Server 6.3.0 released 

This is a release of VNC Server and supporting programs, for installation on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   **NEW:** Support for Ubuntu 18.04 LTS. Note Wayland is *not* supported, so for VNC Server in Service Mode you must edit the [`/etc/gdm3/custom.conf`] file, uncomment [`WaylandEnable=false`], and reboot in order to remotely access the login screen.
-   **NEW:** If VNC Server is configured to use [Smartcard/certificate store authentication](https://help.realvnc.com/hc/en-us/articles/360002250377), certificates from connecting users are automatically checked for revocation using OCSP, before falling back to CRLs. To use only OCSP, set the [LdapCertificateRevocation](https://help.realvnc.com/hc/en-us/articles/360002251297) parameter to [`EnforceOcsp`].
-   Under Windows, if VNC Server is configured to use [Smartcard/certificate store authentication](https://help.realvnc.com/hc/en-us/articles/360002250377), certificates from connecting users are now checked against the Enterprise NTAuth store, rather than the Root store.
-   If VNC Server is configured to use [single sign-on authentication](https://help.realvnc.com/hc/en-us/articles/360002250257) (SSO), connecting domain users with Active Directory accounts in different forests are now checked, providing cross-forest trust relationships are in place.
-   Under Windows, if VNC Server in Service Mode is configured to [log to file](https://help.realvnc.com/hc/en-us/articles/360002251297) (rather than Windows Event Log), the default destination directory is now [`C:\ProgramData\RealVNC-Service`].
-   FIXED: Under Linux, VNC Server in Virtual Mode sessions no longer leak audio to local speakers.
-   FIXED: Under Windows, the [DisplayDevice](https://help.realvnc.com/hc/en-us/articles/360002251297) parameter now recognizes monitors plugged into multiple or discrete graphics cards.

## VNC Viewer for iOS 3.5.0 released 

This is a release of VNC Viewer for iOS devices you want to control from. Search 'RealVNC' in the App Store.

-   **NEW:** Control a remote touch panel directly, rather than using the device screen as a trackpad. To do this, select **Interaction \> Touch panel** from a connection's settings, either before or during a session.
-   The connection method (whether cloud or direct) is now displayed on a session's information screen.
-   FIXED: Hardware keyboard left and right arrow keys now work when the scrolling function key bar is active.

------------------------------------------------------------------------

[]

# February 2018 

## VNC Viewer for iOS 3.4.0 released 

This is a minor release for VNC Viewer on iOS devices to connect from. Search 'RealVNC' in the App Store.

-   **NEW:** Support for iPhone X. Unpinning the VNC Viewer toolbar now reveals a movable floating toolbar.
-   FIXED: VNC Viewer now only replaces two consecutive hyphens [`--`] with an em dash [`-`] if keyboard auto-correct is enabled via the app Settings.
-   FIXED: VNC Viewer no longer crashes when the hyphen key is pressed, or any key is held down, on a connected Bluetooth keyboard.

------------------------------------------------------------------------

[]

# December 2017 

## VNC Server 6.2.1 released 

This is a patch release for VNC Server and supporting programs installed on remote computers you want to control. [Download](https://www.realvnc.com/connect/download/vnc/).

-   The message displayed on [accept/reject prompts](https://www.realvnc.com/en/connect/security/#can-i-approve-people-as-they-try-to-connect) can now be customized using the VNC Server [`QueryConnectMessage`] parameter. The custom message can be up to 4096 bytes in length, and utilize the HTML [`<br/>`] syntax to insert new lines.
-   VNC Server now checks Certificate Revocation Lists up to 25MB in size when [smartcard/certificate store authentication](https://help.realvnc.com/hc/en-us/articles/360002250377) is enabled. A larger value can be specified using the VNC Server [`LdapCertificateCrlLimit`] parameter.

------------------------------------------------------------------------

[]

# November 2017 

[VNC Viewer 6.17.1113 released]

VNC Viewer is now ready to conduct instant support sessions (see above) from supported Windows, Mac and Linux computers. [Download](https://www.realvnc.com/connect/download/viewer/).

------------------------------------------------------------------------

[]

## 6.2.0 

  Released
  ------------
  9 Aug 2017

-   **NEW:** VNC Connect is now available in Brazilian Portuguese.
-   **NEW:** Under Red Hat Linux distributions, VNC Server in Virtual Mode can now utilize the version of the Xorg server running on the system, rather than the out-of-date version built-in to Xvnc. Desktop environments such as Gnome 3 and modern applications and extensions will likely be compatible out-of-the-box. [See how to set this up](https://help.realvnc.com/hc/en-us/articles/360003474752).
-   The [VNC Connect download](https://www.realvnc.com/connect/download/vnc/) now consists just of VNC Server and supporting programs, for computers you are licensed to control. VNC Viewer is no longer bundled. You are free to [download VNC Viewer](https://www.realvnc.com/connect/download/viewer/) to as many computers and devices you want to control from as you like.
-   VNC Viewer for macOS is now a disk image (DMG) that you can install by dragging it to the Applications folder.
-   In VNC Viewer, you can now drag-and-drop a computer onto a label in the sidebar to assign that label to the computer. To create a new label, right-click on the Address book.
-   You can set the [QueryOfferViewOnly](https://help.realvnc.com/hc/en-us/articles/360002251297) VNC Server parameter to [`FALSE`] to remove the view-only option from the prompt shown when VNC Viewer users are attempting to connect (leaving just the reject and accept options).

------------------------------------------------------------------------

[]

## 6.1.1 

  Released
  -------------
  30 May 2017

-   FIXED: Active Directory user accounts with no expiry date can now be used to authenticate to VNC Server using single sign-on (SSO)
-   FIXED: VNC Server's Information Center dialog no longer shows an erroneous error message when the legacy [`SecurityTypes`] parameter is set to a value other than [`<auto>`] (this may affect users upgrading from VNC 5.x).
-   FIXED: VNC Server in Virtual Mode ([`Xvnc`]) no longer crashes due to a bug in the X11 render extension.

------------------------------------------------------------------------

[]

## 6.1.0 

  Released
  ------------
  2 May 2017

For a video explaining major features, and links to other resources, please see our [release summary](https://www.realvnc.com/connect/release/) page.

-   **NEW:** VNC Server supports [multi-factor authentication](https://help.realvnc.com/hc/en-us/articles/360002250077). Choose a scheme based on X.509 digital certificates stored on pluggable smartcards/authentication tokens or in certificate stores, or a RADIUS server implementation from an identity management provider such as RSA SecurID or Duo. Alternatively, create a [custom scheme](https://help.realvnc.com/hc/en-us/articles/360002250077) containing as many factors as you need.
-   **NEW:** Conveniently assign [discovery permissions](https://help.realvnc.com/hc/en-us/articles/360002320778) to computers in your RealVNC account by creating groups of people and computers. Restricting discovery improves security, and helps team members reduce the number of computers they interact with in VNC Viewer.
-   **NEW:** Organize computers in VNC Viewer using labels. Right-click on the address book to create a new label, or assign a label to a computer on its **Properties** page.
-   **NEW:** Display a details view of computers VNC Viewer instead of a screenshot icon view, and sort by name, last connected time, and label.
-   More intuitive scaling options for the remote computer desktop are now available from VNC Viewer's **Properties** page.
-   VNC Server now prompts you to send [anonymous usage data](https://www.realvnc.com/legal/#privacy) to RealVNC, to help improve the user experience. You can opt out on VNC Server's **Options \> Privacy** page.

### Linux 

-   The VNC Server in Virtual Mode daemon now fully supports persistent virtual desktops. The [ConnectToExisting](https://help.realvnc.com/hc/en-us/articles/360002251297) parameter no longer requires an underscore (denoting a beta feature).

------------------------------------------------------------------------

[]

## 6.0.3 

  Released
  ---------------
  10 April 2017

-   FIXED: Your computer now recovers automatically if it wrongly reports that it has been cloned.

------------------------------------------------------------------------

[]

## 6.0.2 

  Released
  -----------------
  8 February 2017

-   **NEW:** VNC Connect is available for Raspberry Pi. It is [included](https://www.realvnc.com/raspberrypi/) with Raspbian, and [pre-licensed](https://help.realvnc.com/hc/en-us/articles/360002249917) to offer both cloud *and* direct connectivity to Home subscribers.
-   **NEW:** VNC Viewer has a medium setting for the picture quality of a remote desktop, to complement high and low. By default, the picture quality is automatically adjusted to suit the speed of the network.
-   VNC Connect is available in French, German, and Spanish again. The appropriate language for the desktop of each user is automatically selected. This can be changed (if required) using the [Locale](https://help.realvnc.com/hc/en-us/articles/360002251297) parameter.

------------------------------------------------------------------------

[]

## 6.0.1 

  Released
  ------------------
  23 November 2016

-   The VNC Server user interface now makes it easier to enable cloud connectivity if you have an Enterprise subscription or trial.
-   VNC Server now prompts for administrative credentials (where necessary) in a more timely manner under Linux.

------------------------------------------------------------------------

[]

## 6.0.0 

  Released
  ------------------
  01 November 2016

### All platforms 

-   **NEW:** VNC has a new brand name, VNC Connect. VNC Server and VNC Viewer have new brand colors, icons and logos.
-   **NEW:** VNC Connect is licensed by annual [subscription](https://help.realvnc.com/hc/en-us/articles/360002249677) rather than perpetual license key. When a paid Professional or Enterprise subscription expires, remote access stops. If you're an existing, entitled VNC 5.x customer, you can [automatically upgrade](https://help.realvnc.com/hc/en-us/articles/360002318658) to a new Enterprise subscription.
-   **NEW:** Establish secure, seamless, reliable [cloud](https://www.realvnc.com/en/connect/docs/cloud-connectivity.html#cloud-connectivity) [connections ](https://help.realvnc.com/hc/en-us/articles/360002249737)from VNC Viewer to VNC Server. If you have an Enterprise subscription, this can be as well as, or instead of, traditional [direct connections](https://help.realvnc.com/hc/en-us/articles/360002249797).
-   **NEW:** Invite people in to your [team](https://help.realvnc.com/hc/en-us/articles/360024741652) to quickly share remote access, and manage computers, subscriptions, renewals and payment methods much more conveniently online using your [RealVNC account](https://help.realvnc.com/hc/en-us/articles/360002317757).
-   **NEW:** Sign in to VNC Viewer with your RealVNC account credentials to backup and sync your address book between all your desktop and mobile devices.
-   **NEW:** VNC Address Book is integrated into VNC Viewer, so everything is accessible from one place. Use **File \> Import connections** to transfer VNC 5.x connections in from VNC Address Book, or from a directory of [`.vnc`] files.
-   **NEW:** VNC Viewer can remember remote access credentials so you don't have to enter them each time. Note under Linux we additionally recommend setting a master password for VNC Viewer; see below.
-   **NEW:** Use **File \> Preferences \> Privacy** to set a master password to protect VNC Viewer from unauthorized use.
-   **NEW:** Save desktop previews for connections (that is, screenshots in thumbnail form) to make VNC Viewer more intuitive to use.
-   **NEW:** Give connections friendly names.
-   **NEW:** Quickly forget sensitive data such as passwords and desktop previews if VNC Viewer is running on a shared computer.
-   **NEW:** If you start VNC Viewer and simultaneously establish a direct connection at the command line, use the [`-useaddressbook`] flag to integrate with your address book, for example [`vncviewer`]` `[`-useaddressbook`]` `[`192.168.1.99:65`]. If the connection is to a known computer, stored settings are applied. If the connection is to a new computer, it is added to your address book.
-   **NEW:** Configure the rate at which a desktop is panned when in full screen mode using the [BumpScrollSpeed](https://help.realvnc.com/hc/en-us/articles/360002254618) VNC Viewer parameter.
-   VNC Server now needs an Enterprise subscription in order to run in [User Mode or Virtual Mode](https://help.realvnc.com/hc/en-us/articles/360002320718). Only direct connectivity is available in these modes.
-   VNC Viewer now sets **File \> Preferences \> Proxy** to the system proxy server by default, rather than to no proxy server.
-   VNC Deployment Tool and VNC Viewer for Java are [no longer supported](https://help.realvnc.com/hc/en-us/articles/360002252557).

### Windows 

-   **NEW:** Support for Windows Server 2016. [Full supported platforms list](https://help.realvnc.com/hc/en-us/articles/360002252798).

### Mac 

-   **NEW:** Support for macOS 10.12 Sierra. Note that only 64-bit package files are available for macOS 10.10, 10.11 and 10.12.

### Linux 

-   **NEW:** Support for Ubuntu 16.04 LTS.
-   The process of installing VNC Connect without administrative privileges is now [simpler](https://help.realvnc.com/hc/en-us/articles/360002322677)
-   FIXED: Setting the [`DisableTrayIcon`] VNC Server parameter to [`1`] now correctly removes the VNC Server icon from the notification area.

[]

### Known issues 

-   VNC Connect is only available in English. Spanish, French and German versions will follow soon.
-   After resuming from sleep, it may take a minute or so for your VNC Server computer to be available for cloud connections.
-   Standard selection mechanisms such as CTRL-A or holding down the SHIFT or CTRL key while clicking do not yet allow you to select multiple connections in VNC Viewer.
-   Choosing **File \> Export connections** in VNC Viewer to export to [`.vnc`] files exports all connections, not just the one currently-selected.

------------------------------------------------------------------------

## Legacy VNC 5.x 

[Important: we have now announced the end-of-life for VNC 5.x. Learn more here.](/hc/en-us/articles/360017492037)

Release notes for the legacy VNC 5.x software can be [found here](https://help.realvnc.com/hc/en-us/articles/5923644513821).