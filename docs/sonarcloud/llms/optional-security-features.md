# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/saml/ping-identity/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/saml/ms-entra-id/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/saml/ping-identity/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/saml/ms-entra-id/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/saml/ping-identity/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/saml/ms-entra-id/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/saml/ping-identity/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/saml/ms-entra-id/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/saml/ping-identity/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/saml/ms-entra-id/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/saml/ping-identity/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/saml/ms-entra-id/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/ping-identity/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/ms-entra-id/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/saml/ping-identity/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/saml/ms-entra-id/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/saml/ping-identity/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/saml/ms-entra-id/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ping-identity/optional-security-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/optional-security-features.md

# Setup of security features

Once you have registered SonarQube Server in Microsoft Entra ID (see [setup-in-entra-id](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id "mention")), you can set up the following security features:

* The encryption of SAML assertions emitted by Microsoft Entra ID for SonarQube Server. For more information, see [SAML token encryption in Entra ID](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/howto-saml-token-encryption?tabs=azure-portal).
* The signing of the SAML requests from SonarQube Server to Entra ID. For more information, see [Enforce signed SAML authentication requests](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/howto-enforce-signed-saml-authentication).

{% hint style="info" %}
The same key pair is used for both security features (encryption and signing).
{% endhint %}

### Step 1: Generate the asymmetric key pair and certificate <a href="#generate-keys-and-certificate" id="generate-keys-and-certificate"></a>

Generate the asymmetric key pair to use for encryption (PKCS8). The public key should be stored in an X.509 certificate file in `.cer` format. You can copy the contents of the certificate file to a text editor and save it as a `.cer` file. The certificate file should contain only the public key, not the private key.

### Step 2: Configure the security feature(s) in Microsoft Entra ID <a href="#configure-in-pid" id="configure-in-pid"></a>

<details>

<summary>To enable the encryption of SAML assertions</summary>

Add the certificate to the Microsoft Entra ID application you created for SonarQube Server:

1. Go to **Identity** > **Applications** > **Enterprise applications** > **All applications** and select the application for SonarQube Server.
2. On the application’s page, select **Token encryption**.
3. On the Token encryption page, select **Import Certificate** to import the `.cer` file that contains your public X.509 certificate.
4. Once the certificate is imported, activate encryption by selecting the three dots next to the thumbprint status and then selecting **Activate token encryption**.

<figure><img src="broken-reference" alt="Activate encryption in Microsoft Entra ID"><figcaption></figcaption></figure>

5. Select **Yes** to confirm activation of the token encryption certificate.
6. Confirm that the SAML assertions emitted for the application are encrypted.
7. Enforce the response signature: see below.

</details>

<details>

<summary>If you use encryption, enforce response signature</summary>

1. In Microsoft Entra ID, go to **Identity** > **Applications** > **Enterprise applications** > **All applications** and select the application for SonarQube Server.
2. On the application’s page, select **Single sign-on**.
3. In **SAML Certificates** > **Token signing certificates**, select **Edit**. The **SAML Signing Certificate** dialog opens.
4. In **Signing option**, enforce the response signature. It means, select either the **Sign SAML Response** or **Sign SAML response and assertion** option.
5. Save.

<figure><img src="broken-reference" alt="In Signing Option, don&#x27;t select Sign SAML assertion"><figcaption></figcaption></figure>

</details>

<details>

<summary>To enable the signing verification</summary>

1. In Microsoft Entra ID, go to **Identity** > **Applications** > **Enterprise applications** > **All applications** and select the application for SonarQube Server.
2. On the application’s page, select **Single sign-on**.
3. In **SAML Certificates > Verification certificates**, select **Edit**.
4. Go to **Identity** > **Applications** > **Enterprise applications** > **All applications** and select the application for SonarQube Server.
5. Select **Require verification certificates**.
6. Upload the public key certificate.
7. Save. The **Verification certificates** section shows **1** active certificate.

<figure><img src="broken-reference" alt="Check the active certificate"><figcaption></figcaption></figure>

</details>

### Step 3: Configure the security feature(s) in SonarQube Server <a href="#configure-in-sq" id="configure-in-sq"></a>

To configure the resquest signing and/or the assertion decryption in SonarQube Server:

1. Go to **Administration** > **Configuration** > **General Settings** > **Authentication > SAML**.
2. In **SAML Configuration** > **SAML**, select **Edit**. The **Edit SAML configuration** dialog opens.
3. Copy the PKCS8 private key file contents.
4. Paste it in **Service provider private key.**
5. Copy the self-signed certificate contents.
6. Paste it in **Service provider certificate.**
7. To enable the signing of the SAML requests, select in addition the **Sign requests** option.
8. Select **Save configuration**.
9. Select **Test Configuration**.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [overview](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/overview "mention")
* [setup-in-entra-id](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id "mention")
* [setup-in-sq](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/setup-in-sq "mention")
* [scim-provisioning-with-azure-ad](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad "mention")
