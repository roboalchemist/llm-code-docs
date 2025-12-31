# Source: https://docs.aporia.com/integrations/sso-saml-integration.md

# Source: https://docs.aporia.com/v1/integrations/sso-saml-integration.md

# Source: https://docs.aporia.com/integrations/sso-saml-integration.md

# Source: https://docs.aporia.com/v1/integrations/sso-saml-integration.md

# Single Sign On (SAML)

You can easily give access to Aporia to your team using your favorite SAML Idp.

The integration can be found on the "Integrations" page, accessible through the sidebar:

![All Integrations](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FogmjRuZ5XbmPSJwXoBPm%2Fall_integrations.png?alt=media)

### Setting up the SAML integration

After clicking the **Connect** button inside the **SAML Single sign on** card (only available for *Professional* users), you will be redirected to the "Integrations" page.

![Exchange data](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FStxU1ERCg8tp56OoPvnG%2Fsaml_exchange_data.png?alt=media)

### Integrate with your Idp

Create a new application in your favorite SAML Idp and fill in the relevant details under the **For you** title. Here's a demonstration of the process of integrating with OKTA below.

1. Sign in to your OKTA dev account.
2. In the sidebar, click on **Applications -> Applications**.
3. Click on the **Create App Integration** button.
4. Choose **SAML 2.0** and click **Next**. You should now be in step 1 of the creation wizard named **General settings**.\
   &#x20;

   <figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FnlIgkJTdfpWDLTx8JxwX%2Fsaml_okta_create_app_step_1.png?alt=media" alt=""><figcaption></figcaption></figure>
5. Fill in the **App name** as **Aporia** and click **Next**. Moving forward to step 2, **Configure SAML**.
6. Fill in the **Single sign on URL** and **Audience URI** according to the fields in the **SAML integration** page in Aporia.

<figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FdTaV2Qr48Ycet1SDzlBU%2Fsaml_okta_create_app_step_2.png?alt=media" alt=""><figcaption></figcaption></figure>

&#x20;7\. Scroll to the **Attribute Statements** section. Fill in the data as follows:

| Name                                                                 | Name format   | Value          |
| -------------------------------------------------------------------- | ------------- | -------------- |
| <http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress> | URI Reference | user.email     |
| <http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname>    | URI Reference | user.firstName |
| <http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname>      | URI Reference | user.lastName  |

Click on the **Add Another** button to add a new attribute.

1. Scroll down and click **Next**. In step 3, fill in the requested data however you think is right and click on **Finish**.

### Integrate with Aporia

1. Inside your OKTA application page, click on the **Sign On** tab.
2. Scroll down and click the **View Setup Instructions** button.
3. Copy the value under **Identity Provider Single Sign-On URL** step and download the **X.509 Certificate**.
4. In Aporia, under the **For us** title, fill in the data you gathered from step 3 and click on **Connect**.&#x20;

   <figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2F9d0M20yreuYCDrY2UKoZ%2Fsaml_for_us.png?alt=media" alt=""><figcaption></figcaption></figure>
5. You'll be redirected to the **Integration success page** where you'll be able to see and edit your connection data.

<figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FFfqt7xvtmH3Oc1hgyvHW%2Fsaml_success.png?alt=media" alt=""><figcaption></figcaption></figure>

You can now go and test your connection using the Idp-initiated login link.
