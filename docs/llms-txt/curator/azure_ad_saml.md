# Source: https://docs.curator.interworks.com/setup/authentication/azure_ad_saml.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure AD

> A guide to setting up Azure AD authentication for Curator.

## Provisioning Users on Azure AD

For provisioning users with Azure AD, you will need to have a user created in both Azure AD and Tableau Server - their
username's must match (the "Application username format" step in #4 below).

Once the user logs in, their username in Azure needs to match *exactly* the username of a user on Tableau Server.

## Curator Setup

If you have not installed Curator you can do this with the commands in the Installation documentation.

Also ensure you have connected to your Tableau Server instance following the [Tableau Server connections steps](/creating_integrations/tableau_connection/creating_a_connection).

## Tableau Setup

**Tableau Cloud**
Tableau has excellent documentation on connecting Azure AD to Tableau Cloud. [https://help.tableau.com/current/online/en-us/saml\_config\_azure\_ad.htm](https://help.tableau.com/current/online/en-us/saml_config_azure_ad.htm)

Make sure to follow the additional setup steps in the Tableau Cloud documentation.

**Tableau Server**
To ensure that after a user signs in to SAML via Curator they do not have to re-sign in to the embedded Tableau Server Dashboard:

On your Tableau Server run the command below:

```bash  theme={null}
tsm configuration set -k wgserver.saml.iframed_idp.enabled -v true
```

Next, either run:

```bash  theme={null}
tsm pending-changes apply
tsm restart
```

Or open TSM in your browser and click Pending Changes at the top of the page then click 'Apply Changes and Restart'.

## Azure App Creation

The app you create here will be in addition to the one you already setup for Tableau.

### Create your Azure App

1. Login to [https://portal.azure.com](https://portal.azure.com)
2. In the search bar search for "Azure Active Directory" and click the result that matches from the result list.
3. From the left-hand menu click "Enterprise Applications"
4. Click "Create a new application"
5. Click the "+ Create your own application"
6. Enter a name for your app and select the **non-gallery** option - We recommend the name `Curator`
7. Click "Create"

## Azure to Curator Configuration

### Import Curator Metadata to your Azure App

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`)
2. Navigate to the **Settings** > **Security** > **Authentication Settings** section from the left-hand menu.
3. Change the "Authentication Type" to SAML
4. This will expose two buttons, click the "Download SAML Metadata" button, and save the file somewhere you can soon retrieve.
5. Return to the app you created in the steps above in the Azure portal, and from the left-hand navigation click
   "Single sign-on".
6. At the top click "Upload metadata file" and upload the file you downloaded from Curator in step #4 here.

### Import Azure Metadata to your Curator Instance

1. Continuing from the steps above, while still on the same page find the section of the page titled
   "SAML Signing Certificate" and click the "Download" link next to **Federation Metadata XML**
2. Save this file.
3. Click the "Import SAML Metadata" button and follow the steps to upload the file downloaded in step #7.
4. After the file is uploaded, ensure your Authentication Type is still set to SAML and re-save your settings.

#### Troubleshooting Attributes and Claims

In many cases you will need to adjust the "Attributes and Claims" section on your app by adding a new claim with the
name "username".  If you see an error on logging in after setting up saying "User \[username] not found" the
\[username] is what Azure is sending to Curator.  That must match exactly the username found on Tableau Server.

**Note**: If you have already created a Tableau app in Azure and your authentication is running successfully, then
simply ensure the Attributes and Claim and configuration of your Curator app matches exactly the setup you have for
your Tableau app.

**Troubleshooting Tableau Login**
If a Tableau login button appears where a Dashboard should be after configuring SAML, be sure to follow the steps to
enable iFrame embedding in the following document:
[https://help.tableau.com/current/online/en-us/saml\_config\_okta.htm#optional-enable-iframe-embedding](https://help.tableau.com/current/online/en-us/saml_config_okta.htm#optional-enable-iframe-embedding)
