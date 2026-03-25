# Source: https://docs.ox.security/get-started/onboarding-to-ox/connect-to-ox/sign-in-to-ox/logging-into-microsoft-entra-id.md

# SSO with Microsoft Entra ID

Microsoft Entra ID (formerly Azure Active Directory) supports OpenID Connect (OIDC) for secure single sign-in.\
OX supports OIDC SSO with Entra ID so your users can sign in to OX with their company credentials.\
This section matches the structure and tone of your Okta SSO page for consistency.

## Prerequisites

* Entra admin permissions to register applications and manage Enterprise applications.
* OX Owner or Admin permissions.

## Step 1: Register the application \[Entra]

Create an application registration in Entra ID that represents OX. This app sets the redirect URI and provides the Application (client) ID you will use in OX.

To register the application:

1. In the **Entra admin center**, go to **Applications** > **App registrations** > **New registration**, and set the following parameters:

| Parameter                    | Description                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------- |
| **Name:**                    | Set the app name, for example, **OX Security SSO**.                             |
| **Supported account types:** | **Accounts in this organizational directory only (Single tenant)**.             |
| **Redirect URI:**            | **Platform:** **Web** \| **URL:** `https://auth.app.ox.security/login/callback` |

1. Select **Register**.

## Step 2: Create a client secret \[Entra]

1. Open the app **Certificates & secrets** page.
2. Select **New client secret**.
3. Enter a description and select an expiry period.
4. Select **Add**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7c0bf7b9799c00255c71176997865e0e1dc31c6c%2FAzure_entra_Secret_ID%20(1).png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

1. Copy and save the **Value** now. You will not see it again.

## Step 3: Configure SSO in OX \[OX]

1. In the OX platform, go to **Settings** > **Login Settings** and select **Microsoft Entra ID**. Take the values from the [Configuration](https://app.ox.security/settings?tab=login\&loginOption=AzureAD)screen.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-36300b53f44ce848a6a22aa1e893df714d5fbf6d%2Fsso%20microsoft%20entra%20config%20screen.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Fill the fields using as follows:

| Parameter                                 | Description                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entra domain or Tenant (Directory) ID** | Enter your tenant primary domain (for example, `contoso.onmicrosoft.com`) or the Directory (tenant) ID GUID.                                                                                                                                                                                                                                                                           |
| **Application (client) ID**               | Paste the **Application (client) ID** from the Entra app registration **Overview**.                                                                                                                                                                                                                                                                                                    |
| **Client Secret (Value)**                 | Paste the client secret value you created in Entra.                                                                                                                                                                                                                                                                                                                                    |
| **Enable auto provisioning**              | Enable this if you want users to sign in without inviting them in the OX Members page and to control roles and scopes using Entra ID groups. **Note:** If you do not configure auto-provisioning with roles, users who are not invited sign in as **Read Only**. If you do configure roles, manage role assignments only in Entra ID. OX role changes are ignored for Entra SSO users. |
| **Sync OX Group Roles**                   | When enabled, OX assigns a role (Admin, Developer, Policy Manager, Read Only) based on the user’s Entra ID group membership. Manage memberships in Entra ID.                                                                                                                                                                                                                           |
| **Sync OX Group Scopes**                  | When enabled, OX grants data visibility based on Entra ID group names that represent application owner scopes or tag scopes. Manage memberships in Entra ID.                                                                                                                                                                                                                           |

1. Select **Save**.

## Step 4: Assign users to the Enterprise application \[Entra]

1. In the **Entra admin center**, go to **Enterprise applications** and open your app.
2. Go to **Users and groups**.
3. Select **Add user/group** and assign the people and groups who can sign in to OX.
4. Select **Assign**.

## Step 5: Enable app-initiated login and catalog visibility \[Entra]

1. In **App registrations** > your app > **Branding & properties**, set the following parameters:

| Parameter         | Value                                                                                                                                         |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Home page URL** | `https://app.ox.security/sso-login?organization=<ORG_ID>&organization_name=<ORG_SLUG>&display_name=<DISPLAY_NAME>&connection=waad-<ORG_SLUG>` |

1. In **Enterprise applications** > your app > **Properties**, set the following parameters:

| Parameter                         | Value   |
| --------------------------------- | ------- |
| **Enabled for users to sign-in?** | **Yes** |
| **Assignment required?**          | **Yes** |
| **Visible to users?**             | **Yes** |

1. Select **Save**.

## Step 6: Map Entra ID groups to OX roles \[Entra and OX]

1. In **Groups**, create the groups you need using these exact names:\
   `OXApp-Admin`\
   `OXApp-Developer`\
   `OXApp-Dev Manager/Security Champion`\
   `OXApp-Policy Manager`\
   `OXApp-Read Only`
2. Add the relevant users to each group.
3. Include group claims in the token for OX (for example, add **groups** to the ID token in **Token configuration**).
4. In the OX platform, enable **Sync OX Group Roles** in **Settings** > **Login Settings**.

## Step 7: Map Entra ID groups to OX scopes \[Entra and OX]

1. In **Groups**, create scope groups using these formats. Use values from **View details** in the OX **Application scope** dropdown.

   **App Owner scope**\
   `OXAppOwnerScope-<SCOPE_NAME>-id:<APP_OWNER_ID>`\
   Example: `OXAppOwnerScope-DevOps-id:devops@acme.com`

   **Tag scope**\
   `OXTagScope-<TAG_NAME>-id:<TAG_ID>`\
   Example: `OXTagScope-app-id:acme-app`
2. Add members to each scope group.
3. Ensure group claims include these groups for OX.
4. In the OX platform, enable **Sync OX Group Scopes** in **Settings** > **Login Settings**.

## Step 8: Test the sign-in \[OX]

1. In the OX platform, go to `https://app.ox.security/` or your environment URL.
2. Select **Sign in with Microsoft** and sign in with an assigned user.
3. If you configured the **Home page URL** in Step 5, open that link to start the flow.

## Troubleshooting

| Symptom                                    | Where to fix | What to check                                                                                                                                                   |
| ------------------------------------------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reply URL mismatch                         | Entra        | The **Redirect URI** must exactly match `https://auth.app.ox.security/login/callback`.                                                                          |
| Invalid client secret                      | Entra and OX | Paste the secret **Value** in OX and verify it is not expired.                                                                                                  |
| User not authorized to use the app         | Entra        | **Enterprise applications** → your app → **Users and groups**. Ensure the user or their group is assigned.                                                      |
| Roles or scopes do not match after sign-in | Entra and OX | Verify the user’s Entra group membership, ensure group claims are in the ID token, and confirm **Sync OX Group Roles** or **Sync OX Group Scopes** is on in OX. |
