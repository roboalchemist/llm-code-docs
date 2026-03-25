# Source: https://docs.brightdata.com/integrations/chrome.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Configure Proxy Settings in Chrome

> Transform your browsing with proxies in Chrome! They’re perfect for safeguarding your privacy, accessing restricted sites, and juggling multiple accounts. In this guide, we’ll walk you through the setup and help you make the most of Chrome proxies.

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

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

## Changing Proxy Settings in Chrome

Ready to unlock the power of proxies in Chrome? It’s simple—just follow these steps and you’re good to go:

### Step 1. **Access Chrome Settings**.

Open Chrome, click on the **three-dot menu** in the top-right corner, and choose **Settings** from the dropdown.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/chrome1.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=ee217bf9e2cb45c47b0a8b97651eceee" alt="" width="336" height="801" data-path="images/integrations/chrome1.png" />
</Frame>

### Step 2. **Open System Proxy Settings**.

Navigate to the **System** section and select **Open your computer’s proxy settings** to proceed.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/chrome2.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=0e826ecbe659a9ca8734f974763c4d9e" alt="" width="1276" height="724" data-path="images/integrations/chrome2.png" />
</Frame>

### Step 3. **Configure Proxy in Your Operating System**.

Since Chrome uses your operating system’s proxy settings, you’ll be redirected to the system configuration screen. Follow these steps based on your OS:

* **On Windows**: Enable “Use a proxy server,” then enter the proxy address and port provided in your [Bright Data dashboard](https://brightdata.com/cp/zones).
* **On macOS**: Select the appropriate protocol (like HTTP or SOCKS5) and input the proxy address, port, and credentials. It’s quick and straightforward!

All done! Your Chrome browser is now set up with **Bright Data**. Whether you’re managing accounts, shopping worldwide, or browsing privately, you’re ready for a secure and seamless experience.
