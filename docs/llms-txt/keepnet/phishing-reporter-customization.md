# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-customization.md

# Phishing Reporter Customization

This document provides a detailed description of the **Phishing** **Reporter** product. You can understand the basic functions of the **Phishing** **Reporter** page and use the suspicious email reporter add-in by following this document.

You can access the **Phishing** **Reporter** and the menu of related options from the left sidebar of the platform dashboard.

## What is the Phishing Reporter?

Phishing Reporter is an add-in that allows users to easily report a suspicious email to cyber security teams. Quick, comprehensive analysis and response can be provided when used in conjunction with the Incident Responder. Further details about the capabilities and requirements are available in this [document](https://doc.keepnetlabs.com/next-generation-product/platform/incident-responder).

This add-on is compatible with Outlook, Outlook Web Access, Outlook Desktop, Outlook Mobile, Office 365, and Google Workspace environments.

You can download and customize the reporter add-in from the platform interface, as well as see which users currently have the add-in installed.

{% hint style="warning" %}
When the add-in is distributed over Office 365 or Google Workspace, it is automatically installed and active for all users. Add-in user information is only available for those using Outlook Desktop (with the MSI extension)
{% endhint %}

## How to Customize the Phishing Reporter?

Go to the **Phishing Reporter** page from the left sidebar menu of the dashboard and select **Users > Settings**.

Customization is available to four features:

1. Add-in Settings
2. Email Settings
3. Other Settings
4. Diagnostic Tool

### Add-in Settings

You can easily customize any of the fields in the phishing reporter add-in's appearance and dialog settings. It also supports multiple languages, so you can tailor the add-in to various languages and deploy it to employees in their preferred language. To add a new language, simply click on the "**+ Add New Language**" button in the **"Dialog Box Settings."**

<table><thead><tr><th width="213"></th><th></th></tr></thead><tbody><tr><td>Add-in name</td><td>Name of the add-in.</td></tr><tr><td>Brand name</td><td>Company name used for the add-in.</td></tr><tr><td>Add-in logo</td><td><p>For best results, the logo should be 60px (w) :60px (h).</p><p>The maximum disk image size is 2 MB; .png and .jpg formats are acceptable.</p></td></tr><tr><td>Dialog box heading</td><td>Header information used in pop-up messages.</td></tr><tr><td>Confirm button label</td><td><strong>Yes</strong> button text used in confirmation messages.</td></tr><tr><td>No button label</td><td><strong>No</strong> button text used in confirmation messages.</td></tr><tr><td>Okay button label</td><td><strong>Okay</strong> button text used in confirmation messages.</td></tr><tr><td>Instant report message</td><td>Text that will appear after a user reports a suspicious email.</td></tr><tr><td>Connection error message</td><td>Text that will appear if the server cannot be accessed when a report is attempted.</td></tr><tr><td>Sending error message</td><td>Text that will appear if the reported email is not delivered to the platform.</td></tr><tr><td>No email selected message</td><td>Text that will appear if the user tries to report an email without selecting an email.</td></tr><tr><td>Bad format email message</td><td>Text that will appear if the user tries to report an email that is not eligible for reporting.</td></tr><tr><td>Show confirmation message when reporting email</td><td>You must check this box if you wish to include a confirmation message window for a reported email.</td></tr><tr><td>Show confirmation message when deleting email</td><td>This option opens a dialog box that allows you to remove the associated email after a report.<br><br>If you select the "Automatically" option, the reported email will be deleted from the inbox.</td></tr><tr><td>Turn off email forwarding for reported phishing simulation emails</td><td><p>If you enable this option:<br></p><ol><li>When an employee reports a <strong>phishing simulation email</strong>, a dialog box will appear confirming the report, and employees will receive a <strong>congratulatory message</strong> for recognizing the simulation email.</li><li>Reported <strong>phishing simulation emails</strong> will <strong>not</strong> be forwarded to the SOC team's email address specified in the <strong>Email Settings</strong> menu. This ensures that SOC teams can <strong>focus on real suspicious emails</strong> instead of simulated ones.</li><li>Reported <strong>phishing simulation emails</strong> will <strong>not</strong> be forwarded to the <strong>Incident</strong> <strong>Responder</strong> product.</li></ol></td></tr><tr><td>Warning label</td><td>You have the option to add a message as a tag to the reported email to warn the reported user.</td></tr></tbody></table>

Click the **Next** button to go to the next page and save your changes in the first time customization. When the first customization is done, you can use the **Save** **Changes** button to save your changes or use the **Manage** **and** **Download** button to save your settings and download the add-in immediately.

### Email Settings

This section includes two email-related features that you can enable and configure.

#### Send Us Copy

When employees use the **Keepnet Reporter** button to report an email, you can enable this option to send the reported emails to the platform reporting or **Incident Responder** product for analysis and response.

If this option is disabled, only platform-generated emails—such as training notifications and simulation emails—are sent to the platform reporting or Incident Responder platform. Any other reported emails from users will **not** be forwarded to the platform.

#### Information Email

You can configure the add-in to send a reported email to the SOC or IT team as an attachment in **.eml** format using the "**Send Information Email for Reported Incidents"** option. You can customize the following settings:

{% hint style="danger" %}
To use this feature, please enable the "**Send Information Email for Reported Incidents"** option.
{% endhint %}

<table><thead><tr><th width="150"></th><th width="560.1428571428571"></th></tr></thead><tbody><tr><td>Recipient Email Address</td><td>Email address that will receive the reported e-mail</td></tr><tr><td>CC</td><td>Optional additional recipient</td></tr><tr><td>BCC</td><td>Optional additional blind copy recipient</td></tr><tr><td>Email Subject</td><td>Subject line for the email used when reporting a suspicious email. Use {SUBJECT} merge tag as a variable for reported emails' original subject.</td></tr><tr><td>Email Message</td><td>Message template for the email used when reporting a suspicious email</td></tr></tbody></table>

Click the **Next** button to go to the next page and save your changes in the first time customization. When the first customization is done, you can use the **Save** **Changes** button to save your changes or use **Save** **and** **Download** button to save your settings and download the add-in immediately.

### Other Settings

You can also customize additional settings.

<table><thead><tr><th width="150"></th><th width="583.1428571428571"></th></tr></thead><tbody><tr><td>Proxy Settings</td><td>If users are accessing the internet through a proxy, you can enable the plugin to detect the proxy configuration of the computer where it will be installed.</td></tr><tr><td>Site URL</td><td><p>API address that will be used when reporting an email via the add-in.</p><p><strong>Please contact the support team if a change is needed.</strong></p></td></tr><tr><td>API Key</td><td><p>The API key is to be used in the add-in to communicate with the platform.</p><p><strong>Please contact the support team if a change is needed.</strong></p></td></tr><tr><td>Company ID</td><td><p>The Company ID is to be used in the add-in to communicate with the platform.</p><p><strong>Please contact the support team if a change is needed.</strong></p></td></tr><tr><td>Enterprise Vault</td><td>The suspicious email can be searched in the user's backup emails during the investigation.</td></tr></tbody></table>

Click the **Next** button to go to the next page and save your changes in the first time customization. When the first customization is done, you can use the **Save** **Changes** button to save your changes or use **Save** **and** **Download** button to save your settings and download the add-in immediately.

### Diagnostic Tool

The **Diagnostic** **Tool** provides information about the status of the add-in by sending the statistics of the add-in to the platform regularly. The advanced level of awareness presented makes distribution and regulation of the add-in easier for system admins. For example, if the add-in has been disabled by a user or for any reason, the tool can be used to ensure automatic activation or report the situation to the platform for system admins to be aware of this case.

{% hint style="warning" %}
The Diagnostic Tool is designed only for use on Outlook Desktop add-in with the MSI extension. When the add-in is distributed over Office 365 or Google Workspace, it is automatically installed and active for all users.
{% endhint %}

<table><thead><tr><th width="150"></th><th width="583.1428571428571"></th></tr></thead><tbody><tr><td>Check and Enable All Disabled Add-ins Automatically</td><td>The reporter add-in can be enabled automatically if it is not enabled for a reason.</td></tr><tr><td>Proxy Settings</td><td>If users are accessing the internet through a proxy, you can enable the plugin to detect or use the defined proxy configuration of the computer where it will be installed.</td></tr></tbody></table>

After completing the configuration steps and customizations, you can click the **Save** **and** **Download** button to download the add-in for your environment.

## How to View Which Users Have the Phishing Reporter Add-In Installed?

The Phishing Reporter menu offers the option to view a list of users who have the add-in installed and its activation status.

{% hint style="warning" %}
When the add-in is distributed over Office 365 or Google Workspace, it is automatically installed and active for all users. add-in user information is only available for those using Outlook Desktop (with the MSI extension)
{% endhint %}

<table><thead><tr><th width="150"></th><th width="583.1428571428571"></th></tr></thead><tbody><tr><td>E-mail</td><td>Email address of the add-in user. This field may be left blank if there is no target user information for the related user on the platform.</td></tr><tr><td>Add-in Status</td><td>Status of the add-in. If the Diagnostic Tool has not been enabled, the only visible status will be <strong>Online</strong> or <strong>Offline</strong>. The Diagnostic Tool will indicate <strong>Disabled,</strong> <strong>Not</strong> <strong>Installed</strong> or much information about the add-in/user.</td></tr><tr><td>Last Seen</td><td>Date and time the add-in was last active.</td></tr><tr><td>Diagnostic Tool</td><td>Status of the Diagnostic Tool service. The tool can be Installed, Not Installed or Error.</td></tr><tr><td>Device</td><td>Name of the computer used.</td></tr><tr><td>Version</td><td>Version information of the installed add-in</td></tr><tr><td>Actions</td><td>Delete the phishing reporter user data from the phishing reporter users page.</td></tr></tbody></table>

## Video Tutorial

This tutorial provides a detailed description of the Phishing Reporter product. You can understand the basic functions of the Phishing Reporter page and use the suspicious email reporter add-in by following this tutorial.

{% embed url="<https://www.youtube.com/watch?v=djRb16Row1Q>" %}

## FAQ

### Q: Is the Diagnostic Tool only available for the Outlook Desktop version of the add-on? Can it be used with Office 365 or Google workspace?

A: The Diagnostic Tool is designed specifically for the Outlook Desktop version. There is no need for the Diagnostic Tool for O365 and Google Workspace add-ins.

### Q: I performed an update to the add-in. Do I need to uninstall the old version?

A: No. The new version of the add-in will update the old version.

### Q: Do I need to update my existing Outlook, Office 365 or Google Workspace add-in if I change the content of the add-on on the platform?

A: You need to redistribute the current version of the add-in in order for any changes to be activated.

### Q: When a user reports a suspicious email, can a backup of the reported email be forwarded to the SOC team?

A: Yes. please see more information on the ‘Email Settings’ page.

### Q: Can I have a warning pop-up appear before the notification to prevent unintentional emails from being reported after clicking the add-in button?

A: Yes, you can enable the ‘Show confirmation message when reporting email’ option under the Add-in Settings page.

### Q: Can I transfer the Phishing Reporter information to my own cybersecurity solutions or monitoring tools?

A: Yes. You can export all information related to Phishing Reporter via [REST API](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/rest-api) using the [API](https://api.keepnetlabs.com/docs/index.html) document.

### Q: Does the add-in will prompt a "Delete" message after reports the phishing/training emails sent by the platform?

A: No, the add-in will first ask if you wish to report it and then will show a message that the admin is customized under the **"Turn off email forwarding for reported Phishing Simulation emails"** field. There won't be other prompts such as **"Do you wish to delete the original email"** after report emails sent by the platform.

### Q: After the deployment of Phishing Reporter, how can I access it and use it on my OWA account?

A: Log in to your OWA email account and **open** **an** **email**. After that, on the right-hand side, click on the **Apps** button and click on the **Phishing** **Reporter** button to report the suspicious email.
