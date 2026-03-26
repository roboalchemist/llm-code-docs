# Source: https://docs.debricked.com/tools-and-integrations/single-sign-on-sso/single-sign-on-sso-through-okta.md

# Single Sign-On (SSO) through Okta (OIDC)

{% hint style="info" %}
*This feature is currently only available for* [*SCA Enterprise*](https://debricked.com/pricing/) *customers.*
{% endhint %}

This article details how to configure Okta as the primary Identity Provider to facilitate SSO with OpenText Core SCA. For details regarding integration with other Identity Providers, see [Single Sign-On (SSO)](https://docs.debricked.com/tools-and-integrations/single-sign-on-sso).

### Supported features

* Single Sign-On (OpenID Connect) initiated via Okta
* Automatic account creation in OpenText Core SCA on initial sign-on

### Requirements <a href="#requirements" id="requirements"></a>

* The Okta Single Sign-On integration is only available for the Enterprise customers.
* To complete the integration, you must:
  * Have an Okta account with administrator rights.
  * Install the OpenText Core SCA application in your Okta instance.

### Configuration <a href="#configuration" id="configuration"></a>

To configure your SSO integration to Okta follow the following steps:

#### Gather information from Okta <a href="#gatherinformationfromokta" id="gatherinformationfromokta"></a>

1. In the Okta admin page, click the **OpenText Core SCA** application.
2. Navigate to the **Sign On** tab.
3. Copy the values of **Client ID** and **Client secret** (you can click the eye to toggle the visibility).
4. Click **OpenID Provider Metadata** and open the document.
5. In the opened document, find the ***Issuer key*** and copy the URL-value.

#### Complete integration with OpenText Core SCA <a href="#completetheintegrationwithdebricked" id="completetheintegrationwithdebricked"></a>

To complete the integration, enter the following information:

* **Issuer URL** (the URL used to fetch OIDC information)
* **Email Domains** (the email domains which will be designated to your organization)
* **Client ID** (identifier of the OpenText Core SCA integration)
* **Client secret** (secret to authorize the integration, also provided when installing the integration in your IdP)

You can forward it to us by either:

* Getting in touch with the support team at [***support@debricked.com***](mailto:support@debricked.com)
* Submitting the configuration data through an API endpoint at <https://debricked.com/api/1.0/open/sso/oidc/request>

### Log into OpenText Core SCA using SSO <a href="#logintodebrickedusingsso" id="logintodebrickedusingsso"></a>

\
Once the integration is completed, you can log into OpenText Core SCA.
