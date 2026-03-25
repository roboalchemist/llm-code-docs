# Source: https://docs.fiddler.ai/reference/access-control/okta-integration-saml.md

# Okta SAML

Learn how to integrate Fiddler with Okta for seamless Single Sign-On (SSO) authentication using the Security Assertion Markup Language (SAML) protocol.

## Overview

This integration allows your users to access Fiddler using their existing Okta credentials. Users are automatically provisioned in Fiddler on their first successful login, eliminating the need for manual user invitations.

## Prerequisites

Before starting, ensure you have:

* **Okta Administrator Access**: Permissions to create and configure applications in your Okta organization
* **Fiddler AuthN Administrator Access**: "Org Owner" role in Fiddler's AuthN management console
* **Deployment Information**: Your Fiddler deployment base URL

{% hint style="info" %}
The URL to the AuthN management console is your Fiddler instance base URL prepended with `authn-`. For example, if your base URL is `https://acme.cloud.fiddler.ai` then you can access the AuthN management console at `https://authn-acme.cloud.fiddler.ai`.
{% endhint %}

## Configuring Okta and Fiddler for Integration

{% stepper %}
{% step %}
**Fiddler AuthN Console Sign-in**

Sign in using the AuthN Console Org Owner user account credentials provided by your Fiddler representative:

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-197be4feb904b044646cf83a995b97af87c12a11%2Fauthn-signin-page-2.png?alt=media" alt="Fiddler AuthN console sign in page"><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Select Your Organization**

Ensure your organization is selected in the dropdown. You may see the *fiddler* organization, but this is reserved for system use and should not be edited. Here we are using the *example1* organization:

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-aae7f33f668e66aebb76ee4a5c5bfd246dc59e15%2Fsso-authn-console-home-page.png?alt=media" alt="Fiddler AuthN console home page"><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Navigate to Identity Providers in Settings**

Select *Settings* tab from the top menu and then select *Identity Providers* from the left navigation menu:

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-7e1d7d27e98fab7400dbeb2882d2f61d3c416fb0%2Fauthn-settings-idp-list.png?alt=media" alt="Fiddler AuthN console add provider page"><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Add and Configure New SAML Provider**

1. Select the SAML option in the *Add provider* section which brings up the Sign in with SAML form.
2. Choose a name for the Okta SAML integration. Note that this name will be displayed on the SSO login button on the Fiddler sign-in page so choose a name your users will recognize.
3. Paste the following placeholder value into the Metadata Xml text area. This is necessary for AuthN to create the URLs needed when you create the Okta app integration. It will be replaced in a later step.

{% code title="Placeholder Metadata Xml value" %}

```
PD94bWwgdmVyc2lvbj0iMS4wIj8+DQo8bWQ6RW50aXR5RGVzY3JpcHRvciB4bWxuczptZD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOm1ldGFkYXRhIg0KICAgICAgICAgICAgICAgICAgICAgdmFsaWRVbnRpbD0iMjAyNS0wOC0zMFQxMzo0NToxM1oiDQogICAgICAgICAgICAgICAgICAgICBjYWNoZUR1cmF0aW9uPSJQVDYwNDgwMFMiDQogICAgICAgICAgICAgICAgICAgICBlbnRpdHlJRD0iaHR0cDovL2xvY2FsaG9zdDo4MDgwIj4NCiAgICA8bWQ6U1BTU09EZXNjcmlwdG9yIEF1dGhuUmVxdWVzdHNTaWduZWQ9ImZhbHNlIiBXYW50QXNzZXJ0aW9uc1NpZ25lZD0iZmFsc2UiIHByb3RvY29sU3VwcG9ydEVudW1lcmF0aW9uPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6cHJvdG9jb2wiPg0KICAgICAgICA8bWQ6TmFtZUlERm9ybWF0PnVybjpvYXNpczpuYW1lczp0YzpTQU1MOjEuMTpuYW1laWQtZm9ybWF0OnVuc3BlY2lmaWVkPC9tZDpOYW1lSURGb3JtYXQ+DQogICAgICAgIDxtZDpBc3NlcnRpb25Db25zdW1lclNlcnZpY2UgQmluZGluZz0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmJpbmRpbmdzOkhUVFAtUE9TVCINCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBMb2NhdGlvbj0iaHR0cDovL2xvY2FsaG9zdDo4MDgwL2NvbnN1bWUvZGF0YSINCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBpbmRleD0iMSIgLz4NCiAgICAgICAgDQogICAgPC9tZDpTUFNTT0Rlc2NyaXB0b3I+DQo8L21kOkVudGl0eURlc2NyaXB0b3I+
```

{% endcode %}

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-67bafd517ebdb8353256759cd6990619fbf7adef%2Fauthn-okta-saml-add-provider.png?alt=media" alt="Fiddler AuthN console new SAML configuration"><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Create the IdP**

Select the Create button. Once the page refreshes, there are four URLs displayed. These three URLs will be required in the Okta App Integration steps. The fourth URL is unused.

* ZITADEL Metadata
* ZITADEL ACS Login Form URL
* ZITADEL ACS Intent API

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-c67fd537e6f3cb8e5f3188837de184cee2bbe4db%2Fauthn-okta-saml-add-provider-urls.png?alt=media" alt="Fiddler AuthN console create IdP login and URLs required for SAML IdP configuration in Okta."><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Create New App Integration in Okta**

1. Open your Okta Admin console and navigate to the Applications page and select the *Create App Integration* button:

   <figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-45b6920a7759abb74c9870a45bf460b0ceff358d%2Fokta-admin-applications.png?alt=media" alt="Okta admin console Applications page"><figcaption></figcaption></figure>
2. In the sign-in method modal, select SAML 2.0 and select the *Next* button:

   <figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-b60f071fea0a9b96513fae7a28c7e39952e84230%2Fokta-admin-create-app-integration%20(1).png?alt=media" alt="Okta admin console select SAML 2.0 sign-in method"><figcaption></figcaption></figure>
3. Name your Fiddler instance per your company guidelines and select the *Next* button:

   <figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-4ebbd752c0d105cae8001bfab9dd4fe5683f7cac%2Fokta-admin-create-app-integration-2%20(1).png?alt=media" alt="Okta admin console enter your new app name"><figcaption></figcaption></figure>

{% endstep %}

{% step %}
**Configure the Okta App**

1. Enter the *ACS Login Form* URL from the AuthN console into the *Single sign-on URL* text box
   1. Ensure the *Use this for Recipient URL and Destination URL* checkbox is selected
2. Enter the *Metadata* URL from the AuthN console into the Audience URI (SP Entity ID) text box

   <figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-6cd0ae54bc0ea287f8a8cad847f2d0b2a380d560%2Fokta-admin-saml-app-config%20(1).png?alt=media" alt="Okta admin console configure SAML settings"><figcaption></figcaption></figure>
3. Expand the *Advanced Settings* section
4. In the *Other Requestable SSO URLs* section, select the *+ Add Another* button and enter the *ACS Intent API* URL copied from the AuthN console's [identity provider page](#create-the-idp), and enter 0 for the *Index*

   <figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-7eb7077d6073dcfcf55f164a4a6d418cd340cdab%2Fokta-admin-saml-app-config-2.png?alt=media" alt="Okta admin console configure SAML settings - requestable URL"><figcaption></figcaption></figure>
5. In the *Attribute Statements* section, add the required attributes setting *Name format* as Basic for all entries:

   <figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-b713539452cb6d0adca1a24a5aa32ebaa4de2bda%2Fokta-admin-saml-app-config-3.png?alt=media" alt="Okta admin console configure SAML settings - attribute statements"><figcaption></figcaption></figure>

   1. Name=firstName, Value=user.firstName
   2. Name=lastName, Value=user.lastName
   3. Name=email, Value=user.email
6. Select the *Next* button. No changes are required on this page
7. Select the *Finish* button to complete the creation of the application
8. Copy the *Metadata URL* value on the Sign On page from the SAML 2.0 section

   <figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-ab52533b7e5246d93bdac8d21950c30d20af7b87%2Fokta-admin-saml-app-settings.png?alt=media" alt="Okta admin console configure SAML settings - copy metadata URL"><figcaption></figcaption></figure>

{% endstep %}

{% step %}
**Replace the Placeholder Metadata XML**

1. Please return to the Fiddler AuthN console where we left it in Step 5
2. Delete the placeholder Metadata XML value and leave it blank
3. Paste the Metadata URL copied from Okta in the previous step into the *Metadata URL* text box

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-b9a813ccdb533b01f707189686b4ee68d8db839c%2Fauthn-okta-saml-metadata-url.png?alt=media" alt="Fiddler AuthN console clear Metadata Xml and paste in Metadata URL"><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Configure Additional Parameters**

1. Expand the *optional* section
2. Ensure the *Automatic create* and *Automatic update* checkboxes are selected
3. Set the *Determines whether an identity will be prompted to be linked to an existing account* dropdown to *Check for existing Username*

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-14ec75cbe433302ba6ce0ea73e30854ab3c3b249%2Fauthn-okta-saml-config.png?alt=media" alt="Fiddler AuthN console additional required settings"><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Save the Configuration Changes**

Select the *Save* button, and you will be returned to the Settings page for your Organization:

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-e03c0c7fec3ae0e44d4a9c62c051f563c5a5b492%2Fauthn-okta-saml-settings-new-idp.png?alt=media" alt="Fiddler AuthN console saving new SAML IdP"><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Activate the Okta SAML IdP**

1. Select your IdP from the list for which the Metadata XML field is populated. The contents were dynamically inserted from the Metadata URL.

   <figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-b5043f5fc51ee73f314e97fd98c064c8cc7be8e0%2Fauthn-okta-saml-new-metadata-xml.png?alt=media" alt="Fiddler AuthN console active new SAML IdP"><figcaption></figcaption></figure>
2. At the top of the page, select the *Activate* button to enable this IdP login.
3. Select *Login Behavior and Security* from the left nav menu and ensure the *External login allowed* checkbox is selected.

   <figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-f9f59db78b0f0e9c2a3d61d985f5e9d3907c509b%2Fauthn-okta-saml-allow-ext-login.png?alt=media" alt="Fiddler AuthN console additional SAML IdP configuration"><figcaption></figcaption></figure>

{% endstep %}

{% step %}
**Create a Custom Action**

Select the *Actions* tab from the top menu

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-05e6b8b53c24ac3b539d42538eaf4a20d16a0d67%2Fauthn-okta-saml-create-action-script.png?alt=media" alt="Fiddler AuthN console new custom Action script"><figcaption></figcaption></figure>

1. Select the *New* button in the *Scripts* section to create a new action script
2. Copy the *Okta SAML Action Script* below and paste it into the script text area
3. Enter `setAttributesOnOktaSAMLAuth` in the Name text box
4. Select the *Add* button

{% code title="Okta SAML Action Script" %}

```javascript
function setAttributesOnOktaSAMLAuth(ctx, api) {
    let firstName = ctx.v1.providerInfo.attributes["firstName"];
    let lastName = ctx.v1.providerInfo.attributes["lastName"];
    let email = ctx.v1.providerInfo.attributes["email"];
    let groups = ctx.v1.providerInfo.attributes["groups"];
    
    let nameParts = [firstName, lastName];
    let filteredParts = nameParts.filter(part => part);
	let displayName = filteredParts.join(' ');
  
    if (firstName != undefined) {
      api.setFirstName(firstName);
    }
    if (lastName != undefined) {
      api.setLastName(lastName);
    }
    if (email != undefined) {
      // Email is returned as an object in SAML response.
      // We typecast it to string before normalizing it.
      email = String(email).toLowerCase();
      api.setEmail(email);
      api.setEmailVerified(true);
      api.setPreferredUsername(email);
    }
    if (displayName != undefined) {
      api.setDisplayName(displayName);
    }
  
    api.v1.user.appendMetadata('fiddler_authentication_type', 'SSO:OKTA:SAML');
    if (groups === null || groups === undefined){
      groups = []
    }
    api.v1.user.appendMetadata('fiddler_groups', groups);
  }
```

{% endcode %}
{% endstep %}

{% step %}
**Configure the Action Trigger**

Scroll down to the *Flows* section

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-0285c474ac09d9710e591b68499acc30d455327d%2Fauthn-okta-saml-action-script-set-trigger.png?alt=media" alt="Fiddler AuthN console new Action trigger creation"><figcaption></figcaption></figure>

1. Select the *+ Add trigger* button
2. Select the *Post Authentication* option for the *Trigger Type* dropdown
3. Select the *setAttributesOnOktaSAMLAuth* option for the *Actions* dropdown
4. Select the *Save* button
   {% endstep %}

{% step %}
**Validate the Integration**

1. Enter your Fiddler URL. This is [https://example1.dev.fiddler.ai ](https://example1.dev.fiddler.ai/)in our example. Your Fiddler URL will vary according to your company name and the Fiddler deployment type.
2. Ensure you see the Fiddler Sign-on page and that the page displays the *SSO Login - Okta SAML* button:

   <figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-ae09f0851c1bd77701aa690935fe5edd39fb50c1%2Fauthn-okta-saml-enabled-signin-page.png?alt=media" alt="Fiddler application homepage displaying the new SSO login method in addition to the email sign-in form"><figcaption></figcaption></figure>
3. Select the button and confirm that the Fiddler application loads:

   <figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-bc0bfebe55dd1427cf42c22e338cf711df579627%2Fokta-saml-fiddler-home-page.png?alt=media" alt="Fiddler application landing page"><figcaption></figcaption></figure>

{% hint style="info" %}
The first user to sign in to the Fiddler application is automatically assigned the Fiddler Org Admin role: subsequent members are Org Members by default
{% endhint %}

{% hint style="info" %}
Ensure your Okta user account is assigned to the new Okta application created
{% endhint %}
{% endstep %}
{% endstepper %}

### Getting Help

For additional assistance:

* Review the Okta system logs for authentication attempts
* Verify network connectivity between Fiddler and Okta
* Contact your Fiddler representative with specific error messages

## Reference Documentation

For detailed configuration guidance, refer to the official documentation:

* [Okta SAML Configuration Guide](https://zitadel.com/docs/guides/integrate/identity-providers/okta-oidc) - Comprehensive setup instructions
* [General SSO Authentication Guide](https://docs.fiddler.ai/reference/access-control/sso-authentication-guide) - Overview of SSO concepts and troubleshooting
* [Mapping AD Groups to Fiddler Teams](https://docs.fiddler.ai/reference/access-control/mapping-ad-groups-to-fiddler-teams) - Group synchronization details

## Important Notes

* **Automatic User Provisioning**: Users are automatically created on first successful login—no manual invitations required
* **Data Storage**: Fiddler stores only the user's first name, last name, email address, and SAML token from Okta
* **API Access**: For programmatic API access, users must create access tokens from the "Credentials" tab in Fiddler's Settings page
* **Single Authentication Method**: Users can only authenticate via either SSO or email authentication, not both

## Next Steps

After successful integration:

1. **Train Users**: Provide guidance on accessing Fiddler through Okta SSO
2. **Configure Teams**: Set up Fiddler teams to match your organizational structure
3. **Test Group Sync**: Verify automatic group synchronization is working as expected
4. **Monitor Usage**: Review authentication logs and user access patterns
