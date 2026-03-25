# Source: https://docs.axonius.com/docs/censys.md

# Censys

Censys monitors infrastructure and discovers unknown assets across the Internet.

<br />

### Asset Types Fetched

* Devices, Certificates

<br />

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API ID/API Secret

<br />

### Permissions

To obtain your [**API ID** and **API Secret**](#required-parameters), log into [https://censys.io/account/api](https://censys.io/account/api) and navigate to the API tab, where you should see credentials under **API Credentials**. Copy these values into Axonius during the Censys adapter setup, specify the query you'd like to run, click save, and the Censys adapter should be configured.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(510).png" />

Keep in mind that Censys API calls cannot be made faster than one request per second for the basic paid version, and one request per 2.5 seconds for the free version. In addition, there is a 25,000 call-per-month limit for the basic paid version, and a 250 call-per-month limit for the free version. You may want to adjust the "Minimum number of hours until next entities fetch" setting under Advanced Adapter Settings to ensure that you do not exceed your Censys monthly quota if you are using a Censys query that returns a significant number of results (as the default global fetch setting will result in re-running this query every 12 hours).

<br />

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Censys Domain** - Should be ‘censys.io' for API Version 1, 'search.censys.io’ for API Version 2, or 'api.platform.censys.io' for API Version 3.
2. **Is paid tier** - Check this if you are using the paid version of Censys (which has a limit of 250 API calls per month and a rate of one call per 2.5 seconds).
3. **API/Organization ID** and **API Secret**  - Your Censys API/Organization ID and secret values as specified in the [Permissions ](#permissions)section (API ID for Version 1 and 2, Organization ID for Version 3).
4. **API Version** - The version number of the Censys API. Select Version 1 (default domain: censys.io), Version 2 (default domain: search.censys.io), or Version 3 (default domain: api.platform.censys.io).
5. **Search Type** - The Censys search type to perform.
   * For Version 1, it can be ipv4 or websites.
   * For Versions 2 and 3, it can be hosts or certificates.
6. **Search Query** - A Censys search query following their syntax guide for the Search Type you selected (This is optional for Version 2). For Version 3, the CENQL queries must be used.

<Image alt="Censys connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Censys_AddConnection.png" />

<br />

### Optional Parameters

1. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
2. **CDIR CSV For Search** - Upload a CSV file with a list of subnets to be used for fetching data from Censys. The file must contain a CIDR column for searching.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Get device full details** - Select this option to enrich each device with its full details.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />