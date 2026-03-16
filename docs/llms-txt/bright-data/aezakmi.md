# Source: https://docs.brightdata.com/integrations/aezakmi.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With Aezakmi

> Enhance your anonymity and streamline your online tasks with Bright Data in Aezakmi. Follow this guide to configure secure and reliable proxy connections for your browser profiles.

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

## What is Aezakmi?

Aezakmi is a browser automation tool designed for marketers, researchers, and developers who require multiple browser profiles with unique configurations. With Bright Data, you can ensure secure, anonymous, and location-targeted browsing while avoiding IP bans and tracking.

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

## Why Use Bright Data With Aezakmi?

* **Enhanced Privacy**: Mask your real IP address for secure browsing.

* **Geo-Targeting**: Access region-specific content with country-specific proxies.

* **Consistent Performance**: Ensure reliable and uninterrupted connections for all your browser profiles.

## How to Integrate Bright Data With Aezakmi

Follow these steps to configure Bright Data proxies in Aezakmi:

**Step 1. Install and Log In to Aezakmi**

1\. Download and install Aezakmi from the [official website](https://aezakmi.run/).

2\. Open the application and log in with your account credentials.

**Step 2. Create a New Browser Profile**

1\. Navigate to your [dashboard](https://account.aezakmi.run/#/dashboard) or click **Create New Profile** in the **Aezakmi Extension**.

2\. Configure your profile by selecting parameters such as:

* **Operating System**

* **Browser**

* **Screen Resolution**

* **Videocard Model**

3\. Click **Generate Fingerprint** to create a unique browser fingerprint profile tailored to your setup.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/aezakmi1.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=0a988c15688206e9c18144fe61f321f9" alt="" width="1080" height="643" data-path="images/integrations/aezakmi1.png" />
</Frame>

**Step 3. Enable Proxy for Your Profile**

1\. In the profile setup screen, enter a descriptive name in the **Profile Name** field to easily identify the profile later.

2\. Toggle **Enable Proxy** to *On* to activate the proxy configuration options.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/aezakmi2.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=9254815a47def3bfc1c8137dacf4d669" alt="" width="1099" height="182" data-path="images/integrations/aezakmi2.png" />
</Frame>

**Step 4. Configure Proxy Settings**

1\.  Under the proxy settings section, enter your Bright Data proxy details:

* **Protocol**: Choose HTTP, HTTPS, or SOCKS5 based on your proxy type.

* **Address**: Enter [`http://brd.superproxy.io/`.](http://brd.superproxy.io/.)

* **Port**:  33335

* **User**: Input your Bright Data username.

* **Password**: Input your Bright Data password.

2\. Click **Check Proxy** to verify your connection. Ensure the test completes successfully.

<Note>
  For geo-targeted proxies, include the country code in the username, formatted as `your-username-country-XX` (e.g., `your-username-country-US`).
</Note>

**Step 5. Save and Launch**

* Once your proxy details are verified, click **Save Fingerprint** to apply the settings and save the profile.

By integrating Bright Data with Aezakmi, you can unlock a secure and efficient browsing experience. Whether managing multiple accounts, scraping data, or accessing geo-restricted content, Bright Data ensures privacy, reliability, and performance. Get started today to maximize your productivity!
