# Source: https://docs.api7.ai/enterprise/api-portal/custom-portal-enable-scim-okta.md

# Configure SCIM Provisioning for Developer Portal with Okta

This guide explains how to enable SCIM (System for Cross-domain Identity Management) provisioning for your **Custom Developer Portal**. By integrating Okta, you can automatically synchronize user accounts to your portal, ensuring consistent access control.

Since the [Developer Portal](https://docs.api7.ai/enterprise/api-portal/custom-portal.md) is based on the [API7 Developer Portal Boilerplate](https://github.com/api7/api7-portal-boilerplate), this configuration involves modifying the source code to enable the SCIM plugin in the authentication system ([Better Auth](https://www.better-auth.com/)).

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. Custom Developer Portal deployed and configured based on the `apps/site` structure of the boilerplate. See [Set Up Developer Portal with Provider Portal](https://docs.api7.ai/enterprise/api-portal/getting-started.md) and [Customize Developer Portal](https://docs.api7.ai/enterprise/api-portal/custom-portal.md).
2. An [Okta](https://www.okta.com/) account with administrative privileges.

## Create a SCIM Application in Okta[â](#create-a-scim-application-in-okta "Direct link to Create a SCIM Application in Okta")

Before modifying your portal code, set up a SCIM application in Okta.

1. Log in to the Okta Admin Console.

2. Navigate to **Applications** > **Applications**.

3. Click **Browse App Catalog**.

4. Search for `SCIM` and select **SCIM 2.0 Test App (Header Auth)**.

   ![Search for SCIM integration in Okta](https://static.api7.ai/uploads/2026/01/21/JICs1XPI_okta-scim-01-search.png)

5. Click **Add Integration**.

6. In the **General Settings** tab, name the application (e.g., "API7 Portal").

   ![Configure general settings](https://static.api7.ai/uploads/2026/01/21/6BW2sunV_portal-scim-okta-general-settings.png)

7. In the **Sign-On Options** tab, select **Secure Web Authentication (SWA)**.

   * Alternatively, select SAML/OIDC if you have configured SSO separately.

   ![Select sign-on options](https://static.api7.ai/uploads/2026/01/21/vWNGosPh_okta-scim-04-signon-options-select-web-auth.png)

8. Click **Done** to finish creating the application.

## Enable SCIM in Developer Portal[â](#enable-scim-in-developer-portal "Direct link to Enable SCIM in Developer Portal")

Update your portal's code to install and configure the SCIM plugin.

### Install SCIM Plugin[â](#install-scim-plugin "Direct link to Install SCIM Plugin")

In your project root (or `apps/site` directory), install the SCIM plugin. Ensure the version matches your `better-auth` version.

```
pnpm add @better-auth/scim@1.4.10
```

### Add Plugin to Server and Client[â](#add-plugin-to-server-and-client "Direct link to Add Plugin to Server and Client")

Modify the server and client files to register the SCIM plugin:

apps/site/src/lib/auth/server.ts

```
import {
  // ... existing imports
  organization,
  openAPI,
} from 'better-auth/plugins';
import { scim } from '@better-auth/scim';

export const auth = betterAuth({
  // ... existing config
  plugins: [
    nextCookies(),
    organization(),
    openAPI(),
    scim(),
    ...getTestingConfig(),
  ],
});
```

apps/site/src/lib/auth/client.ts

```
import {
  // ... existing imports
  genericOAuthClient,
} from 'better-auth/client/plugins';
import { scimClient } from '@better-auth/scim/client';

export const authClient = createAuthClient({
  basePath: AUTH_BASE_PATH,
  plugins: [
    organizationClient(),
    magicLinkClient(),
    genericOAuthClient(),
    scimClient(),
  ],
});
```

### Update Route Handler HTTP Methods[â](#update-route-handler-http-methods "Direct link to Update Route Handler HTTP Methods")

SCIM requires specific HTTP methods (`PUT`, `PATCH`, `DELETE`) for user management. Update your route handler for these methods:

apps/site/app/api/auth/\[...all]/route.ts

```
// export const { GET, POST } = toNextJsHandler(auth.handler);
export const { GET, POST, PUT, PATCH, DELETE } = toNextJsHandler(auth.handler);
```

### Update Database Schema[â](#update-database-schema "Direct link to Update Database Schema")

The SCIM plugin requires additional database tables. Generate the schema and apply migrations:

```
cd apps/site
pnpm db:generate-schema
pnpm db:generate
pnpm db:migrate
```

You should see an output similar to the following:

```
> @api7ee/site@0.5.6 db:migrate /path/to/your/project/apps/site
> drizzle-kit migrate

No config path provided, using default 'drizzle.config.ts'
Reading config file '/path/to/your/project/apps/site/drizzle.config.ts'
Using 'pg' driver for database querying
[â] migrations applied successfully!
```

### Generate SCIM Token[â](#generate-scim-token "Direct link to Generate SCIM Token")

Create a temporary script to generate the SCIM token for Okta integration.

1. Create the following script:

   apps/site/scripts/get-scim-token.ts

   ```
   import { auth } from '@/lib/auth/server';

   async function main() {
     // 1. Sign in as an admin to get a session
     const loginRes = await auth.api.signInEmail({
       returnHeaders: true,
       body: {
         email: 'admin@example.com', // Replace with your admin email
         password: 'password1234', // Replace with your admin password
       },
     });

     const headers = {
       cookie: loginRes.headers.get('set-cookie') || '',
     };

     // 2. Generate the SCIM Token for Okta
     const res = await auth.api.generateSCIMToken({
       body: {
         providerId: 'okta',
       },
       headers,
     });
     console.log('SCIM Token:', res.scimToken);
   }
   main().catch((err) => console.trace(err));
   ```

2. Run the script:

   ```
   pnpm dlx tsx ./scripts/get-scim-token.ts
   ```

3. Copy the generated token, which is in the format of `Y0xRcHlHZTVVZGM5aTl3U19SSGtWSFczOm9rdGE=`.

## Configure Okta API Integration[â](#configure-okta-api-integration "Direct link to Configure Okta API Integration")

Connect Okta to your Developer Portal.

1. In Okta, navigate to the **Provisioning** tab of your SCIM application.

2. Click **Configure API Integration** > **Enable API Integration**.

3. Configure the following defaults:

   * **SCIM 2.0 Base URL**: Enter your portal's auth URL appended with `/scim/v2`, for example `https://<YOUR_PORTAL_DOMAIN>/api/auth/scim/v2`.
   * **API Token**: Enter `Bearer <YOUR_SCIM_TOKEN>`. Ensure there is a space between `Bearer` and the token.

4. Click **Test API Credentials** to verify the connection. If successful, click **Save**.

![Configure API integration](https://static.api7.ai/uploads/2026/01/21/KftTlW3Q_portal-scim-okta-config-api-integration.png)

## Configure Provisioning and Assign Users[â](#configure-provisioning-and-assign-users "Direct link to Configure Provisioning and Assign Users")

Before you assign users to the application, you should first enable and configure how Okta will provision user accounts and lifecycle changes to your SCIMâenabled app. This ensures that Okta can create, update, and deactivate accounts correctly once assignments are made.

### Configure Provisioning[â](#configure-provisioning "Direct link to Configure Provisioning")

1. In Okta, navigate to the **Provisioning** tab of your SCIM application.

2. Select **To App** settings and click **Edit** to configure provisioning.

3. Enable the following options so Okta can manage user lifecycle events in your app:

   <!-- -->

   * **Create Users**: provision new users created in Okta to the app
   * **Update User Attributes**: synchronize profile updates from Okta to the app
   * **Deactivate Users**: deactivate users in the app when they are unassigned or deactivated in Okta

4. Click **Save**.

![Enable create users](https://static.api7.ai/uploads/2026/01/21/M1csHXQ2_portal-scim-okta-edit-allow-create-users.png)

### Assign Users[â](#assign-users "Direct link to Assign Users")

1. In Okta, navigate to the **Assignments** tab of your SCIM application.
2. Click **Assign** > **Assign to People** (or **Assign to Groups**).
3. Select users or groups and click **Assign**, then **Done**.

![Assign to users](https://static.api7.ai/uploads/2026/01/21/6t33H2PD_portal-scim-okta-check-assigned.png)

## Verify[â](#verify "Direct link to Verify")

To confirm user synchronization, check your Developer Portalâs user list or database to verify that the users you assigned in Okta have been provisioned correctly:

![Verify users in database](https://static.api7.ai/uploads/2026/01/21/nn6QMkms_portal-scim-okta-check-in-db.png)
