# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/diagnostic-tool.md

# Diagnostic Tool

In standard Windows, the MS Outlook service does not support monitoring and reporting the functionality of the installed add-ins on it. This service has been developed in order to monitor and report whether Keepnet Outlook add-in functions properly or not.

Using this service, system administrators will be aware of the potential environment-based errors which could affect the Keepnet Outlook Phishing Reporter add-in not functioning properly and be able to take action.

## Downloading Diagnostic tool

Go to **Phishing Reporter > Settings > Diagnostic Tool** to download the diagnostic tool.

Configure the following settings:

* **Proxy Settings:** Enable proxy settings for the Diagnostic Tool to go internet through a proxy.
* **Optional Settings:** Select if you want the Diagnostic Tool to check the Phishing Reporter add-in and enable it automatically if disabled.

Once you're happy with your settings, click **Download** under the diagnostic tool. Then follow the steps below to install the service.

## Installation

There are two options to install the service, either install it on your computer or deploy the service to thousands of users' computers using centralized software distribution tools.

### Normal installation

* Click on the **MSI package** to install it on your computer.
* Click the **Next** button and continue with the default settings.
* Click the **Yes** button to finish the installation.

### Silent Installation

You can use the following commands for silent installation and removal.

<table><thead><tr><th width="178.5"></th><th></th></tr></thead><tbody><tr><td>Silent Installation</td><td>C:\Windows\System32\msiExec.exe -i "KeepnetPhishDiagInstaller.msi" /QN /norestart</td></tr><tr><td>Silent Removal</td><td>C:\Windows\System32\msiExec.exe -x "KeepnetPhishDiagInstaller.msi" /QN /norestart</td></tr><tr><td>Product Guid Detection</td><td>get-wmiobject Win32_Product | Format-Table IdentifyingNumber, Name, LocalPackage -AutoSize</td></tr><tr><td>Remove with Product Guid</td><td>C:\Windows\System32\msiExec.exe -x {product-guid} /QN /norestart</td></tr></tbody></table>

Once the installation is complete, you can confirm that the diagnostic tool has been installed by going to **Phishing Reporter > Users** and looking under the **Diagnostic tool** column.

This column will show one of the following in the table below.

<table data-header-hidden><thead><tr><th width="176.5"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Not Installed</td><td>The diagnostic tool has not been installed</td><td></td></tr><tr><td>Online</td><td>The diagnostic tool has been installed, and the user is online</td><td></td></tr><tr><td>Offline</td><td>The diagnostic tool is installed, but the user is offline</td><td></td></tr><tr><td>Error/Uninstalled</td><td>There is an error with the diagnostic tool installation or the tool has been removed</td><td></td></tr></tbody></table>

### Understand Diagnostic Tool information

To view the **Diagnostic Tool** information, go to **Phishing Reporter > Users** and look under the **Add-in Status** column. When hovering the mouse over this column under the desired user, you will see the following information below.

<table data-header-hidden><thead><tr><th width="150.5"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Add-in is installed and</td><td><ul><li>User is online</li><li>User is offline</li></ul></td><td></td></tr><tr><td>HKLM Number</td><td><p>List of possible <a href="https://learn.microsoft.com/en-us/visualstudio/vsto/registry-entries-for-vsto-add-ins?redirectedfrom=MSDN&#x26;view=vs-2022#LoadBehavior">values</a>:</p><p>1: Active: Don't load automatically</p><p>2: Disabled: Load at startup</p><p>3: Active: Load at startup</p></td><td></td></tr><tr><td>Boot time</td><td>How long it takes for the add-in to start</td><td></td></tr><tr><td>Outlook version</td><td>Version information of Outlook application</td><td></td></tr><tr><td>Outlook Architecture</td><td><p>Either:</p><ul><li>X32</li><li>X64</li></ul></td><td></td></tr><tr><td>OS version</td><td>User’s operating system version information</td><td></td></tr></tbody></table>

The Diagnostic Tool has been successfully installed, operated and can communicate with the platform to help you obtain Phishing Reporter status information for all target users.

## Troubleshooting

For troubleshooting purposes, you can provide the support team with the log and configuration files, which can be found in the following path on the user's computer.

* C:\Program Files (x86)\Keepnet Labs\KeepnetLabs Phishing Reporter Diagnostic Service

## Tutorial Video

This video tutorial explains how to customize the Diagnostic Tool service and download it.

{% embed url="<https://youtu.be/oI6cwzpE0Js>" %}

## FAQ

### Q: Some users have the add-in enabled, but they seem offline on the interface. Why?

A: If the add-in is installed and active, but seems Offline, then the Outlook application is closed. If Outlook is still running, but it is still Offline, it means that there is a communication problem between the add-in and the platform. You can easily detect this problem from the logs created by the add-in on the user's computer or get support from our support team.

### Q: How do I know if the add-in is disabled by the user or by Outlook?

A: If you see the “Inactive" notification, then it is disabled by the user. If it says “Disabled", it means that it is disabled by Outlook. You can also verify this from the interface of user’s Outlook Desktop in the **File > Options > Add-Ins** window.

### Q: Can I have different teams log into the Keepnet Portal and see only the Outlook detail report page?

A: With the [user role](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles) feature, you can authorize your users with custom permissions.
