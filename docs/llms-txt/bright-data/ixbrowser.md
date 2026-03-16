# Source: https://docs.brightdata.com/integrations/ixbrowser.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Integrate Bright Data With IXBrowser

> Streamline your account management and secure your browsing with Bright Data and IXBrowser. Follow this guide to configure Bright Data for a seamless and anonymous experience using IXBrowser.

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

## What is IXBrowser?

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

**IXBrowser** is a privacy-focused anti-detect browser tailored for managing multiple accounts across different platforms. It provides advanced anonymity features, allowing users to bypass restrictions and avoid detection. Integrating Bright Data with IXBrowser further enhances privacy and enables geo-targeted browsing.

## How to Integrate Bright Data With IXBrowser

<Steps>
  <Step title="Download and Install IXBrowser">
    1. Visit the [IXBrowser website](https://ixbrowser.com/) and download the application.
    2. Install the software and log in using your account credentials.
  </Step>

  <Step title="Create a New Profile">
    1. Open IXBrowser and navigate to the **Profile List** section under **Browser Profile**.
    2. Click **Create New Profile** to begin setting up a new browser instance.
    3. In the profile settings, provide a descriptive name in the **Profile Name** field to easily identify your profile later.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/mDnOYJMdf2BWnkdI/images/integrations/ixbrowser1.png?fit=max&auto=format&n=mDnOYJMdf2BWnkdI&q=85&s=5aacb1c42002326d974009aad0cc0dad" alt="" width="1364" height="197" data-path="images/integrations/ixbrowser1.png" />
    </Frame>
  </Step>

  <Step title="Configure Proxy Settings">
    1. Switch to the **Proxy Configuration** tab within the profile setup page.

    2. Toggle **Custom** to enable the proxy setup options.

    3. Fill in the following proxy details retrieved from your [Bright Data dashboard](https://brightdata.com/cp/zones):
       * **Proxy Type**: Choose HTTP, HTTPS, or SOCKS5 depending on your proxy type.
       * **Proxy Host**: `http://brd.superproxy.io/`
       * **Proxy Port**: Enter the port number from your Bright Data dashboard.
       * **Proxy Account**: Use your Bright Data `username`.
       * **Proxy Password**: Use your Bright Data `password`.

    4. Once you’ve entered the details, click **Create** to save the configuration.

    <Note>
      For geo-targeted proxies, format your username as `your-username-country-XX` (e.g., `your-username-country-US`) to access a specific region.
    </Note>
  </Step>

  <Step title="Launch the Profile">
    1. Navigate back to the **Profile List** section.
    2. Locate your newly created profile and click **Open** to launch the browser with the configured Bright Data proxy settings.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/mDnOYJMdf2BWnkdI/images/integrations/ixbrowser2.png?fit=max&auto=format&n=mDnOYJMdf2BWnkdI&q=85&s=3af64492251d72bfa6fedf2267d297f8" alt="" width="1353" height="278" data-path="images/integrations/ixbrowser2.png" />
    </Frame>
  </Step>
</Steps>

Integrating Bright Data with IXBrowser ensures private and reliable account management while enhancing your online anonymity. Whether you’re managing multiple accounts or performing geo-targeted activities, this setup empowers you with secure and seamless browsing. Get started now for a more efficient experience!
