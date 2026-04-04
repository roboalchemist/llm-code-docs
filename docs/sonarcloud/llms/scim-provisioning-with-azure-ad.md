# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/scim/scim-provisioning-with-azure-ad.md

# SCIM with Microsoft Entra ID

*Automatic provisioning through SCIM is available starting in* [*Enterprise Edition*](https://www.sonarsource.com/plans-and-pricing/enterprise/)*.*

You can enable SCIM to automate user and group provisioning from Microsoft Entra ID (previously known as Azure AD) to SonarQube Server. For an overall understanding of the feature, see the [overview](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/scim/overview "mention") page.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* You have a working SAML configuration. See [introduction](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/ms-entra-id/introduction "mention").
* The connection from the Identity Provider to SonarQube must not be blocked on the network (unlike SAML, SCIM requires a direct network connection from the Identity Provider to SonarQube).

### Configuring SonarQube Server <a href="#configuring-sonarqube" id="configuring-sonarqube"></a>

1\. Within SonarQube Server, go to **Administration** > **Authentication** > **SAML**.

2\. Under **Provisioning**, click **Automatic user and group provisioning with SCIM**.

3\. Click **Save** and validate the pop-up window if you are sure you want to enable SCIM.

SCIM is now enabled in SonarQube Server, it will handle all the queries coming from Microsoft Entra ID about users and groups.

### Configuring Microsoft Entra ID <a href="#configuring-azure-a-d" id="configuring-azure-a-d"></a>

1. In Microsoft Entra ID, go to **Identity** > **Applications** > **Enterprise applications** > **All applications** and select the application created for SonarQube Server. On the application’s page, select **Provisioning**.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/GvdOHGsNtLlIq9QyCpyq/865f8aa4d8e419c405168214b487945252218717.png" alt="Select Manage > Provisioning in MS Entra ID to start the SCIM configuration"><figcaption></figcaption></figure>

2. On the **Provisioning** page, click **Get started**.
3. Under **Provisioning Mode**, select **Automatic**.
4. Configure the **Admin Credentials** section as follows:
   * **Tenant Url**: `<sqServerBaseUrl>/api/scim/v2`
   * **Secret token**: Paste a SonarQube Server's user-type token, see [managing-tokens](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-tokens "mention"), for an admin account in this field. For safety reasons, we recommend using a token from a local admin account (not managed through SCIM).

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/omDPr31IY3SccMuQ7Klu/5ffa01e41e509c222ab73436e823e2147ed19a08.png" alt="In the Provisioning page of MS Entra ID, set the automatic mode and enter the admin credentials"><figcaption></figcaption></figure>

5. Click **Test Connection** to check that your credentials are valid, then click **Save.**
6. Under **Mappings**, click on **Provision Microsoft Entra ID Groups**. This opens the **Attribute Mapping** dialog for groups.
7. Under **Target Object Actions**, make sure that **Create**, **Update**, and **Delete** are enabled.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/nF8J3Yb7vY8OEHXIlAHg/2bb7ad5fe1bfe5f2914495b5c101f5c95ccca86c.png" alt="In the Attribute mapping page of MS Entra ID, select the target object actions to confiugre SCIM"><figcaption></figcaption></figure>

8. In **Attribute Mappings**, make sure `displayName` appears in both columns of the mapping. This ensures groups are mapped based on their names.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/gFxELNXKajNEqHIB87rv/36e1fbee4765b2a714e74e4c24713be4f854ce81.png" alt="In Attribute Mappings in MS Entra ID, make sure displayName appears in both columns"><figcaption></figcaption></figure>

9. Click **Save.** This takes you back to the **Provisioning** page. If this was the default configuration, go back to the previous page.
10. Under **Mappings**, click on **Provision Microsoft Entra ID Users**. This opens the **Attribute Mapping** dialog for users.
11. Under **Target Object Actions**, make sure that **Create**, **Update,** and **Delete** are enabled.
12. In **Attribute Mappings** , map the `userName` **customappsso Attribute** (target) to the **Microsoft Entra ID Attribute** (source) used as SAML user login attribute in your SAML configuration.\
    For example, if your login attribute is `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` in your SonarQube Server’s SAML configuration and it is mapped to `user.userprincipalname` (default), use `userprincipalname` here. Otherwise, if it is mapped to `user.mail`, then use `mail` instead.

<figure><img src="broken-reference" alt="map the userName customappsso Attribute (target) to the Microsoft Entra ID Attribute (source) used as SAML user login attribute in your SAML configuration."><figcaption></figcaption></figure>

{% hint style="info" %}
To check which Microsoft Entra ID attribute is used as SAML user login attribute:

1. In SonarQube, go to **Administration** > **Authentication** > **SAML**.

2. In **SAML Configuration > SAML**, select **Edit**. The MS Entra ID attribute is the value of **SAML user login attribute**.
   {% endhint %}

3. Click **Save.** This takes you back to the **Provisioning** page.

4. In the **Settings > Scope** section, select **Sync only assigned users and groups**.

<figure><img src="broken-reference" alt="In MS Entra ID, select Sync only assigned users and groups"><figcaption></figcaption></figure>

15. Set the provisioning status to **On** and click **Save**. The Microsoft Entra ID users and groups will be synchronized with SonarQube Server.

{% hint style="info" %}
Microsoft Entra ID runs a SCIM synchronization every 40 minutes. Changes in Microsoft Entra ID are not reflected immediately in SonarQube Server.
{% endhint %}
