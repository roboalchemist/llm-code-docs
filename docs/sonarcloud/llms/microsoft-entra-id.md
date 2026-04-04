# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/editing-configuration-old-method/microsoft-entra-id.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/configure-sso/microsoft-entra-id.md

# SAML SSO with Entra ID

To set up SAML SSO with Microsoft Entra ID, first open the SSO setup assistant as described below:

1. Retrieve your enterprise. See [..](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention") for more details.
2. Select **Administration** > **Single Sign-On**. The **Single Sign-On** page opens.
3. Select **Open Configuration** and then **Get started**. The setup assistant opens.
4. Select **Custom SAML**.
5. Follow the steps described below.

{% hint style="warning" %}

* Group synchronization doesn’t work with Microsoft Entra ID’s nested groups.
* Microsoft Entra ID’s SAML tokens have a limit regarding the number of groups a user can belong to (see the description of groups in the [Claims in SAML Token](https://learn.microsoft.com/en-us/entra/identity-platform/reference-saml-tokens#claims-in-saml-tokens) table). In such cases, you might need to reduce the number of groups the user is in.
  {% endhint %}

### Step 1: Create the SonarQube Cloud application in Microsoft Entra ID <a href="#create-application" id="create-application"></a>

![](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-57207a6ea125a621e9e9a6cc816accc29a971592%2Fsonarqube-cloud-sso-step2-step1.png?alt=media)

1\. In Microsoft Entra ID, go to **Applications** > **Enterprise applications** > **All applications**.

2\. Select **New application** and then **Create your own application**.

{% hint style="warning" %}
Make sure you choose **Create your own application**. Do not select the non-affiliated **Sonarqube** Microsoft Entra Gallery app, which contains configurations that may prevent proper integration.
{% endhint %}

3\. Fill in the name and select the **Integrate any other application you don’t find in the gallery** option.

4\. Select **Create**.

5\. From the **Manage** section of the SonarQube Cloud application, go to **Single sign-on** > **SAML**.

6\. In the **Basic SAML Configuration** section, select **Edit,** fill in the **Identifier** and the **Reply URL** fields as described below, and save.

<details>

<summary>Identifier and Reply URL fields</summary>

<table><thead><tr><th width="153">Field</th><th>Description</th></tr></thead><tbody><tr><td>Identifier</td><td>Copy-paste the <strong>Service Provider Identity ID</strong> field value from the setup assistant.</td></tr><tr><td>Reply URL</td><td>Copy-paste the <strong>Single Sign-On URL</strong> field value from the setup assistant.</td></tr></tbody></table>

</details>

5\. In the setup assistant, select **Next** to go to the step **2. Configure Connection**.

### Step 2: Configure the connection <a href="#configure-connection" id="configure-connection"></a>

<div align="left"><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-430eeadfe2efa2d5e4dfaab86827d52c142666d0%2Fe6a6f5210613ce371883788e40f8b844cfa724ed.png?alt=media" alt="" width="563"></div>

1. In your SonarQube Cloud application in Microsoft Entra ID, go to **SAML Certificates**. Copy the value of the **App Federation Metadata Url** field and paste it into the **Metadata URL** field in the **Automatic** tab of the setup assistant page.
2. In the assistant, select **Create Connection** and **Proceed.** SonarQube Cloud is trying to connect to your Identity Provider. If the connection is established, the assistant moves to step **3. Attribute Mapping**.

### Step 3: Set up the attributes <a href="#set-up-attributes" id="set-up-attributes"></a>

1\. In the **Attributes & Claims** section of your SonarQube Cloud application in Microsoft Entra ID, configure the attributes used by SonarQube Cloud as described below. To add an attribute, select **Add new claim**.

<details>

<summary>Attributes</summary>

<table><thead><tr><th width="135"></th><th width="146">Attribute name</th><th width="169">Source attribute</th><th>Description</th></tr></thead><tbody><tr><td><strong>Mapping for name</strong></td><td>Copy-paste from the assistant.</td><td><code>givenname</code> or your own user name attribute</td><td><p>The full name of the user.</p><p>The default list of attributes includes <code>givenname</code> (first name) and <code>surname</code> (last name). If you prefer to show the full name, you must create a new claim in MS Entra ID.</p></td></tr><tr><td><strong>Mapping for login</strong></td><td>Copy-paste from the assistant.</td><td><code>userprincipalname</code></td><td>A unique name to identify the user in SonarQube Cloud.</td></tr><tr><td><strong>Mapping for email</strong></td><td>Copy-paste from the assistant.</td><td><code>mail</code></td><td>The email of the user.</td></tr></tbody></table>

</details>

2\. Select **Add a group claim**, and configure the group attribute as described below. Once done, the option to add a group will be unavailable and the group attribute will be listed with the other attributes in the **Add new claim** tab.

<details>

<summary>Group attribute</summary>

The group attribute is used for automatic group synchronization.

<table><thead><tr><th width="182">Parameter or option</th><th>Value</th></tr></thead><tbody><tr><td><strong>Group Claims</strong></td><td><strong>Groups assigned to the application</strong></td></tr><tr><td><strong>Source attribute</strong></td><td><strong>Cloud-only group display names</strong> or (if using on-prem Active Directory for group synchronisation) <strong>sAMAccountName</strong></td></tr><tr><td><strong>Emit group name for cloud-only groups</strong></td><td><p>• If using sAMAccountName: select the option</p><p>• Otherwise: ignore the option</p></td></tr></tbody></table>

</details>

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-747dd324ceb13b4f51307bb67c03285719164df3%2Fsonarqube-cloud-ms-entra-id-attributes-claims__Cs0040.png?alt=media" alt="When you add your new group claims, they will appear on the Microsoft Azure Attributes &#x26; Claims page." width="563"><figcaption></figcaption></figure></div>

3\. In the assistant, select **Next** to go to the step **4. Test SSO**.

### Step 4: Test SSO <a href="#test-sso" id="test-sso"></a>

1. Select the **Test Connection** button. The test is started and the results are displayed on the page as illustrated below.

<figure><img src="broken-reference" alt="Before you finish step 2 configuring your connection using SonarQube Cloud’s setup assistant, test and enable your configuration."><figcaption></figcaption></figure>

2. If the test was successful, select **Done**.

### Related pages <a href="#related-pages" id="related-pages"></a>

[verify-user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/verify-user-groups "mention")\
[inviting-users-to-sign-in](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/inviting-users-to-sign-in "mention")\
[terminate-setup](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/terminate-setup "mention")\
[deleting-sso-configuration](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/deleting-sso-configuration "mention")
