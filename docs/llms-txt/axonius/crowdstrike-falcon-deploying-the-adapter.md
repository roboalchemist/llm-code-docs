# Source: https://docs.axonius.com/docs/crowdstrike-falcon-deploying-the-adapter.md

# Deploying the CrowdStrike Falcon Adapter

To deploy the *CrowdStrike Falcon* adapter, perform the following steps:

## 1. Create CrowdStrike Falcon credentials with the appropriate permissions

To create credentials using the following authentication method:

<Accordion title="Client ID / Client Secret" icon="fa-key">
  1. Log in to the **Falcon admin panel**.
  2. Go to **Support and resources** then select **API clients and keys**.

  <Image align="center" src="https://files.readme.io/ec51971229f742f1a71e5dabc2e3d17204556a2fdd8e9f779bffba9670e10632-SupportAndResources.png" width="290px" alt="image.png" />

  3. Click **Add API Client** and select the [permissions](/docs/crowdstrike-falcon#required-permissions).

  <Image align="center" src="https://files.readme.io/da5cf2077aeb61c563ead29a7b4dcf03456f2d2b9a4b188db2ace3fd98a2310d-image.png" width="375px" alt="image.png" />

  4. Click **Create**, then copy and securely store the generated **Client ID**, **Client Secret**, and **Base URL**.
</Accordion>

<Accordion title="Username / Password" icon="fa-user-lock">
  1. Log in to the **Falcon admin panel**.

  2. Navigate to **Host setup and management** then select **User management**.

  3. Click **Create user** and enter the User email, First name, Last name and Roles for the service account.

     <Image align="center" src="https://files.readme.io/9465c192424a1ac3877e643f649ac6d70ddac42ad1e8317130c14eda2cefd8e5-image.png" width="375px" alt="image.png" />

  4. Assign the [permissions](/docs/crowdstrike-falcon#required-permissions) to fetch Axonius SaaS Applications Settings.

  5. Log in once as this new user to initialize Multi-Factor Authentication.

  6. Securely store the Email and Password for later use.
</Accordion>

## 2. Set up the CrowdStrike Falcon adapter in Axonius

Create the Adapter connection in Axonius. Based on the authentication method, fill out the specific fields, and configure optional settings.

## Add a New Connection

* Navigate to the **Adapters** page, search for `CrowdStrike Falcon`, and click on the adapter tile.

  <Image align="left" alt="CrowdStrike Falcon tile" border={true} src="https://files.readme.io/33ce287f7f52acbec72cdf6ac292c40bb48ecedc4f6d6adf4e1d318ceb60d01a-CrowdStrike_Falcon_Adapter.png" className="border" />
* On the top right side, click on **Add Connection**.
* The **Add Connection** drawer opens.
  ![CrowdStrike Falcon add connection](https://files.readme.io/70e8c08edd75edb8a53daf5579f4dc4beb6e01320439eb27148909818ec31ef7-CrowdStrike_Add_Connection.png)

### Required Fields

* **CrowdStrike Domain** - The hostname of the API server. Could be one of the following:

  * `https://api.crowdstrike.com` or `https://api.us-2.crowdstrike.com` (US region)
  * `https://api.eu-1.crowdstrike.com/` (EU region)
  * `https://api.laggar.gcw.crowdstrike.com/` (Government)
* **User Name / Client ID** and **API Key / Client Secret** - Enter the *Client ID* and *Client Secret* generated when you created the API client in **CrowdStrike Falcon** admin console.

<Callout icon="📘" theme="info">
  Note\
  **Older or custom CrowdStrike deployments might use *User Name* and *API Key*. If your environment uses these legacy settings, enter them into the *User Name / Client ID* and *API Key / Client Secret* fields respectively.**
</Callout>

* **Connection Label** - Name to identify this adapter connection.

### Optional Fields

<Accordion title="Expand/Collapse" icon="fa-cog">
  * **Admin User Name** - The value you enter in the User Name field in CrowdStrike for the new user you created to allow Axonius to fetch Axonius SaaS Applications data.

  * **Admin Password** - The password you set for the new user in CrowdStrike.

  * **2FA Secret Key** - The secret generated in CrowdStrike for setting up 2-factor authentication for the CrowdStrike user created for collecting Axonius SaaS Applications data.

  * **Member CID** – Enter a CrowdStrike CID to fetch data from all tenants associated with that CID. To fetch data only from the primary tenant, leave this field blank.

  * **Verify SSL** – Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** – Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Ignore devices that have not been seen by this connection in the last X hours** – Select whether to avoid fetching old devices that are no longer part of your network, but that still exist in the present adapter connection.
    * When enabled, the adapter fetches only device assets that have been seen by this connection within the specified number of hours (Last Seen field).
      * For example, if set to 2160 hours, any device not seen in the last 90 days will be ignored..
    * When disabled, the adapter fetches devices according to the global **Ignore devices that have not been seen by this connection in the last X hours** option. For more information, see [Adapter Advanced Settings](/docs/advanced-settings).

  * **Threat Graph API User** and **Threat Graph API Key** – Fetch data from the CrowdStrike Threat Graph API.

  * **Notes** – Add a note of up to 250 characters for this adapter connection.

  * **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network.\
    To use this option, you need to set up an Axonius Gateway.
</Accordion>

### Troubleshooting

If you get an 403 Client Error when trying to connect the adapter:

* Verify your API scopes.
* In the **CrowdStrike Admin Console**, add the IP address of your Axonius instance to your IP allow list.

## 3. (Optional) Configure Advanced Settings

Refer to [CrowdStrike Falcon Advanced Settings](docs/crowd-strike-advanced-settings).