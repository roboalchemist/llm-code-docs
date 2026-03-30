# Source: https://docs.axonius.com/docs/zoom.md

# Zoom

Zoom is a remote conferencing service that provides video conferencing, online meetings, chat, and mobile collaboration.

## Asset Types Fetched

* Devices, Users, Licenses, Application Settings, Activities, SaaS Applications, Accounts/Tenants

## Before You Begin

### APIs

Axonius uses the following APIs:

* [Zoomrooms](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/dashboardZoomRooms)

* [List H323./SIP Devices](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/deviceList)

* [List meetings](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/dashboardMeetings)

* [List Zoom Room devices](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/listZRDevices)

* [List Users](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/users)

<Callout icon="📘" theme="info">
  **Note**

  Zoom has an API limit per day. See [Rate limits by account type](https://developers.zoom.us/docs/api/rest/rate-limits/#rate-limits-by-account-type).
</Callout>

### Create a User Account

<Callout icon="📘" theme="info">
  **Note**

  The following steps are only required to fetch Application Settings and Licenses.
</Callout>

1. From Zoom's Admiun menu, navigate to **User Management `>` Users**.
2. Click **Add Users**.

<Image alt="SaveUsers" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SaveUsers.png" />

3. Enter the email address for the new account and click **Add**.

<Image alt="Add\(1\)" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Add(1).png" />

5. Access the new email inbox you created and open the verification email from Zoom.
6. Click **Approve the Request**.

<Image alt="ApproveTheRequest" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ApproveTheRequest.png" />

7. Add a password for the new user. The password must contain at least 32 characters.
8. **Configure user permissions:**
   1. From the Admin menu, navigate to **User Management `>` Roles**.
   2. Click **Add Role**.
   3. Enter a name for the role and click **Add**.

<Image alt="AddRole2" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddRole2.png" />

9. Under **Role Settings** `>` **User and Permission Management**, mark the **View** checkbox for the following permissions:
   * Users
   * User advanced settings
   * Role management
   * Groups
   * Account profile
   * Account setting
   * Single Sign-On
   * Integration
10. From the left menu, select **Billing** and then mark the **View** checkbox for the following permissions:
    * Subscription
    * Billing information

      <Callout icon="📘" theme="info">
        **Note**

        For the full list of permissions, API endpoints and scopes required for each asset type - see [Zoom Permissions](https://docs.axonius.com/axonius-help-docs/docs/zoom-permissions).
      </Callout>
11. Click **Save Changes**.

<Image alt="RoleSettings" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RoleSettings.png" />

12. Click the **Role Members** tab.
13. Click **Add Members**.

<Image alt="AddRoleMembers" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddRoleMembers.png" />

14. Enter the email address that you created and click **Add**.

### Enable 2-Factor Authentication (2FA) With Google Authenticator

<Callout icon="📘" theme="info">
  **Note**

  This part is mandatory if your organization requires 2-Factor Authentication.
</Callout>

1. Log into the Zoom web portal as an admin (**not** the newly created user).
2. Enable 2FA (You can skip this step if 2FA is already enabled for the account/group.):
   1. Navigate to **Advanced `>` Security**.
   2. Enable **Sign in with Two-Factor Authentication**.
   3. If a verification dialog appears, click **Enable** to verify the change.
   4. Select **Enable 2FA for users that are in the specified groups**, then click the pencil icon and select the group the newly created user belongs to.
   5. Click **OK**.
3. Set up 2FA for the user account:
   1. Log into the Zoom web portal with the newly created user account.
   2. Install Google Authenticator on your phone or add a Chrome extension.
   3. Select your device type and then click **Next**. A QR code is displayed.
   4. Click **Can't scan QR Code?**
   5. Copy the **Secret key** that appears.
   6. Back in Axonius, paste the copied secret key in the **2FA Secret Key** connection field.
   7. Back in Zoom, in the wizard, click **Back**.
   8. Open the Google Authenticator (2FA app) on your mobile device.
   9. Tap the option to scan a QR code (Look for a camera or QR code icon).
   10. Scan the QR code on the Zoom web portal. The 2FA app will generate a 6-digit, one-time code.
   11. Click **Next**.

## Next Steps

1. Configure the required [permissions](https://docs.axonius.com/axonius-help-docs/docs/zoom-permissions) to connect the adapter and fetch assets.
2. [Connect Zoom in Axonius](https://docs.axonius.com/axonius-help-docs/docs/connecting-zoom-in-axonius).
3. (Optional) Configure [Advanced Settings](https://docs.axonius.com/axonius-help-docs/docs/zoom-advanced-settings).

### Related Enforcement Actions

[Zoom - Send Message](/docs/zoom-send-message)

[Zoom - Delete User](/docs/zoom-delete-user)

[Zoom - Create User](/docs/zoom-create-user)

[Zoom - Update User Group](/docs/zoom-update-user-group)