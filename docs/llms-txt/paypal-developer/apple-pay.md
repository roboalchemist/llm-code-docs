# Integrate Apple Pay with JS SDK for direct merchants

## Apple Pay integration

Apple Pay is a mobile payment and digital wallet service provided by Apple Inc.

Buyers can use Apple Pay to make payments on the web using the Safari web browser or an iOS device.

Sellers can use Apple Pay to sell:

- Physical goods, such as clothes and electronics.
- Digital goods, such as software.
- Intangible professional services, such as concerts or gym memberships.

[Visit this site](https://developer.apple.com/documentation/passkit/apple_pay) for more information about Apple Pay.

![applepay-sheet-xxl-m.png](https://www.paypalobjects.com/ppdevdocs/img/applepay-sheet-xxl-m.png)

## Supported countries and currencies

Apple Pay supports payments in 34 countries and 22 currencies:

- **Countries:** Australia, Austria, Belgium, Bulgaria, Canada, China, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hong Kong, Hungary, Ireland, Italy, Japan, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Singapore, Slovakia, Slovenia, Spain, Sweden, United States, United Kingdom
- **Currencies:** AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD, USD

## How it works

The Apple Pay button shows up on your website when a customer uses the Safari web browser on an eligible device.

When your buyer selects the Apple Pay button:

- Your website shows the buyer a payment sheet.
- The buyer confirms the purchase details, such as the shipping address and payment method.
- The buyer authorizes the purchase on the payment sheet.

The payment sheet helps streamline the checkout process by showing the customer the information needed to make the payment.

Payment sheets can show the user's name, address, shipping information, and email address. You can customize this payment sheet to include the user details and payment information you need for your Apple Pay integration.

[Visit this site](https://support.apple.com/en-us/HT208531) for more details about Apple Pay's compatibility.

![applepay_mobile.png](https://www.paypalobjects.com/ppdevdocs/img/applepay_mobile.png)

## Integration video

Watch our video tutorial for this integration:

## Know before you code

You must be an approved partner to integrate the Apple Pay SDK.

For customers to pay with Apple Pay, they must be in a region where Apple Pay is supported, and their devices must meet the following requirements:

- Device compatibility: The device must support Apple Pay.
- iOS version: iOS 12.1 or later.
- Desktop: macOS 10.14.1 or later.
- Supported browsers: Safari. With the [latest Apple Pay SDK](https://applepay.cdn-apple.com/jsapi/1.latest/apple-pay-sdk.js) , customers can also pay using non-Safari browsers.

PayPal also provides iframe support for ApplePay. To use ApplePay within an iframe:

- The iframe tag must have the attribute allow="payment".
- The parent domain hosting the iframe needs to have its domain validated by following the usual process with PayPal.

## Create Apple Pay sandbox account

Create an Apple Pay sandbox account on the Apple Developer website to get a test wallet and test cards to test your Apple Pay integration.

If you already have an Apple sandbox account, you can use that account and move on to the next step.

- Create an [Apple developer account](https://developer.apple.com/).
- Create an [Apple sandbox account](https://developer.apple.com/apple-pay/sandbox-testing/).
- Get test cards from your Apple sandbox account.

## Integrate Apple JavaScript SDK

Use this script to integrate with the PayPal JavaScript SDK:

```html
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&currency=USD&buyer-country=US&merchant-id=SUB_MERCHANT_ID&components=applepay"></script>
```

Include `applepay` in the `components` list.

Use this script to integrate with the Apple JavaScript SDK:

```html
<script src="https://applepay.cdn-apple.com/jsapi/1.latest/apple-pay-sdk.js"></script>
```

PayPal's Apple Pay component interacts with your JavaScript code in 4 areas:

- Checking merchant eligibility for Apple Pay: `paypal.Applepay().config()`.
- Creating an Apple Pay session.
- Handling the `onvalidatemerchant` callback: `paypal.Applepay().validateMerchant()`.
- Handling the `onpaymentauthorized` callback: `paypal.Applepay().confirmOrder()`.

Before you show the Apple Pay button, make sure that you can create an Apple Pay instance and that the device can make an Apple Pay payment.

Use `ApplePaySession.canMakePayments` to check if the device can make Apple Pay payments.

## Register your sandbox domains

- Log into the PayPal Developer Dashboard.
- Register all high-level domains and subdomains that show the Apple Pay button, such as businessexample.com and checkout.businessexample.com.
- After the domains and subdomains are registered, you can test the Apple Pay buttons after you register the domains and subdomains.

## Create Apple Pay sandbox account

- Create an Apple Pay sandbox account on the Apple Developer website to get a test wallet and test cards to test your Apple Pay integration.

If you already have an Apple sandbox account, you can use that account and move on to the next step.

- Create an [Apple developer account](https://developer.apple.com/).
- Create an [Apple sandbox account](https://developer.apple.com/apple-pay/sandbox-testing/).
- Get test cards from your Apple sandbox account.

## Integrate Apple Pay checkout

Follow this integration process to add Apple Pay as a checkout option, customize the payment experience, and process payments.

## Test your integration

Test your Apple Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

Use your personal sandbox login information during checkout to complete a payment using Apple Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com) to see that the money has moved into your account.

- Open your test page with the Safari web browser on an iOS device or computer.
- Get a test card from your Apple sandbox account.
- Add the test card to your Apple Wallet on your iOS device or by using the Safari browser on the web.
- Tap the Apple Pay button to open a pop-up with the Apple Pay payment sheet.
- Make a payment using the Apple Pay payment sheet.
- If you have an additional confirmation page on your merchant website, continue to confirm the payment.
- Log in to your merchant account and continue to your confirmation page to confirm that the money you used for payment showed up in the account.

## Go live

Make Apple Pay available to buyers using your website or app.

## Important: Before going live, complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY) to process Apple Pay payments with your live PayPal account.

## Live environment

If you're a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business).

Use your personal production login information during checkout to complete an Apple Pay transaction. Then log into [paypal.com](https://www.paypal.com) to see the money move out of your account.

## Getting started in your live environment

Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.

- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Register your live domain on PayPal

- Add all high-level domains that show the Apple Pay button.
- Log into the PayPal Developer Dashboard.
- Select the Sandbox/Live toggle so it shows Live.
- Go to Apps & Credentials.
- Scroll down to Features &gt; Accept payments &gt; Advanced Credit and Debit Card Payments.
- Check if Apple Pay is enabled. If Apple Pay isn't enabled, select the Apple Pay checkbox and select the Save link to enable Apple Pay.
- Select the Manage link in the Apple Pay section.
- Select Add Domain and enter your domain name.
- Select Register Domain. If registration fails, check that the domain association file is live and saved to the right place on your live site.

## Register your live domain on PayPal

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.
- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Create Apple Pay sandbox account

- Create an Apple Pay sandbox account on the Apple Developer website to get a test wallet and test cards to test your Apple Pay integration.

If you already have an Apple sandbox account, you can use that account and move on to the next step.

- Create an [Apple developer account](https://developer.apple.com/).
- Create an [Apple sandbox account](https://developer.apple.com/apple-pay/sandbox-testing/).
- Get test cards from your Apple sandbox account.

## Integrate Apple Pay checkout

- Follow this integration process to add Apple Pay as a checkout option, customize the payment experience, and process payments.

## Test your integration

- Test your Apple Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

- Use your personal sandbox login information during checkout to complete a payment using Apple Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com) to see that the money has moved into your account.

## Go live

- Make Apple Pay available to buyers using your website or app.

## Important: Before going live, complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY) to process Apple Pay payments with your live PayPal account.

## Live environment

- If you're a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business).

Use your personal production login information during checkout to complete an Apple Pay transaction. Then log into [paypal.com](https://www.paypal.com) to see the money move out of your account.

## Getting started in your live environment

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.

- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Register your live domain on PayPal

- Add all high-level domains that show the Apple Pay button.
- Log into the PayPal Developer Dashboard.
- Select the Sandbox/Live toggle so it shows Live.
- Go to Apps & Credentials.
- Scroll down to Features &gt; Accept payments &gt; Advanced Credit and Debit Card Payments.
- Check if Apple Pay is enabled. If Apple Pay isn't enabled, select the Apple Pay checkbox and select the Save link to enable Apple Pay.
- Select the Manage link in the Apple Pay section.
- Select Add Domain and enter your domain name.
- Select Register Domain. If registration fails, check that the domain association file is live and saved to the right place on your live site.

## Register your live domain on PayPal

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.
- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Create Apple Pay sandbox account

- Create an Apple Pay sandbox account on the Apple Developer website to get a test wallet and test cards to test your Apple Pay integration.

If you already have an Apple sandbox account, you can use that account and move on to the next step.

- Create an [Apple developer account](https://developer.apple.com/).
- Create an [Apple sandbox account](https://developer.apple.com/apple-pay/sandbox-testing/).
- Get test cards from your Apple sandbox account.

## Integrate Apple Pay checkout

- Follow this integration process to add Apple Pay as a checkout option, customize the payment experience, and process payments.

## Test your integration

- Test your Apple Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

- Use your personal sandbox login information during checkout to complete a payment using Apple Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com) to see that the money has moved into your account.

## Go live

- Make Apple Pay available to buyers using your website or app.

## Important: Before going live, complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY) to process Apple Pay payments with your live PayPal account.

## Live environment

- If you're a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business).

Use your personal production login information during checkout to complete an Apple Pay transaction. Then log into [paypal.com](https://www.paypal.com) to see the money move out of your account.

## Getting started in your live environment

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.

- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Register your live domain on PayPal

- Add all high-level domains that show the Apple Pay button.
- Log into the PayPal Developer Dashboard.
- Select the Sandbox/Live toggle so it shows Live.
- Go to Apps & Credentials.
- Scroll down to Features &gt; Accept payments &gt; Advanced Credit and Debit Card Payments.
- Check if Apple Pay is enabled. If Apple Pay isn't enabled, select the Apple Pay checkbox and select the Save link to enable Apple Pay.
- Select the Manage link in the Apple Pay section.
- Select Add Domain and enter your domain name.
- Select Register Domain. If registration fails, check that the domain association file is live and saved to the right place on your live site.

## Register your live domain on PayPal

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.
- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Create Apple Pay sandbox account

- Create an Apple Pay sandbox account on the Apple Developer website to get a test wallet and test cards to test your Apple Pay integration.

If you already have an Apple sandbox account, you can use that account and move on to the next step.

- Create an [Apple developer account](https://developer.apple.com/).
- Create an [Apple sandbox account](https://developer.apple.com/apple-pay/sandbox-testing/).
- Get test cards from your Apple sandbox account.

## Integrate Apple Pay checkout

- Follow this integration process to add Apple Pay as a checkout option, customize the payment experience, and process payments.

## Test your integration

- Test your Apple Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

- Use your personal sandbox login information during checkout to complete a payment using Apple Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com) to see that the money has moved into your account.

## Go live

- Make Apple Pay available to buyers using your website or app.

## Important: Before going live, complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY) to process Apple Pay payments with your live PayPal account.

## Live environment

- If you're a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business).

Use your personal production login information during checkout to complete an Apple Pay transaction. Then log into [paypal.com](https://www.paypal.com) to see the money move out of your account.

## Getting started in your live environment

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.

- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Register your live domain on PayPal

- Add all high-level domains that show the Apple Pay button.
- Log into the PayPal Developer Dashboard.
- Select the Sandbox/Live toggle so it shows Live.
- Go to Apps & Credentials.
- Scroll down to Features &gt; Accept payments &gt; Advanced Credit and Debit Card Payments.
- Check if Apple Pay is enabled. If Apple Pay isn't enabled, select the Apple Pay checkbox and select the Save link to enable Apple Pay.
- Select the Manage link in the Apple Pay section.
- Select Add Domain and enter your domain name.
- Select Register Domain. If registration fails, check that the domain association file is live and saved to the right place on your live site.

## Register your live domain on PayPal

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.
- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Create Apple Pay sandbox account

- Create an Apple Pay sandbox account on the Apple Developer website to get a test wallet and test cards to test your Apple Pay integration.

If you already have an Apple sandbox account, you can use that account and move on to the next step.

- Create an [Apple developer account](https://developer.apple.com/).
- Create an [Apple sandbox account](https://developer.apple.com/apple-pay/sandbox-testing/).
- Get test cards from your Apple sandbox account.

## Integrate Apple Pay checkout

- Follow this integration process to add Apple Pay as a checkout option, customize the payment experience, and process payments.

## Test your integration

- Test your Apple Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

- Use your personal sandbox login information during checkout to complete a payment using Apple Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com) to see that the money has moved into your account.

## Go live

- Make Apple Pay available to buyers using your website or app.

## Important: Before going live, complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY) to process Apple Pay payments with your live PayPal account.

## Live environment

- If you're a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business).

Use your personal production login information during checkout to complete an Apple Pay transaction. Then log into [paypal.com](https://www.paypal.com) to see the money move out of your account.

## Getting started in your live environment

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.

- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Register your live domain on PayPal

- Add all high-level domains that show the Apple Pay button.
- Log into the PayPal Developer Dashboard.
- Select the Sandbox/Live toggle so it shows Live.
- Go to Apps & Credentials.
- Scroll down to Features &gt; Accept payments &gt; Advanced Credit and Debit Card Payments.
- Check if Apple Pay is enabled. If Apple Pay isn't enabled, select the Apple Pay checkbox and select the Save link to enable Apple Pay.
- Select the Manage link in the Apple Pay section.
- Select Add Domain and enter your domain name.
- Select Register Domain. If registration fails, check that the domain association file is live and saved to the right place on your live site.

## Register your live domain on PayPal

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.
- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Create Apple Pay sandbox account

- Create an Apple Pay sandbox account on the Apple Developer website to get a test wallet and test cards to test your Apple Pay integration.

If you already have an Apple sandbox account, you can use that account and move on to the next step.

- Create an [Apple developer account](https://developer.apple.com/).
- Create an [Apple sandbox account](https://developer.apple.com/apple-pay/sandbox-testing/).
- Get test cards from your Apple sandbox account.

## Integrate Apple Pay checkout

- Follow this integration process to add Apple Pay as a checkout option, customize the payment experience, and process payments.

## Test your integration

- Test your Apple Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

- Use your personal sandbox login information during checkout to complete a payment using Apple Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com) to see that the money has moved into your account.

## Go live

- Make Apple Pay available to buyers using your website or app.

## Important: Before going live, complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY) to process Apple Pay payments with your live PayPal account.

## Live environment

- If you're a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business).

Use your personal production login information during checkout to complete an Apple Pay transaction. Then log into [paypal.com](https://www.paypal.com) to see the money move out of your account.

## Getting started in your live environment

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.

- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Register your live domain on PayPal

- Add all high-level domains that show the Apple Pay button.
- Log into the PayPal Developer Dashboard.
- Select the Sandbox/Live toggle so it shows Live.
- Go to Apps & Credentials.
- Scroll down to Features &gt; Accept payments &gt; Advanced Credit and Debit Card Payments.
- Check if Apple Pay is enabled. If Apple Pay isn't enabled, select the Apple Pay checkbox and select the Save link to enable Apple Pay.
- Select the Manage link in the Apple Pay section.
- Select Add Domain and enter your domain name.
- Select Register Domain. If registration fails, check that the domain association file is live and saved to the right place on your live site.

## Register your live domain on PayPal

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.
- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Create Apple Pay sandbox account

- Create an Apple Pay sandbox account on the Apple Developer website to get a test wallet and test cards to test your Apple Pay integration.

If you already have an Apple sandbox account, you can use that account and move on to the next step.

- Create an [Apple developer account](https://developer.apple.com/).
- Create an [Apple sandbox account](https://developer.apple.com/apple-pay/sandbox-testing/).
- Get test cards from your Apple sandbox account.

## Integrate Apple Pay checkout

- Follow this integration process to add Apple Pay as a checkout option, customize the payment experience, and process payments.

## Test your integration

- Test your Apple Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

- Use your personal sandbox login information during checkout to complete a payment using Apple Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com) to see that the money has moved into your account.

## Go live

- Make Apple Pay available to buyers using your website or app.

## Important: Before going live, complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY) to process Apple Pay payments with your live PayPal account.

## Live environment

- If you're a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business).

Use your personal production login information during checkout to complete an Apple Pay transaction. Then log into [paypal.com](https://www.paypal.com) to see the money move out of your account.

## Getting started in your live environment

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.

- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Register your live domain on PayPal

- Add all high-level domains that show the Apple Pay button.
- Log into the PayPal Developer Dashboard.
- Select the Sandbox/Live toggle so it shows Live.
- Go to Apps & Credentials.
- Scroll down to Features &gt; Accept payments &gt; Advanced Credit and Debit Card Payments.
- Check if Apple Pay is enabled. If Apple Pay isn't enabled, select the Apple Pay checkbox and select the Save link to enable Apple Pay.
- Select the Manage link in the Apple Pay section.
- Select Add Domain and enter your domain name.
- Select Register Domain. If registration fails, check that the domain association file is live and saved to the right place on your live site.

## Register your live domain on PayPal

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.
- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Create Apple Pay sandbox account

- Create an Apple Pay sandbox account on the Apple Developer website to get a test wallet and test cards to test your Apple Pay integration.

If you already have an Apple sandbox account, you can use that account and move on to the next step.

- Create an [Apple developer account](https://developer.apple.com/).
- Create an [Apple sandbox account](https://developer.apple.com/apple-pay/sandbox-testing/).
- Get test cards from your Apple sandbox account.

## Integrate Apple Pay checkout

- Follow this integration process to add Apple Pay as a checkout option, customize the payment experience, and process payments.

## Test your integration

- Test your Apple Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

- Use your personal sandbox login information during checkout to complete a payment using Apple Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com) to see that the money has moved into your account.

## Go live

- Make Apple Pay available to buyers using your website or app.

## Important: Before going live, complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY) to process Apple Pay payments with your live PayPal account.

## Live environment

- If you're a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business).

Use your personal production login information during checkout to complete an Apple Pay transaction. Then log into [paypal.com](https://www.paypal.com) to see the money move out of your account.

## Getting started in your live environment

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.

- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Register your live domain on PayPal

- Add all high-level domains that show the Apple Pay button.
- Log into the PayPal Developer Dashboard.
- Select the Sandbox/Live toggle so it shows Live.
- Go to Apps & Credentials.
- Scroll down to Features &gt; Accept payments &gt; Advanced Credit and Debit Card Payments.
- Check if Apple Pay is enabled. If Apple Pay isn't enabled, select the Apple Pay checkbox and select the Save link to enable Apple Pay.
- Select the Manage link in the Apple Pay section.
- Select Add Domain and enter your domain name.
- Select Register Domain. If registration fails, check that the domain association file is live and saved to the right place on your live site.

## Register your live domain on PayPal

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.
- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Create Apple Pay sandbox account

- Create an Apple Pay sandbox account on the Apple Developer website to get a test wallet and test cards to test your Apple Pay integration.

If you already have an Apple sandbox account, you can use that account and move on to the next step.

- Create an [Apple developer account](https://developer.apple.com/).
- Create an [Apple sandbox account](https://developer.apple.com/apple-pay/sandbox-testing/).
- Get test cards from your Apple sandbox account.

## Integrate Apple Pay checkout

- Follow this integration process to add Apple Pay as a checkout option, customize the payment experience, and process payments.

## Test your integration

- Test your Apple Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

- Use your personal sandbox login information during checkout to complete a payment using Apple Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com) to see that the money has moved into your account.

## Go live

- Make Apple Pay available to buyers using your website or app.

## Important: Before going live, complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY) to process Apple Pay payments with your live PayPal account.

## Live environment

- If you're a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business).

Use your personal production login information during checkout to complete an Apple Pay transaction. Then log into [paypal.com](https://www.paypal.com) to see the money move out of your account.

## Getting started in your live environment

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.

- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Register your live domain on PayPal

- Add all high-level domains that show the Apple Pay button.
- Log into the PayPal Developer Dashboard.
- Select the Sandbox/Live toggle so it shows Live.
- Go to Apps & Credentials.
- Scroll down to Features &gt; Accept payments &gt; Advanced Credit and Debit Card Payments.
- Check if Apple Pay is enabled. If Apple Pay isn't enabled, select the Apple Pay checkbox and select the Save link to enable Apple Pay.
- Select the Manage link in the Apple Pay section.
- Select Add Domain and enter your domain name.
- Select Register Domain. If registration fails, check that the domain association file is live and saved to the right place on your live site.

## Register your live domain on PayPal

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.
- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Create Apple Pay sandbox account

- Create an Apple Pay sandbox account on the Apple Developer website to get a test wallet and test cards to test your Apple Pay integration.

If you already have an Apple sandbox account, you can use that account and move on to the next step.

- Create an [Apple developer account](https://developer.apple.com/).
- Create an [Apple sandbox account](https://developer.apple.com/apple-pay/sandbox-testing/).
- Get test cards from your Apple sandbox account.

## Integrate Apple Pay checkout

- Follow this integration process to add Apple Pay as a checkout option, customize the payment experience, and process payments.

## Test your integration

- Test your Apple Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

- Use your personal sandbox login information during checkout to complete a payment using Apple Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com) to see that the money has moved into your account.

## Go live

- Make Apple Pay available to buyers using your website or app.

## Important: Before going live, complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY) to process Apple Pay payments with your live PayPal account.

## Live environment

- If you're a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business).

Use your personal production login information during checkout to complete an Apple Pay transaction. Then log into [paypal.com](https://www.paypal.com) to see the money move out of your account.

## Getting started in your live environment

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.

- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Register your live domain on PayPal

- Add all high-level domains that show the Apple Pay button.
- Log into the PayPal Developer Dashboard.
- Select the Sandbox/Live toggle so it shows Live.
- Go to Apps & Credentials.
- Scroll down to Features &gt; Accept payments &gt; Advanced Credit and Debit Card Payments.
- Check if Apple Pay is enabled. If Apple Pay isn't enabled, select the Apple Pay checkbox and select the Save link to enable Apple Pay.
- Select the Manage link in the Apple Pay section.
- Select Add Domain and enter your domain name.
- Select Register Domain. If registration fails, check that the domain association file is live and saved to the right place on your live site.

## Register your live domain on PayPal

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.
- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Create Apple Pay sandbox account

- Create an Apple Pay sandbox account on the Apple Developer website to get a test wallet and test cards to test your Apple Pay integration.

If you already have an Apple sandbox account, you can use that account and move on to the next step.

- Create an [Apple developer account](https://developer.apple.com/).
- Create an [Apple sandbox account](https://developer.apple.com/apple-pay/sandbox-testing/).
- Get test cards from your Apple sandbox account.

## Integrate Apple Pay checkout

- Follow this integration process to add Apple Pay as a checkout option, customize the payment experience, and process payments.

## Test your integration

- Test your Apple Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

- Use your personal sandbox login information during checkout to complete a payment using Apple Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com) to see that the money has moved into your account.

## Go live

- Make Apple Pay available to buyers using your website or app.

## Important: Before going live, complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY) to process Apple Pay payments with your live PayPal account.

## Live environment

- If you're a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business).

Use your personal production login information during checkout to complete an Apple Pay transaction. Then log into [paypal.com](https://www.paypal.com) to see the money move out of your account.

## Getting started in your live environment

- Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.

- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

## Register your live domain on PayPal

- Add all high-level domains that show the Apple Pay button.
- Log into the PayPal Developer Dashboard.
- Select the Sandbox/Live toggle so it shows Live.
- Go to Apps & Credentials.
- Scroll down to Features &gt; Accept payments &gt; Advanced Credit and Debit Card Payments.
- Check if Apple Pay is enabled. If Apple Pay isn't enabled, select the Apple Pay checkbox and select the Save link to enable Apple Pay.
- Select the Manage link in the Apple Pay section.
- Select Add Domain and enter your domain name.
- Select Register Domain. If registration fails, check that the domain association file is live and saved