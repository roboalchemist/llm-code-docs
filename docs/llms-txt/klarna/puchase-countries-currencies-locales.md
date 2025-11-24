# Source: https://docs.klarna.com/payments/web-payments/before-you-start/data-requirements/puchase-countries-currencies-locales.md

# Purchase country, locale, and currency

## When initiating a payment, you need to define a country, locale, and currency for the payment session. Learn which are the valid values for these parameters and how to map them.

## Country

We offer different payment methods and purchase flows depending on the country. It is important that you share with us the correct country in the request to initiate a payment. You need to sign an agreement (or addendum to an agreement) for each country you want to enable in your Klarna payments offer. Contact [merchant support](https://www.klarna.com/merchant-support/) to add a new country to your setup.

## Locale

We support a limited set of locales per country. You can check them next in the [Data mapping section](https://docs.klarna.com/payments/web-payments/before-you-start/data-requirements/puchase-countries-currencies-locales.md).

## Currency

We only support the local currency of each country.

## Data mapping

The following table shows the list of available countries, locales, and currencies for Klarna payments. **Important:** Keep in mind that the locale used will define also the expected characters in all data points. For example, if you define `locale=en-GR` , then data points are expected to be in latin characters and not greek characters. In order to send greek characters you should `define locale=el-GR`.

| **Country** | **`purchase_country`** | **`locale`** | **`currency`** |
|----|----|----|----|
| Australia | AU | en-AU | AUD |
| Austria | AT | de-AT, en-AT | EUR |
| Belgium | BE | nl-BE, fr-BE, en-BE | EUR |
| Canada | CA | en-CA, fr-CA | CAD |
| Czech Republic | CZ | cs-CZ, en-CZ | CZK |
| Denmark | DK | da-DK, en-DK | DKK |
| Finland | FI | fi-FI, sv-FI, en-FI | EUR |
| France | FR | fr-FR, en-FR | EUR |
| Germany | DE | de-DE, en-DE | EUR |
| Greece**\*** | GR | el-GR, en-GR | EUR |
| Hungary | HU | hu-HU, en-HU | HUF |
| Ireland (Republic of Ireland) | IE | en-IE | EUR |
| Italy | IT | it-IT, en-IT | EUR |
| Mexico | MX | en-MX, es-MX | MXN |
| Netherlands | NL | nl-NL, en-NL | EUR |
| New Zealand | NZ | en-NZ | NZD |
| Norway | NO | nb-NO, en-NO | NOK |
| Poland | PL | pl-PL, en-PL | PLN |
| Portugal | PT | pt-PT, en-PT | EUR |
| Romania | RO | ro-RO, en-RO | RON |
| Slovakia | SK | sk-SK, en-SK | EUR |
| Spain | ES | es-ES, en-ES | EUR |
| Sweden | SE | sv-SE, en-SE | SEK |
| Switzerland | CH | de-CH, fr-CH, it-CH, en-CH | CHF |
| United Kingdom | GB | en-GB | GBP |
| United States | US | en-US, es-US | USD |