# Source: https://planetscale.com/docs/security/authentication-methods.md

# Authentication methods

> There are three ways to authenticate with PlanetScale: _email address and password_, _single sign-on_, and _OAuth via GitHub_.

## Overview

Let's break down how each of these work.

## Email address and password

This is the only authentication mechanism where PlanetScale maintains user credentials.

Additionally, users can opt to configure [two-factor authentication (2FA)](/docs/security/multi-factor-authentication). This option requires **something you know** *(i.e. your password)* and **something you have** *(i.e. recovery codes)*.

## Single sign-on

Users can authenticate with their chosen corporate identity provider *(i.e. Okta)* instead of maintaining passwords with PlanetScale.

Once [SSO](/docs/security/sso) is enabled for an `organization`, all members are redirected through that identity provider's authentication flow. Moving forward, they must pass through SSO to access their PlanetScale account.

## OAuth via GitHub

Users can authenticate with PlanetScale using their GitHub account.

<Warning>
  PlanetScale doesn't maintain the passwords for these accounts. Losing access to your GitHub account prevents accessing
  your PlanetScale account.
</Warning>

<Note>
  Enabling SSO removes OAuth access for all members of your *organization*, meaning they will no longer be able
  to sign in with their GitHub credentials.
</Note>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt