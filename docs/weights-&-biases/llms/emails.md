# Source: https://docs.wandb.ai/platform/app/settings-page/emails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Add, delete, and manage email addresses and login methods in your W&B profile settings page.

# Manage email settings

Add, delete, manage email types and primary email addresses in your W\&B Profile Settings page. Select your profile icon in the upper right corner of the W\&B dashboard. From the dropdown, select **Settings**. Within the Settings page, scroll down to the Emails dashboard:

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/UhAQoGpm-LvpH3-8/images/app_ui/manage_emails.png?fit=max&auto=format&n=UhAQoGpm-LvpH3-8&q=85&s=36191f575b13a1e3d73d09c1c4e9e635" alt="Email management dashboard" width="1434" height="654" data-path="images/app_ui/manage_emails.png" />
</Frame>

## Manage primary email

The primary email is marked with a 😎 emoji. The primary email is automatically defined with the email you provided when you created a W\&B account.

Select the kebab dropdown to change the primary email associated with your Weights And Biases account:

<Note>
  Only verified emails can be set as primary
</Note>

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/UhAQoGpm-LvpH3-8/images/app_ui/primary_email.png?fit=max&auto=format&n=UhAQoGpm-LvpH3-8&q=85&s=eb64ad48a30858181664651f7e869444" alt="Primary email dropdown" width="454" height="320" data-path="images/app_ui/primary_email.png" />
</Frame>

## Add emails

Select **+ Add Email** to add an email. This will take you to an Auth0 page. You can enter in the credentials for the new email or connect using single sign-on (SSO).

## Delete emails

Select the kebab dropdown and choose **Delete Emails** to delete an email that is registered to your W\&B account

<Note>
  Primary emails cannot be deleted. You need to set a different email as a primary email before deleting.
</Note>

## Log in methods

The Log in Methods column displays the log in methods that are associated with your account.

A verification email is sent to your email account when you create a W\&B account. Your email account is considered unverified until you verify your email address. Unverified emails are displayed in red.

Attempt to log in with your email address again to retrieve a second verification email if you no longer have the original verification email that was sent to your email account.

Contact [support@wandb.com](mailto:support@wandb.com) for account log in issues.
