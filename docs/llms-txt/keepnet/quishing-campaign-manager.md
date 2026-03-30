# Source: https://doc.keepnetlabs.com/next-generation-product/platform/quishing-simulator/quishing-campaign-manager.md

# Quishing Campaign Manager

A quishing campaign can be launched to target users in two ways. The **Fast** **Launch** option allows you to initiate a quishing campaign quickly and easily, without having to designate any settings. However, if you prefer customization, advanced features are available to refine the campaign using the **Campaign** **Manager** option, such as **Schedule**, **Multiple** **Target** **Groups**, **SMTP** **Delay**, **Expire** **Date**, **Multiple** **Scenarios,** and **Randomize** to allow you to modify a variety of elements to suit your needs.

## Campaign Manager Components

The components of the **Campaign** **Manager** page are explained below.

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Campaign Name</td><td>The name of the campaign and <strong>Instance</strong> information indicating the number of times the campaign has been launched</td><td></td></tr><tr><td>Target Users</td><td>The number of target users who will receive the quishing email</td><td></td></tr><tr><td>Status</td><td><p><strong>Status</strong> information of the campaign. (idle, running, completed, canceled, error)</p><ul><li><strong>Idle:</strong> The campaign has been launched and has not started yet</li><li><strong>Individual Printout:</strong> The campaign is launched as a printout.</li><li><strong>Running:</strong> The campaign started and running</li><li><strong>Completed:</strong> The campaign is delivered to all target users</li><li><strong>Canceled:</strong> The campaign has been canceled by system admin</li><li><strong>Error:</strong> The status field displays an error message if there is a delivery problem or campaign error</li></ul></td><td></td></tr><tr><td>Scenarios</td><td>Shows how many scenarios has been launched in the campaign.</td><td></td></tr><tr><td>Quishing Type</td><td><p>The quishing type of the campaign:</p><ul><li><strong>Email:</strong> The quishing campaign is launched to users via email.</li><li><strong>Individual Printout:</strong> The quishing campaign is launched to users via the printout.</li></ul></td><td></td></tr><tr><td>Method</td><td>Method type of the campaign</td><td></td></tr><tr><td>Created By</td><td>The source of the quishing campaign (system, custom)</td><td></td></tr><tr><td>Email Delivery</td><td>The selected email delivery option, <a href="../company/company-settings/smtp-settings">SMTP</a> or <a href="../company/company-settings/direct-email-creation">DEC</a> rule.</td><td></td></tr><tr><td>Date Created</td><td>The date and time the campaign was created</td><td></td></tr><tr><td>Last Launch</td><td>The date of the most recent use of the campaign</td><td></td></tr><tr><td>Actions</td><td><p>These settings give you the ability to <strong>edit</strong>, <strong>preview</strong>, or <strong>delete</strong> campaigns, as well as create new instances. You can also resend a campaign to specific users.</p><ul><li><strong>Edit:</strong> Change the settings of the relevant campaign</li><li><strong>Create a New Instance:</strong> Relaunch the campaign</li><li><strong>Print Preview:</strong> Print preview the campaign if it is launched via the 'Individual Printout Campaign' method.</li><li><strong>Duplicate:</strong> Create a copy of the campaign</li><li><strong>Delete:</strong> Delete the campaign</li></ul></td><td></td></tr></tbody></table>

## Campaign Instances

In the **Campaign** **Name** column, the **Instances** option will provide details of the campaign, such as how many times it has been launched and the users targeted.

The components of the **Campaign** **Instances** page are explained below.

<table data-header-hidden><thead><tr><th width="162"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Frequency</td><td>If you selected multiple scenarios, it shows how often you send the scenarios randomly to the selected groups.</td><td></td></tr><tr><td>Schedule</td><td>The date and time the campaign will launch</td><td></td></tr><tr><td>Target Users</td><td>The number of scheduled target users</td><td></td></tr><tr><td>Status</td><td><p>Current status of the campaign</p><p>(idle, running, completed, cancelled, error)</p></td><td></td></tr><tr><td>Date Created</td><td>The creation date of the campaign</td><td></td></tr><tr><td>Actions</td><td><p>The following options are available:</p><ol><li><strong>Launch:</strong> Launch the scheduled or save for a later campaign immediately.</li><li><strong>View Report:</strong> Access detailed reports of a campaign. You can find more information about the report details here.</li><li><strong>Delete:</strong> Delete the campaign report.</li><li><strong>Cancel:</strong> Use it to prevent the campaign email from being sent to users who have not yet received it.</li><li><strong>Download Individual Printout:</strong> Download the printout PDF file that contains the quishing campaign for all of the selected target users</li></ol></td><td></td></tr></tbody></table>

## Create a Campaign

Click on **"+** **NEW"** on the **Quishing Simulator > Campaign Manager** page to create a new quishing campaign to set up to launch target users in four simple steps:

**First, select the type of the quishing campaign;** either you can send the quishing campaign via email by selecting the **"Email Campaign"** or print out the quishing campaign to deliver as paper to your employees by selecting the **"Individual Printout Campaign"**.

And then please follow the steps below to set up the rest of the campaign settings.

* Campaign Settings
* Quishing Scenarios
* Target Audience
* Delivery Settings
* Campaign Summary

{% hint style="warning" %}
Before launching a quishing campaign, you must create a [target user group](https://doc.keepnetlabs.com/next-generation-product/platform/company/target-users).
{% endhint %}

### Campaign Settings

Enter basic information about this campaign. The components of the **Campaign** **Info** page are explained below.

<table><thead><tr><th width="154.66855801213072"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Campaign Name</td><td>The name of the campaign</td><td></td></tr><tr><td>Tracking Duration</td><td>Select the time period you want to keep this campaign active</td><td></td></tr><tr><td>Mark As Test</td><td>Select this box if you want to exclude the results of the campaign from the overall company score</td><td></td></tr></tbody></table>

### Quishing Scenarios

Select one scenario to send selected target users or select multiple quishing scenarios to distribute randomly.

{% hint style="info" %}
If multiple scenarios are selected, each user will receive a random scenario.
{% endhint %}

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Scenarios</td><td>Select scenarios to be sent to selected target users.</td><td></td></tr><tr><td>Type</td><td>Filter scenarios according to their method type.</td><td></td></tr><tr><td>Language</td><td>Filter scenarios according to their language.</td><td></td></tr><tr><td>Difficulty</td><td>Filter scenarios according to their difficulty level.</td><td></td></tr><tr><td>Training</td><td><p>Select training and send the training via email or redirect it immediately once the user falls for a phishing campaign.</p><p><strong>Enrollment:</strong> Users can either be redirected to the training immediately with the <strong>"Start Training Immediately"</strong> option or opt to receive the training later through an email with the <strong>"Enroll via Email Notification"</strong> option.</p><ul><li><strong>Click Only:</strong> The users who click the phishing link will be redirected to the training immediately, or a training email will sent later.</li><li><strong>Data Submission:</strong> The users who submit their credentials will be redirected to the training immediately, or a training email will sent later.</li><li><strong>MFA:</strong> The users who submit their MFA code will be redirected to the training immediately, or a training email will sent later.</li></ul><p><strong>Reminder:</strong> The users who don't complete the training will receive additional reminder emails.</p><p><strong>Certificate:</strong> The users who complete the training will receive a certificate.<br><br><strong>Edit Training Redirect Page:</strong> The training redirect page is written in English by default, but it can be fully customized. The users who once fall to simulation will be redirected to the training redirection page if you selected the 'Start Training Immediately' option.</p></td><td></td></tr></tbody></table>

### Target Audience

Select target groups for your campaign.

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Target Audience</td><td>Choose one or several recipient groups to send the selected phishing scenarios to.</td><td></td></tr><tr><td>Limit Recipients</td><td><ul><li><strong>Send only to users with an active phishing reporter add-in:</strong> Select this option to send the campaign only to users with an active phishing reporter plug-in.</li><li><strong>Send this campaign to randomly selected users:</strong> Choose this option to send the phishing campaign to randomly selected users within the target group. You have the option to choose a percentage of the group or a specific number of users.</li></ul></td><td></td></tr></tbody></table>

### Delivery Settings

Set email delivery options.

The components of the **Delivery** **Settings** page are explained below.

{% hint style="info" %}
You can skip this step if you have chosen the "Individual Printout Campaign" option for your quishing campaign.
{% endhint %}

<table><thead><tr><th width="142"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Email Delivery</td><td>Choose the email delivery settings, which can be either <a href="../company/company-settings/smtp-settings">SMTP</a> or <a href="../company/company-settings/direct-email-creation">DEC</a>.</td><td></td></tr><tr><td>Frequency</td><td>If you have <strong>selected</strong> <strong>multiple</strong> <strong>scenarios</strong>, you can choose how often you would like to send the scenarios randomly to the selected groups.</td><td></td></tr><tr><td>Schedule</td><td><p>The date and time of the campaign launch:</p><ul><li><strong>Save for later:</strong> Check this box if you want to send the campaign later. To send now, click the "<strong>Now</strong>" button after opening the date and time pop-up.</li><li><strong>Schedule for:</strong> Check this box to begin the campaign on a specific date.</li></ul></td><td></td></tr><tr><td>Distribution</td><td><p>When you launch a quishing campaign to a large audience, this feature ensures that the emails are not blocked or quarantined by the recipient's email server. It achieves this by distributing the emails over a period of time rather than sending them all at once.</p><ul><li><strong>Send emails when the campaign starts:</strong> As the campaign begins, emails are immediately dispatched to the selected target users.</li><li><p><strong>Send emails on defined days and hours:</strong> You can determine the specific days and times when emails will be delivered to the chosen target users.</p><ul><li><strong>Sending limit per batch:</strong> Define the quantity of emails you'd like to send to the recipients in each batch during the chosen days and times.</li><li><strong>Send emails with delay every:</strong> Decide on the duration of the pause between sending each batch, whether it's in seconds, minutes, or hours.</li></ul></li></ul><p>The system will automatically determine and show you the duration required to send the campaign to the designated number of recipients based on your chosen settings.</p></td><td></td></tr></tbody></table>

### Campaign Summary

All of the quishing campaign details are easily accessible on one page, along with a preview of the quishing scenario and the landing page.

The components of the **Campaign** **Summary** page are explained below.

<table><thead><tr><th width="161"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Name</td><td>Name of the quishing campaign</td><td></td></tr><tr><td>Method</td><td>The selected scenarios method types.</td><td></td></tr><tr><td>Difficulty</td><td>It shows how tricky the quishing campaign will be to spot. "Easy" means it's simpler to recognize as a test.</td><td></td></tr><tr><td>Tracking Duration</td><td>It shows how long you want to keep this campaign active.</td><td></td></tr><tr><td>Starting</td><td>When the campaign will be launched.</td><td></td></tr><tr><td>Sending Limit</td><td>The quantity of emails you'd like to send to the recipients in each batch.</td><td></td></tr><tr><td>Email Delivery</td><td>The selected email delivery option, which can be either <a href="../company/company-settings/smtp-settings">SMTP</a> or <a href="../company/company-settings/direct-email-creation">DEC</a>.</td><td></td></tr><tr><td>Frequency</td><td>If you have <strong>selected</strong> <strong>multiple</strong> <strong>scenarios</strong>, it shows how often you would like to send the scenarios randomly to the selected groups.</td><td></td></tr><tr><td>Target Users</td><td><p>The target users who will receive the phishing email.</p><p>Click on <strong>Preview</strong> to see the target users count and target user groups.</p></td><td></td></tr><tr><td>Email to be sent</td><td><p>The phishing email template selected for the campaign</p><p>Click <strong>Preview</strong> to see how it will be displayed in the target users’ inboxes</p></td><td></td></tr><tr><td>Landing page for users who click on the phishing link</td><td><p>The landing page template selected for the campaign.</p><p>Click <strong>Preview</strong> to see how it will be displayed in the target users’ browsers</p></td><td></td></tr></tbody></table>

Click **Start** to launch the campaign.

Click **Cancel** to rescind all of the actions, then click **Quit** in the pop-up window. If you want to make additional edits, click **Continue** **Editing**.

## Video Tutorial

This tutorial covers the **Quishing** **Campaign** **Manager** with options such as **Schedule**, **Multiple** **Target** **Groups**, **SMTP** **Delay**, **Expire** **Date**, **Multiple** **Scenarios,** or **Randomize** to allow you to modify various elements to suit your needs.

{% embed url="<https://youtu.be/h13p5CtQ9Rg>" %}

## **FAQ**

### Q: Why do quishing emails contain the "X-MS-Exchange-Organization-SkipSafeLinksProcessing: true" header?

A: This header prevents Microsoft Defender from analyzing links in quishing emails, ensuring accurate test results and preventing false positives.
