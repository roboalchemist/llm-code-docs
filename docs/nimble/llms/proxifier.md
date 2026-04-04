# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/integration-guides/proxifier.md

# Proxifier

Proxifier is a network gateway that allows applications that do not support working through proxy servers to operate through a SOCKS or HTTPS proxy, without having to re-route all traffic through the proxy network. Using Proxifier, it’s possible to route applications through a single entry point on Nimble IP and direct each one to the relevant IP pipeline.

### Installing Proxifier

To begin working with Proxifier, download and install the application from the Proxifier website.

### Adding Nimble’s pipeline

In this guide, we will be using Windows as an example, although setting up on macOS is very similar and follows the same configuration steps.

1. To connect Proxifier with Nimble IP, you will need to create a profile - click on the ‘**Profile**’ tab at the top left, and from the drop-down menu select **‘Proxy Servers’**.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/iduIUp0TZuKgZwDsHWkN/Proxifier%20-%20Nimble%20IP%20-%201.png" alt=""><figcaption></figcaption></figure>

2\. Click “**Add**” to set Nimble IP as a proxy server.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/itzpmZ7ePtZqm6PyLSos/Proxifier%20-%20Nimble%20IP%20-%202.webp" alt=""><figcaption></figcaption></figure>

3\. Enter the following server information:

* Address ⇒ **ip.nimbleway.com**
* Port ⇒ **7000**
* Protocol ⇒ **HTTPS**

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/RM9MnvB3VKEh8ifUUBYK/Proxifier%20-%20Nimble%20IP%20-%203.png" alt=""><figcaption></figcaption></figure>

4\. Authentication This is when you need to decide which Nimble pipeline you would like to use, determined by the pipeline name in the username connection string. Your Nimble account comes pre-configured with one pipeline for a quick start, and your account manager will provide you with its username and password. We will discuss the option for adding additional pipelines in the “Setting proxy rules” section below.

* Check the box to enable username and password authentication
* Username ⇒ Nimble’s username string: account-***\[accountName]***-pipeline-**\[pipelineName]**
* Password ⇒ Nimble’s pipeline password

{% hint style="info" %}
Your Nimble account manager will provide you with the username and password for your pipeline.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7d8YDGRAEh6xzZC6js5X/Proxifier%20-%20Nimble%20IP%20-%204.webp" alt=""><figcaption></figcaption></figure>

### Check the proxy connection

5\. To verify the setup was successful, click on **‘Check’** and Proxifier will test the connection and report back its status.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/ZK7IJxtHu8ruAL9nJMFK/Proxifier%20-%20Nimble%20IP%20-%205.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/ELzQjBePmd5LnKMnPVls/Proxifier%20-%20Nimble%20IP%20-%206.png" alt=""><figcaption></figcaption></figure>

6\. Once you receive confirmation that the connection is set up correctly, go back to the main Proxifier window and click “**OK”** to save your profile.

**Note**: We recommend you do not set Nimble IP as your default proxy server as this may result in an unwanted amount of traffic going through Nimble.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/ZE7RFEvOi7qxQmj8ZIu0/Proxifier%20-%20Nimble%20IP%20-%207.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/qMYKtSerggx8YM2w8jGR/Proxifier%20-%20Nimble%20IP%20-%208.png" alt=""><figcaption></figcaption></figure>

### Controlling proxy session behavior

So far, we have covered how to connect a single pipeline from Nimble to Proxifier. Now it’s time to decide in which scenarios this connection should be used, and whether you need to connect multiple Nimble pipelines.

1. In case the requests you send through Nimble should all have the same session behavior and targeting (location, IP rotation, session control, etc.), the profile previously created is all you need. We suggest you configure your session preferences in the Nimble pipeline, as it will help our optimization engines select more relevant IPs for your use case. Check out our Admin API documentation for more details on how to configure your pipelines.
2. If you have multiple use cases, each with its own proxy connection requirements, there are two ways to control the session behavior for each case:
   1. Create multiple pipelines in Nimble IP, one for each profile in Proxifier. As previously mentioned, this helps our optimization engines tune in to your needs faster. Read more on the use of pipelines and their available configurations.
   2. Use the username string set in each Proxifier profile to configure the proxy connection and session behavior. Read more about Nimble Backconnect Gateway API and possible configurations.

### Adding proxy rules

We’ll now connect various applications and scenarios to the Proxifier profiles that channel each one through Nimble IP.

Click on the **‘Profile’** tab again, but this time choose ‘**Proxification rules**’.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/J9yjHX8kOdWfHWJ50DxZ/Proxifier%20-%20Nimble%20IP%20-%209.webp" alt=""><figcaption></figcaption></figure>

In the rules window, select the profiles created for use with Nimble:

1. Set the applications that are allowed to access each Nimble pipeline.
2. In case your proxy use cases are split by domain or port, you have the option to set those as part of your rules as well.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/Kds8fCaw9SLnznylhYtf/Proxifier%20-%20Nimble%20IP%20-%2010.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/qcmUxTJM1GaagM74qqxZ/Proxifier%20-%20Nimble%20IP%20-%2011.png" alt=""><figcaption></figcaption></figure>

### DNS Resolution

In order to improve your data-gathering success, DNS resolution should be done by Nimble IP.

1. Under the Profiles menu, select **‘Name Resolution’**.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/FkhnmMK5qpWWV8Pwweya/Proxifier%20-%20Nimble%20IP%20-%2012.webp" alt=""><figcaption></figcaption></figure>

2\. Under **‘Proxifier DNS settings’** select **‘Resolve hostnames through proxy’**.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7AKsYxRAFk6V9i9lltUe/Proxifier%20-%20Nimble%20IP%20-%2013.png" alt=""><figcaption></figcaption></figure>

Click **‘OK’** at the bottom and you are ready to go!
