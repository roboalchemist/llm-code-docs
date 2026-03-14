# Source: https://docs.statsig.com/access-management/scim/okta_scim_setup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Okta SCIM Setup

This guide outlines the process for setting up SCIM (System for Cross-domain Identity
Management) integration between Statsig and Okta. This integration allows for automated
user provisioning and management.

## Prerequisites

* An Okta account with admin access
* A SCIM Key from the [Statsig Console](/access-management/scim/overview#how-to-obtain-scim-auth-key) (requires Statsig Org Admin rights)

<Note>
  ### Integration Notes

  * User email management is not enabled on SCIM yet.
  * When a user is removed from Statsig, they will be automatically unassigned in Okta. Conversely, if a user is unassigned or deactivated in Okta, they will be removed from the Statsig Organization.
  * Creation of Statsig Projects and Roles is not supported via SCIM.
</Note>

## Step 1: Create a New App Integration in Okta

* Log in to your Okta admin console
* Navigate to Applications > Applications > Create App Integration
* Select "SWA - Secure Web Authentication"

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step1-create-new-custom-integration.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=9a4fc28f1af1231b910562ac8b85b9f7" alt="Okta Create App Integration dialog selecting Secure Web Authentication" width="2078" height="1378" data-path="images/okta_scim_steps/step1-create-new-custom-integration.png" />
</Frame>

## Step 2: Configure App Settings

* Set the App name to "Statsig SCIM"
* Enter a placeholder URL for the App Login Page (this is a required field but not used for SCIM). Ex: `https://console.statsig.com/`

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step2-configure-app-settings.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=9174bfa9d20694fca0d6696d9f78fa30" alt="Okta app settings form with Statsig SCIM name and placeholder login URL" width="1514" height="1308" data-path="images/okta_scim_steps/step2-configure-app-settings.png" />
</Frame>

## Step 3: Enable SCIM Provisioning

* After creating the integration, go to the "General" tab
* Click on "Edit" in the "Provisioning" section
* Enable "SCIM Provisioning"

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step3-enable-scim.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=c16e26b67e4ff0d6b88a0abd94fe4426" alt="Okta application general tab highlighting provisioning section and SCIM toggle" width="1538" height="1326" data-path="images/okta_scim_steps/step3-enable-scim.png" />
</Frame>

## Step 4: Configure SCIM Settings

:::info

`Import Groups` requires an Okta flag `SELECTIVE_APP_IMPORT_PLATFORM`. If this flag is enabled for your organization, please select this option. If it is not, leave it unchecked.

:::

* Navigate to the `Provisioning` tab
* Set the SCIM connector base URL to: [https://statsigapi.net/scim](https://statsigapi.net/scim)
* Set "Unique identifier field for users" to `userName`
* Enable
  * `Import New Users and Profile Update`
  * `Push New Users`
  * `Push Profile Updates`
  * `Push Groups`
  * `Import Groups` (Only if your organization has the `SELECTIVE_APP_IMPORT_PLATFORM` flag enabled, see note above)
* Set the authentication mode to "HTTP Header"
* For the authorization header, use the SCIM Bearer token generated in Statsig by your Org Admin. See [How to Obtain SCIM Auth Key](/access-management/scim/overview#how-to-obtain-scim-auth-key) for more details.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step4.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=b4cc20c1a7d7828805410daf99c0eb64" alt="Okta provisioning tab showing SCIM base URL and push settings" width="2038" height="1836" data-path="images/okta_scim_steps/step4.png" />
</Frame>

## Step 5: Configure Okta to Statsig Settings

* Enable "Create Users"
* Enable "Update User Attributes"
* Enable "Deactivate Users"

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step5-configure-okta-to-statsig-settings.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=9febf95a278dd16f090c6edf1b3b8cd6" alt="Provisioning To App settings enabling create, update, and deactivate actions" width="2038" height="1766" data-path="images/okta_scim_steps/step5-configure-okta-to-statsig-settings.png" />
</Frame>

## Step 6: Import Existing Statsig Users and Groups

* In Okta, go to the Statsig app's "Import" tab
* Click "Import Now" to fetch existing Statsig users and groups
* Process the imported users as needed

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step6-import-existing-users.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=5614b5de292ff6d608475ee7ed59a8d1" alt="Okta Import tab with Import Now button for Statsig users and groups" width="2040" height="1440" data-path="images/okta_scim_steps/step6-import-existing-users.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).