# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/phishing-campaign-manager.md

# Phishing Campaign Manager

A phishing campaign can be launched to target users in two ways. The **Fast** **Launch** option allows you to initiate a phishing campaign quickly and easily, without having to designate any settings. However, if you prefer customization, advanced features are available to refine the campaign using the **Campaign** **Manager** option, such as **Schedule**, **Multiple** **Target** **Groups**, **SMTP** **Delay**, **Expire** **Date**, **Multiple** **Scenarios,** and **Randomize** to allow you to modify a variety of elements to suit your needs.

## Campaign Manager Components

The components of the **Campaign** **Manager** page are explained below.

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Campaign Name</td><td><p>The name of the campaign</p><p><strong>Instance</strong> information indicating the number of times the campaign has been launched is available next to the campaign name</p></td><td></td></tr><tr><td>Target Users</td><td>The target users who will receive the phishing email</td><td></td></tr><tr><td>Status</td><td><p><strong>Status</strong> information of the campaign. (idle, running, completed, paused, canceled, error)</p><ul><li><strong>Idle</strong> <strong>=</strong> The campaign is launched and has not started yet</li><li><strong>Running</strong> <strong>=</strong> The campaign is in progress</li><li><strong>Completed</strong> <strong>=</strong> The campaign is delivered to all target users</li><li><strong>Paused</strong> <strong>=</strong> The campaign has been temporarily suspended</li><li><strong>Canceled</strong> <strong>=</strong> The campaign has been withdrawn</li><li><strong>Error</strong> <strong>=</strong> The status field displays an error message if there is a delivery problem</li></ul></td><td></td></tr><tr><td>Scenarios</td><td>Shows how many scenarios has been launched in the campaign.</td><td></td></tr><tr><td>Scenario Distribution</td><td>Shows how scenarios are assigned to users (e.g., same random scenario for all, different random scenarios for each, AI Ally selects scenario for each user or manual selection).</td><td></td></tr><tr><td>Method</td><td>Method type of the campaign</td><td></td></tr><tr><td>Training</td><td>List the phishing campaigns that were launched with training content.</td><td></td></tr><tr><td>Created By</td><td>The source of the phishing campaign (system, custom)</td><td></td></tr><tr><td>Email Delivery</td><td>The selected email delivery option, <a href="../company/company-settings/smtp-settings">SMTP</a> or <a href="../company/company-settings/direct-email-creation">DEC</a> rule.</td><td></td></tr><tr><td>Date Created</td><td>The date and time the campaign was created</td><td></td></tr><tr><td>Last Launch</td><td>The date of the most recent use of the campaign</td><td></td></tr></tbody></table>

### Actions

These settings give you the ability to **edit**, **preview**, or **delete** campaigns, as well as create new instances. You can also resend a campaign to specific users.

Click on the **three dots** “︙” button under the **Action** heading to adjust the following features.

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Preview</td><td>Preview the campaign details, including the Email Template, Landing Page, and any associated training content that was selected.</td><td></td></tr><tr><td>Edit</td><td>Change the settings of the relevant campaign</td><td></td></tr><tr><td>Create New Instance</td><td>Create a copy of the same campaign and launch it to the different target groups.</td><td></td></tr><tr><td>Delete</td><td>Delete the campaign</td><td></td></tr></tbody></table>

## Campaign Instances

In the **Campaign** **Name** column, the **Instances** option will provide details of the campaign, such as how many times it has been launched and the users targeted.

The components of the **Campaign** **Instances** page are explained below.

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Frequency</td><td>If you have selected multiple scenarios, it shows how often the system will send the selected scenarios randomly to the selected groups.</td><td></td></tr><tr><td>Start Time</td><td>The date and time the campaign is launched</td><td></td></tr><tr><td>Target Users</td><td>The total target users that the campaign was launched to.</td><td></td></tr><tr><td>Status</td><td>Current status of the campaign (idle, running, completed, paused, canceled, error)</td><td></td></tr><tr><td>Date Created</td><td>The creation date of the campaign</td><td></td></tr></tbody></table>

### Actions

You can delete, pause, or resume a paused instance on the **Campaign** **Instances** page as well as you also have the option to view detailed reports of an instance or resend the campaign.

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Launch</td><td>Resend a campaign to a selected group</td><td></td></tr><tr><td>View Report</td><td>Access detailed reports of a campaign You can find more information about the report details <a href="phishing-campaign-reports">here</a></td><td></td></tr><tr><td>Delete</td><td>Delete the campaign report</td><td></td></tr><tr><td>Cancel</td><td>Terminate an active campaign. The system won't send the phishing email to the users who haven't received it.</td><td></td></tr></tbody></table>

## Create a Campaign

Click on **"+** **NEW"** on the **Phishing Simulator > Campaign Manager** page to create a new phishing campaign to set up to launch target users in four simple steps:

* Campaign Settings
* Phishing Scenarios
* Target Audience
* Delivery Settings
* Campaign Summary

{% hint style="warning" %}
Before launching a phishing campaign, you must create a [target user group](https://doc.keepnetlabs.com/next-generation-product/platform/company/target-users).
{% endhint %}

### Campaign Settings

Enter basic information about this campaign. The components of the **Campaign** **Info** page are explained below.

<table><thead><tr><th width="154.66855801213072"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Campaign Name</td><td>The name of the campaign</td><td></td></tr><tr><td>Hyper-Personalization</td><td><p>This feature allows you to tailor simulation scenarios based on the recipient’s language preferences. You can choose from two options when launching a campaign:</p><ul><li><strong>Send in a manually selected language:</strong> Select a specific language to send the scenario to all recipients, regardless of their preferred language settings.</li><li><strong>Send in the target users' preferred language:</strong> Deliver scenarios in each recipient’s preferred language. If a user has no preferred language set, the scenario will be sent in the company's default language.</li></ul></td><td></td></tr><tr><td>Smart Grouping</td><td>Users who clicked the campaign are automatically added to the selected target group.</td><td></td></tr><tr><td>Tracking Duration</td><td>Select the time period you want to keep this campaign active</td><td></td></tr><tr><td>Mark As Test</td><td>Select this box if you want to exclude the results of the campaign from the overall company score</td><td></td></tr><tr><td>Reply Tracking</td><td>Enter custom reply-to address to track replies. Please click <a href="#how-to-track-people-who-reply-to-phishing-simulation-emails">here</a> to learn more.</td><td></td></tr></tbody></table>

### Phishing Scenarios

Select one scenario to send selected target users or select multiple phishing scenarios to distribute randomly.

{% hint style="info" %}
If multiple scenarios are selected, each user will receive a random scenario.
{% endhint %}

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Scenarios</td><td>Select scenarios to be sent to selected target users.</td><td></td></tr><tr><td>Type</td><td>Filter scenarios according to their method type.</td><td></td></tr><tr><td>Language</td><td>Filter scenarios according to their language.</td><td></td></tr><tr><td>Difficulty</td><td>Filter scenarios according to their difficulty level.</td><td></td></tr><tr><td>Category</td><td>Filter scenarios according to their threat type.</td><td></td></tr><tr><td>Scenario Distribution</td><td><p>Select how scenarios will be sent to users:</p><ul><li><strong>Select</strong> <strong>scenarios</strong> <strong>manually:</strong> The selected scenarios by the admin will be sent to target users.</li><li><strong>Select</strong> <strong>random</strong> <strong>scenarios</strong> <strong>for</strong> <strong>each</strong> <strong>user</strong>: The platform will randomly select scenarios from the scenarios menu for each user. Use filters (Type, Language, Difficulty, and Category) to list scenarios from which the platform will pick randomly.</li><li><strong>Select</strong> <strong>the</strong> <strong>same</strong> <strong>random</strong> <strong>scenario</strong> <strong>for</strong> <strong>all</strong> <strong>users</strong>: The platform will randomly select one scenario from the scenarios menu for all users. Use filters (Type, Language, Difficulty, and Category) to list scenarios from which the platform will pick randomly.</li><li><p><strong>AI Ally selects scenario for each user:</strong> If you filter scenarios by Type, Language, Difficulty, or Category and then proceed to select target users, the AI Ally will choose a scenario from the filtered options for each user.</p><ul><li>The selection will be based on each user's specific attributes, such as their Phone Number, Timezone, Company Country, and Department Name to ensure the most relevant scenario is sent to each user.</li><li>As information, Personally Identifiable Information (PII) is never shared with the AI model.</li></ul></li></ul></td><td></td></tr><tr><td>Training</td><td><p>Select training and send the training via email or redirect it immediately once the user falls for a phishing campaign.</p><p><strong>Enrollment:</strong> Users can either be redirected to the training immediately with the <strong>"Start Training Immediately"</strong> option or opt to receive the training later through an email with the <strong>"Enroll via Email Notification"</strong> option.</p><ul><li><strong>Click Only:</strong> The users who click the phishing link will be redirected to the training immediately, or a training email will sent later.</li><li><strong>Data Submission:</strong> The users who submit their credentials will be redirected to the training immediately, or a training email will sent later.</li><li><strong>Attachment:</strong> The users who open the attached file will receive the training via email.</li><li><strong>MFA:</strong> The users who submit their MFA code will be redirected to the training immediately, or a training email will sent later.</li></ul><p><strong>Reminder:</strong> The users who don't complete the training will receive additional reminder emails.</p><p><strong>Certificate:</strong> The users who complete the training will receive a certificate.<br><br><strong>dit Training Redirect Page:</strong> The training redirect page is written in English by default, but it can be fully customized. The users who once fall to simulation will be redirected to the training redirection page if you selected the 'Start Training Immediately' option.</p></td><td></td></tr></tbody></table>

### Target Audience

Select target groups for your campaign.

<table><thead><tr><th width="150"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Target Audience</td><td>Choose one or several recipient groups to send the selected phishing scenarios to.</td><td></td></tr><tr><td>Limit Recipients</td><td><ul><li><strong>Send only to users with an active phishing reporter add-in:</strong> Select this option to send the campaign only to users with an active phishing reporter plug-in.</li><li><strong>Send this campaign to randomly selected users:</strong> Choose this option to send the phishing campaign to randomly selected users within the target group. You have the option to choose a percentage of the group or a specific number of users.</li></ul></td><td></td></tr></tbody></table>

### Delivery Settings

Set email delivery options.

The components of the **Delivery** **Settings** page are explained below.

{% hint style="info" %}
If multiple companies are selected and DEC is chosen for email delivery, but a customer doesn't have DEC configuration, or it fails, the system will use the default SMTP in the customer's company profile to sending simulation emails to the target users.
{% endhint %}

<table><thead><tr><th width="142"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Email Delivery</td><td>Choose the email delivery settings, which can be either <a href="../company/company-settings/smtp-settings">SMTP</a> or <a href="../company/company-settings/direct-email-creation">DEC</a>.</td><td></td></tr><tr><td>Frequency</td><td>If you have <strong>selected</strong> <strong>multiple</strong> <strong>scenarios</strong>, you can choose how often you would like to send the scenarios randomly to the selected groups.</td><td></td></tr><tr><td>Schedule</td><td><p>The date and time of the campaign launch:</p><ul><li><strong>Save for later:</strong> Check this box if you want to send the campaign later. To send now, click the "<strong>Now</strong>" button after opening the date and time pop-up.</li><li><strong>Schedule for:</strong> Check this box to begin the campaign on a specific date.</li><li><strong>Enable Region-Aware Time Zone Delivery:</strong> Send phishing simulation emails based on the target users' time zones. Users without a defined time zone will receive the email based on the organization's main time zone.</li></ul></td><td></td></tr><tr><td>Distribution</td><td><p>When you launch a phishing campaign to a large audience, this feature ensures that the emails are not blocked or quarantined by the recipient's email server. It achieves this by distributing the emails over a period of time rather than sending them all at once.</p><ul><li><strong>Send emails when the campaign starts:</strong> As the campaign begins, emails are immediately dispatched to the selected target users.</li><li><p><strong>Send emails on defined days and hours:</strong> You can determine the specific days and times when emails will be delivered to the chosen target users.</p><ul><li><strong>Sending limit per batch:</strong> Define the quantity of emails you'd like to send to the recipients in each batch during the chosen days and times.</li><li><strong>Send emails with delay every:</strong> Decide on the duration of the pause between sending each batch, whether it's in seconds, minutes, or hours.</li></ul></li></ul><p>The system will automatically determine and show you the duration required to send the campaign to the designated number of recipients based on your chosen settings.</p></td><td></td></tr></tbody></table>

{% hint style="info" %}

* Handles thousands to millions of emails per day via **SMTP**, with a delivery speed of up to 100,000 emails per minute under ideal conditions.
* If **Direct Email Campaign (DEC)** is selected, the sending limit is **130,000 requests per 10 seconds**, but this is configurable based on requirements.
  {% endhint %}

### Campaign Summary

All of the phishing campaign details are easily accessible on one page, along with a preview of the phishing scenario and the landing page.

The components of the **Campaign** **Summary** page are explained below.

<table><thead><tr><th width="167"></th><th width="580.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Campaign Info</td><td>The name of the campaign, the difficulty level, and the phishing technique employed. (Data Submission, Click only, Attachment)</td><td></td></tr><tr><td>Settings</td><td>Date and time of the campaign, the number of emails to be sent, and the email delivery info</td><td></td></tr><tr><td>Other</td><td>Other additional enabled settings will appear here such as "mark as test" option.</td><td></td></tr><tr><td>Target Users</td><td><p>The target users who will receive the phishing email.</p><p>Click on <strong>Preview</strong> to see the target users count and target user groups.</p></td><td></td></tr><tr><td>Email that will be sent to users</td><td><p>The phishing email template selected for the campaign</p><p>Click <strong>Preview</strong> to see how it will be displayed in the target users’ inboxes</p></td><td></td></tr><tr><td>Landing page for users who click on the phishing link</td><td><p>The landing page template selected for the campaign.</p><p>Click <strong>Preview</strong> to see how it will be displayed in the target users’ browsers</p></td><td></td></tr><tr><td>Schedule</td><td>By enabling the frequency feature, you can view the date and time when the scenarios will be delivered to the selected groups.</td><td></td></tr></tbody></table>

Click **Start** to launch the campaign.

Click **Cancel** to rescind all of the actions, then click **Quit** in the pop-up window. If you want to make additional edits, click **Continue** **Editing**.

## How to Track People Who Reply to Phishing Simulation Emails

The "**Reply** **Tracking**" feature allows system administrators to monitor and identify users who respond to phishing simulation emails. This not only helps in evaluating employee awareness but also provides valuable insights into how users engage with suspicious emails. By understanding user behavior, organizations can tailor their training efforts and mitigate potential risks more effectively.

#### Why Use the Reply Tracking Feature?

* **Identify High-Risk Users**: Track which employees engage with phishing emails by replying, so you can provide targeted training to address their vulnerabilities.
* **Gain Behavioral Insights**: Understand what employees typically write when responding to phishing emails, which can reveal potential patterns of risky behavior.
* **Improve Security Awareness**: Use the data collected to refine your awareness campaigns and educate employees on best practices for handling suspicious emails.

#### How to Enable and Use the Reply Tracking Feature

Follow the steps below to enable and utilize this feature:

1. Navigate to **Phishing Simulator > Campaign Manager**, then click the **+ NEW** button.
2. Fill in the required fields. For more details on setting up a campaign, refer to the [beginning of the documentation](#create-a-campaign).
3. Enable the **"Reply Tracking"** option.
4. Enter a **custom email name** and **select one of the simulation domains** provided by the platform.
5. To review the content of reply emails, enable the **"Save reply email content for review"** option. This allows you to view the content of the replies directly in the campaign report.
6. Click **Next** and select the scenario you wish to launch for your employees.
7. Configure the remaining settings as needed. For detailed guidance, refer to the **"**[**Create a Campaign**](#create-a-campaign)**"** section in the documentation.

Once your campaign is live, any employee who replies to the simulation email will appear in the campaign report under the **Replied** menu. You can review the details of their replies if you have enabled the **"Save reply email content for review"** option.

For more information about campaign reports, refer to the full documentation [here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/phishing-campaign-reports).

## **How to Launch Scenarios Based on Users’ Preferred Language**

The **Preferred Language** feature allows you to send phishing simulation scenarios in each recipient’s preferred language. If a preferred language is not set, the system will default to the company's preferred language.

#### **Setting Up Preferred Languages for Users**

Before launching a campaign with this feature, you must assign preferred languages to users:

1. Navigate to **Company > Target Users**.
2. Assign a preferred language to each user.
3. Add these users into a **Target Group**.

#### Create Multi-Language Scenario with Localization

Before creating a campaign that sends a scenario in your users’ preferred languages, make sure the scenario includes a localized **email template** and **landing page**. This ensures each employee receives both assets in their own preferred language.

1. Create or duplicate an [email template](https://doc.keepnetlabs.com/next-generation-product/platform/manage-phishing-scenarios/email-templates#how-to-add-a-new-email-template), then add localized versions for the required languages using the **localization** feature.
2. Create or duplicate a [landing page](https://doc.keepnetlabs.com/next-generation-product/platform/manage-phishing-scenarios/landing-pages#how-to-add-a-new-landing-page-template), then add localized versions for the required languages using the **localization** feature.
3. Create a **scenario** and add your localized email template and landing page.

You can now proceed to the next section to launch your scenario.

#### **Enabling Preferred Language in a Campaign**

To launch a campaign using this feature:

1. Navigate to **Phishing Simulator > Campaign Manager**.
2. Click the **+ NEW** button to create a new campaign.
3. In the **Hyper-Personalization** section, select:
   * **"Send in the target users’ preferred language"**\
     → The system will send scenarios in each recipient’s preferred language. If no preferred language is set, the company's default language will be used.
4. Complete the remaining campaign fields and settings as needed.
5. Click **Next** to proceed through **scenario** **selection**, **target** **groups**, and **other** **customizations**.
6. Click **Launch** to start the campaign.

#### **How Scenarios Are Assigned Based on Language**

* If a scenario template is available in the user's preferred language, they will receive that version.
* If a scenario template is not available in the user’s preferred language, the system will send the scenario in the **company’s default language**.
* If no scenario template matches either the user's preferred language or the company’s default language, the system will prompt you to select appropriate language versions before launch.

This ensures that users receive scenarios in the most relevant language for them, improving the effectiveness of phishing simulations.

## Video Tutorial

This tutorial covers the **Campaign** **Manager** options such as **Schedule**, **Multiple** **Target** **Groups**, **SMTP** **Delay**, **Expire** **Date**, **Multiple** **Scenarios,** and **Randomize** to allow you to modify various elements to suit your needs.

{% embed url="<https://www.youtube.com/watch?v=k3yPzdgn604>" %}

## FAQ

### Q: Is it possible to remove the phishing simulation email from target users’ inboxes once the campaign has been launched?

A: Yes. The Incident Responder investigation feature gives you the capability to delete the phishing simulation email.

### Q: Can I cancel the phishing simulation after the campaign has been launched?

A: No. You can only cancel the campaign before the launch date.

### Q: Can I change the date and time of the campaign after it has been scheduled?

A: Yes. You can adjust the campaign settings at any time before the launch date.

### Q: Is there a way to exclude phishing campaigns from showing up in the reports section, for example, if they were launched for testing purposes?

A: Yes. On the **Advanced** **Settings** tab, the **Exclude** from reports feature provides this capability.

### Q: If I select multiple scenarios for my campaign, how will the system distribute them among my employees?

A: When multiple scenarios are selected for a campaign, the distribution of emails will be calculated based on the number of users divided by the number of scenarios. For example, if you have 100 users and 4 scenarios, each scenario will be sent to 25 users.

### Q: Why do simulation emails contain the "X-MS-Exchange-Organization-SkipSafeLinksProcessing: true" header?

A: This header prevents Microsoft Defender from analyzing links in phishing simulation emails, ensuring accurate test results and preventing false positives.

### **Q: I launched a campaign with training attached and selected the 'Start Training Immediately' option. Although the user failed the simulation, their status shows as 'In Queue' in the Sending Report on the enrollment report. Why is that?**

**A:** This status occurs because the user clicked the simulation link and was redirected to the training enrollment page but did **not** click the **'START TRAINING'** button to begin the training.

Until the user actively starts the training by clicking this button, their status will remain as **'In Queue'**. Once they start the training, the status will automatically update accordingly.
