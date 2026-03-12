# Source: https://doc.keepnetlabs.com/next-generation-product/platform/quishing-simulator/quishing-campaign-reports.md

# Quishing Campaign Reports

This section describes the basic functionalities of quishing campaign reports, which you can find from the **Quishing Simulator >** [**Campaign Manager** ](https://doc.keepnetlabs.com/next-generation-product/smishing-simulator/smishing-campaign-manager#campaign-instances)menu.

## **View Report Details**

To view the details of a quishing campaign report, navigate to the **Quishing Simulator >** **Campaign** **Manager** menu. Then, select the **Instance** button for the campaign you want to review, and click on **Action** followed by **View Report.**

### **Summary**

The **Summary** provides a brief synopsis of the quishing scenario and options for further action.

<table><thead><tr><th width="150"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Download Report</td><td>A .xlsx format version of the quishing scenario report is available for download by clicking the <strong>Download</strong> <strong>Report</strong> button.</td></tr><tr><td>Resend Campaign</td><td>Resend the quishing scenario to the same target user group with the same settings by clicking the <strong>Resend Campaign</strong> button.</td></tr></tbody></table>

#### Summary Widgets

This section provides the opportunity to display the results of the campaign in a useful pie chart presentation.

<table><thead><tr><th width="150"></th><th width="586.1428571428571"></th></tr></thead><tbody><tr><td>No Response</td><td>The number and percentage of target users who did not take any action in response to the quishing email.</td></tr><tr><td>Opened Email</td><td>The number and percentage of target users who opened the quishing email</td></tr><tr><td>Scanned QR Link</td><td>The number of target users who scanned the QR code in the simulation email.</td></tr><tr><td>Submitted Data</td><td>The number of target users who scanned the QR code and then submitted their credentials on the HTML page.</td></tr></tbody></table>

### Campaign Info

<table><thead><tr><th width="150"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Target Group</td><td>The total number of target groups that are enrolled in the quishing campaign email.</td></tr><tr><td>Target Users</td><td>The total number of users selected to receive the quishing campaign email.</td></tr><tr><td>Languages</td><td>Language used in the quishing scenario.</td></tr><tr><td>Campaign Lifetime</td><td>The date and time the quishing campaign will be terminated. No additional data will be processed in the quishing report after the expired date.</td></tr><tr><td>Duration</td><td>The number of days that the campaign will stay active.</td></tr></tbody></table>

### Email Delivery

<table><thead><tr><th width="135"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Delivery Start - End</td><td>The date and time the campaign was started and was/will be ended to complete sending the email to all selected users.</td></tr><tr><td>Duration</td><td>It shows how long it took to send the campaign email to all selected users.</td></tr><tr><td>Delivery Status</td><td>Out of the total number of chosen users, it displays how many of them successfully received the campaign email and how many did not.<br><br>Please go to <a href="#sending-report">Sending Report</a> menu to see more information.</td></tr></tbody></table>

### Quishing Scenarios

#### Scenario Info

This section displays general information about the content of the quishing scenario. If you selected multiple scenarios, you can switch between them to preview.

<table><thead><tr><th width="150"></th><th width="581.1428571428571"></th></tr></thead><tbody><tr><td>Name</td><td>Name of the quishing scenario.</td></tr><tr><td>Method</td><td><p>Quishing scenarios can be created in one of several forms.</p><p><strong>Data Submit =</strong> Designed to detect target users who scan the QR code and submit data on the landing page.</p><p><strong>Click-Only =</strong> Designed to detect users who scan the QR code and open the link.</p></td></tr><tr><td>Difficulty</td><td>Difficulty level of the quishing scenario (easy, medium, hard)</td></tr><tr><td>Language</td><td>Language used in the quishing scenario.</td></tr></tbody></table>

#### Email that will be sent to users

This section displays details of the sender’s name, the difficulty level, and the quishing scenario type sent to the target users.

You can preview the email template design of the quishing scenario sent to the target users by clicking on the **Preview** button.

#### Landing Page for Users Who Clicked on the QR Code Link

The URL, difficulty level, and scenario type of the landing page content of the quishing scenario sent to the target users are displayed here.

You can preview the landing page design of the quishing scenario sent to the target users by clicking on the **Preview** button.

## Top Menus

### Opened

This section displays the information of the target users who opened the quishing scenario email.

<table><thead><tr><th width="150"></th><th width="584.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Scenario Name</td><td>Name of the quishing scenario that is sent to user</td></tr><tr><td>Last Opened</td><td>Date and time a target user last opened the quishing email</td></tr><tr><td>Times Opened</td><td>Number of times a target user opened the quishing email</td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same quishing email.</p><p>The <strong>Details</strong> option shows the date and time a user opened the quishing email, the user agent, browser information, geolocation, IP information, and other information.</p></td></tr></tbody></table>

### Scanned QR Link

This section provides details of the target users who scanned the QR code and opened the quishing link.

<table><thead><tr><th width="150"></th><th width="583.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Scenario Name</td><td>Name of the quishing scenario that is sent to user</td></tr><tr><td>Last Clicked</td><td>Date and time the user last clicked on the URL in the quishing email</td></tr><tr><td>Times Clicked</td><td>Number of times the user scanned the QR code and opened the quishing link.</td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same quishing email.</p><p>The <strong>Details</strong> option shows the date and time a user opened the quishing email, the user agent, browser information, geolocation, IP information, and other information.</p></td></tr></tbody></table>

### Submitted Data

This section displays details of a target user who submitted data on the landing page of the quishing scenario.

<table><thead><tr><th width="150"></th><th width="585.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Password Complexity</td><td><p>Complexity level of the password submitted on the landing page of the quishing email. (very weak, weak, medium, strong, very strong)</p><p><strong>TIP:</strong> The platform only captures the length and the first character of a password.</p></td></tr><tr><td>Scenario Name</td><td>Name of the quishing scenario that is sent to user</td></tr><tr><td>Last Submission</td><td>Date and time that the user last submitted data on the landing page of the quishing scenario</td></tr><tr><td>Times Submitted</td><td>Number of times that the target user submitted data on the landing page of the quishing scenario</td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same quishing email.</p><p>The <strong>Details</strong> option shows the date and time a user opened the quishing email, the user agent, browser information, geolocation, IP information, and other information.</p></td></tr></tbody></table>

### No Response

This section displays the details of target users who did not take any action in response to the quishing email.

<table><thead><tr><th width="150"></th><th width="585.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Scenario Name</td><td>Name of the quishing scenario that is sent to user</td></tr><tr><td>Email Send Date</td><td>Date and time that the quishing email was sent to the target user</td></tr><tr><td>Action</td><td>The <strong>Resend</strong> button allows you to resend the same quishing email.</td></tr></tbody></table>

### Reporters

This section provides details of target users who reported quishing emails using the phishing reporter add-in.

{% hint style="info" %}
Additional information on the Phishing Reporter is available [here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter).
{% endhint %}

<table><thead><tr><th width="150"></th><th width="584.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Scenario Name</td><td>Name of the quishing scenario that the user reported.</td></tr><tr><td>Last Reported</td><td>Date and time when a user reported the quishing email using the phishing reporter add-in.</td></tr><tr><td>Times Reported</td><td>Number of times that a user reported the quishing email using the phishing reporter add-in.</td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same quishing email.</p><p>The <strong>Details</strong> option shows the date and time a user opened the quishing email, the user agent, browser information, geolocation, IP information, and other information.</p></td></tr></tbody></table>

### Sending Report

This section provides a summary report of the delivery of the quishing email to the target users.

<table><thead><tr><th width="150"></th><th width="584.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Scenario Name</td><td>Name of the quishing scenario that is sent to user</td></tr><tr><td>Last Send Date</td><td><p>Status of the quishing email sent to the target user</p><p><strong>In Queue =</strong> The quishing email is in the queue to be sent.</p><p><strong>Successful =</strong> The quishing email was sent successfully.</p><p><strong>Error =</strong> An error occurred in the delivery of the quishing email.</p><p><strong>Cancelled =</strong> This user was eliminated as a target for this quishing campaign.</p></td></tr><tr><td>Times Reported</td><td>Number of times that a user reported the quishing email using the phishing reporter add-in.</td></tr><tr><td>Action</td><td>The <strong>Resend</strong> button allows you to resend the same quishing email.</td></tr></tbody></table>

## Understanding Bot Activity vs. Human Activity in Reports

In quishing campaign reports, **Human Activity** refers to real actions taken by users, such as opening emails, clicking quishing links, or submitting data. In contrast, **Bot Activity** represents automated interactions triggered by email security systems, spam filters, or sandboxing tools. These bots scan emails and follow links as part of their protective duties—sometimes even before users see the message.

Bot activity may appear in both **Opened** and **Scanned** **QR Link** sections of the report. For example, if a security system opens an email to analyze it, or clicks a link to test the destination, these actions may be captured and flagged as bot interactions.

To ensure accurate reporting, the platform automatically detects and labels such activity based on predefined detection rules. Any record classified as **Bot Activity** will carry a special tag and can be excluded from the view by clicking the **“Hide Bot Activity”** button. Admins can also hover over the info (ⓘ) icon in the **Activity Type** column to see which rule was triggered.

The detection rules are:

* **A1 – Unusual User-Agent Interacted:** Triggered when an atypical or suspicious user-agent (browser identifier) is detected.
* **A2 – Honeypot Link Reused:** The hidden quishing link inside of the email clicked multiple times by the same IP and user-agent within 5 minutes—indicating automation.
* **A3 – Same-Second Activity Spike:** Multiple activities occurred at the exact same time, which is unlikely for human users.
* **A4 – Stop Bot Activity Challenge Failed:**
  * **A4.1** – The quishing phishing link was clicked, but the invisible browser javascript challenge was not passed.
  * **A4.2** – The browser failed to load required scripts that a real user’s browser would normally execute.

If customers see several entries marked as **Bot Activity**, it typically means that their security tools pre-screened the quishing simulation links. To evaluate real user behavior, they should filter the report by **Activity Type** or use the **“Hide Bot Activity”** toggle. For better accuracy in future simulations, they may consider allow listing Keepnet domains to reduce interference from automated systems.

By filtering out bot noise, organizations gain a clearer understanding of **true user actions and risk levels**.

## Video Tutorial

This tutorial describes the basic functionalities of quishing campaign reports.

{% embed url="<https://youtu.be/f-0zggMD_98>" %}
