# Source: https://help.realvnc.com/hc/en-us/articles/5518809415453-RealVNC-Server-for-Mobile-FAQs

# RealVNC Server for Mobile - FAQs 

[Follow](/hc/en-us/articles/5518809415453-RealVNC-Server-for-Mobile-FAQs/subscription.html "Opens a sign-in dialog")

![Avatar](https://help.realvnc.com/system/photos/360077753378/Jack_Naisbett_Professional_Headshot_for_web_-_Copy.jpg)

**[Jack N RealVNC](/hc/en-us/profiles/364261730191-Jack-N-RealVNC)**

Updated August 07, 2025 17:10

## How do I connect to my phone or tablet? 

### Device Access 

To use RealVNC Server for Mobile with Device Access you will need a subscription that includes mass deployment and an MDM, such as Microsoft Intune, to apply a [cloud connectivity token](https://help.realvnc.com/hc/en-us/articles/360005474138-Using-Cloud-connectivity-tokens).

Once RealVNC Server for Mobile has been joined to your Team, you will be able to connect to the mobile device as you would for a computer in RealVNC Viewer. There is no username or password to provide, instead all connections must be approved by the user of the mobile device that you are connecting to.

### On-Demand Assist 

As a technician, you will use RealVNC Viewer on Windows, Mac or Linux to [generate a 9 digit session code](https://help.realvnc.com/hc/en-us/articles/360002251457#starting-an-instant-support-session-with-an-end-user-0-2) in the same way you would when connecting to Windows or Mac. Your end users will download and install the RealVNC Server mobile app from their app store and enter the 9 digit code provided by the technician. Read more about On-Demand Assist [here](https://www.realvnc.com/en/connect/pricing/instant-support/).

**[Note for both Device Access and On-Demand Assist, the RealVNC Server mobile app must be open and in the foreground to approve incoming connections for both Device Access and On-Demand Assist, or your device must be configured to allow notifications while screen broadcasting is activated.]**

## What can and can't I do? 

RealVNC Server for Mobile allows you to remotely access an Android or iOS device. Please note that remote access to iOS devices is view only; remote control is not yet supported.

*\* For Device Access an MDM for app deployment is required, such as Microsoft Intune.*

## Which versions of Android and iOS/iPadOS are supported? 

RealVNC Server for Android is supported on Android 8 and later.

RealVNC Server for iOS/iPadOS is supported on iOS/iPadOS 14 and later.

## Can I connect to an unattended phone or tablet? 

RealVNC Server for Mobile can only be used in attended access mode, with the remote device requiring a user present to accept the connection.

## Why can\'t I control my iPhone or iPad? 

Remote control is not yet supported for iOS devices; all connections are view only.

## Can I make a direct connection to my phone or tablet without accessing the Internet? 

No, RealVNC Server for Mobile supports cloud connections only.

## Which features are unavailable when connecting to my phone or tablet? 

File transfer, chat, remote printing, audio and screen recording are not yet supported.

## Can I change the app between Device Access and On-Demand Assist? 

Once RealVNC Server for Mobile has been joined to a Device Access Team, you will no longer be able to connect to it using On-Demand Assist. To switch to On-Demand Assist, you will need to remove the device from your Team using the [RealVNC Connect portal](https://manage.realvnc.com/en/) and removing the relevant configuration policy in your MDM.

## Which permissions are required for the apps? 

For Android, to use Device Access you will need to allow the app to display notifications.

For iOS, the app requests permissions to display notifications, as well as connecting to devices on your local network. For Device Access, notifications must also be enabled in iOS\' Settings, Notification, Screen Sharing. You can read more about how to do this [here](https://help.realvnc.com/hc/en-us/articles/10569605518493).

## The \"Listen for connections\" button is missing in RealVNC Server for iOS, how can I start a session? 

Please check that another app is not already broadcasting your screen. If it is, disable it and re-launch RealVNC Server for iOS. If you continue to experience issues, please contact support [here](https://help.realvnc.com/hc/en-us).

## Can I connect to a locked phone or tablet? 

No, the phone or tablet must be unlocked for connections to be successful.

## How do I deploy RealVNC Server for Mobile using an MDM? 

Please see [Deploying RealVNC Server for Mobile using Microsoft Intune](/hc/en-us/articles/6450666419101)

## Are there any known issues? 

Yes, see [RealVNC Server for Mobile - Known Issues](/hc/en-us/articles/6262341473565).

## Can I talk to someone if I need help? 

Yes, if your subscription includes access to technical support you can contact the team [here](https://help.realvnc.com/hc/en-us).