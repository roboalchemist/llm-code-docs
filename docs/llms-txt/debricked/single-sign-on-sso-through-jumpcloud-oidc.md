# Source: https://docs.debricked.com/tools-and-integrations/single-sign-on-sso/single-sign-on-sso-through-jumpcloud-oidc.md

# Single Sign-On (SSO) through JumpCloud OIDC

{% hint style="info" %}
*This feature is currently only available for*  [*SCA Enterprise*](https://debricked.com/pricing/) *customers.*
{% endhint %}

This article details how to configure JumpCloud OIDC as the primary Identity Provider to facilitate SSO with OpenText Core SCA. For details regarding integration with other Identity Providers, see [Single Sign-On (SSO)](https://docs.debricked.com/tools-and-integrations/single-sign-on-sso).

### Adding a new application <a href="#addinganewapplication" id="addinganewapplication"></a>

1. In your JumpCloud Admin portal, click **SSO** under **User Authentication** in the sidebar.
2. Click **+ Add new application** at the top of the page.
3. Once the applications modal is open, click **Custom OIDC App** to start setting up the OpenText Core SCA integration.

### Configuring OpenText Core SCA application <a href="#configuringthedebrickedapp" id="configuringthedebrickedapp"></a>

After clicking on **Custom OIDC App** you will be asked to name the new application. It is suggested to provide an easily recognizable name, for example, “Debricked” or “Debricked SSO”.

Select the **SSO** tab and complete the configuration:

1. In the **Redirect URIs** input, set: \*<https://debricked.com/app/sso/oidc/auth\\>\*.
2. The **Client Authentication Type** should be set to “**Client Secret Basic”.**
3. Set the **Login URL** to: \*<https://debricked.com/app/sso/oidc/login\\>\*.
4. Add three parameters to the **Attribute Mapping** section to enable OpenText Core SCA to fetch the necessary user data. On the left, you can find the attribute names (make sure they are spelled correctly) and on the right the corresponding JumpCloud name. The mapping is as follows:

* email → email
* given\_name → firstname
* family\_name → lastname

Now that everything is set up, you can click **Activate** at the bottom right of the page to save the application.

JumpCloud will now present you with the ClientID and Client Secret which you will need to send to OpenText Core SCA support team to complete the integration.

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

Note that in order for your users to be able to use this application you will need to assign them to the new application you have created. To do so, click the OpenText Core SCA application from your JumpCloud Admin Portal and go to the **User Groups** tab, from here you will be able to assign user groups to this application

Once your users are added, they can direct log in from <https://debricked.com/app/sso/login> . You can also invite them from OpenText Core SCA (keep in mind that they must be assigned to the application on your vendor side) from your Admin Tools. This invite will be a special *SSO invite*, which will redirect them to your Identity Provider and let them log in to OpenText Core SCA.

### Testing setup <a href="#testingthesetup" id="testingthesetup"></a>

Once your integration has been added to your enterprise account, you can enable it in the OpenText Core SCA web tool by visiting the **User Permissions** tab in **Admin Tools**.

Head over to <https://debricked.com/app/sso/login>, type enterprise email ID (the same email domain which you submitted before). You should be redirected to your Identity Provider and be able to authenticate. After logging in, you will be redirected and logged in to OpenText Core SCA as well.
