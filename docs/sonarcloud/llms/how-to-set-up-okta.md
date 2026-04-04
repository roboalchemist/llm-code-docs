# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/saml/how-to-set-up-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/how-to-set-up-okta.md

# With Okta

Note that Okta does not support service provider-signed requests even if they are enabled on the SonarQube Server side.

To integrate Okta (identity provider) with SonarQube Server (service provider), both sides need to be configured.

{% hint style="warning" %}
Make sure the SonarQube Server URL is correctly set in SonarQube Server. See [server-base-url](https://docs.sonarsource.com/sonarqube-server/instance-administration/server-base-url "mention") for more details.
{% endhint %}

### Create a new application in the Okta admin dashboard <a href="#create-a-new-application-in-the-okta-admin-dashboard" id="create-a-new-application-in-the-okta-admin-dashboard"></a>

1. Under **Applications**, select **Create App Integration**.

<figure><img src="broken-reference" alt="Create your first app integration in Okta for SonarQube."><figcaption></figcaption></figure>

2. Choose **SAML 2.0** in the **Sign-in Method** dialog.
3. Under **General Settings**, fill in the **App name** with *SonarQube* (or another name that you prefer), and select **Do not display application icon to users**.

<figure><img src="broken-reference" alt="Enter in App name with SonarQube, and select Do not display application icon to users."><figcaption></figcaption></figure>

#### Configure SAML settings <a href="#configure-saml-settings" id="configure-saml-settings"></a>

1. Under **General Settings**, configure the following fields:
   * **Single sign on URL**: `<Your SonarQube Server URL>/oauth2/callback/saml` (e.g., `https://sonarqube.mycompany.com/oauth2/callback/saml`).
   * **Audience URI (SP Entity ID)**: Something like `sonarqube` (SonarQube Server default value). It must not contain whitespace.

<figure><img src="broken-reference" alt="Configure SonarQube’s SAML single sign on (SSO) setting in Okta."><figcaption></figcaption></figure>

2. An assertion signature is mandatory. You must keep the following default settings in *Show Advanced Settings*:
   * **Response**: Choose *Signed*.
   * **Assertion Signature**: Choose *Signed*.
   * **Signature Algorithm**: Choose *RSA-SHA256*.
3. (Optional) If you want to enable assertion encryption, expand *Show Advanced Settings* and configure the following fields:
   * **Assertion Encryption**: Choose *Encrypted*.
   * **Encryption Algorithm**: Choose *AES256-GCM* for high security.
   * **Key Transport Algorithm**: Choose *RSA-OAEP*.
   * **Encryption Certificate**: Add the service provider certificate. It should be the same certificate as the one found in the SonarQube Server SAML settings under **Service provider certificate**.

<figure><img src="broken-reference" alt="Show Advanced Settings and configure the fields to enable assertion encryption."><figcaption></figcaption></figure>

4. Under **Attribute Statements**, add the following attribute mappings:
   1. Create a mapping for the *name*:
      * **Name**: `name`.
      * **Name format**: *Unspecified*.
      * **Value**: Choose `user.displayName`.
   2. Create a mapping for the *login*:
      * **Name**: `login`.
      * **Name format**: *Unspecified*.
      * **Value**: Choose `user.login`.
   3. (Optional) Create a mapping for the *email*:
      * **Name**: `email`.
      * **Name format**: *Unspecified*.
      * **Value**: Choose `user.email`.

<figure><img src="broken-reference" alt="Attributes statement in Okta"><figcaption></figcaption></figure>

d. (Optional) Under *Group Attribute Statements* (See details in [overview](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/overview "mention")):

* **Name**: `groups`.
* **Name format**: *Unspecified*.
* **Filter**: Choose *Matches regex* and set the value to `.*`.

<figure><img src="broken-reference" alt="Where to define your optional SonarQube group attributes in Okta."><figcaption></figcaption></figure>

5. Select **Finish** in the **Feedback** dialog to confirm the creation of the application.
6. You can now add users and groups in the *Assignments* tab of the application.

<figure><img src="broken-reference" alt="Where you assign SonarQube users in Okta."><figcaption></figcaption></figure>

7. Navigate to the **Sign On** tab of the *SonarQube* application in Okta.

<figure><img src="broken-reference" alt="Navigate to the Sign On tab of the SonarQube application in Okta."><figcaption></figcaption></figure>

8. Next to the **SAML Signing Certificates** subsection, you will find the configurations needed for setting up SonarQube Server, under **View SAML setup instructions**.

<figure><img src="broken-reference" alt="Where you can find SAML setup instructions in Okta."><figcaption></figcaption></figure>

### In SonarQube Server, Configure SAML authentication <a href="#in-sonarqube-configure-saml-authentication" id="in-sonarqube-configure-saml-authentication"></a>

1. Go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **SAML.**
2. Select **Create configuration.** A dialog opens.
3. Provide the fields below:
   * **Application ID**: The value of the *Audience URI (SP Entity ID)* you set in Okta (for example, `sonarqube`).
   * **Provider ID**: The value of *Identity Provider Issuer* provided in **View SAML setup instructions** from Okta.
   * **SAML login URL**: The value of *Identity Provider Single Sign-On URL* provided in **View SAML setup instructions** from Okta.
   * **Identity provider certificate**: The value of *X.509 Certificate* provided in **View SAML setup instructions** from Okta.
   * **SAML user login attribute**: `login` (or whatever you configured above when doing the mapping).
   * **SAML user name attribute**: `name` (or whatever you configured above when doing the mapping).
   * (Optional) **SAML user email attribute**: `email` (or whatever you configured above when doing the mapping).
   * **Sign requests**: Not supported for Okta.
   * (Optional) **Service provider private key**: The private key is required for assertion encryption support. It must be provided for SonarQube Server in `PKCS8` format without encryption. You can find instructions for converting to different key formats [here](https://manpages.ubuntu.com/manpages/focal/man1/pkcs8.1ssl.html).
   * (Optional) **Service provider certificate**: The certificate is required for assertion encryption support. It must be shared with Okta in order to activate the assertion encryption.

The service provider private key and certificate can be either a new self-signed pair or any existing pair available in your infrastructure.

### Enabling and testing SAML authentication <a href="#enabling-and-testing-saml-authentication" id="enabling-and-testing-saml-authentication"></a>

1. Save the SAML configuration by selecting **Save configuration.**
2. Before enabling the SAML authentication on SonarQube Server, you can verify that the configuration is correct by clicking on **Test Configuration**. A SAML login will be initiated and useful information about the SAML response obtained from the Identity provider will be returned.
3. Enable the configuration by selecting **Enable configuration**.
4. In the login form, the new button **Log in with Okta** (or a custom name specified in the **Provider Name** field) allows users to connect with their SAML account.

<div align="left"><figure><img src="broken-reference" alt="Log in with Okta button that appears in the user login form"><figcaption></figcaption></figure></div>

### Group synchronization <a href="#group-synchronization" id="group-synchronization"></a>

To use the Just-in-Time provisioning's group synchronization feature:

1. Verify the user groups in SonarQube Server so that the automatic group synchronization can take place properly. See [#justintime-provisioning](https://docs.sonarsource.com/sonarqube-server/instance-administration/overview#justintime-provisioning "mention").
2. Make sure you have configured a `groups` attribute in your Okta application (see above).
3. Enable the group synchronization in SonarQube Server:
   * Go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **SAML**.
   * Select the **Edit** button to open your SAML Okta configuration.
   * In **SAML group attribute,** enter `groups`, or the name you gave to this attribute in your Okta Application.
   * Select **Save configuration**.

### Enabling SCIM provisioning <a href="#enabling-scim-provisioning" id="enabling-scim-provisioning"></a>

Starting in [Enterprise edition](https://www.sonarsource.com/plans-and-pricing/enterprise/), once you’ve set up Okta as your SAML Identity Provider, you can set up SCIM provisioning to automate user and group provisioning within Okta.

For more information, see [scim-provisioning-with-okta](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/scim/scim-provisioning-with-okta "mention").
