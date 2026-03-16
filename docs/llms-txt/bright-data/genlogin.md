# Source: https://docs.brightdata.com/integrations/genlogin.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Use Bright Data With GenLogin

> Securely manage multiple browser profiles with Bright Data and GenLogin. This guide will walk you through the steps to integrate Bright Data with GenLogin for anonymous and efficient browsing.

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

## What is GenLogin?

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

**GenLogin** is an advanced browser profile management tool designed for professionals handling multiple accounts or projects. It enables the creation of isolated browser environments, ensuring each profile operates securely and independently. By integrating **Bright Data**, you can enhance GenLogin’s capabilities with reliable, anonymous proxy connections.

## How to Integrate Bright Data With GenLogin

<Steps>
  <Step title="Download and Open GenLogin">
    1. Visit the [GenLogin website](https://genlogin.com/) and download the application compatible with your operating system.
    2. Install GenLogin by following the on-screen instructions and launch the application.
    3. Log in to your GenLogin account. If you don’t have one, sign up for free.
  </Step>

  <Step title="Create or Edit a Browser Profile">
    1. From the GenLogin dashboard, click **Create Profile** to create a new profile or select an existing one to edit.
    2. In the profile settings, give your profile a unique and recognizable name in the **Name** field.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/genlogin1.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=738bd248bd82d4d91a4c781d8cf2b73f" alt="" width="1319" height="285" data-path="images/integrations/genlogin1.png" />
    </Frame>
  </Step>

  <Step title="Configure Proxy Settings">
    1. Scroll to the **Network** section in the profile setup.

    2. Choose **Your Proxy** and input your Bright Data details:
       * **Proxy Type**: Select HTTP, HTTPS, or SOCKS5.
       * **Proxy Host**: Enter `http://brd.superproxy.io/`.
       * **Proxy Port**: Use the port provided in your [Bright Data dashboard](https://brightdata.com/cp/zones/page/plans).
       * **Username**: Input your Bright Data username.
       * **Password**: Enter your Bright Data password.

    3. To ensure accuracy, click **Check Proxy** to verify the connection.
  </Step>

  <Step title="Save and Launch the Profile">
    1. Once the proxy details are successfully verified, click **Create profile** to apply the settings.
    2. Navigate to the **Profiles** section and find the profile you just created.
    3. Click **Start** to open the browser with the configured settings.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/genlogin2.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=9a01437f4dbd28395c57a609fb18dc96" alt="" width="1900" height="307" data-path="images/integrations/genlogin2.png" />
    </Frame>
  </Step>

  <Step title="Verify Proxy Connection">
    1. Within the launched profile, open a browser and navigate to [httpbin.org/ip](http://httpbin.org/ip).
    2. Confirm that the displayed IP matches your Bright Data proxy, verifying the setup.
  </Step>
</Steps>

Integrating Bright Data with GenLogin enhances your ability to manage multiple accounts securely and efficiently. With Bright Data’s reliable proxies and GenLogin’s robust browser profile management, you can achieve unparalleled privacy and productivity. Start leveraging the power of Bright Data and GenLogin today!
