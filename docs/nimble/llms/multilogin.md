# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/integration-guides/multilogin.md

# Multilogin

Multilogin provides you with browser and device fingerprints, and together with Nimble IP, you can access sites online from multiple destinations with full anonymity.

### Adding Nimble’s Backconnect Gateway

Before adding a proxy to your Multilogin profile, make sure you have a Nimble pipeline configured with the correct target country and IP rotation interval. Here is the information you will need for your Multilogin profile:

| Server            | ip.nimbleway.com                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| Port              | 7000                                                                                           |
| Username string   | Will have the following structure: account-***\[accountName]***-pipeline-***\[pipelineName]*** |
| Pipeline password | Each Pipeline uses its own password for authentication                                         |

{% hint style="info" %}
Your Nimble account manager will provide you with the username and password for your pipeline.
{% endhint %}

### Installing Multilogin

If you are new to Multilogin, start by installing the application from their website at [multilogin.com](https://multilogin.com/) and creating an account.

### Multilogin setup

To use Multilogin, you will need to create a browser profile and set a proxy to use with your profile.

1. Start by clicking **‘Create New’** to add a browser profile:

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/ustYbuL2iFlse0RFGRyf/multilogin%20-%20Nimble%20IP%20-%201.png" alt=""><figcaption></figcaption></figure>

2\. Set a name for your profile (we used Nimble in our example).

3\. Choose an operating system and browser for your profile.

4\. Go to Proxy on the left navigation bar and click on **“Edit proxy settings”:**

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/jkpTu5rEUIxGyRZrcH1k/multilogin%20-%20Nimble%20IP%20-%202.png" alt=""><figcaption></figcaption></figure>

5\. Select “HTTP proxy” as the connection type.

6\. Set the following:

* New address ⇒ *ip.nimbleway.com*
* Port ⇒ *7000*
* Login ⇒ Nimble’s pipeline ***username string***
* Password ⇒ Nimble’s pipeline ***password***

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/KyE4NiUtE4xRwgjf3Ko2/multilogin%20-%20Nimble%20IP%20-%203.png" alt=""><figcaption></figcaption></figure>

**Note**: Make sure to enable ‘Timezone, WebRTC and Geolocation fingerprints based on the external IP’ to ensure your profile works correctly with Nimble:

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/FOq0IrHOVBMINGFA3X04/multilogin%20-%20Nimble%20IP%20-%204.webp" alt=""><figcaption></figcaption></figure>

### Checking profile setup

7\. Click “**Check proxy**” to verify the setup was correct. You should see the external IP and country provided by Nimble appearing.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/gnEEtxmLQygIhvVyx96e/multilogin%20-%20Nimble%20IP%20-%205.webp" alt=""><figcaption></figcaption></figure>

8\. Click “**Create profile**” to save and use your profile.

### Additional setup options

In the example above, Nimble’s pipeline controls the target country for your proxy connection. Changing the target country in the pipeline settings will apply to all Multilogin profiles using this pipeline.

This is the recommended way to control country targeting; however, in case you prefer to control country setup from your Multilogin profiles, you can add a -country- value to the username string. For example: account-\[accountName]-pipeline-\[pipelineName]-**country-US**

You can review all gateway connection options in our Backconnect API documentation.
