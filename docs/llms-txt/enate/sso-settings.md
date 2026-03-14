# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/sso-settings.md

# SSO Settings

## Overview

You can configure your single sign-on settings in the System Settings section of Builder.

To configure Single-Sign On, you must:

1. [Add a service provider certificate](#adding-a-service-provider-certificate) - the service provider is the application providing service, i.e. Enate.
2. [Add identity provider settings](#adding-identity-provider-settings) - the identity provider is the system authenticating usernames and passwords, i.e. your third party systems such as Azure AD.&#x20;

{% hint style="info" %}
Note that in order to edit these settings, a user must have the 'Edit System Settings' access option enabled as part of their [user role](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/user-roles-and-feature-access). Users without this access option will be able to view the settings in read-only mode.
{% endhint %}

## Adding a service provider certificate

To add a service provider certificate, you can either generate a new one or upload an existing certificate.&#x20;

If you are generating a brand new certificate, fill in the following settings:

<table><thead><tr><th width="284">Setting</th><th>Note</th></tr></thead><tbody><tr><td>Subject</td><td>This is just for your reference. Mandatory.</td></tr><tr><td>Key Size</td><td>Value depends your security standards.</td></tr><tr><td>Hashing Algorithm</td><td>Value depends your security standards.</td></tr><tr><td>Validity Period in Years</td><td>How long would you like the certificate to be valid for. Enter the number of years. Maximum of 2 years.</td></tr></tbody></table>

## Adding identity provider settings

To create an identity provider, you can either enter the necessary settings manually or import the metadata exported from your third-party system to auto-fill the necessary settings.

<table><thead><tr><th width="231">Setting</th><th>Note</th></tr></thead><tbody><tr><td>Name</td><td>This is mainly for your reference. It also shows on the login page as a tooltip. Mandatory. E.g. Sign in with Office 365.</td></tr><tr><td>Description</td><td>This is just for your reference. Optional. E.g. Logs in Enate users using their Enate account.</td></tr><tr><td>Logo</td><td>This is the logo that will appear on the login page. File must be .pgn, .gif or .jpeg and 120 by 28 pixels. Mandatory.</td></tr><tr><td>Login Binding Type</td><td>Set this to match how it is set in your identity provider, or how your identity provider's documentation tells you to set it. This will be auto-filled in if you import a metadate file.</td></tr><tr><td>Logout Binding Type</td><td>Set this to match how it is set in your identity provider, or how your identity provider's documentation tells you to set it. This will be auto-filled in if you import a metadate file.</td></tr><tr><td>Allow Identity Provider Initiated Login/Allow Unsolicited AuthN Requests</td><td><p>This determines whether you acknowledge or ignore unsolicited AuthN requests. Unsolicited AuthN requests occur when a user starts the login procedure from the Identity Provider without first visiting Enate.<br></p><p>During a solicited request, the User visits the Enate login page, clicks the SSO provider logo and is redirected. Upon completion of the authentication, they are redirected back to Enate where the authentication completes. This was solicited by Enate.<br></p><p>During an unsolicited request, the user visits the Identity Provider, possibly an 'Application Directory', and clicks the Enate logo. They are redirected to Enate where authentication completes. Because this flow was initiated by the Identity Provider, it is considered unsolicited by Enate.</p></td></tr><tr><td>Identity Provider ID/Identity Provider Entity ID</td><td>Set this to match how it is set in your identity provider, or how your identity provider's documentation tells you to set it. This setting will be auto-filled if you have imported a metadate file.</td></tr><tr><td>Single Logout URL</td><td>Set this to match how it is set in your identity provider, or how your identity provider's documentation tells you to set it. This setting will be auto-filled if you have imported a metadate file.</td></tr><tr><td>Single Sign On URL</td><td>Set this to match how it is set in your identity provider, or how your identity provider's documentation tells you to set it. This setting will be auto-filled if you have imported a metadate file.</td></tr><tr><td>User Identifier Claim</td><td>Which claim (e.g. first name, last name, etc. that has been set up in your third party identity provider) you want to use to maps to your users' email addresses. Set this to match how it is set in your identity provider, or how your identity provider's documentation tells you to set it. This setting will be auto-filled if you have imported a metadate file. This is a free text field as well as a dropdown, so it can be customized, but it will likely just be email addresses.</td></tr><tr><td>Identity Provider Certificate</td><td>Add a copy of the certificate (Base-64 CER) provided by your third party identity provider. This setting will be auto-filled if you have imported a metadate file.</td></tr></tbody></table>
