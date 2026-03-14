# Source: https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/user-provisioning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.hoppscotch.io/llms.txt
> Use this file to discover all available pages before exploring further.

# SCIM Integration for User Provisioning

> Manage users efficiently with SCIM provisioning in Hoppscotch.

User management can become overwhelming as your organization scales. **SCIM (System for Cross-domain Identity Management)** offers a standardized way to handle user provisioning, updates, and deprovisioning. With SCIM integration, Hoppscotch connects directly to your Identity Provider (IdP), helping you manage users in one place and reflect those changes across systems.

## Setting Up SCIM Provisioning

Follow the steps below to configure SCIM-based user provisioning in Hoppscotch and integrate it with your Identity Provider (IdP).

### 1. Enable SCIM in Hoppscotch

* Open the **Admin Dashboard** and navigate to the **Configurations** section.
* Find the **SCIM Provisioning** option under **User Provisioning** block and enable it.
* Copy the **SCIM Base URL (`http(s)://<backend-URL>/scim/v2`)** provided after activation, as it will be needed for the integration.

<Frame>
  <img src="https://mintcdn.com/hoppscotch/WCaaGbVhL02n1fVh/images/user-provisioning/user-provisioning.png?fit=max&auto=format&n=WCaaGbVhL02n1fVh&q=85&s=c07c6cd9cf3d52c187033d2995296c61" width="1600" height="286" data-path="images/user-provisioning/user-provisioning.png" />
</Frame>

### 2. Generate an InfraToken

* Go to the **[InfraTokens](/documentation/self-host/enterprise-edition/admin-dashboard#infra-tokens)** section of the dashboard.
* Create a new token for SCIM-related operations.
* Copy the InfraToken and store it securely, as it will be used to authenticate SCIM requests from your IdP.

<Frame>
  <img src="https://mintcdn.com/hoppscotch/WCaaGbVhL02n1fVh/images/user-provisioning/generate-infra-token.png?fit=max&auto=format&n=WCaaGbVhL02n1fVh&q=85&s=18354d2079fe3e6373cf288002e2cc87" width="1600" height="770" data-path="images/user-provisioning/generate-infra-token.png" />
</Frame>

### 3. Configure SCIM in your Identity Provider `Example: Okta`

* Log in to your [Okta](https://www.okta.com/) dashboard, select your application, and navigate to the application's settings.
* Enable SCIM provisioning under the **General** tab.

<Frame>
  <img src="https://mintcdn.com/hoppscotch/WCaaGbVhL02n1fVh/images/user-provisioning/enable-scim-provisioning.png?fit=max&auto=format&n=WCaaGbVhL02n1fVh&q=85&s=cf8723eb8c3c869476da2910d2e7803d" width="1600" height="616" data-path="images/user-provisioning/enable-scim-provisioning.png" />
</Frame>

* Go to the **Provisioning > Integration** section:
  * Paste the **SCIM Base URL** you copied from Hoppscotch.
  * Specify the unique identifier field for users (e.g., `email`) and configure provisioning actions (e.g., Import New Users, Profile Updates, Push New Users, Push Profile Updates) according to your requirements.
  * Use the `InfraToken` generated in the Hoppscotch Admin Dashboard as the **Authorization Token** and save the configuration.

<Frame>
  <img src="https://mintcdn.com/hoppscotch/WCaaGbVhL02n1fVh/images/user-provisioning/scim-integration.png?fit=max&auto=format&n=WCaaGbVhL02n1fVh&q=85&s=1c2b97428cedc416b222a08387ad60d8" width="1074" height="900" data-path="images/user-provisioning/scim-integration.png" />
</Frame>

* Under **Provisioning > To App**, enable the following actions:
  * **Create Users**
  * **Update User Attributes**
  * **Deactivate Users**
    Save the settings once done.

<Frame>
  <img src="https://mintcdn.com/hoppscotch/WCaaGbVhL02n1fVh/images/user-provisioning/provisioning-to-app.png?fit=max&auto=format&n=WCaaGbVhL02n1fVh&q=85&s=e3eaf7fae6d0c1a48092a5bfe7c40eeb" width="1224" height="900" data-path="images/user-provisioning/provisioning-to-app.png" />
</Frame>

## Add a custom attribute

SCIM supports extending the user schema to include custom fields to meet your organization's specific requirements:

* In Okta, head to **Directory > Profile Editor** and locate the SCIM application.
* Click **Add Attribute** to create a custom attribute you wish to include in the provisioning process.

<Frame>
  <img src="https://mintcdn.com/hoppscotch/WCaaGbVhL02n1fVh/images/user-provisioning/profile-editor.png?fit=max&auto=format&n=WCaaGbVhL02n1fVh&q=85&s=90927746ea020aee06756e99c09452d3" width="1603" height="904" data-path="images/user-provisioning/profile-editor.png" />
</Frame>

* Fill in the required fields and assign a valid **External namespace**. For SCIM 2.0, the following namespaces are supported in Okta:

```bash  theme={null}
# Use this for basic user attributes
urn:ietf:params:scim:schemas:core:2.0:User

# Use this for enterprise-specific user extensions
urn:ietf:params:scim:schemas:extension:enterprise:2.0:User
```

* Once finished, click **Save Attribute** to apply the changes.

<Frame>
  <img src="https://mintcdn.com/hoppscotch/WCaaGbVhL02n1fVh/images/user-provisioning/add-custom-attribute.png?fit=max&auto=format&n=WCaaGbVhL02n1fVh&q=85&s=3d8778ccf9e18c2b264ae12b33739add" width="756" height="900" data-path="images/user-provisioning/add-custom-attribute.png" />
</Frame>

The **custom attribute** will now be automatically synchronized during user creation or updates.

<Tip> Once configured, assigning a user or group to the application will trigger user creation in Hoppscotch and grant them access to your instance. If a user is unassigned, they will be removed from Hoppscotch and their access permissions will be revoked. </Tip>


Built with [Mintlify](https://mintlify.com).