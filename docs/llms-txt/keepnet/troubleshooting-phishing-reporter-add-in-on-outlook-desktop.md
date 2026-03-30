# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/6.-setup-phishing-reporter/deploy-keepnets-customisable-phishing-report-button/step-2.-deploy-phishing-reporter/how-to-deploy-add-in-in-outlook/troubleshooting-phishing-reporter-add-in-on-outlook-desktop.md

# Troubleshooting Phishing Reporter Add-In on Outlook Desktop

If you've installed the Phishing Reporter on the Microsoft Outlook Desktop version successfully but are unable to see the Phishing Reporter button, here are some steps you can follow to troubleshoot the issue.

## Step 1: Check your Outlook Version

First, confirm that you are using a version of Outlook that is compatible with Phishing Reporter. It might be possible that your current Outlook version is outdated and not supported by the add-in. Phishing Reporter usually supports the most recent versions of Outlook, but you can double-check the specific versions from [here](https://doc.keepnetlabs.com/Next-Generation-Product/miscellaneous/platform-requirements/phishing-reporter-requirements#software-requirements).

## Step 2: Verify Installation

Make sure the Phishing Reporter Add-in was installed correctly. If the installation was interrupted or not completed, it could result in the button not appearing.

* Press the Win+S button combination on your keyboard, and find ‘Installed Apps’.
* Locate 'Phishing Reporter Outlook AddIn' in the list of installed programs.
* If you cannot find it, try reinstalling the software.

## Step 3: Enable Add-in

Sometimes, the add-in might not be enabled, or it may have been disabled. Here's how to check:

* In Outlook, go to 'File' > 'Options' > 'Add-ins'.
* In the 'Manage' dropdown, select 'COM Add-ins', then select 'Go'.
* If 'Phishing Reporter' is listed but not checked, tick the checkbox to enable it.
* If 'Phishing Reporter' is not listed, it means the add-in is not installed correctly. Try reinstalling.

## Step 4: Check the Ribbon

In some cases, the button may not be visible because it's not added to your Outlook ribbon, or it's located under a different tab.

* Right-click on the ribbon and select 'Customize the Ribbon'.
* Look for 'Phishing Reporter Add-in Name' in the list. If it's there, make sure it's ticked and placed under the Home tab.

## Step 5: Check Windows Event Logs

Sometimes, Outlook or the add-in may be experiencing issues that could be found in the Windows Event Logs.

* Type 'Event Viewer' in the Start menu and open it.
* On the left side, navigate to 'Windows Logs' > 'Application'.
* Look for any recent warnings or errors related to Outlook or the Phishing Reporter Add-in around the time you last launched Outlook. Pay particular attention to Event ID 45 and 59, which might be related to this issue.

### 5.1 - AddIn Disabled

When examining your Windows Event Logs, you may encounter a log entry indicating that the Phishing Reporter add-in has been disabled by Outlook. This typically occurs when the add-in takes too long to load at startup. Once identified, the disabled add-in can be enabled again, as outlined in Step 3 of this guide. If the issue continues after this action, please refer to Step 8 for further troubleshooting assistance.

```
Event ID:59
Source:Outlook
Log:Application
Message:Outlook disabled the following add-in(s):

ProgID: PhishingReporter.Outlook.Addin
GUID: {D0F2562C-3BC1-42E3-B34E-8A735974A173}
Name: PhishingReporterAddIn
Description: AddinModule
Load Behavior: 2
HKLM: 1
Location: C:\Program Files (x86)\Phishing Reporter\Phishing Reporter Outlook 
Threshold Time (Milliseconds): 1000
Time Taken (Milliseconds): 1875
Disable Reason: This add-in caused Outlook to start slowly.
Policy Exception (Allow List): 0
```

### 5.2 - AddIn Load Times

Microsoft Outlook Desktop may occasionally deactivate add-ins to prevent the application from crashing. By leveraging the Windows Event Logs, you can acquire valuable insights about the loading times of all add-ins. This knowledge helps identify add-ins exceeding the optimal loading time of 1000 milliseconds.

Outlook loaded the following add-in(s):

```
Name: Microsoft Exchange Add-in
Description: Exchange support for Unified Messaging, e-mail permission rules, and calendar availability.
ProgID: UmOutlookAddin.FormRegionAddin
GUID: {F959DBBB-3867-41F2-8E5F-3B8BEFAA81B3}
Load Behavior: 3
HKLM: 1
Location: C:\Program Files\Microsoft Office\root\Office16\ADDINS\UmOutlookAddin.dll
Boot Time (Milliseconds): 0

Name: Skype Meeting Add-in for Microsoft Office
Description: Skype Meeting Add-in for Microsoft Office
ProgID: UCAddin.LyncAddin.1
GUID: {A6A2383F-AD50-4D52-8110-3508275E77F7}
Load Behavior: 3
HKLM: 1
Location: C:\Program Files\Microsoft Office\root\Office16\UCAddin.dll
Boot Time (Milliseconds): 15

Name: PhishingReporterAddIn
Description: AddinModule
ProgID: PhishingReporter.Outlook.Addin
GUID: {D0F2562C-3BC1-42E3-B34E-8A735974A173}
Load Behavior: 3
HKLM: 1
Location: C:\Program Files (x86)\Phishing Reporter\Phishing Reporter Outlook AddIn\adxloader64.dll
Boot Time (Milliseconds): 146
```

```
Request url: https://addin-api.keepnetlabs.com/api/heartbeat response content : RestHttpClient.cs : Post : 109
System.Net.Http.HttpRequestException: An error occurred while sending the request. ---> System.Net.WebException: The remote name could not be resolved: 'keepnetaddin.xcompany.local'
```

### 7.3 - Unable to connect to the remote server

This log indicates a network connectivity error during an HTTP request.

This error usually stems from the following situations:

* The network connection dropped or there is a temporary problem in the network. In this case, the network connection should be checked and, if necessary, the network may need to be restarted or the network settings may need to be checked.
* The client side is using an incorrect IP address or port number. In this case, the target and parameters of the request should be checked.
* The connection is being blocked due to a firewall or other network security settings. In this case, the security settings should be checked.

**Error Log:**

```
Request url : https://addin-api.keepnetlabs.com/api/notify/email response content :   : RestHttpClient.cs : Post : 104
System.Net.Http.HttpRequestException: An error occurred while sending the request. ---> System.Net.WebException: Unable to connect to the remote server ---> System.Net.Sockets.SocketException: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond 1.1.1.1:235
```

### 7.4 - The remote name could not be resolved

This log represents a network error situation.

This error usually stems from the following situations:

* Network connection problems. In this case, the network connection should be checked, and it should be ensured that the computer has general access to the internet.
* The DNS server is not functioning correctly. In this case, the DNS server should be checked, if necessary, restarted, or DNS settings should be reviewed.

**Error Log:**

```
Request url: https://addin-api.keepnetlabs.com/api/heartbeat response content : RestHttpClient.cs : Post : 104
System.Net.Http.HttpRequestException: An error occurred while sending the request. ---> System.Net.WebException: The remote name could not be resolved: 'addin-api.keepnetlabs.com'
```

## Step 8: Contact Support

If the above steps don't resolve your issue, it's suggested to ask for assistance from the Keepnet support team. There are two primary ways to get in touch with them:

1. **Email:** You can send an email to <support@keepnetlabs.com>. Make sure to include all relevant details about your problem, such as your Outlook version, OS version, and any other pertinent information about your system.
2. **Support Portal:** Alternatively, you can submit a ticket directly via the Keepnet support portal at <https://support.keepnetlabs.com/portal/en/home>.

For additional information on how to contact support, please refer to our [Help Desk](https://doc.keepnetlabs.com/resources/keepnet-support-help-desk) documentation.
