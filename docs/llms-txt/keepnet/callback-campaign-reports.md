# Source: https://doc.keepnetlabs.com/next-generation-product/platform/callback-simulator/callback-campaign-reports.md

# Callback Campaign Reports

This section describes the basic functionalities of callback campaign reports, which you can find from the **Callback Simulator >** [**Campaign Manager**](https://doc.keepnetlabs.com/next-generation-product/platform/callback-campaign-manager#campaign-instances) menu.

## **View Report Details**

To view the details of a callback campaign report, navigate to the **Callback Simulator > Campaign Manager** menu. Then, select the **Instance** button for the campaign you want to review, and click on **Action** followed by **View Report.**

### **Summary**

The **Summary** provides a brief synopsis of the callback scenario and options for further action.

<table><thead><tr><th width="150"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Download Report</td><td>A .xlsx format version of the callback campaign report is available for download by clicking the <strong>Download</strong> <strong>Report</strong> button.</td></tr><tr><td>Resend Campaign</td><td>Resend the callback scenario to the same target user group with the same settings by clicking the <strong>Resend Campaign</strong> button.</td></tr></tbody></table>

#### Summary Widgets

This section provides the opportunity to display the results of the campaign in a useful pie chart presentation.

<table><thead><tr><th width="150"></th><th width="586.1428571428571"></th></tr></thead><tbody><tr><td>No Response</td><td>The number and percentage of target users who did not take any action in response to the callback email.</td></tr><tr><td>Opened Email</td><td>The number and percentage of target users who opened the callback email</td></tr><tr><td>Called Back</td><td>The number of target users who called the simulation phone number listed on the simulation email.</td></tr><tr><td>Entered Digits</td><td>The number of target users who submitted their credentials on the call.</td></tr></tbody></table>

### Campaign Info

<table><thead><tr><th width="150"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Target Users</td><td>The total number of users selected to receive the callback campaign email.</td></tr><tr><td>Campaign Lifetime</td><td>The date and time the callback campaign will be terminated. No additional data will be processed in the callback report after the expired date.</td></tr><tr><td>Languages</td><td>Language used in the callback scenario.</td></tr></tbody></table>

### Email Delivery

<table><thead><tr><th width="135"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Delivery Start - End</td><td>The date and time the campaign was started and was/will be ended to complete sending the email to all selected users.</td></tr><tr><td>Duration</td><td>It shows how long it took to send the campaign email to all selected users.</td></tr><tr><td>Delivery Status</td><td>Out of the total number of chosen users, it displays how many of them successfully received the campaign email and how many did not.<br><br>Please go to <a href="#sending-report">Sending Report </a>menu to see more information.</td></tr></tbody></table>

### Callback Scenarios

#### Scenario Info

This section displays general information about the content of the callback scenario. If you selected multiple scenarios, you can switch between them to preview.

<table><thead><tr><th width="150"></th><th width="581.1428571428571"></th></tr></thead><tbody><tr><td>Name</td><td>Name of the callback scenario.</td></tr><tr><td>Difficulty</td><td>Difficulty level of the callback scenario (easy, medium, hard)</td></tr><tr><td>Language</td><td>Language used in the callback scenario.</td></tr></tbody></table>

#### Email Template

This section displays details of the sender’s name, the difficulty level, and the callback scenario type sent to the target users.

You can preview the email template design of the callback scenario sent to the target users by clicking on the **Preview** button.

#### Callback Template

The difficulty, AI language or callback voice steps of the callback scenario sent to the target users are displayed here.

You can preview the callback template design of the callback scenario sent to the target users by clicking on the **Preview** button.

## Top Menus

### Opened

This section displays the information of the target users who opened the callback campaign email.

<table><thead><tr><th width="150"></th><th width="584.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Last Opened</td><td>Date and time a target user last opened the callback email</td></tr><tr><td>Times Opened</td><td>Number of times a target user opened the callback email</td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same callback email.</p><p>The <strong>Details</strong> option shows the date and time a user opened the callback email, the user agent, browser information, geolocation, IP information, and other information.</p></td></tr></tbody></table>

### Called Back

This section provides details of the target users who called the phone number back listed on the callback simulation email.

<table><thead><tr><th width="150"></th><th width="583.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Scenario Name</td><td>Name of the callback scenario that is sent to user</td></tr><tr><td>Last Caller ID</td><td>The simulation phone number that is selected for the callback campaign.</td></tr><tr><td>Last Called Back</td><td>Last date and time that the user called back the phone number listed on the callback simulation email.</td></tr><tr><td>Times Called Back</td><td>Number of times the user called back the phone number listed on the callback simulation email.</td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same callback email.</p><p>The <strong>Details</strong> option shows the date and time a user opened the callback email, the user agent, browser information, geolocation, IP information, and other information.</p></td></tr></tbody></table>

### Entered Digits

This section displays details of a target user who submitted data on the phone call.

<table><thead><tr><th width="150"></th><th width="585.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Last Caller ID</td><td>The simulation phone number that is selected for the callback campaign.</td></tr><tr><td>Last Entered Digits</td><td>Last date and time that the user submitted credentials on the phone call.</td></tr><tr><td>Times Entered Digits</td><td>Number of times that the target user submitted data on the phone call.</td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same callback email.</p><p>The <strong>Details</strong> option shows the date and time a user opened the callback email, the user agent, browser information, geolocation, IP information, and other information.</p></td></tr></tbody></table>

### No Response

This section displays the details of target users who did not take any action in response to the callback email.

<table><thead><tr><th width="150"></th><th width="585.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Scenario Name</td><td>Name of the callback scenario that is sent to user</td></tr><tr><td>Email Send Date</td><td>Date and time that the callback email was sent to the target user</td></tr><tr><td>Action</td><td>The <strong>Resend</strong> button allows you to resend the same callback email.</td></tr></tbody></table>

### Reporters

This section provides details of target users who reported callback emails using the phishing reporter add-in.

{% hint style="info" %}
Additional information on the Phishing Reporter is available [here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter).
{% endhint %}

<table><thead><tr><th width="150"></th><th width="584.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Scenario Name</td><td>Name of the callback scenario that is sent to user</td></tr><tr><td>Last Reported</td><td>Date and time when a user reported the callback email using the phishing reporter add-in.</td></tr><tr><td>Times Reported</td><td>Number of times that a user reported the callback email using the phishing reporter add-in.</td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same callback email.</p><p>The <strong>Details</strong> option shows the date and time a user opened the callback email, the user agent, browser information, geolocation, IP information, and other information.</p></td></tr></tbody></table>

### Sending Report

This section provides a summary report of the delivery of the callback email to the target users.

<table><thead><tr><th width="150"></th><th width="584.1428571428571"></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Date Last Send</td><td>Last date and time that the callback email sent to user.</td></tr><tr><td>Delivery Status</td><td><p>Status of the callback email sent to the target user</p><ul><li><strong>In Queue =</strong> The callback email is in the queue to be sent.</li><li><strong>Successful =</strong> The callback email was sent successfully.</li><li><strong>Error =</strong> An error occurred in the delivery of the callback email.</li><li><strong>Cancelled =</strong> This user was eliminated as a target for this callback campaign.</li></ul></td></tr><tr><td>Action</td><td><p>The action buttons:</p><ul><li>The <strong>Resend</strong> button allows you to resend the same callback email.</li><li>The <strong>Details</strong> button to see the detailed email delivery status.</li></ul></td></tr></tbody></table>

## Understanding Bot Activity vs. Human Activity in Reports

In callback campaign reports, **Human Activity** refers to real actions taken by users, such as **opening** **emails**. In contrast, **Bot Activity** represents automated interactions triggered by email security systems, spam filters, or sandboxing tools. These bots scan emails and follow links as part of their protective duties—sometimes even before users see the message.

Bot activity may appear in the **Opened** section of the report. For example, if a security system opens an email to analyze it, or clicks a link inside of the email to test the destination, these actions may be captured and flagged as bot interactions.

To ensure accurate reporting, the platform automatically detects and labels such activity based on predefined detection rules. Any record classified as **Bot Activity** will carry a special tag and can be excluded from the view by clicking the **“Hide Bot Activity”** button. Admins can also hover over the info (ⓘ) icon in the **Activity Type** column to see which rule was triggered.

The detection rules are:

* **A1 – Unusual User-Agent Interacted:** Triggered when an atypical or suspicious user-agent (browser identifier) is detected.
* **A2 – Honeypot Link Reused:** The hidden callback phishing simulation link inside of the email clicked multiple times by the same IP and user-agent within 5 minutes—indicating automation.
* **A3 – Same-Second Activity Spike:** Multiple activities occurred at the exact same time, which is unlikely for human users.
* **A4 – Stop Bot Activity Challenge Failed:**
  * **A4.1** – The callback phishing simulation link was clicked, but the invisible browser javascript challenge was not passed.
  * **A4.2** – The browser failed to load required scripts that a real user’s browser would normally execute.

If customers see several entries marked as **Bot Activity**, it typically means that their security tools pre-screened the callback simulation links inside of the callback email. To evaluate real user behavior, they should filter the report by **Activity Type** or use the **“Hide Bot Activity”** toggle. For better accuracy in future callback simulations, they may consider allow listing Keepnet domains to reduce interference from automated systems.

By filtering out bot noise, organizations gain a clearer understanding of **true user actions and risk levels**.

## Video Tutorial

This tutorial describes the basic functionalities of callback campaign reports.

{% embed url="<https://youtu.be/nHOEMGiW-7U?si=XLPJsRkmBbJ0LSkf>" %}
