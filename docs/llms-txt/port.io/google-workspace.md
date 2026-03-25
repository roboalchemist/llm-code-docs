# Source: https://docs.port.io/sso-rbac/sso-providers/saml/google-workspace.md

# Google Workspace

Follow this step-by-step guide to configure the integration between Port and Google Workspace.

info

In order to complete the process you will need to contact us to receive the information you require, as well as the information Port requires from you. All is elaborated below.

## Port-Google Workspace integration benefits[â](#port-google-workspace-integration-benefits "Direct link to Port-Google Workspace integration benefits")

* Connect to the Port application via your Google Workspace Application.
* Your Google Workspace teams will be automatically synced with Port upon a user sign-in.
* Set granular permissions on Port according to your Google Workspace groups.

## Create your Google Workspace application[â](#create-your-google-workspace-application "Direct link to Create your Google Workspace application")

1. In the [Google Admin Console](https://admin.google.com/), in the sidebar menu, navigate to **Apps** -> **Web and mobile apps**:

![](/assets/ideal-img/webAndMobile.1225df7.257.png)

<br />

2. Click on `Add app` followed by `Add custom SAML app`:

![](/assets/ideal-img/addSamlApp.7cd84a5.300.png)

<br />

3. Define the initial Port application settings:

   1. `App name`: Insert a name of your choice for the Port app, like `Port`.
   2. Add an `App icon` (optional):

   Port Logo

   ![Port\&#39;s logo](/assets/images/PortIcon-b535fa79c7fc8d10c3dbcc6107733c66.png)

   3. Press `Continue`

![](/assets/ideal-img/appNameAndIcon.e67e0fd.300.png)

<br />

4. Take note of the following:

   <!-- -->

   1. Your `SSO URL`;
   2. Your `Certificate`.

![](/assets/ideal-img/SSOandCert.21b94dc.300.png)

<br />

Pass these to Port.<br />

Press `Continue`.

5. Configure your new application as shown below:

* `ACS URL` - `https://auth.getport.io/login/callback?connection={CONNECTION_NAME}`
* `Entity ID` - `urn:auth0:port-prod:{CONNECTION_NAME}`

note

We will provide your `{CONNECTION_NAME}` (Contact us using chat/Slack/mail to [support.port.io](http://support.port.io/)).

Press `Continue`

![](/assets/ideal-img/acsURLandEntityID.6cadd1d.300.png)

<br />

6. Create the following mappings (email\_verified needs to be a constant for all users, with the value `true` ):

*Google Directory attributes*:

* **`Primary email`** -> `email`
* **`First name`** -> `name`
* **`email_verified`** -> `email_verified`

*Google membership* (optional): This mapping is only relevant if you wish to pass groups to Port.

* **`Google Groups`**(list) -> `groups`

Press `Finish`

![](/assets/ideal-img/attributeMapping.f28d859.300.png)

<br />

7. Specify permissions to the application:

After creating the app, you need to set up permissions for who has access to this application.

Navigate to your your new application's page, and click **User access**:

![](/assets/ideal-img/userAccessInApp.6ef573c.300.png)

<br />

Then choose from the left side menu, either to enable the app for `Everyone`, for `Groups` or for `Organizational units`.

Make sure that for any of the options you would like to enable the app for, you check the `ON` checkbox:

![](/assets/ideal-img/turnAccessOn.26933e3.300.png)

<br />

7. Log in with using your new Google app:

![](/assets/ideal-img/loginUsingApp.1d4bd27.300.png)

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
