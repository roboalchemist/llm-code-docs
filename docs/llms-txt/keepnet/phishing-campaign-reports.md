# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/phishing-campaign-reports.md

# Phishing Campaign Reports

This section describes the basic functionalities of phishing campaign reports, which you can find from the **Phishing Simulator > Campaign Manager** and click the **Instances** button to access the reports of the phishing campaign.

Once you go inside the **Instances** of a campaign, you will see reports for that campaign; click on the **View** **Report** button under the **Actions** column to access the phishing campaign report.

## **View Report Details**

In a campaign report, there are many sub-menus that provide valuable statistics about your phishing campaign. Here are the following menus on a campaign report:

### **Summary**

The **Summary** provides a brief synopsis of the phishing scenario and options for further action.

<table><thead><tr><th width="150"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Download Report</td><td>An .xls format version of the phishing scenario report is available for download by clicking the Download Report button.</td></tr><tr><td>Resend Campaign</td><td>Resend the phishing scenario to the same target user group with the same settings by clicking the <strong>Resend Campaign</strong> button.</td></tr></tbody></table>

#### Summary Widgets

This section provides the opportunity to display the results of the campaign in a useful pie chart presentation.

<table><thead><tr><th width="150"></th><th width="586.1428571428571"></th></tr></thead><tbody><tr><td>Opened Email</td><td>The number and percentage of target users who opened the phishing email</td></tr><tr><td>Clicked Email</td><td>The number and percentage of target users who clicked on the URL in the phishing email.</td></tr><tr><td>Submitted Data</td><td>The number and percentage of target users who submitted data on the landing page of the phishing scenario.</td></tr><tr><td>Opened Attachment</td><td>The number and percentage of target users who opened the attachment file.</td></tr><tr><td>Phishing Reporters</td><td>The number and percentage of target users who reported the simulated phishing email by using the platform's suspicious email reporter add-in.</td></tr><tr><td>No Response</td><td>The number and percentage of target users who did not take any action in response to the phishing e-mail.</td></tr></tbody></table>

### Campaign Info

<table><thead><tr><th width="150"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Target Groups</td><td>The total number of target groups selected for the phishing campaign.</td></tr><tr><td>Hyper-Personalization</td><td>With the 'Preferred Language' option, users will receive scenarios in their preferred language. Those without a preferred language will receive scenarios in the company's default language.</td></tr><tr><td>Smart Grouping</td><td>If enabled, users who fail at the phishing campaign are automatically added to the selected target group.</td></tr><tr><td>Target Users</td><td>The total number of users selected to receive the phishing campaign email.</td></tr><tr><td>Campaign Lifetime</td><td>The date and time the phishing campaign will be terminated. No additional data will be processed in the phishing report after the expired date.</td></tr><tr><td>Languages</td><td>Language used in the phishing scenario.</td></tr><tr><td>Scenario Distribution</td><td>Shows which scenario distribution setting is used for the campaign. See more info about the scenario distribution feature <a href="../phishing-campaign-manager#phishing-scenarios">here</a>.</td></tr><tr><td>Reply Tracking</td><td>Shows if the reply tracking feature is enabled or not for the phishing campaign.</td></tr></tbody></table>

### Scenario Info

<table><thead><tr><th width="150"></th><th></th></tr></thead><tbody><tr><td>Number of Categories</td><td>The number of categories of selected scenarios.</td></tr><tr><td>Languages</td><td>The number of languages of selected scenarios.</td></tr><tr><td>Method</td><td>The list of methods of selected scenarios.</td></tr><tr><td>Difficulty</td><td>The difficulty levels of selected scenarios.</td></tr></tbody></table>

### Email Delivery

<table><thead><tr><th width="174.29296875"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Delivery Start - End</td><td>The date and time the campaign was started and was/will be ended to complete sending the email to all selected users.</td></tr><tr><td>Duration</td><td>It shows how long it took to send the campaign email to all selected users.</td></tr><tr><td>Delivery Status</td><td>Out of the total number of chosen users, it displays how many of them successfully received the campaign email and how many did not.<br><br>Please go to <a href="#sending-report">Sending Report</a> menu to see more information.</td></tr></tbody></table>

### Phishing Scenarios

This section displays general information about the content of the phishing scenario. If you selected multiple scenarios, you can switch between them to preview.

<table><thead><tr><th width="150"></th><th width="581.1428571428571"></th></tr></thead><tbody><tr><td>Name</td><td>Name of the phishing scenario.</td></tr><tr><td>Method</td><td><p>Phishing scenarios can be created in one of several forms.</p><ul><li><strong>Data Submit =</strong> Designed to detect target users who submit data on the landing page.</li><li><strong>Attachment =</strong> Designed to detect users who open the attached file by opening the file attachment in the e-mail.</li><li><strong>Click-Only =</strong> Designed to detect users who click on the phishing link in the email.</li></ul></td></tr><tr><td>Difficulty</td><td>Difficulty level of the phishing scenario (easy, medium, hard)</td></tr><tr><td>Language</td><td>Language used in the phishing scenario.</td></tr></tbody></table>

#### Email that will be sent to users

This section displays details of the sender’s name, the difficulty level, and the phishing scenario type sent to the target users.

You can preview the email template design of the phishing scenario sent to the target users by clicking on the **Preview** button.

#### Landing Page for Users Who Clicked on the Phishing Link

The URL, difficulty level, and scenario type of the landing page content of the phishing scenario sent to the target users are displayed here.

You can preview the landing page design of the phishing scenario sent to the target users by clicking on the **Preview** button.

### Opened

This section displays the information of the target users who opened the phishing scenario email.

<table><thead><tr><th width="150"></th><th width="584.1428571428571"></th><th></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td><td></td></tr><tr><td>Last Name</td><td>Last name of the target user</td><td></td></tr><tr><td>Email Address</td><td>Email address of the target user</td><td></td></tr><tr><td>Department</td><td>Department of the target user</td><td></td></tr><tr><td>Preferred Language</td><td>User's preferred language that is set from the Target Users menu.</td><td></td></tr><tr><td>Scenario Name</td><td>Name of the phishing scenario that is sent to user</td><td></td></tr><tr><td>Scenario Language</td><td>Language of the related scenario that was sent to user.</td><td></td></tr><tr><td>Last Opened</td><td>Date and time a target user last opened the phishing email</td><td></td></tr><tr><td>Times Opened</td><td>Number of times a target user opened the phishing email</td><td></td></tr><tr><td>Hide Sandbox Activity</td><td>If a sandbox solution has analyzed the simulated phishing email that is generated for the target user, you can choose to show or hide this false positive information in the menu.</td><td></td></tr><tr><td>Activity Type</td><td><p>List the human or sandbox activities by using one of the following options.</p><ul><li><strong>Human Activity:</strong> The human has opened the simulated phishing email.</li><li><strong>Sandbox Activity:</strong> The sandbox solutions have opened the simulated phishing email.</li></ul></td><td></td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same phishing email.</p><p>The <strong>Details</strong> option shows the date and time a user opened the phishing email, the user agent, browser information, geolocation, IP information, and other information.</p></td><td></td></tr></tbody></table>

### Clicked

This section provides details of the target users who clicked on the phishing link.

<table><thead><tr><th width="150"></th><th width="583.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Preferred Language</td><td>User's preferred language that is set from the Target Users menu.</td></tr><tr><td>Scenario Name</td><td>Name of the phishing scenario that is sent to user</td></tr><tr><td>Scenario Language</td><td>Language of the related scenario that was sent to user.</td></tr><tr><td>Last Clicked</td><td>Date and time the user last clicked on the URL in the phishing email</td></tr><tr><td>Times Clicked</td><td>Number of times the user clicked on the phishing link</td></tr><tr><td>Hide Sandbox Activity</td><td>If a sandbox solution has analyzed the simulated phishing email that is generated for the target user, you can choose to show or hide this false positive information in the menu.</td></tr><tr><td>Activity Type</td><td><p>List the human or sandbox activities by using one of the following options.</p><ul><li><strong>Human Activity:</strong> The human has clicked the simulated phishing link.</li><li><strong>Sandbox Activity:</strong> The sandbox solutions have clicked the simulated phishing link.</li></ul></td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same phishing email.</p><p>The <strong>Details</strong> option shows the date and time a user opened the phishing email, the user agent, browser information, geolocation, IP information, and other information.</p></td></tr></tbody></table>

### Submitted Data

This section displays details of a target user who submitted data on the landing page of the phishing scenario.

<table><thead><tr><th width="150"></th><th width="585.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Preferred Language</td><td>User's preferred language that is set from the Target Users menu.</td></tr><tr><td>Password Complexity</td><td><p>Complexity level of the password submitted on the landing page of the phishing email. (very weak, weak, medium, strong, very strong)</p><p><strong>TIP:</strong> The platform only captures the length and the first character of a password. Click <a href="#how-password-complexity-is-calculated">here</a> for more information.</p></td></tr><tr><td>Scenario Name</td><td>Name of the phishing scenario that is sent to user</td></tr><tr><td>Scenario Language</td><td>Language of the related scenario that was sent to user.</td></tr><tr><td>Last Submission</td><td>Date and time that the user last submitted data on the landing page of the phishing scenario</td></tr><tr><td>Times Submitted</td><td>Number of times that the target user submitted data on the landing page of the phishing scenario</td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same phishing email.</p><p>The <strong>Details</strong> option shows the date and time a user opened the phishing email, the user agent, browser information, geolocation, IP information, and other information.</p></td></tr></tbody></table>

### Opened Attachment

This section displays the details of a target user who opened the attachment file.

<table><thead><tr><th width="150"></th><th width="585.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Preferred Language</td><td>User's preferred language that is set from the Target Users menu.</td></tr><tr><td>Scenario Name</td><td>Name of the phishing scenario that is sent to user</td></tr><tr><td>Scenario Language</td><td>Language of the related scenario that was sent to user.</td></tr><tr><td>Last Opened</td><td>Date and time that the user last opened the attachment file</td></tr><tr><td>Times Opened</td><td>Number of times that the target user opened the attached file</td></tr><tr><td>Activity Type</td><td>It shows if the user has <a href="#understanding-bot-activity-vs.-human-activity-in-reports">Bot Acvitiy or Human Activity</a> data for the campaign.</td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same phishing email.</p><p>The <strong>Details</strong> option shows the date and time a user opened the phishing email, the user agent, browser information, geolocation, IP information, and other information.</p></td></tr></tbody></table>

### No Response

This section displays the details of target users who did not take any action in response to the phishing email.

<table><thead><tr><th width="150"></th><th width="585.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Preferred Language</td><td>User's preferred language that is set from the Target Users menu.</td></tr><tr><td>Scenario Name</td><td>Name of the phishing scenario that is sent to user</td></tr><tr><td>Scenario Language</td><td>Language of the related scenario that was sent to user.</td></tr><tr><td>Last Send Date</td><td>Date and time that the phishing email was sent to the target user</td></tr><tr><td>Action</td><td>The <strong>Resend</strong> button allows you to resend the same phishing email.</td></tr></tbody></table>

### Phishing Reporter

This section provides details of target users who reported phishing emails using the phishing reporter add-in.

{% hint style="info" %}
Additional information on the Phishing Reporter is available [here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter).
{% endhint %}

<table><thead><tr><th width="150"></th><th width="584.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Preferred Language</td><td>User's preferred language that is set from the Target Users menu.</td></tr><tr><td>Scenario Name</td><td>Name of the phishing scenario that the user reported.</td></tr><tr><td>Scenario Language</td><td>Language of the related scenario that was sent to user.</td></tr><tr><td>Last Reported</td><td>Date and time when a user reported the phishing email using the phishing reporter add-in.</td></tr><tr><td>Times Reported</td><td>Number of times that a user reported the phishing email using the phishing reporter add-in.</td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same phishing email.</p><p>The <strong>Details</strong> option shows the date and time a user opened the phishing email, the user agent, browser information, geolocation, IP information, and other information.</p></td></tr></tbody></table>

### Sending Report

This section provides a summary report of the delivery of the phishing email to the target users.

<table><thead><tr><th width="150"></th><th width="584.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Preferred Language</td><td>User's preferred language that is set from the Target Users menu.</td></tr><tr><td>Scenario Name</td><td>Name of the phishing scenario that is sent to user</td></tr><tr><td>Scenario Language</td><td>Language of the related scenario that was sent to user.</td></tr><tr><td>Email Delivery</td><td>Which SMTP is used to deliver the simulation emails to the users.</td></tr><tr><td>Date Sent</td><td>The last date and time that the email has been sent to target user.</td></tr><tr><td>Delivery Status</td><td><p>Status of the phishing email sent to the target user</p><ul><li><strong>In Queue =</strong> The phishing email is in the queue to be sent.</li><li><strong>Successful =</strong> The phishing email was sent successfully.</li><li><strong>Error =</strong> An error occurred in the delivery of the phishing email.</li><li><strong>Cancelled =</strong> This user was eliminated as a target for this phishing campaign.</li></ul></td></tr><tr><td>Action</td><td>The <strong>Resend</strong> button allows you to resend the same phishing email.<br><br>The <strong>Details</strong> button allows you to see the email delivery details.</td></tr></tbody></table>

## How Password Complexity is Calculated

When a user submits a form containing a password field, we evaluate the password using a scoring system that determines how strong or weak it is. This score is based on the structure and patterns used in the password.

{% hint style="warning" %}
We do not store or receive full user passwords. Before the form is submitted:

* Only the first character of the password is kept.
* All remaining characters are replaced with asterisks (\*), e.g. P\*\*\*\*\*\*\*\*.

This ensures that no actual password is transmitted or stored, supporting both user privacy and compliance with security best practices.
{% endhint %}

**Positive Scoring Factors**

| Feature                | Scoring Logic                  | Description                                      |
| ---------------------- | ------------------------------ | ------------------------------------------------ |
| Length                 | length \* 4                    | Longer passwords score higher                    |
| Uppercase letters      | (length - uppercaseCount) \* 2 | More uppercase letters (A–Z) = more points       |
| Lowercase letters      | (length - lowercaseCount) \* 2 | More lowercase letters (a–z) = more points       |
| Numbers                | count \* 4                     | Numbers increase the score                       |
| Symbols                | count \* 6                     | Symbols (!@# etc.) give a strong boost           |
| Middle numbers/symbols | count \* 2                     | Placing numbers/symbols in the middle adds bonus |
| Meets requirements     | # of types used \* 2           | Bonuses for using at least 3–4 character types   |

**Negative Scoring Factors**

| Weak Pattern             | Penalty Logic     | Description                                    |
| ------------------------ | ----------------- | ---------------------------------------------- |
| Only letters             | -length           | No digits or symbols = deduction               |
| Only numbers             | -length           | No letters or symbols = deduction              |
| Repeated characters      | -variable penalty | Penalized based on how often characters repeat |
| Consecutive uppercase    | -count \* 2       | Sequences like "AAA" are discouraged           |
| Consecutive lowercase    | -count \* 2       | Same logic as above with lowercase             |
| Consecutive numbers      | -count \* 2       | Same logic with digits                         |
| Sequential letters (abc) | -count \* 3       | Penalizes predictable patterns                 |
| Sequential numbers (123) | -count \* 3       | <p><br></p>                                    |
| Sequential symbols (!@#) | -count \* 3       | <p><br></p>                                    |

**Complexity Rating (Based on Score)**

<table><thead><tr><th width="187.8359375">Score Range</th><th>Complexity Rating</th><th>Description</th></tr></thead><tbody><tr><td>0–19</td><td>5 (Very Weak)</td><td>Needs major improvement</td></tr><tr><td>20–39</td><td>4 (Weak)</td><td>Below average</td></tr><tr><td>40–59</td><td>3 (Moderate)</td><td>Meets some standards</td></tr><tr><td>60–79</td><td>2 (Strong)</td><td>Good overall security</td></tr><tr><td>80–100</td><td>1 (Very Strong)</td><td>Excellent password</td></tr></tbody></table>

Thank you — here is the final version incorporating that **bot activity may apply to both "Opened Email" and "Clicked Link" events**, and still maintaining the correct documentation format with only one Heading 2 and one Subheading 3:

## Understanding Bot Activity vs. Human Activity in Reports

In phishing campaign reports, **Human Activity** refers to real actions taken by users, such as opening emails, clicking links, or submitting data. In contrast, **Bot Activity** represents automated interactions triggered by email security systems, spam filters, or sandboxing tools. These bots scan emails and follow links as part of their protective duties—sometimes even before users see the message.

Bot activity may appear in both **Opened Email** and **Clicked Link** sections of the report. For example, if a security system opens an email to analyze it, or clicks a link to test the destination, these actions may be captured and flagged as bot interactions.

To ensure accurate reporting, the platform automatically detects and labels such activity based on predefined detection rules. Any record classified as **Bot Activity** will carry a special tag and can be excluded from the view by clicking the **“Hide Bot Activity”** button. Admins can also hover over the info (ⓘ) icon in the **Activity Type** column to see which rule was triggered.

The detection rules are:

* **A1 – Unusual User-Agent Interacted:** Triggered when an atypical or suspicious user-agent (browser identifier) is detected.
* **A2 – Honeypot Link Reused:** The hidden phishing link inside of the email clicked multiple times by the same IP and user-agent within 5 minutes—indicating automation.
* **A3 – Same-Second Activity Spike:** Multiple activities occurred at the exact same time, which is unlikely for human users.
* **A4 – Stop Bot Activity Challenge Failed:**
  * **A4.1** – The phishing link was clicked, but the invisible browser javascript challenge was not passed.
  * **A4.2** – The browser failed to load required scripts that a real user’s browser would normally execute.

If customers see several entries marked as **Bot Activity**, it typically means that their security tools pre-screened the phishing simulation links. To evaluate real user behavior, they should filter the report by **Activity Type** or use the **“Hide Bot Activity”** toggle. For better accuracy in future simulations, they may consider allow listing Keepnet domains to reduce interference from automated systems.

By filtering out bot noise, organizations gain a clearer understanding of **true user actions and risk levels**.

## Tutorial Video

This tutorial describes the basic functionalities of phishing campaign reports which you can find in the Campaign Reports menu.

{% embed url="<https://www.youtube.com/watch?v=tmcLSeQHROw>" %}

## FAQ

### Q: Can I download a phishing scenario report?

A: Yes. You can download a report that provides details of the campaign by clicking on the **Download Report** button.

### Q: Can I change the content of the report of the phishing scenario?

A: No. The information in the report cannot be changed.

### Q: Can I resend the scenario to users who did not open the email?

A: Yes. The resend function allows you to send the phishing scenario to any user you select.

### Q: Can I check on the status of the campaign?

A: Yes. The Sending Report option provides you with a view of the current activity of the phishing scenario.

### Q: **Can I import reports into my own reporting tool (e.g., Qlik Sense, Tableau, PowerBI)?**

A: Yes. You can transfer all of our reports through an API, enabling you to use the information as needed to suit your business. Additional information on APIs is available [here.](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/rest-api)

### Q: What are the differences between the Only Opened Emails, Only Clicked Links vs Opened Emails and Clicked Links tabs in the downloaded excel report?

A: The differences are explained below.

* "Only Opened Emails" will show the users who only opened the email and didn't go further, such as clicking the link.
* "Only Clicked Links" will show the users who opened the email and then clicked the link and didn't go further, such as data submission.
* "Opened Emails" will show the users who opened emails. It doesn't matter if user clicked the link or submitted any data.
* "Clicked Links" will show the users who opened and then clicked the link. It doesn't matter if the user submitted any data.

### **Q:** How do you determine if a "user agent" belongs to a sandbox or a real email user?

**A:** Please see below how the **Sandbox** **Activity** **Detection** feature works to identify false positive clicks.

1. **Rule 1: User Agent Signatures:** We have a list of 10+ sandbox user agent patterns. If a user action matches these, it's flagged as sandbox activity.
2. **Rule 2: Honeypot Link:** We embed invisible "Honeypot" links in our emails. While humans can't see or click them, sandboxes often access them, revealing their presence.
3. **Rule 3: Request Header Analysis:** By examining request headers, we can identify unique characteristics that differentiate sandbox activities from real user actions.

### Q: Some users failed to receive the simulation via DEC and show the error 'The process failed to get the correct properties.'

A: If users did not receive the simulation email via DEC and show the error 'The process failed to get the correct properties' in the Sending Report section of the campaign report, it may indicate that these users have been deleted, do not have an email license, have no inbox, or have been deactivated. Please check the users in your Microsoft 365 admin panel to ensure they are all active and have a valid mailbox license.
