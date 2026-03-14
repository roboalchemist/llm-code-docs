# Source: https://docs.ox.security/get-started/onboarding-to-ox/connect-to-ox/sign-in-to-ox/sso-okta-express-config.md

# SSO Okta Express Config

This article describes how to set up SSO with Okta that is fast and secure. The feature includes:

* **Service Provider (SP)-Initiated Authentication (SSO) Flow:** The authentication flow occurs when the user logs in to OX.
* **Just-In-Time (JIT) Provisioning:** Users are automatically created on their first login. Email and name attributes are provisioned.
* **Universal Logout:** When enabled, Okta can terminate user sessions and tokens when risk is detected or when an admin initiates logout.

## Just-in-time (JIT) provisioning

With JIT provisioning enabled, users are automatically created in OX when they first sign in via Okta.

* When a user authenticates via Okta for the first time, a new user account is automatically created with the email and name from Okta.
* The user is granted access to OX immediately.

**Attributes Provisioned**

* Email address
* Full name

**Auto-provisioning of roles and scopes (optional)**

See steps 5 and 6.

## Prerequisites

* Okta admin rights to configure the setup.
* Contact your OX support team to discuss if this approach aligns with your use case.

## Configuration steps

* [Add the OX application in Okta](#step-1-add-the-ox-application-in-okta)
* [Express configure SSO](#step-2-express-configure-sso)
* [Enable universal logout](#step-3-enable-universal-logout)
* [Assign users and test](#step-4-assign-users-and-test)
* [Configure auto-provisioning for roles (optional)](#step-5-configure-auto-provisioning-for-roles-optional)
* [Configure auto-provisioning for scopes (optional)](#step-6-configure-auto-provisioning-for-scopes-optional)

### Step 1: Add the OX application in Okta

1. In Okta, go to **Applications > Browse App Catalog**.
2. Search for OX and click **Add Integration**.
3. Click **Done**.

### Step 2: Express configure SSO

1. In the newly created OX application, click the **Sign On** tab.
2. Click E**xpress Configure & Universal UL**.
3. Select the organization you want to set up with Okta SSO.
4. When prompted for credentials, enter the admin email and temporary password provided by OX. Alternatively, use a Google or GitHub social login.
5. In the next screen, approve the connection with OX to complete the setup.

### Step 3: Enable universal logout

1. In the **Sign On** tab of the OX application.
2. Activate the checkbox **Okta system or admin initiates logout**.

### Step 4: Assign users and test

Once OX has confirmed the setup is complete:

1. Assign the admin account to the OX application in Okta.
2. Assign any other users or groups that should have access to OX.
3. Test the login flow. Open [OX](https://www.ox.security/)and log in with the admin account.
4. You should be automatically redirected to your Okta SSO login.

### Step 5: Configure auto-provisioning for roles (optional)

Roles are provisioned in Okta.

1. In Okta, go to **Directory > Profile Editor**.
2. Search for a user of the app.
3. Set the name of the Roles variable to **userGroups**.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4e3e51952217bce261c6c71284d3f5e8862396f6%2FSSO%20Okta%20express%20config%20create%20usergroups.png?alt=media" alt=""><figcaption></figcaption></figure>
4. Select the user.
5. Click **Add Attribute** and add all the settings shown in the image.\
   ![](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-dd1e3f8c976df87c4f617d289c3b598d12033473%2FSSO%20Okta%20express%20config%20roles%20and%20scopes.png?alt=media)
6. Click **Save and Add Another**.\
   For the last user, click **Save**, not **Save and Add Another**.

### Step 6: Configure auto-provisioning for scopes (optional)

Scopes are provisioned in Okta.

1. In Okta, go to **Directory > Profile Editor**.
2. Search for a user of the app.
3. Set the name of the Scopes variable to **userScopes**.
4. Select the user.
5. Click **Add Attribute** and add all the settings shown in the image.
6. Click **Save and Add Another**.
7. For the last user, click **Save**, not **Save and Add Another**.

## Universal logout

When Universal Logout is enabled, Okta can terminate user sessions across all applications. The feature ensures that when a user is logged out of Okta, they are also logged out of OX. Universal logout is triggered when:

* An administrator initiates a logout from the Okta Admin Console.
* The Okta system detects risk and terminates sessions for security.

## Troubleshooting

If you need help, reach out to [OX support](http://support@ox.security).
