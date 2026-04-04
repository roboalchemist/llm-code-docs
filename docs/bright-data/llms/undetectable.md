# Source: https://docs.brightdata.com/integrations/undetectable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With Undetectable

> Learn how to configure Bright Data in Undetectable for secure and anonymous browsing. This step-by-step guide will help you enhance your online privacy and efficiency.

<Accordion title="Expand to get your Bright Data Proxy Access Information">
  ### Your proxy access information

  Bright Data proxies are grouped in "Proxy zones". Each zone holds the configuration for the proxies it holds.

  To get access to the proxy zone:

  1. Login to Bright Data control panel
  2. Select the proxy zone or setup a new one
  3. Click on the new zone name, and select the **Overview** tab.
  4. In the overview tab, under **Access details** you can find the proxy access details, and copy them to clipboard on click.
  5. You will need: Proxy Host, Proxy Port, Proxy Zone username and Proxy Zone password.
  6. Click on the copy icons to copy the text to your clipboard and paste in your tool's proxy configuration.

  ### Access Details Section Example

    <img src="https://mintcdn.com/brightdata/fC1f9RYBP6dv7X6V/snippets/accessdetails.png?fit=max&auto=format&n=fC1f9RYBP6dv7X6V&q=85&s=dfffcbfd5b7b4f07481f534159e6f710" alt="" width="597" height="508" data-path="snippets/accessdetails.png" />

  ### Residential proxy access

  To access Bright Data's **Residential Proxies** you will need to either get verified by our compliance team, or install a certificate. [Read more...](https://docs.brightdata.com/proxy-networks/residential/network-access)

  ### Targeting search engines?

  If you target a search engine like google, bing or yandex, you need a special Search Engine Results Page (**SERP**) proxy API. Use Bright Data SERP API to target search engines.
  [Click here to read more about Bright Data SERP proxy API.](https://docs.brightdata.com/scraping-automation/serp-api/introduction)

  ### Correct setup of proxy test to avoid "PROXY ERROR"

  In many tools you will see a "test proxy" function, which performs a conncectivity test to your proxy, and some add a geolocation test as well, to identify the location of the proxy.
  To correctly test your proxy you should target those search queries to:
  `https://geo.brdtest.com/welcome.txt` .

  Some tools use popular search engines (like google.com) as a default test target. Bright Data will block those requests and you tool will show **proxy error** although your proxy is perfectly fine.

  If your proxy test fails, this is probably the reason. Make sure that your test domain is not a search engine (this is done in the tool configuration, and not controlled by Bright Data).
</Accordion>

## What is Undetectable?

Undetectable is an anti-detect browser that enables secure and anonymous browsing by creating multiple browser profiles with unique digital fingerprints. It's perfect for managing multiple accounts, web scraping, and other activities requiring privacy and security.

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

## How to Integrate Bright Data With Undetectable

**Step 1. Download and Log In to Undetectable**

1. Visit the [Undetectable website](https://undetectable.io/) and download the application.
2. Install the software on your system and log in using your credentials.

**Step 2. Access Proxy Configuration**

1. Open Undetectable and go to the **Proxy** tab.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/undetectable1.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=0a3cf258c00d8537479215582ab49929" alt="" width="370" height="261" data-path="images/integrations/undetectable1.png" />
</Frame>

2. Click on the **Plus** button to add a new proxy.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/undetectable2.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=7ecc6a163fe2803bbbbe14691a81355e" alt="" width="690" height="187" data-path="images/integrations/undetectable2.png" />
</Frame>

**Step 3. Configure Bright Data Proxy Details**

1. In the proxy setup window:

* Provide a descriptive name in the **Proxy Name** field for easy identification.
* **Type**: Select HTTP or SOCKS5.
* **Host**: `http://brd.superproxy.io/`.
* **Port**: The port number from your [Bright Data dashboard](https://brightdata.com/cp/zones/page/plans).
* **Login**: Your Bright Data username.
* **Password**: Your Bright Data password.

2. Click **Check** to verify the connection.
3. Once verified, click **Save Proxy** to store your proxy settings.

<Note>
  For geo-targeted proxies, format your username as `your-username-country-XX` (e.g., `your-username-country-US`) to select a specific location.
</Note>

With your Bright Data successfully integrated into Undetectable, you’re now ready to browse securely and anonymously. Enjoy enhanced privacy and seamless operations!
