---
id: GoogleSSO
title: Single Sign On with Google
---
## How to set up Google G-Suite as your SAML Identity Provider

Here's a walk-through of setting up Google G-suite as your SAML Identity Provider. This allows your team to log into Zenduty without a new email / password combination, they just log in to your Google account.

1. As an administrator on your Google account, go to the admin portal and click through to Apps > SAML Apps.

2. Choose "SAML apps"

![](/img/Integrations/GoogleSSO/1.png)

1. Click on the "Plus" icon lower-right to add a new SAML app.

2. Choose "Setup my own custom app" at the bottom of the list.

3. We will go with Option 1. In the Google IDP information page, download the Certificate on your local system. Open a notepad and copy-paste the "SSO URL" and "Entity ID". Click on "Next".

![](/img/Integrations/GoogleSSO/2.png)

1. In the Basic information for your Custom App, set "Zenduty" as the Application Name. Grab the logo from [here](https://d8x2313t22dpf.cloudfront.net/landing/img/zenduty-full-transparent-bg.2aeaeb96.png) and upload. Add some descriptive information about the new SAML app. This is used to identify the app for everyone on your Google Apps domain. Click on "Next"

![](/img/Integrations/GoogleSSO/3.png)

1. In the Service Provider Details page, copy the URL "https://www.zenduty.com/api/account/saml/acs/" and paste it into the “ACS URL” field in Google settings.

![](/img/Integrations/GoogleSSO/4.png)

1. Enter "https://www.zenduty.com" for the “Entity ID” field. Make sure you add the "/" or else you might encounter an error.

2. For the "Name ID" fields, select "Basic Information" and "Primary Email". For the "Name ID Format" field, select "Unspecified" and click "Next".

3. In Attribute mapping, click on "ADD NEW MAPPING" and add the attributes below.

email -> Basic Information (Primary Email)
first_name -> Basic Information (First Name)
last_name -> Basic Information (Last Name)

![](/img/Integrations/GoogleSSO/5.png)

1. Click on "Finish" to finish the SAML app setup.

2. Log into your Zenduty account as the owner. On the top right corner, click on the drowdown under your name and click on "Account". On the left panel, click on "Single Sign On"

![](/img/Integrations/GoogleSSO/6.png)

1. In the SSO form, select "Google SSO" under "Select SSO Provider"

2. In "SAML endpoint" input, paste the "SSO URL" you saved from Step 5. In "SAML Entity ID" input, paste "Entity ID" you saved from Step 5. Open the certificate you downloaded form Step 5 in a text editor. In the "Certificate" input, paste the certificate.

3. Click on "Save Integration" to complete your SSO setup!
