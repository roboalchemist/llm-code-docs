# Source: https://tyk.io/docs/product-stack/tyk-enterprise-developer-portal/getting-started/setup-email-notifications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up email notification service

> Learn how to set up email notifications in the Tyk Enterprise Developer Portal.

## Email Configuration

Configuring the emailing settings is necessary for the portal to send notifications to admin users and API consumers.
Once the configuration is finished, the portal will send emails upon the following events:

* Password reset;
* New access request;
* Access request approved;
* Access request rejected;
* Pending user registration request;
* Invitation to a user to register in the portal;
* User account is activated;
* User account is deactivated;
* New Organisation registration request is created;
* Organisation registration request is accepted;
* Organisation registration request is rejected.

**Prerequisites**

Before setting up the emailing configuration, you need your email server up and running.
To complete the email setup, you will need the following information about your SMTP server:

* Address of your SMTP server;
* A port on which it accepts connections;
* Username and password to connect to your SMTP server.

## Portal Admin User Notifications

To start with, you need to configure an email address where the portal will send notifications for admin users: new API Product access requests, new Organisation registration requests, and so on.
For that, you need to navigate to the General section in the Setting menu, scroll down to the Portal admin notification address, and specify the admin email address in the Portal admin email field.

<img src="https://mintcdn.com/tyk/wHLHFqRiMZq91WJo/img/dashboard/portal-management/enterprise-portal/admin_email_settings.png?fit=max&auto=format&n=wHLHFqRiMZq91WJo&q=85&s=19f5495d14dce4381da4d30031a944a7" alt="Portal admin notification address settings" width="3024" height="1530" data-path="img/dashboard/portal-management/enterprise-portal/admin_email_settings.png" />

## Outbound Mailing

### The default from email

To enable the portal to send notifications to admin users and API Consumers, you need to specify the outbound email address in the Default Email From field.
No notifications will be sent until the Default Email From field is specified.

<img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/default_from_email_settings.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=da3c3f63810726819faafe620ed9c070" alt="Default from email settings" width="3024" height="1526" data-path="img/dashboard/portal-management/enterprise-portal/default_from_email_settings.png" />

### Email Subjects

Once the default from email is configured, you can specify subjects for notifications.
If you don’t, the default subjects will be used for email notifications.

<img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/email_subjects_settings.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=f5b0da1d9bad71b57642252be6ca2607" alt="Email subject settings" width="3024" height="1524" data-path="img/dashboard/portal-management/enterprise-portal/email_subjects_settings.png" />

### SMTP Server Settings

Once the default from email, the admin notification email, and the subjects for outbound emails are configured, you need to configure settings for the SMTP server.
To do so, navigate to the SMTP setting section in the Settings/General menu and specify:

* Your SMTP server host and port;
* The SMTP username and password if authentication is configured for your SMTP server.

<img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/smtp_settings.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=2553992fabe165ca8b910ec37862c6b5" alt="SMTP settings" width="3024" height="1518" data-path="img/dashboard/portal-management/enterprise-portal/smtp_settings.png" />


Built with [Mintlify](https://mintlify.com).