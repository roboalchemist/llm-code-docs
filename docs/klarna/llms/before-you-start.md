# Source: https://docs.klarna.com/conversion-boosters/on-site-messaging/before-you-start.md

# Source: https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/before-you-start.md

# Source: https://docs.klarna.com/conversion-boosters/express-checkout/before-you-start.md

# Source: https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-hpp/before-you-start.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/sap-commerce-cloud/before-you-start.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/vtex/before-you-start.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/salesforce-commerce-cloud/before-you-start.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/before-you-start.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/prestashop/before-you-start.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/woocommerce/before-you-start.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/before-you-start.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/wix/before-you-start.md

# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/adyen/before-you-start.md

# Before you start

## Leverage the Adyen-Klarna partnership to offer seamless payment experiences, with easy onboarding for existing Adyen users and flexible integration options for new businesses.

## Overview

Adyen is a powerhouse in the realm of financial technology, providing an all-encompassing solution that caters to the needs of leading businesses across the globe. It's not just a payment processor; Adyen offers a seamless, end-to-end payment experience, combined with rich, data-driven insights and an array of financial products, all integrated into one global platform. This innovative approach enables businesses to expand their operations, enhance customer experiences, and achieve their strategic goals with unprecedented speed and efficiency. With Adyen, companies are equipped to navigate the complexities of the digital economy, making it the go-to partner for achieving scalable growth and success.

### New to Adyen and Klarna?

[Find out how you can benefit from our partnership](https://www.klarna.com/international/business/adyen/). Once you’re ready to get started, contact Adyen to learn how to complete your integration. Klarna is supported through various Adyen integration types, including API-only integration, drop-in and components for web and mobile platforms, or third-party plug-ins. The integration journey varies depending on which type you have in place. To learn how to integrate the various Adyen integration types for Klarna Payments, please refer to Adyen's [Klarna integration guide](https://docs.adyen.com/payment-methods/klarna). For more general information about Adyen's different integration types, please refer to Adyen's [online payments](https://docs.adyen.com/online-payments) page.

### Already integrated with Adyen

This documentation outlines different integration options and guides you through seamlessly adding Klarna to your checkout. Our best practices help you get the most out of your partnership with Klarna.

## Automatic onboarding via Adyen

To add Klarna to your Adyen integration, follow these steps:

1.  Log into your [Adyen Customer Area](https://authn-live.adyen.com/authn/ui/login?request=eyJBdXRoblJlcXVlc3QiOnsiYWN0aXZpdHlHcm91cCI6IkJPX0NBIiwiY3JlZHNSZWFzb24iOlsiTG9nZ2luZyBpbiB0byBhcHBsaWNhdGlvbiBjYSJdLCJmb3JjZU5ld1Nlc3Npb24iOiJmYWxzZSIsImZvcmdvdFBhc3N3b3JkVXJsIjoiaHR0cHM6XC9cL2NhLWxpdmUuYWR5ZW4uY29tXC9jYVwvbG9iYnlcL3Bhc3N3b3JkLXJlc2V0XC9mb3Jnb3QtcGFzc3dvcmQiLCJyZXF1ZXN0VGltZSI6IjIwMjMtMDEtMTZUMTU6MzY6MTIrMDE6MDAiLCJyZXF1ZXN0ZWRDcmVkZW50aWFscyI6W3siUmVxdWVzdGVkQ3JlZGVudGlhbCI6eyJhY2NlcHRlZEFjdGl2aXR5IjpbeyJBY2NlcHRlZEFjdGl2aXR5Ijp7ImFjdGl2aXR5R3JvdXAiOiJCT19DQSIsImFjdGl2aXR5VHlwZSI6IklNUExJQ0lUIiwibWlsbGlzZWNvbmRzQWdvIjo5MDAwMDB9fV0sInR5cGUiOiJQQVNTV09SRCJ9fSx7IlJlcXVlc3RlZENyZWRlbnRpYWwiOnsiYWNjZXB0ZWRBY3Rpdml0eSI6W3siQWNjZXB0ZWRBY3Rpdml0eSI6eyJhY3Rpdml0eUdyb3VwIjoiQk9fQ0EiLCJhY3Rpdml0eVR5cGUiOiJHUkFDRV9DT09LSUUiLCJtaWxsaXNlY29uZHNBZ28iOjB9fV0sInR5cGUiOiJUV09fRkFDVE9SIn19XSwicmVxdWVzdGluZ0FwcCI6ImNhIiwicmV0dXJuVXJsIjoiaHR0cHM6XC9cL2NhLWxpdmUuYWR5ZW4uY29tXC9jYVwvY2FcLyIsInNpZ25hdHVyZSI6IlYwMDJTY1JvYm85QlVRUW1zOEJtRmhzaTJsN1wvRXZxUVREMkd5T2xEbk11YzU0UjA9In19).
2.  If you have multiple accounts, make sure you’ve selected the account to which you want to add Klarna.
3.  Go to **Settings**\> **Payment methods**.
4.  Click **Request payment methods**.
5.  Enter the name **Klarna** and select **Klarna Pay Now**, **Klarna Pay Later**, and **Klarna Pay Over Time**.
6.  Enter your details, then click **Submit** to complete the process.

All the heavy lifting is done and you will receive a Klarna activation email within a minute. Depending on your Adyen integration, you may need to perform some additional steps to make Klarna available in your checkout. Please note that line items are required for payments request towards Adyen to initiate a Klarna session. For more details, please refer to Adyen's [Klarna integration guide](https://docs.adyen.com/payment-methods/klarna).