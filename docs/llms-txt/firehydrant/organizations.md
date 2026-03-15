# Source: https://docs.firehydrant.com/docs/organizations.md

# Organizations

> 📘 Note:
>
> Multiple organizations are available for customers on our [Enterprise pricing plan](https://firehydrant.com/pricing/). Reach out to our sales team if you'd like more information.

Many businesses have unique incident management practices and security concerns for different teams. Teams requiring this separation can now use separate "organizations" in FireHydrant to manage multiple FireHydrant instances while still using the same Slack workspace.

In FireHydrant, the hierarchy is as follows:

<Image alt="Accounts consist of Organizations" align="center" width="400px" src="https://files.readme.io/cbf6aaa-image.png">
  Accounts consist of Organizations
</Image>

## Setting up multiple organizations

To set up multiple organizations, please [contact our support team](https://support.firehydrant.com/hc/en-us/requests/new). Currently, this capability is not self-service in the portal. Changes should reflect immediately for any user(s) included in the new organizations created.

When creating new organizations, the new org will be empty (e.g., no Runbooks, Teams/Users, Integrations configured, etc.).

Revisit our [Admin Quickstart](https://docs.firehydrant.com/docs/admin-quickstart), [Integrations Overview](https://docs.firehydrant.com/docs/integrations-overview), [Introduction to Runbooks](https://docs.firehydrant.com/docs/introduction-to-runbooks), and other documentation for setting things up in the new Organization you create.

> 📘 Note:
>
> If your Account has multiple organizations, remember to instruct all of your users to run `/fh switch org` to ensure they are set to declare incidents in the correct organization. All users will be able to declare in any organization belonging to their general Account.

### Switching organizations in Slack

<Image alt="Switch organizations in Slack with `/fh switch org`" align="center" width="400px" src="https://files.readme.io/d1ad0a1-multi-org-slack-switching.png">
  Switch organizations in Slack with `/fh switch org`
</Image>

Slack users linked to multiple FireHydrant organizations can run FireHydrant commands against either organization. To reduce continually having to select an organization, users can switch between organizations using the `/fh switch org` command.

<Image alt="Users will see a success message after switching orgs in Slack" align="center" width="650px" src="https://files.readme.io/57c7837-multi-org-slack-notice.png">
  Users will see a success message after switching orgs in Slack
</Image>

Since any user within a Slack workspace can open an incident regardless of their license, when any user runs `/fh new` they will be prompted to select an organization before opening the new incident.

### Switching organizations in the UI

Once you have multiple organizations configured, any users who are part of multiple organizations will see a change in the web interface - a new dropdown on the upper left to denote which organization they are in.

<Image alt="Organization switcher in the UI" align="center" width="400px" src="https://files.readme.io/16638a4-image.png">
  Organization switcher in the UI
</Image>

For a user to switch, they should click the dropdown and select the organization they'd like to switch to.

Additionally, you can easily share links to incidents and other pages in the web app with users who are part of multiple organizations because the URL will correctly switch the user into the organization where the content lives.

If a user does not have access to a particular organization and they attempt to click on a link, they will receive a 404 error.

## Managing organization settings in FireHydrant

<Image alt="Modifying specific org settings" align="center" width="650px" src="https://files.readme.io/86a1fc6-image.png">
  Modifying specific org settings
</Image>

In the FireHydrant web application, users can manage their organization settings under their User Profile. To access the User Profile page, click the user avatar in the upper right corner and click "Profile." Organization settings for each organization are separate, so the user will need to switch and navigate to the same page to change org-specific settings.

### API Keys and Organizations

API keys have always been scoped to an organizational level. With multiple organizations, API keys for one org will not take action on, or provide access to, another organization.

### SSO and SCIM Provisioning

To get users into the proper organization in FireHydrant, you must create distinct SSO applications for each organization in your IDP (Okta, Google, etc.). You can use automatic or just-in-time provisioning for your users when configuring multiple organizations.

You can visit our docs for [SSO with SAML](https://docs.firehydrant.com/docs/sso-with-saml) and [SSO with SCIM](https://docs.firehydrant.com/docs/sso-with-scim) to learn more about administrating users in FireHydrant.