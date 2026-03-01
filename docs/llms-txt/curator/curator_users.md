# Source: https://docs.curator.interworks.com/setup/authentication/curator_users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Curator Users

> A guide to setting up local Curator users to authenticate with SAML.

If you would like to use SAML for authentication with your Curator users, but do not want to use a 3rd party tool
(e.g. Okta) you're in luck - you can utilize Curator as your Identity Provider (IdP)!  However, there is one important
caveat: if you set up Curator as your IdP by following the instructions for Curator Users below, you will also need to
make Curator your IdP for any connected applications (e.g. Tableau Cloud).
, they will then be redirected back to whichever entry point they came in from (e.g. Tableau Cloud will redirect back to
Tableau's homepage and Curator will redirect back to Curator's homepage).

**If you set up Curator as your IdP for Tableau ALL users will see the Curator login when trying to access
Tableau directly**.

NOTE: This setup will *not* work with Tableau Server, and is not needed due to the availability of using Trusted Ticket
on Tableau Server.

## 1. Curator Setup

If you have not installed Curator yet, please refer to our installation documentation in the setup section on the
left-hand side menu.

Also ensure you have connected to your Tableau Cloud instance following the
[REST API  Integration steps](/creating_integrations/tableau_connection/creating_a_connection).

## 2. Retrieve Tableau SAML Details

Next, navigate to your Tableau Cloud instance and find the Tableau Entity ID and the Assertion Consumer Service URL
(ACS) by setting your Authentication type to SAML.

[Tableau Cloud Documentation for reference](https://help.tableau.com/current/online/en-us/saml_config_okta.htm)

## 3. Curator IdP Setup

1. Navigate to the **Settings** > **Security** > **SAML IdP** section from the left-hand menu.

2. Fill out the required fields:
   * For the **Curator Entity ID** enter the URL of your Curator website
   * For the **Tableau Entity ID** paste in the value you retrieved from the previous step
   * For the **Assertion Consumer Service URL (ACS)** paste in the values

3. Once the form is completed, click the "Auto-Generate Key/Cert" button and fill out the form, then click "Generate".

4. Save this page

5. After saved successfully, click the "Download Metadata" button at the top and save this file, it will default to
   `curator_metadata.xml`.

## 4. Setup Tableau Cloud SAML

1. Return to Tableau Cloud
2. Click the **Settings** menu item on the left, then the **Authentication** tab at the top of the page.
3. Ensure "SAML" is selected under the "Enable an additional authentication method" section.
4. Find the "Import metadata file into Tableau Cloud" section, and upload the `curator_metadata.xml` file you download
   in the previous step then click "Apply"
5. In the "Match attributes" below, ensure the "Identity Provider (IdP) Assertion Name" is set to "email", and select
   "Full name" for "Display Name", and change the value to "full\_name" and click "Apply"

Last, you can click the "test connection" button in the *Import metadata file into Tableau Cloud* section to ensure your
SAML authentication has been set up correctly to direct users to Curator.  You should see your Curator login screen
appear (if you are not already logged in).

You can now change individual users on the list-users screen in Tableau Cloud by changing the user's configuration to SAML.

## 6. Testing Your Curator Users Authentication

**NOTE**: You *must* complete Step #3 for this button to display.

1. Navigate to the **Settings** > **Tableau** > **Frontend Users** section from the left-hand menu.
2. Click the "Sync from Tableau" button
3. Once the sync has finished, open an incognito window in your web-browser
4. Visit your Tableau Cloud site and log in with a user that has been registered as a SAML user on Tableau Cloud.
5. You will be redirected to Curator to login, after which you will be redirected again to Tableau Cloud.
6. You have now set up Curator as your SAML IdP, nice work!
