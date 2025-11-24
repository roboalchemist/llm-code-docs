# Source: https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/integrate-using-klarna-web-sdk.md

# Integrate using Klarna Web SDK

## Here you can find the steps, examples, and code snippets you require for On-site messaging integration using our JavaScript library.

To add On-site messaging to your website, you first need to activate the feature in the [Klarna merchant portal](https://docs.klarna.com/resources/business-tools/merchant-portal-guide/conversion-boosters/) and check that you've all [prerequisites](https://docs.klarna.com/conversion-boosters/on-site-messaging/before-you-start/) covered.

If your site's On-site Messaging was set up prior to January 2024, take a look at our [guide](https://docs.klarna.com/conversion-boosters/on-site-messaging/additional-resources/migration-to-the-new-klarna-websdk/) to migrate to the new WedSDK.

## Step 1: Activation

### 1. Log in to the Merchant portal

Log in to the Merchant portal using one of the following links:

- [Merchant portal (production environment)](https://portal.klarna.com/)
- [Merchant portal playground (test environment)](https://portal.playground.klarna.com)


![ The login screen of the Merchant portal.](1cd86b60-b490-44d3-ba29-ed31aba2be69_OSM_Login_2022-11_01.jpeg)
*The login screen of the Merchant portal.*

To try out the feature, perform a test integration in the test (playground) environment, then follow the [Step 6](https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/integrate-using-klarna-web-sdk/#step-2-implementation-6-publish-the-changes-to-your-website) to complete the integration in the live (production) environment.

The changes you make in the playground environment won't impact your production integration.

### 2. Go to On-site messaging app

Once you're logged in, go to the **Conversion boosters** section on top or use the On-site messaging shortcut in the **Tools** section.


![ On-site messaging shortcuts in the Merchant portal.](e035b839-148f-45a3-a3ad-59e2a95a0835_Screenshot+2024-02-28+at+11.56.17.jpeg)
*On-site messaging shortcuts in the Merchant portal.*

### 3. Select the store to be configured

Now you can see the On-site messaging app on the sidebar. If you have access to multiple entities with the same user, select the corresponding one from the **dropdown selector**. The selector displays **Partner Accounts** or **Stores**, depending on your setup. Then click **Get started** to begin the activation.


![klarna docs image](b0d82dfa-b1b4-429b-8e6a-b0cd33e029cb_Screenshot+2024-02-28+at+11.36.36.jpeg)image

### 4. Allowlisting your domain

You can now allowlisting the origin domain where our Web SDK will be used.


![klarna docs image](411ad715-0d61-4ebc-96b8-273e720d01d4_Screenshot+2024-02-28+at+11.36.55.jpeg)image

## Step 2: Install JavaScript library

#### 1. Go to Installation

Once you've allowlisted your origin, you will have access to your client identifier and the snippets you need to implement on your website.


![ Click on Client Identifiers page to manage them.](70f2e262-7bcb-46bc-8c8e-988e8cfed45d_Screenshot+2024-02-29+at+10.37.48.jpeg)
*Click onClient Identifiers pageto manage them.*

### 2. Copy the installation snippet and add it to your website.

In **Add installation code**, go to **Web SDK** tab and click **Copy to clipboard** to copy the JavaScript library code snippet and insert the copied snippet in your website's source code right after the opening 

<body>

 tag.


![klarna docs image](e3b5d019-4459-4eca-b1e3-b3aa839ae72c_Screenshot+2024-02-29+at+10.54.03.jpeg)image

This library is the core of On-site messaging integration as it lets your website communicate with On-site messaging. The library renders the On-site messaging content in the placement tags.

###### *An example of an HTML file with the JavaScript library snippet. **You have to copy your own script from the Merchant portal**.*

``` html
<!DOCTYPE html>

<html>
<head>
<title>My store</title>
</head>
<body>
<script async="" data-client-id="your_klarna_live_client_" data-environment="playground | production" src="https://js.klarna.com/web-sdk/v1/klarna.js">
</script>
</body>
</html>
```

You need to add this web SDK only once, if you installed Express checkout before, skip step 2. and go directly to the step 3.

## Step 3: Add dynamic placements

### 1. View available placements

Once you've installed the JavaScript library, it's time to add placements.

A placement is an HTML tag with all the attributes required to display messaging on your website. You can think of it as the container for the messaging that the JavaScript library delivers. Some placements require the purchase amount to display the message.

Placements are available in Merchant portal. Go to **On-site messaging** and click **Placements**. You'll see all the placements available for your configuration.


![klarna docs image](999e2654-904c-4596-a1b9-438af04bbdd8_Screenshot+2024-02-29+at+11.26.03.jpeg)image

If you're promoting Klarna in multiple countries use the **Region**& **Country**dropdowns to view the relevant placement for each country.

You can also check the tags out in the [Placements section](https://docs.klarna.com/conversion-boosters/on-site-messaging/additional-resources/placements/) of our documentation.

If you're testing your integration in the test (playground) environment, a **TEST DRIVE** badge appears on each placement.

### 2. Copy the placement code

Find the placement you want to add to your website, then click **Copy to clipboard**.


![klarna docs image](d70ed1ac-a6fd-49f9-9638-52d494ad7d7d_Screenshot+2024-02-29+at+11.28.03.jpeg)image

The numerical values in the placement preview are placeholders and aren't representative of the true values you see in a live integration.

### 3. Add the placement to your website

You can now add the copied tag to your website. Insert placement code snippets **where you want the messaging to appear**.

###### *An HTML example with JavaScript library and a placement tag installed. When integrating, you have to copy your own placement tags from the Merchant portal as they're generated specifically for your configuration.*

``` html
<!DOCTYPE html>

<html>
<head>
<title>My store</title>
</head>
<body>
<script async="" data-client-id="your-data-client-id" data-environment="playground | production" src="https://js.klarna.com/web-sdk/v1/klarna.js">
</script>
    ...
    <!-- Placement v2 -->
<klarna-placement data-key="footer-promotion-auto-size" data-locale="en-GB"></klarna-placement>
<!-- end Placement -->
</body>
</html>
```

You can modify the look and feel of the On-site messaging placements. Use any of the two available ways to do so: [using CSS on your website](https://docs.klarna.com/conversion-boosters/on-site-messaging/additional-resources/styling-on-site-messaging-with-css/) or \[ using Klarna's Merchant Portal\].

### 4. Publish the changes to your website

You're now ready to publish the messaging to your site.

Before the go-live:

- You can also [customize the content](https://docs.klarna.com/conversion-boosters/on-site-messaging/additional-resources/styling-on-site-messaging-with-css/) to match your store's look and feel.
- Replace the playground JavaScript library snippet. Your client ID is different in playground and production. If you don't replace the snippet, the changes won't be visible in your production environment.


![klarna docs image](f65cdd76-5270-4974-8967-241313455e86_osm_go_live.jpeg)image

## Step 4: Go live

After you complete the integration in the test (playground) environment, follow these steps to display messaging in your live store.

### 1. Replace the playground JavaScript library snippet

Log in to the [Merchant portal (production environment)](https://portal.klarna.com/) and go to **On-site messaging**\> **Installation**.


![klarna docs image](f65cdd76-5270-4974-8967-241313455e86_osm_go_live.jpeg)image

Copy the installation snippet and insert it in place of the snippet you previously copied from the playground environment.

Don't skip this step as your client ID is different in playground and production. If you don't replace the snippet, the changes won't be visible in your production environment.

### 2. Customize styling for placements in production

If you've created any custom styles for placements in the playground environment and want to use them in production, you have to create them from scratch in the production Merchant portal. Currently, it is not possible to copy them between playground and production.

You don't have to replace the placement code snippets.


![klarna docs image](b9e8fd7b-32ff-480e-8a69-78e537aeb29d_custom-design.jpeg)image

### 3. Disclose tracking technologies used by Klarna Web SDK

If you choose to integrate the Klarna Web SDK on your website, for example but not limited to, to enable Klarna’s conversion boosters or other similar features, you are responsible for informing your users about the tracking technologies employed. This information must be provided prior to any tracking taking place, for instance via a cookie banner or similar mechanism.

You must disclose both strictly necessary tracking technologies and any specific technologies used by the Klarna Web SDK, including details such as name, purpose, provider, use of local storage, and retention period.

You may use the below wording as is, or adapt it to align with your existing cookie banner or privacy policy, provided the information remains complete, accurate, and compliant with applicable laws:

<span>*Strictly necessary cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. For the purpose of ensuring service security and prevention of fraud, we do also collect device fingerprints, including, but not limited to, your browser name, IP address, time zone and language preference and service availability.*</span>

| Name | Purpose | <span>Supplier (first/ third)</span> | <span>Session/ Persistent/local</span> | Expiry |
|----|----|----|----|----|
| <span>\_\_klarna_sdk_klarna-shopping-session</span> | <span>This cookie is used to ensure service security, service availability, and to prevent fraud.</span> | <span>Third party</span> | <span>Local storage</span> | 48h |

### 4. Validate if the integration is working as expected

## Troubleshooting integration

Something doesn't look quite right? Th the frequent integration errors and frequently ask

### I'm not happy with the loading time

Take a look at our \[ Best practices\] for tips about improving the loading time.

### On-site messaging is not loading on my page

- Check that your <klarna-placement> and script tags are valid HTML.
- Make sure you're only loading 1 instance of the JavaScript library per page.
- Check that you're using the snippet with the right `data-client-id` from the correct environment.
- On-site messaging is connected to your payment methods, so make sure everything is enabled and that Klarna payments is loaded on your checkout page.
- Often, the purchase amount isn't correct. Make sure you're sending the correct purchase amount in minor units.
- If all the above is working, check the network requests to js.klarna.com. Look for errors and 204s to find minor errors that keep On-site messaging from loading.

### Links on the placements sometimes are unclickable on mobile devices

On-site messaging is rendered inside shadow DOM to improve loading times. Using the Fastclick library makes the elements unclickable inside shadow DOM. This is a [known issue](https://github.com/ftlabs/fastclick/issues/604).

Here are some ways to fix the issue:

- Remove the FastClick library (optimal solution).
- Add the `needsclick` class to all shadowhost divs. Shadowhost divs of On-site messaging are added dynamically by the On-site messaging script while processing the placements. You have to observe the change and add the `needsclick` class only after a shadowhost div is appended. To query the elements where the `needsclick` class should be added, run the following:

###### *Querying elements that require a `needsclick` class.*

``` javascript
const elements = document.querySelectorAll('klarna-placement div')
```</klarna-placement></body>