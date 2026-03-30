# Source: https://docs.axonius.com/docs/jfrog-xray.md

# JFrog Xray

JFrog Xray is a software composition analysis (SCA) tool that scans software artifacts for security vulnerabilities, open source license compliance, and software quality.

### Asset Types Fetched

* Compute Images

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [JFrog Xray REST APIs](https://jfrog.com/help/r/xray-rest-apis/introduction-to-the-xray-rest-apis).

### Permissions

The value supplied in [User Name](#required-parameters) must have read permissions in order to fetch Repos, Artifacts, and Violations.

The value supplied in [User Name](#required-parameters) must have the Manage Reports role in order to fetch Vulnerabilities.

#### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the JFrog Xray server.
   * You can either use your JFrog URL in the following format: [http://myjfrog.mycompany.org](http://myjfrog.mycompany.org)
   * Or use your Artifactory server hostname and the Artifactory router port: http\://ARTIFACTORY\_SERVER\_HOSTNAME:8082
2. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.

![JFrog Xray](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JFrog%20Xray.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Global Endpoints Config** - Click on `>` to open the following settings for configurable global endpoints:
  * **Fetch Only X Latest Versions of Each Artifact** - Specify how many of the latest versions of each artifact to fetch. When specified, the adapter will add a new field called "Version Rank" to indicate which version is for each artifact (1 = latest version).
  * **Ignore Artifacts With Names Containing These Strings** - Artifacts with names matching these strings will be skipped and not displayed.
* **Endpoints Config** - By default the adapter enriches users via various endpoints. Click on `>` to open the following settings for configurable endpoints:
  * **Enrich Artifacts Endpoint with Vulnerabilities Reports Endpoint** - Toggle on to enrich the artifacts endpoint with the vulnerabilities reports endpoint.
  * **Start Vulnerabilities Reports - applies context on the following endpoints: Status Vulnerabilities Reports** - Click on `>` to open the following settings for configurable endpoints:
    * **Severities Allow List** *(optional)* - Select one or more severities of vulnerabilities fetched to include in the allow list. Clear options that you want to exclude from the fetch.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                           | Supported | Notes |
| --------------------------------- | --------- | ----- |
| API v1 Xray version 3.8 and above | Yes       | --    |

## Troubleshooting

* In order to fetch the vulnerabilities, this adapter creates an Xray vulnerabilities report. There is a limit of maximum saved reports (default: 100). If you already have the maximum amount of reports in your environment, the vulnerabilities cannot be fetched. In order to create a report, you can either delete unnecessary reports or increase the limit in the [Xray System YAML](https://jfrog.com/help/r/jfrog-installation-setup-documentation/xray-system-yaml).