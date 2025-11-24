# Source: https://docs.stripe.com/tax/supported-countries/asia-pacific.md

# Collect tax in Asia Pacific

Learn how to use Stripe Tax to calculate, collect, and report tax in the Asia Pacific region.

In the Asia Pacific (APAC) region, Stripe supports tax calculation in the following countries. Click the links below to learn about the thresholds in each country and the types of goods and services we support.

- [AM](https://docs.stripe.com/tax/supported-countries/asia-pacific/armenia.md)

- [AU](https://docs.stripe.com/tax/supported-countries/asia-pacific/australia.md)

- [BH](https://docs.stripe.com/tax/supported-countries/asia-pacific/bahrain.md)

- [BD](https://docs.stripe.com/tax/supported-countries/asia-pacific/bangladesh.md)

- [KH](https://docs.stripe.com/tax/supported-countries/asia-pacific/cambodia.md)

- [GE](https://docs.stripe.com/tax/supported-countries/asia-pacific/georgia.md)

- [HK](https://docs.stripe.com/tax/supported-countries/asia-pacific/hong-kong.md)

- [IN](https://docs.stripe.com/tax/supported-countries/asia-pacific/india.md)

- [ID](https://docs.stripe.com/tax/supported-countries/asia-pacific/indonesia.md)

- [JP](https://docs.stripe.com/tax/supported-countries/asia-pacific/japan.md)

- [KZ](https://docs.stripe.com/tax/supported-countries/asia-pacific/kazakhstan.md)

- [KG](https://docs.stripe.com/tax/supported-countries/asia-pacific/kyrgyzstan.md)

- [LA](https://docs.stripe.com/tax/supported-countries/asia-pacific/laos.md)

- [MY](https://docs.stripe.com/tax/supported-countries/asia-pacific/malaysia.md)

- [NP](https://docs.stripe.com/tax/supported-countries/asia-pacific/nepal.md)

- [NZ](https://docs.stripe.com/tax/supported-countries/asia-pacific/new-zealand.md)

- [OM](https://docs.stripe.com/tax/supported-countries/asia-pacific/oman.md)

- [PH](https://docs.stripe.com/tax/supported-countries/asia-pacific/philippines.md)

- [SA](https://docs.stripe.com/tax/supported-countries/asia-pacific/saudi-arabia.md)

- [SG](https://docs.stripe.com/tax/supported-countries/asia-pacific/singapore.md)

- [KR](https://docs.stripe.com/tax/supported-countries/asia-pacific/south-korea.md)

- [TW](https://docs.stripe.com/tax/supported-countries/asia-pacific/taiwan.md)

- [TJ](https://docs.stripe.com/tax/supported-countries/asia-pacific/tajikistan.md)

- [TH](https://docs.stripe.com/tax/supported-countries/asia-pacific/thailand.md)

- [TR](https://docs.stripe.com/tax/supported-countries/asia-pacific/turkiye.md)

- [AE](https://docs.stripe.com/tax/supported-countries/asia-pacific/united-arab-emirates.md)

- [UZ](https://docs.stripe.com/tax/supported-countries/asia-pacific/uzbekistan.md)

- [VN](https://docs.stripe.com/tax/supported-countries/asia-pacific/vietnam.md)

## When and how to register for tax collection

There are different rules for when and how you need to register to collect tax depending on the country. Click the links above to learn about the thresholds for tax collection in each location.

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights about your potential tax registration obligations in each location. Stripe only monitors if you have reached a tax threshold for sales outside of the country your business is based in. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the [monitoring tool works](https://docs.stripe.com/tax/monitoring.md).

See [Needs attention](https://dashboard.stripe.com/tax/locations?primary_tab=needs_attention) tab to get insights about your potential tax registration obligations in each location. Stripe only monitors if you have reached a tax threshold for sales outside of the country your business is based in. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the [monitoring tool works](https://docs.stripe.com/tax/monitoring.md).

Stripe can collect tax if your business is based in Australia, Hong Kong, Japan, New Zealand and Singapore. Your business needs to be a remote seller with no physical presence (such as a shop or warehouse) to collect tax on Stripe in the other countries listed above.

After you’ve registered with a country, go to [Registrations](https://dashboard.stripe.com/tax/registrations) to add your registrations to Stripe in the Dashboard to start collecting tax on your transactions in that location.

After you’ve registered with a country, go to [Locations](https://dashboard.stripe.com/tax/locations) to add your registrations to Stripe in the Dashboard to start collecting tax on your transactions in that location.

## How we calculate taxes

Stripe can calculate tax for [any of the product tax codes you assign to your products](https://docs.stripe.com/tax/tax-codes.md) and for domestic and cross-border sales in Australia, Hong Kong, Japan, New Zealand and Singapore. For the other countries listed, Stripe only supports calculation for [digital products](https://docs.stripe.com/tax/tax-codes.md?type=digital) sold by remote sellers.

### Domestic transactions

A transaction where your business and your customer are in the same country is called a domestic transaction. Stripe assumes the sale of most goods or services to be taxable unless the tax authority has specifically made them exempt.

### Cross border transactions

A cross-border transaction is where your customer is located in a different country to your business or when goods are shipped from one country to another.

Stripe calculates tax on a cross-border transaction taking into account the following factors:

- The location of your business
- The tax registrations you’ve added to Stripe
- The location of the buyer
- The type of the product sold (based on which [product tax code](https://docs.stripe.com/tax/tax-codes.md) you assigned to your product)
- The status of the customer (whether they’re an individual or a business)

#### Digital products

Digital products are non-physical items or services that are delivered, given, or rendered electronically. This includes digital goods and electronically supplied services. We determine whether you’re selling digital products or physical goods using the [product tax code](https://docs.stripe.com/tax/tax-codes.md) you assigned to your product.

Digital products are generally taxable in the country where your customer is located. However sales of digital products to businesses in other countries might have reverse charge applied. With reverse charge, your business provides an invoice for the purchase so that your customer can calculate the tax.

#### Physical goods

When physical goods are shipped to a customer in a different country to your business, the transaction is referred to as an export. Exports are zero rated and Stripe applies the [zero rate](https://docs.stripe.com/tax/zero-tax.md). The transaction might still be subject to taxes and customs duties in the country your customer is in. Stripe doesn’t calculate these.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. Go to [Registrations](https://dashboard.stripe.com/tax/registrations) to access these reports. Learn more about [the different types of reports](https://docs.stripe.com/tax/reports.md).

Stripe provides reports of your completed tax transactions. Go to [Locations](https://dashboard.stripe.com/tax/locations) to access these reports. Learn more about [the different types of reports](https://docs.stripe.com/tax/reports.md).

You’re responsible for filing and remitting your taxes. Stripe doesn’t file taxes on your behalf.
