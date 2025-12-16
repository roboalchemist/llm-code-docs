# Source: https://www.metabase.com/docs/latest/people-and-groups/authenticating-with-saml

<div>

1.  [Home](/docs/latest/)
2.  [People and Groups](/docs/latest/people-and-groups/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# SAML-based authentication

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

SAML authentication is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

Integrating your SSO with Metabase allows you to:

-   Provision a Metabase account when someone logs in to Metabase.
-   Automatically pass user attributes from your SSO to Metabase to power [row and column security](../permissions/row-and-column-security).
-   Let people access Metabase without re-authenticating.

## Confirm the password for your Metabase admin account

Before setting up SAML, make sure you know the password for your Metabase admin account. If you encounter any issues during the setup process, you can login via the "Admin backup login" option on the sign-in screen.

## Setting up SAML with your IdP in Metabase

Once you've [confirmed the password to your Metabase admin account](#confirm-the-password-for-your-metabase-admin-account), head over to the **Settings** section of the Admin Panel, then click on the **Authentication** tab. Click the **Set up** button in the SAML section of the Authentication page, and you'll see this form:

![SAML form](images/saml-form.png)

The form includes three sections:

1.  [Metabase info that you'll have to input into your identity provider (IdP)](#generic-saml-configuration).
2.  [IdP info that you'll need to tell Metabase about](#enabling-saml-authentication-in-metabase).
3.  [Signing SSO requests (optional)](#settings-for-signing-sso-requests-optional).

## SAML guides

First you'll need to make sure things are configured correctly with your IdP. Each IdP handles SAML setup differently.

We've written up some guides for the most common providers:

-   [Auth0](saml-auth0)
-   [Microsoft Entra ID](saml-azure)
-   [Google](saml-google)
-   [Keycloak](saml-keycloak)
-   [Okta](saml-okta)

If you don't see your IdP listed here:

-   Refer to your IdP's reference docs on configuring SAML. You'll be looking for something like this [OneLogin SAML guide](https://onelogin.service-now.com/support?id=kb_article&sys_id=83f71bc3db1e9f0024c780c74b961970).
-   Using the information found on the Metabase SAML form, fill out your IdP's SAML form.
-   For more information, see the next section on [Generic SAML configuration](#generic-saml-configuration).

## User provisioning

By default, Metabase will create accounts for people who don't yet have a Metabase account but who are able to log in via SAML SSO.

If you've set up [User provisioning with SCIM](./user-provisioning), you'll want to turn this setting off so that Metabase doesn't automatically create a new account for anyone who authenticates successfully, as you may want to use SCIM to determine who can and can't create an account in Metabase.

## Generic SAML configuration

The top portion of the SAML form in Metabase has the information you'll need to fill out your IdP's SAML form, with buttons to make copying the information easy.

The names of the fields in the Metabase SAML form won't always match the names used by your IdP. We've provided a description of each field below to help you map information from one place to another.

### URL the IdP should redirect back to

The redirect URL is the web address that people will be sent to after signing in with your IdP. To redirect people to your Metabase, your redirect URL should be your Metabase [Site URL](../configuring-metabase/settings#site-url), with `/auth/sso` at the end.

For example, if your Metabase Site URL is `https://metabase.yourcompany.com`, you'll use

``` highlight
https://metabase.yourcompany.com/auth/sso
```

as the redirect URL in your IdP's SAML form.

Different IdPs use different names for the redirect URL. Here are some common examples:

  Provider              Name
  --------------------- --------------------------
  [Auth0](saml-auth0)   Application Callback URL
  [Okta](saml-okta)     Single Sign On URL
  OneLogin              ACS (Consumer) URL

### User attributes

Metabase will automatically log in people who've been authenticated by your SAML identity provider. To do so, the first assertion returned in the identity provider's SAML response *must* contain attributes for each person's first name, last name, and email.

Most IdPs already include these assertions by default, but some (such as [Okta](./saml-okta)) must be configured to include them.

Generally you'll need to paste these user attributes (first name, last name, and email) into fields labelled "Name", "Attributes" or "Parameters".

> If you allow people to edit their email addresses: make sure to update the corresponding account emails in Metabase. Keeping email addresses in sync will protect people from losing access to their accounts.

### Settings for signing SSO requests (optional)

These are additional settings you can fill in to sign SSO requests to ensure they don't get tampered with.

## Enabling SAML authentication in Metabase

Metabase will now need to know some things about your IdP. Here's a breakdown of each of the settings:

### SAML identity provider URL

Metabase will redirect login requests to the Identity Provider URL, where people will go to log in with SSO.

Different IdPs use different names for the Identity Provider URL. Here are some common examples:

  Provider              Name
  --------------------- --------------------------------------
  [Auth0](saml-auth0)   Identity Provider Login URL
  [Okta](saml-okta)     Identity Provider Single-Sign On URL
  OneLogin              SAML 2.0 Endpoint (HTTP)

### SAML identity provider issuer

The SAML identity provider issuer is a unique identifier for the IdP. You might also see "Issuer" referred to as "Entity ID". Assertions from the IdP will contain this information, and Metabase will verify that the issuer matches the value you set.

We recommend that you set this value to make your SAML configuration more secure.

  Provider              Name
  --------------------- -----------------------------
  [Auth0](saml-auth0)   Identity Provider Login URL
  [Okta](saml-okta)     Identity Provider Issuer
  OneLogin              Issuer URL

### SAML identity provider certificate

The SAML identity provider certificate is an encoded certificate that Metabase will use when connecting to the IdP URI. The certificate will look like a big blob of text that you'll want to copy and paste carefully --- the spacing is important!

Your IdP might have you download this certificate as a file (usually `.cer` or `.pem`), which you'll then need to open up in a text editor to copy the contents to then paste into the box in Metabase.

Note that your certificate text may include header and footer comments that look like `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`. These comments should be included when pasting your certificate text into Metabase.

  Provider              Name
  --------------------- ---------------------
  [Auth0](saml-auth0)   Signing Certificate
  [Okta](saml-okta)     X.509 Certificate
  OneLogin              X.509 Certificate

### Settings for signing SSO requests (optional)

To sign request so that they can't be tampered with, you'll need to provide additional settings.

If your IdP encrypts SAML responses, you'll need to ensure this section is filled out.

> If you change any of these settings, either during initial setup or after editing an existing value, you will need to restart Metabase due to the way the keystore file is read.

-   **SAML keystore path:** the absolute path to the keystore file to use for signing SAML requests.
-   **SAML keystore password:** the magic spell that will open the keystore.
-   **SAML keystore alias:** the alias for the key that Metabase should use for signing SAML requests.

## SAML Single logout (SLO)

Metabase supports single logout (SLO) for SAML.

The endpoint for SLO: `/auth/sso/handle_slo`

So if your Metabase is served at `metabase.example.com` the logout service POST binding URL would be:

``` highlight
https://metabase.example.com/auth/sso/handle_slo
```

### Enable SAML SLO

SLO isn't configurable from the Metabase interface. To enable it, you'll need to set the following options using environment variables or your Metabase configuration file:

-   [`MB_SAML_SLO_ENABLED`](../configuring-metabase/environment-variables#mb_saml_slo_enabled) to `true`;
-   [`MB_SAML_IDENTITY_PROVIDER_URI`](../configuring-metabase/environment-variables#mb_saml_identity_provider_uri) to your IdP's SLO endpoint;
-   [`MB_SESSION_COOKIE_SAMESITE`](../configuring-metabase/environment-variables#mb_session_cookie_samesite) to `none`.

For the `MB_SESSION_COOKIE_SAMESITE` setting to work with `none`, Metabase must be served over HTTPS. Browsers like Chrome will block cookies in cross-site requests if SSL is not enabled. Without HTTPS, logout requests from your IdP (such as Okta) won't include the session cookie, which means Metabase won't be able to end the session properly.

## Synchronizing group membership with your IdP

This setting allows you to assign users to Metabase groups based on an attribute of your users in your IdP. This setting may not correlate to group functionality provided by your IdP; you may need to create a separate user attribute to set people's Metabase groups, like `metabaseGroups`.

First, you will need to create a SAML user attribute that you will use to indicate which Metabase groups the person should be a part of. This created user attribute can be a XML string or a list of XML strings. Different IdPs have different ways of handling this, but you will likely need to edit your user profiles or find a way to map a user's groups to a list of Metabase group names.

## Configuring the group schema in Metabase

Once you've gotten everything set up in your SAML provider, you'll need to configure the group schema in Metabase.

1.  Turn on the **Synchronize group memberships** setting.
2.  Click **Edit mappings**.
3.  Click **Create a mapping**.
4.  Enter in the name of one of the groups you entered as your `metabaseGroups` attribute values, then click the **Add** button.
5.  Click the dropdown that appears under the `Groups` heading to select the Metabase group(s) that users with this particular `metabaseGroups` value should be added to.
6.  Click **Save**.
7.  After that, type in the name of the user attribute you added in your SAML provider. In this case, we told Okta that the `metabaseGroups` attribute should be named `MetabaseGroupName`, so that's what we'll enter in the Group Attribute Name field in Metabase.

![Group schema](images/saml-okta-groups.png)

## Creating Metabase accounts with SSO

> Paid plans [charge for each additional account](../cloud/how-billing-works#what-counts-as-a-user-account).

A new SSO login will automatically create a new Metabase account.

Metabase accounts created with an external identity provider login don't have passwords. People who sign up for Metabase using an IdP must continue to use the IdP to log into Metabase.

## Disabling password logins

> **Avoid locking yourself out of your Metabase!** Turning off password logins applies to all Metabase accounts, *including your Metabase admin account*. Before turning off password logins, make sure you can log in to your admin account using SSO.

To *require* people to log in with SSO, disable password authentication from **Admin settings** \> **Authentication**. Turn off the **Enable Password Authentication** toggle.

![Password disable](images/password-disable.png)

## New account notification emails

When people log in to Metabase for the first time via SSO, Metabase will automatically create an account for them, which will trigger an email notification to Metabase administrators. If you don't want these notifications to be sent, go to **Admin settings \> Authentication \> User provisioning**, and toggle off **"Notify admins of new users provisioned from SSO"**

## Example code using SAML

You can find example code that uses SAML authentication in the [SSO examples repository](https://github.com/metabase/sso-examples).

## Troubleshooting SAML issues

-   [Troubleshooting SAML](../troubleshooting-guide/saml).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/people-and-groups/authenticating-with-saml.md) ]