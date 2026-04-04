# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/integration-guides/android.md

# Android

Android is by far the most popular mobile OS on the planet, with upwards of 70% market share. Connecting an Android device to Nimble IP is easy and straightforward, with no 3rd-party apps needed!

### Proxy Setup - Wi-Fi

1. To get started, open your device's settings, and then Internet/Network settings.

![](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/HApKUL8pPoQ5fkQs2sFR/Android%20-%20Nimble%20IP%20-%201.png)

2\. Next, click on the network you’re currently connected to in order to view its properties.

![](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/i4Fea5QhCYq1yqBONQl1/Android%20-%20Nimble%20IP%20-%202.png)

3\. Click on the pencil at the top right to edit the network’s settings, and then on “Advanced options”.

![](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/M5QpB96nBbmAtNDHnS31/Android%20-%20Nimble%20IP%20-%203.png)

4\. Scroll down until you see “Proxy”. Set your proxy settings to manual. A few new fields will be added, including “Proxy hostname” and “Proxy port”.

&#x20;      For Proxy hostname, enter “*ip.nimbleway.com*”.

&#x20;      For Proxy port, use “7000”.

&#x20;      Then click save.

![](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/W1Nz31cgy8Z8dmdg7H4L/Android%20-%20Nimble%20IP%20-%204.webp)

5\. At this point, your phone will begin sending your requests through Nimble IP, but you still need to authenticate your device. To do so, open Chrome and browse to any website. You’ll immediately be asked to sign in with a username and password.

* Username ⇒ Nimble’s username string: account-***\[accountName]***-pipeline-***\[pipelineName]***
* Password ⇒ Nimble’s pipeline password

{% hint style="info" %}
Your Nimble account manager will provide you with the username and password for your pipeline.
{% endhint %}

![](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/IanjTTJl6ZTMxMkjiidk/Android%20-%20Nimble%20IP%20-%205.png)

Click Sign in, and you’re done!

### Proxy Setup - Cellular

1. Open your device's settings, and then click on Mobile Networks.

![](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/DV6GQDNomVWknuF8fUr6/Android%20-%20Nimble%20IP%20-%206.png)

2\. Next, click on “Access Point Names”, or on some devices APNs.

![](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/fnk08PAF5tPZMlKJKNxl/Android%20-%20Nimble%20IP%20-%207.webp)

3\. Click on the currently active APN.

![](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/PrkHBVp8kKHtAuZX8kv5/Android%20-%20Nimble%20IP%20-%208.webp)

4\. Enter in the following details:

* Proxy ⇒ *ip.nimbleway.com*
* Port ⇒ *7000*
* Username ⇒ Nimble’s pipeline **username string**
* Password ⇒ Nimble’s pipeline ***password***

![](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/TRghxIkinkcLhcoQP7NQ/Android%20-%20Nimble%20IP%20-%209.png)

Congratulations! You’ve connected your Android device, and requests will now be routed through Nimble IP.

{% hint style="info" %}
Because Android is used by many manufacturers, the process may be slightly different on your device. Furthermore, different manufacturers will allow different apps to use proxies, so be sure to check that the app you’d like to use supports proxies.
{% endhint %}
