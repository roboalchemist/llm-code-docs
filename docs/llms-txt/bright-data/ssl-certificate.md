# Source: https://docs.brightdata.com/general/account/ssl-certificate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SSL Certificate

<Note>
  You can use Bright Data products without the SSL certificate:

  1. Using **Bright Data proxy API**. Read more: [API vs. native Access](https://docs.brightdata.com/api-reference/authentication)
  2. Get your account **verified** with our [KYC process](https://docs.brightdata.com/proxy-networks/residential/network-access#kyc-verification)
</Note>

The SSL certificate allows you to establish end-to-end encrypted connections when using [Residential Proxies](https://docs.brightdata.com/proxy-networks/residential/introduction), [Mobile proxies](https://docs.brightdata.com/proxy-networks/mobile/introduction), [Unlocker API](https://docs.brightdata.com/scraping-automation/web-unlocker/introduction) or the [SERP API](https://docs.brightdata.com/scraping-automation/serp-api/introduction) in **native** proxy mode.

If you are just doing preliminary testing, you can also proceed without the SSL certificate and use it later.

Using the SSL certificate is straight forward. You download it, and choose how you want to use it in your environment.

## Download the SSL certificate

<Tip>
  Bright data has a **new** SSL certificate with works with proxy port: `33335`.
</Tip>

1. **Right click** on this [link](https://brightdata.com/static/brightdata_proxy_ca.zip) to "save as" the file to your hard drive.
2. **Unzip the file** and choose the certificate to use. Most users - espcially if they are new to Bright Data - should use the **new** SSL certificate.

## Bright Data new SSL Certificate

<Warning>
  Bright Data new SSL certificate support for browser extension is coming soon. **Refrain** from upgrading to the new certificate if you use the Browser Extension
</Warning>

Bright data now using an updated SSL Certificate which expires in September 2034. When using this certificate it is essential to configure your native proxy port to be `33335` which is the port serving requests secured by the new certificate.

If you use our old SSL certificate note that it is deprecated and expires in September 2026, and works towards port `22225`. To ensure your smooth and secure operations use the **new** certificate with port `33335`. Read more in: [FAQ: Which port shall I use 22225 or 33335](https://docs.brightdata.com/general/faqs#which-port-shall-i-use-22225-or-33335)

## Using the SSL certificate in your code

If you write scraping code, in most cases, you do not need to install the SSL certificate in your environment. Simply load the SSL certificate in your code. For example, for CURL:

```sh  theme={null}
curl --proxy brd.superproxy.io:33335 --proxy-user brd-customer-<account-id>-zone-<zone-name>:<zone-password> --cacert <PATH TO CA.CRT> "https://geo.brdtest.com/mygeo.json"
```

You can refer to Bright Data sample code examples in the dashboard for exact syntax.

## Installation of the SSL certificate

In some cases, for example when using some third party tools that don't allow loading the certificate from your hard drive, you still need to install the SSL certificate on your computer.

### Where do I install the certificate?

The SSL certificate needs to be installed **on the host that is running the actual scraping code or application.**

In most cases this is your PC but, if you use a cloud-hosted server to run your code, you need to install the SSL certificate on the server itself.

### Installation instructions

This takes 2 minutes - simply follow these instructions:

<Tabs>
  <Tab title="Windows">
    * If you didn't do so already, **Right click** on this [link](https://brightdata.com/static/brightdata_proxy_ca.zip) to "save as" the file to your hard drive.
    * Double click the ca.crt file
    * Follow the Windows instructions to install the certificate.
    * Reboot your computer
    * After rebooting, you will be able to connect to Bright Data product you needed (Residential Proxy, Unlocker API or SERP API)
  </Tab>

  <Tab title="Chrome">
    * Once you've download the [certificate](https://brightdata.com/static/brightdata_proxy_ca.zip) file (see the instruction on the top of this article)

    <AccordionGroup>
      <Accordion title="Go to Browser settings">
        <Frame>
                    <img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/faqs/proxy-networks/browser-settings.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=f4fa8827d627bc9226cd8abc7223834e" alt="browser-settings.png" width="328" height="639" data-path="images/general/faqs/proxy-networks/browser-settings.png" />
        </Frame>
      </Accordion>

      <Accordion title="Go to Privacy and security and click on Security">
        <Frame>
                    <img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/faqs/proxy-networks/privacy-and-security.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=38c0e4d18cef84e93eda18015aa3d376" alt="privacy-and-security.png" width="1369" height="707" data-path="images/general/faqs/proxy-networks/privacy-and-security.png" />
        </Frame>
      </Accordion>

      <Accordion title="Scroll down and click on Manage certificate">
        <Frame>
                    <img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/faqs/proxy-networks/manage-certificate.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=60596e13df89811bb2e2b74718ac4b49" alt="manage-certificate.png" width="1343" height="861" data-path="images/general/faqs/proxy-networks/manage-certificate.png" />
        </Frame>
      </Accordion>

      <Accordion title="Go to Trusted Certification Authorities and click Import">
        <Frame>
                    <img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/faqs/proxy-networks/trusted-certification-authorities.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=2f003ff4d07e987be6bf22d37c4071b6" alt="trusted-certification-authorities.png" width="1343" height="861" data-path="images/general/faqs/proxy-networks/trusted-certification-authorities.png" />
        </Frame>
      </Accordion>

      <Accordion title="Click on Next">
        <Frame>
                    <img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/faqs/proxy-networks/click-next.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=11ed28a18d6bbc0ebd9f90c6c0941c3b" alt="click-next.png" width="553" height="532" data-path="images/general/faqs/proxy-networks/click-next.png" />
        </Frame>
      </Accordion>

      <Accordion title="Click Browse and select the certificate you just downloaded, and click Next">
        <Frame>
                    <img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/faqs/proxy-networks/click-browse.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=2edc96af61cb71e08d868e5b5a4c8eb2" alt="click-browse.png" width="562" height="545" data-path="images/general/faqs/proxy-networks/click-browse.png" />
        </Frame>
      </Accordion>

      <Accordion title="Select &#x22;Place all certificates in the following store&#x22; and click Next">
        <Frame>
                    <img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/faqs/proxy-networks/place-all-certificates.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=b2ed310b3eac137542146c0fc0aa6100" alt="place-all-certificates.png" width="556" height="537" data-path="images/general/faqs/proxy-networks/place-all-certificates.png" />
        </Frame>
      </Accordion>

      <Accordion title="Make sure Certificate Store Selected by User is &#x22;Trusted Root Certification Authorities&#x22;, and click Finish">
        <Frame>
                    <img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/faqs/proxy-networks/trusted-root-certification-authorities.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=13958cfb1526ec01478e1f73862f6f25" alt="trusted-root-certification-authorities.png" width="663" height="639" data-path="images/general/faqs/proxy-networks/trusted-root-certification-authorities.png" />
        </Frame>
      </Accordion>

      <Accordion title="Click OK">
        <Frame>
                    <img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/faqs/proxy-networks/click-ok.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=65383b5fa5917ad873cb6a3084c8b824" alt="click-ok.png" width="509" height="352" data-path="images/general/faqs/proxy-networks/click-ok.png" />
        </Frame>
      </Accordion>
    </AccordionGroup>
  </Tab>

  <Tab title="Firefox">
    * Type in the address bar: `about:preferences#advanced`
    * Under “Security” click “View Certificates”
    * Select the authorities tab, and click “Import” button below
    * Browse to the directory you downloaded the certificate file to, select the certificate file and click “Open”
    * In the popup box click the checkbox “Trust this CA to identify websites”
    * Click OK to complete the installation
    * Make sure Bright Data proxy is configured as Firefox's proxy, and browse thru proxy to a protected website
  </Tab>

  <Tab title="Linux">
    * Copy the downloaded certificate file `ca.crt` to the `/usr/local/share/ca-certificates/` folder.
    * Run `sudo update-ca-certificates`. The output of the command should state that 1 certificate was added.
    * Go to an SSL-protected website to check that everything is working as cted.
  </Tab>

  <Tab title="macOS">
    * Double-click the downloaded certificate file. You will see the "Keychain Access" application.
    * Double-click the "luminati.io" certificate to see a popup with certificate settings.
    * Select "Always Trust" in the "When using this certificate" dropdown.
    * Close the popup enter your credentials when asked.
    * Restart your browser and go to an SSL-protected website to check that everything is working as expected.
  </Tab>

  <Tab title="iOS">
    * Open up Safari
    * Navigate to this page and download the certificate using [this link](https://brightdata.com/static/brightdata_proxy_ca.zip), but first read the following two items.
    * Click Install and provide your passcode
    * Click Install in the top right corner and then Done
    * Go to iPhone "Settings"
    * Go to "About"
    * Go to "Certificate Trust Settings"
    * Enable the "luminati.io" certificate
    * You can now go to an SSL-protected website in any browser installed in your system to check that everything is working as expected.
  </Tab>

  <Tab title="Android">
    * Download the following [certificate](https://brightdata.com/static/brightdata_proxy_ca.zip) and save it on your phone.
    * On your phone, look for the downloaded zip through 'My files' and extract it.
    * Go yo Settings > Security and privacy > More security settings
    * Under 'Crednetial storage' click 'Install from device storage'
    * Select 'CA certificate' and click 'Install anyway'
    * Enter your password
    * Select the certificate you extracted from your files and click 'Done'
    * You can now go to an SSL-protected website in any browser installed in your system to check that everything is working as expected.
  </Tab>
</Tabs>

## How to ignore SSL errors?

In some cases you will need to install our certificate or ignore SSL errors in order to get access to specific products or features. In case you are not interested in installing our certificate, you can ignore SSL errors. Check out the following code snippets for different programming languages, the highlighted part is what needs to be added to your code in order to ignore SSL errors.

<CodeGroup>
  ```sh Curl theme={null}
  # Add -k to ignore ssl errors
  curl --proxy brd.superproxy.io:33335 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password> -k "http://lumtest.com/myip.json"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node
  /*This sample code assumes the request-promise package is installed. If it is not installed run: "npm install request-promise"*/
  require('request-promise')({
      url: 'http://lumtest.com/myip.json',
      proxy: 'http://brd-customer-<customer_id>-zone-<zone_name>:<zone_password>@brd.superproxy.io:33335',

      // Make sure you set reject rejectUnauthorized to false
      rejectUnauthorized: false,
  })
  .then(function(data){ console.log(data); },
      function(err){ console.error(err); });
  ```

  ```python Python theme={null}
  #!/usr/bin/env python
  print('If you get error "ImportError: No module named \'six\'" install six:\n'+\
      '$ sudo pip install six');

  import sys

  # Make sure you add these two line to ignore ssl error
  import ssl
  ssl._create_default_https_context = ssl._create_unverified_context


  if sys.version_info[0]==2:
      import six
      from six.moves.urllib import request
      opener = request.build_opener(
          request.ProxyHandler(
              {'http': 'http://brd-customer-<customer_id>-zone-<zone_name>:<zone_password>@brd.superproxy.io:33335',
              'https': 'http://brd-customer-<customer_id>-zone-<zone_name>:<zone_password>@brd.superproxy.io:33335'}))
      print(opener.open('http://lumtest.com/myip.json').read())

  if sys.version_info[0]==3:
      import urllib.request
      opener = urllib.request.build_opener(
          urllib.request.ProxyHandler(
              {'http': 'http://brd-customer-<customer_id>-zone-<zone_name>:<zone_password>@brd.superproxy.io:33335',
              'https': 'http://brd-customer-<customer_id>-zone-<zone_name>:<zone_password>@brd.superproxy.io:33335'}))
      print(opener.open('http://lumtest.com/myip.json').read())
  ```

  ```cs C# theme={null}
  using System;
  using System.Net;

  class Example
  {
      static void Main()
      {

          // Make sure you add this line to ignore ssl error
          ServicePointManager.ServerCertificateValidationCallback += (sender, cert, chain, sslPolicyErrors) => true;

          var client = new WebClient();
          client.Proxy = new WebProxy("brd.superproxy.io:33335");
          client.Proxy.Credentials = new NetworkCredential("brd-customer-<customer_id>-zone-<zone_name>", "<zone_password>");
          Console.WriteLine(client.DownloadString("http://lumtest.com/myip.json"));
      }
  }
  ```

  ```ruby Ruby theme={null}
  #!/usr/bin/ruby

  require 'uri'
  require 'net/http'
  require 'net/https'

  uri = URI.parse('http://lumtest.com/myip.json')
  proxy = Net::HTTP::Proxy('brd.superproxy.io', 33335, 'brd-customer-<customer_id>-zone-<zone_name>', '<zone_password>')

  req = Net::HTTP::Get.new(uri)

  # Make sure you add verify_mode => OpenSSL::SSL::VERIFY_NONE
  result = proxy.start(uri.host,uri.port, :use_ssl => uri.scheme == 'https', :verify_mode => OpenSSL::SSL::VERIFY_NONE) do |http|
      http.request(req)

  send

  puts result.body
  ```

  ```java Java theme={null}
  package example;

  import org.apache.http.HttpHost;
  import org.apache.http.client.fluent.*;

  public class Example {
      public static void main(String[] args) throws Exception {
          HttpHost proxy = new HttpHost("brd.superproxy.io", 33335);
          String res = Executor.newInstance()
              .auth(proxy, "brd-customer-<customer_id>-zone-<zone_name>", "<zone_password>")
              .execute(Request.Get("http://lumtest.com/myip.json").viaProxy(proxy))
              .returnContent().asString();
          System.out.println(res);
      }
  }

  /*In the above example, we are not explicitly ignoring SSL
  I will share with you a short code I wrote that does ignore SSL using JAVA (was taken from cloud proxy manager examples) */

  import java.io.*;
  import java.net.*;
  import java.security.cert.X509Certificate;
  import javax.net.ssl.*;
  import java.util.Base64;

  public class Example {
      public static void main(String[] args) throws Exception {
          // Disable restricted headers for proxy authentication
          System.setProperty("jdk.http.auth.tunneling.disabledSchemes", "");

          // Set up a TrustManager that does not validate certificate chains
          SSLContext sc = SSLContext.getInstance("SSL");

          TrustManager trust_manager = new X509TrustManager() {
              public X509Certificate[] getAcceptedIssuers() {
                  return null;
              }

              public void checkClientTrusted(X509Certificate[] certs, String authType) {
              }

              public void checkServerTrusted(X509Certificate[] certs, String authType) {
              }
          };
          TrustManager[] trust_all = new TrustManager[] { trust_manager };
          sc.init(null, trust_all, new java.security.SecureRandom());
          HttpsURLConnection.setDefaultSSLSocketFactory(sc.getSocketFactory());

          // Set up the proxy and open a connection
          URL url = new URL("https://geo.brdtest.com/mygeo.json");
          Proxy proxy = new Proxy(Proxy.Type.HTTP, new InetSocketAddress("brd.superproxy.io", 33335));
          URLConnection yc = url.openConnection(proxy);

          // Set default Authenticator for proxy authentication
          Authenticator.setDefault(new Authenticator() {
              @Override
              public PasswordAuthentication getPasswordAuthentication() {
                  return new PasswordAuthentication("brd-customer-<customer_id>-zone-<zone_name>", "<zone_password>".toCharArray());
              }
          });

          // Read and print the response from the server
          BufferedReader in = new BufferedReader(new InputStreamReader(yc.getInputStream()));
          String inputLine;
          while ((inputLine = in.readLine()) != null)
              System.out.println(inputLine);
          in.close();
      }
  }
  ```

  ```vba VBA theme={null}
  Imports System.Net

  Module Module1
      Sub Main()
        
          ' Make sure you add this line to ignore ssl error
          ServicePointManager.ServerCertificateValidationCallback = Function(se, cert, chain, sslerror) True

          Dim Client As New WebClient
          Client.Proxy = New WebProxy("http://brd.superproxy.io:33335")
          Client.Proxy.Credentials = New NetworkCredential("brd-customer-<customer_id>-zone-<zone_name>", "<zone_password>")
          Console.WriteLine(Client.DownloadString("http://lumtest.com/myip.json"))
      End Sub
  End Module
  ```

  ```php PHP theme={null}
  <?php
  $curl = curl_init('http://lumtest.com/myip.json');
  curl_setopt($curl, CURLOPT_PROXY, 'http://brd.superproxy.io:33335');
  curl_setopt($curl, CURLOPT_PROXYUSERPWD, 'brd-customer-<customer_id>-zone-<zone_name>:<zone_password>');

  // Make sure you add this line to ignore ssl error
  curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 0);

  curl_exec($curl);
  ?>
  ```

  ```perl Perl theme={null}
  #!/usr/bin/perl

  use LWP::UserAgent;

  # Make sure you add this line to ignore ssl error
  use IO::Socket::SSL qw( SSL_VERIFY_NONE );

  my $agent = LWP::UserAgent->new();
  $agent->proxy(['http', 'https'], "http://brd-customer-<customer_id>-zone-<zone_name>:<zone_password>\@brd.superproxy.io:33335");
  $agent->ssl_opts(verify_hostname => 0, SSL_verify_mode => SSL_VERIFY_NONE);
  print $agent->get('http://lumtest.com/myip.json')->content();
  ```
</CodeGroup>

## Bright Data Proxy Manager SSL analysis

Some features require the Proxy Manager to have access to HTTPS traffic. This can be done by enabling the **SSL Analyzing** option on the proxy port configuration page.

Once you allow Proxy Manager to terminate the SSL you will also need to [trust Bright Data Certificate Authority (CA)](https://brightdata.com/static/brightdata_proxy_ca.zip).

Under the hood Proxy Manager will create a secure encrypted HTTPS connection with the target site, decrypt the traffic to log requests and run rules based on your settings and then pass the response back to your client in an encrypted HTTPS connection with a certificate signed by our CA certificate.
