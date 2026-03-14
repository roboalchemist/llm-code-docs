# Source: https://docs.airbyte.com/platform/access-management/sso.md

# Source: https://docs.airbyte.com/platform/2.0/access-management/sso.md

# Source: https://docs.airbyte.com/platform/1.8/access-management/sso.md

# Source: https://docs.airbyte.com/platform/1.7/access-management/sso.md

# Source: https://docs.airbyte.com/platform/1.6/access-management/sso.md

# Single Sign-On (SSO)

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

<!-- -->

Single Sign-On (SSO) allows you to enable logging into Airbyte using your existing Identity Provider (IdP) like Okta or Active Directory.

SSO is available in Airbyte Enterprise and on Cloud with the Teams add-on. [Talk to us](https://airbyte.com/company/talk-to-sales) if you are interested in setting up SSO for your organization.

## Set up[​](#set-up "Direct link to Set up")

You can find setup explanations for all our supported Identity Providers on the following subpages:

<!-- -->

## [📄️<!-- --> <!-- -->Microsoft Entra ID](/platform/1.6/access-management/sso-providers/azure-entra-id.md)

[This page guides you through setting up Single Sign-On with Airbyte using Microsoft Entra ID (formerly known as Azure ActiveDirectory).](/platform/1.6/access-management/sso-providers/azure-entra-id.md)

## [📄️<!-- --> <!-- -->Okta](/platform/1.6/access-management/sso-providers/okta.md)

[This page guides you through setting up Okta for Single Sign-On with Airbyte.](/platform/1.6/access-management/sso-providers/okta.md)

## Logging in[​](#logging-in "Direct link to Logging in")

* Cloud
* Self-Managed

Once we inform you that you’re all set up, you can log into Airbyte using SSO by visiting [cloud.airbyte.com/sso](https://cloud.airbyte.com/sso) or select the **Continue with SSO** option on the login screen.

Specify your *company identifier* and hit “Continue with SSO”. You’ll be forwarded to your IdP's login page (e.g. Okta login page). Log into your work account and you’ll be forwarded back to Airbyte Cloud and be logged in.

*Note:* you were already logged into your company’s Okta account you might not see any login screen and directly get forwarded back to Airbyte Cloud.

Accessing your self hosted Airbyte will automatically forward you to your IdP's login page (e.g. Okta login page). Log into your work account and you’ll be forwarded back to your Airbyte and be logged in.
