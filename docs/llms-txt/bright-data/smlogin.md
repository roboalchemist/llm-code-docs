# Source: https://docs.brightdata.com/integrations/smlogin.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With SMLogin

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

## What is SMLogin?

SMLOGIN, a cutting-edge anti-correlation fingerprint browser, offers a robust solution for users needing to operate multiple accounts across various platforms efficiently. By simulating real devices and providing a multi-account/multi-platform secure operation environment, SMLOGIN stands out for its ease of use, reduced resource consumption, and comprehensive security features.

Integrating SMLOGIN with Bright Data's proxies further amplifies these benefits, providing users with an unmatched level of anonymity, security, and flexibility in their online operations.

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

## Benefits of Using Bright Data Proxies

The synergy between SMLOGIN and [Bright Data's proxy services](https://brightdata.com/proxy-types) brings forth an unparalleled solution for digital marketers, e-commerce operators, and data analysts who manage numerous accounts. Here's why this combination is a game-changer:

* **Unmatched Global Network:** Bright Data offers access to an unparalleled network of over 72 million [real residential IPs worldwide](https://brightdata.com/proxy-types/residential-proxies), covering data centers, residential areas, and mobile networks. This vast selection ensures SMLOGIN users can seamlessly manage accounts from any geographic location, crucial for tasks requiring specific regional access.
* **Superior Anonymity and Security**: Operating multiple accounts demands a high level of anonymity to prevent detection and potential bans. Bright Data's proxies provide robust security features that safeguard users' digital footprints, ensuring each SMLOGIN session remains undetectable and secure from prying eyes.
* **High-Speed Performance:** Speed is of the essence in today's fast-paced digital environment. Bright Data's efficient proxy servers guarantee minimal latency and fast loading times, enhancing SMLOGIN's performance and allowing for quicker operations across multiple accounts.
* **Cost-Effective and Resource-Efficient:** Compared to the high costs associated with cloud servers and virtual machines, Bright Data's proxy solutions offer a more economical and resource-efficient alternative for managing multiple accounts. This efficiency is particularly beneficial for users leveraging SMLOGIN for extensive e-commerce operations and social media campaigns.
* **Flexible and Scalable Solutions:** Bright Data's proxy services are designed to be highly flexible, catering to a [wide array of use cases](https://brightdata.com/use-cases) from web scraping and competitive analysis to social media management and e-commerce operations. Whether you're managing a handful of accounts or thousands, Bright Data's infrastructure can scale to meet your needs without compromising on quality or security.
* **Easy Integration and Comprehensive Support:** Integrating Bright Data proxies with SMLOGIN is straightforward, ensuring users can quickly set up and start managing their accounts with enhanced anonymity and efficiency. Furthermore, Bright Data offers extensive documentation and dedicated support, assisting users in maximizing their use of proxies with SMLOGIN for optimal results.

By integrating SMLOGIN with Bright Data's proxy solutions, users unlock a potent combination for multi-account management, bolstered by unmatched security, global reach, and operational efficiency.

## SMLOGIN Proxy Integration

Follow this step-by-step guide to integrate our proxy services with SMLOGIN in a few minutes.

<Frame caption="Software download page with download button highlighted">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/smlogin19.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=f21f1cad61a4859119ee03c41a9a2344" alt="smlogin19.png" width="1999" height="1250" data-path="images/integrations/smlogin19.png" />
</Frame>

### Register and Download SMLOGIN

Begin by registering for an account at [SMLOGIN's registration page](https://sys.smlogin.cc/#/passport/register).

Download the SMLOGIN application compatible with Windows 7 and above from SMLOGIN Downloads.

<Frame caption="Login page with email and password fields">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/smlogin17.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=2c5e19c3896e7b7b88e0c0e895eb8364" alt="smlogin17.png" width="1366" height="768" data-path="images/integrations/smlogin17.png" />
</Frame>

### Installation and Account Login

Install the SMLOGIN application following the on-screen instructions.

Launch SMLOGIN and log into your account using your credentials.

<Frame caption="Browser window showing SMLogin interface and options">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/smlogin11.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=19f4acf5f5936aff6f82172f302f4e3b" alt="smlogin11.png" width="1366" height="768" data-path="images/integrations/smlogin11.png" />
</Frame>

### Creating a New Profile

In the SMLOGIN dashboard, click on the “+ one-click new profiles” button to create a new browser profile.

<Frame caption="Creating a new profile in application interface">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/smlogin13.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=6132d12ae4cf29f6946c4c81f7e63638" alt="smlogin13.png" width="1366" height="768" data-path="images/integrations/smlogin13.png" />
</Frame>

### Setting Up the Profile

Customize your new profile according to your preferences, including setting up browser fingerprints, screen resolution, and any other specifics relevant to your browsing or operational needs.

<Frame caption="Browser view of profile management screen">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/smlogin22.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=dc869bf6bd4d9b7ce377e20f30ac997b" alt="smlogin22.png" width="1366" height="768" data-path="images/integrations/smlogin22.png" />
</Frame>

### Binding IP to the Profile

Once the profile setup is complete, it will appear on the dashboard. Next to the newly created profile, find and click the “Bind IP” option to proceed with configuring the proxy settings.

<Frame caption="Software showing proxy IP options for configuration">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/smlogin5.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=9a0da0d0b412ca325f00bfd18183cb28" alt="smlogin5.png" width="1366" height="768" data-path="images/integrations/smlogin5.png" />
</Frame>

### Configuring the Proxy

From the “Proxy Type” dropdown menu select “HTTP” for default Bright Data proxy use. If using Bright Data's Residential Proxies, you may also choose “Luminati (Residential)” from the dropdown list.

<Frame caption="Proxy settings: IP brd.superproxy.io with port 33335.">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/smlogin6.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=dee5324c4dc2cd3fa7fa5dfa8c577688" alt="smlogin6.png" width="1366" height="768" data-path="images/integrations/smlogin6.png" />
</Frame>

### Entering Proxy Details

Fill in the proxy details: Host, Port, Username, and Password.

* **Host**: Enter the proxy server address brd.superproxy.io
* **Port**: Specify the proxy port as 33335
* **Username**: Your Bright Data username
* **Password**: Your Bright Data password

<Frame caption="Software interface showing proxy IP settings and information">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/smlogin2.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=18ce9985459c967222f067efcb0135f5" alt="smlogin2.png" width="1366" height="768" data-path="images/integrations/smlogin2.png" />
</Frame>

### Verifying the Proxy Connection

Click on the “check proxy” button to test the connectivity. You should see your proxy IP and location details if the setup is successful.

<Frame caption="Proxy IP settings window on SMLOGIN application">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/smlogin16.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=daeee78646eb2d1e05e16e3f2e68b3cb" alt="smlogin16.png" width="1366" height="768" data-path="images/integrations/smlogin16.png" />
</Frame>

### Saving the Proxy Configuration

After confirming the proxy details are correct and the test is successful, click on “Save proxy” to finalize the proxy settings for the profile.

<Frame>
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/smlogin8.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=a225abed5bbb6c481f78cf60ca4de1d0" alt="smlogin8.png" width="1366" height="768" data-path="images/integrations/smlogin8.png" />
</Frame>

### Launching the Profile

Open the profile you've just configured by clicking on it. Now, you're all set to browse the internet securely and efficiently, powered by Bright Data proxies.

<Warning>
  **Important note**:

  If you are using Bright Data’s Residential Proxies, Unlocker API or SERP API, you need to install an SSL certificate to enable end-to-end secure connections to your target website(s).

  This is a simple process, see [this guide](https://docs.brightdata.com/general/account/ssl-certificate#installation-of-the-ssl-certificate) for instructions.
</Warning>
