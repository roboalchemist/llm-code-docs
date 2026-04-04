# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/scim/scim-provisioning-with-okta.md

# SCIM with Okta

*Automatic provisioning through SCIM is available starting in* [*Enterprise Edition*](https://www.sonarsource.com/plans-and-pricing/enterprise/)*.*

You can enable SCIM to automate user and group provisioning from Okta to SonarQube Server. For an overall understanding of the feature, see the [overview](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/scim/overview "mention") page.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* You have a working SAML configuration. See [how-to-set-up-okta](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/how-to-set-up-okta "mention").
* The connection from the Identity Provider to SonarQube must not be blocked on the network (unlike SAML, SCIM requires a direct network connection from the Identity Provider to SonarQube).
* If your SonarQube Server is unaccessible over the public internet, you need to configure an [Okta On-Premises Provisioning (OPP)](https://help.okta.com/en-us/content/topics/provisioning/opp/opp-architecture.htm) agent and [SCIM connector](https://help.okta.com/en-us/content/topics/provisioning/opp/opp-create-scim-connectors.htm). The OPP agent acts as a bridge, enabling Okta to interact with your on-premise SonarQube instance via the SCIM protocol.

### Configuring SonarQube Server <a href="#configuring-sonarqube" id="configuring-sonarqube"></a>

To enable SCIM provisioning in SonarQube Server:

1\. Go to **Administration** > **Authentication** > **SAML**

2\. Select **Automatically provision user and group with SCIM** under the **Provisioning** section.

3\. Select **Save** and validate the popup if you are sure you want to enable SCIM.

SCIM is now enabled in SonarQube Server, it will handle all queries coming from Okta about users and groups.

### Configuring Okta <a href="#configuring-okta" id="configuring-okta"></a>

1. In SonarQube Server, [managing-tokens](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-tokens "mention") from an admin account. We strongly advise that the admin account used is a local one (not SCIM managed) for safety reasons. You will use this token in Step 5 below.
2. From your Okta board, choose *Your SonarQube Server application* > **General** > **App Settings** and select **Edit**.
3. Choose **SCIM** and select **Save**. This will create a new **Provisioning** tab.
4. Choose the newly created **Provisioning** tab and click on **Edit.**

<figure><img src="broken-reference" alt="In Okta, configure SCIM provisioning"><figcaption></figcaption></figure>

5. Configure the SCIM Connection fields as follows:
   * **SCIM connector base URL**: `<Your SonarQube Server URL>/api/scim/v2`
   * **Unique identifier field for users**: *`userName`*
   * **Supported provisioning actions**: enable **Push New Users**, **Push Profile Updates** and **Push Groups**, as shown in the above picture
   * **Authentication Mode**: select **HTTP Header** and copy the token generated in Step 1 into Okta’s **HTTP Header** > **Bearer** field\*\*.\*\*
6. Click **Save**. Under the **Push Groups** tab that appears, select the groups to provision to SonarQube Server. You have two options:
   1. Select them by name, one by one, by clicking **+ Push Groups** > **Find groups by name**.
   2. Create a rule to match multiple groups at once. Click **+ Push Groups** > **Find groups by rule**, give it the name and the criteria of your choice, then click **Create rule**. Note that Okta does not support regular expressions here and that matching groups are immediately provisioned when the rule is created.

<figure><img src="broken-reference" alt="Push groups by rule option in Okta for SCIM configuration"><figcaption></figcaption></figure>

<figure><img src="broken-reference" alt="Create a rule in Okta to push groups to SonarQube"><figcaption></figcaption></figure>

7. **T**o check that the SCIM connection is valid, click on **Test Connector Configuration**. A green checkmark indicates that all the fields are properly filled.
8. Click **Save**.
9. In the next screen, click **Edit** and check the **Create Users**, **Update User Attributes** and **Deactivate Users** provisioning options.

<figure><img src="broken-reference" alt="Screenshot of the SCIM Provisioning to App page in Okta."><figcaption></figcaption></figure>

10. Click **Save**. Okta users will be automatically provisioned with SonarQube Server.

Note that if a user gets suspended in Okta, the corresponding user account remains unchanged in SonarQube Server.

### Provisioning already assigned users <a href="#provisioning-already-assigned-users" id="provisioning-already-assigned-users"></a>

Users that are assigned before SCIM is enabled are not automatically provisioned. In the UI, an exclamation mark is displayed next to their names in the **Assignments** tab:

<figure><img src="broken-reference" alt="To force the provision of these users, click on Provision User."><figcaption></figcaption></figure>

To force the provision of these users, click on **Provision User**. The exclamation mark should disappear, meaning that the users have been provisioned.
