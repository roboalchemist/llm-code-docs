# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/prestashop/conversion-boosters/how-to-enable-sign-in-with-klarna-in-prestashop.md

# How to enable Sign in with Klarna in PrestaShop

## This guide explains how to add Sign in with Klarna to your PrestaShop store.


![klarna docs image](e7dc3339-8065-4b32-8eb7-6a8bdcccd0bb-SIWK-Theme-Examples.jpeg)image

## What is Sign in with Klarna?

Sign in with Klarna (SIWK) speeds up your sign-in, sign-up, and checkout processes by leveraging existing Klarna accounts. Pre-saved shopper and payment data is automatically populated for a low-friction shopping experience that minimizes drop-off and results in higher conversion and sales.

To learn more about Sign in with Klarna, refer to the [product documentation](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/before-you-start/).

## Prerequisites

To be able to offer Sign in with Klarna, you have to first enable Klarna in your PrestaShop store by installing the [Klarna Payments for PrestaShop](https://docs.klarna.com/platform-solutions/e-commerce-platforms/prestashop/payments/klarna-payments-on-prestashop/) plugin.

After that, you will need to complete the required configuration details for Sign in with Klarna in the [Klarna Merchant Portal](https://portal.klarna.com), such as privacy, terms, redirect URLs, and scopes.

## Configuration in PrestaShop

### Redirect URL

The Redirect URL is built for your shop, available when Sign in with Klarna for PrestaShop is enabled. The Redirect URL pattern is **<https: %7burl-of-your-shop%7d="" callback="" klarna="" siwk="">** ; note that this callback URL must be publicly accessible via your shop server.

### Required Customer Data & Additional Customer Data

Some scopes are required for the PrestaShop integration, including: Email Address, Phone number, and Full name. These scopes are not configurable in the Klarna settings in your shop admin and **must match** the enabled scopes as set in the Klarna Merchant Portal; other scopes are optional and configurable.

### Styling

There are multiple styling options that can be configured, including Theme, Shape, and Alignment. You can read more about the button styling configurations [here](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/additional-resources/button-styling/).


![ Settings related to Sign in with Klarna enablement in Prestashop.](ZvQA07VsGrYSv8J3_SIWKforPrestaShop.jpeg)
*Settings related to Sign in with Klarna enablement in Prestashop.*

### Placements

Sign in with Klarna will only display on your shop once some placements are enabled. There are three page types where Sign in with Klarna are available for the integration: Authentication and Cart pages. Where to place the Sign in with Klarna button:

- Always place the button wherever the user can sign in or create an account, such as the Sign-in page and the Account creation page.
- Place the button where users are asked to provide profile information, such as the Cart page.

### Best Practices

Position the button in the section of the page before the manual alternative and include 'or' and a divider between the Klarna button and the manual alternative, to clearly indicate that 'Continue with Klarna' is an alternative option. Once the customer creates their account and is redirected back to your site, they should be taken back to your site in a logged in state to continue their journey, either exploring your site, or checking out. There shouldn’t be any additional steps after the customer creates their account, especially not asking for the same information that was provided during account creation, or asking to verify already verified details. More best practices can be found [here](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/additional-resources/best-practices/).

### Troubleshooting tips

#### Button doesn’t show on storefront

- Verify your account credentials, particularly client id and API key, are accurate
- Verify [your shop domain is](https://docs.klarna.com/resources/business-tools/merchant-portal-guide/settings/#client-identifiers)set as an Allowed Origin in [Klarna Merchant Portal](https://portal.klarna.com)

#### Klarna modal opens, and immediately closes

- Verify the scopes within [Klarna Merchant Portal](https://portal.klarna.com) are the same or greater than the scopes within your shop backoffice</https:>