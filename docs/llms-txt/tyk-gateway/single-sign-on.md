# Source: https://tyk.io/docs/tyk-cloud/teams-users/single-sign-on.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Single Sign-On (SSO) in Tyk Cloud

> Learn how to set up and manage Single Sign-On (SSO) in Tyk Cloud Control Plane deployments.

## What is SSO?

Single Sign-On (SSO) is an authentication process that empowers users to access various services and applications using a single set of credentials. This streamlines the login experience by eliminating the need to remember multiple usernames and passwords for different platforms.

These credentials are securely stored with an Identity Provider(IdP). An Identity Provider (IdP) is a service that stores and manages digital identities. Companies can use these services to allow their employees or users to connect with the resources they need.

## Pre-requisites

<Note>
  To be able to configure Single Sign-On authentication, an SSO entitlement needs to be enabled in the subscription plan.
  If you are interested in getting access, contact your account manager or reach out to our [support@tyk.io](<mailto:support@tyk.io?subject=Tyk Cloud Single sign on>)
</Note>

## Add new SSO profile

To add a new SSO profile, login to Tyk Cloud, navigate to the *Profile* list and click on the *ADD PROFILE* button.

<img src="https://mintcdn.com/tyk/DsQbeJAEGJcPZUbZ/img/cloud/cloud-sso-profile-list.png?fit=max&auto=format&n=DsQbeJAEGJcPZUbZ&q=85&s=a8a6b1e08a543e301fea4475b7a24b45" alt="Tyk Cloud SSO profile list" width="2056" height="691" data-path="img/cloud/cloud-sso-profile-list.png" />

Populate the form with all the mandatory fields and click the *ADD PROFILE* button.

<img src="https://mintcdn.com/tyk/DsQbeJAEGJcPZUbZ/img/cloud/cloud-sso-add-profile-form.png?fit=max&auto=format&n=DsQbeJAEGJcPZUbZ&q=85&s=27f7058c8cddf38d2e8830ce74bf263b" alt="Tyk Cloud SSO add profile form" width="2056" height="796" data-path="img/cloud/cloud-sso-add-profile-form.png" />

The table below explains the fields that should be completed:

| Field name            | Explanation                                                                                                                                                                                                                                                              |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Provider name         | Used to distinguish between different SSO providers.                                                                                                                                                                                                                     |
| Client ID             | Used for client authentication with the IdP provider. The value can be found in your chosen IdP provider's configuration.                                                                                                                                                |
| Client Secret         | Used for client authentication with the IdP provider. The value can be found in your chosen IdP provider's configuration.                                                                                                                                                |
| Discovery URL         | Used to read your IdP's openid configuration. This URL can be found in your chosen IdP provider's configuration.                                                                                                                                                         |
| Default User Group ID | The ID of the user group that new users are allocated to by default upon registration.                                                                                                                                                                                   |
| Only registered users | A check-box that defines which users are allowed to use SSO. If checked, only users who are already registered in Tyk Cloud are allowed to login with SSO. If un-checked, new users will be added to Tyk Cloud in the *Default* user group upon successful registration. |

As illustrated below an authentication and callback URL will be generated, once the new profile has been added. You need to add these URLs to the configuration of your chosen IdP provider.
The Auth URL is your custom URL that can be used to start the SSO login flow whereas Callback URL is the URL that the SSO provider will callback to confirm successful authentication.

<img src="https://mintcdn.com/tyk/DsQbeJAEGJcPZUbZ/img/cloud/cloud-sso-add-config-details.png?fit=max&auto=format&n=DsQbeJAEGJcPZUbZ&q=85&s=f1d0d8ae132ce49f4de63d444cfe70bd" alt="Tyk Cloud SSO example of filled form" width="2133" height="1037" data-path="img/cloud/cloud-sso-add-config-details.png" />

## Edit SSO profile

To update/re-configure SSO profile, login to Tyk Cloud, navigate to *Profile* list and click on the profile that you would like to update.

<img src="https://mintcdn.com/tyk/DsQbeJAEGJcPZUbZ/img/cloud/cloud-sso-edit-select.png?fit=max&auto=format&n=DsQbeJAEGJcPZUbZ&q=85&s=7bea25f7ffd5bed2e64f41f4a15cdbe7" alt="Tyk Cloud SSO edit selection" width="2133" height="707" data-path="img/cloud/cloud-sso-edit-select.png" />

Edit the fields you would like to change and then click on the *SAVE PROFILE* button.

<img src="https://mintcdn.com/tyk/DsQbeJAEGJcPZUbZ/img/cloud/cloud-sso-save-edit.png?fit=max&auto=format&n=DsQbeJAEGJcPZUbZ&q=85&s=110d753f127d00a1063168fb6641ca08" alt="Tyk Cloud SSO save edit selection" width="2133" height="1023" data-path="img/cloud/cloud-sso-save-edit.png" />

## Delete SSO profile

<Warning>
  Please note the action of deleting an SSO profile cannot be undone.

  To delete an SSO profile, login to Tyk Cloud, navigate to *Profile* list and click on the profile you would like to remove.
</Warning>

<img src="https://mintcdn.com/tyk/DsQbeJAEGJcPZUbZ/img/cloud/cloud-sso-delete-select.png?fit=max&auto=format&n=DsQbeJAEGJcPZUbZ&q=85&s=a30b3246d82df1089339be5b02f42625" alt="Tyk Cloud SSO delete selection" width="2133" height="707" data-path="img/cloud/cloud-sso-delete-select.png" />

On the profile page, click on the *DELETE PROFILE* button.

<img src="https://mintcdn.com/tyk/DsQbeJAEGJcPZUbZ/img/cloud/cloud-sso-delete-click.png?fit=max&auto=format&n=DsQbeJAEGJcPZUbZ&q=85&s=8a3fe4e3716bea209d8ed2c9731ffd5f" alt="Tyk Cloud SSO delete accept" width="2133" height="974" data-path="img/cloud/cloud-sso-delete-click.png" />

On the confirmation window, confirm by clicking the *DELETE PROFILE* button.

<img src="https://mintcdn.com/tyk/DsQbeJAEGJcPZUbZ/img/cloud/cloud-sso-delete-confirm.png?fit=max&auto=format&n=DsQbeJAEGJcPZUbZ&q=85&s=0d68c946e901603687c3206064842716" alt="Tyk Cloud SSO delete confirm" width="2133" height="976" data-path="img/cloud/cloud-sso-delete-confirm.png" />

After profile deletion, the authentication URL will not be available anymore.

Built with [Mintlify](https://mintlify.com).
