# Source: https://www.courier.com/docs/platform/workspaces/okta-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Okta Integration

> Set up Okta SSO and SCIM provisioning with Courier to enable secure logins, role management, and automated user syncing via SAML 2.0 and Okta’s admin interface.

## Prerequisites

* An Okta account with Admin privileges.
* Each user must be invited to Courier via email before they can log in with Okta.
* Some steps require information exchanged with Courier. Before continuing, contact [Courier Support](mailto:support@courier.com) for assistance setting up Okta sign-in.

## Create the App Integration in Okta

1. Navigate to the Applications > Applications section of the Okta admin panel
2. Hit the "Create App Integration Button":

<Frame caption="Create App Integration button">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/create-app.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=c8484a7163f4809bc343e66558e6d2cc" alt="Create App Integration button." width="2880" height="1548" data-path="assets/platform/workspaces/create-app.png" />
</Frame>

3. Select SAML 2.0 and hit "Next"

<Frame caption="Select Sign-in Method">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/saml.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=f1e244045ed6059627a7751f417098fb" alt="Select Sign-in Method" width="2880" height="1546" data-path="assets/platform/workspaces/saml.png" />
</Frame>

4. Enter `Courier` as the app name and optionally provide the Courier logo (available after the screenshot) then click "Next"

<Frame caption="App Name & Logo">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/general-settings.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=bc1fd9044a397a9d24aa2bedb7830dc9" alt="App Name & Logo" width="2880" height="1548" data-path="assets/platform/workspaces/general-settings.png" />
</Frame>

<Note>
  You can optionally upload the Courier logo. Download it here:

  <div class="button-group">
    <a class="button button--primary" href="pathname:///img/logo_2023.png" download="courier_logo">Download PNG</a>
  </div>
</Note>

5. Contact Courier support for a `Single sign on URL` and an `Audience URI`. Enter them in their respective fields under SAML settings.

<Frame caption="SSO URL and Audience URI fields">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/settings-urls.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=2d84e9d2dad66df55f14c9564482008a" alt="SSO URL and Audience URI fields" width="2880" height="1548" data-path="assets/platform/workspaces/settings-urls.png" />
</Frame>

6. In the **Attribute Statements** section, enter the following information:

| Name                                                                 | Name Format | Value      |
| -------------------------------------------------------------------- | ----------- | ---------- |
| `id`                                                                 | Unspecified | user.id    |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` | Unspecified | user.email |

<Frame caption="Okta attribute statements">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/attributes.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=cf8b114282874e6030823de12d5bdc04" alt="Okta attribute statements." width="1416" height="588" data-path="assets/platform/workspaces/attributes.png" />
</Frame>

7. Hit the "Next" button towards the bottom of the page
8. Under the "Application Feedback" section, select "I'm an Okta customer adding an internal app" and hit "Finish":

<Frame caption="Okta feedback form">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/feedback-form.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=f63dc97194d46df9e7782bd6400b576b" alt="Okta feedback form" width="1440" height="344" data-path="assets/platform/workspaces/feedback-form.png" />
</Frame>

9. From the "Sign On" tab of the new Courier application integration, find the Metadata URL. Copy the link address and send it to the Courier support team member

<Frame caption="Okta Metadata URL">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/metadata.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=080f77a24df59a783881a70269ae2916" alt="Okta Metadata URL" width="748" height="720" data-path="assets/platform/workspaces/metadata.png" />
</Frame>

That's all you need for Okta sign-in. Assign users from the **Assignments** tab of the Courier app integration in Okta.

## Creating a Courier Bookmark App

Bookmark apps direct users to a specific web page from the Okta dashboard. Use one so your team can launch Courier directly from Okta.

<Note>
  You need a bookmark URL from Courier for IdP-initiated SSO. [Contact Support](mailto:support@courier.com) to get your URL.
</Note>

### Steps

1. Log in to the Okta admin panel as an Admin.
2. Go to **Applications > Applications**.
3. Click **Browse App Catalog**.
4. Search for `Bookmark App`, select it, and click **Add**.
5. Enter an app name (e.g. `Courier Login`).
6. Paste the URL from Courier Support into the URL field:

<Frame caption="Okta Bookmark App Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/okta-bookmark-app.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=8dbe9494de9046eaf6b062b62a3d5e67" alt="Okta Bookmark App Settings" width="1920" height="1212" data-path="assets/platform/workspaces/okta-bookmark-app.png" />
</Frame>

7. Click `Save`.
8. Assign to users to test.

## Migrating Users To Okta

1. From the [Settings > Security](https://app.courier.com/settings/security) page, confirm that "Require Google SSO" is not checked

<Frame caption="Google SSO Setup">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/google-sso.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=6f03af70cd0e4d9fc381bf60edec0843" alt="Google SSO checkbox in security settings" width="1958" height="260" data-path="assets/platform/workspaces/google-sso.png" />
</Frame>

2. From the [Settings > Team](https://app.courier.com/settings/team) page in Courier, remove and then re-invite users who should sign in with Okta

## Accepting an Okta Invitation

1. Sign out of Courier
2. Click the "join" button from the email invite
3. Enter your work email (the email address your invite was sent to)
4. Hit continue

<Frame caption="Courier login page">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/log-in.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=539706d5c430f8c9ff7f01ba0c157fea" alt="Courier login page with email entry" width="657" height="434" data-path="assets/platform/workspaces/log-in.png" />
</Frame>

<Note>
  Users with Okta logins to Courier must use the email login process.

  <Frame caption="Email Login Process">
    <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/log-in-email.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=ebd7e8ba63386956a56f9eac15cfd25a" alt="Email login process for Okta users" style={{width: 500}} width="642" height="384" data-path="assets/platform/workspaces/log-in-email.png" />
  </Frame>
</Note>

## User Provisioning with Okta SCIM v2

1. Contact Courier support for a SCIM endpoint URL and bearer token
2. Navigate to the Courier App from the Okta admin panel
3. Navigate to the provisioning tab and click "Edit"

<Frame caption="Provisioning settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/provisioning.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=14f098b87e0f4a9992ea80c6efa6d9c2" alt="Okta provisioning tab with Edit button" width="2028" height="574" data-path="assets/platform/workspaces/provisioning.png" />
</Frame>

4. Enter the URL provided by Courier into the "SCIM connector base URL"
5. Enter `userName` into the "Unique identifier field for users"
6. Check "Push New Users" and "Push Profile Updates" for the "Supported provisioning actions"
7. For "Authentication Mode" select `HTTP Header`
8. Enter the Bearer token provided by Courier

<Frame caption="SCIM authentication settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/scim-auth.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=42a6a8ded11d6b4ed47fff6a4f1f5b4f" alt="SCIM connector URL and authentication settings" width="1532" height="1380" data-path="assets/platform/workspaces/scim-auth.png" />
</Frame>

9. Hit "Save"
10. After 30 seconds the provisioning tab should have a "To App" section on the left. If it doesn't, try refreshing the page. Once it appears select it and hit the "Edit" button
11. Check the "Create Users", "Update User Attributes", and "Deactivate Users" features and hit save

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/to-app-settings.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=d9b8556e74ccc2927b42f5df9278dc38" alt="" width="2004" height="1166" data-path="assets/platform/workspaces/to-app-settings.png" />
</Frame>

12. Using the side menu navigate to Directory > Profile Editor and hit the edit profile button of the Courier App

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/profile-editor.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=39b7037c80b6b114366a9b77fa9c7736" alt="" width="2700" height="1152" data-path="assets/platform/workspaces/profile-editor.png" />
</Frame>

13. Hit the "Add Attribute" button

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/profile-editor-attributes.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=5caadd86a920687c0885e47aabe780be" alt="" width="2022" height="910" data-path="assets/platform/workspaces/profile-editor-attributes.png" />
</Frame>

14. Enter the following values:
    * Data type: `string`
    * Display name: `Role`
    * Variable name: `role`
    * External name: `role`
    * External namespace: `urn:ietf:params:scim:schemas:core:2.0:User`
    * Description: `Courier Role`

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/add-attribute-form.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=7bbbf275e75ae617f14a644f41da854f" alt="" width="1380" height="1060" data-path="assets/platform/workspaces/add-attribute-form.png" />
</Frame>

15. Check the "Define enumerated list of values" checkbox and enter the following values:

* Display Name: `Admin`, Value: `ADMINISTRATOR`
* Display Name: `Manager`, Value: `MANAGER`
* Display Name: `Developer`, Value: `DEVELOPER`
* Display Name: `Designer`, Value: `DESIGNER`
* Display Name: `Support`, Value: `SUPPORT_SPECIALIST`
* Display Name: `Analyst`, Value: `ANALYST`

16. Check the "Attribute required" checkbox and hit "save"

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/add-attribute-form-extra.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=f9a60e8794831f03a5efe8a1aa270ddd" alt="" width="1378" height="1436" data-path="assets/platform/workspaces/add-attribute-form-extra.png" />
</Frame>

<Note>
  If users were already assigned to the Courier app before you set up provisioning, edit their assignment and update their role.
</Note>

### Finalizing User Provisioning

* Changes to user assignments in the Courier Okta app will automatically be reflected in the Courier Workspace.
* Users will receive an invite via email to Courier when added.
* Users are automatically removed from the Courier Workspace when no longer assigned in Okta.
