# Source: https://docs.gitguardian.com/platform/enterprise-administration/saml-sso-configuration.md

# Configure SAML SSO

> Configure SAML-based Single Sign-On for your GitGuardian workspace, including identity provider setup and advanced options.

Single Sign-On (or SSO) allows you to manage your organization's entire membership via a third-party provider.

GitGuardian supports the SAML2 standard for SSO which allows the Owner or any Manager of the workspace to configure any SAML2-enabled Identity Provider (IdP) system.

## Set up SSO

To configure your SSO, navigate to Settings > [Authentication](https://dashboard.gitguardian.com/settings/workspace/auth).

Detailed set up procedures are available for the following IdP:

- [Google](./sso-providers/google)
- [Okta](./sso-providers/okta)
- [Auth0](./sso-providers/auth0)
- [Microsoft Entra ID](./sso-providers/entra-id)
- [Duo](./sso-providers/duo)
- [Keycloak](./sso-providers/keycloak)

For all other SAML2-enabled IdP, you can follow the [generic procedure](./sso-providers/generic).

## Just-In-Time (JIT) provisioning

GitGuardian supports Just-In-Time (JIT) provisioning. **New members of your workspace are automatically registered with GitGuardian on their first login attempt with SAML2 SSO** if they are authorized on the IdP side.

You don't need to invite users manually. You just need to authorize them **on the IdP's side** by being part of the "GitGuardian group". Users who are not part of the GitGuardian group on the IdP side will be rejected during their attempt to sign in via SSO.

:::info
GitGuardian does not support JIT deprovisioning yet but you can use [SCIM](./scim-configuration) to automatically deprovision your users.
:::

## Default access level

Because GitGuardian uses Just-In-Time (JIT) provisioning, new members will be given **a default access level upon their first login**.

"Member" is the default setting. You can modify this default in your [Authentication settings page](https://dashboard.gitguardian.com/settings/workspace/auth/saml).

![SSO default access level](/img/platform/enterprise-administration/sso_default_access_level.png)

If you selected "Member" as the default access level and your workspace is under the Business plan, you must also configure whether new Members will be part of the ["All-incidents" team](../collaboration-and-sharing/teams#a-specific-team-the-all-incidents-team) or not upon sign up.

![SSO All-incidents team default membership setting](/img/platform/collaboration-and-sharing/sso-all-incidents-team-default-membership-setting.png)

## Force SSO

Once you have successfully set up an SAML2 SSO integration, in your [Authentication settings page](https://dashboard.gitguardian.com/settings/workspace/auth/saml), you have the option to **force the SSO**:

- If the option is turned ON, **all the members of your workspace will have to go through your IdP in order to be able to access your GitGuardian workspace**. Only the users you have authorized on your IdP's side will be able to sign into your GitGuardian workspace.
- If the option is turned OFF, members of your workspace can still login via SSO, going through your IdP, but they can also sign up via email.

![SSO force sso](/img/platform/enterprise-administration/sso_force_sso.png)

:::warning
Once SSO is forced, all the members of the workspace, including the owner, will have to connect using SSO. If the owner has never connected with SSO, you will not be able to activate the option.

Make sure that your SSO connection works before enforcing SSO. In case of issues, you can contact the [support team](mailto:support@gitguardian.com) for assistance.
:::

## SCIM-related settings

If you have [SCIM](./scim-configuration) enabled, additional settings appear in the Authentication settings page:

- **Default team membership permission**: Controls the incident permission level given to members synchronized via SCIM (Can view or Can edit).
- **Enable notifications for SCIM operations**: Sends notifications when SCIM updates affect users or teams.

Learn more in the [SCIM settings section](./scim-configuration#scim-settings).

## Email domain reservation

:::tip Essential Step: Reserve Your Email Domain
After configuring SSO, you must **reserve your email domain** to enable the full SSO experience. This critical step:
- **Enables automatic SSO discovery** - Users can log in from the main login page by entering their email; GitGuardian automatically redirects them to your SSO provider
- **Prevents workspace fragmentation** - Users cannot create separate workspaces with their company email, ensuring everyone joins the same workspace
- **Simplifies user experience** - Without domain reservation, users must bookmark and use the dedicated SSO login URL

**To reserve your domain:**
1. Navigate to Settings > [Email Domain Management](https://dashboard.gitguardian.com/settings/workspace/domains)
2. Follow the instructions to reserve your organization's email domain

Learn more about [email domain management](./email-domain-management).
:::

## FAQ

**How to verify that my SSO connection is working?**

If you have not reserved [an email domain](./email-domain-management#how-to-reserve-an-email-domain), please remember your SSO login URL.
1. Make sure to know your login credentials, i.e., your `email` and `password`.
2. Log out of the application.
3. Go to the SSO login URL, and log in by selecting the SSO option.
   For additional security purpose, GitGuardian will ask you to submit your email and password to confirm your identity.

**My Identity Provider (IdP) does not support "emailAddress" as the Name ID format. What do I do?**

If your IdP does not support `emailAddress` as the Name ID format, please [contact us](mailto:support@gitguardian.com). We will allow you to use `unspecified` as the Name ID format.

:::caution
When using `unspecified` as the Name ID format, you must ensure that you send the email addresses of your IdP users as an `email_address` attribute. This is mandatory, as email is the unique identifier that GitGuardian uses for its users.
:::

![SSO NameId unspecified and email_address attribute](/img/platform/enterprise-administration/sso_nameid_unspecified_and_email_address_attribute.png)

**I want to configure MFA for GitGuardian. What do I do?**

Combining SSO with MFA is more secure than using a simple SSO connection.

Leverage the MFA feature provided by all the SSO providers we support. We strongly advise that you enable the [Force SSO setting](#force-sso) to ensure that through SSO authentication, MFA is applied to all users authenticating to GitGuardian.
