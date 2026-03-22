# Source: https://scrapfly.io/docs/proxy-saver/certificates

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/proxy-saver/certificates

Markdown Content:
Certificate Configuration
-------------------------

To use Proxy Saver with HTTPS and SSL connections you need to configure your proxy tool to trust the Scrapfly Proxy Saver TLS certificate or ignore certificate verification process. Here's how to do it with popular proxy tools.

[Quick Install](https://scrapfly.io/docs/proxy-saver/certificates#install)
--------------------------------------------------------------------------

Run this one-liner to automatically install the certificate for your OS (Linux, macOS, WSL):

`curl -sL https://scrapfly.io/install-ca.sh | sh`

[Download the Certificate](https://scrapfly.io/docs/proxy-saver/certificates#download)
--------------------------------------------------------------------------------------

Download the certificate directly:

`curl -o scrapfly-ca.crt https://scrapfly.io/ca.crt`

Or find it in the [Proxy Saver dashboard](https://scrapfly.io/dashboard/proxy-saver) under each proxy profile.

[Container Configuration](https://scrapfly.io/docs/proxy-saver/certificates#containers)
---------------------------------------------------------------------------------------

When using Docker, you can download and install the Proxy Saver certificate directly during the image build:

*   [Debian](https://scrapfly.io/docs/proxy-saver/certificates#debian-image)
*   [Alpine](https://scrapfly.io/docs/proxy-saver/certificates#alpine-image)

```
# Dockerfile example for Debian-slim
FROM debian:bullseye-slim

# Install ca-certificates and curl
RUN apt-get update && apt-get install -y --no-install-recommends \
ca-certificates curl && \
rm -rf /var/lib/apt/lists/*

# Download and install the Proxy Saver certificate
RUN curl -fsSL -o /usr/local/share/ca-certificates/scrapfly-ca.crt https://scrapfly.io/ca.crt && \
update-ca-certificates
```

```
# Dockerfile example for Alpine
FROM alpine:latest

# Install ca-certificates and curl
RUN apk add --no-cache ca-certificates curl

# Download and install the Proxy Saver certificate
RUN curl -fsSL -o /usr/local/share/ca-certificates/scrapfly-ca.crt https://scrapfly.io/ca.crt && \
update-ca-certificates
```

[HTTP Tools](https://scrapfly.io/docs/proxy-saver/certificates#cli-tools)
-------------------------------------------------------------------------

Each CLI tool like `curl` has a custom certificate option using which we can specify the location of the Proxy Saver `scrapfly-ca.cert` certificate file:

*   [CURL](https://scrapfly.io/docs/proxy-saver/certificates#curl-basic)
*   [HTTPIE](https://scrapfly.io/docs/proxy-saver/certificates#httpie-basic)

```
curl \
--cacert /path/to/scrapfly-ca.crt \
--proxy=http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333 \
https://httpbin.dev/anything
```

```
http \
--verify=/path/to/scrapfly-ca.crt \
--proxy=http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333 \
https://httpbin.dev/anything
```

Alternatively, each tool also provides an ability to **ignore certificate verification process** which means the certificate step can be ignored entirely though it's not recommended due to security risks.

*   [CURL](https://scrapfly.io/docs/proxy-saver/certificates#curl-ignore)
*   [HTTPIE](https://scrapfly.io/docs/proxy-saver/certificates#httpie-ignore)

```
curl \
--verify=no \
--proxy=http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333 \
https://httpbin.dev/anything
```

```
http \
--verify=no \
--proxy=http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333 \
https://httpbin.dev/anything
```

[Operating Systems](https://scrapfly.io/docs/proxy-saver/certificates#operating-system)
---------------------------------------------------------------------------------------

The certificate can also be installed in the operating system certificate store to make it available for all applications.

*   [Windows](https://scrapfly.io/docs/proxy-saver/certificates#windows)
*   [macOS](https://scrapfly.io/docs/proxy-saver/certificates#macos)
*   [Linux](https://scrapfly.io/docs/proxy-saver/certificates#linux)

1.   Download the certificate file from the [Proxy Saver dashboard](https://scrapfly.io/dashboard/proxy-saver)

2.   Double click the `.crt` file
3.   Follow the Windows instructions to install the certificate
4.   Reboot your computer
5.   After rebooting, you will be able to connect to Proxy Saver

> To verify whether the certificate was installed correctly use this windows command: 
> 
> ```
> curl -v -x \
> http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io \
> https://httpbin.dev/anything
> # if the certificate was not installed correctly you'll see:
> # curl: (60) SSL certificate problem: unable to get local issuer certificate
> ```

1.   Download the certificate file from the [Proxy Saver dashboard](https://scrapfly.io/dashboard/proxy-saver)
2.   Double click the `.crt` file
3.   Select "Always Trust" in the "When using this certificate" options dropdown.
4.   Reboot any active programs to be able to connect to Proxy Saver

> To verify whether the certificate was installed correctly use this macos command: 
> 
> ```
> curl -v -x \
> http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io \
> https://httpbin.dev/anything
> # if the certificate was not installed correctly you'll see:
> # curl: (60) SSL certificate problem: unable to get local issuer certificate
> ```

1.   Download the certificate file from the [Proxy Saver dashboard](https://scrapfly.io/dashboard/proxy-saver)
2.   Copy the `.crt` file to `/usr/local/share/ca-certificates/`
3.   Run `sudo update-ca-certificates`
4.   Reboot any active programs to be able to connect to Proxy Saver

> To verify whether the certificate was installed correctly use this linux command: 
> 
> ```
> curl -v -x \
> http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io \
> https://httpbin.dev/anything
> # if the certificate was not installed correctly you'll see:
> # curl: (60) SSL certificate problem: unable to get local issuer certificate
> ```

[Web Browsers](https://scrapfly.io/docs/proxy-saver/certificates#web-browsers)
------------------------------------------------------------------------------

Each web browser can also take custom certificates to trust HTTPS connections certified by Proxy Saver.

*   [Chrome/Chromium](https://scrapfly.io/docs/proxy-saver/certificates#chrome)
*   [Firefox](https://scrapfly.io/docs/proxy-saver/certificates#firefox)

1.    Download the certificate file from the [Proxy Saver dashboard](https://scrapfly.io/dashboard/proxy-saver)
2.    Go to browser's certificate settings page `chrome://settings/certificates`
3.   Go to the **Authority** tab and select **Import** to upload your `scrapfly-ca.crt` file.

4.   When prompted for confirmation select all checkboxes and import

1.   Download the certificate file from the [Proxy Saver dashboard](https://scrapfly.io/dashboard/proxy-saver)
2.   Go to browser's certificate settings page `about:preferences#advanced`
3.   Go to the **Privacy & Security** tab and select **View Certificates**

4.   Upload your `scrapfly-ca.crt` file.

5.   When prompted for confirmation select all checkboxes and import

[HTTP Client Libraries](https://scrapfly.io/docs/proxy-saver/certificates#libraries)
------------------------------------------------------------------------------------

Most http client libraries support proxies and can be configured to use custom certificates. Here are some examples for the most popular http client libraries:

*   [requests](https://scrapfly.io/docs/proxy-saver/certificates#python-requests "python")
*   [httpx](https://scrapfly.io/docs/proxy-saver/certificates#python-httpx "python")
*   [curl](https://scrapfly.io/docs/proxy-saver/certificates#php-curl "php")
*   [guzzle](https://scrapfly.io/docs/proxy-saver/certificates#php-guzzle "php")
*   [fetch](https://scrapfly.io/docs/proxy-saver/certificates#nodejs-fetch "nodejs")
*   [net/http](https://scrapfly.io/docs/proxy-saver/certificates#go-nethttp "golang")
*   [reqwest](https://scrapfly.io/docs/proxy-saver/certificates#rust-reqwest "rust")
*   [typhoeus](https://scrapfly.io/docs/proxy-saver/certificates#ruby-typhoeus "ruby")

```
import requests

response = requests.get(
		"https://httpbin.dev/anything",
		proxies={
				"https": "http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333"
		},
		# use scrapfly certificate
		verify="/path/to/scrapfly-ca.crt",
		# or disable verification entirely
		# verify=False
)
# or set for entire session
session = requests.Session()
session.verify = "/path/to/scrapfly-ca.crt"
session.verify = False
session.proxies = {
    "https": "http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333"
}
```

```
import httpx

response = httpx.get(
    "https://httpbin.dev/anything",
    proxies={
        "https://": "http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333"
    },
    # Use scrapfly certificate
    verify="/path/to/scrapfly-ca.crt",
    # Or disable verification entirely
    # verify=False
)

# or set for entire session
client = httpx.Client(
    verify="/path/to/scrapfly-ca.crt",
    # Or disable verification entirely
    # verify=False
    proxies={
        "https://": "http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333"
    }
)

response = client.get("https://httpbin.dev/anything")
print(response.text)
client.close()
```

```
[
        'https' => 'http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333'
    ],
    // Set the path to the custom certificate
    'verify' => '/path/to/scrapfly-ca.crt'
    // If you want to disable SSL verification entirely, set 'verify' to false
    // 'verify' => false
]);

// Send a GET request
$response = $client->get('https://httpbin.dev/anything');

// Print the response body
echo $response->getBody();

?>
```

```
const { HttpsProxyAgent } = require('https-proxy-agent');
const https = require('https');
const fs = require('fs');

// Proxy configuration
const proxy = "http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333";
const agent = new HttpsProxyAgent(proxy);

// Path to custom certificate
const cert = fs.readFileSync("/path/to/scrapfly-ca.crt");

// HTTPS agent with custom certificate
const httpsAgent = new https.Agent({
    ca: cert
});

// Individual request with custom certificate and proxy
fetch('https://httpbin.dev/anything', {
    agent: httpsAgent,
    agent: agent // Attach proxy agent as well
})
.then(response => response.text())
.then(text => console.log(text))
.catch(err => console.error('Request failed', err));
```

```
package main

import (
	"crypto/tls"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
)

func main() {
	// Load your custom CA certificate
	caCertPath := "/path/to/scrapfly-ca.crt"
	caCert, err := ioutil.ReadFile(caCertPath)
	if err != nil {
		fmt.Println("Error loading CA certificate:", err)
		return
	}

	// Create a certificate pool and append the custom CA certificate
	caCertPool := tls.NewCertPool()
	caCertPool.AppendCertsFromPEM(caCert)

	// Set up a proxy URL
	proxyURL, err := url.Parse("http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333")
	if err != nil {
		fmt.Println("Error parsing proxy URL:", err)
		return
	}

	// Configure HTTP transport to use proxy and custom CA certificate
	transport := &http.Transport{
		Proxy: http.ProxyURL(proxyURL),
		TLSClientConfig: &tls.Config{
			RootCAs: caCertPool,
		},
	}

	// Create an HTTP client with the custom transport
	client := &http.Client{
		Transport: transport,
	}

	// Make an HTTP GET request
	resp, err := client.Get("https://httpbin.dev/anything")
	if err != nil {
		fmt.Println("Request error:", err)
		return
	}
	defer resp.Body.Close()

	// Print the response body
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error reading response:", err)
		return
	}
	fmt.Println(string(body))
}
```

```
use reqwest::Client;
use std::fs;
use reqwest::Proxy;
use tokio;

#[tokio::main]
async fn main() -> Result<(), Box> {
    // Load your custom CA certificate
    let ca_cert = fs::read_to_string("/path/to/scrapfly-ca.crt")?;

    // Create a client with proxy and custom CA certificate
    let client = Client::builder()
        .proxy(Proxy::https("http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333")?)
        .add_root_certificate(reqwest::Certificate::from_pem(ca_cert.as_bytes())?)
        .build()?;

    // Send a GET request
    let response = client.get("https://httpbin.dev/anything").send().await?;

    // Print the response body
    let body = response.text().await?;
    println!("{}", body);

    Ok(())
}
```

```
require 'typhoeus'

# Set up the request with a proxy and custom certificate
response = Typhoeus.get(
  "https://httpbin.dev/anything",
  proxy: "http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333",
  sslcert: "/path/to/scrapfly-ca.crt",  # Custom SSL certificate
  ssl_verifypeer: true                  # Enable certificate verification
)

# Print the response body
puts response.body

# If you want to disable SSL verification entirely (not recommended for production)
# response = Typhoeus.get(
#   "https://httpbin.dev/anything",
#   proxy: "http://proxyId-XXX:API_KEY@proxy-saver.scrapfly.io:3333",
#   ssl_verifypeer: false  # Disable SSL verification
# )
```

[Browser Libraries](https://scrapfly.io/docs/proxy-saver/certificates#browser-libraries)
----------------------------------------------------------------------------------------

Browser automation libraries can be configured to trust the Proxy Saver certificate or ignore certificate verification. You can also install the certificate at the [operating system level](https://scrapfly.io/docs/proxy-saver/certificates#operating-system) to make it available for all browser libraries.

*   [Selenium](https://scrapfly.io/docs/proxy-saver/certificates#selenium)
*   [Playwright (Python)](https://scrapfly.io/docs/proxy-saver/certificates#playwright-py)
*   [Playwright (JS)](https://scrapfly.io/docs/proxy-saver/certificates#playwright-js)
*   [Puppeteer](https://scrapfly.io/docs/proxy-saver/certificates#puppeteer)

1.   Ensure you have the required Python packages installed:

`pip install selenium` 
2.   Download the certificate file from the [Proxy Saver dashboard](https://scrapfly.io/dashboard/proxy-saver).
3.   Use the following Python code to load the custom certificate into Selenium's browser session:

```
import os
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options

# Create a new ChromeOptions instance
chrome_options = Options()

# You can ignore all certificate errors:
chrome_options.add_argument(f"--ignore-certificate-errors")
# or add proxy saver certificate
cert_path = "/path/to/proxy-saver.crt"
chrome_options.add_argument(f"--ssl-client-certificate-file={cert_path}")

# Initialize WebDriver with the options and test it:
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://httpbin.dev/anything")
# if the certificate was not installed correctly you'll see:
# SSL certificate problem: unable to get local issuer certificate
``` 

1.   Ensure you have the required Python packages installed:

`pip install playwright` 
2.    Download the certificate file `scrapfly-ca.crt` from the [Proxy Saver dashboard](https://scrapfly.io/dashboard/proxy-saver). 
3.   Use the following Python code to load the custom certificate into Playwright's browser session:

```
import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Launch browser with the custom certificate
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
				    # you can ignore certificates
            ignore_https_errors=True,
						# and add custom certificate:
            extra_http_headers={
                "client-certificate": "/path/to/certificate.crt"
            }
        )

        # Connect to a page to test the certificate
        page = await context.new_page()
        await page.goto("https://httpbin.dev/anything")
        # Print page content to verify
        print(await page.content())
        await browser.close()

asyncio.run(run())
``` 

1.   Ensure you have the required NPM packages installed:

`npm install playwright` 
2.   Download the certificate file `scrapfly-ca.crt` from the [Proxy Saver dashboard](https://scrapfly.io/dashboard/proxy-saver).
3.   Use the following Javascript code to load the custom certificate into Playwright's browser session:

```
// Import Playwright
const { chromium } = require('playwright');

(async () => {
  // Launch the browser with ignoreHTTPSErrors set to true
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext({
    ignoreHTTPSErrors: true  // Ignore SSL errors (useful for self-signed certs)
  });

  // Open a new page
  const page = await context.newPage();

  // Navigate to the target URL
  await page.goto('https://your-internal-url-with-cert.com');

  // Print the page content to verify it loads correctly
  console.log(await page.content());

  // Close the browser
  await browser.close();
})();
``` 

1.   Ensure you have the required NPM packages installed:

`npm install puppeteer` 
2.   Use the following Javascript code to ignore certificate checks:

```
// Import Puppeteer
const puppeteer = require('puppeteer');

(async () => {
  // Launch the browser with ignoreHTTPSErrors set to true
  const browser = await puppeteer.launch({
    headless: false,
    args: ['--ignore-certificate-errors']  // Ignore SSL certificate errors
  });

  // Create a new browser context/page and navigate to url
  const page = await browser.newPage();
  await page.goto('https://httpbin.dev/anything');

  // Print the page content to verify it loads correctly
  const content = await page.content();
  console.log(content);

  await browser.close();
})();
``` 
3.    Optional: as Puppeteer doesn't support custom certificates you can install the system level certificate using [operating system instructions](https://scrapfly.io/docs/proxy-saver/certificates#operating-system).
