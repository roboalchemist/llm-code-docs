# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/configure-sso/generic-operation.md

# Using the setup assistant (generic operation)

The generic operation to configure SSO with SonarQube Cloud's setup assistant is as follows:

1. In SonarQube Cloud, retrieve your enterprise. See [..](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention") for more details.
2. Select **Administration** > **Single Sign-On**. The **Single Sign-On** page opens.
3. Select **Open Configuration** and then **Get Started**. The setup assistant opens.
4. Select **Custom SAML** and select **Next**.
5. Follow the steps described below.

{% hint style="info" %}

* If you use Okta, see [okta](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/configure-sso/okta "mention").&#x20;
* If you use Microsoft Entra ID, see [microsoft-entra-id](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/configure-sso/microsoft-entra-id "mention").
* The SSO setup assistant is a recent addition. If you previously configured SSO using the older method, your setup remains unaffected. However, to leverage the benefits of the new SSO setup assistant, you may delete your existing configuration and create a new one.
  {% endhint %}

### Step 1: Create the SonarQube Cloud application in your identity provider <a href="#create-application" id="create-application"></a>

1. Create the SonarQube Cloud application in your identity provider.
2. Copy the **Service Provider Identity ID** field value from the setup assistant and paste it into the corresponding field in your identity provider.
3. Copy the **Single Sign-On URL** field value from the setup assistant and paste it into the corresponding field in your identity provider.
4. In the setup assistant, select **Next** to go to the step **2. Configure Connection**.

![](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-57207a6ea125a621e9e9a6cc816accc29a971592%2Fsonarqube-cloud-sso-step2-step1.png?alt=media)

### Step 2: Configure the connection <a href="#configure-connection" id="configure-connection"></a>

The operation is different depending on whether your identity provider supports the SAML metadata URL field (URL used by SonarQube Cloud to access metadata information) or not.

<details>

<summary>Metadata URL supported</summary>

1. In your SonarQube Cloud application in your identity provider, copy the value of the field corresponding to the SAML metadata URL .
2. Paste it into the **Metadata URL** field in the **Automatic** tab of the setup assistant page.
3. In the assistant, select **Create Connection** and **Proceed.** SonarQube Cloud is trying to connect to your Identity Provider. If the connection is established, the assistant moves to step **3. Attribute Mapping**.

<div align="left"><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-430eeadfe2efa2d5e4dfaab86827d52c142666d0%2Fe6a6f5210613ce371883788e40f8b844cfa724ed.png?alt=media" alt="" width="563"></div>

</details>

<details>

<summary>Metadata URL not supported</summary>

1. In the assistant, select the **Manual** tab.
2. In your identity provider, copy the value of the SSO login URL field and paste it into **Single Sign-On Login URL** in the assistant.
3. In your identity provider, download the certificate and upload it to the assistant.
4. In the assistant, select **Create Connection** and **Proceed.** SonarQube Cloud is trying to connect to your Identity Provider. If the connection is established, the assistant moves to step **3. Attribute Mapping**.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-b26ffed730b2fc7d685387ae0cd2987929eb0c4f%2Ffadbcbba2cd5927b0ee97b1157ee44188bcb0382.png?alt=media" alt="If you’re using the Manual configuration method in Step 2 when configuring your connection using SonarQube Cloud’s setup assistant, paste the value of your SO login URL into the Single Sign-On Login URL field." width="563"><figcaption></figcaption></figure></div>

</details>

### Step 3: Set up the attributes <a href="#set-up-attributes" id="set-up-attributes"></a>

1. In your identity provider, create the attributes for name, login, email, and groups (the group attribute is used for automatic group synchronization. To do so, for each attribute, copy the attribute name from the assistant and paste it into the attribute’s name field in your identity provider.
2. In the assistant, select **Next** to go to step **4. Test SSO**.

### Step 4: Test SSO <a href="#test-sso" id="test-sso"></a>

1. Select the **Test Connection** button. The test is started and the results are displayed on the page as illustrated below.

<figure><img src="broken-reference" alt="Before you finish step 2 configuring your connection using SonarQube Cloud’s setup assistant, test and enable your configuration."><figcaption></figcaption></figure>

2. If the test was successful, select **Done**.

### Related pages <a href="#related-pages" id="related-pages"></a>

[verify-user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/verify-user-groups "mention")\
[inviting-users-to-sign-in](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/inviting-users-to-sign-in "mention")\
[terminate-setup](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/terminate-setup "mention")\
[editing-sso-configuration](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/editing-sso-configuration "mention")\
[deleting-sso-configuration](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/deleting-sso-configuration "mention")
