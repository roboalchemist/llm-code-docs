# Source: https://docs.axonius.com/docs/example-saml-based-authentication-with-azure-active-directory.md

# Example: SAML Based Authentication with Microsoft Entra ID

The following example describes how to enable SAML-based authentication in Axonius with Microsoft Entra ID (formerly Azure AD).

<Callout icon="📘" theme="info">
  Note

  Microsoft updates their UI from time to time. The location of fields on their pages may be different than described here.
</Callout>

## Configuring a SAML Instance Using Metadata Files

Microsoft Entra ID allows the use of metadata files that make SAML instance configuration easy. The metadata file contains the specific URLs used to connect between Axonius and Entra ID. This process requires moving between Axonius and Entra ID, so keep both open in separate tabs.

**Do the following in Axonius:**

See [SAML-Based Login Settings](/docs/saml-based-login-settings) for descriptions of these fields.

1. Log in to Axonius as an administrator, then go to **Settings -> Access Management -> LDAP & SAML**, and toggle on **Allow SAML-based logins**.
2. Under SAML Instance, in **Name of the identity provider** enter a name for the SAML instance. This name will appear on the Axonius Log-in page after the instance is created.
3. In **Unique name of IDP**, enter a unique name for this SAML configuration. The IDP can be up to 10 lower case characters (a-z) or numbers (0-9). Save this name so that you can refer to it later. Once the instance is saved this value cannot be changed. See [Unique Name of IDP](/docs/example-saml-based-authentication-with-azure-active-directory#unique-name-of-idp) below.
4. Click **Save**.
5. Click **Download Metadata file**.
6. Keep this page open in Axonius.
7. Go to **Entra ID**.

**Do the following in Microsoft Entra ID:**

1. Log in to the Entra ID portal, go to **Azure Active Directory**, and click **Enterprise Applications**.

<Image align="center" alt="EntraIDEnterpriseApplications.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EntraIDEnterpriseApplications.png" />

3. On the top toolbar, click **New application** to create an application for Axonius.

<Image align="center" alt="SAMLAzureAD-NewApp.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLAzureAD-NewApp.png" />

The Cloud application gallery is displayed.

3. Click **Create your own application**.

<Image align="center" alt="SAMLEntraID-CreateOwnApp.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLEntraID-CreateOwnApp.png" />

A 'Create your own application' pane opens on the right.

4. In **What's the name of your app?**, enter a name for your application. This name does not have to be the same name as you used in Axonius.

<Image align="center" alt="SAMLEntraID-AppName.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLEntraID-AppName.png" />

5. Select **Integrate with any other application you don’t find in the gallery (Non-gallery**).

6. Click **Create**.

   After your application is created, the Overview page of the new app is displayed.

7. Under Getting Started, click **Set up single sign on**.

<Image align="center" alt="SAML-EntraIDAppOverview.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAML-EntraIDAppOverview.png" />

The Single sign-on page is displayed.

8. Under Single sign-on method, click **SAML**.

<Image align="center" alt="SAML-EntraIDSAML.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAML-EntraIDSAML.png" />

The SAML-based Sign-on page is displayed.

9. Click **Upload metadata file**. To the right of the file name box, click the file icon to upload the metadata file.

<Image align="center" alt="SAML-EntraIDUploadmetadataFile.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAML-EntraIDUploadmetadataFile.png" />

10. Navigate to the metadata file on your system, select it, and click **Add**.
    The Basic SAML Configuration pane opens to the right with the Identifier, Reply URL, and Logout Url fields populated with URLs from the metadata file.

<Image align="center" alt="SAML-EntraIDBasicSAMLConfig.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAML-EntraIDBasicSAMLConfig.png" />

11. Click **Save**.
12. In the SAML Certificates section, copy the App Federation Metadata Url.

<Image align="center" alt="SAML-EntraIDAppFedMetadataURL.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAML-EntraIDAppFedMetadataURL.png" />

13. Keep this page open in Entra ID.
14. Go back to **Axonius**.

**Do the following in Axonius:**

1. Paste the metadata URL from Entra ID into the **Metadata URL** field.

<Image align="center" alt="SAML-AxoniusMetadataURL.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAML-AxoniusMetadataURL.png" />

The following fields are populated behind the scenes:

* Single sign-on service URL
* Entity ID
* Single logout service URL

2. Click **Save**.

**Testing the single sign-on**
Entra ID may ask if you want to test the single sign-on with entraTest.

1. In Entra ID, click **Yes**.
2. In the Test single sign-on with entraTest panel, click **Test sign in**.

You can also test it by logging out of Axonius and using the new log in with  button on the Axonius Log-in page.

## Configuring a SAML Instance Without Using the Metadata File

Use this procedure to configure a SAML instance without using the metadata file.

**Do the following in Axonius:**

See [SAML-Based Login Settings](/docs/saml-based-login-settings) for descriptions of these fields.

1. Log in to Axonius as an administrator, then go to **Settings -> Access Management -> LDAP & SAML**, and toggle on **Allow SAML-based logins**.
2. Under SAML Instance, in **Name of the identity provider** enter a name for the SAML instance. This name will appear on the Axonius Log-in page after the instance is created.
3. In **Unique name of IDP**, enter a unique name for this SAML configuration. The IDP can be up to 10 lower case characters (a-z) or numbers (0-9). Once the instance is saved this value cannot be changed. See [Unique Name of IDP](/docs/example-saml-based-authentication-with-azure-active-directory#unique-name-of-idp) below.
4. Click **Save**.
5. Click **Download Metadata file**.
6. Keep this page open in Axonius.
7. Go to **Entra ID**.

**Do the following in Microsoft Entra ID:**

1. Log in to the Entra ID portal, go to **Azure Active Directory**, and click **Enterprise Applications**.
2. Click **All applications**.

<Image align="center" alt="SAMLAzureAD-AllApps.png" border={false} width="250px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLAzureAD-AllApps.png" />

3. On the top toolbar, click **New application** to create an application for Axonius.

<Image align="center" alt="SAMLAzureAD-NewApp.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLAzureAD-NewApp.png" />

The Cloud application gallery is displayed.

3. Click **Create your own application**.

<Image align="center" alt="SAMLEntraID-CreateOwnApp.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLEntraID-CreateOwnApp.png" />

4. Enter a name for your application.

   <Image align="center" alt="SAMLEntraID-AppName.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLEntraID-AppName.png" />

5. Select **Integrate with any other application you don’t find in the gallery (Non-gallery**)

6. Click **Create**.

7. Under Manage click **Single sign-on** and then **SAML**.

<Image align="center" alt="SAMLEntraID-SingleSignOn.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLEntraID-SingleSignOn.png" />

9. Click **Upload metadata file** and then the file folder ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLEntraID-BlueFolder.png) to the right. Select the metadata file you downloaded from Axonius in the first step above and click **Add**.

<Image align="center" alt="SAMLEntraID-UploadMetaDataFile.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLEntraID-UploadMetaDataFile.png" />

The URLs are populated into the Identifier, Reply URL, and Logout URL fields.

<Image align="center" alt="SAMLEntraID-SingleSignOnURLs.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLEntraID-SingleSignOnURLs.png" />

12. Click **Save**.
13. Copy the **App Federation Metadata Url** in **SAML Signing Certificate**.

<Image align="center" alt="SAMLEntraID-AppFedMetaURL.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLEntraID-AppFedMetaURL.png" />

:::

**Do the following in Axonius:**

5. Under **User Assignment Settings**:
   * In **Default role for new SAML user only** user, select a default role. This role is assigned when there is no matching assignment rule.
   * In **Default Data Scope for new SAML user only**, select the Data Scope to assign to new users. This Data Scope is assigned when there is no matching assignment rule.
   * In **Evaluate user assignment on**, select to which users the role assignment setting will apply.
     * **New users** - The selected role is assigned to new users logging in with SAML for the first time.
     * **New and existing users** - The selected role is assigned to all users when they log in with SAML.
6. Click **Save**.

**Do the following in Microsoft Entra ID:**

The user should now be able to log in to Axonius with Entra ID.

**Verify the configuration works both ways - Axonius to Entra ID and Entra ID to Axonius**

1. Log in to Axonius using Entra ID and log out just to confirm it works.
2. In Entra ID, under **Manage**, click **Properties**.
3. Copy the **User access URL** and paste it into a new browser tab to confirm it takes you to Axonius.

## Unique Name of IDP

When configuring a SAML instance within Axonius without using the metadata file process, you may be asked to provide a "**Unique name of IDP**" value. This is an arbitrary value that is used to maintain IDP uniqueness in environments that use more than one SAML configuration. If a "Unique name of IDP" value is provided, it must also be appended with a leading `?idp=` to the URL in the Entra ID SSO Application configuration under the "**Identifier (Entity ID)**" field.

In the example screenshots, an IDP value of "**12345678**" has been configured.

<Image alt="azureSSOIDPValue.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/2146756221da50012a9cd9d3d2f23fda6ff97482/Images/azureSSOIDPValue.png" />

<Image alt="SAMLInstanceEntraExampleIDP-2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLInstanceEntraExampleIDP-2.png" />