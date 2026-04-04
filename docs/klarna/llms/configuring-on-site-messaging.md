# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/prestashop/conversion-boosters/configuring-on-site-messaging.md

# Configuring On-site messaging in Prestashop

### Activate On-site messaging

The "On-site Messaging" section of the module contains configuration options and settings for Klarna On-site-Messaging. [On-site messaging](https://docs.klarna.com/conversion-boosters/on-site-messaging/before-you-start.md) is a way to let customers know that Klarna is available on your website. As of version 1.3.0+, On-site messaging is supported, for standard PrestaShop themes, such as [Classic](https://devdocs.prestashop-project.org/8/themes/).  Compatibility with non-standard themes is not guaranteed or supported. The **Client Identifier** is found in the [Klarna Merchant Portal](https://portal.klarna.com/), at Payments settings -\> Client identifier, or also from "Conversion boosters" top menu -\> On-site Messaging app -\> Installation. Ensure you copy it without quotes or whitespace.


![ Klarna Merchant Portal -> Client identifier](ZkNAoiol0Zci9Gi0_ClientIdentifiers.jpeg)
*Klarna Merchant Portal -> Client identifier*

Also, add your shop's domain in **Allowed origins** within **Client identifier** section.


![ Klarna Merchant Portal -> Allowed origin](af9e9cd4-44f4-4179-8287-87f3c7d49937-Allowed-origin.jpeg)
*Klarna Merchant Portal -> Allowed origin*

Paste the Client Identifier from the Klarna Merchant Portal in the **Client ID** field in the PrestaShop Klarna module, in the "Credentials" section.


![ PrestaShop Back Office -> Klarna module Credentials ](ZwbDuYF3NbkBXGbS_PrestaShopCredentials.jpeg)
*PrestaShop Back Office -> Klarna module Credentials*

Determine which placement types are desired; product and cart page placements are recommended.


![OSM configuration in Prestashop](ZwbGsYF3NbkBXGcD_PrestaShopOSM.jpeg)
*OSM configuration in Prestashop*

Data from the customer's browser for the shop (e.g. language and currency switcher) and shop data are used to determine the appropriate data-locale for the On-site messaging placement.  

- For all non-EUR currency, the code matches currency and checks for supported language. Based on the customer's chosen language, the module returns a locale. The currency list has only one match for each country, so the module has predefined regions based on currency, e.g. if currency PLN is matched, Polish language is used, data-locale would be pl-PL. If any other language were to be used, en-PL would be returned instead as no other language is supported for the Poland region.
- As EUR currency supports multiple regions, the logic is more complex. The module first uses the current billing country (e.g. if the customer entered address data in checkout). If the customer's country is not set, the module uses the default shop's country. Based on the country, the module searches for a region match. Then the module proceeds to check for language and returns a specific locale. For these cases, the module first respects the current country, so the region would not differ. (The module can't use language solely as language could be used in multiple countries. For example Belgium doesn't have a single national language so without respecting the country, Belgium region would never be used.)
- On both cases if no match is found (neither currency, nor country), the module returns default locale en-\*\* based on what is configured in Klarna's settings. This locale on install will be set to default to the shop's country.

Positioning of the displayed on-site messaging placement(s) on the shop page are not currently configurable within the module. This functionality may be added in the future, but a target date is not yet available.