# Source: https://docs.axonius.com/docs/cisco-identity-services-engine-ise.md

# Cisco Identity Services Engine (ISE)

The Cisco Identity Services Engine (ISE) adapter connects to the Cisco ISE management interface in order to enable the creation and enforcement of security and access policies for endpoint devices connected to managed routers and switches.

## Asset Types Fetched

* Devices
* Users

## Before You Begin

### Required Ports

Axonius must communicate with Cisco ISE Domain through the following ports:

* External RESTful Services (ERS) REST API: 9060

* Cisco Platform Exchange Grid (pxGrid) API: 8910

* Management API (If fetching auth sessions): 443

* For more details, see <Anchor label="Cisco ISE Ports Reference" target="_blank" href="https://www.cisco.com/c/en/us/td/docs/security/ise/3-5/install_guide/b_ise_Installation_Guide_35/b_ise_InstallationGuide_chapter_7.html">Cisco ISE Ports Reference</Anchor> and <Anchor label="Cisco Developer Documentation" target="_blank" href="https://developer.cisco.com/docs/identity-services-engine/latest/#!setting-up/using-the-api">Cisco Developer Documentation</Anchor>.

### Authentication Methods

* User Name and Password

### Required Permissions

The value supplied in [User Name](#required-parameters) must have **Read-only** access to devices.
To create a service account for Axonius with the sufficient permissions for calling the Cisco ISE API, do as follows:

1. Navigate to **Administration** `>` **Admin Access** `>` **Administrators** `>` **Admin Users** and click  **Add**.

![ise-account-step-1](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Ise-account-step-1.png)

2. Assign an access type. Select **ReadOnly**. You can choose between **Read/Write** or **ReadOnly**.

3. Add the user to one of the following Admin Groups: **ERS Admin** or **ERS Operator**.

4. Enable ERS (External RESTful Services) to allow REST calls. To do this, navigate to **Administration** `>` **System** `>` **Settings** `>` **ERS Settings** then select **Enable ERS for Read/Write** under the Primary Administration Node:

   <Image align="center" alt="image.png" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(594).png" className="border" />

<Callout icon="📘" theme="info">
  Note

  The ERS setting must be enabled after each upgrade as it is reset to "disabled" during each upgrade. If you plan on utilizing this adapter, we recommend adding a note to your Cisco ISE upgrade process documentation that the REST API should be enabled at the end of each upgrade.
</Callout>

### Authorizing Axonius in pxGrid Services on your Cisco ISE domain

To authorize Axonius with the sufficient permissions for using the pxGrid services do as follows:

1. Enable the **Use pxGrid to Fetch Live Sessions** checkbox in the **Add Connection** dialog.

2. Clicking **Save and Fetch** will generate an Axonius ID that will follow in an error to authorize the generated ID in the pxGrid System: (Next steps)
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ISE%20pxGrid%20Connector%20error22.png)

3. Log into the ISE Admin GUI, navigate to **Administration** `>` **pxGrid Services**

<Image align="center" alt="ise-account-step-1" border={true} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ISE%20Menu.png" className="border" />

4. If the user you define does not appear in the Cisco UI, you might have to navigate to the “Settings” tab in the Cisco ISE pxGrid Administration settings page and tick the checkbox labeled “Allow password based account creation“.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ise_user_setting.png)

5. Select the Axonius client and click **Approve** as shown in the image.

<Image align="center" alt="ISEGRidStep4" border={true} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ISEGRidStep4.png" className="border" />

6. Click **Save and Fetch** to complete the configuration and establish the connection. If the error mentioned in step 2 occurs with the same account, check whether the Axonius account (Axonius\_XXXX) is authorized in pxGrid.

<Image align="center" alt="ISE pxGrid Connector error22" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ISE%20pxGrid%20Connector%20error22.png" className="border" />

<Callout icon="📘" theme="info">
  Note

  pxGrid Services should be enabled on your Cisco ISE domain.
</Callout>

### Enabling pxGrid Services in Cisco ISE Administration

To enable pxGrid Services in Cisco ISE Administration:

1. Log into the ISE Admin GUI, navigate to **Administration** `>` **Deployment**
2. Select the ISE node to be used for the pxGrid persona.

<Image align="center" alt="CiscpISEGRidStep2" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscpISEGRidStep2.png" className="border" />

3. Select **pxGrid** and click **Save**.

<Image align="center" alt="CiscoISEGRidlast" border={true} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoISEGRidlast.png" className="border" />

<Callout icon="📘" theme="info">
  Note

  For Cisco ISE pxGrid to be enabled you must have a plus license on ISE deployment. For more details, see [Configure ISE 2.4 and FMC 6.2.3 pxGrid Integration](https://www.cisco.com/c/en/us/support/docs/security/identity-services-engine-24/214481-configure-ise-2-4-and-fmc-6-2-3-pxgrid-i.html).
</Callout>

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Cisco ISE Domain** - Enter the hostname or IP address of the Cisco ISE server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** - Enter the credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

![CiscoISEN(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoISEN\(1\).png)

### Optional Parameters

1. **Cisco pxGrid Domain** - Set this parameter to connect to a pxgrid domain instead of the regular domain used for ERS. When this parameter is not set, the same ISE domain is used for both pxgrid and ERS APIs.
2. **Use pxGrid to Fetch Live Sessions**  -
   * If enabled, Axonius will enrich the data collected from Cisco ISE by enabling pxGrid. Using pxGrid requires a plus licence and requires an additional authentication step from pxGrid Services on your Cisco ISE domain. For more details, see [Authorize Axonius in pxGrid Services](/docs/cisco-identity-services-engine-ise#auth).
   * If disabled, Axonius will not enable pxGrid.
3. **pxGrid Client Certificate** / **pxGrid Client Private Key** / **pxGrid Client Private Key Password** / **pxGrid Client Root CA chain** - Those settings are required for xmpp client with pxgrid 1.0. For details, contact [Axonius Support](https://support.axonius.com/).

   <Callout icon="📘" theme="info">
     Note

     The xmpp client has been deprecated by Cisco. Axonius will continue supporting it, but it is advised to transition to the REST client to fetch pxGrid data.
   </Callout>
4. **Use v1.1 Object Model for ERS API**  - Select when using either Cisco ISE versions 2.4 or  2.7, or if you receive a “Connection Fails”  HTTP 400 error.

   <Callout icon="📘" theme="info">
     Note

     This parameter is only used with the ERS API. It has no effect when using the pxGrid API.
   </Callout>
5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
6. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Fetch Internal Users** - Select this option to fetch internal users.
2. **Fetch Guest Users** - Select this option to fetch guest users.
3. **Fetch Admin Users** - Select this option to fetch admin users.
4. **Fetch endpoints (through ERS)** - Select this option to fetch data from the ISE endpoint through the ERS endpoint API.
5. **Enrich Endpoints with Authentication Status and Session Parameters** - Select this option to add authentication status data for each fetched endpoint. This will also fetch and enrich endpoint devices with session parameters (See examples from [ISE Monitoring API](https://community.cisco.com/t5/security-knowledge-base/ise-monitoring-api-examples/ta-p/4800437#toc-hId--2136851129)), which will allow to populate the **Last Seen** field, for example.
6. **Enrich Endpoints with Policy Name** - Select this option to enrich endpoint devices with the policy name.
7. **Fail client on pxGrid connection error** *(default: true)* - Select to propagate errors originating from the pxGrid connection when *Use pxGrid to fetch live sessions* is enabled for a client. When this is not set, errors are propagated only when there are errors from both pxGrid and ERS connectivity to a client.

   <Callout icon="📘" theme="info">
     Note

     When configuring the Cisco ISE and you do not want to use the pxGrid fetch to retrieve the data, enable **Fetch endpoints**.
   </Callout>
8. **Skip devices without IP address** - Select this option to not fetch devices that do not have an IP address.
9. **Only include devices that have a name OR an IP address** -  Select this option to only fetch devices that have either an asset name or an IP address.
10. **Only include devices that have a name AND an IP address** - Select this option to only fetch devices that have both an asset name and an IP address.

    <Callout icon="💡" theme="warn">
      Important

      If a Cisco ISE connection has '**Fetch endpoints**' enabled and at the same time has '**Skip devices without IP address**' or '**Only include devices that have a name AND an IP address**' enabled, then the endpoints data will not be ingested, because endpoints don’t have IP address data.
    </Callout>

### Related Enforcement Actions

* [Cisco AMP - Assign Assets to Group](/docs/cisco-amp-assign-endpoint-to-group)
* [Cisco Identity Services Engine (ISE) - Apply Policy to Devices](/docs/cisco-ise)