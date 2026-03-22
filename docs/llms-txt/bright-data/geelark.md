# Source: https://docs.brightdata.com/integrations/geelark.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Use Bright Data With Geelark

> Integrate Bright Data with Geelark to maximize your privacy and efficiency. This guide walks you through configuring Bright Data proxies for secure and anonymous browsing using Geelark.

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

## What is Geelark?

**Geelark** is a versatile browser profile management tool designed for privacy-conscious users and professionals. It allows you to create isolated browser environments, manage multiple accounts, and customize browsing profiles to suit your needs. With Bright Data, you can take your Geelark profiles to the next level by ensuring anonymity, bypassing restrictions, and accessing geo-specific content.

## How to Integrate Bright Data With Geelark

<Steps>
  <Step title="Prerequisites">
    1. **Bright Data Proxy Credentials**:
       * Log in to your [Bright Data dashboard](https://brightdata.com/cp/zones) to get your **Host**, **Port**, **Username**, and **Password**.
       * Use a geo-specific username if you need a proxy from a specific location (e.g., `your-username-country-US`).

    2. **Geelark Installed**:
       * Download and install Geelark from [geelark.com](https://geelark.com/).
       * Launch Geelark and log in using your account credentials.
       * If you don’t have an account, click on **Sign Up** to create one.
  </Step>

  <Step title="Create and Configure a New Profile">
    1. On the Geelark dashboard, click on **New Profile**.
    2. Enter a **Name** and select the desired operating system for the profile.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/geelark1.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=7546f2a42022fca4850912aaf492ce51" alt="" width="761" height="239" data-path="images/integrations/geelark1.png" />
    </Frame>
  </Step>

  <Step title="Configure Proxy Settings">
    1. In the **Proxy Settings** section, select the **Custom** option.

    2. Choose the **Proxy Type** (HTTP, HTTPS, or SOCKS5) based on your Bright Data configuration.

    3. Enter the following Bright Data proxy details:
       * **Proxy Host**: `http://brd.superproxy.io/`.
       * **Port**: Use the port number provided in your [Bright Data dashboard](https://brightdata.com/cp/zones).
       * **Username**: Your Bright Data `username`.
       * **Password**: Your Bright Data `password`.

    4. Click on **Check Proxy** to verify the proxy settings. Ensure the connection is successful before proceeding.
  </Step>

  <Step title="Save and Launch the Profile">
    1. After configuring the proxy settings, click on **OK** to save the profile.
    2. On the Geelark dashboard, locate the newly created profile and click on **Start** to launch it.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/geelark2.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=4f1c3639177b6f56d0a8c0f4ce04d472" alt="" width="1198" height="241" data-path="images/integrations/geelark2.png" />
    </Frame>
  </Step>

  <Step title="Test Your Setup">
    1. Within the launched profile, open a web browser.
    2. Navigate to [httpbin.org/ip](http://httpbin.org/ip) to verify that your IP address reflects the Bright Data, confirming that the setup is successful.
  </Step>
</Steps>

Integrating Bright Data with Geelark gives you a powerful combination of privacy, control, and efficiency. Whether you’re managing multiple browser profiles, accessing geo-restricted content, or ensuring secure connections, Bright Data helps you achieve your goals seamlessly. Try it out today and elevate your Geelark experience!
