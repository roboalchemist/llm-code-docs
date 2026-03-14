# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/smtp-settings.md

# SMTP Settings

This section explains the functionality of SMTP Settings and provides some related use cases to assist you in creating an optimal configuration.

To access the SMTP settings, go to **Company > Company Settings > SMTP Settings**.

## What is SMTP used for?

The Simple Mail Transfer Protocol (SMTP) is an internet standard communication protocol for email transmission. The platform includes a default email service available to all customers; however, you also have the option to use your own email server to send phishing, training and other emails.

{% hint style="warning" %}
If you have the [Phishing Simulator](https://keepnetlabs.com/products/phishing-simulator) product, enabling SMTP relay authorization on the mail server will allow you to mimic brand impersonation phishing techniques, including the sender's address information.
{% endhint %}

The steps below explain how to define proxy server settings for the platform to access the internet or other networks.

## SMTP Settings Page

You can view, edit, or delete any SMTP configurations at the **Company > Company Settings > SMTP Settings** page.

<table><thead><tr><th width="169"></th><th width="579.1428571428571"></th></tr></thead><tbody><tr><td>Name</td><td>The SMTP settings name.</td></tr><tr><td>SMTP Address</td><td>The SMTP server address (hostname or IP address)</td></tr><tr><td>Created By</td><td>The company name who created the SMTP settings.</td></tr><tr><td>Date Created</td><td>The date and time that SMTP settings were created.</td></tr><tr><td>Status</td><td>The status can be set to inactive to not to use SMTP settings anymore.</td></tr><tr><td>Actions</td><td>The SMTP settings can be edited or deleted.</td></tr></tbody></table>

## How to Configure the SMTP

Go to **Company > Company Settings > SMTP Settings** from the main menu. Then click **+ NEW** to create a new SMTP setting.

The components of the SMTP setting page are:

<table><thead><tr><th width="150"></th><th width="519.1428571428571"></th></tr></thead><tbody><tr><td>SMTP Setting Name</td><td>Name of the SMTP setting</td></tr><tr><td>Service Provider</td><td>Select an SMTP service provider from predefined options such as Gsuite, O365, or Custom.</td></tr><tr><td>SMTP Server Address</td><td>Host/IP address and port information of the SMTP server</td></tr><tr><td>Username or Email Address</td><td>Username or email address to be used for the SMTP</td></tr><tr><td>Password</td><td>Password for the SMTP username or email address</td></tr><tr><td>Use Authentication</td><td>Select this option if your SMTP server requires authentication</td></tr><tr><td>Use SSL</td><td>Select this option if the email service supports or requires an SSL connection</td></tr><tr><td>Has SMTP Relay</td><td>Select this option if SMTP relay authorization is enabled on email server for the platform</td></tr><tr><td>Make Available For</td><td>Choose companies where SMTP settings will be available to be used by chosen companies.</td></tr><tr><td>Reply To</td><td>The email address that will be receiving the reply if an email user tries to reply to training, phishing or other emails that have been sent from the platform</td></tr><tr><td>Error To</td><td>Error messages will be delivered to this email address</td></tr><tr><td>CC</td><td>Email address that will receive a copy of sent emails</td></tr><tr><td>BCC</td><td>Email address that will receive a blind copy of sent emails. Primary and secondary recipients cannot see tertiary recipients</td></tr><tr><td>Custom Header</td><td>The header of the email that will be sent can be customized</td></tr></tbody></table>

{% hint style="warning" %}
**Make Available For option is only available for system admins with a Reseller role**
{% endhint %}

## Test SMTP Settings

You can check whether the email has been sent via the defined email server by simply clicking on the **Send** **Test** **Email** button on the email settings page.

You will receive a notification of a successful test if everything is correct. If settings are failed, you will receive a notification of an error message that will show what’s the configuration issue.

## FAQ

### Q: Once an SMTP connection has been configured, can I send an email on the platform with different domain addresses?

A: Yes. If your SMTP server has an SMTP relay feature enabled, you can send mail using more than one domain address. If the SMTP relay has not been activated, you can only send emails using corporate domains authorized for your email server.

### Q: Can I create more than one SMTP in the system?

A: Yes. The platform offers the flexibility to use several SMTP configurations.

### Q: Can I choose the SMTP to be used for a phishing or training campaign?

A: Yes. You can select the SMTP to be used when you launch a campaign at Phishing Simulator > Campaign Manager for phishing campaigns.

### Q: Can I choose the SMTP to be used for my notification templates?

A: Yes. You can set the SMTP information to notification templates by editing the templates from **Company Settings > Notification Templates**.
