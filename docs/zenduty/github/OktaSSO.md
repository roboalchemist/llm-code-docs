---
id: OktaSSO
title: Single Sign On with Okta
---
## How to set up Okta as your SAML Identity Provider

Here's a walk-through of setting up Okta as your SAML Identity Provider. This allows your team to log into Zenduty without a new email / password combination.

1. Log in to Zenduty as an administrator. In another tab, Log into Okta as an administrator.

2. In Zenduty, click on your name in the top right corner, which will reveal a dropdown with your account's domain name. Copy your account domain name for later use.

![](/img/Integrations/Okta/11.png)

1. Go to your Okta admin dashboard. Click on "Applications". Click on "Add Application" and search for "Zenduty" in the Okta application marketplace. Click on "Add" next to Zenduty.

![](/img/Integrations/Okta/12.png)

1. Click on the Zenduty application in Okta. Click on the "Sign On" tab. Click on "Edit" in the "Settings" section.

![](/img/Integrations/Okta/13.png)

1. In the "Default Relay State" box, enter the Zenduty account subdomain you copied in Step 2. FOr Application username format, Select "Email".

2. Click on "View Setup Instructions". This will open a new tab which will contain three values which you need to temporarily copy in a text editor for the next step - SAML endpoint, SAML Entity ID and Certificate.

![](/img/Integrations/Okta/14.png)

![](/img/Integrations/Okta/15.png)

1. Assign users to the Zenduty application on Okta.

2. Go back to the Zenduty tab. On the top right corner, click on the drowdown under your name and click on "Account". On the left panel, click on "Single Sign On"

3. In the SSO form, select "Okta SSO" under "Select SSO Provider"

4. In "SAML endpoint" input, paste the "SAML endpoint" you saved from Step 6. In "SAML Entity ID" input, paste "SAML Entity ID" you saved from Step 6. In the "Certificate" input, paste the Certificate copied from step 6.

![](/img/Integrations/Okta/16.png)

1. Click on "Save Integration" to complete your SSO setup!

2. To test SP-initiated SSO, logout of your Zenduty account and click on Login. Click on "Login with your identity provider". Enter your account domain name and click on "Continue". Authenticate your Okta credentials to login into Zenduty.

3. To test iDP-initiated SSO, logout of your Zenduty account. Login to your Okta account and from the application list, click on Zenduty. You will be logged into Zenduty.
