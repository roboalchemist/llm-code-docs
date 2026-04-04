# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/authentication/scim/how-to-set-up-scim-in-okta.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/authentication/scim/how-to-set-up-scim-in-okta.md

# How to set up SCIM in Okta

*SCIM provisioning is available starting in* [*Enterprise Edition*](https://www.sonarsource.com/plans-and-pricing/enterprise/)*.*

SCIM is a standard used to automate the exchange of user identity info between the identity provider and service provider. If you use Okta as an identity provider, you can enable SCIM to automate user provisioning and de-provisioning for SonarQube through Okta.

Once you enable SCIM in Okta, any user assigned to the SonarQube application in Okta is automatically provisioned in SonarQube. If a user gets unassigned from the SonarQube application or deactivated in Okta, the corresponding user account is automatically deactivated in SonarQube. However, if a user gets suspended in Okta, the corresponding user account remains unchanged in SonarQube.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

You’ve integrated Okta with SonarQube, as described on the [how-to-set-up-okta](https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/authentication/saml/how-to-set-up-okta "mention") page.

### Enabling SCIM in SonarQube <a href="#enabling-scim-in-sonarqube" id="enabling-scim-in-sonarqube"></a>

To enable SCIM provisioning in SonarQube, do one of the following:

* In your configuration file, set the `sonar.scim.enabled` server property to *`true`.*
* In the SonarQube UI, go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **SAML** and activate the **SCIM users (de)provisioning** option.

### Enabling SCIM in Okta <a href="#enabling-scim-in-okta" id="enabling-scim-in-okta"></a>

**Step 1**: From your Okta board, choose *your SonarQube application >* **General** > **App Settings** > **Edit**.

**Step 2**: Check **Enable SCIM provisioning** and click on **Save**. This will create a **Provisioning** tab.

**Step 3**: Choose the newly created **Provisioning** tab and click on **Edit.**

![Screenshot of the SCIM connection screen.](https://152261287-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBmptmznn7RpPe5u7vdup%2Fuploads%2Fgit-blob-207a9310ab6253cd3d864fd221c5ca507884793c%2F8c2b207dcbe05c836d0db919a6612bf45bf18ebd.png?alt=media)

Screenshot of the SCIM connection screen.

**Step 4**: Configure the SCIM Connection fields as follows:

* **SCIM connector base URL**: `<Your SonarQube URL>/api/scim/v2`
* **Unique identifier field for users**: *`userName`*
* **Supported provisioning actions**: enable importing new users and profile updates, pushing new users, and pushing profile updates as shown in the above picture
* **Authentication Mode**: select **Basic Auth**

**Step 5**: In SonarQube, [generating-and-using-tokens](https://docs.sonarsource.com/sonarqube-server/9.9/user-guide/user-account/generating-and-using-tokens "mention") for an admin account and copy the token into Okta’s **Basic Auth** > **Username** field.

**Step 6**: To check that the SCIM connection is valid, click on **Test Connector Configuration**. A green checkmark indicates that all the fields are properly filled.

**Step 7**: Click on **Save**.

**Step 8**: In the next screen, click **Edit** and check the **Create Users**, **Update User Attributes** and **Deactivate Users** provisioning options.

![Screenshot of the SCIM Provisioning to App page in Okta.](https://152261287-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBmptmznn7RpPe5u7vdup%2Fuploads%2Fgit-blob-88f46467771ba37bd1e263704c41e45eb98a3f36%2Fe7899126e856b0e91a50caabd1c8a0a816aa22ea.png?alt=media)

Screenshot of the SCIM Provisioning to App page in Okta.

**Step 9**: Click on **Save**.

### Provisioning already assigned users <a href="#provisioning-already-assigned-users" id="provisioning-already-assigned-users"></a>

Users that are assigned before SCIM is enabled are not automatically provisioned. In the UI, an exclamation mark is displayed next to their names in the **Assignments** tab:

![Screenshot showing the Provision User button in Okta.](https://152261287-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBmptmznn7RpPe5u7vdup%2Fuploads%2Fgit-blob-fa8d7edcc2f6c41c663d5c11de84cac446b8ca51%2Fef900448be8d85e8907c6a9b284a03c324ec79df.png?alt=media)

Screenshot showing the Provision User button in Okta.

To force the provision of these users, click on **Provision User**. The exclamation mark should disappear, meaning that the users have been provisioned.
