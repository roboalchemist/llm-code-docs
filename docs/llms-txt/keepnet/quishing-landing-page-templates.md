# Source: https://doc.keepnetlabs.com/next-generation-product/platform/quishing-simulator/manage-quishing-scenarios/quishing-landing-page-templates.md

# Quishing Landing Page Templates

The **Quishing Simulator > Quishing Scenarios > Landing Page Templates** page has ready-to-use landing page designs. You can use these pages as they are or customize them for your quishing campaigns. Landing pages take users to a specific webpage, which can either give them information about the phishing campaign or ask for their credentials.

The components of the **Landing Page Templates** page are explained below.

<table data-header-hidden><thead><tr><th width="147.5"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Template name</td><td>Name of the landing page template</td><td></td></tr><tr><td>Method</td><td><p>The quishing technique employed</p><p><strong>Data Submit</strong> = Used to detect target users who submit data on the landing page<br><br><strong>Click-Only</strong> = Used to detect target users who click the unknown link</p></td><td></td></tr><tr><td>Language</td><td>List the landing page templates in selected languages.</td><td></td></tr><tr><td>Tags</td><td>Tags can be added to the email template to enable viewing using related tag lists.</td><td></td></tr><tr><td>Difficulty</td><td>The level of difficulty to recognize a phishing attempt <strong>(Easy, Medium, Hard).</strong> Please <a href="../../../phishing-simulator#q-how-is-the-difficulty-level-determined">click here</a> to see how the difficulty level is determined.</td><td></td></tr><tr><td>Created By</td><td><p><strong>System:</strong> Standard phishing landing page templates are provided with the module.</p><p><br><strong>Custom:</strong> Quishing landing page templates created or customized by users.</p></td><td></td></tr><tr><td>Stop bots to prevent false clicks</td><td>The bots prevention feature is enabled or disabled for the landing page.</td><td></td></tr><tr><td>Date Created</td><td>The date and time the landing page template was created</td><td></td></tr></tbody></table>

## Landing Page Templates Actions

This section explains how to create, edit, preview, clone, or delete a landing page.

### How to Create a New Landing Page Template

Follow the steps below to add a new landing page that you can use in a new or existing quishing scenario:

1. Click the **+New** button in the upper right corner of the **Quishing Simulator > Quishing Scenarios > Landing Page Templates** page.
2. Complete the required fields on the first page, then click **Next**.
3. On the **Page Settings** page, provide the **QR Code Link:** the URL to be used to redirect users to this page after scanning the QR code.
4. Under the **QR Code** **Link** field, you can enable the **"Stop bots to prevent false clicks"** feature to detect and stop bot activity automatically to prevent false clicks, ensuring genuine traffic to your quishing campaign.
5. Click **Edit** to make any customization on the landing page or **Save** to complete the process.

## How to Add a Second Page Using the Template Picker

You can add a second page to any landing page template without building it from scratch. A **template picker for Page 2** lets you reuse an existing landing page as the second page with a single click.

**To add a second page to a landing page template:**

1. Create a new landing page or open an existing one for editing (see [How to Create a New Landing Page Template](#how-to-create-a-new-landing-page-template) or [How to Edit a Landing Page Template](#how-to-edit-a-landing-page-template)).
2. On the **Page Settings** step (or when editing the template), use the **template picker for Page 2** to choose a second page.
3. Select any existing **Click-Only** or **Data Submission** landing page from your library — it will be added as Page 2 automatically.
4. Click **Save** to apply. You no longer need to build the second page manually or copy HTML.

The same feature is available in [Phishing Simulator](https://doc.keepnetlabs.com/next-generation-product/phishing-simulator/manage-phishing-scenarios/landing-pages#how-to-add-a-second-page-using-the-template-picker) and [Smishing Simulator](https://doc.keepnetlabs.com/next-generation-product/smishing-simulator/manage-smishing-scenarios/landing-page-templates#how-to-add-a-second-page-using-the-template-picker).

### How to Edit a Landing Page Template

Click on the **three dots '⋮'** button in the **Actions** option on the far right of the relevant page, and then click the **Edit** button.

### How to Preview a Landing Page

Click on the **eye icon (preview)** button under the **Actions** column on the far right of the relevant page.

### How to Clone a Landing Page

Click on the **three dots '⋮'** button in the **Actions** option on the far right of the relevant page, and then click the **Duplicate** button.

### How to Delete a Landing Page

Click on the **three dots '⋮'** button in the **Actions** option on the far right of the relevant page, and then click the **Delete** button.

## **Utilizing Merge Tags in Landing Page Templates**

Here's a list of merge tags to help you make your landing pages more personal. Adding these tags can make your quishing campaign more tailored to the recipient.

<table><thead><tr><th width="210.5">Merge Tag</th><th>Description</th></tr></thead><tbody><tr><td>Full Name</td><td>Inserts the target user's first and last name.</td></tr><tr><td>First Name</td><td>Inserts the target user's first name.</td></tr><tr><td>Last Name</td><td>Inserts the target user's last name.</td></tr><tr><td>Email</td><td>Inserts the target user's email address.</td></tr><tr><td>Company Name</td><td>Displays your organization's name, sourced from the company profile.</td></tr><tr><td>Date Sent</td><td>Inserts the date when the campaign is launched.</td></tr><tr><td>Current Date</td><td>Inserts the current date when the campaign is launched.</td></tr><tr><td>Current Date Plus 10 Days</td><td>Inserts a date that is 10 days after the campaign's launch date.</td></tr><tr><td>Current Date Minus 10 Days</td><td>Inserts a date that is 10 days before the campaign's launch date.</td></tr><tr><td>Random Number One Digit</td><td>Generates and inserts a random one-digit number.</td></tr><tr><td>Random Number Two Digit</td><td>Generates and inserts a random two-digit number.</td></tr><tr><td>Random Number Three Digit</td><td>Generates and inserts a random three-digit number.</td></tr><tr><td>User Language</td><td>Inserts the target user's Preferred Language information on the landing page</td></tr><tr><td>User Department</td><td>Inserts the target user's Department information on the landing page.</td></tr></tbody></table>

## Video Tutorial

**Landing** **pages** direct the user to a specific page and can be used for a variety of purposes, such as requesting login credentials or other sensitive information. This tutorial will walk through the steps of creating/editing a landing page.

{% embed url="<https://youtu.be/j69ht6Me6Do>" %}
