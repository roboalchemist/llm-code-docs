# Source: https://docs.axonius.com/docs/shodan.md

# Shodan

Shodan is a search engine for Internet-connected devices.

Based on specified subnet or list of subnets, data fetched from Shodan include: hostname, ports open to the world, vulnerabilities, address information (country, region, city), ISP and more.

## Asset Types Fetched

* Devices
* Aggregated Security Findings
* SaaS Applications
* Domains & URLs

## Before You Begin

### Authentication Methods

* API Key

### Required Permissions

The adapter connection requires an API Key associated with a Shodan account that has the necessary permissions to fetch assets.

### Generating the Shodan API Key

1. Register an account in Shodan.
2. Visit your registered email id and activate the account.
3. Login to your account and you will find the API keys under profile overview tab.
4. Copy the API key and specify it in the [API Key](#parameters) field.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Shodan Domain** *(default: api.shodan.io)* - Should be kept as `api.shodan.io`.
2. **API Key** - Enter the API key you have defined (see [Generating the Shodan API Key](#generating-the-shodan-api-key)).

<Image alt="ShodanParameters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-3VGK6PHG.png" />

### Optional Parameters

<Callout icon="📘" theme="info">
  Note

  You have to either enter a **CIDR CSV File**, a **CIDR** subnet list, or a **Query Search** in order to configure this adapter.
</Callout>

1. **CIDR** *(default: empty)* - Specify a subnet to be used for fetching data from Shodan. If you want Shodan to scan multiple subnets, use the **CIDR CSV File** option to upload a CSV file with a list of subnets.
2. **CIDR CSV File Name** - This field is mandatory if a CSV File is being uploaded. If you upload several CIDR CSV files (in different Shodan adapter servers), you can specify a logical name for that file. The entered file name will be displayed in the Shodan adapter server list, enabling you to easily distinguish between different Shodan adapter servers.
3. **CIDR CSV File** - Upload a CSV file with a list of subnets  to be used for fetching data from Shodan. Click **Upload File** to upload the file. The structure of the CSV file should be as follows:
   * **"CIDR"** column *(required)* - Each row in the CSV should be populated with its subnet in the `X.Y.Z.N/P` format.
   * **DNSNAME** column *(optional)* - Each row in the CSV should be populated with the server name, if known.

     <Callout icon="📘" theme="info">
       Note

       While the `DNSNAME` column is optional, the CSV file must contain at least two columns (CIDR and one other).
     </Callout>
4. **Query Search** - Specify a search query using [Shodan's search query syntax](https://help.shodan.io/the-basics/search-query-fundamentals). This field will tell the adapter to execute the query you have specified to find devices information.
5. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.
6. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
7. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Ignore "www" in hostname before shorting** *(default: false)* - Enable this option to remove the `www` from the device hostname. This way, the "short hostname" configuration will affect the domain and not the `www` part.
2. **Fetch Vulnerabilities** *(default: true)* - Select whether to fetch vulnerabilities (parsed as Aggregated Security Findings).
3. **Parse devices as Domain & URLs** *(default: false)* - Enable this option to duplicate device data fetched from Shodan and display it within the **URL & Domains** asset type as well as the **Devices** asset type.

<br />