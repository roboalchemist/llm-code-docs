# Source: https://gitbook.com/docs/help-center/resolving-connection-lost-message.md

# Resolving "Connection Lost" message

The "Connection lost" message often indicates that GitBook's necessary network connections are being blocked by your computer or network settings.

Here are a few possible causes for your connectivity issues:

* Temporary local or regional network issues
* Browser security settings
* Browser plugins
* Security/antivirus
* Firewalls
* Plugins/extensions
* Proxies
* Local network settings
* Your provider
* Your area/region

{% hint style="info" %}
As a first step, we recommend clearing your cache and restarting your browser.
{% endhint %}

### Try a Different Browser or Device

Sometimes, the issue might be with the browser or the device you're using. Try to access GitBook using a different browser or device to verify if the problem continues.

If GitBook is functioning without issues on another browser, contact support and include information about the browser you used when the problem occurred.

### Restart your Wi-Fi and ethernet connections.

We recommend restarting your Wi-Fi and ethernet connections and turning them back on.&#x20;

### Disable Unnecessary Browser Extensions

Browser extensions can interfere with the way websites work. Try removing any extensions that are not essential, especially those that are designed to block content or manage network requests.

### Safelisting services GitBook uses to run its app

We recommend checking the list of services that GitBook relies on to run its app. If you have any firewall or application that blocks all traffic or some of the sites listed below, you should add an exception to allow GitBook to work in your network.

#### App <a href="#app" id="app"></a>

* `*.gitbook.com`
  * `app.gitbook.com`
  * `api.gitbook.com`
  * `clearbit-risk.gitbook.com`
  * `files.gitbook.com`
  * `segment-cdn.gitbook.com`
  * `segment-api.gitbook.com`
* `*.gitbook.io`

#### CDNs <a href="#cdns" id="cdns"></a>

* `cdn.iframe.ly`
* `cdn.polyfill.io`

#### Google APIs <a href="#google-apis" id="google-apis"></a>

* `*.googleapis.com`
  * `firebase.googleapis.com`
  * `firestore.googleapis.com`
  * `www.googleapis.com`
* `*.googleusercontent.com`
* `*.googletagmanager.com`

#### Sentry <a href="#sentry" id="sentry"></a>

* `*.sentry.io`
