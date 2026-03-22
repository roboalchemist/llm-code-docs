# Source: https://docs.brightdata.com/integrations/sphere-browser.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Integrate Bright Data With Sphere Browser

> Integrate Bright Data with Sphere Browser to manage multiple accounts securely and anonymously. Follow this step-by-step guide for a seamless configuration.

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

## What is Sphere Browser?

**Sphere Browser** is an anti-detect browser designed for managing multiple accounts without risking detection. It allows users to create unique browser profiles with isolated fingerprints, making it an ideal tool for marketing professionals, e-commerce, and privacy enthusiasts. Integrating Bright Data with Sphere Browser enhances anonymity and unlocks geo-targeted capabilities.

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

## How to Integrate Bright Data With Sphere Browser

**Step 1. Download and Install Sphere Browser**

1. Visit the [Sphere Browser website](https://linkensphere.info/en/#) and download the application.
2. Install the software on your device and log in with your account credentials.
3. Open Sphere Browser and click **Proxy** to begin configuring your setup.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/sphere-browser1.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=9628f5148f9102fa919f3d5b2a7cab70" alt="" width="1595" height="164" data-path="images/integrations/sphere-browser1.png" />
</Frame>

**Step 2. Configure Proxy Settings**

1. In the profile creation window, provide a unique and descriptive name in the **Profile Name** field to identify your browser instance easily.
2. Go to your [Bright Data dashboard](https://brightdata.com/cp/zones) 
3. Under the **Overview** tab, in the **Access Details** section, compose in a text editor the connect string in the following format: `` host:port:username:password` ``
4. Return to Sphere Browser and paste the credentials into the appropriate field.
5. Click the **Create** button (icon with a checkmark) to save the proxy settings.

<Note>
  For geo-targeted proxies, format your username as `your-username-country-XX` (e.g., `your-username-country-US`) to select a specific location.
</Note>

**Step 3. Launch and Verify**

1. Locate the profile you just configured.
2. Click **Check Proxy** to ensure the connection is successful.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/sphere-browser2.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=843c007caa62a9247e15d2876c39a1e2" alt="" width="1278" height="209" data-path="images/integrations/sphere-browser2.png" />
</Frame>

Integrating Bright Data with Sphere Browser ensures a secure and anonymous browsing experience tailored to your needs. Whether managing multiple accounts or exploring geo-restricted content, this setup gives you the privacy and flexibility you need. Start leveraging the power of Bright Data and Sphere Browser today!
