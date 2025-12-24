# Source: https://help.realvnc.com/hc/en-us/articles/6450666419101-Deploying-RealVNC-Server-for-Mobile-using-Microsoft-Intune

# Deploying RealVNC Server for Mobile using Microsoft Intune 

[Follow](/hc/en-us/articles/6450666419101-Deploying-RealVNC-Server-for-Mobile-using-Microsoft-Intune/subscription.html "Opens a sign-in dialog")

![Avatar](https://help.realvnc.com/system/photos/360077753378/Jack_Naisbett_Professional_Headshot_for_web_-_Copy.jpg)

**[Jack N RealVNC](/hc/en-us/profiles/364261730191-Jack-N-RealVNC)**

Updated August 08, 2025 20:39

This article covers how to deploy the RealVNC Server mobile apps with Microsoft Intune. The steps below require that you have already enrolled your [Android](https://docs.microsoft.com/en-us/mem/intune/user-help/why-enroll-android-device) and [iOS](https://docs.microsoft.com/en-us/mem/intune/user-help/enroll-your-device-in-intune-ios) devices to Intune.

# Deploying the RealVNC Server mobile app to enrolled devices 

These steps apply to using RealVNC Server for Mobile with either Device Access or On-Demand Assist.

## iOS 

1.  Navigate to Apps section of [Microsoft Endpoint Manager](https://endpoint.microsoft.com/#blade/Microsoft_Intune_DeviceSettings/AppsMenu/overview)
2.  Click iOS/iPadOS in the \"By platform\" section\
    \
    ![ios1.PNG](/hc/article_attachments/6451385925149)\
    \
3.  Click Add\
    \
    ![ios2.PNG](/hc/article_attachments/6451385925021)\
    \
4.  Select iOS store app as the App type, then click Select\
    \
    ![ios3.PNG](/hc/article_attachments/6451397696541)\
    \
5.  Click Search the App Store\
    \
    ![ios4.PNG](/hc/article_attachments/6451386059165)\
    \
6.  Search for RealVNC Server and select the RealVNC Server app from the list of results\
    \
    ![ios5.PNG](/hc/article_attachments/6451397756957)\
    \
7.  Review the information that is populated then click Next.\
    **Note: ensure that the Minimum operating system is set to iOS 14.0.**
8.  Configure the app assignments to match your requirements using the appropriate links in each section. Once you have finished adding assignments, click Next\
    \
    [![ios6.PNG](/hc/article_attachments/6451397781661)](/hc/article_attachments/6451397781661)\
    \
9.  Review the information shown on the summary screen, and click Create
10. Intune will start deploying the app to the assigned devices. You can check the progress of the deployment from the app\'s information screen\
    \
    ![ios7.PNG](/hc/article_attachments/6451397830045)

## Android 

#### Important note about Android Control 

When deploying RealVNC Server for Android, remote control is only available if the device is using a fully managed deployment profile.

Management profiles that enable an Android Work Profile (e.g. BYOD and COPE models) do not support remote control as Work Profile apps cannot use the Accessibility service.

**To deploy RealVNC Server for Android using Microsoft Intune, you need to have [linked your Intune account to your Managed Google Play account](https://docs.microsoft.com/en-us/mem/intune/enrollment/connect-intune-android-enterprise)**

1.  Navigate to Apps section of [Microsoft Endpoint Manager](https://endpoint.microsoft.com/#blade/Microsoft_Intune_DeviceSettings/AppsMenu/overview)
2.  Click Android in the \"By platform\" section\
    \
    ![android1.PNG](/hc/article_attachments/6451955986717)\
    \
3.  Click Add\
    \
    ![android2.PNG](/hc/article_attachments/6451941708701)\
    \
4.  Select Managed Google Play app as the App type, then click Select\
    \
    ![android3.PNG](/hc/article_attachments/6451956080541)\
    \
5.  Search for RealVNC Server and select the RealVNC Server app from the list of results\
    \
    ![android6.PNG](/hc/article_attachments/6451956173213)\
    \
6.  Click Approve, then confirm the approval settings as per your requirements\
    \
    ![android7.PNG](/hc/article_attachments/6451942024989)\
    \
7.  Click Select, then Sync\
    \
    ![android8.PNG](/hc/article_attachments/6451956274973)\
    \
8.  This will take you back to your list of Android applications. Click Refresh at the top until RealVNC Server appears. Once it is listed, select it from the list\
    \
    ![android9.PNG](/hc/article_attachments/6451942198813)\
    \
9.  Click Properties, then click Edit next to Assignments\
    \
    ![android10.PNG](/hc/article_attachments/6451956400541)\
    \
10. Configure the app assignments to match your requirements using the appropriate links in each section. Once you have finished adding assignments, click Review + save\
    \
    [![android11.PNG](/hc/article_attachments/6451956564893)](/hc/article_attachments/6451956564893)\
    \
11. Intune will start deploying the app to the assigned devices. You can check the progress of the deployment from the app\'s information screen\
    \
    ![android12.PNG](/hc/article_attachments/6451956551325)

# Joining RealVNC Server for Mobile to your Device Access Team 

To use RealVNC Server for Mobile with your [Device Access subscription](https://www.realvnc.com/en/connect/device-access/), you will need a subscription that includes mass deployment to generate the required [cloud connectivity token](https://help.realvnc.com/hc/en-us/articles/360005474138).

1.  Navigate to Apps section of [Microsoft Endpoint Manager](https://endpoint.microsoft.com/#blade/Microsoft_Intune_DeviceSettings/AppsMenu/overview)
2.  Click App configuration policies in the \"Policy\" section\
    \
    ![appconfig1.PNG](/hc/article_attachments/6452288482589)\
    \
3.  Click Add, Managed devices\
    \
    ![appconfig2.PNG](/hc/article_attachments/6452302109469)\
    \
4.  Enter a name for the configuration policy (e.g. RealVNC Server for Mobile - Device Access), select the platform (iOS/iPadOS or Android), set RealVNC Server as the targeted app and then click Next\
    \
    ![appconfig3.PNG](/hc/article_attachments/6452288578333)\
    \
5.  Select Use configuration designer as the format, then add a row with the below details.\
    Note: for Android, the Permissions section can be ignored.\
    \
    **Configuration key:** joinCloud (Join Cloud on Android)\
    **Value type:** String\
    **Configuration value:** Your [cloud connectivity token](https://help.realvnc.com/hc/en-us/articles/360005474138) from the Deployment page of the [RealVNC Connect portal](https://manage.realvnc.com/)\
    \
    You can optionally add devices to a [computer group in RealVNC Connect](https://help.realvnc.com/hc/en-us/articles/360002320778) or set a specific name for the device by adding an additional row:\
    \
    **Configuration key:** joinGroup (Join Group on Android)\
    **Value type:** String\
    **Configuration value:** The name of the Computer Group from the [RealVNC Connect portal](https://manage.realvnc.com/)\
    \
    **Configuration key**: joinName (Join Name on Android)\
    **Value type**: String\
    **Configuration value**: The name of the device as it will appear in RealVNC Viewer and the RealVNC Connect portal. Note, you can use certain Intune properties as listed [here for iOS](https://learn.microsoft.com/en-gb/mem/intune/apps/app-configuration-policies-use-ios#tokens-used-in-the-property-list) and [here for Android](https://learn.microsoft.com/en-gb/mem/intune/apps/app-configuration-policies-use-android#supported-variables-for-configuration-values).\
    \
6.  Click Next when you are done\
    \
    ![appconfig4.PNG](/hc/article_attachments/6452288599837)\
    \
7.  Select the groups of devices that you want to apply the app configuration policy to, then click Next\
    \
    ![appconfig5.PNG](/hc/article_attachments/6452302325533)\
    \
8.  Review the information on the summary screen, then click Create\
    \
    ![appconfig6.PNG](/hc/article_attachments/6452288706461)\
    \
9.  Intune will start deploying the app configuration policy to the assigned devices. You can check the progress of the deployment from the configuration policy\'s information screen\
    \
    ![appconfig7.PNG](/hc/article_attachments/6452288780701)\
    \
10. Once the configuration policy has been applied to the device, RealVNC Server for Mobile will be joined to your team when the RealVNC Server mobile app is next launched on the device