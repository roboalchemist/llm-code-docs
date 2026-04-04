# Source: https://doc.keepnetlabs.com/next-generation-product/platform/smishing-simulator/smishing-campaign-manager.md

# Smishing Campaign Manager

The campaign manager assists admins in launching smishing campaigns to the end users. The settings such as **Save for Later, Send Now, Schedule, Target Groups, Distribution, Scenarios** or **Message Settings** are set up from here before launching the campaign to end users.

## Smishing Campaign Manager

This section describes the basic functionalities of the campaign manager page, where you can find all the campaign reports from the **Smishing > Campaign Manager** menu.

The components of the campaign manager page are explained below.

<table data-header-hidden><thead><tr><th width="124.5"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Campaign Name</td><td>Name of the smishing campaign</td><td></td></tr><tr><td>Target Users</td><td>Number of target users to whom the phishing scenario was sent</td><td></td></tr><tr><td>Status</td><td>Current status of the phishing campaign (idle, running, completed, paused, error, canceled)</td><td></td></tr><tr><td>Scenarios</td><td>Represents how many scenarios has been selected for the campaign.</td><td></td></tr><tr><td>Method</td><td>The selected scenarios method types.</td><td></td></tr><tr><td>Created By</td><td>Name of the company that created the phishing campaign</td><td></td></tr><tr><td>Date Created</td><td>Date and time that the phishing campaign was created</td><td></td></tr><tr><td>Last Launch</td><td>Date and time that the phishing campaign was launched</td><td></td></tr><tr><td>Actions</td><td><p>Following options are available:</p><ol><li><strong>Preview:</strong> Click it to preview the scenarios attached to the campaign.</li><li><strong>Edit:</strong> Click it to customize the campaign and relaunch.</li><li><strong>Create New Instance:</strong> Click it to relaunch to target groups with original campaign settings.</li><li><strong>Delete:</strong> Click it to delete the campaign and reports from the platform.</li></ol></td><td></td></tr></tbody></table>

## Campaign Instances

This section explains the details of campaign reports, where you can access them by clicking the “**Instances**” button on the campaign manager page.

The components of the **Campaign Instances** page are explained below.

<table data-header-hidden><thead><tr><th width="162"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Schedule</td><td>The date and time the campaign will launch</td><td></td></tr><tr><td>Target Users</td><td>The number of scheduled target users</td><td></td></tr><tr><td>Status</td><td><p>Current status of the campaign</p><p>(idle, running, completed, paused, cancelled, error)</p></td><td></td></tr><tr><td>Date Created</td><td>The creation date of the campaign</td><td></td></tr><tr><td>Actions</td><td><p>Following options are available:</p><ol><li><strong>Launch:</strong> Launch the scheduled or save for later campaign immeditelay.</li><li><strong>View Report:</strong> Access detailed reports of a campaign You can find more information about the report details here.</li><li><strong>Delete:</strong> Delete the campaign report.</li><li><strong>Pause:</strong> Suspend email delivery in the active campaign.</li><li><strong>Resume:</strong> Resume email delivery in the paused campaign.</li><li><strong>Stop:</strong> Terminate active email deliveries in the running campaign.</li></ol></td><td></td></tr></tbody></table>

## How to send a Smishing Campaign

Click on **+ NEW** on the **Smishing > Campaign Manager** page to create a new smishing campaign within these simple steps:

* Smishing Campaign Settings
* Smishing Scenarios
* Target Groups
* SMS Settings
* Campaign Summary

{% hint style="info" %}
Before launching a smishing campaign, you must [create a target user](https://doc.keepnetlabs.com/next-generation-product/platform/company/target-users) with users who must have phone numbers on the **Company > Target Users** page.
{% endhint %}

### Campaign Settings

Select a name for the campaign, when it will be sent, and if you want this campaign to be excluded from your reports.

The components of the **Campaign Settings** page are explained below.

<table data-header-hidden><thead><tr><th width="174.5"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Campaign Name</td><td>The name of the campaign</td><td></td></tr><tr><td>Tracking Duration</td><td>Select the time period you want to keep this campaign active</td><td></td></tr><tr><td>Mark As Test</td><td>Check this if you wish to exclude this campaign from your reports</td><td></td></tr></tbody></table>

### Smishing Scenarios

Select one scenario to send selected target users or select multiple phishing scenarios to distribute randomly.

{% hint style="info" %}
If multiple scenarios are selected, each user will receive a random scenario.
{% endhint %}

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Scenarios</td><td>Select scenarios to be sent to selected target users.</td><td></td></tr><tr><td>Type</td><td>Filter scenarios according to their method type.</td><td></td></tr><tr><td>Language</td><td>Filter scenarios according to their language.</td><td></td></tr><tr><td>Difficulty</td><td>Filter scenarios according to their difficulty level.</td><td></td></tr><tr><td>Training</td><td><p>Select training and send the training via email or redirect it immediately once the user falls for a phishing campaign.</p><p><strong>Enrollment:</strong> Users can either be redirected to the training immediately with the <strong>"Start Training Immediately"</strong> option or opt to receive the training later through an email with the <strong>"Enroll via Email Notification"</strong> option.</p><ul><li><strong>Click Only:</strong> The users who click the phishing link will be redirected to the training immediately, or a training email will sent later.</li><li><strong>Data Submission:</strong> The users who submit their credentials will be redirected to the training immediately, or a training email will sent later.</li><li><strong>MFA:</strong> The users who submit their MFA code will be redirected to the training immediately, or a training email will sent later.</li></ul><p><strong>Reminder:</strong> The users who don't complete the training will receive additional reminder emails.</p><p><strong>Certificate:</strong> The users who complete the training will receive a certificate.</p></td><td></td></tr></tbody></table>

### Target Audience

Choose one or several recipient groups to send the selected phishing scenarios to.

<table data-header-hidden><thead><tr><th width="158"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Group Name</td><td>The name of the target group you wish to send the campaign to</td><td></td></tr><tr><td>Company Name</td><td>The name of the company that created the target group</td><td></td></tr><tr><td>Priority</td><td>Specify the priority information of the target user. If the priority is high, the user will get the email first.</td><td></td></tr><tr><td>Date Created</td><td>The date the user was created</td><td></td></tr><tr><td>Limit Recipients</td><td><strong>Send this campaign to randomly selected users:</strong> Choose this option to send the phishing campaign to randomly selected users within the target group. You have the option to choose a percentage of the group or a specific number of users.</td><td></td></tr></tbody></table>

When you select a specific target group, you will see the summary table of users on the right side of the target audience page.

<table data-header-hidden><thead><tr><th width="135"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>First Name</td><td>User’s first name</td><td></td></tr><tr><td>Last Name</td><td>User’s surname</td><td></td></tr><tr><td>Email</td><td>User’s email address</td><td></td></tr></tbody></table>

Once you have selected the target group you wish to launch the camping to, click **Next**.

### SMS Settings

Set up the following fields correctly.

<table><thead><tr><th width="172.66855801213072"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Sender Phone Number</td><td>Select the phone number from the dropdown menu that the end user will see when receiving the smishing text.<br><br>When you select multiple numbers, messages will be sent from a randomly chosen number during delivery.</td><td></td></tr><tr><td>Frequency</td><td>If you have <strong>selected</strong> <strong>multiple</strong> <strong>scenarios</strong>, you can choose how often you would like to send the scenarios randomly to the selected groups.</td><td></td></tr><tr><td>Schedule</td><td><p>The date and time of the campaign launch:</p><ul><li><strong>Save for later:</strong> Check this box to send the campaign later. To send now, click on the "<strong>Now</strong>" button after opening the date and time pop-up.</li><li><strong>Schedule for:</strong> Check this box to begin the campaign on a specific date.</li><li><strong>Enable</strong> <strong>Region-Aware Time Zone Delivery:</strong> Send SMS simulation messages according to the target users' local time zones. If a user’s time zone is not defined, the email will be sent based on the organization's primary time zone.</li></ul></td><td></td></tr><tr><td>Distribution</td><td><p>When you launch a smishing campaign to a large audience, this feature ensures that the emails are not blocked or quarantined by the recipient's email server. It achieves this by distributing the emails over a period of time rather than sending them all at once.</p><ul><li><strong>Send emails when the campaign starts:</strong> As the campaign begins, emails are immediately dispatched to the selected target users.</li><li><p><strong>Send emails on defined days and hours:</strong> You can determine the specific days and times when emails will be delivered to the chosen target users.</p><ul><li><strong>Sending limit per batch:</strong> Define the quantity of emails you'd like to send to the recipients in each batch during the chosen days and times.</li><li><strong>Send emails with delay every:</strong> Decide on the duration of the pause between sending each batch, whether it's in seconds, minutes, or hours.</li></ul></li></ul><p>The system will automatically determine and show you the duration required to send the campaign to the designated number of recipients based on your chosen settings.</p></td><td></td></tr></tbody></table>

### Campaign Summary

All of the details of the smishing campaign are easily accessible on one page, along with a preview of the vishing call steps.

The components of the **Campaign Summary** page are explained below.

<table data-header-hidden><thead><tr><th width="186"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Campaign Name</td><td>The name of the campaign.</td><td></td></tr><tr><td>Method</td><td>The smishing scenario method selected.</td><td></td></tr><tr><td>Difficulty</td><td>The difficulty level of the smishing scenario.</td><td></td></tr><tr><td>Starting</td><td>The date and time that the vishing campaign will start distribution.</td><td></td></tr><tr><td>Duration</td><td>The time period this campaign will be active.</td><td></td></tr><tr><td>Sender Phone Number</td><td>The phone number that end users will see when receiving the smishing scenario.</td><td></td></tr><tr><td>Target Users</td><td>A preview of the target users selected.</td><td></td></tr><tr><td>Smishing Scenarios</td><td><p>A preview of the one or multiple smishing scenarios selected.</p><p>For multiple scenarios, click on the name of the scenario to preview the selected text message and landing page.</p></td><td></td></tr></tbody></table>

Click **Start** to launch the campaign.

Click **Cancel** to rescind all of the actions, then click **Quit** in the pop-up window. If you want to make additional edits, click **Continue Editing**.

## Video Tutorial

This video tutorial covers the **Campaign** **Manager** options such as **Save for Later, Send Now, Schedule, Target Groups, Distribution, Scenarios,** or **Message Settings** to allow you to modify various elements to suit your needs.

{% embed url="<https://www.youtube.com/watch?index=2&list=PLTfpxvprC-_xwsgbaZw2ilbIeRUZtFnFn&v=qzB-9OiTo1M>" %}

## FAQ

### Why does an SMS go to the spam folder when I launch an SMS phishing campaign?

1. A phishing URL could cause the SMS simulation to be marked as spam.
2. The phone number was reported as suspicious.
3. Keywords that impersonate big names, like Microsoft or Outlook, etc.

#### Solutions:

1. Test your Smishing simulation campaign on various GSM providers to ensure it is not marked as spam.
2. If it goes to spam, first check the URL to ensure it doesn't look suspicious. For example, outlook.company.com is suspicious; use email-login.company.com instead.
3. Change the sender phone number to use a number never detected as suspicious by carriers.

### How do you ensure that messages arrived at destination?

Yes, we provide delivery reports in real time. You can make sure the phone number has got the SMS test or failed to delivery with reason by following the [Smishing Report > Sending Report > Delivery Status](https://doc.keepnetlabs.com/next-generation-product/platform/smishing-campaign-reports#sending-report)

### Which protocols are used for the exchange of SMS?

The primary protocols used for the exchange of SMS messages include SMPP (Short Message Peer-to-Peer) and HTTP/HTTPS for API communications. SMPP is a standard protocol for exchanging SMS messages between SMS peer entities such as short message service centers, while HTTP/HTTPS protocols are used for API-based interactions, enabling secure communication over the internet.

### Do you have any document testifying that all data collected is destructed after a certain amount of time?

Keepnet adheres to strict data privacy and security protocols, ensuring that all collected data is managed responsibly. According to our [data retention policy](https://doc.keepnetlabs.com/resources/compliance#data-retention-and-disposal-procedure), all data collected through our services, including the SMS phishing simulator, is securely destroyed after a predetermined period, in compliance with applicable data protection regulations. We can provide documentation detailing our data destruction procedures and timelines upon request, highlighting our commitment to maintaining the privacy and security of our users' data.

<br>
