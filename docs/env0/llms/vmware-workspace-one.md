# Source: https://docs.envzero.com/guides/sso-integrations/vmware-workspace-one.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# VMware Workspace ONE Integration

> Set up VMware Workspace ONE as a SAML identity provider for env zero authentication

## Introduction

This guide will detail the various steps required to integrate VMware workspace one as a SAML provider for your env zero organization. The current implementation is used for authentication only, where you define your users in your workspace one account to enable them access to your env zero organization.

<Note>
  **Self-Service Configuration Available**: You can configure SAML SSO directly from your organization settings. See [Self-Service SSO Integration](/guides/sso-integrations/self-service-sso) for an overview, or [Self-Service SAML Setup](/guides/sso-integrations/self-service-saml) for step-by-step instructions.
</Note>

## Steps

1. Login to your workspace one account and go to the Home tab.
2. Under `Services` you should see `Workspace ONE Access`, click on the `Manage` button.

<img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/9417800-vmware_manage.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=b52963b451d711422817cb2990c83b87" alt="" width="758" height="414" data-path="images/guides/sso-integrations/9417800-vmware_manage.png" />

1. In the `Workspace One Access` go to the `Catalog` tab.
2. Click on the `New` button.
3. Enter under the `name` textbox - env zero
4. Add a description, icon, and select the category of the app, and click on the `Next` button.
5. In the `Authentication Type` choose `SAML 2.0`
6. In the `Configuration` choose manual.
7. In the `Single Sign-on URL` and `Recipient URL` enter the following: `https://login.app.env0.com/login/callback?connection={YOUR_ENV0_ORG_ID}`
8. In the `Application ID` enter the following: `urn:auth0:env0:{YOUR_ENV0_ORG_ID}`
9. `Username Format` should be `Unspecified`
10. `Username Value` should be `${user.userName}`
11. Click on the `Advanced Properties` link.
12. In the `Request Signature` and the `Encryption Certificate` enter the data found in this file [here](https://drive.google.com/file/d/1jz1BgKR5pmWB9WFITpBIczPsytgKXRUt).
13. Under the `Custom Attribute Mapping` section add the following:

| Name      | Format | Value                              |
| :-------- | :----- | :--------------------------------- |
| email     | Basic  | \${user.email}                     |
| firstName | Basic  | \${user.firstName}                 |
| lastName  | Basic  | \${user.lastName}                  |
| name      | Basic  | ${user.firstName} ${user.lastName} |

<img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/ae921ff-vmware_attr.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=c7965dace5d8739dd36d833eb438a577" alt="" width="1600" height="563" data-path="images/guides/sso-integrations/ae921ff-vmware_attr.png" />

1. Click on the `Next` button.
2. Choose the relevant `Access Policy` and click on the `Next` button.
3. Make sure the summary is correct and click on \`Save and Assign”.
4. Assign the relevant users.
5. Go back to the `Catalog` tab.
6. Click on the `Settings` tab.
7. Click on the `SAML Metadeta`
8. Download the `Signing Certificate`
9. Close the `Settings` modal, and click on the `env zero` application you have just created.
10. Copy the `Launch URL` and send it to us.
11. Navigate to your env zero organization settings and go to the **SSO** tab.
12. Click on **SAML** and complete the self-service form with:
    * Identity Provider Single Sign-on URL (Launch URL)
    * X.509 Certificate

Built with [Mintlify](https://mintlify.com).
