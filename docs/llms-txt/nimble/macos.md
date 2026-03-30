# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/integration-guides/macos.md

# macOS

MacOS natively supports proxy servers like Nimble IP, and allows installed applications to use the proxy connection for their communications over the internet. Although some applications (like Firefox) use an internal proxy configuration, most applications will use the macOS settings.

MacOS supports a variety of different proxy protocols, and flexibly allows for different proxies to be configured for different network connections.

### Configuring proxy settings

1. To get started, open your System Preferences by clicking on the Apple menu → System Preferences.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/f6XVbLISbCaIK1tBBgJ0/Nimble%20IP%20-%20Mac%20-%201.png" alt=""><figcaption></figcaption></figure>

2\. Next, click on “Network” to open your network settings.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/c4j21YYaY8fkyVUfRICw/Nimble%20IP%20-%20Mac%20-%202.webp" alt=""><figcaption></figcaption></figure>

3\. From the list on the left-hand side, select the network connection you’d like to connect to Nimble IP. In this example, we’ll be configuring the Wi-Fi connection. Once you have made a selection, click on the “Advanced...” button.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/MbMhF7ZjrPCLICYWMH0B/Nimble%20IP%20-%20Mac%20-%203.png" alt=""><figcaption></figcaption></figure>

4\. In the advanced configuration window, select the “Proxies” tab from the top menu.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/J4yQSC2t5ROKMDYsdSt4/Nimble%20IP%20-%20Mac%20-%204.webp" alt=""><figcaption></figcaption></figure>

5\. In the protocol selection list, check “Secure Web Proxy (HTTPS)”. Next, under “Secure Web Proxy Server”, enter “ip.nimbleway.com”, and in the adjacent box separated by a colon (:) enter “7000”. These are Nimble’s host and port settings. Check “Proxy server requires password”, and in the username and password field enter your Nimble pipeline username string and pipeline password.&#x20;

* **Your Nimble account manager will provide you with the username and password for your pipeline.**

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/u0K9ns047XxbdAVCkVhp/Nimble%20IP%20-%20Mac%20-%205.webp" alt=""><figcaption></figcaption></figure>

6\. Press “OK” in the Wi-Fi settings window, and then “Apply” in the Network settings window to save and apply your proxy settings.

### **Congratulations!**

You’ve successfully connected your macOS computer to Nimble’s IP Infrastructure. Your secure web traffic will now be routed through Nimble.
