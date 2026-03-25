# Source: https://docs.axonius.com/docs/elasticsearch.md

# Elasticsearch

The Elasticsearch adapter imports device information from an Elasticsearch database.

<Callout icon="📘" theme="info">
  Prerequisite

  [Metricbeats](https://www.elastic.co/guide/en/beats/metricbeat/current/metricbeat-installation-configuration.html) must be setup and running in order to generate and format the ElasticSearch information in the way this adapter requires.
</Callout>

### Asset Types Fetched

* Devices, Aggregated Security Findings, Users, Software, SaaS Applications

## Before You Begin

**Ports**

See [Port](/docs/elasticsearch#required-parameters) below.

**Authentication Method**

* User Name/Password for Cloud
* API Key ID/API Key for on-prem

### APIs

Axonius uses the [Elasticsearch 9 API](https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html).

### Permissions

You must have the read [index privilege](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/security-privileges.html#privileges-list-indices) for the target data stream, index, or alias.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Elasticsearch server.
2. **Port** *(default: 9200)* - Specify the port of the Elasticsearch system.
3. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **API Key ID** and **API Key** are not supplied, **User Name** and **Password** are required.
</Callout>

4. **API Key ID** and **API Key** - An API Key ID and API key associated with a user account that has the permissions to fetch assets. API Key ID and API Key can be used instead of user name and password. For details see [Elasticsearch Create API Key](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html).

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Key ID** and **API Key** are required.
</Callout>

<Image alt="Elasticsearch.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Elasticsearch.png" />

### Optional Parameters

1. **Data Streams Search Target** *(optional, Recommended)* - The target path search to fetch from. Enter a Comma-separated list of data streams, indices, and aliases to search. Supports Elastic wildcard (\*) expressions.
   * Make sure you  Choose sources which return ECS Host or winlog  fields(See Note below)
     * Examples:<br />
       .ds-logstash-dhcpd-*<br />
       logs-*<br />
       filebeat-\*

To search all data streams and indices, omit this parameter or use \* or \_all. Please see data below as this may return unexpected results.

<Callout icon="📘" theme="info">
  Note

  Axonus fetches data structured in the Elastic Common Schema that has some of the Host fields listed in the Host Structure. Refer to:

  * [Common Elastic Structure](https://www.elastic.co/guide/en/ecs/current/index.html)

  * [Host Structure](https://www.elastic.co/guide/en/ecs/current/ecs-host.html)
    Wildcard indexes may search large amounts of records which do not contain Host Details and are not parsed as devices.

  Specifying a Data Stream is recommended.<br />
  For further information see:

  * [An introduction to the Elastic data stream naming scheme](https://www.elastic.co/blog/an-introduction-to-the-elastic-data-stream-naming-scheme)

  * [Set up a data stream](https://www.elastic.co/guide/en/elasticsearch/reference/current/set-up-a-data-stream.html)
</Callout>

2. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-setting).

3. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

4. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **Logs contain user information** - If logs contain user data, select this option to fetch users instead of devices.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Hour range filter** *(default: 10)*  - Inspect all logs within the last specified hours and extract devices from all data received. Minimum value is `1`; Maximum value is `72`.
2. **Page size** *(default: 500, max: 500)* - Enter a page size to control the number of items to return per request to the Search API. Decreasing this number may improve fetch stability.
3. **Fetch devices without hostname** - Select whether to fetch devices from Elasticsearch that do not have a hostname.
4. **Parse dynamic fields** - Select this option to parse all the fields fetched from the API as dynamic fields. These are fields created during the fetch process. They can be queried, and their names and types are defined by the field name and value parsed.
5. **Use fetch time for Last Seen** - Select this option to set that all entities (devices and users) fetched by this adapter have their Last Seen set to the time the entity was fetched (fetch\_time).
6. **Custom query** *(optional)* - Enter a JSON-formatted object name that refers to the additional fields you want to parse for each asset. You need to define this custom object on your Elasticsearch environment. The adapter can parse data for Installed Software, Vulnerabilities (Aggregated Security Findings), BIOS, and Hardware Serial.

**Custom Object Fields**
The custom object you define in Elasticsearch needs to include the following fields:

* For Installed Software:
  * 'identifying\_number'  - Software ID
  * 'name' - Software name
  * 'publisher' - Software publisher
  * 'version' - Software version
  * 'install\_source' - Where the software is installed on the host
  * 'install\_date' - When the software was installed on the host
* For Vulnerabilities:
  * 'vulnerable\_software' - Vulnerable Software name
  * 'cve\_id' - Vulnerability ID
  * 'cve\_description' - Vulnerability description
  * 'cvss\_base\_score' - Vulnerability score
  * 'cv\_updated\_at' - When the CVE's information was last modified
* For BIOS data:
  * 'bios\_manufacturer' - The manufacturer of the BIOS software
  * 'bios\_release\_date' - The release data of this BIOS' version
  * 'bios\_serial' - The serial number of the BIOS release
  * 'bios\_version' - BIOS version
* For Hardware Serial, include the 'hardware\_serial' field, representing the hardware's serial number.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version            | Supported | Notes |
| ------------------ | --------- | ----- |
| Elasticsearch 7.10 | Yes       |       |