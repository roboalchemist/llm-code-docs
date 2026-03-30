# Source: https://doc.keepnetlabs.com/next-generation-product/platform/incident-responder/investigations.md

# Investigations

This document displays the functions on **Incident Responder > Investigation**. Users will learn how to handle Investigations and carry out Incident Response processes.

You can find the investigations that have already been initiated on **Incident Responder > Investigation**. The table below provides a detailed explanation of the functions on this page.

<table data-header-hidden><thead><tr><th width="150"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Investigation name</td><td>The name of the initiated Investigation.</td></tr><tr><td>Trigger</td><td>Indicates the initialization status of the Investigation. (E.g., Manual Investigation, Auto Investigation)</td></tr><tr><td>Status</td><td>The status information of the investigation. Filter the investigations based on the status (E.g., Finished, Expired or Running)</td></tr><tr><td>Date Created</td><td>The date when the investigation was started.</td></tr><tr><td>Expiry Date</td><td>The date when the investigation was completed.</td></tr><tr><td>Scan Status</td><td>A summary on how many users the investigation was completed and on how many it was not.</td></tr><tr><td>Progress</td><td>This is the completion status of the investigation as a percentage. When it is completed, it is displayed as <strong>"Completed".</strong></td></tr><tr><td>Action</td><td>Investigation details are available here. The investigation can be stopped with the <strong>“Stop Action ■”</strong> button.</td></tr></tbody></table>

## **How to Start an Investigation?**

### **Auto Investigation**

Click on **Incident Responder > Investigation** menu to access **Auto Investigation** and report details.

If the analysis result of an email in the **Reported Emails** is determined as **Malicious or Phishing**, an automatic investigation is launched to search for the email within all users’ inboxes. The administrator will then decide what to do with the next steps.

{% hint style="info" %}
Auto Investigation starts automatically by default as a result of a malicious email analysis.
{% endhint %}

When an **Auto investigation** or **Manual investigation** is started, platform admins are informed about the details of the process via email.

### Starting a Manual Investigation

Click the **Incident Responder > Investigation** menu to start **Manual Investigation** and access the report details.

With the **Manual** **Investigation** feature, platform administrators can detect suspicious emails within their employees' email boxes using the criteria in the table below. After detecting these suspicious emails, it is possible to delete the relevant emails from the users' email boxes or send a warning message to the users in order to prevent damage.

When the **New** button on the page is clicked to start a new Investigation, the **Start New Manual Investigation** window appears on the screen and you can start **Manual** **Investigation** by filling in the information in the table below.

<table data-header-hidden><thead><tr><th width="150"></th><th width="581.1428571428571"></th></tr></thead><tbody><tr><td>Investigation Name</td><td>The Investigation name is set and only visible to the administrator. If not changed, the name investigation will be the creation date by default</td></tr><tr><td>Target Users</td><td><p>The user(s) you will start the investigation with are determined from this field.<br></p><p>With the <strong>All Users option</strong>, investigation is started for all target users who installed the suspicious email reporter add-in.<br></p><p>With the <strong>User Group option</strong>, investigation is started by selecting specific target user groups.<br></p><p>With <strong>Specific Users</strong>, investigation is started on specific target users</p></td></tr><tr><td>Email Date Range</td><td>It is the date range information that emails will be scanned.</td></tr><tr><td>Select Sources</td><td>You can specify the source(s) for the investigation.</td></tr><tr><td>Duration</td><td>You can determine how long the initiated investigation will be active.</td></tr><tr><td>Action</td><td><p>As a result of the investigation, an action can be defined when the relevant email is detected.<br><br>Warning labels can be sent to emails found with the <strong>Notify user only</strong> option. The message to be sent can be determined from the <strong>"Message"</strong> field.<br><br>Using the <strong>Move to trash</strong> option emails found can be moved to the Trash.<br></p><p>With the <strong>Delete email</strong> option, emails found can be permanently deleted.</p></td></tr></tbody></table>

Please click the **Next** button to set up the filters. First, select either **AND** or **OR** criteria, and then choose the filters. Emails that match the selected filters will be listed in the investigation report.

<table><thead><tr><th width="122"></th><th></th></tr></thead><tbody><tr><td>AND / OR</td><td>Select which option you wish to start the investigation with.</td></tr><tr><td>Filters</td><td><p>Add any of the following conditions:</p><p><strong>Header:</strong></p><ul><li><strong>Subject:</strong> Search based on the email's subject line.</li><li><strong>From:</strong> Search based on the email's sender or "from" address.</li><li><strong>To:</strong> Search based on the email's recipient(s).</li><li><strong>CC:</strong> Search based on email addresses in the CC field.</li><li><strong>BCC:</strong> Search based on email addresses in the BCC field.</li><li><strong>Sender</strong> <strong>Name:</strong> Search based on the name of the sender.</li><li><strong>IP</strong> <strong>Address:</strong> Search based on the sender's IP address.</li></ul><p><strong>Body:</strong></p><ul><li><strong>Keyword:</strong> Search for specific words or phrases in the email body.</li><li><strong>URL:</strong> Search for specific web addresses or URLs in the email body.</li><li><strong>Regex:</strong> Use regular expressions to define complex search patterns in the email body.</li></ul><p><strong>Attachment:</strong></p><ul><li><strong>File</strong> <strong>Name:</strong> Search for emails with specific attachment file names.</li><li><strong>File</strong> <strong>Size:</strong> Search for emails with attachments of a particular size.</li><li><strong>File</strong> <strong>Extension:</strong> Search for emails with attachments of specific file types such as ".pdf, .html, .mp4"</li><li><strong>SHA512:</strong> Search for emails with attachments that have a specific SHA-512 hash value.</li><li><strong>MD5:</strong> Search for emails with attachments that have a specific MD5 hash value.</li></ul></td></tr></tbody></table>

{% hint style="info" %}
To start an Investigation, you need one of the integrations in the [Mail Configuration](https://doc.keepnetlabs.com/next-generation-product/platform/incident-responder/mail-configurations) menu, or you need the [Phishing Reporter Desktop](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter) plugin installed.
{% endhint %}

### **Investigation Detail Page**

We will explain the **Details** function in the **Action** menu on **Incident Responder > Investigation**. By clicking the **Details** button, you can access the details of an Investigation already initiated.

After completing the steps of the Manual Investigation initialization process, you will be directed to the “**Investigation Details**” page. You can view the investigation details from this area. Widgets and mail details are displayed here.

Information summarizing the Investigation process can be viewed from the Widgets section.

The details are outlined in the table below.

<table data-header-hidden><thead><tr><th width="150"></th><th width="583.1428571428571"></th></tr></thead><tbody><tr><td>Investigation Status</td><td>There are 3 different investigation statuses:<br><br><strong>1- Running status:</strong> It means that the Investigation that has been started is continuing.<br><br><strong>2- Finished status:</strong> It means that the investigation is completed for all users within a certain period of time.<br><br><strong>3- Expire status:</strong> It means that the time set for investigation has expired.</td></tr><tr><td>Users (Could not be scanned)</td><td>The number or status of users where Investigation cannot be done for any reason.</td></tr><tr><td>Scanned Users</td><td>The information on how many users the Investigation was launched in total.</td></tr><tr><td>Emails Scanned</td><td>The information on how many emails Investigation was launched and scanned.</td></tr><tr><td>Duplicate</td><td>It allows an easy way to copy and recreate the investigation criteria.</td></tr></tbody></table>

On the left side of the **Investigation Details** page, you can see which folder contained the detected emails that met the search parameters. The table below includes a description of each folder's purpose.

<table data-header-hidden><thead><tr><th width="150"></th><th width="583.1428571428571"></th></tr></thead><tbody><tr><td>Expiry Time</td><td>Indicates in which interval the investigation will run and on what date it will end. The date is specified with the Duration feature where admin can change before starting an investigation.</td></tr><tr><td>Found Users</td><td>The information and progress on which users the investigation was carried out and how many user inboxes were searched can be viewed in detail.</td></tr><tr><td>Folders</td><td>Under the Folders field, there are <strong>Inbox, Junk, Draft, Sent, Deleted Items and Others fields.</strong></td></tr><tr><td>Inbox</td><td>The email that is detected in the users’ inbox after the scan.</td></tr><tr><td>Junk</td><td>The email that is detected in the users’ junk box after the scan.</td></tr><tr><td>Draft</td><td>The email that is detected in the users’ email draft after the scan.</td></tr><tr><td>Sent</td><td>The email that is detected in the users’ sent box after the scan.</td></tr><tr><td>Deleted Items</td><td>The email that is detected in the users’ deleted items after the scan.</td></tr><tr><td>Others</td><td>The email that is detected in the users’ other custom folders after the scan.Veritas Enterprise Vault.</td></tr><tr><td>Stored</td><td>The email that is detected in the Veritas Enterprise Vault after the scan.</td></tr></tbody></table>

The details of the fields in **Found Users** on the left menu of the report page is described in detail in the table below.

<table data-header-hidden><thead><tr><th width="160.4000244140625"></th><th width="584.1428571428571"></th></tr></thead><tbody><tr><td>Owner</td><td>The onwer of the email box the incident is found in.</td></tr><tr><td>From</td><td>The email of the sender of the reported email.</td></tr><tr><td>To</td><td>The email of the reported email reciever.</td></tr><tr><td>Sender Name</td><td>The name of the reciever of the reported email.</td></tr><tr><td>Subject</td><td>The subject information of the reported email.</td></tr><tr><td>Attachment</td><td>Record of if an attachment is included in the reported email.</td></tr><tr><td>Source</td><td>The information on which source (Outlook, O365, Exchange or Google Workspace) the investigation was made.</td></tr><tr><td>Filter</td><td>If one or more of your search criteria has been met.</td></tr><tr><td>Status</td><td>The status of the reported email.</td></tr><tr><td>Trash Can (Actions)</td><td>Delete the reported email from the users inbox.</td></tr><tr><td>Warning Sign (Actions)</td><td>Send user a warning message about the reported email.</td></tr></tbody></table>

### **Start an Investigation through/via a Reported Email**

This section explains how you can easily search for any of the suspicious emails reported to the system in the **Incident Responder** menu.\
\
In the left menu, go to **Incident Responder > Reported Emails**.

After clicking on the three dots (“︙”) under the **Actions**, click on the **Investigate** button and you can start an investigation for the reported emails. The platform automatically extracts the fields from the reported email's analysis results and defines them in the investigation filters, so you don't need to set them manually.

## Video Tutorial

This tutorial explains the functions on **Incident Responder > Investigation**. Users will learn how to handle Investigations and carry out Incident Response processes.

{% embed url="<https://youtu.be/t44xH7KuGdo>" %}

## **FAQ**

### Q: Which operator (AND / OR) logic do the criteria (determined when starting the investigation) work among themselves?

A: The criteria works with either AND/OR logic, both options are supported.

### **Q: Can an Investigation be started on all sources at the same time?**

A: Yes, Investigation can be launched on Outlook, O365, Exchange, Google Workspace and Phishing Reporter Outlook Desktop users at the same time.

### **Q: What happens if the scope of the Investigation is large and is not completed within the specified time frame?**

A: The status of the Investigation will be **Expired**. However if the Investigation is completed within the specified time frame, the status will be **Finished**.

### **Q: What happens to the progress of Investigation if the user that the investigation was made on goes offline while the investigation is being done on the Outlook source?**

A: If the relevant user becomes online again, the investigation continues from where it left off.

### **Q: Can I read emails in the mailbox of a user while I am doing an investigation?**

A: No, you cannot. Platform administrators are only able to see the Subject, To, From, Sender Name and whether the relevant email has an Attachment in the details of their investigations.

### **Q: Can emails that are permanently deleted be restored?**

A: Emails that are permanently deleted can be recovered from the "**Recover Deleted Items**" menu on Outlook within 14 days.

### **Q: How can I view the logs related to this product?**

A: All logs can be accessed in the Audit menu.

### Q: Can Investigation be started for Outlook Desktop users that are 'offline'?

A: No, the investigation cannot be started because the add-in will be closed when Outlook is closed. In order for Investigation to start, the user's Outlook account must be active and the add-in must be running.
