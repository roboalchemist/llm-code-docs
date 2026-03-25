# Source: https://docs.brightdata.com/integrations/shadowrocket.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With Shadowrocket

> Learn how to integrate Bright Data with Shadowrocket for secure and seamless browsing on your iOS device. Follow this step-by-step guide to configure proxies and enhance your online privacy.

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

## What is Shadowrocket?

**Shadowrocket** is a powerful iOS app designed to route network traffic through proxies. It supports various proxy types, including HTTP, HTTPS, and SOCKS5, and is popular for its flexibility and ease of use, making it a favorite choice for secure browsing and data management.

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

## How to Integrate Bright Data With Shadowrocket

### Step 1: Install Shadowrocket

1. Open the **App Store** on your iOS device.
2. Search for **Shadowrocket** and download the app.
3. Install the application and open it after installation.

### Step 2: Add a New Proxy Configuration

1. Open the **Shadowrocket** app.
2. Tap the **+** button in the top-right corner to add a new proxy.

### Step 3: Configure Proxy Settings

1. In the configuration window:
   * **Type**: Select HTTP, HTTPS, or SOCKS5 based on your proxy type.
   * **Server**: Enter `http://brd.superproxy.io/`.
   * **Port**: Use the port number provided in your [Bright Data dashboard](https://brightdata.com/cp/zones/page/plans).
   * **Username**: Input your Bright Data username.
   * **Password**: Input your Bright Data password.

2. Save the configuration by tapping **Done** or **Save** in the top-right corner.

### Step 4: Test Your Proxy

1. Go back to the main **Shadowrocket** screen.
2. Enable the proxy by toggling the switch next to your newly created configuration.
3. Open a browser or app and visit [httpbin.org/ip](http://httpbin.org/ip) to verify that the proxy is working correctly.

<Note>
  If you require proxies for specific locations, format your username as `your-username-country-XX` (e.g., `your-username-country-US`) to connect through a proxy from that region.
</Note>

### You're All Set!

Your Shadowrocket app is now integrated with Bright Data. Enjoy secure, private, and anonymous browsing, enhanced with flexible geo-targeting options and seamless performance.
