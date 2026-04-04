# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/integration-guides/windows.md

# Windows

Configuring Windows to work with Nimble IP allows any running application to use the proxy connection for its communication over the internet.

In the latest versions of Windows OS (10 and up), the server and port are set by the OS, whereas the credentials (username and password) must be set by each application individually.

### Configuring proxy settings

1. To get started, open “Proxy settings” on Windows - click the Windows key and search for “proxy settings”.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/vMukeAteIq17KRMYF1JZ/Nimble%20IP%20-%20Window%20-%201.png" alt=""><figcaption></figcaption></figure>

* You can also find Proxy settings under “Network & Internet” settings.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/LpxIPW7R6JiC3YHbCdTD/Nimble%20IP%20-%20Window%20-%202.png" alt=""><figcaption></figcaption></figure>

2\. There are two ways to set up a proxy; by script or manually. In this guide, we’ll set up the proxy manually - click on “Set up” to add a proxy server and port.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/EaarkczTvXEe3PzrF8Yc/Nimble%20IP%20-%20Window%20-%203.png" alt=""><figcaption></figcaption></figure>

3\. To use the proxy, switch “Use a proxy server” to ON, then add ip.nimbleway.com as your “Proxy IP server”, enter port 7000, and then click “Save” to enable your setup.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/Fy6OyqxtMTpA5i3TG1gc/Nimble%20IP%20-%20Window%20-%204.png" alt=""><figcaption></figcaption></figure>

### Entering credentials

As each application must manage its own credentials in Windows 10 and later, the way to set the username and password depends on the application you’re using. For example, to set your credentials in Chrome:

1. Open Chrome.
2. Enter the URL for the page you wish to visit.
3. Chrome will prompt you for Nimble’s Backconnect proxy gateway credentials:

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/ZyghTC7uyvkiRWYyQJ3v/Nimble%20IP%20-%20Window%20-%205.png" alt=""><figcaption></figcaption></figure>

4\. Enter your Nimble proxy username and password (provided by your account manager when your account was opened).

5\. Click Sign in and your page will load through Nimble IP.

### Controlling your connection

By modifying your connection string, you can control your targeted location. See Nimble’s Backconnect Gateway guide for all username configuration options.

### Allow-listing your IP instead of using credentials

In some cases, it’s easier to allow-list your IP in your Pipeline settings instead of using credentials. This allows you to connect to Nimble IP, with all session controls managed by your Pipeline’s default settings.

If you'd like to learn more about using Allow-lists and managing pipelines, see our Nimble IP documentation.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/A95qunMVd1Di3KY8cZsM/Nimble%20IP%20-%20Window%20-%206.png" alt=""><figcaption></figcaption></figure>
