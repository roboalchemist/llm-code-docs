# Source: https://docs.port.io/sso-rbac/sso-providers/oidc/onelogin.md

# Onelogin

Follow this step-by-step guide to configure the integration between Port and Onelogin.

info

In order to complete the process you will need to contact Port to deliver and receive information, as detailed in the guide below.

## Port-Onelogin integration benefits[â](#port-onelogin-integration-benefits "Direct link to Port-Onelogin integration benefits")

* Connect to the Port application via a Onelogin app;
* Your Onelogin roles will be automatically synced with Port, upon user sign-in;
* Set granular permissions on Port according to your Onelogin roles.

## How to configure the Onelogin app integration for Portâ[â](#how-to-configure-the-onelogin-app-integration-for-port "Direct link to How to configure the Onelogin app integration for Portâ")

### Step #1: Create a new Onelogin application[â](#step-1-create-a-new-onelogin-application "Direct link to Step #1: Create a new Onelogin application")

1. In the Admin Console, go to Applications -> Applications.
2. Click `Add App`.

![Onelogin new application wizard](/assets/images/OneloginCreateApp-ffe7fd0c76592db7825a51c71652abed.png)

3. In the search box type **OpenID Connect**, then select `OpenId Connect (OIDC)`:

![Onelogin new application OIDC](/assets/images/OneloginSelectOidcFromSearch-f604f0d692d9f1ee03d368844d481fd7.png)

4. Define the initial Port application settings:

   1. `Display Name`: Insert a name of your choice for the Port app, like `Port`.
   2. Add rectangular and square icons (optional):

   ![Port\&#39;s logo](data:image/png;base64,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)

   ![Port\&#39;s icon](/assets/images/PortIcon-b535fa79c7fc8d10c3dbcc6107733c66.png)

![Onelogin initial new application](/assets/images/OneloginInitialApp-ffd3e27da73fa474254702c9e8019623.png)

Click `Save`.

tip

Most of the following steps involve editing the initial Port app you created. Keep in mind you can always go back to it by opening the admin console and going to Applications -> Applications, the Port app will appear in the application list.

### Step #2: Configure your Onelogin application[â](#step-2-configure-your-onelogin-application "Direct link to Step #2: Configure your Onelogin application")

In the Port app, go to the `Configuration` menu and follow these steps:

1. Under `Login URL` paste the following login URL:

Setting authorization endpoint based on account region

Port exposes two API instances, one for the EU region of Port, and one for the US region of Port.<br /><!-- -->Use the correct endpoint based on your account region, and make sure to to replace `{CONNECTION_NAME}` with the value provided to you by Port.

* EU
* US

```
https://auth.getport.io/authorize?response_type=token&client_id=96IeqL36Q0UIBxIfV1oqOkDWU6UslfDj&connection={CONNECTION_NAME}&redirect_uri=https%3A%2F%2Fapp.getport.io
```

```
https://auth.us.getport.io/authorize?response_type=token&client_id=4lHUry3Gkds317lQ3JcgABh0JPbT3rWx&connection={CONNECTION_NAME}&redirect_uri=https%3A%2F%2Fapp.us.getport.io
```

note

We will provide your `{CONNECTION_NAME}` (Contact us using chat/Slack/mail to [support.port.io](http://support.port.io/)).

2. Under `Redirect URI's` set: `https://auth.getport.io/login/callback`.

   * The Redirect URI is where Onelogin sends the authentication response and ID token for the sign-in request.

Click `Save`.

warning

Be sure to click save before moving on to the next step because without the `Redirect URI's` filled in, trying to save any other application parameter will result in an error.

### Step #3: Configure OIDC settings[â](#step-3-configure-oidc-settings "Direct link to Step #3: Configure OIDC settings")

In the Port app, go to the `SSO` menu and follow these steps:

1. Copy the `Client ID` and the `Client Secret` and send it to Port (on the slack channel).

2. Click on the `Well-known Configuration` Link, and send the page address to Port (its format will be `https://{YOUR_DOMAIN}.onelogin.com/oidc/2/.well-known/openid-configuration`)

3. Change the Token Endpoint - Authentication Method to `None (PKCE)`:

![Okta app settings](/assets/images/OneloginSSOSetting-8cfe11b02745b8b7b05372724401cdb2.png)

Click `Save`.

### Step #4: Add `email_verified` custom property to all users[â](#step-4-add-email_verified-custom-property-to-all-users "Direct link to step-4-add-email_verified-custom-property-to-all-users")

The use of OpenID requires that Onelogin passes to Port an `email_verified` field upon user login. Onelogin does not store and expose that field by default, so in this step, you are going to configure that field and apply it to all users in your Onelogin account. The steps outlined here can also be found in the [Onelogin documentation](https://developers.onelogin.com/openid-connect/guides/email-verified).

1. In the Admin Console, go to Users -> Custom User Fields.

2. Click on `New User Field`.

3. Enter the following details:

   <!-- -->

   1. `Name`: Email Verified
   2. `Shortname`: email\_verified

![Onelogin email verified user field](/assets/images/OneloginEmailVerifiedUserField-178c134d6cdc8e4d30b58374de247170.png)

The custom field is `null` by default, in order to change its value to `true` you will create a custom mapping rule:

note

It is also possible to manually change the value of the `Email Verified` field to `true` for each user that requires access to Port in your organization. However, granting access manually to a large number of users is not scalable.

tip

The mapping specified here will set the value of the `Email Verified` custom field to `true` for every user whose `Status` is `Active` in your Onelogin organization. Feel free to use a different mapping if you seek a specific mapping.

1. Go to Users -> Mappings

2. Click on `New Mapping`

3. Enter mapping details:

   <!-- -->

   1. `Name`: Insert a friendly name for the mapping, like `Set Email Verified`;
   2. `Conditions`: Set the condition: - Status - is - Active;
   3. `Actions`: Set the action: Set Email Verified - true.

4. Click `Save`.

![Onelogin Email Verified Mapping Rule](/assets/images/OneloginEmailVerifiedMappingRule-0d5551b69cf6d8f323e94ac828951bc7.png)

After creating the mapping rule, go back to Users -> Mappings and click on `Reapply All Mappings`. The new mapping might process for a few minutes before it is applied. You can check the mapping job status either by going to Activity -> Jobs or by looking at a specific user and verifying that it has the `Email Verified` field set to `true` (and not the default empty field).

### Step #5: Configure OpenID Claims[â](#step-5-configure-openid-claims "Direct link to Step #5: Configure OpenID Claims")

In the Port app, go to the `Parameters` menu and follow these steps:

1. Click on the `+` button;
2. In the form that appears, under `Field Name` write: `openid` and click `save`;
3. In the value drop down that appears, select `OpenID name`.

Repeat the process two more times and add the following additional parameters:

1. `Field Name`: email, `Value`: Email
2. `Field Name`: email\_verified, `Value`: Email Verified (Custom)

At the end of the process, your `Parameters` section will look like this:

![Onelogin App Parameters Setting](/assets/images/OneloginParametersSetting-75c959b0a5eb2014ea99a55d6fb445ca.png)

Click `Save`.

### Step #6: Exposing the application to your organization[â](#step-6-exposing-the-application-to-your-organization "Direct link to Step #6: Exposing the application to your organization")

1. In the `Application` page, select the Port app and go to the `Access` menu.

2. In the `Roles` section, select the roles you want to expose the Port app to:

   ![Onelogin Assign App Roles](/assets/images/OneloginAssignAppRoles-9c5c9650ae07d690c4ec1b894a2db7c3.png)

3. Click `Save`.

After completing these steps, users with roles that the Port app was assigned to, will see the Port app in their Portal and upon clicking it, will be logged in to Port:

[Onelogin Portal With Port App](/assets/files/OneloginPortalWithApp-9495574bc3ee4e364c36e5e71ff7051e.png)

Direct access via URL

After configuring the SSO connection, you can initiate the login flow directly via URL.<br /><!-- -->Use the following URL based on your account region, and make sure to to replace `{CONNECTION_NAME}` with the value provided to you by Port.

* EU
* US

```
https://auth.getport.io/authorize?response_type=token&client_id=96IeqL36Q0UIBxIfV1oqOkDWU6UslfDj&connection={CONNECTION_NAME}&redirect_uri=https%3A%2F%2Fapp.getport.io
```

```
https://auth.us.getport.io/authorize?response_type=token&client_id=4lHUry3Gkds317lQ3JcgABh0JPbT3rWx&connection={CONNECTION_NAME}&redirect_uri=https%3A%2F%2Fapp.us.getport.io
```

***

## How to allow pulling Onelogin roles to Port[â](#how-to-allow-pulling-onelogin-roles-to-port "Direct link to How to allow pulling Onelogin roles to Port")

note

This stage is **OPTIONAL** and is required only if you wish to pull all of your Onelogin roles into Port inherently.

**Benefit:** managing permissions and user access on Port.<br />**Outcome:** for every user that logs in, we will automatically get their associated Onelogin roles, according to your definition in the settings below.

To allow automatic Onelogin roles support in Port, please follow these steps:

1. In the `Application` page, select the Port app and go to the `Parameters` menu;

2. Click on the `Groups` claim:

   ![Onelogin App Parameters Setting](/assets/images/OneloginParametersSetting-75c959b0a5eb2014ea99a55d6fb445ca.png)

3. Update the groups claim:

   1. Change the value of `Default if no value selected` to `User Roles`;
   2. From the dropdown, select `Semicolon delimited input`:

   ![Onelogin App Groups Claim Setting](/assets/images/OneloginGroupsClaim-d9e8d3b0402f77f6d0dd995c3682547f.png)

   3. Click `Save`.

4. Click `Save`.
