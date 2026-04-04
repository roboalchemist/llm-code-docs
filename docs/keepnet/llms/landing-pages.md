# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/manage-phishing-scenarios/landing-pages.md

# Landing Pages

Landing pages direct the user to a specific page, and can be used for a variety of purposes, such as requesting login credentials or other sensitive information.

The [**Phishing Simulator**](https://keepnetlabs.com/products/phishing-simulator) **> Phishing Scenarios > Landing Page Templates** page contains standard default landing pages you can select and use for your phishing scenario or customize according to your preferences. You also have the option to create an entirely new landing page.

The components of the **Landing Page Templates** page are explained below.

<table><thead><tr><th width="150"></th><th width="590.1428571428571"></th></tr></thead><tbody><tr><td>Template name</td><td>The name of the landing page template</td></tr><tr><td>Method</td><td><p>The phishing technique employed.</p><ul><li><strong>Data Submit:</strong> Used to detect target users who submit data on the landing page</li><li><strong>Attachment:</strong> Used to detect target users who download the attachment in the phishing simulation email</li><li><strong>Click-Only:</strong> Used to detect target users who click unknown links in the phishing email</li></ul></td></tr><tr><td>Languages</td><td>Filter landing pages based on your preferred languages.</td></tr><tr><td>Difficulty</td><td>The level of difficulty to recognize a phishing attempt <strong>(Easy, Medium, Hard).</strong> Please <a href="../..#q-how-is-the-difficulty-level-determined">click here</a> to see how the difficulty level is determined.</td></tr><tr><td>Creation Type</td><td>Filter landing pages based on their creation type (e.g., Manual or AI Ally).</td></tr><tr><td>Created By</td><td><p><strong>System:</strong> Standard landing page templates are provided with the product.</p><p><strong>Custom:</strong> Landing pages created or customized by users</p></td></tr><tr><td>Stop Bot Activity</td><td>It shows the stop bot activity feature enabled for the landing page. By default, it is enabled and cannot be disabled to ensure that the target user activities are accurately captured.</td></tr><tr><td>Tags</td><td>Tags can be added to the landing page to enable viewing using related tag lists.</td></tr><tr><td>Date Created</td><td>The date and time the landing page was created</td></tr></tbody></table>

## Landing Page Templates Actions

This section explains how to edit, preview, clone, or delete a landing page.

### How to Edit a Landing Page Template

Click on the three dots '⋮' button in the **Actions** option on the far right of the relevant page, and then click the **Edit** button.

### How to Preview a Landing Page

Click on the three dots '⋮' button in the **Actions** option on the far right of the relevant page, and then click the **Preview** button.

### How to Clone a Landing Page

Click on the three dots '⋮' button in the **Actions** option on the far right of the relevant page, and then click the **Duplicate** button.

### How to Delete a Landing Page

Click on the three dots '⋮' button in the **Actions** option on the far right of the relevant page, and then click the **Delete** button.

## How to Add a New Landing Page Template

Follow the steps below to add a new landing page that you can use in a new or existing phishing scenario:

1. Click the **+New** button in the upper right corner of the **Phishing Simulator > Phishing Scenarios > Landing Page Templates** page.
2. Complete the required fields on the first **Template** **Info** page, then click **Next**.
3. On the **Page Settings** page, provide the **Phishing Link:** the URL to be used in the phishing email.
4. **Localize:** Localize your main landing page template to different languages. Click [here](https://localization.keepnetlabs.com/) to learn the benefits of the feature and more information.
5. Click **Edit** to make any changes or **Save** to complete the process.

## How to Add a Second Page Using the Template Picker

You can add a second page to any landing page template without building it from scratch. A **template picker for Page 2** lets you reuse an existing landing page as the second page with a single click.

**To add a second page to a landing page template:**

1. Create a new landing page or open an existing one for editing (see [How to Add a New Landing Page Template](#how-to-add-a-new-landing-page-template) or [How to Edit a Landing Page Template](#how-to-edit-a-landing-page-template)).
2. On the **Page Settings** step (or when editing the template), use the **template picker for Page 2** to choose a second page.
3. Select any existing **Click-Only** or **Data Submission** landing page from your library — it will be added as Page 2 automatically.
4. Click **Save** to apply. You no longer need to build the second page manually or copy HTML.

This applies to landing page templates in **Phishing Simulator**. The same template picker for Page 2 is also available in [Smishing Simulator](https://doc.keepnetlabs.com/next-generation-product/smishing-simulator/manage-smishing-scenarios/landing-page-templates#how-to-add-a-second-page-using-the-template-picker) and [Quishing Simulator](https://doc.keepnetlabs.com/next-generation-product/quishing-simulator/manage-quishing-scenarios/quishing-landing-page-templates#how-to-add-a-second-page-using-the-template-picker).

## How to Add Just-in-time Learning Page

Follow the steps below to add a new just-in-time learning page that you can use in a new or existing phishing scenario:

1. Go to **Phishing Simulator > Phishing Scenarios > Landing Page Templates** page.
2. Search **'Just-in-time Learning Page: Email Warning Signs'** and click the **Duplicate** button to customize.
3. Customize any fields on the first **Template** **Info** page, then click **Next**.
4. On the **Page Settings** page, provide the **Phishing Link:** the URL to be used in the phishing email.
5. Review your red flag landing page, or click the **Edit** button to customize it.
6. Once you complete customization or review, click **Save** to complete the process.

Once you create your just-in-time learning page, now click [here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/phishing-scenarios#how-to-add-a-new-phishing-scenario-with-red-flags) to learn how to combine your red flag email template and just-in-time learning page in a scenario to be able to launch to your employees.

## How to Add a new Landing Page with AI

Follow the steps below to effortlessly create custom landing page templates with the help of **AI** **Ally**. Once your landing page template is ready, it can be used in a new or existing phishing campaign:

* Click the **+New** button in the upper right corner of the **Phishing Simulator** > **Phishing Scenarios** > **Landing Page Templates** page.
* Complete the required fields on the first **Template** **Info** page, then click **Next**.
* On the **Page Settings** page, provide the **Phishing Link:** the URL to be used in the phishing email.
* Click on **Use AI Ally** and describe the scenario and key details for the landing page you want to generate.
  * Once described, select the **Language** in which the landing page will be created.
* After providing the scenario details, click the **Generate Landing Page** button to create your landing page.
* Once the landing page is generated, click **Edit** to make any changes, or **Save** to finalize the landing page template creation process.

Here are some helpful ready-to-use AI prompts for creating landing pages.

<table><thead><tr><th width="137">Template Name</th><th width="133">Method Type</th><th width="435">Command Prompt</th></tr></thead><tbody><tr><td>Google Login Page</td><td>Data Submission</td><td>Create a landing page that closely resembles the Google Login Page. Ensure the design includes fields for email and password input, a "Forgot email?" link, and a "Next" button. Include a Google logo at the top and a small text link for "Help" and "Privacy Policy". The page should have a clean, minimalistic design with a white background.</td></tr><tr><td>Amazon Login Page</td><td>Data Submission</td><td>Create a landing page that looks like the Amazon Login Page. Include fields for email and password, a "Forgot Password?" link, and a "Sign-In" button. Add a small Amazon logo at the top and include a checkbox for "Keep me signed in". Below the login form, include a "Create your Amazon account" link. The design should have a white background with light gray borders.</td></tr><tr><td>Company Event Registration Form</td><td>Data Submission</td><td>Create a landing page for a company event registration. Include fields for full name, email, phone number, and a dropdown to select the department. Add a "Register" button at the bottom. The page should also include a banner at the top with the company logo and event name. The color scheme should match typical corporate branding with a professional look.</td></tr><tr><td>Password Reset Page</td><td>Data Submission</td><td>Create a landing page for a system password reset. Include a field for entering the email address, a "Submit" button, and a link for "Contact Support" in case the user has trouble resetting their password. The design should be simple with a white background, and include a small company logo at the top. The instructions should be clear and concise.</td></tr><tr><td>Bank Account Login Page</td><td>Data Submission</td><td>Create a landing page that mimics a bank account login page. Include fields for "Username" and "Password", a "Forgot Username or Password?" link, and a "Sign In" button. Add a small bank logo at the top, and include links for "Enroll Now" and "Help". The design should be secure and professional, with a dark blue and white color scheme.</td></tr><tr><td>Subscription Confirmation Page</td><td>Data Submission</td><td>Create a landing page for subscription confirmation. Include a message saying "Thank you for subscribing!", a field for entering an email address to confirm the subscription, and a "Confirm Subscription" button. Add a small note about privacy at the bottom. The design should be clean and modern, with a focus on ease of use.</td></tr><tr><td>E-commerce Checkout Page</td><td>Data Submission</td><td>Create a landing page for an e-commerce checkout process. Include fields for billing information (name, address, city, state, zip code), payment information (credit card number, expiration date, CVV), and a "Place Order" button. Add a small shopping cart icon at the top, and a summary of the order on the right side. The design should be user-friendly with a focus on security.</td></tr><tr><td>Event Ticket Purchase Page</td><td>Data Submission</td><td>Create a landing page for purchasing event tickets. Include fields for selecting the number of tickets, seating options, and payment details. Add a "Purchase Tickets" button at the bottom, and a small banner at the top with the event name and date. The design should be vibrant and engaging, with a focus on creating excitement for the event.</td></tr><tr><td>Phishing Awareness Oops Page</td><td>Click Only</td><td>Create a landing page that tells the user they've clicked on a simulated phishing email. The message should say "Oops! The email you just clicked was a phishing simulation. Don't worry, this is to help you learn." Include three key rules: 1. Avoid unknown links/attachments. 2. Verify the sender's email. 3. Be cautious of too-good-to-be-true offers. The design should be clear and educational.</td></tr><tr><td>Security Training Oops Page</td><td>Click Only</td><td>Create a landing page that informs the user they interacted with a simulated phishing email. The message should say "Oops! You just clicked on a test phishing email for training purposes." Include three rules: 1. Avoid unknown links. 2. Verify sender legitimacy. 3. Be cautious of urgent requests. Design it to be instructional and easy to understand.</td></tr></tbody></table>

## **Utilizing JavaScript on Landing Pages**

JavaScript enhances landing pages with dynamic behavior and interactivity. This capability helps you create more engaging and realistic phishing simulations by enabling features such as:

1. **Real-time content manipulation**\
   Example: Add a countdown timer that shows “You have 30 seconds left to complete this form.” This creates urgency and makes the simulation feel more realistic.
2. **Form validation**\
   Example: When a user tries to submit a form without entering an email address, JavaScript can show a warning like: “Please enter your email before submitting.” This mimics real websites that check inputs.
3. **Conditional content display**\
   Example: Show a hidden message only if a user types in a certain keyword or clicks a specific button, such as “Access Granted” after filling a field correctly.

Please follow the steps below to use the JavaScript code editor feature.

* Go to **Phishing Simulator > Phishing Scenarios > Landing Pages**
* Click **+ NEW** to create a new landing page
* Complete the required fields on the first page, then click **Next**
* Click **Edit** at the bottom center of the page to open the landing page editor
* At the top of the editor, click **Import** to open the HTML code editor
* Inside the editor, locate the notice: *“Some scripts may be blocked for security reasons. Click here to add custom JavaScript code.”*
* Click the link to open a pop-up where you can safely insert your JavaScript
* After inserting your script, click **Save** to apply your changes and publish the landing page

You can now [create a scenario](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/manage-phishing-scenarios/phishing-scenarios) with your email template and landing page and then [launch](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/phishing-campaign-manager) it to your email inbox to test the landing page to confirm if everything works as you expect.

## **Utilizing Merge Tags in Landing Page Templates**

Here's a list of merge tags to help you make your landing pages more personal. Adding these tags can make your phishing campaign more tailored to the recipient.

<table><thead><tr><th width="197.96484375">Merge Tag</th><th>Description</th></tr></thead><tbody><tr><td>Full Name</td><td>Inserts the target user's first and last name.</td></tr><tr><td>First Name</td><td>Inserts the target user's first name.</td></tr><tr><td>Last Name</td><td>Inserts the target user's last name.</td></tr><tr><td>Email</td><td>Inserts the target user's email address.</td></tr><tr><td>From Name</td><td>Inserts the sender's name from the associated email template for this landing page scenario.</td></tr><tr><td>From Email</td><td>Inserts the sender's email address from the associated email template for this landing page scenario.</td></tr><tr><td>Subject</td><td>Inserts the subject line from the associated email template for this landing page scenario.</td></tr><tr><td>Company Logo</td><td>Displays your organization's logo, sourced from the <a href="../../company/company-settings/white-labeling">Whitelabeling</a> page.</td></tr><tr><td>Company Name</td><td>Displays your organization's name, sourced from the company profile.</td></tr><tr><td>Date Sent</td><td>Inserts the date when the campaign is launched.</td></tr><tr><td>Current Date</td><td>Inserts the current date when the campaign is launched.</td></tr><tr><td>Current Date Plus 10 Days</td><td>Inserts a date that is 10 days after the campaign's launch date.</td></tr><tr><td>Current Date Minus 10 Days</td><td>Inserts a date that is 10 days before the campaign's launch date.</td></tr><tr><td>Random Number One Digit</td><td>Generates and inserts a random one-digit number.</td></tr><tr><td>Random Number Two Digit</td><td>Generates and inserts a random two-digit number.</td></tr><tr><td>Random Number Three Digit</td><td>Generates and inserts a random three-digit number.</td></tr><tr><td>User Language</td><td>Inserts the target user's Preferred Language information on the landing page</td></tr><tr><td>User Department</td><td>Inserts the target user's Department information on the landing page.</td></tr></tbody></table>

## Video Tutorial

Landing pages direct the user to a specific page and can be used for a variety of purposes, such as requesting login credentials or other sensitive information. This tutorial will walk through the steps of creating/editing a landing page.

{% embed url="<https://youtu.be/9k45qxAhHR0>" %}

## FAQs

### Q: Can I divert employees who click the link to a URL not hosted by Keepnet?

A: Yes! You can direct users to your own URL instead of using a standard Keepnet landing page. To set this up, select a Keepnet landing page, and replace the URL in the provided HTML code with the URL of your hosted landing page. Here’s how you do it:

1. Choose a Keepnet landing page for your phishing scenario.
2. Insert the following HTML code, substituting `https://www.google.com` with your own landing page URL:

   ```html
   htmlCopy code<meta http-equiv="refresh" content="1; URL=https://www.your-landing-page.com" />
   ```

This setup will automatically redirect anyone who clicks on the link to your chosen landing page after 1 second, allowing us to track the click-through.
