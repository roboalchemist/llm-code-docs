# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/setup-in-entra-id.md

# Setup in Microsoft Entra ID

This is the first step of SAML authentication setup with Microsoft Entra ID. For an overview of the complete setup, see [introduction](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/introduction "mention").

### Step 1: Create the SAML application for SonarQube Server in MS Entra ID <a href="#create-app" id="create-app"></a>

1. In **Microsoft Entra ID**, go to **Manage** > **Enterprise applications** > **All applications**.
2. Select **New application** and then **Create your own application**.

{% hint style="warning" %}
Make sure you choose "Create your own application". Do not select the non-affiliated "Sonarqube" Microsoft Entra Gallery app, which contains configurations that may prevent proper integration.
{% endhint %}

<figure><img src="broken-reference" alt="Select New application to create your own application"><figcaption></figcaption></figure>

3. Fill in the name and select the **Integrate any other application you don’t find in the gallery** option.

<figure><img src="broken-reference" alt="In the Create your own application pane, select Integrate any other application you don&#x27;t find in the gallery option"><figcaption></figcaption></figure>

4. Select **Create**.

### Step 2: Configure the application for SonarQube Server in MS Entra ID <a href="#configure-app" id="configure-app"></a>

1. Go to **Single sign-on** > **SAML**. The **Set up Single Sign-On with SAML** page opens

<figure><img src="broken-reference" alt="Select the SAML button"><figcaption></figcaption></figure>

2. In the **Basic SAML Configuration** section of the page, select **Edit**, fill in the **Identifier** and the **Reply URL** fields as described below, and save.

<details>

<summary>Basic configuration fields</summary>

<table><thead><tr><th width="106">Field</th><th>Description</th></tr></thead><tbody><tr><td>Identifier</td><td>Identifier of the SonarQube application in Entra ID.</td></tr><tr><td>Reply URL</td><td><p>Must be in the format:<br><code>&#x3C;sqServerBaseUrl>/oauth2/callback/saml</code></p><p><strong>Example</strong>: <code>https://my-sonarqube.com/oauth2/callback/saml</code></p><p><strong>Note</strong>: Make sure the server base URL is correctly set in SonarQube<sup>1)</sup>.</p></td></tr></tbody></table>

1\) See [server-base-url](https://docs.sonarsource.com/sonarqube-server/instance-administration/server-base-url "mention").

<figure><img src="broken-reference" alt="Select the Edit tool in the Basic SAML configuration section"><figcaption></figcaption></figure>

</details>

3. In the **Attributes & Claims** section of the page, configure the attributes used by SonarQube Server as described below. To add an attribute, select **Add new claim**.

<details>

<summary>Attributes &#x26; claims</summary>

The table below shows possible mappings you can use for the SAML attributes used by SonarQube Server.

<table><thead><tr><th width="173">SAML attribute used by SonarQube</th><th width="231">Description</th><th width="264">Attribute in Microsoft Entra ID</th><th>Required</th></tr></thead><tbody><tr><td>Login</td><td>A unique name to identify the user in SonarQube.</td><td>Example: <code>user.userprincipalname</code></td><td>x</td></tr><tr><td>Name</td><td>The full name of the user.</td><td>Example: <code>user.displayname</code></td><td>x</td></tr><tr><td>Email</td><td>The email of the user.</td><td>Example: <code>user.mail</code></td><td><br></td></tr></tbody></table>

{% hint style="warning" %}
The NameID attribute is not used in SonarQube Server.
{% endhint %}

<figure><img src="broken-reference" alt="Attributes &#x26; Claims section in Microsoft Entra ID"><figcaption></figcaption></figure>

</details>

4. If you use Just-in-Time provisioning with the group synchronization feature:
   1. Verify the user groups in SonarQube Server (see see *Group synchronization* in [#justintime-provisioning](https://docs.sonarsource.com/sonarqube-server/instance-administration/overview#justintime-provisioning "mention"))
   2. Add a group attribute by selecting Add a group claim and do one of the following:
      * To enable the synchronization of Active Directory (AD) groups, set **Source attribute** to **sAMAccountname**.
      * To enable the synchronization of cloud-only groups, set **Source attribute** to **Cloud-only group display names.**
      * To enable the synchronization of both AD groups and cloud-only groups, set **Source attribute** to **sAMAccountname** and select the **Emit group name for cloud-only groups** checkbox.

Once done, the option to add a group will be unavailable and the group attribute will be listed with the other attributes in the **Add new claim** tab.

<figure><img src="broken-reference" alt="Adding a group claim in Microsoft Entra ID"><figcaption></figcaption></figure>

{% hint style="warning" %}

* Group synchronization doesn’t work with Microsoft Entra ID’s nested groups.
* Microsoft Entra ID SAML tokens have a limit regarding the number of groups a user can belong to (see the description of groups in the [Claims in SAML Token](https://learn.microsoft.com/en-us/entra/identity-platform/reference-saml-tokens#claims-in-saml-tokens) table). In such cases, you might need to reduce the number of groups the user is in.
  {% endhint %}

5. Alternatively to step 4 above, you may use SCIM user and group provisioning, see [scim-provisioning-with-azure-ad](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad "mention").
6. In the **SAML Certificates** section of the page, download **Certificate (Base64)**. (You will have to copy-paste the downloaded certificate into SonarQube Server during the setup of SonarQube Server).

<figure><img src="broken-reference" alt="SAML certificates section of Microsoft Entra ID"><figcaption></figcaption></figure>

7. Assign users and groups as follows:
   1. Go to **Manage** > **Users and groups**.
   2. Select **Add user/group** to assign users or groups to the application.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [overview](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/overview "mention")
* [setup-in-sq](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/setup-in-sq "mention")
* [optional-security-features](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/optional-security-features "mention")
* [scim-provisioning-with-azure-ad](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad "mention")
