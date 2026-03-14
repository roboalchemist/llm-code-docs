# Source: https://doc.keepnetlabs.com/next-generation-product/platform/quishing-simulator/manage-quishing-scenarios/quishing-templates.md

# Quishing Templates

The **Quishing Simulator > Quishing Scenarios > Quishing Templates** page provides you with system default quishing email templates. You can use them as they are or customize them as needed for your quishing campaign.

The components of the **Quishing Templates** page are explained below:

<table data-header-hidden><thead><tr><th width="147.5"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Template name</td><td>Name of the email template</td><td></td></tr><tr><td>Quishing Type</td><td><p>The quishing type of the scenario:</p><ul><li><strong>Email:</strong> The email template can be used in a scenario where it can be launched over email.</li><li><strong>Individual Printout:</strong> The email template can be used in a scenario where it can be launched over the printout.</li></ul></td><td></td></tr><tr><td>Method</td><td><p>The quishing technique employed</p><ul><li><strong>Data Submit</strong> = Used to detect target users who submit data on the landing page</li><li><strong>Click-Only</strong> = Used to detect target users who click the unknown link</li><li><strong>MFA:</strong> Used to detect target users who enter their MFA codes on the landing page</li></ul></td><td></td></tr><tr><td>Languages</td><td>List the quishing templates in selected languages.</td><td></td></tr><tr><td>Tags</td><td>Tags can be added to the email template to enable viewing using related tag lists.</td><td></td></tr><tr><td>Difficulty</td><td>The level of difficulty to recognize a phishing attempt <strong>(Easy, Medium, Hard).</strong> Please <a href="../../../phishing-simulator#q-how-is-the-difficulty-level-determined">click here</a> to see how the difficulty level is determined.</td><td></td></tr><tr><td>Created By</td><td><p><strong>System:</strong> Standard quishing email templates are provided with the module.</p><p><br><strong>Custom:</strong> Quishing quishing templates created or customized by users.</p></td><td></td></tr><tr><td>Date Created</td><td>The date and time the email template was created</td><td></td></tr></tbody></table>

## **Quishing Email Template** Actions

This section explains how to create, edit, preview, clone, or delete a quishing email template.

### How to Create a **Quishing** Email Template

Follow the steps below to create a new quishing email template for use in a new or existing quishing campaign:

1. Click the **+ New** button in the upper right corner of the **Quishing Simulator > Quishing Scenarios > Email Template** page.
2. Complete the required fields on the first page, then click **Next**.
3. Write the **"From Email, From Name, Subject,** and **Body"** of the quishing email for your campaign on the **Email Templates** page.
4. In your email template, click "**Edit",** go to "**Merge** **tags",** and drag the "**QR** **Code"** tag into the template to add a QR code.
5. Click **Save** to complete the process.

### How to Create a Printout **Quishing** Email Template

You can create a printout quishing email template where you can use this email template in a printout scenario.

1. Click the **+ NEW** button in the upper right corner of the **Quishing Simulator > Quishing Scenarios > Email Template** page.
2. Click on the **"Individual Printout Template"** option.
3. Complete the required fields on the first page, then click **Next**.
4. Customize your email template by clicking the **Edit** button, then go to "**Merge** **tags",** and drag the "**QR** **Code"** tag into the template to add a QR code.
5. Click **Save** to complete the process.

### How to Edit a **Quishing** Email Template

Click on the **three dots '⋮'** button in the **Actions** option on the far right of the relevant page, and then click the **Edit** button.

### How to Preview a **Quishing** Email Template

Click on the **three dots '⋮'** button in the **Actions** option on the far right of the relevant page, and then click the **Preview** button.

### How to Printout **Quishing** Email Template

Click on the **eye icon (preview)** button under the **Actions** column on the far right of the relevant page.

### How to Clone a **Quishing** Email Template

Click on the **three dots '⋮'** button in the **Actions** option on the far right of the relevant page, and then click the **Duplicate** button.

### How to Delete a **Quishing** Email Template

Click on the **three dots '⋮'** button in the **Actions** option on the far right of the relevant page, and then click the **Delete** button.

## **Utilizing Merge Tags in Quishing** Email **Templates**

Here's a selection of merge tags to customize your email template for a more personalized quishing campaign. Using these tags can make your simulated phishing attack more specific to each recipient.

<table><thead><tr><th width="210.5">Merge Tag</th><th>Description</th></tr></thead><tbody><tr><td>Full Name</td><td>Inserts the target user's first and last name.</td></tr><tr><td>First Name</td><td>Inserts the target user's first name.</td></tr><tr><td>Last Name</td><td>Inserts the target user's last name.</td></tr><tr><td>QR Code</td><td>Inserts the QR code into your email template for users to scan it.</td></tr><tr><td>Email</td><td>Inserts the target user's email address.</td></tr><tr><td>From Name</td><td>Inserts the sender's name from the associated email template for this landing page scenario.</td></tr><tr><td>From Email</td><td>Inserts the sender's email address from the associated email template for this landing page scenario.</td></tr><tr><td>Subject</td><td>Inserts the subject line from the associated email template for this landing page scenario.</td></tr><tr><td>Company Logo</td><td>Displays your organization's logo, sourced from the <a href="../../company/company-settings/white-labeling">Whitelabeling</a> page.</td></tr><tr><td>Company Name</td><td>Displays your organization's name, sourced from the company profile.</td></tr><tr><td>Date Sent</td><td>Inserts the date when the campaign is launched.</td></tr><tr><td>Current Date</td><td>Inserts the current date when the campaign is launched.</td></tr><tr><td>Current Date Plus 10 Days</td><td>Inserts a date that is 10 days after the campaign's launch date.</td></tr><tr><td>Current Date Minus 10 Days</td><td>Inserts a date that is 10 days before the campaign's launch date.</td></tr><tr><td>Random Number One Digit</td><td>Generates and inserts a random one-digit number.</td></tr><tr><td>Random Number Two Digit</td><td>Generates and inserts a random two-digit number.</td></tr><tr><td>Random Number Three Digit</td><td>Generates and inserts a random three-digit number.</td></tr></tbody></table>

## Video Tutorial

The **Email** **Templates** page provides you with system-default quishing email templates. You can use them as they are or customize them as needed for your quishing campaign.

{% embed url="<https://youtu.be/RnbfRh7KGVI>" %}
