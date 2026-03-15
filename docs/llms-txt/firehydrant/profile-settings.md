# Source: https://docs.firehydrant.com/docs/profile-settings.md

# Profile Settings

<Image alt="Example user profile page" align="center" width="650px" src="https://files.readme.io/625ae66-CleanShot_2024-08-13_at_16.10.33.png">
  Example user profile page
</Image>

Profile settings allow users to modify details and behavior surrounding their FireHydrant experience.

## Profile

* **Avatar**- Users can import their Slack avatar if they have linked their Slack accounts to FireHydrant. Learn more about [linking accounts here](https://docs.firehydrant.com/docs/slack-integration#linking-users)
* **Your name** - User's name. This impacts how the user's name is displayed everywhere in FireHydrant
* **Your email** - User's email. If you have configured [SSO with SAML](https://docs.firehydrant.com/docs/sso-with-saml) then this field will not be available to change
* **Alternate Emails** - FireHydrant typically uses OAuth connections to match users between FireHydrant and other applications, but sometimes FireHydrant needs email addresses to compare (for example, Jira Server). Alternate emails help for applications with which FireHydrant cannot use OAuth to link accounts.
* **Phone Numbers (Signals-only)** - You can set up and verify phone numbers to be used with Signals notifications. For more information, visit [Notification Preferences](https://docs.firehydrant.com/docs/signals-notification-preferences).
* **Linked Accounts** - For integrations configured with FireHydrant, users will need to link their 3rd-party accounts with FireHydrant accounts to attribute users (e.g., ticketing assignees, meeting hosts, and more). The specific function varies by integration. Clicking "Link" on any of these will take the user through an OAuth flow.

## Signals Notifications

<Image alt="Signals Notification preferences" align="center" width="650px" src="https://files.readme.io/ffff2b3-CleanShot_2024-08-13_at_16.28.27.png">
  Signals Notification preferences
</Image>

This tab is only visible if you have [FireHydrant Signals](https://docs.firehydrant.com/docs/signals-introduction) enabled. Here, you can configure how you'd like to be paged when an alert is opened and you are on-call. You can also configure reminders for shifts you're assigned to.

For more information, visit [Notification Preferences](https://docs.firehydrant.com/docs/signals-notification-preferences).

## Password & Security

<Image alt="Password & Security tab" align="center" width="400px" src="https://files.readme.io/346982e-CleanShot_2024-08-13_at_16.26.11.png">
  Password & Security tab
</Image>

This tab allows you to change your password or request a password reset flow if you've lost/forgotten your password. The password reset flow will send a confirmation email, and clicking on it will take you to a form where you can update and change your password.

## Other User Settings

* **Weekly Summary Email** - Users can opt in or out of a weekly summary email that provides high-level statistics on incidents for the previous week. Each user's summaries will only include incidents they can access, which depends on their [Private Incident Access](https://docs.firehydrant.com/docs/private-incident-access). Users added to private incident(s) ad-hoc will see said incident(s) in the weekly summary.