# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/integration-guides/adspower.md

# AdsPower

AdsPower provides stealthy browsers that allow you to use multiple social or e-commerce accounts on a single computer simultaneously by providing a unique browser fingerprint for each account. It also includes a browser automation tool that enables you to run multiple accounts simultaneously as if they were being accessed from different physical devices.

### Follow these steps to integrate Nimble IP with AdsPower

1. Sign up for an account at AdsPower.

* Download and install the [AdsPower software here.](https://share.adspower.net/rf7gskzRbmRSqfn)
* Launch AdsPower and create a new browser profile.
* Click "New profile" to generate a new virtual browsing profile.
* Enter your profile name, then scroll down to the proxy configuration.

<div><img src="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/008d6cc5-b3a5-4887-bc72-be327d850792/adsPower_1.png" alt="sPower 1.png"> <figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/SlhwVwcjGfuNI897XpnL/adsPower%201.png" alt=""><figcaption></figcaption></figure></div>

* Configure the proxy server with your browser profile.
* **HTTP is available with the Nimble IP.**

<div><img src="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a35035e-af94-4ee0-8aa0-309e6ff58270/adsPower_2.png" alt="adsPower 2.png"> <figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/xzUuAdqt3s89AaSlEp8i/adsPower%202.png" alt=""><figcaption></figcaption></figure></div>

In the Nimble User Dashboard, navigate to the Nimble IP page and click “add pipeline”.

<div><img src="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a637f679-7a38-4cd0-b802-3125fb1237c9/vmlogin_image_3.png" alt="vmlogin image 3.png"> <figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/WapVVECh2RLVEr0UKkU4/Nimble%20IP.png" alt=""><figcaption></figcaption></figure></div>

In your new pipeline, you will find the IP address, port, username, and password

<div><img src="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9594c0af-62a3-4ce3-8bf8-4ee38461d8b6/nimble_ip1.png" alt="nimble ip1.png"> <figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/0YPd3vxP48vtzvJ4KkwB/Nimbl%20IP%202.png" alt=""><figcaption></figcaption></figure></div>

To set up and test the proxy in the AdsPower dashboard:

1. Copy the proxy info from the Nimble user dashboard to the AdsPower platform.
2. Configure the proxy using the following information:

* Proxy type: HTTP
* IP address: [ip.nimbleway.com](https://tracking.nimbleway.com/SHp)
* Port: 7000
* Username: your pipeline username
* Password: your pipeline password

That's all! AdsPower will now use proxies from Nimble IP. To learn more about Nimble IP and open an account [visit our website](https://tracking.nimbleway.com/SHp).
