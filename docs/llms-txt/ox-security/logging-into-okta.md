# Source: https://docs.ox.security/get-started/onboarding-to-ox/connect-to-ox/sign-in-to-ox/logging-into-okta.md

# SSO with Okta

Okta is an identity and access management platform that supports OpenID Connect (OIDC) for secure single sign-on.

OX supports OIDC SSO with Okta so your users can sign in to OX with their company credentials.

This guide shows how to create an OIDC Web Application in Okta, connect it to OX, and optionally use Okta groups to control OX roles and scopes.

## Prerequisites

* Okta Admin Console permissions to create applications and manage groups.
* OX Owner or Admin permissions.

## Step 1: Create the OIDC application \[Okta]

Create an OpenID Connect (OIDC) Web Application in Okta that represents OX. This app sets the redirect URI and provides the Client ID and Client Secret you need when connecting to OX.

**To create the OIDC application:**

1. Sign in to the **Okta Admin Console**.
2. Select **Applications** > **Applications** > **Create App Integration**, and set the following:

* **Sign-in method:** **OIDC – OpenID Connect**.
* **Application type:** **Web Application**.

1. Select **Next**, and set the following:

* **App integration name:** enter a clear name, for example, **OX Security SSO**.
* **Sign-in redirect URIs:** add your OX callback URL. Take the URL from the [Okta Configuration](https://app.ox.security/settings?tab=login\&loginOption=Okta)dialog box (<https://app.ox.security/settings?tab=login\\&loginOption=Okta>).

1. Select **Save**.

## Step 2: Get Client ID and Client Secret \[Okta]

* In the **Okta Admin Console**, go to **Applications > Applications > your app >** **General**, and find and copy: **Client ID** and **Client Secret**.

## Step 3: Configure SSO in OX \[OX]

1. In the OX platform, go to **Settings** > **Login Settings** and select **Okta**. The [Okta Configuration](https://app.ox.security/settings?tab=login\&loginOption=Okta) dialog box opens.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c443a39db3d48f0e98e51a0ba8e0d211b77a7803%2Fokta%20configuration%20screen%20(1).png?alt=media" alt="" width="396"><figcaption></figcaption></figure>

<table><thead><tr><th width="219">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><strong>Okta Domain</strong></td><td>Add your Okta domain (for example, <code>https://your-domain.okta.com</code>).</td></tr><tr><td><strong>Client ID</strong></td><td>Paste the Client ID from the Okta app.</td></tr><tr><td><strong>Client Secret</strong></td><td>Paste the Client Secret from the Okta app.</td></tr><tr><td><strong>Enable auto provisioning</strong></td><td>Enable this option if you want users to sign in without inviting them in the OX Members page and to control roles and scopes using Okta groups.<br><strong>Note:</strong><br>- If you do not configure auto-provisioning with roles, users who are not invited from the OX Members page sign in as <strong>Read Only</strong> by default.<br>- If you configure auto-provisioning with roles, manage role assignments only in Okta. Role changes in the OX Members page are ignored for users who sign in with Okta SSO.</td></tr><tr><td><strong>Sync OX Group Roles</strong></td><td>Roles define the permission level a user has in OX (Admin, Developer, Policy Manager, Read Only). When you map Okta groups to OX roles, Okta becomes the single source of truth for who can do what. This reduces manual changes in OX, enforces least-privilege, and keeps audits simple because access is managed in one place.</td></tr><tr><td><strong>Sync OX Group Scopes</strong></td><td>Scopes control what data and assets a user can see or manage in OX (for example by application owner or by tag). Mapping Okta groups to OX scopes lets you segment access cleanly across teams, business units, or projects. You keep sensitive areas visible only to the right people, and visibility updates follow org changes in Okta automatically.</td></tr></tbody></table>

1. Select **Save**.

## Step 4: Assign users to the app \[Okta]

1. In the **Okta Admin Console**, go to **Applications > your app > Assignments**
2. Select **Assign**, and assign **People** and **Groups** who can sign in to OX.
3. Select **Save**.

## Step 5: Enable app-initiated login and catalog visibility \[Okta]

1. In the **Okta Admin Console**, go to **Applications > your app** > **General** > **App Settings** > **Edit**.
2. **Login initiated by:** select **Either Okta or App**.
3. Select **Display application icon to users**.
4. **Initiate login URI:** Take the URL from the [Okta Configuration](https://app.ox.security/settings?tab=login\&loginOption=Okta)dialog box (<https://app.ox.security/settings?tab=login\\&loginOption=Okta>).

> **Note:** For On-Prem\
> [`https://app.ox.security/sso-login?organization=`](https://app.ox.security/sso-login?organization=)`<ORG_ID>&organization_name=<ORG_SLUG>&display_name=<DISPLAY_NAME>Example:`\
> <https://app.ox.security/sso-login?organization=org_XXX&organization_name=d7992de2-acme&display_name=acmeorg&connection=okta-acme>

1. Select **Save**.

## Step 6: Map Okta groups to OX roles \[Okta and OX]

1. In the **Okta Admin Console**, go to **Directory** > **Groups**.
2. Select **Add group**.
3. Create the groups you need using these exact names:\
   `OXApp-Admin`\
   `OXApp-Developer`\
   `OXApp-Dev Manager/Security Champion`\
   `OXApp-Policy Manager`\
   `OXApp-Read Only`
4. Open each new group, select **Assign people,** and add the relevant users or groups.
5. Go to Applications > your app > **Sign On** > **OpenID Connect ID Token** > **Edit**
6. **Group claim type:** **Filter**.
7. **Group claim filter:** **groups** **Matches regex** `.*`\
   (This includes group names in the ID token.)
8. Select **Save**.
9. In the OX platform, go to **Settings > Login Settings** and enable **Sync OX Group Roles**.

## Step 7: Map Okta groups to OX scopes \[Okta and OX]

1. In the **Okta Admin Console**, go to **Directory** > **Groups**
2. Select **Add group**.
3. Name scope groups using these formats. Use values from **View details** in the OX **Application scope** dropdown.

   **App Owner scope**\
   `OXAppOwnerScope-<SCOPE_NAME>-id:<APP_OWNER_ID>`\
   Example: `OXAppOwnerScope-DevOps-id:devops@acme.com`

   **Tag scope**\
   `OXTagScope-<TAG_NAME>-id:<TAG_ID>`\
   Example: `OXTagScope-app-id:acme-app`
4. Open each new group, select **Assign people**, and add the relevant users or groups.
5. Go to **Applications > your app >** **Sign On** . **OpenID Connect ID Token** . **Edit**
6. **Group claim type:** **Filter**.
7. **Group claim filter:** **groups** **Matches regex** `.*`
8. Select **Save**.
9. In the OX platform, go to **Settings > Login Settings** and enable **Sync OX Group Scopes**.

## Step 8: Test the sign-in \[OX]

1. In the OX platform, go to `https://<ENV>.app.ox.security/`.
2. Select **Sign in with Okta** and sign in with a user you assigned.
3. If you configured the **Initiate login URI**, you can open that link to start the flow directly.

## Troubleshooting

| Symptom                            | Where to fix | What to check                                                                                                                          |
| ---------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| Invalid redirect URI               | Okta         | The **Sign-in redirect URIs** entry must exactly match `https://auth.<ENV>.app.ox.security/login/callback`.                            |
| Invalid client or secret           | OX and Okta  | Paste the exact **Client ID** and **Client Secret** from the Okta app. Ensure the secret is valid.                                     |
| User not authorized to use the app | Okta         | Applications → your app → **Assignments**. Ensure the user or their group is assigned.                                                 |
| Roles do not match after sign-in   | Okta and OX  | Verify the user’s Okta group membership. Ensure **Group claim filter** includes groups and **Sync OX Group Roles/Scopes** is on in OX. |
