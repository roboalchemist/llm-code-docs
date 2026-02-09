# Source: https://getlago.com/docs/integrations/taxes/lago-eu-taxes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Lago EU Taxes

Lago now features an automatic European tax detection integration for your customers.

## Enable Lago's EU Tax integration

Activate Lago's automatic EU tax detection in just a few steps:

1. Navigate to your Lago instance **Settings**;
2. Select the **'Lago EU Tax Management'** integration;
3. Enter or confirm your organization's country; and
4. Hit **'Connect'** to activate this integration.

## Automated EU tax rates detection

When you connect the Lago EU Tax Management integration, it automatically generates a list of standard European tax rates.
These rates, labeled as `automated` in Lago, are synchronized with the latest standard tax rates for European countries,
ensuring your tax calculations are always up-to-date and compliant.

Each tax rate begins with the `lago_` prefix, ensuring a uniform and easily identifiable format across your tax rate list.
This systematic approach simplifies the management and recognition of these automated tax entries within your system.

<Frame caption="Automated tax rates">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/automated-tax-rates.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=ef746ad0623c78dcb937f240813ba445" data-og-width="2404" width="2404" data-og-height="1352" height="1352" data-path="integrations/images/automated-tax-rates.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/automated-tax-rates.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=4ca1c55b6f6bf14d3dc9ecbb0b4513ce 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/automated-tax-rates.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=c1c84dda91591c671129ba3978057512 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/automated-tax-rates.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=73e75a0d26826a6689c9f4d3787e8bda 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/automated-tax-rates.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=80e9330fb9362e0df57edd579eb66248 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/automated-tax-rates.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=650304904caec553d1b607a91d15a0ac 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/automated-tax-rates.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=aaa1f951a8a8a41829ae836a59e294c1 2500w" />
</Frame>

## Auto-application of taxes: decision tree

<Frame caption="Automated tax rates">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-eu-taxes-decision-tree.jpg?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=0092646e2d989857a2059be8d9e7112e" data-og-width="8442" width="8442" data-og-height="4642" height="4642" data-path="integrations/images/lago-eu-taxes-decision-tree.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-eu-taxes-decision-tree.jpg?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=223061ae8de7a00116ee8dcc08c49c0a 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-eu-taxes-decision-tree.jpg?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=56e9a47b1f7690a76e4f55645321674b 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-eu-taxes-decision-tree.jpg?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=1d1c020247bde317c6e9b61eeba0555d 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-eu-taxes-decision-tree.jpg?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=3707e6352a75ebd2b5f24c9627c56c09 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-eu-taxes-decision-tree.jpg?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=3382e7939f0bc808bf1fa4533e976f31 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-eu-taxes-decision-tree.jpg?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=f65900990d5a968960b3fae0dae4c0bb 2500w" />
</Frame>

Lago's initial step in the automated tax application involves verifying if a customer has a `tax_identification_number`.
This check occurs whenever a customer's profile is created or updated, ensuring that the most current tax-related information
is used in subsequent processes.

### B2B tax decision process

When a `tax_identification_number` is identified on a customer profile, Lago conducts a real-time verification
using the [EU's VAT Information Exchange System (VIES)](https://ec.europa.eu/taxation_customs/vies/#/vat-validation) to
confirm the existence of the company.

**In case the VIES check matches a valid company:**

1. If the customer's company is registered in the same country as your organization, Lago applies the customer
   country's tax rate;
2. If the customer's company is registered in the same country as your organization, but there is a tax exception for a particular zipcode, Lago applies the tax exception of this specific zipcode; or
3. If the customer's company is registered in a different country than your organization, Lago implements a
   **reverse charge** mechanism, applying a 0% tax rate.

### B2C tax decision process

If the VIES check does not confirm an active company or if no `tax_identification_number` is provided,
Lago then assesses the `country` associated with your customer. Based on this:

1. If your customer's `country` is unspecified, Lago defaults to applying your organization's country tax rate; or
2. If your customer's `country` is within the European Union, Lago applies the tax rate corresponding your customer's EU country; or
3. If your customer's `country` is outside the European Union, Lago applies a **tax exempt** rate at 0%.

## Guidelines for VIES checks by Lago

Lago performs VIES verifications under these circumstances:

* The Lago EU Tax Management integration is activated;
* A customer profile is either created or updated. Changes in customer details could influence their applicable tax rates;
* Zipcodes are important to define tax exceptions. Make sure to define them for all your customers; and
* When a new tax rate is identified for a customer, Lago automatically updates the customer's profile by replacing the old tax rate with the new one.

## Logging VIES verifications

Lago ensures transparency and compliance by logging each VIES check. This occurs whenever you create or update a customer.
For each check, Lago dispatches a webhook message. This allows you to record these validations for compliance purposes.
You can access and review any of these automated checks as needed.
