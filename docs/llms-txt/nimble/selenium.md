# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/integration-guides/selenium.md

# Selenium

Selenium is a popular web browsing automation tool used in website testing and web scraping applications. In this guide, we'll walk you through the simple steps to connect Nimble IP with Selenium using Node.js.

{% hint style="info" %}
This guide assumes you have already installed Selenium and Node.js on the relevant computer/server.
{% endhint %}

&#x20;First, we install the `proxy-chain` extension which will help us authenticate Selenium requests to Nimble IP:

```bash
npm install selenium-webdriver proxy-chain
```

With `proxy-chain` installed, we can now build our main script:

{% code overflow="wrap" %}

```javascript
const { Builder } = require('selenium-webdriver');
const proxyChain = require('proxy-chain');
const chrome = require('selenium-webdriver/chrome');

(async () => {
    const oldProxyUrl = 'http://account-accountName-pipeline-pipelineName:pipelinePassword@ip.nimbleway.com:7000'; // Replace with your actual proxy credentials and URL
    const newProxyUrl = await proxyChain.anonymizeProxy(oldProxyUrl);

    const options = new chrome.Options();
    options.addArguments(`--proxy-server=${newProxyUrl}`);

    const driver = await new Builder()
        .forBrowser('chrome')
        .setChromeOptions(options)
        .build();

    try {
        await driver.get('https://example.com'); // Replace with your target URL
        console.log('Page loaded');
        
        // Add any actions you want to perform on the page here

    } finally {
        await driver.quit();
        await proxyChain.closeAnonymizedProxy(newProxyUrl, true);
    }
})();
```

{% endcode %}

#### Explanation

1. **Anonymize the Proxy URL:**  `proxyChain.anonymizeProxy(oldProxyUrl)` is used to create a new anonymized proxy URL that encapsulates authentication details.
2. **Configure Selenium to Use the Proxy:** The new proxy URL is added to Chrome’s launch options via the `addArguments` method. This instructs Selenium's Chrome WebDriver to route all requests through the anonymized proxy server.
3. **Clean Up:** It’s important to properly close both the Selenium driver and the anonymized proxy server after your tests are complete to ensure no resources are left hanging.

This setup allows you to use Nimble IP with Selenium in a clean and efficient manner, handling authentication seamlessly and avoiding manual proxy configuration complexities.
