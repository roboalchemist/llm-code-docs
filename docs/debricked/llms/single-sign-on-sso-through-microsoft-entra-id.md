# Source: https://docs.debricked.com/tools-and-integrations/single-sign-on-sso/single-sign-on-sso-through-microsoft-entra-id.md

# Single Sign-On (SSO) through Microsoft Entra ID (OIDC)

{% hint style="info" %}
*This feature is currently only available for* [*SCA Enterprise*](https://debricked.com/pricing/) *customers.*
{% endhint %}

This article details how to configure Microsoft Entra ID as the primary Identity Provider to facilitate SSO with OpenText Core SCA. For details regarding integration with other Identity Providers, see [Single Sign-On (SSO)](https://docs.debricked.com/tools-and-integrations/single-sign-on-sso).

### Registering a new Microsoft Entra ID application <a href="#registeringanewazurea-dapplication" id="registeringanewazurea-dapplication"></a>

1. Search for **App registrations.**
2. Click **New registration.** It is suggested to name your application “OpenText Core SCA”, but it is not mandatory.&#x20;
3. In the **Redirect URI,** section select **Web** as type of application and enter:

<https://debricked.com/app/sso/oidc/auth>

4. **Confirm** the details and proceed to the next step.

### Getting client ID <a href="#gettingtheclientid" id="gettingtheclientid"></a>

You can find the Client ID from the Overview section, the first page you will see after creating the application.

#### Creating Client Secret <a href="#creatingthe-clientsecret" id="creatingthe-clientsecret"></a>

1. On the sidebar, click **Certificates & secrets**.
2. Click **New client secret** and choose a name and expiration date. When it is created, ensure to copy and store somewhere, as it will only be visible once.

### Getting OIDC metadata endpoint (issuer URL) <a href="#gettingtheoidcmetadataendpoint-issuerurl" id="gettingtheoidcmetadataendpoint-issuerurl"></a>

This is needed for OpenText Core SCA to know where to redirect the user, fetching credentials tokens and fetching user information.

1. Go back to the **Overview** from the sidebar and click **Endpoints** tab.
2. The one needed is called the **OpenID Connect metadata document**.

### Communicating data with OpenText Core SCA <a href="#communicatingthedatawithdebricked" id="communicatingthedatawithdebricked"></a>

To complete the integration, enter the following information:

* **Issuer URL** (the URL used to fetch OIDC information)
* **Email Domains** (the email domains which will be designated to your organization)
* **Client ID** (identifier of the OpenText Core SCA integration)
* **Client secret** (secret to authorize the integration, also provided when installing the integration in your IdP)

You can forward it to us by either:

* Getting in touch with the support team at [***support@debricked.com***](mailto:support@debricked.com)
* Submitting the configuration data through an API endpoint at <https://debricked.com/api/1.0/open/sso/oidc/request>

### Adding users <a href="#addingusers" id="addingusers"></a>

Note that in order for your users to be able to use this application you will need to assign them to the new application you have added.

1. Go to **Enterprise applications**.&#x20;
2. Click on your OpenText Core SCA application and then go to **Users and groups**. Here, you will be able to assign users and user groups.
3. Once your users are added, they can directly log in from <https://debricked.com/app/sso/login>.\
   You can also invite them from OpenText Core SCA (note that they must be assigned to the application on your vendor side) from your **Admin Tools**. This invite will be a special “SSO invite” which will redirect them to your Identity Provider and let them log into OpenText Core SCA.

### Testing setup <a href="#testingthesetup" id="testingthesetup"></a>

Once your integration has been added to your enterprise account, you can confirm it on the OpenText Core SCA service by visiting the **User Permissions** tab in **Admin Tools**.

You can head over to <https://debricked.com/app/sso/login>, input the enterprise email (with the same email domain which you submitted), and you will be redirected to your Identity Provider to authenticate. After logging in, you will be redirected and logged into OpenText Core SCA.
