# Source: https://docs.axonius.com/docs/cloudfit-cfs.md

# CloudFit CFS

CloudFit CFS delivers managed, custom applications for cloud, hybrid, and on-premise environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the CloudFit CFS server that Axonius can communicate with.
2. **Port** *(required, default 9200)* - The port of the CloudFit CFS system.
3. **User Name** and **Password** *(optional, default: empty)* - The credentials for a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  If **API Key ID** and **API Key** are not supplied, you must specify **User Name** and **Password**.
</Callout>

4. **API Key ID** and **API Key** *(optional, default: empty)* - An API Key ID and API key associated with a user account that has the permissions to fetch assets. API Key ID and API Key can be used instead of user name and password. For details see [Elasticsearch Create API Key](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html).

<Callout icon="📘" theme="info">
  Note

  If **User Name** and **Password** are not supplied, you must specify **API Key ID** and **API Key**.
</Callout>

5. **Data Streams Search Target** *(optional, default: empty)* - The target path search to fetch from
   * If supplied, Axonius will fetch the data from the defined list. The list should be passed in a comma-separated, listing data streams, indices and index aliases. Elastic wildcard (\*) expressions are supported.
   * If not supplied, all data will be fetched.
     6    **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="CloudFitCFS.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CloudFitCFS.png" />

## APIs

Axonius uses the [Elasticsearch 7.10 API](https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html) to fetch CloudFit CFS data.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, and it is not functioning as expected.

| Version            | Supported | Notes |
| ------------------ | --------- | ----- |
| Elasticsearch 7.10 | Yes       |       |