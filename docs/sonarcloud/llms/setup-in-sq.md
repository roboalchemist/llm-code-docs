# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/saml/ping-identity/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/saml/ms-entra-id/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/saml/ping-identity/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/saml/ms-entra-id/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/saml/ping-identity/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/saml/ms-entra-id/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/saml/ping-identity/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/saml/ms-entra-id/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/saml/ping-identity/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/saml/ms-entra-id/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/saml/ping-identity/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/saml/ms-entra-id/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/ping-identity/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/ms-entra-id/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/saml/ping-identity/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/saml/ms-entra-id/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/saml/ping-identity/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/saml/ms-entra-id/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ping-identity/setup-in-sq.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/setup-in-sq.md

# Setup in SonarQube Server

This is the second step of SAML authentication setup with Microsoft Entra ID. For an overview of the complete setup, see [introduction](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/introduction "mention").

Proceed as follows:

1. Open MS Entra ID to prepare the copy-paste of single-sign-on settings in SonarQube Server.
2. Configure SAML in SonarQube Server.

### Open MS Entra ID <a href="#open-entra-id" id="open-entra-id"></a>

To prepare the copy-paste of single-sign-on settings in SonarQube Server:

1. In Microsoft Entra ID, go to **Identity** > **Applications** > **Enterprise applications** > **All applications and** select the application you created for SonarQube Server.
2. On the application’s page, select **Single sign-on**. You will need to retrieve values related to sections **1**, **2**, and **4**. In section **2**, select **Edit** first to open the **Attributes & Claims** page.

<figure><img src="broken-reference" alt="Locate in MS Entra ID the field values to be copy-pasted to SonarQube"><figcaption></figcaption></figure>

### Configure SonarQube Server <a href="#configure-sq" id="configure-sq"></a>

1. Go to **Administration** > **Configuration** > **General Settings** > **Authentication> SAML**.
2. Select **Create Configuration**.

<figure><img src="broken-reference" alt="Select the Create Configuration button to create a new SonarQube configuration for SAML"><figcaption></figcaption></figure>

3. Fill in the fields as explained in the table below.

<table><thead><tr><th width="207">Field in SonarQube Server</th><th>Description</th></tr></thead><tbody><tr><td>Application ID</td><td>Value in MS Entra ID:In the <strong>Basic SAML Configuration</strong> section (<strong>1</strong>), value of the <strong>Identifier(Entity ID)</strong> field.</td></tr><tr><td>Provider ID</td><td>Value in MS Entra ID:In the <strong>Set up &#x3C;applicationForSonarQubeServer></strong> section (<strong>4</strong>), value of the <strong>Microsoft Entra ID Identifier</strong> field.</td></tr><tr><td>Provider Name</td><td>Name of the Identity Provider displayed in SonarQube Server login page when SAML authentication is active.</td></tr><tr><td>SAML Login URL</td><td>Value in MS Entra ID:In the <strong>Set up &#x3C;applicationForSonarQubeServer></strong> section (<strong>4</strong>), value of the <strong>Login URL</strong> field.</td></tr><tr><td>Identity provider certificate</td><td>Certificate downloaded from SonarQube app in Microsoft Entra ID<sup>1)</sup>.</td></tr><tr><td>SAML user login attribute</td><td><p>Value in MS Entra ID:In the <strong>Attributes &#x26; Claims</strong> section (<strong>2</strong>), select <strong>Edit</strong> and retrieve the <strong>Claim name</strong> (URL type value) of the attribute to be used for Login.</p><p>For an example, see the SonarQube Server screenshot below.</p></td></tr><tr><td>SAML user name attribute</td><td><p>Value in MS Entra ID:In the <strong>Attributes &#x26; Claims</strong> section (<strong>2</strong>), select <strong>Edit</strong> and retrieve the <strong>Claim name</strong> (URL type value) of the attribute to be used for Name.</p><p>For an example, see the SonarQube Server screenshot below.</p></td></tr><tr><td>SAML user email attribute</td><td>Optional.<br>Value in MS Entra ID:In the <strong>Attributes &#x26; Claims</strong> section (<strong>2</strong>), select <strong>Edit</strong> and retrieve the <strong>Claim name</strong> (URL type value) of the attribute to be used for email.</td></tr><tr><td>SAML group attribute</td><td>Optional (if you use the Just-in-Time provisioning’s group synchronization feature).<br>Value in MS Entra ID:In the <strong>Attributes &#x26; Claims</strong> section (<strong>2</strong>), select <strong>Edit</strong> and retrieve the <strong>Claim name</strong> (URL type value) of the <code>groups</code> attribute.</td></tr></tbody></table>

1\) See [#configure-app](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/setup-in-entra-id#configure-app "mention").

Below is a SonarQube Server screenshot with SAML attribute value examples in SonarQube.

<figure><img src="broken-reference" alt="SAML user login and name value examples in SonarQube"><figcaption></figcaption></figure>

4. Save the configuration.
5. Before enabling SAML authentication on SonarQube Server, you can verify that the configuration is correct by selecting **Test Configuration**. This will initiate a SAML login and return useful information about the SAML response obtained from the identity provider.
6. Select **Enable configuration**.
7. Check that the SonarQube Server login form now contains a SAML login button. The text highlighed in the figure below can be configured through the **Provider Name** field of the SAML configuration in SonarQube Server.

<figure><img src="broken-reference" alt="SonarQube Server login form with login button for SAML"><figcaption></figcaption></figure>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [overview](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/overview "mention")
* [setup-in-entra-id](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id "mention")
* [optional-security-features](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/optional-security-features "mention")
* [scim-provisioning-with-azure-ad](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad "mention")
