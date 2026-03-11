# Source: https://docs.axonius.com/docs/vmware-airwatch.md

# Omnissa Workspace ONE (AirWatch)

<Callout icon="📘" theme="info">
  Note

  This adapter was formerly named **VMware Workspace ONE (AirWatch)**.
</Callout>

Omnissa Workspace ONE (formerly AirWatch) provides enterprise mobility management (EMM) software and standalone management systems for content, applications, and email.

## Asset Types Fetched

* Devices
* Users
* Software
* SaaS Applications

## Before You Begin

### Authentication Methods

* Client ID / Client Secret
* User Name / Password / API Key

### Required Permissions

The adapter requires a system administrator (Admin) account with REST API permissions enabled at the relevant Organization Group and an account type that is allowed to generate the necessary API keys or OAuth service credentials.

### APIs

Axonius uses the <Anchor label="Omnissa Workspace ONE (AirWatch) REST API" target="_blank" href="https://brookspeppin.com/2021/07/24/rest-api-in-workspace-one-uem/">Omnissa Workspace ONE (AirWatch) REST API</Anchor> to retrieve asset data.

### Generating the API Key

1. On the Workspace ONE admin panel, click **Groups & Settings** → **All Settings**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(6\).png)

2. Click **System → Advanced → API → REST API**.

   <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(408).png" />

3. Click **Add** to create a new API key.

4. Add an indicative service name, set it to **Admin** Account Type, and then copy the API key and save it to a secure location.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **AirWatch Domain** - The hostname or IP address of the Omnissa Workspace ONE server.
2. **Authentication Method** - Select an authentication method: **OAuth** or **User Credentials**
   1. **OAuth** - When selected, the the following authentication fields are displayed:
      1. **Client ID** and **Client Secret** - Enter the Client ID and Client Secret to be used to authenticate the request. For more information about obtaining a Client ID and Client Secret, refer to <Anchor label="How to Use REST API in Workspace ONE UEM " target="_blank" href="https://brookspeppin.com/2021/07/24/rest-api-in-workspace-one-uem/">How to Use REST API in Workspace ONE UEM </Anchor>.
      2. **Access Token Domain** - Select the access token domain: `apac`, `emea`, `na` or `uat`. For information about the Access Token URL, refer to <Anchor label="Access Token URLs" target="_blank" href="https://kb.vmware.com/s/article/76967">Access Token URLs</Anchor>.
   2. **User Credentials** - When selected, the following authentication fields are displayed:
      1. **User Name** and **Password** - Enter the credentials for a user account that has the permissions to fetch assets.
      2. **API Key** - API key for the REST API, created in the admin panel.

         <Callout icon="📘" theme="info">
           Note

           If a user name is a dedicated user created solely for the adapter usage, you must first login as that user to create the recovery key. Then, the adapter connection should be successful.
         </Callout>

### Optional Parameters

1. **API Rate Limit (Calls per Minute)** - Enter a rate limit for the number of requests per minute to be sent to Omnissa. If left empty, the number of requests initiated by the connection for this adapter will be unlimited.
2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.
4. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
5. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Async chunks** *(required, default: 50)* - Specify the number of parallel requests all connections for this adapter will send to the Omnissa Workspace ONE server in parallel at any given point.
2. **Page Size** *(required, default: 500)* - Set the number of results per page received for a given query to the Omnissa Workspace ONE server, to gain better control on the performance of all connections of for this adapter.
3. **Socket recv session timeout** *(required, default: 300)* - Specify how many seconds all connections for this adapter will wait for a response before considering the request as timed out.
4. **Fetch devices not enrolled** *(required, default: true)* - By default this adapter also fetches devices that are not enrolled from the Omnissa Workspace ONE server. Clear this option to not fetch devices that are not enrolled.
5. **Fetch extended information** \*(required, default: true) - By default this adapter fetches additional information for each device, such as the **Security Patch Date** field. Clear this option to not fetch additional information for each device.
6. **Fetch device apps** - Select this option to fetch additional information for each device application from the Omnissa Workspace ONE server.
7. **Fetch device networks** - Select this option to fetch device networks from the Omnissa Workspace ONE server.
8. **Fetch device notes** - Select this option to fetch device notes from the Omnissa Workspace ONE server.
9. **Fetch device tags** - Select this option to fetch device tags from the Omnissa Workspace ONE server.
10. **Fetch device profiles** - Select this option to fetch device profiles from the Omnissa Workspace ONE server.
11. **Fetch device group** - Select this option to fetch the device group data.
12. **Fetch GPS data for the last X days** *(default: 0)* - Specify the number of days back to fetch the device's GPS data.
13. **Only fetch installed software** - Select this option to only fetch installed software.
    * If selected, only software with a Status of '2' (Installed) will be included in the fetch.
    * If disabled, all software listed under devices will be fetched, regardless of status.
14. **Fetch device compliance data** *(required, default: true)* - Select to query the compliance API. If this option is clear, the device compliance API is not queried and related data is not fetched.
15. **Fetch device sensors information** - Select this option to fetch device sensor information.
16. **Fetch baselines** - Select this option to fetch baselines based on the organizational group the adapter finds. A "Baselines" column will be added to each device and you will be able to run queries on it, if required.
17. **Fetch security search information** - Select this option to fetch security information for a device.
18. **Fetch extensive search** - Select this option to search results containing the devices and their product assignment information and fetch that data.
19. **Fetch users** *(default: true)* - Select this option to fetch users (if you clear this option, users are not fetched).
20. **Fetch Smart Groups** - Select this option to fetch Smart Groups.
21. **Parse friendly name as hostname** - Select this option to use the AirWatch Friendly Name as the hostname in Axonius.

### Related Enforcement Actions

* [Omnissa Workspace ONE (Airwatch) - Tag Devices](https://docs.axonius.com/axonius-help-docs/docs/omnissa-workspace-one-airwatch-tag-devices)
* [Omnissa Workspace ONE (Airwatch) - Delete Devices](https://docs.axonius.com/axonius-help-docs/docs/airwatch-delete-devices)