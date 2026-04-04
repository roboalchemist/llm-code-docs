# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/editing-configuration-old-method/okta.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/configure-sso/okta.md

# SAML SSO with Okta

To set up SAML SSO with Okta, first open the SSO setup assistant as described below:

1. Retrieve your enterprise. See [..](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention") for more details.
2. Select **Administration** > **Single Sign-On**. The **Single Sign-On** page opens.
3. Select **Open Configuration** and then **Get Started**. The setup assistant opens.
4. Select **Custom SAML**. Follow the steps described below.

### Step 1: Create the SonarQube Cloud application in Okta <a href="#create-application" id="create-application"></a>

![](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-57207a6ea125a621e9e9a6cc816accc29a971592%2Fsonarqube-cloud-sso-step2-step1.png?alt=media)

1\. In Okta, under **Applications**, select **Create App Integration**.

2\. In the **Sign-in Method** dialog, select **SAML 2.0**.

3\. Select **Create**.

4\. Fill in the fields and options as described in the table below.

<table><thead><tr><th width="186">Step</th><th width="216">Field or option</th><th>Description</th></tr></thead><tbody><tr><td><strong>General settings</strong></td><td>Application label</td><td><p>SonarQube Cloud application name.</p><p>Example**: SonarQube Cloud**.</p></td></tr><tr><td><br></td><td>Do not display application icon to users</td><td>Select this option. (This is because SonarQube Cloud doesn’t support IdP-initiated SSO).</td></tr><tr><td><strong>SAML settings</strong></td><td>Single sign on URL</td><td>Copy-paste the <strong>Single Sign-On URL</strong> field value from the setup assistant.</td></tr><tr><td><br></td><td>Audience URI (SP Entity ID)</td><td>Copy-paste the <strong>Service Provider Identity ID</strong> field value from the setup assistant.</td></tr><tr><td><br></td><td>Response</td><td>Select <strong>Signed</strong>.</td></tr><tr><td><br></td><td>Assertion Signature</td><td>Select <strong>Signed</strong>.</td></tr><tr><td><br></td><td>Signature Algorithm</td><td>Select <strong>RSA-SHA256.</strong></td></tr><tr><td><strong>SAML settings: Advanced settings</strong></td><td><br></td><td>If you want to enable assertion encryption, expand <strong>Show Advanced Settings</strong></td></tr><tr><td><br></td><td>Assertion Encryption</td><td>Select <strong>Encrypted</strong>.</td></tr><tr><td><br></td><td>Encryption Algorithm</td><td>Select <strong>AES256-GCM</strong> for high security.</td></tr><tr><td><br></td><td>Key Transport Algorithm</td><td>Select <strong>RSA-OAEP</strong>.</td></tr><tr><td><br></td><td>Encryption Certificate</td><td>The public X.509 certificate used by the identity provider to authenticate SAML messages.</td></tr></tbody></table>

5\. In the **Feedback** dialog, select **Finish** to confirm the creation of the SonarQube Cloud application.

6\. In the setup assistant, select **Next** to go to the step **2. Configure Connection**.

### Step 2: Configure the connection <a href="#configure-connection" id="configure-connection"></a>

<div align="left"><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-430eeadfe2efa2d5e4dfaab86827d52c142666d0%2Fe6a6f5210613ce371883788e40f8b844cfa724ed.png?alt=media" alt="" width="563"></div>

1. In Okta’s SonarQube Cloud application, go to **Sign On** > **Settings** > **Sign on methods**. Copy the value of the **Metadata URL** field and paste it to the **Metadata URL** field in the **Automatic** tab of the setup assistant page.
2. In the assistant, select **Create Connection** and **Proceed.** SonarQube Cloud is trying to connect to your Identity Provider. If the connection is established, the assistant moves to step **3. Attribute Mapping**.

### Step 3: Set up the attributes <a href="#set-up-attributes" id="set-up-attributes"></a>

1. In Okta’s SonarQube Cloud application, go to **Sign On** and select **Edit** in the **SAML Attributes** section.
2. Add three attribute mappings as described in the table below.
3. In **Group Attribute Statements**, enter the values for the groups attribute as described in the table below.
4. In the assistant, select **Next** to go to the step **4. Test SSO**.

<table><thead><tr><th width="126"></th><th width="154">Attribute name</th><th width="140">Name format</th><th>Value</th><th>Filter</th></tr></thead><tbody><tr><td><strong>Mapping for name</strong></td><td>Copy-paste from the assistant.</td><td>Unspecified</td><td>user.displayName</td><td><br></td></tr><tr><td><strong>Mapping for login</strong></td><td>Copy-paste from the assistant.</td><td>Unspecified</td><td>user.login</td><td><br></td></tr><tr><td><strong>Mapping for email</strong></td><td>Copy-paste from the assistant.</td><td>Unspecified</td><td>user.email</td><td><br></td></tr><tr><td><strong>Mapping for groups</strong></td><td>Copy-paste from the assistant.</td><td>Unspecified</td><td><br></td><td>Select <strong>Matches regex</strong> and set the value to <strong>.*.</strong></td></tr></tbody></table>

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-e5b3dff11b034ee62fd1c88f55fabe67aa86bd91%2F0cbe4a6b825ff45f929210640060f030cf07d46f.png?alt=media" alt="The name and group attribute statements your define in Step 3 are visible here."><figcaption></figcaption></figure></div>

### Step 4: Test SSO <a href="#test-sso" id="test-sso"></a>

1. Select the **Test Connection** button. The test is started and the results are displayed on the page as illustrated below.

<figure><img src="broken-reference" alt="Before you finish step 2 configuring your connection using SonarQube Cloud’s setup assistant, test and enable your configuration."><figcaption></figcaption></figure>

2. If the test was successful, select **Done**.

### Related pages <a href="#related-pages" id="related-pages"></a>

[verify-user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/verify-user-groups "mention")\
[inviting-users-to-sign-in](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/inviting-users-to-sign-in "mention")\
[terminate-setup](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/terminate-setup "mention")\
[deleting-sso-configuration](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/deleting-sso-configuration "mention")
