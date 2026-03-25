# Source: https://doc.keepnetlabs.com/next-generation-product/platform/smishing-simulator/smishing-campaign-reports.md

# Smishing Campaign Reports

This section describes the basic functionalities of phishing campaign reports, which you can find from the **Smishing >** [**Campaign Manager** ](https://doc.keepnetlabs.com/next-generation-product/platform/smishing-campaign-manager#campaign-instances)menu.

The components of a campaign reports page are explained below.

<table data-header-hidden><thead><tr><th width="160"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Last Launch</td><td>Date and time the smishing scenario was last sent to a target user group</td><td></td></tr><tr><td>Target Users</td><td>Number of target users to whom the smishing scenario was sent</td><td></td></tr><tr><td>Status</td><td>Current status of the smishing campaign (idle, running, completed, paused, error)</td><td></td></tr><tr><td>Date Created</td><td>Date and time that the smishing scenario was first created</td><td></td></tr><tr><td>Action</td><td>Options available include <strong>View Report</strong>, which provides a summary of a selected smishing scenario, and the <strong>Delete</strong> button, which will delete the report.</td><td></td></tr></tbody></table>

## View Report Details

You can review the details of a smishing campaign report by navigating to **Smishing Simulator** > Campaign Manager, then clicking the **instance** of the smishing campaign, and selecting the **View Report** button under the **Actions** column.

### Summary

The **Summary** provides a brief synopsis of the smishing campaign and options for further action.

<table data-header-hidden><thead><tr><th width="198"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Download Report</td><td>An .xls format version of the smishing campaign report is available for download by clicking the <strong>Download Report</strong> button.</td><td></td></tr><tr><td>Resend Campaign</td><td>Resend the smishing campaign to the same target user group with the same settings by clicking the <strong>Resend Campaign</strong> button.</td><td></td></tr></tbody></table>

#### Summary Widgets

<table data-header-hidden><thead><tr><th width="173"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>No Response</td><td>The number of target users who did not take any action on the smishing text.</td><td></td></tr><tr><td>Clicked Link</td><td>The number of target users who clicked on the phishing link in the smishing text.</td><td></td></tr><tr><td>Submitted Data</td><td>The number of target users who clicked on the phishing link in the smishing text and submitted personal data on the landing page of the phishing link.</td><td></td></tr></tbody></table>

#### Campaign Info

<table data-header-hidden><thead><tr><th width="187"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Target Users</td><td>The number of target users selected in the smishing campaign.</td><td></td></tr><tr><td>Campaign Lifetime</td><td>The total number of days that the campaign will run. After the date ends, the campaign report will no longer accept any new user data to the report.</td><td></td></tr><tr><td>Languages</td><td>The selected language for the smishing campaign.</td><td></td></tr></tbody></table>

#### Message Sending

<table data-header-hidden><thead><tr><th width="190"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Sending Start-End</td><td>The date that the first and last text was sent.</td><td></td></tr><tr><td>Sending Status</td><td>The number of texts sent out of the total of users.</td><td></td></tr><tr><td>Sender Phone Number</td><td>The phone number that is used to call the users in the campaign.</td><td></td></tr></tbody></table>

### Smishing Scenarios

#### Text Message Template that will be sent to users

This section displays details of smishing scenarios used in the smishing campaign such as the SMS message, the difficulty level, and the landing page. You can preview the details of smishing scenarios that are selected for the smishing campaign.

#### Landing Page for users who clicked on the smishing link

The landing page URL, difficulty level, and type of the landing page are displayed here. You can preview the landing page design by clicking on the **Preview** button.

### Clicked

This section provides details of the target users who clicked on the phishing link.

<table data-header-hidden><thead><tr><th width="157.5"></th><th></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Scenario</td><td>Name of the smishing scenario used in the smishing campaign</td></tr><tr><td>Last Clicked</td><td>Date and time the user last clicked on the URL in the smishing text</td></tr><tr><td>Times Clicked</td><td>Number of times the user clicked on the phishing link</td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to send the same smishing text.<br></p><p>The <strong>Details</strong> option shows the date and time a user opened the phishing link, the user agent, browser information, geolocation, IP information, and other information.</p></td></tr></tbody></table>

### Submitted Data

This section displays details of a target user who submitted data on the landing page of the phishing scenario.

<table data-header-hidden><thead><tr><th width="165.5"></th><th></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Password Complexity</td><td>Complexity level of the password submitted on the landing page of the smishing email. (very weak, weak, medium, strong, very strong)</td></tr><tr><td>Last Submission</td><td>Date and time that the user last submitted data on the landing page.</td></tr><tr><td>Times Submitted</td><td>Number of times that the target user submitted data on the landing page.</td></tr><tr><td>Action</td><td><p>The <strong>Resend</strong> button allows you to resend the same phishing email.</p><p>The <strong>Details</strong> option shows the date and time a user submitted credentials on the landing page.</p></td></tr></tbody></table>

### No Response

This section displays the details of target users who did not take any action in response to the smishing text.

<table data-header-hidden><thead><tr><th width="172.5"></th><th></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target users</td></tr><tr><td>Last Name</td><td>Last name of the target users</td></tr><tr><td>Email Address</td><td>Email address of the target users</td></tr><tr><td>Department</td><td>Department of the target users</td></tr><tr><td>Snenario Name</td><td>The name of the selected scenario</td></tr><tr><td>Email Send Date</td><td>Date and time that the smishing text was sent to the target user</td></tr><tr><td>Action</td><td>The <strong>Resend</strong> button allows you to resend the same sms message.</td></tr></tbody></table>

### Sending Report

This section provides a summary report of the delivery of the sms message to the target users.

<table data-header-hidden><thead><tr><th width="161.5"></th><th></th></tr></thead><tbody><tr><td>First Name</td><td>First name of the target user</td></tr><tr><td>Last Name</td><td>Last name of the target user</td></tr><tr><td>Email Address</td><td>Email address of the target user</td></tr><tr><td>Department</td><td>Department of the target user</td></tr><tr><td>Last Sent Date</td><td>Date and time that the smishing text was last sent to the target user</td></tr><tr><td>Send Status</td><td><p>Status of the smishing text sent to the target user</p><ul><li><strong>In Queue:</strong> The sms message is in the queue to be sent.</li><li><strong>Successful:</strong> The sms message was sent successfully.</li><li><strong>Not Delivered:</strong> The sms message wasn't delivered. Hover your mouse on the status to see the details of why it's not delivered.</li><li><strong>Error:</strong> An error occurred in the delivery of the sms message.</li><li><strong>Canceled:</strong> This user was eliminated as a target for this smishing campaign.</li></ul></td></tr><tr><td>Action</td><td>The <strong>Resend</strong> button allows you to resend the same sms message to the selected user(s)</td></tr></tbody></table>

## Tutorial Video

This tutorial describes the basic functionalities of smishing campaign reports which you can find in the [campaign manager](https://doc.keepnetlabs.com/next-generation-product/platform/smishing-campaign-manager#campaign-instances) menu.

{% embed url="<https://www.youtube.com/watch?index=5&list=PLTfpxvprC-_xwsgbaZw2ilbIeRUZtFnFn&v=262xOxfGtA4>" %}

## FAQ

### Q: Can I download a smishing scenario report?

A: Yes. You can download a report that provides details of the smishing campaign by clicking on the **Download** **Report** button.

### Q: Can I change the content of the report of the smishing scenario?

A: No. The information in the report cannot be changed.

### Q: Can I resend the smishing campaign to users who did not response to SMS message?

A: Yes. The resend function allows you to send the smishing campaign to the users.

### Q: Can I check if SMS messages are delivered successfully to the employees?

A: Yes. The **Sending** **Report** menu provides you with a view of SMS message delivery to the employee's phone number.

### **Q: Why SMS Messages Are Not Delivered to Some Users?**

**A:** If you hover over the **Not Delivered** status and see one of the following messages:

* `SMS sending failed. StatusCode: 251, Description: Message successfully sent out for delivery, however final confirmation of delivery to handset was not received.`
* `SMS sending failed. StatusCode: 207, Description: Error delivering message to handset (reason unknown).`

It indicates that the SMS message was either **blocked by the mobile carrier due to spam-related content** or the **landing page domain used in your scenario was flagged as spam**.

To resolve this issue:

1. Edit your **SMS Template**, then click the **ENHANCE** button to regenerate and optimize the message.
2. Edit your **Landing Page**, and **update the domain** with another available one from your domain list.

After making these changes, try sending the campaign again.
