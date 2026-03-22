# Source: https://docs.rootly.com/integrations/scim.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SCIM

> Configure SCIM (System for Cross-domain Identity Management) integration for automated user provisioning and management.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/scim/images-1.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=cb02f5c046d14ac65c6235296ee77355" width="873" height="593" data-path="images/integrations/scim/images-1.webp" />
</Frame>

## Features

The following features are supported by Rootly:

* **Create users**. Users assigned to the Rootly application in your identity provider will be automatically added as members of your organization in Rootly.
* **Deactivate users**. Users unassigned from the Rootly application in your identity provider will be automatically removed as members of your organization in Rootly.
* **Import users**. Users can be imported at once into Rootly.
* **Update User Attributes**. User attributes updated in your identity provider will be updated in Rootly (e.g. first name, last name).
* **Sync SCIM Groups to Teams**. SCIM groups pushed from your identity provider can be automatically synced to Rootly Teams, including group creation, renaming, and member synchronization.

## Requirements

Make sure you setup [SSO](/integrations/sso) first.

**Rootly Tenant URL Endpoint:** `https://rootly.com/scim`

**Note**: The endpoint will only resolve in the application after SSO setup has been completed first as noted above.

## Okta

### Enable SCIM provisioning functionality in Okta

1. In Okta, navigate to **Applications > Rootly**
2. Click on the **Provisioning** tab in the application. Under the **Settings** panel on the left-hand side, click the **Integrations** link. Then click **Configure API Integration**.
3. Enter your API Token, you will find it under `Rootly > Integrations > SSO` under `SCIM Token`.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/scim/images-2.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=694ce61daca7489f620308759bc719eb" width="886" height="687" data-path="images/integrations/scim/images-2.webp" />
</Frame>

### Enable “create users” and “Deactivate users” functionalities in Okta[](#sKgme)

1. In Okta, navigate to **Applications > Rootly**
2. Click on the **Provisioning** tab in the application. Under the **Settings** panel on the left-hand side, click the **To App** link.
3. Click the **Edit** button at the top right. Check the **Enable** box next to **Create users** and **Deactivate users** to automatically provision/deprovision users in Rootly when they are assigned/unassigned to the Rootly app in Okta.
4. Ensure the **Default username** used to create accounts in Okta is set to **email**. If it’s not, update this value by going to the **Sign on** tab of the Rootly application in Okta, click **Edit**, then set the **Application username** format to **email** under the **Credentials settings** section.

### Provision Users via Push Groups

**Create a Group**

1. In Okta, navigate to **Directory > Groups** on the left navigation pane.
2. Click on **+Add Group**.
3. Give the Group a `name` and an optional `description`.
4. Now you have a Group which you can add Users to and provision the entire Group to a Rootly Role.

**Provision a Group**

1. In Okta, navigate to **Applications > Rootly**
2. Click on the **Push Groups** tab
3. Click on **+Push Groups** button to find the Group you'd like to provision.
   1. Click on the Group you'd like to provision from the dropdown.
4. Switch from **Create Group** to **Link Group**.
5. Click **Save**.
6. Navigate to your Rootly UI and select **Integrations > SSO**.
7. Under the **Role Assignment** section, select which **Rootly Role** you'd like to assign to the **Okta Group**.
8. You're all set! Now, every time you add a user to that Okta Group, they will be provisioned to Rootly in the associated Rootly Role.

## Microsoft Entra

### Enabled SCIM provisioning functionality in Microsoft Entra

[https://learn.microsoft.com/en-us/entra/identity/saas-apps/rootly-provisioning-tutorial](https://learn.microsoft.com/en-us/entra/identity/saas-apps/rootly-provisioning-tutorial "https://learn.microsoft.com/en-us/entra/identity/saas-apps/rootly-provisioning-tutorial")﻿

## Google Workspace

### Enabled SCIM provisioning functionality in Google Workspace[](#Kpp0A)

Google Workspace only supports SCIM for a few apps for reasons we aren't aware about. Fortunately enough we can take advantage of those to make it work with rootly.

* Add a new Web and Mobile apps
  <Frame>
    <img alt="Document Image" src="https://mintcdn.com/rootly/6qP0tS1GNk4jbxrs/images/integrations/scim/images-3.webp?fit=max&auto=format&n=6qP0tS1GNk4jbxrs&q=85&s=7ca7d08b88b06361936ade0ea181d8c7" width="319" height="205" data-path="images/integrations/scim/images-3.webp" />
  </Frame>
* Then add Adobe App
  <Frame>
    <img alt="Document Image" src="https://mintcdn.com/rootly/6qP0tS1GNk4jbxrs/images/integrations/scim/images-4.webp?fit=max&auto=format&n=6qP0tS1GNk4jbxrs&q=85&s=044059290a0198fa83c17fc96c311b7d" width="2153" height="753" data-path="images/integrations/scim/images-4.webp" />
  </Frame>
* In the next form fill out all fields with
  * [https://dummy.com/saml](https://dummy.com/saml)
* When it comes to configure auto-provisioning, copy the SCIM token you can find under Rootly > Integrations > SSO.
* Endpoint url to configure is [https://rootly.com/scim](https://rootly.com/scim "https://rootly.com/scim")
* Select a group of user you want to import into rootly or leave empty.
* Finally enabled the application. The sync should kick in shortly.

## Keycloak

### Enable SCIM provisioning functionality in Keycloak

1. **Install the SCIM Extension**
   * Download the keycloak-scim JAR file from the [releases](https://github.com/mitodl/keycloak-scim/releases)
   * Place it in `/opt/keycloak/providers/` directory
   * Restart Keycloak to load the extension

2. **Configure Event Listeners**
   * Navigate to **Realm Settings > Events**
   * In the **Event Listeners** tab, add `scim` to the list of listeners
   * Save the configuration

3. **Create SCIM Federation Provider**
   * Navigate to **User Federation**
   * Click **Add provider** and select **SCIM**
   * Configure the following settings:
     * **UI display name**: `Rootly`
     * **SCIM 2.0 endpoint**: `https://rootly.com/scim`
     * **Endpoint content type**: `application/scim+json`
     * **Auth mode**: `BEARER`
     * **Auth password/token**: Enter your SCIM token from `Rootly > Integrations > SSO`

4. **Configure Username Format**
   * Set the environment variable `SCIM_EMAIL_AS_USERNAME=true` to ensure usernames are sent in email format
   * This is required for proper user matching in Rootly

5. **Enable Propagation Features**
   * **Enable user propagation**: On
   * **Enable group propagation**: On (optional)
   * **Log SCIM requests and responses**: On (for debugging)
   * **Import action**: `CREATE_LOCAL`

6. **Optional Periodic Sync**
   * **Periodic full sync**: Enable if you want regular full user synchronization
   * **Periodic changed users sync**: Enable for incremental synchronization

### Testing the Configuration

* Create a test user in Keycloak
* Check Rootly to verify the user was automatically provisioned
* Review logs in Keycloak for any SCIM errors

**Note**: Ensure your Rootly SCIM token is valid and SSO is properly configured before setting up the SCIM integration.

## Sync SCIM Groups to Teams

Rootly can automatically sync SCIM groups from your identity provider to Rootly Teams. When enabled, the following lifecycle events are synced:

* **Create** — When a SCIM group is pushed to Rootly, a corresponding Team is created (or linked if a Team with the same name already exists).
* **Rename** — When a SCIM group is renamed in your identity provider, the linked Rootly Team is renamed to match.
* **Members** — When members are added or removed from a SCIM group, the linked Rootly Team membership is updated to match. Removals in the identity provider are also propagated.

### Enable Group Sync

1. Navigate to **Integrations > SSO** in your Rootly dashboard.
2. Toggle **Sync SCIM groups to teams** to enabled.
3. Save the configuration.

<Note>
  The **Sync SCIM groups to teams** toggle must be enabled by Rootly support. Please contact [support@rootly.com](mailto:support@rootly.com) to have this feature enabled for your organization.
</Note>

Once enabled, push your SCIM groups from your identity provider. If you had existing SCIM groups before enabling the toggle, they will be automatically backfilled and linked to corresponding Rootly Teams.

### Supported Identity Providers

Group sync works with any SCIM-compatible identity provider that supports pushing groups, including:

* **Okta** — Use the **Push Groups** tab in the Rootly application to push groups.
* **Microsoft Entra** — Configure group provisioning in the Rootly enterprise application.
* **Google Workspace** — Push groups through the SCIM auto-provisioning configuration.
* **Keycloak** — Enable group propagation in the SCIM federation provider settings.

## Troubleshooting

If you encounter any questions or difficulties with SSO or SCIM provisioning, please contact Rootly support via [support@rootly.com](mailto:support@rootly.com).


Built with [Mintlify](https://mintlify.com).