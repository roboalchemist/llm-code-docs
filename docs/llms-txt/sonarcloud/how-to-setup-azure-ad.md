# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/authentication/saml/how-to-setup-azure-ad.md

# How to setup Azure AD

The following content may be useful if you’re using Azure AD as a SAML Identity Provider.

To integrate Azure AD (Identity Provider) with SonarQube (Service Provider), both sides need to be configured.

For SonarQube, navigate to **Administration** > **Authentication** > **SAML**. For Azure AD, login to Azure and navigate to Azure AD.

### Set up the SonarQube application in Azure AD <a href="#set-up-the-sonarqube-application-in-azure-a-d" id="set-up-the-sonarqube-application-in-azure-a-d"></a>

**Step 1**: In Azure AD, navigate to **Enterprise applications** and add a **New Application**.

![The Azure navigation path to create a new application for your SonarQube SAML authentication.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-9dd5df136b073091f79ad9eea24dc5e436473148%2F0442d5ccf1d5592da829c4c65516103840758903.jpg?alt=media)

The Azure navigation path to create a new application for your SonarQube SAML authentication.

**Step 2**: Create your **own application** and fill in the **name**.

![Create a new Enterprise application for SonarQube when setting up SAML authentication in Azure.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-a9f7ba0fcb004301443a89b0611f2d2ff43a2899%2F68875a89673874289ea23e34d9fe913bcba11f70.jpg?alt=media)

Create a new Enterprise application for SonarQube when setting up SAML authentication in Azure.

### Link SonarQube with Azure AD <a href="#link-sonarqube-with-azure-a-d" id="link-sonarqube-with-azure-a-d"></a>

**Step 1**: Navigate to **Single sign-on** and select **SAML**.

![Navigate to Single sign-on in Azure and select SAML to begin the authentication process.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-a05186f1c570693e3964e64ec51c9617f7f3e375%2Fb54f564840c2fbc85bdfb639a4da26dac05463a1.jpg?alt=media)

Navigate to Single sign-on in Azure and select SAML to begin the authentication process.

**Step 2**: Edit the **Basic SAML Configuration** and fill in the **Identifier** and the **Reply URL** fields. The **Identifier** has to be the same as the **Application ID** in SonarQube. The **Reply URL** must have the format `<Your SonarQube URL>/oauth2/callback/saml`. The **Reply URL** uses the **Server base URL** provided in SonarQube under **Administration** > **General**.

![When setting up your SSO with SAML, edit the Basic SAML Configuration and fill in the Identifier and the Reply URL.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-ade8c11e8ebafaf001c03daa41496ce53adc6d00%2F7e6ac22a4d6017820e49d0ab2e5f868a9de06a7a.jpg?alt=media)

When setting up your SSO with SAML, edit the Basic SAML Configuration and fill in the Identifier and the Reply URL.

**Step 3**: Make sure that the **Application ID** in SonarQube has the same value as the **Identifier** in the Identity Provider.

![Confirm that the Application ID in SonarQube has the same value as the Identifier in the Identity provider.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-80a56ac95908dd78834c01d8a5df0d6e5e2960ba%2Fba2f3ef2088652821317cac2fdaf635739a35560.png?alt=media)

Confirm that the Application ID in SonarQube has the same value as the Identifier in the Identity provider.

**Step 4**: In the Azure AD SAML configuration, navigate to **Set up** and copy the **Login URL** and **Azure AD Identifier**.

![In the Azure AD SAML configuration, navigate to Set up and copy the Login URL and Azure AD Identifier.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-ecbbd3cf38090a6b788095f8b84d5a1325788f3e%2F9cde44170aa628f2b307e40bf8f1b93d160491fa.jpg?alt=media)

In the Azure AD SAML configuration, navigate to Set up and copy the Login URL and Azure AD Identifier.

**Step 5**: Paste the **Login URL** into the **SAML login url** and the **Azure AD Identifier** into the **Provider ID** field in the SonarQube SAML configuration.

![Paste the Azure AD Identifier into the Provider ID field and the Login URL into the SAML login url into your SonarQube SAML configuration.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-e901735d5cc3a5e483d9b96ff0489ccf51d5c368%2F0221f48586d7f3cfcc8901eede418f8ecbee2d7e.png?alt=media)

Paste the Azure AD Identifier into the Provider ID field and the Login URL into the SAML login url into your SonarQube SAML configuration.

### Attributes and claims <a href="#attributes-and-claims" id="attributes-and-claims"></a>

**Step 1**: In the Azure AD SAML configuration, edit **Attributes & Claims** to view, edit or add attributes.

![Edit Attributes & Claims to view, edit or add attributes when configuring SAML authentication in Azure.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-f771cbab78be0406f3abcb9e807c6d99e6901695%2Fc96c8e9821d77b29ff74b690b6988d1a93789db2.jpg?alt=media)

Edit Attributes & Claims to view, edit or add attributes when configuring SAML authentication in Azure.

SonarQube uses the following attributes:

* * **Login** (required) A unique name to identify the user in SonarQube. The default Azure AD attribute `emailaddress` is used in the example.
  * **Name** (required) The full name of the user. The default Azure AD attribute `givenname` is used in the example.
  * **Email** (optional) The email of the user.
  * **Group** (optional) Supports mapping to group names in SonarQube. Group name passed by Azure AD and the group name in SonarQube should match. Otherwise, the default **sonar-users** group is assigned.

{% hint style="warning" %}
The **NameID** attribute is *not* used in SonarQube.
{% endhint %}

**Step 2**: Corresponding configuration in SonarQube. The namespace + name of the attribute should be used, as defined in Azure AD.

![The corresponding configuration in SonarQube uses the Azure namespace + name of the attribute to be used.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-de8fced6f0907082813307f766dcf89fc19147aa%2Fdf3b35e6d38519ae6cac9aca777ed529296a7a44.png?alt=media)

The corresponding configuration in SonarQube uses the Azure namespace + name of the attribute to be used.

### Certificates and signatures <a href="#certificates-and-signatures" id="certificates-and-signatures"></a>

**Step 1**: Navigate to **SAML Certificates** and download **Certificate (Base64)**.

![Navigate to SAML Certificates and download Certificate (Base64).](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-ce874c3ef7286b3d085877aaee92420a857a48cb%2F78ccd1e191d4de389eda46304f29d71152c51c37.jpg?alt=media)

Navigate to SAML Certificates and download Certificate (Base64).

**Step 2**: The certificate should be copied into the **Identity provider certificate** field in the SonarQube SAML configuration.

**Step 3** (Optional): Encryption for SonarQube requests can be activated by generating an asymmetric key pair. (For more information, see [SAML token encryption in Azure](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/howto-saml-token-encryption?tabs=azure-portal)) Add the private key in SonarQube.

![Copied the Service provider private key field value to add to your SonarQube SAML configuration.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-4e2f19d83e699015c4903b51571500c3ab92f7b2%2Fbbb845b7f8b410267fda9b276065c0f51a09953e.png?alt=media)

Copied the Service provider private key field value to add to your SonarQube SAML configuration.

Import the public key certificate (.cer) file in Azure AD and activate token encryption.

![Import the public key certificate (.cer) file in Azure AD and activate token encryption for your SonarQube SAML authentication.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-63973e34a5866ea73a08e1e0416ceb96d5f8a46d%2F28b3585fe9f3b34530e30da26a7ddc91f585283c.jpg?alt=media)

Import the public key certificate (.cer) file in Azure AD and activate token encryption for your SonarQube SAML authentication.

**Step 4** (Optional): Azure AD supports signed SAML requests from the Service Provider (under Preview). Edit the **Verification certificates**, upload a certificate, and enable the **Require verification certificates** option.

![To edit the Verification certificates, upload a certificate and enable the Require verification certificates option.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-7eb911f5cacfdc439f0fa4a6da961948b70a61fe%2Fe2dfee6ddbc543cf00f2f96964081201ac2d7291.jpg?alt=media)

To edit the Verification certificates, upload a certificate and enable the Require verification certificates option.

In SonarQube, fill in the corresponding private key and the same certificate and enable the **Sign requests** option.

![In SonarQube, fill in the corresponding private key and the same certificate and enable the Sign requests option.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-39455bd6c250c215cf4c95d108d3f1f96ecbdab1%2F3ae81f5b6aff4e7b3a22782d47a983a354c94007.png?alt=media)

In SonarQube, fill in the corresponding private key and the same certificate and enable the Sign requests option.

### Users and groups <a href="#users-and-groups" id="users-and-groups"></a>

**Step 1**: In the Azure AD SonarQube application, navigate to **Users and groups** and assign users or groups to the application.

![Add SonarQube users and groups when setting up your SAML authentication in Azure.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-7ef7eeedf89a18d560c7cadc3628258633484c83%2F06776c1846e0c614dd4bb6675afaeb3860631304.jpg?alt=media)

Add SonarQube users and groups when setting up your SAML authentication in Azure.

### Group mapping <a href="#group-mapping" id="group-mapping"></a>

Group mapping between Azure AD and SonarQube can be achieved either by using the Azure AD roles or the Azure AD groups. For either case, the corresponding group name should exist in SonarQube under **Administration** > **Security** > **Groups**. (For more information, see [security](https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/security "mention"))

* For mapping with the Azure AD groups, a group claim must be added with `sAMAccountName` as a source attribute.

{% hint style="warning" %}
According to Azure, this source attribute only works for groups synchronized from an on-premises Active Directory using AAD Connect Sync 1.2.70.0 or above.
{% endhint %}

![Where to map your SAML groups in Azure before you can add a group claim.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-da147a659b0550a0cde49f68f25d9fe24aca8953%2Fbe930f289f0342655a25a2bcfd1a76c7ec83ef62.jpg?alt=media)

Where to map your SAML groups in Azure before you can add a group claim.

![The attribute used to define your user group in SAML.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-250d19c34bab3e4f24ffc51b48b8c8b72aae3712%2Feb04ff7497cbdc1bfb6aa22b8b85e2aa08f65215.png?alt=media)

The attribute used to define your user group in SAML.

* For mapping with the Azure AD app roles, an application role should be assigned to the user. Azure AD sends the role claim automatically with `http://schemas.microsoft.com/ws/2008/06/identity/claims/role` as a key.

![The attribute used to define your user group role in SAML.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-c6d9a9240551c4ae0b392f2857f21d584f184d6e%2F874c3e2c2bf8fcd8b20648f42ca9a4b4fa099b99.png?alt=media)

The attribute used to define your user group role in SAML.

### Enabling and testing SAML authentication <a href="#enabling-and-testing-saml-authentication" id="enabling-and-testing-saml-authentication"></a>

**Step 1**: In the SonarQube SAML settings, enable SAML.

![Where to enable SAML for Azure from the SonarQube SAML settings.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-2f6fd7c80cd352b335b0a878c07e122c773da823%2F7e4a291670d29d60202f3df8fedaf13b5f687795.png?alt=media)

Where to enable SAML for Azure from the SonarQube SAML settings.

**Step 2**: In the login form, the new button **Log in with SAML** (or a custom name specified in the `sonar.auth.saml.providerName` setting) allows users to connect with their SAML account.

![Log in to SonarQube with your SAML authentication.](https://739659627-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwuQmJTVPOsx7zNT5Aqwl%2Fuploads%2Fgit-blob-14a05f1527aed807b8089c8cc89ccabe5e908984%2Fdff2e7de8ec99f51368ca08903761820d9319adb.png?alt=media)

Log in to SonarQube with your SAML authentication.

Before enabling the SAML authentication on SonarQube, you can verify that the configuration is correct by clicking on **Test Configuration**. A SAML login will be initiated and useful information about the SAML response obtained from the Identity provider will be returned.
