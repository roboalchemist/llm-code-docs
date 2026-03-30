# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/integration-guides/mulogin.md

# MuLogin

MuLogin is a multi-session browser that helps you manage multiple online accounts from a single interface while maintaining your privacy and security.

Using MuLogin, you can create multiple virtual browser profiles that act as separate users, each with its own unique digital fingerprint. This allows you to access multiple accounts from a single device without compromising your data or leaving a trace.

In this guide, we’ll demonstrate step-by-step how to connect Incogniton’s virtual profiles with Nimble IP Pipelines for full proxy support.

### Follow these steps to integrate Nimble with MuLogin

1. Sign up for a free account at [mulogin.com](http://mulogin.com/).

* Download and install the Incogniton software [here](https://www.mulogin.com/download.php?l=en).
* Navigate to the "Add Browser" option on the right side of the screen.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/R3aLzUcj7u4rgDWW41pi/mulogin.png" alt=""><figcaption></figcaption></figure>

1. Scroll down to “Proxy Settings” and select “HTTP”.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/zt2LCYvsCECLl8AjnwmQ/MULOGING2.png" alt=""><figcaption></figcaption></figure>

In the Nimble User Dashboard, navigate to the Nimble IP page and click “add pipeline”.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/4WIbw4wNqCKTHzSwezq8/image.png" alt=""><figcaption></figcaption></figure>

In your new pipeline, you will find the IP address, port, username, and password.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/yr26aBtT3opYZTaoZEPY/image.png" alt=""><figcaption></figcaption></figure>

To set up and test the proxy in the MuLogin dashboard:

1. Open the proxy settings in MuLogin.
2. Configure the proxy using the following information:
   * Proxy type: HTTP
   * IP address: ip.nimbleway.com
   * Port: 7000
   * Username
   * Password
3. Test the proxy to ensure it's working correctly by clicking “Check the network”.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7B9Rx5A11Ap8WdhS1e0p/mulogin%203.png" alt=""><figcaption></figcaption></figure>

That’s all! Your MuLugin profile is now connected to Nimble IP, and requests will be routed through Nimble’s proxy infrastructure.
