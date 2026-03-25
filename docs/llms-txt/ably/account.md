# Source: https://ably.com/docs/platform/account.md

# Account overview

Manage all aspects of your account, from Two-factor authentication ([2FA](https://ably.com/docs/platform/account/2fa.md)) and billing to user management and personal preferences.

Begin by [logging](https://ably.com/login) in to Ably through your browser. Once you're logged in, you have access to the Ably dashboard, where you can click on the Account navigation dropdown to access the account settings:

![Ably Account Settings](https://raw.githubusercontent.com/ably/docs/main/src/images/content/screenshots/dash/account.png)

### Settings

Manage your Ably account settings, including authentication, [billing](https://ably.com/docs/platform/pricing/billing.md), and account ownership:

* Use your account's unique identifier (Account ID) when contacting support.
* Account owners can require all users to set up two-factor authentication (2FA) for added security.
* Account owners and users with the billing role can update billing and package details. They are the only users who can modify these settings or transfer account ownership.
* Transfer ownership or cancel the account, contact [Ably support.](https://ably.com/support)

### Billing

Manage your [billing](https://ably.com/docs/platform/pricing/billing.md) and package settings to scale your services:

* Review your current package to assess if it fits your needs, whether free, pay-as-you-go, or committed use.
* Ensure your billing information is up to date, including company name, billing email (optional), address, international phone number, and timezone.
* View and manage invoices and payment methods once your account has been upgraded.

### Limits

Understand and manage your package [limits](https://ably.com/docs/platform/pricing/limits.md) by tracking usage across messages, data, connections, and channels:

* Limits are applied to prevent service disruption and vary by package.
* Limits can be time-based, quantity-based, or rate-based, and they may apply either per connection/channel or across the entire account.
* Notifications are provided when limits are nearing or exceeded, and detailed logs of warnings and exceeded limits are accessible in the account dashboard.

### Usage

Monitor your account's resource consumption with detailed usage statistics:

* The usage statistics table monitors app performance by tracking resource usage, such as messages, data transferred, connections, and channels.
* The statistics chart visualizes app usage data over time, allowing users to define specific time ranges, zoom in on different periods, and analyze metrics in detail.

### Users

Manage the [users](https://ably.com/docs/platform/account/users.md) associated with your account:

* The account owner role has full permissions to manage the account, including inviting and removing users, and assigning roles like developer, billing, or admin.
* Multiple roles can be assigned to a single user.
* Remove, or change user roles within an Ably account.

### My Settings

Control personal account settings:

* View and edit name, email, and password.
* Enable two-factor authentication (2FA) for added security.
* Connect and manage login providers (Google, GitHub).
* Customize Ably email preferences (product updates, news, educational emails)
* Set up notifications for account usage.

### My Access tokens

Create access tokens for the [Control API:](https://ably.com/docs/platform/account/control-api.md)

* Users can create new tokens by providing a descriptive name, assigning an account, selecting capabilities, and securely storing the token once generated.
* Users can revoke existing tokens through the settings section, but this action is irreversible and will immediately invalidate the token for API access.
* After a token is created, the full token cannot be viewed again, so it must be securely stored upon generation.

## Related Topics

* [User management](https://ably.com/docs/platform/account/users.md): Learn how to manage users, user roles, and the permissions associated with each role.
* [Organizations](https://ably.com/docs/platform/account/organizations.md): Manage Ably organizations, provision users, configure SSO with SCIM, and handle account roles.
* [Single sign-on (SSO)](https://ably.com/docs/platform/account/sso.md): Single sign-on enables users to authenticate with Ably using your own identity provider.
* [Two-factor authentication (2FA)](https://ably.com/docs/platform/account/2fa.md): Enable two-factor authentication for your Ably account.
* [Enterprise customization](https://ably.com/docs/platform/account/enterprise-customization.md): How Enterprise customers can create a custom endpoint and benefit from Active Traffic Management and other advanced Ably features.
* [Programmatic management using Control API](https://ably.com/docs/platform/account/control-api.md): The Control API is a REST API that enables you to manage your Ably account programmatically. This is the Control API user guide.

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
