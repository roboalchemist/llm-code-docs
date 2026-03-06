# Source: https://northflank.com/docs/v1/application/collaborate/manage-an-organisation.md

# Manage an organisation

Organisations on Northflank allow you to manage multiple teams. You can provision and manage users by syncing your user directory, add your own single sign-on (SSO) identity provider, and configure security for your organisation.

![Viewing an organisation's dashboard in the Northflank application](https://assets.northflank.com/documentation/v1/application/collaborate/manage-an-organisation/org-dashboard.png)

> [!note] 
> [Click here](https://cal.com/team/northflank/northflank-enterprise) to schedule a call about on-boarding your organisation to Northflank.

## Create an organisation

You can create an organisation in the Northflank application from your user dashboard's organisations page.

You can also [schedule a call](https://cal.com/team/northflank/northflank-enterprise) to discuss on-boarding your organisation to Northflank, and selecting the right plan for your needs.

![Creating an organisation in the Northflank application](https://assets.northflank.com/documentation/v1/application/collaborate/manage-an-organisation/create-organisation.png)

## Manage organisation security

### Restrict teams and members

In your organisation settings you can:

- prevent members of your organisation from joining teams on Northflank that do not belong to your organisation

- prevent users that are not members of your organisation from being added to organisation teams

- restrict organisation invites to email addresses at your linked domains (if you have [configured single sign-on](#configure-single-sign-on))

![Editing an organisation's settings in the Northflank application](https://assets.northflank.com/documentation/v1/application/collaborate/manage-an-organisation/org-settings.png)

### Multifactor Authentication

You can enable require MFA from your organisation's security page to enforce multifactor authentication for your organisation members. Organisation members will be prompted to [set up an authenticator application for their Northflank account](https://northflank.com/docs/v1/application/secure/single-sign-on-multi-factor-authentication#multi-factor-authentication) before they can access Northflank, and they will need to enter their one-time passcode on every log in attempt.

You can also set a maximum login session duration in hours, which will automatically log organisation members out and require them to re-authenticate after the time period.

### Clear member login sessions

You can clear member login sessions from your organisation's security page to immediately log out all user accounts from your organisation.

## Create organisation roles

You can [manage user roles on an organisational level](https://northflank.com/docs/v1/application/secure/use-role-based-access-control#create-organisation-roles) to ensure compliance with your security policies, restrict users to specific teams, and grant organisational permissions.

![Creating an organisational role in the Northflank application](https://assets.northflank.com/documentation/v1/application/collaborate/manage-an-organisation/org-role.png)

## Manage organisation billing

You can add your payment method and tax ID for an organisation to [manage billing for all teams](https://northflank.com/docs/v1/application/billing/pricing-on-northflank) in the organisation.

As well monitoring spend by project and resource type, you can also monitor spend by team.

Invoices for each team's usage can be downloaded from the team billing page.

![Viewing an organisation's billing page in the Northflank application](https://assets.northflank.com/documentation/v1/application/collaborate/manage-an-organisation/org-billing.png)

## Configure single sign-on (SSO)

You can link your existing authentication with Northflank to allow your users to sign in using SSO.

Northflank uses [WorkOS SSO](https://workos.com/single-sign-on) to integrate Northflank with your identity provider using SAML and OpenID Connect (OIDC).

To enable single sign-on, follow these steps:

- While viewing an organisation, navigate to Settings.

- Under Single Sign On, enter one or more domain names associated with your organisation, e.g. `example.com`. You should input all the domain names that are associated with the email addresses of organisation members.

- Optionally, you can Allow port security SSO with external domains. This does not affect organisation members signing into Northflank, but can allow users with external domains in your identity provider to access services, if enabled for that service.

- Then, you can Set-up SSO. This will redirect you to the single sign-on setup, provided via WorkOS. Follow the instructions on the pages provided. At the end of the setup, you will be prompted to test the connection. When this test succeeds, your identity provider will be linked to Northflank.

Users from your identity provider can now sign up and log in to Northflank. To avoid logging in via a non-SSO account, users should log in via the Log in with Organisation Single Sign On option on the login page, or navigate to [[https://app.northflank.com/sso-login](https://app.northflank.com/sso-login)](https://app.northflank.com/sso-login).

Some identity providers also support directly logging in via your organisation’s external dashboard.

By default, accounts are created via JIT (Just In Time) provisioning - accounts are not created automatically and will instead be created when a user signs in for the first time.

When a user logs in to Northflank for the first time via SSO, they will automatically be a member of the organisation. Additionally, these users cannot create teams or resources that do not belong to the organisation, and cannot leave the organisation without deactivating the account.

To reconfigure the settings provided during setup, click the Configure SSO button. To disable Single Sign-On, click Disable SSO.

### Converting an existing account

A team member with an account that was not created through SSO must continue to log in via username and password. However, an organisation admin can convert their existing account to a SSO account. On the Members page, select the user you wish to convert to SSO. In the top right, click the Convert to SSO button. The user can then log in to Northflank via SSO, and their account will no longer be able to be accessed via username and password.

> [!warning] 
> Converting an account to SSO is a destructive action and cannot be reversed. If a user is a member of any teams
outside of their organisation, they will not be able to be converted to an SSO account - they should leave or delete
any teams they are a part of that do not belong to the organisation.

### Configuring SSO Settings

After linking your identity provider you can also select how users can be invited to teams in your organisation:

- Select SSO only to disable manual invites. This will prevent users in the organisation from inviting users by email address. Users will only be able to sign up via your SSO.

- Enable require approval for any SSO sign-ups. When a user creates an account using SSO they will be added to a queue until their request is confirmed or rejected. This conflicts with automatically [provisioning users with directory sync](#sync-your-directory), and cannot/should not be enabled at the same time.

> [!note] Unlock SSO and directory sync
> Contact [[support@northflank.com](mailto:support@northflank.com)](mailto:support@northflank.com) or [schedule a meeting](https://cal.com/team/northflank/northflank-enterprise) to enable single sign-on and directory sync for your organisation.

## Sync your directory

You can sync your user directory with Northflank to update users on Northflank based on their directory groups.

You can enable Automatically provision organisation members to automatically provision organisation users on Northflank. You can restrict automatic provisioning to selected directory groups, so only users for teams using Northflank are automatically created.

Roles can be synced with directory groups to enable you to assign and remove roles from users by updating their directory groups.

Northflank uses [WorkOS Directory Sync](https://workos.com/directory-sync) to integrate Northflank with your directory. You must have enabled [single sign-on](#configure-single-sign-on) to use directory sync.

## Next steps

- [Link your Git account: Integrate your Git accounts with Northflank to start building and deploying your code.](/v1/application/getting-started/link-your-git-account)
- [Create a project: Create a project to contain your services, persistent data, secrets, and more.](/v1/application/getting-started/create-a-project)
- [Add a card: Add a credit or debit card to your user or team account, and select the card to charge.](/v1/application/billing/add-a-card)
- [Configure role-based access control: Grant granular permissions and manage users with roles for teams and organisations.](/v1/application/secure/use-role-based-access-control)
- [Grant API access: Create API roles to grant access to the Northflank API, with granular permissions.](/v1/application/secure/grant-api-access)
