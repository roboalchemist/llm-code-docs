# Source: https://docs.axonius.com/docs/redseal.md

# RedSeal

RedSeal’s network modeling and risk scoring platform models customers'  hybrid data centers including public cloud, private cloud, and physical networks.

## Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications

The RedSeal adapter connection requires the following parameters:

1. **URL** – The address for the RedSeal server.
2. **User Name** and **Password** – The user name and password with a 'Model Admin' role. This role enables access to the RedSeal API.

<Image alt="RedSeal.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RedSeal.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Number of requests in parallel** *(required, default: 5)* - Specify the number of requests to make at the same time in order to fetch information about devices.
2. **Fetch Metrics Data** - Select this option to fetch metrics data.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>