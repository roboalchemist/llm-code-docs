# Source: https://docs.axonius.com/docs/example-saml-based-authentication-with-microsoft-active-directory-ad.md

# Example: SAML Based Authentication with Microsoft Active Directory (AD)

The following example describes how to enable SAML based authentication in Axonius with Microsoft Active Directory AD. The step-by-step example below uses  Windows Server 2016, but the same logic can be applied to other versions of Microsoft Active Directory (AD) as well.

<Callout icon="📘" theme="info">
  Note

  Microsoft updates their UI from time to time. The location of fields on their pages may be different than described here.
</Callout>

<br />

**To download the metadata file from the Axonius SAML instance:**

1. Configure the following settings for each SAML instance. Learn about [Using Multiple SAML Providers](/docs/saml-based-login-settings#using-multiple-saml-providers).
   * **Name of the identity provider** *(required)* - If your identity provider supports metadata URL parsing, you can use the link to automatically fill in some details. If it doesn't, fill them manually in the **Name of the identity provider** field. Note that the name of the identity provider can be any string you like; It is used only to identify the identity provider within Axonius.
   * **Unique name of IDP** *(required)* - A unique name for the identity provider that cannot be changed after it is saved. This name must be added to the SSO provider when creating the connection. The IDP name:
     * Cannot contain spaces, hyphens, or a long word.
     * Can be up to 10 characters and may contain numbers.
     * Examples: AxSSO00001, AxLogin001, AxAzure001

<Callout icon="📘" theme="info">
  IDP Note

  After configuring this option and saving, the IDP field will become inactive and cannot be changed. The option will appear in the list of available identity providers for the user. The IDP must be added to paths.
</Callout>

2. Click **Save** at the bottom of the page to save the instance.
3. Click **Download Metadata file**. The file is downloaded to your local Downloads folder.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLMetaDataFileDownload.png)

In Microsoft AD:

1. Log in to an Active Directory server as an administrator, and open the Active Directory Federation Services (AD FS) management tool. Click "Relying Party Trusts" and then "Add Relying Party Trust".

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(343).png" />

2. Select "Claims Aware" and click "Start"

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(344).png" />

3. Select "Import data about the relying party from a file" and select the metadata file. Then click "Next".

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(345).png" />

4. Specify a display name for the application and click "Next".

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(346).png" />

5. Choose an access control policy and click "Next".

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(347).png" />

6. Click "Next" and Close.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(348).png" />

7. From the list of Relying Party Trusts, select the relying party trust we just created. Make sure that it is enabled, and then right click it and select "Edit Claim Issuance Policy".

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(349).png" />

8. Click "Add Rule" and select the "Send LDAP Attributes as Claims" template, then click "Next".

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(350).png" />

9. Fill in the details to send Axonius the id, first name and last name of any user that will sign in. Then, click "Finish" and "OK".

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(351).png" />

10. Log in to Axonius as an administrator, navigate to System Setting Categories/Subcategories pane->GUI->Login, and Enable SAML based logins. Use the metadata URL for your domain:
    *https\://\[\[ADFS server name]]/FederationMetadata/2007-06/FederationMetadata.xml*