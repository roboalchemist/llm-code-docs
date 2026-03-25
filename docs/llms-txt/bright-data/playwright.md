# Source: https://docs.brightdata.com/integrations/playwright.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With Playwright

> Streamline your web automation with Bright Data and Playwright. This guide shows you how to configure secure, anonymous proxies that reduce detection risks and keep your tasks running smoothly.

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

## What is Playwright?

Playwright is a versatile Node.js toolkit for automating popular browsers in one go. Whether you’re scraping data, testing applications, or building seamless automation flows, Playwright’s unified interface and robust features help you get more done in less time—without compromising quality.

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session)

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access)

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

## How to Integrate Bright Data With Playwright

### Prerequisites

1. **Node.js**: Download and install the latest version from [nodejs.org](https://nodejs.org/).

2. **Playwright Package**: Add Playwright to your project:

3. **Bright Data Account**: You must have an active Bright Data account with at least one enabled proxy zone.\
   For browser automation use cases, **ISP or Data Center proxies are recommended** for better stability.

4. **Proxy Access Permissions**: Ensure your IP is allowlisted in the Bright Data dashboard (if IP whitelisting is enabled) and that your proxy zone is active.

5. **Supported Operating System**: Playwright is supported on the following operating systems:

   * macOS
   * Linux
   * Windows

   Make sure your system meets Playwright’s browser runtime requirements.

6. **Basic JavaScript Knowledge**: Familiarity with JavaScript, Node.js, and `async/await` syntax is recommended to correctly configure and manage Playwright scripts.

7. **Network Stability**: A stable internet connection is required to download browser binaries and maintain proxy connections during automation tasks.

```bash  theme={null}
npm install playwright
```

### Get Your Bright Data Credentials

Log in to your [Bright Data dashboard](https://brightdata.com/cp/zones/page/plans) and note the following details:

* **Host**: [http://brd.superproxy.io/](http://brd.superproxy.io/)
* **Port**: `33335`
* **Username**: Enter your Bright Data `username`.
* **Password**: Enter your Bright Data `password`.

You’ll need these for proxy authentication.

### Configure Playwright to Use Bright Data

<Note>
  If you want to use Playwright with Bright Data's Browser API, please refer to the [Browser API documentation](https://docs.brightdata.com/scraping-automation/scraping-browser/introduction) for correct setup and code examples. Proxy Integration guides below are for direct proxy integration, not for Browser API.
</Note>

1. **Set the Proxy Server**: Include your Bright Data host and port in the browser launch options. Use the format `host:port`.
2. **Add Authentication**: Provide your Bright Data **username** and **password** to ensure secure access.

### Ignoring SSL Errors

If you get SSL errors working our residential proxies or Unlocker API set: `ignoreHTTPSErrors: True` in your JS code. Alternatively - you can setup our certificate on your system or import it into your code. More access information can be found [here](https://docs.brightdata.com/integrations/playwright#expand-to-get-your-bright-data-proxy-access-information).

### Example Code

```javascript  theme={null}
import { chromium } from 'playwright';

// Bright Data proxy configuration
const BRIGHTDATA_HOST = process.env.BRIGHTDATA_HOST || 'brd.superproxy.io';
const BRIGHTDATA_PORT = process.env.BRIGHTDATA_PORT || '33335';
const BRIGHTDATA_USERNAME = process.env.BRIGHTDATA_USERNAME;
const BRIGHTDATA_PASSWORD = process.env.BRIGHTDATA_PASSWORD;

// Optional: use session to keep the same IP
const SESSION_ID = 'session_1';

(async () => {
  const browser = await chromium.launch({
    headless: true, // set to false for debugging
    proxy: {
      server: `http://${BRIGHTDATA_HOST}:${BRIGHTDATA_PORT}`,
      username: `${BRIGHTDATA_USERNAME}-session-${SESSION_ID}`,
      password: BRIGHTDATA_PASSWORD,
    },
  });

  const context = await browser.newContext({
    ignoreHTTPSErrors: true, // prevents SSL issues with residential / Unlocker proxies
  });

  const page = await context.newPage();

  // Verify proxy connection
  await page.goto('https://lumtest.com/myip.json', {
    waitUntil: 'networkidle',
    timeout: 60000,
  });

  const ipInfo = await page.textContent('pre');
  console.log('Proxy IP info:', ipInfo);

  // Navigate to target website
  await page.goto('https://example.com', {
    waitUntil: 'domcontentloaded',
  });

  console.log('Page title:', await page.title());

  // Optional screenshot for validation
  await page.screenshot({ path: 'playwright-brightdata.png' });

  await browser.close();
})();
```

With **Bright Data** integrated into **Playwright**, your automation is both secure and discreet. Enjoy faster workflows, reduced detection risks, and greater peace of mind as you scrape, test, and automate online tasks.
