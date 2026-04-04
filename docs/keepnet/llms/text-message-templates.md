# Source: https://doc.keepnetlabs.com/next-generation-product/platform/smishing-simulator/manage-smishing-scenarios/text-message-templates.md

# Text Message Templates

The **Smishing Simulator > Scenarios > Text Message Templates** page provides you with system default smishing text templates. You can use them as they are or customize them as needed for your smishing campaign.

The components of the **Text Message Templates** page are explained below:

<table data-header-hidden><thead><tr><th width="147.5"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Template name</td><td>Name of the email template</td><td></td></tr><tr><td>Method</td><td><p>The smishing technique employed<br></p><ul><li><strong>Data Submission</strong> = Used to detect target users who submit data on the landing page</li><li><strong>Click Only</strong> = Used to detect target users who click unknown links in the smishing text</li></ul></td><td></td></tr><tr><td>Tags</td><td>Tags can be added to the email template to enable viewing using related tag lists.</td><td></td></tr><tr><td>Difficulty</td><td>The level of difficulty to recognize a phishing attempt <strong>(Easy, Medium, Hard).</strong> Please <a href="../..#q-how-is-the-difficulty-level-determined">click here</a> to see how the difficulty level is determined.</td><td></td></tr><tr><td>Created By</td><td><p><strong>System:</strong> Standard phishing email templates are provided with the module.</p><p><br><strong>Custom:</strong> smishing text created or customized by users.</p></td><td></td></tr><tr><td>Date Created</td><td>The date and time the email template was created</td><td></td></tr></tbody></table>

## **Text Message Template** Actions

This section explains how to create, edit, preview, clone, or delete a text message email template.

### How to Create a Text Message Template

Follow the steps below to create a new text template for use in a new or existing smishing campaign:

1. Click the **+New** button in the upper right corner of the **Smishing Simulator > Smishing Scenarios > Template Info** page.
2. Complete the required fields on the first page, then click **Next**.
3. Write the text message for your template on the **Text Message Settings** page.\
   **Note:** Use the merge tag **{PHISHINGURL}** for the link to be added to the text message
4. Click **Save** to complete the process.

### How to Edit a Text Message Template

Click on the **three dots '⋮'** button in the **Actions** option on the far right of the relevant page, and then click the **Edit** button.

### How to Preview a Text Message Template

Click on the **eye icon (preview)** button under the **Actions** column on the far right of the relevant page.

### How to Clone a Text Message Template

Click on the **three dots '⋮'** button in the **Actions** option on the far right of the relevant page, and then click the **Duplicate** button.

### How to Delete a Text Message Template

Click on the **three dots '⋮'** button in the **Actions** option on the far right of the relevant page, and then click the **Delete** button.

## **Utilizing Merge Tags in Text Message Templates**

Here's a list of merge tags to help you make your SMS text message template more personal. Adding these tags can make your phishing campaign more tailored to the recipient.

<table><thead><tr><th width="210.5">Merge Tag</th><th>Description</th></tr></thead><tbody><tr><td>Full Name</td><td>Inserts the target user's first and last name.</td></tr><tr><td>First Name</td><td>Inserts the target user's first name.</td></tr><tr><td>Last Name</td><td>Inserts the target user's last name.</td></tr><tr><td>Phishing URL</td><td>Inserts a phishing simulation URL for the recipient to click and view the landing page.</td></tr><tr><td>Company Name</td><td>Displays your organization's name, sourced from the company profile.</td></tr><tr><td>Date Sent</td><td>Inserts the date when the campaign is launched.</td></tr><tr><td>Current Date</td><td>Inserts the current date when the campaign is launched.</td></tr><tr><td>Current Date Plus 10 Days</td><td>Inserts a date that is 10 days after the campaign's launch date.</td></tr><tr><td>Current Date Minus 10 Days</td><td>Inserts a date that is 10 days before the campaign's launch date.</td></tr><tr><td>Random Number One Digit</td><td>Generates and inserts a random one-digit number.</td></tr><tr><td>Random Number Two Digit</td><td>Generates and inserts a random two-digit number.</td></tr><tr><td>Random Number Three Digit</td><td>Generates and inserts a random three-digit number.</td></tr></tbody></table>

## Video Tutorial

The **Text** **Message** **Templates** page provides you with system-default phishing email templates. You can use them as they are or customize them as needed for your phishing campaign.

{% embed url="<https://youtu.be/8mImcO1OU2U>" %}
