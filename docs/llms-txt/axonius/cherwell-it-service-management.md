# Source: https://docs.axonius.com/docs/cherwell-it-service-management.md

# Cherwell IT Service Management

Cherwell IT Service Management is a service desk platform enabling automation for process workflows, supporting tasks, and related approvals.

### Asset Types Fetched

* Devices
* Users
* Business Applications
* Tickets

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password
* Client ID

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Cherwell Domain** - The hostname or IP address of the Cherwell server.
2. **User Name** and **Password** - The user name and the password of a read-only user.
3. **Client ID** - Enter the client ID created in the CSM Administrator. For details, see [Cherwell - Obtaining API Client IDs](https://help.ivanti.com/ch/help/en_US/CSM/2024/documentation_bundle/system_administration/rest_api/csm_rest_obtaining_client_ids.htm).

<Image alt="CherwellITServiceManagement.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CherwellITServiceManagement.png" />

### Optional Parameters

1. **Field Names Suffix** - Specify a common suffix for the various Cherwell fields.
   * If supplied, Axonius will omit the specified suffix when mapping the Cherwell fields to the Axonius device fields.
   * If not supplied, Axonius will not omit the specified suffix when mapping the Cherwell fields to the Axonius device fields. It may impact the mapped fields.
2. **Sleep 1 second every token request** - Select this option to wait before sending authentication tokens.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **CI Type Name Include List** *(optional)* - Specify a comma-separated list of CI types ([Configuration Items, such as: computer or mobile device](https://cherwellsupport.com/WebHelp/es/5.0/23293.htm)) in Cherwell.
2. **Parse Last Seen from Fields** - Enter a comma-separated list of fields from the raw data that can represent the last seen. If more than one field is provided, the most recent one is parsed. (Most commonly used fields: `LastReconciledDate`, `LastModifiedDateTime`, `LastADLogon`, `LastConnectedToVPN`)
3. **Fetch Only Deployed Devices** - Select this option to fetch only deployed devices.
4. **Fetch Applications Relationship ID** - Enter a string to fetch application data related to the device according to the specified relationship ID.
5. **Fetch Business Applications** - Select this option to fetch business applications.
6. **Status Include List** - Only fetch devices with the following status. Enter a list of status separated by commas.
7. **Add Status To Retired Device Hostnames** - Select to add the status as a suffix to host names, when the status is either 'Retired', 'Disposed', or 'Prepared for Disposal'. When the status is added, the hostname will appear 'Windows-PC\[Retired]' (for example).
8. **Concatenate Hostname To Device Identifier** *(default, false)* - When you select this option, if there is a change in the Cherwell record hostname field, then a new device is created. Note that for time configured in *Delete devices that have not been returned from the source in the last X hours* (default 48 hours), it may seem that the number of devices has doubled, but this is rectified after that time has passed.
9. **Parse Friendly Name as Device Name and Hostname** - Select this option to extract the device name and hostname from the friendly name.
10. **Advanced fields to show in basic view (Devices)** *(Custom Schema Entry (JSON))* - You can configure fields that generally appear in 'Advanced' to appear in 'Basic' view for devices. Use these settings to add JSON text that represents the SNAP structure to parse the raw data field to basic view in the GUI.
11. **Advanced fields to show in basic view (Users)**  *(Custom Schema Entry (JSON))* - You can configure fields that generally appear in 'Advanced' to appear in 'Basic' view for users. Use these settings to add JSON text that represents the SNAP structure to parse the raw data field to basic view in the GUI.

<Callout icon="📘" theme="info">
  Note

  For both **Advanced fields to show in basic view** settings, refer to [Showing Advanced Fields in Basic View](/docs/cherwell#showing-json-fields-in-basic-view) for more information.
</Callout>

13. **Fetch EC Action ticket updates** - Select this option to configure the adapter to fetch updates on tickets created by Axonius users. The updated ticket information is displayed in the **Tickets** table showing information on all tickets in the system (**Assets> Tickets**) or on Tickets of a specific asset (in the **Asset Profile** of the relevant asset).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Showing JSON Fields in Basic View

You can configure fields that generally appear in JSON to appear in Basic view. Configure for Devices, Business Applications, Databases; and for Users and Tickets separately, as required. Use the plus sign to add an entry to each field.

<Image alt="AdvancedFieldsBasic" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdvancedFieldsBasic.png" />

<Image alt="BasicViewUsersTIckets" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-1UY6Z32N.png" />

Enter fields in the following JSON format:

```json
[
{
    "label":"My First Field", 
    "raw_field": "field_a",
    "field_type": "str"
},
{
    "label":"My Second Field",
    "raw_field": "field_b",
    "field_type": "int"
},
{
    "label":"My third Field -  Application Name",
    "raw_field": "application/name",
    "field_type": "str"
},
{
    "label":"My third Field -  Application Number",
    "raw_field": "application/number",
    "field_type": "int"
}
]
```

* **label** - the name for the field you want to appear in the basic view
* **raw\_field** - the name of the field as it appears in JSON format on the Adapter Connections page of the Asset Profile (or Advanced view table)
* **field\_type** -the field type as  it appears in JSON format. The following field types are supported. int, string, datetime, float, bool. You can write them in the following ways:

  'int', 'string', 'str', 'date', 'datetime', 'float', 'bool', 'boolean'.

### Related Enforcement Actions

* [Cherwell IT Service Management - Create Incident](/docs/create-cherwell-incident)
* [Cherwell IT Service Management - Create Incident per Asset](/docs/create-cherwell-incident-per-entity)