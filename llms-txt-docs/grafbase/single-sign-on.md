# Source: https://grafbase.com/docs/platform/self-hosting/single-sign-on.md

# Single sign on with OpenID Connect

To authenticate with the Grafbase Enterprise Platform API used by the Dashboard and the CLI, you have two options: access tokens created from the dashboard, or log in with your Identity Provider (IdP) — also known as Single Sign On (SSO). In this page, we explore that last method.

The Enterprise Platform supports direct integration with OpenID Connect compliant IdPs. It acts as a client (the Dashboard and CLI) and a resource server (the API). Users log in using the Authorization Code Grant flow. Setting this up only requires properly configuring the Dashboard and API containers. For all the required details, read one of the following guides:

- [Setting up GitLab Single Sign-On with the Enterprise Platform](/guides/enterprise-platform-gitlab)
- [Setting up Okta Single Sign-On with the Enterprise Platform](/guides/enterprise-platform-okta)

If you are setting up the Enterprise Platform with another IdP, that information should allow you to get it working, but please get in touch so we can also create a guide for that IdP.

## JIT provisioning of organization memberships

You can map groups from your IdP (typically communicated through the `groups` claim) to organizations in Grafbase Enterprise Platform, and have users automatically added to these organizations when they first log in. See the detailed guides above for instructions on how to set that up.