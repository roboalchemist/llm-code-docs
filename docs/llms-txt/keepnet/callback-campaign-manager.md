# Source: https://doc.keepnetlabs.com/next-generation-product/platform/callback-simulator/callback-campaign-manager.md

# Callback Campaign Manager

Launch a callback campaign targeting users with enhanced options like **Expiration Date, Mark As Test, Multiple Scenario Selection, SMTP or DEC delivery, Frequency** or **Distribution** via the Campaign Manager.

## Campaign Manager Components

The components of the **Campaign** **Manager** page are explained below.

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Campaign Name</td><td><p>The name of the campaign</p><p><strong>"Instance"</strong> information indicating the number of times the campaign has been launched is available next to the campaign name</p></td><td></td></tr><tr><td>Target Users</td><td>The target users who will receive the callback phishing email</td><td></td></tr><tr><td>Status</td><td><p><strong>Status</strong> information of the campaign. (idle, running, completed, paused, canceled, error)</p><ul><li><strong>Idle</strong> <strong>=</strong> The campaign is launched and has not started yet</li><li><strong>Running</strong> <strong>=</strong> The campaign is in progress</li><li><strong>Completed</strong> <strong>=</strong> The campaign is delivered to all target users</li><li><strong>Paused</strong> <strong>=</strong> The campaign has been temporarily suspended</li><li><strong>Canceled</strong> <strong>=</strong> The campaign has been withdrawn</li><li><strong>Error</strong> <strong>=</strong> The status field displays an error message if there is a delivery problem</li></ul></td><td></td></tr><tr><td>Scenarios</td><td>Shows how many scenarios has been launched in the campaign.</td><td></td></tr><tr><td>Created By</td><td>The source of the phishing campaign (system, custom)</td><td></td></tr><tr><td>Email Delivery</td><td>The selected email delivery option, <a href="../company/company-settings/smtp-settings">SMTP</a> or <a href="../company/company-settings/direct-email-creation">DEC</a> rule.</td><td></td></tr><tr><td>Date Created</td><td>The date and time the campaign was created</td><td></td></tr><tr><td>Last Launch</td><td>The date of the most recent use of the campaign</td><td></td></tr></tbody></table>

### Actions

These settings give you the ability to **edit**, **preview**, or **delete** campaigns, as well as create new instances. You can also resend a campaign to specific users.

Click on the **three dots** “︙” button under the **Action** heading to adjust the following features.

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Preview</td><td>Click the eye icon to preview the campaign</td><td></td></tr><tr><td>Edit</td><td>Change the settings of the relevant campaign</td><td></td></tr><tr><td>Create New Instance</td><td>Relaunch the campaign with the same settings to target groups</td><td></td></tr><tr><td>Delete</td><td>Delete the campaign</td><td></td></tr></tbody></table>

## Campaign Instances

In the **Campaign** **Name** column, the **Instances** option will provide details of the campaign, such as how many times it has been launched and the users targeted.

The components of the **Campaign** **Instances** page are explained below.

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Frequency</td><td>If you have <strong>selected</strong> <strong>multiple</strong> <strong>scenarios</strong>, it shows how often you selected the scenarios to be sent randomly to the selected groups.</td><td></td></tr><tr><td>Target Users</td><td>The number of target users who will receive the campaign</td><td></td></tr><tr><td>Start Time</td><td>The date and time that the campaing was started</td><td></td></tr><tr><td>Status</td><td>Current status of the campaign (idle, running, completed, canceled, error)</td><td></td></tr><tr><td>Date Created</td><td>The creation date of the campaign</td><td></td></tr></tbody></table>

### Actions

You can delete, pause, or resume a paused instance on the **Campaign** **Instances** page as well as you also have the option to view detailed reports of an instance or resend the campaign.

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Launch</td><td>Resend a campaign to a selected group</td><td></td></tr><tr><td>View Report</td><td>Access detailed reports of a campaign</td><td></td></tr><tr><td>Delete</td><td>Delete the campaign report</td><td></td></tr><tr><td>Stop</td><td>Terminate an active campaign</td><td></td></tr></tbody></table>

## Create a Campaign

Click on **"+** **NEW"** on the **Callback Simulator > Campaign Manager** page to create a new callback phishing campaign to set up to launch target users in four simple steps:

* Campaign Settings
* Callback Scenarios
* Target Audience
* Delivery Settings
* Campaign Summary

{% hint style="warning" %}
Before launching a phishing campaign, you must create a [target user group](https://doc.keepnetlabs.com/next-generation-product/platform/company/target-users).
{% endhint %}

### Campaign Settings

Enter basic information about this campaign. The components of the **Campaign** **Info** page are explained below.

<table><thead><tr><th width="154.66855801213072"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Campaign Name</td><td>The name of the campaign</td><td></td></tr><tr><td>Tracking Duration</td><td>Select the time period you want to keep this campaign active</td><td></td></tr><tr><td>Mark As Test</td><td>Select this box if you want to exclude the results of the campaign from the overall company score</td><td></td></tr></tbody></table>

### Phishing Scenarios

Select one scenario to send selected target users or select multiple phishing scenarios to distribute randomly.

{% hint style="info" %}
If multiple scenarios are selected, each user will receive a random scenario.
{% endhint %}

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Scenarios</td><td>Select scenarios to be sent to selected target users.</td><td></td></tr><tr><td>Language</td><td>Filter scenarios according to their language.</td><td></td></tr><tr><td>Voice</td><td>Filter scenarios according to AI voices.</td><td></td></tr><tr><td>Difficulty</td><td>Filter scenarios according to their difficulty level.</td><td></td></tr></tbody></table>

### Target Audience

Select target groups for your campaign.

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Target Audience</td><td>Choose one or several recipient groups to send the selected phishing scenarios to.</td><td></td></tr><tr><td>Limit Recipients</td><td><ul><li><strong>Send only to users with an active phishing reporter add-in:</strong> Select this option to send the campaign only to users with an active phishing reporter add-in.</li><li><strong>Send this campaign to randomly selected users:</strong> Choose this option to send the phishing campaign to randomly selected users within the target group. You have the option to choose a percentage of the group or a specific number of users.</li></ul></td><td></td></tr></tbody></table>

### Delivery Settings

Set email delivery options.

The components of the **Delivery** **Settings** page are explained below.

<table><thead><tr><th width="142"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Email Delivery</td><td>Choose the email delivery settings, which can be either <a href="../company/company-settings/smtp-settings">SMTP</a> or <a href="../company/company-settings/direct-email-creation">DEC</a>.</td><td></td></tr><tr><td>Frequency</td><td>If you have <strong>selected</strong> <strong>multiple</strong> <strong>scenarios</strong>, you can choose how often you would like to send the scenarios randomly to the selected groups.</td><td></td></tr><tr><td>Schedule</td><td><p>The date and time of the campaign launch:</p><ul><li><strong>Schedule for:</strong> Check this box to begin the campaign on a specific date.</li><li><strong>Save for later:</strong> Check this box if you want to send the campaign later. To send now, click the "<strong>Now</strong>" button after opening the date and time pop-up.</li></ul></td><td></td></tr><tr><td>Distribution</td><td><p>When you launch a phishing campaign to a large audience, this feature ensures that the emails are not blocked or quarantined by the recipient's email server. It achieves this by distributing the emails over a period of time rather than sending them all at once.</p><ul><li><strong>Send emails when the campaign starts:</strong> As the campaign begins, emails are immediately dispatched to the selected target users.</li><li><p><strong>Send emails on defined days and hours:</strong> You can determine the specific days and times when emails will be delivered to the chosen target users.</p><ul><li><strong>Sending limit per batch:</strong> Define the quantity of emails you'd like to send to the recipients in each batch during the chosen days and times.</li><li><strong>Send emails with delay every:</strong> Decide on the duration of the pause between sending each batch, whether it's in seconds, minutes, or hours.</li></ul></li></ul><p>The system will automatically determine and show you the duration required to send the campaign to the designated number of recipients based on your chosen settings.</p></td><td></td></tr></tbody></table>

### Campaign Summary

All of the phishing campaign details are easily accessible on one page, along with a preview of the callback email template and callback template.

The components of the **Campaign** **Summary** page are explained below.

<table><thead><tr><th width="138"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Scenario Info</td><td>The name of the campaign, the difficulty level and the tracking duration are listed.</td><td></td></tr><tr><td>Settings</td><td>Date and time of the campaign, the number of emails to be sent in batch, and the email delivery info</td><td></td></tr><tr><td>Other</td><td>Other additional enabled settings will appear here such as "mark as test" option.</td><td></td></tr><tr><td>Target Users</td><td><p>The target users who will receive the callback campaign.</p><p>Click on <strong>Preview</strong> to see the target users count and target user groups.</p></td><td></td></tr><tr><td>Email to be sent</td><td><p>The phishing email template selected for the campaign</p><p>Click <strong>Preview</strong> to see how it will be displayed in the target users’ inboxes</p></td><td></td></tr><tr><td>Callback Template</td><td><p>The selected callback template for the campaign.</p><p>Click <strong>Preview</strong> to see how it will be displayed in the target users’ browsers</p></td><td></td></tr><tr><td>Schedule</td><td>By enabling the frequency feature, you can view the date and time when the scenarios will be delivered to the selected groups.</td><td></td></tr></tbody></table>

Click **Start** to launch the campaign.

Click **Cancel** to rescind all of the actions, then click **Quit** in the pop-up window. If you want to make additional edits, click **Continue** **Editing**.

## Video Tutorial

This tutorial explains the features of the **Campaign** **Manager**, including **Scheduling**, **Targeting** **Multiple** **Groups**, **SMTP** **Delay**, **Expiration** **Date**, **Multiple** **Scenarios**, and **Randomization**. These options help you customize and launch the callback campaign for your target users.

{% embed url="<https://youtu.be/vNps_if7IVQ?si=IzwsJzk4eErmBt_2>" %}

## FAQ

### Q: Is it possible to remove the phishing simulation email from target users’ inboxes once the campaign has been launched?

A: Yes. The investigation feature of the Incident Responder product gives you the capability to delete the phishing simulation email.

### Q: Can I change the date and time of the campaign after it has been scheduled?

A: Yes. You can adjust the campaign settings at any time before the launch date.

### Q: Is there a way to exclude phishing campaigns from showing up in the reports section, for example, if they were launched for testing purposes?

A: Yes. At the beginning of the campaign creation, enable the **"Mark As Test" f**eature to exclude the campaign report from the overall company score.

### Q: Why do callback emails contain the "X-MS-Exchange-Organization-SkipSafeLinksProcessing: true" header?

A: This header prevents Microsoft Defender from analyzing links in callback emails, ensuring accurate test results and preventing false positives.
