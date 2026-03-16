# Source: https://docs.brightdata.com/integrations/switchyomega.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With SwitchyOmega

> Effortlessly manage your proxies with SwitchyOmega! Learn how to integrate Bright Data with this browser extension to enhance your privacy, streamline account management, and simplify web scraping workflows.

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

## What is SwitchyOmega?

**SwitchyOmega** is a browser extension for Chrome and Firefox designed to make proxy management easy and efficient. Supporting HTTP, HTTPS, SOCKS4, and SOCKS5, it allows you to create custom rules, switch between proxies effortlessly, and enhance your online activities. Whether you're bypassing geo-restrictions, managing multiple accounts, or safeguarding your privacy, SwitchyOmega is an essential tool for flexible proxy configurations.

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

## How to Set Up Bright Data With SwitchyOmega

**Step 1. Install SwitchyOmega**

1. Visit the relevant extension page for your browser:
   * [Chrome Extension](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=en)
   * [Firefox Add-on](https://addons.mozilla.org/en-US/firefox/addon/switchyomega)

2. Add SwitchyOmega to your browser. After installation, the SwitchyOmega icon will appear in your toolbar.

**Step 2. Create a New Proxy Profile**

1. Click the **SwitchyOmega icon** in your browser’s toolbar and select **Options** to open the settings page.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/switchyomega1.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=4a8b3f7dff81bb10f8575cf73677fdeb" alt="" width="184" height="225" data-path="images/integrations/switchyomega1.png" />
</Frame>

2. On the settings page, click **New Profile**.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/switchyomega2.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=bbc44723578caf34cba75ae9cd5eb952" alt="" width="285" height="155" data-path="images/integrations/switchyomega2.png" />
</Frame>

3. Provide a descriptive name for your profile (e.g., “Bright Data Proxy”), select **Proxy Profile**, and click **Create** to save.

<Frame as="div" style={{width:"70%", height:"auto"}}>
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/switchyomega3.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=e190c8b50f6f3d7f20934c9d366fd03a" alt="" width="592" height="610" data-path="images/integrations/switchyomega3.png" />
</Frame>

**Step 3. Configure Bright Data Proxy Details**

1. Enter the following Bright Data proxy details in the profile configuration fields:

   * **Protocol**: Choose HTTP, HTTPS, or SOCKS5 based on your proxy type.
   * **Server**: Input `http://brd.superproxy.io/`.
   * **Port**: Enter the port number provided in your [Bright Data dashboard](https://brightdata.com/cp/zones/page/plans).

2. Click the **Lock** icon to add authentication credentials:

   * **Username**: Your Bright Data username.
   * **Password**: Your Bright Data password.

3. Click **Save Changes** to store the proxy configuration.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/switchyomega4.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=577033a6c49cfd984b2de74f96bd5c68" alt="" width="291" height="228" data-path="images/integrations/switchyomega4.png" />
</Frame>

<Note>
  For country-specific proxies, append the country code to your username (e.g., `your-username-country-US`) to select a specific location.
</Note>

**Step 4. Apply and Activate the Proxy**

1. Click **Apply Changes** to finalize your setup.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/switchyomega5.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=f91b9b831e09df2ee7e218161cde9747" alt="" width="317" height="128" data-path="images/integrations/switchyomega5.png" />
</Frame>

2. To enable the proxy, select your configured profile from the SwitchyOmega dropdown menu in the browser toolbar.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/switchyomega6.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=2d3d977a0d0452b5edebf166bd1effb2" alt="" width="181" height="252" data-path="images/integrations/switchyomega6.png" />
</Frame>

Your Bright Data proxies are now fully integrated with SwitchyOmega. Whether you're managing multiple accounts, browsing securely, or scraping data efficiently, this setup ensures flexibility and control over your proxy configurations.
