# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/saml-settings.md

# SAML Settings

This document explains the functionality of the SAML feature as well as how to set up a SAML to log in to the platform without using email/password credentials.

## About SAML

The platform supports single sign-on (SSO) authentication, which enables administrative users to log in to applications quickly and securely in a single session, without the need to use additional passwords.

## How to Configure SAML

From the main menu, go to **Company > Company Settings > SAML Settings** and then click the **+ NEW** button to create a new SAML configuration.

The details of the SAML configuration edit page are provided in the table below.

### Configuration Details

<table><thead><tr><th width="150"></th><th></th></tr></thead><tbody><tr><td>SAML Name</td><td>Name of the SAML configuration</td></tr><tr><td>Allowed Domains</td><td>Domain names authorized for SSO use</td></tr></tbody></table>

### SAML Configuration For Platform

The information that has been provided by the identity provider must be defined to the platform.

<table><thead><tr><th width="150"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Upload Metadata</td><td>Metadata provided by the identity provider can be used to automatically complete required fields.</td></tr><tr><td>Issuer URL of the IdP</td><td>URL information that must be provided manually if not uploaded in the metadata file</td></tr><tr><td>IdP SSO URL</td><td>Authentication address that must be provided manually if not uploaded in the metadata file</td></tr><tr><td>Upload Certificate</td><td>Certificate to be used for authentication if not uploaded in the metadata file</td></tr><tr><td>IdP Certificate</td><td>If the certificate file for validation couldn’t be uploaded, the certificate can be written as text in this field.</td></tr></tbody></table>

### SAML Configuration For Your Identity Provider

The information that has been provided by the platform must be defined to the identity provider.

<table><thead><tr><th width="150"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Download Metadata</td><td>Metadata file containing all of the required information. The file can be used by the identity provider to get all required information automatically.</td></tr><tr><td>Idp Entity ID</td><td>If the identity provider doesn’t allow a metadata file to be uploaded, Idp Entity ID information can be defined from this field.</td></tr><tr><td>SSO Sign-in URL</td><td>If the authenticator service does not allow a metadata file to be uploaded, the SSO login page URL address information can be defined from this field.</td></tr><tr><td>Metadata URL</td><td>URL address of the metadata file containing all of the information required by the identity provider.</td></tr><tr><td>Bypass SSO Login URL</td><td>The URL address can be used to log in to the platform without SSO.</td></tr><tr><td>SAML Attributes Mapping</td><td>The attributes given in this field should be mapped on the identity provider and must be matched.</td></tr><tr><td>Default Role</td><td>Permission level of users who will log in to the system for the first time using SSO</td></tr><tr><td>Enable SAML SSO</td><td>The SAML setting can be inactivated if there is no more SSO use needed.</td></tr></tbody></table>

{% hint style="warning" %}
The privileges of the automatic account generated for admins who log in to the system using SSO can be defined in the Default Role field. The Custom Roles can be created to restrict the privileges, please see more [here](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles).
{% endhint %}

## SAML Integration Documents

The SAML integration documents for most used identity providers are listed below to assist admins to set up SAML between their identity provider and platform successfully.

* [How to Configure SAML on ADFS](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/saml-settings/how-to-configure-saml-on-adfs)
* [How to Configure SAML on Google Workspace](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/saml-settings/how-to-configure-saml-on-google-workspace)
* [How to Configure SAML on Azure AD](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/saml-settings/how-to-configure-saml-on-azure-ad)
* [How to Configure SAML on Okta](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/saml-settings/how-to-configure-saml-on-okta)

## FAQ

### Q: An admin can't login to platform over SAML and sees a "Your account not registered..." message.

A: The admin email address must be created in the platform under the Company > System Users page in order to log in to the platform over SAML authentication.

### Q: Does the platform still require MFA with SSO/SAML integration?

**A**: No, MFA is only required for email and password logins. With SSO/SAML, all authentication, including MFA, is managed by the SSO provider.
