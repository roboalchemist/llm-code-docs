# Source: https://docs.brightdata.com/integrations/antik.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With Antik

> Integrate Bright Data with Antik to enhance your online anonymity, streamline your tasks, and securely manage browser profiles. Follow this step-by-step guide to configure Bright Data with Antik for efficient and private browsing.

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

## What is Antik?

Antik is a browser-based automation tool designed for users managing multiple accounts, web scraping, and geo-targeted activities. With Bright Data, Antik ensures a secure and private environment for all your automation and browsing needs.

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

## Why Use Bright Data With Antik?

* **Privacy**: Protect your IP address and online identity.

* **Geo-Targeting**: Access region-specific content with Bright Data’s country-specific proxies.

* **Reliability**: Enjoy stable connections for uninterrupted workflows.

## How to Integrate Bright Data With Antik

**Step 1. Download and Log In to Antik**

1\. Visit the [official Antik website](https://antik.io/) and download the application.

2\. Install the software and log in using your account credentials.

**Step 2. Create a New Browser Profile**

1\. From the Antik dashboard, navigate to the **Profiles** tab.

2\. Click **Create** to start configuring a new browser profile.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/antik1.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=8d3af89a0127bb45b18df3c21a7882bb" alt="" width="1418" height="197" data-path="images/integrations/antik1.png" />
</Frame>

**Step 3. Enable Proxy Settings**

1\. Under the **General Settings** tab, locate the **Name** field and enter a recognizable name for your profile to help you identify it later.

2\. Navigate to the **New Proxy** tab.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/antik2.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=dbd86a0aa2fa9db874262b25950cce11" alt="" width="951" height="573" data-path="images/integrations/antik2.png" />
</Frame>

**Step 4. Add Your Bright Data Proxy Details**

1\. Go to your [Bright Data dashboard](https://brightdata.com/cp/zones) and click on the your proxy zone.

2\. Under the **Overview** tab, copy the proxy information in the format of:&#x20;

`host : port : username : passoword `(no spaces).&#x20;

3\. Paste this access information into the **Proxy** field in Antik.

4\. Once the proxy configuration is verified, click **Create** to save your proxy settings.

<Note>
  For geo-targeted proxies, format your username as `your-username-country-XX` (e.g., `your-username-country-US`) to specify a location.
</Note>

**Step 5. Save and Launch**

1\. Go to the **Profiles** tab and select your newly created profile.

2\. Click **Start** to launch the browser with the configured Bright Data settings.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/antik3.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=1602420aaca86975f7310438cebdf3f2" alt="" width="1216" height="244" data-path="images/integrations/antik3.png" />
</Frame>

By integrating Bright Data with Antik, you ensure secure and efficient browsing, making your workflows smooth and private. Whether managing multiple accounts or targeting specific regions, Bright Data provides the reliability you need to stay ahead. Get started today for a seamless browsing experience!
