# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/integration-guides/puppeteer.md

# Puppeteer

Puppeteer is a commonly used browser automation tool that can be useful for accessing and processing web pages programatically. In this guide, we'll walk you step-by-step through connecting  Puppeteer with Nimble IP used Node.js.&#x20;

{% hint style="info" %}
This guide assumes you have already installed Puppeteer and Node.js on the relevant computer/server.
{% endhint %}

To use Puppeteer with Nimble IP, first install the proxy-chain extension.

```bash
npm install puppeteer proxy-chain
```

With proxy-chain installed, we can now build our main script:

{% code overflow="wrap" %}

```javascript
const puppeteer = require('puppeteer');
const proxyChain = require('proxy-chain');

(async () => {
    const oldProxyUrl = 'http://account-accountName-pipeline-pipelineName:pipelinePassword@ip.nimbleway.com:7000'; // Replace with your Nimble Pipeline proxy credentials
    const newProxyUrl = await proxyChain.anonymizeProxy(oldProxyUrl);

    const browser = await puppeteer.launch({
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            `--proxy-server=${newProxyUrl}`, // Use the new anonymized proxy URL
        ],
    });

    const page = await browser.newPage();
    await page.goto('https://example.com'); // Replace with your target URL
    console.log('Page loaded');

    // Add any actions you want to perform on the page here

    // Close the anonymized proxy server
    await proxyChain.closeAnonymizedProxy(newProxyUrl, true);

    await browser.close();
})();
```

{% endcode %}

#### Explanation

1. **Anonymize the Proxy URL:** The `proxyChain.anonymizeProxy(oldProxyUrl)` function takes your proxy URL (which includes the username and password for authentication) and creates a new anonymized proxy URL. This URL will be used by Puppeteer to route its requests.
2. **Use the New Proxy URL in Puppeteer:** The new proxy URL is passed as an argument to Puppeteer's `launch` method. This lets Puppeteer connect through the proxy without needing to handle the authentication headers manually.
3. **Clean Up:** After your browsing is done, it’s good practice to close the anonymized proxy server using `proxyChain.closeAnonymizedProxy(newProxyUrl, true)`, which ensures that the server is not left running unnecessarily.

This method effectively integrates Nimble IP seamlessly with Puppeteer, allowing for all the benefits of Nimble IP to be used in conjunction with existing Puppeteer-based workflows.

If you're interested in upgrade to a modern data Browser, we recommend seeing [Nimble Unlocker Proxy](https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-functions/unlocker-proxy).
