# Source: https://docs.port.io/sso-rbac/sso-providers/saml/jumpcloud.md

# JumpCloud

Follow this step-by-step guide to configure the integration between Port and JumpCloud.

info

In order to complete the process you will need to contact Port to deliver and receive information, as detailed in the guide below.

## Port-JumpCloud integration benefits â[â](#port-jumpcloud-integration-benefits- "Direct link to Port-JumpCloud integration benefits â")

* Connect to the Port application via a JumpCloud app;
* Your JumpCloud teams will be automatically synced with Port, upon user sign-in;
* Set granular permissions on Port according to your JumpCloud user groups.

## How to configure the JumpCloud app integration for Portâ[â](#how-to-configure-the-jumpcloud-app-integration-for-port "Direct link to How to configure the JumpCloud app integration for Portâ")

### Step #1: Create a new JumpCloud application[â](#step-1-create-a-new-jumpcloud-application "Direct link to Step #1: Create a new JumpCloud application")

1. In the Admin Portal, go to User Authentication -> SSO.
2. Click `Add New Application`.

![JumpCloud new application wizard](/assets/images/JumpcloudAddApplication-dc3f656615b2d7abc1a34b272070ce8c.png)

3. In the search box type **Auth0**:

![JumpCloud new application](/assets/images/JumpcloudAuth0Search-41a80deeec6818db046db5db42aca328.png)

4. Define the initial Port application settings:

   1. `Display Label`: Insert a name of your choice for the Port app, like `Port`.

   2. Add an icon (optional):

      Port Logo

      ![Port\&#39;s logo](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQwMCIgdmlld0JveD0iMCAwIDQwMCA0MDAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNzUgMjMxLjIzOEwyMDAuNTYyIDIzMS4yMzlMNzUgMTA1LjY4M1YyMzEuMjM4Wk03NSAyNzQuNzE2VjI3NUM3NSAzMDIuNjE0IDk3LjM4NTggMzI1IDEyNSAzMjVIMzI1VjEyNUMzMjUgOTcuMzg1OCAzMDIuNjE0IDc1IDI3NSA3NUgyNzQuNzI3TDI3NC43MjYgMjc0LjcxNUgyNzQuMjgyVjI3NC43MTdMNzUgMjc0LjcxNlpNMjI5Ljg5IDc1TDIyOS44OSAxOTkuMDc5TDEwNS44MDUgNzVIMjI5Ljg5WiIgZmlsbD0iYmxhY2siLz4KPC9zdmc+Cg==)

   3. **(Optional)** In the SSO tab, change the default IDP URL suffix. ![JumpCloud initial new application](/assets/images/JumpcloudNewSSO-ac0ee49e352632a7f0f1a4313cca81f3.png)

Click `activate`.

5. Click on the newly created application.

   1. Download the IDP Certificate: ![Jumpcloud download certificate](/assets/images/JumpcloudDownloadCert-ba218820909bd2e55276bb3db002c194.png)

   2. Copy the `IDP URL` from the SSO tab ![Jumpcloud IDP URL](/assets/images/JumpcloudIDPUrl-a642d0e9d888ecba1f84e884e7e21bbe.png)

6. Via chat/Slack/mail to [support.port.io](http://support.port.io/), provide Port with the downloaded `certificate.pem` file, and the copied `IDP URL`.

note

After providing the `certificate.pem` file and the the `IDP URL` to Port, you will be provided with you with your `{CONNECTION_NAME}`. Replace the following occurrences with the provided value.

tip

Most of the following steps involve editing the initial Port app you created. Keep in mind you can always go back to it by opening the admin console and going to User Authentication -> SSO, the Port app will appear in the application list.

### Step #2: Configure your JumpCloud application[â](#step-2-configure-your-jumpcloud-application "Direct link to Step #2: Configure your JumpCloud application")

In the Port app, go to the `SSO` menu and follow these steps:

1. Under `IdP Entity ID:` paste the following URL: `https://auth.getport.io`

2. Under `SP Entity ID:` set: `urn:auth0:port-prod:{CONNECTION_NAME}`.

3. Under `ACS URLs`, set: `https://auth.getport.io/login/callback?connection={CONNECTION_NAME}`

![Jumpcloud SSO configuration](/assets/images/JumpcloudConfigureSSO-e45d1f535ccf88513f138ecd2665f571.png)

Click `Save`.

### Step #3: Add user attributes to the app configuration[â](#step-3-add-user-attributes-to-the-app-configuration "Direct link to Step #3: Add user attributes to the app configuration")

The `family_name` and `given_name` attributes are required. These are used by Port to show the full name of a logged in user. To create these attributes follow these steps:

note

The `email` user attribute is created by default when creating the app. Make sure the switch next to the `email` field is set to `on`.

1. In the Port app, go to the `SSO` tab, under the **User Attribute Mapping** section:
2. Click on `add attribute`.
3. Set the `Service Provider Attribute Name` to `given_name`
4. In the `Value` field enter the value: `firstname`
5. Click on `add attribute` again.
6. Set the `Service Provider Attribute Name` to `family_name`
7. In the `Value` field enter the value: `lastname`

![JumpCloud user attributes](/assets/images/JumpcloudAttributes-176081b4fc2c06bd0c82356030ac36fd.png)

### Step #4: Add `email_verified` constant attribute to the Port App[â](#step-4-add-email_verified-constant-attribute-to-the-port-app "Direct link to step-4-add-email_verified-constant-attribute-to-the-port-app")

The use of Auth0 requires that JumpCloud passes to Port an `email_verified` field upon user login. JumpCloud does not store and expose that field by default, so in this step, you are going to configure that field and apply it to all users in your JumpCloud account.

1. In the Port app, go to the `SSO` tab, under the **Constant Attributes** section:
2. Click on `add attribute`.
3. Set the `Service Provider Attribute Name` to `email_verified`
4. In the `Value` field enter the value: `true`

![JumpCloud email verified attribute](/assets/images/JumpCloudEmailVerified-6ef653abcc670e571a3c67f523c34940.png)

note

It is also possible to manually change the value of the `email_verified` field to `true` for each user that requires access to Port in your organization. However, granting access manually to a large number of users is not scalable.

### Step #5: Exposing the application to your organization[â](#step-5-exposing-the-application-to-your-organization "Direct link to Step #5: Exposing the application to your organization")

1. In the Port app, go to the `User Groups` tab.

2. Select the user groups you want to expose the Port app to:

   ![JumpCloud add user groups](/assets/images/JumpcloudAddUserGroups-b7152102ac7060934c389f946a4991fe.png)

3. Click `Save`.

After completing these steps, users with roles that the Port app was assigned to, will see the Port app in their Portal and upon clicking it, will be logged in to Port:

![JumpCloud Portal With Port App](/assets/images/JumpcloudPortApplication-43f47b428a510e61c3a3e4ab1148ea20.png)

Direct access via URL

After configuring the SSO connection, you can initiate the login flow directly via URL.<br /><!-- -->Use the following URL based on your account region, and make sure to to replace `{CONNECTION_NAME}` with the value provided to you by Port.

* EU
* US

```
https://auth.getport.io/authorize?response_type=token&client_id=96IeqL36Q0UIBxIfV1oqOkDWU6UslfDj&connection={CONNECTION_NAME}&redirect_uri=https%3A%2F%2Fapp.getport.io
```

```
https://auth.us.getport.io/authorize?response_type=token&client_id=4lHUry3Gkds317lQ3JcgABh0JPbT3rWx&connection={CONNECTION_NAME}&redirect_uri=https%3A%2F%2Fapp.us.getport.io
```

***

## How to allow pulling JumpCloud Groups to Port[â](#how-to-allow-pulling-jumpcloud-groups-to-port "Direct link to How to allow pulling JumpCloud Groups to Port")

note

This stage is **OPTIONAL** and is required only if you wish to pull all of your JumpCloud Groups into Port inherently.

**Benefit:** managing permissions and user access on Port.<br />**Outcome:** for every user that logs in, we will automatically get their associated JumpCloud Groups, according to your definition in the settings below.

To allow automatic Groups Groups support in Port, please follow these steps:

1. In the Port app, go to the `SSO` tab, under the **Group Attributes** section

2. Check the `include group attributes` box

3. Set the group attributes' name: `memberOf`

![JumpCloud Group configuration](/assets/images/JumpcloudGroupConfig-06989d6dc45298995c58d6837f92837b.png)

4. Click `Save`.
