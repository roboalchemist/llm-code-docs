# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/manage-phishing-scenarios/email-templates.md

# Email Templates

The [**Phishing Simulator**](https://keepnetlabs.com/products/phishing-simulator) **> Phishing Scenarios > Email Templates** page provides you with system default phishing email templates. You can use them as they are or customize them as needed for your phishing campaign.

The components of the **Email Templates** page are explained below.

<table><thead><tr><th width="150"></th><th width="590.1428571428571"></th></tr></thead><tbody><tr><td>Template name</td><td>Name of the email template</td></tr><tr><td>Method</td><td><p>The phishing technique employed.</p><ul><li><strong>Data Submit =</strong> Used to detect target users who submit data on the landing page</li><li><strong>Attachment =</strong> Used to detect target users who download the attachment in the phishing simulation email</li><li><strong>Click-Only =</strong> Used to detect target users who click unknown links in the phishing email</li></ul></td></tr><tr><td>Languages</td><td>Filter email templates based on your preferred languages.</td></tr><tr><td>Tags</td><td>Tags can be added to the email template to enable viewing using related tag lists.</td></tr><tr><td>Difficulty</td><td>The level of difficulty to recognize a phishing attempt <strong>(Easy, Medium, Hard).</strong> Please <a href="../..#q-how-is-the-difficulty-level-determined">click here</a> to see how the difficulty level is determined.</td></tr><tr><td>Creation Type</td><td>Filter email templates based on their creation type (e.g., Manual or AI Ally).</td></tr><tr><td>Created By</td><td><p><strong>System:</strong> Standard phishing email templates are provided with the product.</p><p><strong>Custom:</strong> Phishing email created or customized by users</p></td></tr><tr><td>Date Created</td><td>The date and time the email template was created</td></tr></tbody></table>

## Email Template Actions

This section explains how to edit, preview, clone, or delete an e-mail template.

### How to Edit an Email Template

Click on the three dots '⋮' button in the **Actions** option on the far right of the relevant page, and then click the **Edit** button.

### How to Preview an Email Template

Click on the three dots '⋮' button in the **Actions** option on the far right of the relevant page, and then click the **Preview** button.

### How to Clone an Email Template

Click on the three dots '⋮' button in the **Actions** option on the far right of the relevant page, and then click the **Duplicate** button.

### How to Delete an Email Template

Click on the three dots '⋮' button in the **Actions** option on the far right of the relevant page, and then click the **Delete** button.

## How to Add a New Email Template

Follow the steps below to create a new email template for use in a new or existing phishing campaign:

1. Click the **+New** button in the upper right corner of the **Phishing Simulator > Phishing Scenarios > Email Templates** page.
2. Complete the required fields on the first page, then click **Next**.
3. Complete the sections below on the **Email Settings** page:
   1. **Subject:** Subject line of the phishing email
   2. **From Name:** Sender name that will be visible to the target recipient
   3. **From Email Address:** Sender email address information that will be visible to the target recipient
   4. **CC:** Add a CC email address to your phishing simulation email.
   5. **Attach File:** If desired, you can attach a file to the phishing email. This option is only available if the email template method type is set to **Attachment**.
   6. **View/Edit Template:** View and edit the available email templates in localized languages.
   7. **Localize:** Localize your main email template to different languages. Click [here](https://localization.keepnetlabs.com/) to learn the benefits of the feature and more information.
   8. **Show Red Flags:** Let AI Ally scan the email template and highlight suspicious elements—such as mismatched sender addresses, fake buttons, or misleading icons—while employees are expected to spot these red flags on their own.
   9. **Import Email:** Use the three-dot button to import an MSG or EML file and customize it.
4. Click **Edit** to make any changes or **Save** to complete the process.

## How to Add Email Template with Red Flags

Follow the steps below to create a new email template with red flags for use in a new or existing phishing campaign:

1. Click the **+New** button in the upper right corner of the **Phishing Simulator > Phishing Scenarios > Email Templates** page.
2. Complete the required fields on the first page, then click **Next**.
3. Complete the sections below on the **Email Settings** page:
   1. **Subject:** Subject line of the phishing email
   2. **From Name:** Sender name that will be visible to the target recipient
   3. **From Email Address:** Sender email address information that will be visible to the target recipient
   4. **CC:** Add a CC email address to your phishing simulation email. This is optional.
   5. **Attach File:** If desired, you can attach a file to the phishing email. This option is only available if the email template method type is set to **Attachment**.
   6. **View/Edit Template:** View and edit the available email templates in localized languages.
   7. **Localize:** Localize your main email template to different languages.
   8. **Import Email:** Use the three-dot button to import an MSG or EML file and customize it.
4. **Show Red Flags:** Click the button for AI Ally to scan the email template and highlight suspicious elements—such as mismatched sender addresses, fake buttons, or misleading icons—while employees are expected to spot these red flags on their own.
5. Click **Edit** to make any changes or **Save** to complete the process.

Once you save your email template, now click [here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/landing-pages#how-to-add-a-new-landing-page-template-with-red-flags) to learn how to create and use the email template with just-in-time learning page.

## How to Add a New Email Template with AI

Follow the steps below to effortlessly create custom email templates with the help of **AI** **Ally**. Once your template is ready, it can be used in a new or existing phishing campaign:

* Click the **+New** button in the upper right corner of the **Phishing Simulator** > **Phishing Scenarios** > **Email Templates** page.
* Complete the required fields on the first **Template** **Info** page, then click **Next**.
* Click on **Use AI Ally** and describe the scenario and key details for the email template you want to generate.
  * Once described, select the **Language** in which the email template will be created.
  * If you prefer a plain text email template, do not select the **Enable styled HTML format** option. For an HTML-formatted email template, you may choose this option.
* After providing the scenario details, click the **Generate Email Template** button to create your template.
* Once the template is generated, complete the following sections on the **Email Settings** page:
  * **Subject:** AI Ally will write a subject for your email template; you may customize it.
  * **From Name:** Specify the sender's name that will be visible to the recipient.
  * **From Email Address:** Provide the sender's email address that will be visible to the recipient.
  * **CC:** Add a CC email address to your phishing simulation email.
  * **Attach File:** If desired, you can attach a file to the phishing email. This option is only available if the email template method type is set to **Attachment**.
* Click **Edit** to make any changes, or **Save** to finalize the email template creation process.

Here are some helpful ready-to-use AI prompts for creating email templates.

<table><thead><tr><th width="174">Template Name</th><th>Command Prompt</th></tr></thead><tbody><tr><td>IT Policy Update Request</td><td>Make a template that looks like it is coming from our organization’s IT department, notifying the user about a critical policy update that requires their immediate review. The email should contain a link to a document that they need to acknowledge by the end of the day to remain compliant. Make the tone serious, emphasizing the importance of adhering to the new policy.</td></tr><tr><td>Finance Department Alert</td><td>Create a template that appears to be from our Finance Department, asking the user to verify a payment that is scheduled for today. Include a link that directs them to a secure page to review the details. The tone should be urgent and professional, with an emphasis on preventing unauthorized transactions.</td></tr><tr><td>HR Benefits Update</td><td>Make a template that looks like it is coming from our HR department, informing the user about changes to their benefits package. They are asked to log in to the benefits portal via a provided link to review and accept the new terms. The tone should be informative yet urgent, stressing the need to complete this before the end of the week.</td></tr><tr><td>CEO Urgent Assistance Request</td><td>Create a template that appears to come from our CEO, requesting the user’s urgent help in reviewing a confidential document. The CEO should mention that they are relying on the user’s expertise and that a quick response is needed due to a tight deadline. The tone should be friendly but emphasize the urgency of the task.</td></tr><tr><td>Suspicious Login Alert</td><td>Make a template that looks like it is coming from the organization’s security team, warning the user about a suspicious login attempt on their account. The email should urge them to click a link to verify their identity and secure their account. The tone should be urgent, with a focus on protecting the user’s account from unauthorized access.</td></tr><tr><td>Coworker Sharing a Resource</td><td>Create a template that looks like it’s coming from a coworker, sharing a useful resource or guide related to the user’s recent project. The email should include a link that appears to be to a legitimate document-sharing service. The tone should be casual and collaborative, encouraging the user to check it out.</td></tr><tr><td>Payroll Adjustment Notification</td><td>Make a template that seems to be from the Payroll Department, informing the user of a recent adjustment to their paycheck due to an error. Include a link where they can view the updated payment details. The tone should be apologetic for the error but emphasize the need for the user to verify the correction.</td></tr><tr><td>Company Event Registration</td><td>Create a template that looks like it’s from the company’s event planning team, inviting the user to register for an upcoming company-wide event. The email should include a link to a registration page and stress that space is limited, so they should register as soon as possible. The tone should be enthusiastic and encouraging.</td></tr><tr><td>Account Deactivation Notice</td><td>Make a template that looks like it’s from the user’s account management system, warning them that their account will be deactivated if they do not confirm their details by clicking a provided link. The tone should be formal and emphasize the importance of maintaining active status.</td></tr><tr><td>Software Update Required</td><td>Create a template that looks like it’s from the IT department, informing the user that a critical software update is required to maintain system security. The email should include a link to start the update process and make the tone urgent, with a focus on preventing potential security vulnerabilities.</td></tr></tbody></table>

## **Utilizing Merge Tags in Email Templates**

Here's a list of merge tags to help you make your email template more personal. Adding these tags can make your phishing campaign more tailored to the recipient.

<table><thead><tr><th width="172.6571044921875">Merge Tag Name</th><th width="284.2664794921875">Description</th><th width="294.9862060546875">Merge Tag Code</th></tr></thead><tbody><tr><td>Full Name</td><td>Inserts the target user's first and last name.</td><td>{FULLNAME}</td></tr><tr><td>First Name</td><td>Inserts the target user's first name.</td><td>{FIRSTNAME}</td></tr><tr><td>Last Name</td><td>Inserts the target user's last name.</td><td>{LASTNAME}</td></tr><tr><td>Phishing URL</td><td>Inserts a phishing simulation URL for the recipient to click and view the landing page.</td><td>{PHISHINGURL}</td></tr><tr><td>Email</td><td>Inserts the target user's email address.</td><td>{EMAIL}</td></tr><tr><td>From Name</td><td>Inserts the sender's name from the associated email template for this landing page scenario.</td><td>{FROMNAME}</td></tr><tr><td>From Email</td><td>Inserts the sender's email address from the associated email template for this landing page scenario.</td><td>{FROMEMAIL}</td></tr><tr><td>Subject</td><td>Inserts the subject line from the associated email template for this landing page scenario.</td><td>{SUBJECT}</td></tr><tr><td>Company Logo</td><td>Displays your organization's logo, sourced from the <a href="../../company/company-settings/white-labeling">Whitelabeling</a> page.</td><td>Drag the Company logo option into the email template &#x26; it appears as an image placeholder</td></tr><tr><td>Company Name</td><td>Displays your organization's name, sourced from the company profile.</td><td>{COMPANYNAME}</td></tr><tr><td>Date Sent</td><td>Inserts the date when the campaign is launched.</td><td>{DATE_SENT}</td></tr><tr><td>Current Date</td><td>Inserts the current date when the campaign is launched.</td><td>{CURRENT_DATE}</td></tr><tr><td>Current Date Plus 10 Days</td><td>Inserts a date that is 10 days after the campaign's launch date.</td><td>{CURRENT_DATE_PLUS_10_DAYS}</td></tr><tr><td>Current Date Minus 10 Days</td><td>Inserts a date that is 10 days before the campaign's launch date.</td><td>{CURRENT_DATE_MINUS_10_DAYS}</td></tr><tr><td>Random Number One Digit</td><td>Generates and inserts a random one-digit number.</td><td>{RANDOM_NUMBER_1_DIGIT}</td></tr><tr><td>Random Number Two Digit</td><td>Generates and inserts a random two-digit number.</td><td>{RANDOM_NUMBER_2_DIGITS}</td></tr><tr><td>Random Number Three Digit</td><td>Generates and inserts a random three-digit number.</td><td>{RANDOM_NUMBER_3_DIGITS}</td></tr></tbody></table>

## Video Tutorial

The Email Templates page provides you with system-default phishing email templates. You can use them as they are or customize them as needed for your phishing campaign.

{% embed url="<https://youtu.be/SWuM7K3TvAY>" %}
