# Source: https://www.aptible.com/docs/core-concepts/security-compliance/authentication/sso.md

# Single Sign-On (SSO)

<Frame> <img src="https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/SSO-app-ui.png?fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=69c735cebc73dc9cbaaf925a7e55b981" alt="" data-og-width="5120" width="5120" data-og-height="3060" height="3060" data-path="images/SSO-app-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/SSO-app-ui.png?w=280&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=2a8a1e409cdf0a381d134935cf3cc729 280w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/SSO-app-ui.png?w=560&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=ca0492bcdf096f0be99c486064f8207e 560w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/SSO-app-ui.png?w=840&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=3cfe944f6170be54a9a8b656d0ff4b4f 840w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/SSO-app-ui.png?w=1100&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=bbbd7d84fae265ee12b21877cefab86e 1100w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/SSO-app-ui.png?w=1650&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=6d5a0ce318580db3b2a044def41197dd 1650w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/SSO-app-ui.png?w=2500&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=82f358649697ac43978cc7200aabf926 2500w" /> </Frame>

# Overview

<Info> SSO/SAML is only available on [Production and Enterprise](https://www.aptible.com/pricing)[ plans.](https://www.aptible.com/pricing)</Info>

Aptible provides Single Sign On (SSO) to an [organization's](/core-concepts/security-compliance/access-permissions) resources through a separate, single authentication service, empowering customers to manage Aptible users from their primary SSO provider or Identity Provider (IdP).

Aptible supports the industry-standard SAML 2.0 protocol for using an external provider. Most SSO Providers support SAML, including Okta and Google's GSuite. SAML provides a secure method to transfer identity and authentication information between the SSO provider and Aptible.

Each organization may have only one SSO provider configured. Many SSO providers allow for federation with other SSO providers using SAML. For example, allowing Google GSuite to provide login to Okta. If you need to support multiple SSO providers, you can use federation to enable login from the other providers to the one configured with Aptible.

<Card title="How to setup Single Sign-On (SSO)" icon="book-open-reader" iconType="duotone" href="https://www.aptible.com/docs/sso-setup" />

## Organization Login ID

When you complete [Single Sign On Provider Setup](/how-to-guides/platform-guides/setup-sso), your [organization's](/core-concepts/security-compliance/access-permissions) users can use the SSO link on the [SSO login page](https://dashboard.aptible.com/sso/) to begin using the configured SSO provider. They must enter an ID unique to your organization to indicate which organization they want to access.

That ID defaults to a randomly assigned unique identifier. [Account owners](/core-concepts/security-compliance/access-permissions) may keep that identifier or set an easier-to-remember one on the SSO settings page. Your organization's primary email domain or company name makes a good choice. That identifier is to make login easier for users.

<Warning> Do not change your SSO provider configuration after changing the Login ID. The URLs entered in your SSO provider configuration should continue to use the long, unique identifier initially assigned to your organization. Changing the SSO provider configuration to use the short, human-memorable identifier will break the SSO integration until you restore the original URLs. </Warning>

You will have to distribute the ID to your users so they can enter it when needed. To simplify this, you can embed the ID directly in the URL. For example, `https://dashboard.aptible.com/sso/example_id`. Users can then bookmark or link to that URL to bypass the need to enter the ID manually. You can start the login process without knowing your organization's unique ID if your SSO provider has an application "dashboard" or listing.

## Require SSO for Access

When `Require SSO for Access` is enabled, Users can only access their [organization's](/core-concepts/security-compliance/access-permissions) resources by using your [configured SAML provider](/how-to-guides/platform-guides/setup-sso) to authenticate with Aptible. This setting aids in enforcing restrictions within the SSO provider, such as password rotation or using specific second factors.

Require SSO for Access will prevent users from doing the following:

* [Users](/core-concepts/security-compliance/access-permissions) cannot log in using the Aptible credentials and still access the organization's resources.
* [Users](/core-concepts/security-compliance/access-permissions) cannot use their SSH key to access the git remote.

Manage the Require SSO for Access setting in the Aptible Dashboard by selecting Settings > Single Sign-On.

<Warning> Before enforcing SSO, we recommend notifying all the users in your organization. SSO will be the only way to access your organization at that point. </Warning>

## CLI Token for SSO

To use the [Aptible CLI](/reference/aptible-cli/cli-commands/overview) with Require SSO for Access enabled, users must:

1. Generate an SSO token.
   1. In the Aptible Dashboard, select the user's profile on the top right and then "CLI Token for SSO," which will bring you to the [CLI Token SSO settings page.](https://dashboard.aptible.com/settings/cli-sso-token)
2. Provide the token to the CLI via the [`aptible login --sso $SSO_TOKEN`](/reference/aptible-cli/cli-commands/cli-login) command.

### Invalidating CLI Token for SSO

1. Tokens will be automatically invalidated once the selected duration elapses.
2. Generating a new token will not invalidate older tokens.
3. To invalidate the token generated during your current session, use the "Logout" button on the bottom left of any page.
4. To invalidate tokens generated during other sessions, except your current session, navigate to Settings > Security > "Log out all sessions"

## Exempt Users from SSO Requirement

Users exempted from the Require SSO for Access setting can log in using Aptible credentials and access the organization's resources. Users can be exempt from this setting in two ways:

* users with an Account Owner role are always exempt from this setting
* users added to the SSO Allow List

The SSO Allow List will only appear in the SSO settings once `Require SSO for Access` is enabled.

We recommend restricting the number of Users exempt from the `Require SSO for Access` settings, but there are some use cases where it is necessary; some examples include:

* to allow [users](/core-concepts/security-compliance/access-permissions) to use their SSH key to access the git remote
* to give contributors (e.g., consultants or contractors) access to your Aptible account without giving them an account in your SSO provider
* to grant "robot" accounts access to your Aptible account to be used in Continuous Integration/Continuous Deployment systems
