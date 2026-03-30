# Source: https://help.cloudsmith.io/docs/single-sign-on.md

# Single Sign-On

<HTMLBlock>
  {`
  <div class="cs-headline">Cloudsmith offers support for Single Sign-On (SSO) at the organization level using Security Assertion Markup Language (SAML).  With SAML, organizations can use their existing SSO provider to manage and control access to their Cloudsmith organization account.</div>
  `}
</HTMLBlock>

<HTMLBlock>
  {`
  <div class="cs-spacer"></div>
  <div class="row">
    <div class="cs-box">
      <a href="https://help.cloudsmith.io/docs/single-sign-on-with-azure-ad" class="cs-button-sm cs-swatch-midnight-blue">Azure AD</a>
    </div> 
    <div class="cs-box">
      <a href="https://help.cloudsmith.io/docs/single-sign-on-with-google-g-suite" class="cs-button-sm cs-swatch-midnight-blue">Google</a>
    </div>
    <div class="cs-box">
      <a href="https://help.cloudsmith.io/docs/single-sign-on-with-jumpcloud" class="cs-button-sm cs-swatch-midnight-blue">JumpCloud</a>
    </div>
    <div class="cs-box">
      <a href="https://help.cloudsmith.io/docs/single-sign-on-with-okta" class="cs-button-sm cs-swatch-midnight-blue">Okta</a>
    </div>
    <div class="cs-box">
      <a href="https://help.cloudsmith.io/docs/single-sign-on-with-onelogin" class="cs-button-sm cs-swatch-midnight-blue">OneLogin</a>
    </div>
  </div>
  `}
</HTMLBlock>

## Getting Started

Before configuring SSO with SAML, you'll need:

* A SAML Identity Provider that you can connect with Cloudsmith.
* Manager access to the Cloudsmith organization.

## Supported Providers

Whilst Cloudsmith should work with any generic SAML IdP, we officially support and provide documentation for a number of the most common providers. Please see the below for guides for each officially supported provider:

* [Azure AD](https://help.cloudsmith.io/docs/single-sign-on-with-azure-ad)
* [Google](https://help.cloudsmith.io/docs/single-sign-on-with-google-g-suite)
* [JumpCloud](https://help.cloudsmith.io/docs/single-sign-on-with-jumpcloud)
* [Okta](https://help.cloudsmith.io/docs/single-sign-on-with-okta)
* [OneLogin](https://help.cloudsmith.io/docs/single-sign-on-with-onelogin)

Other providers may be supported if they can set up a generic SAML application. If you need help with an unlisted integration, you can still contact us!

## SAML Landing Page (Login)

Once configured, you'll be able to access the SAML login page of your organization at the following URL:\
[https://cloudsmith.io/orgs/\{ACCOUNT}/saml/login/](https://cloudsmith.io/orgs/\{ACCOUNT}/saml/login/)

Where *ACCOUNT* is your organization's slug/identifier (what you would normally see in the URL when accessing your organization within Cloudsmith). If you're not sure what this is, just ask us.

## Enable SAML

You can enable SAML in your Cloudsmith organization settings:

<Image title="Saml-setup.png" alt={1309} align="center" border={true} src="https://files.readme.io/f5f6a37-Saml-setup.png">
  SAML Authentication Setup
</Image>

You just need to provide your SAML Metadata XML.  You can provide the Metadata XML via a URL, or by copy/pasting the Metadata XML from a file directly inline in the form

You can then enable SAML and optionally choose if you wish to enforce SAML-only authentication.

If you choose to enforce SAML-only authentication all users that belong to this org will be *forced* to authenticate via SAML-only, in order to access Cloudsmith. They will not be able to use password-based authentication or other social auth providers. This is more secure, but use caution to prevent lockouts.

## SAML Group Sync

> 📘
>
> **NOTE** Please do not enable SAML Group Sync before creating your group mappings, as SAML Group Sync will remove any users from a team if there is no corresponding group mapping present.

SAML Group Sync is used to use map an attribute from your Identity Provider to a team in your Cloudsmith Organization. This allows you to add users automatically to the team.

### Creating a Group Mapping

You first need to create mappings that will define which attributes and values will map to the respective teams in your Cloudsmith Organization.

To configure a new mapping, click the "Create Group Sync Mapping" button under "SAML Group Sync":

<Image title="SAML-Group-Sync-Create.png" alt={1122} align="center" src="https://files.readme.io/d13efaf-SAML-Group-Sync-Create.png">
  Create Group Sync Mapping Button
</Image>

You are then presented with the "Create Mapping" form:

<Image title="create-mapping-form.png" alt={445} align="center" border={true} src="https://files.readme.io/3025e50-create-mapping-form.png">
  Create Mapping Form
</Image>

Here you can define the following:

| Field           | Description                                                                  |
| :-------------- | :--------------------------------------------------------------------------- |
| Attribute Key   | The Attribute name from your Identity Provider that you use to define groups |
| Attribute Value | The name of the group from your Identity Provider                            |
| Team            | The team in your Cloudsmith Organization that you want this group mapped to  |
| Role            | The role will be granted within the Team                                     |

Once you have configured your mappings and verified the values are correct, you can then enable the mapping functionality by clicking "Enable SAML Group Sync":

<Image title="SAML-Group-Sync-Enable.png" alt={1122} align="center" src="https://files.readme.io/0cbfea8-SAML-Group-Sync-Enable.png">
  Enable SAML Group Sync Button
</Image>