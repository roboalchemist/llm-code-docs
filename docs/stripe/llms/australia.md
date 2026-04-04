# Source: https://docs.stripe.com/tax/supported-countries/asia-pacific/australia.md

# Collect tax in Australia

Learn how to use Stripe Tax to calculate, collect, and report tax in Australia.

In Australia, Stripe Tax supports calculation and [collection of GST](https://www.ato.gov.au/business/gst/).

## When to register for tax collection

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights about your potential tax registration obligations in Australia. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the [monitoring tool works](https://docs.stripe.com/tax/monitoring.md).

See [Needs attention](https://dashboard.stripe.com/tax/locations?primary_tab=needs_attention) tab to get insights about your potential tax registration obligations in Australia. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the [monitoring tool works](https://docs.stripe.com/tax/monitoring.md).

Remote sellers must register in Australia if their sales of services or low-value goods to Australian individuals exceed 75,000 AUD in the past 12 months or are expected to in the next 12 months. Sales to GST-registered Australian businesses that are subject to reverse charge don’t count toward the threshold. Non-profit organizations who sell remotely have a higher 150,000 AUD threshold but the threshold monitoring tool doesn’t track this.

**Threshold**: 75,000 AUD (or 150,000 AUD for non-profit organizations)

**Time frame**: Previous or current year.

**Included transactions**: Any taxable transactions that reverse charge doesn’t apply to.

Stripe supports domestic registration in Australia for both Australian businesses and remote sellers.

If a remote business sells digital services or low-value goods into Australia exclusively through online marketplaces that are responsible for collecting tax on these sales, the seller isn’t required to register for GST in Australia. These sales don’t count toward the seller’s registration threshold.

## Register to collect tax

Find more information on how to register for GST in Australia on the government website:

- [Registration for businesses with an origin address in Australia](https://www.ato.gov.au/Business/GST/Registering-for-GST/)
- [Registration for remote sellers](https://www.ato.gov.au/Business/International-tax-for-business/Non-resident-businesses-and-GST/) (businesses based outside of Australia selling into Australia)

After you’ve registered to collect tax in Australia, go to [Registrations](https://dashboard.stripe.com/tax/registrations?location=au) to add your registrations to Stripe in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Australia.

After you’ve registered to collect tax in Australia, go to [Locations](https://dashboard.stripe.com/tax/locations?location=au) to add your registrations to Stripe in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Australia.

Learn more about [how to add your registration](https://docs.stripe.com/tax/registering.md#track-your-registrations-in-the-tax-dashboard) in the Dashboard.

## How we calculate taxes

When both your business and your customer are in Australia, Stripe calculates Australian GST unless the sale is exempt or zero-rated.

If you’re a remote seller and sell services to Australian customers, GST is typically collected on sales to individuals. No tax is charged on sales to business customers who provide their Australian Business Register (ABN) number.

When goods are shipped into Australia from abroad, Stripe treats the sale as an export and doesn’t calculate tax, unless you choose to calculate tax on cross-border sales of goods into Australia through the [tax registration settings](https://docs.stripe.com/tax/registering.md#track-your-registrations-in-the-tax-dashboard). Generally, businesses need to collect tax on these sales if they act as the importer for customs purposes. If goods are imported in the customer’s name, the sale is considered to occur outside Australia, and no Australian VAT is due.

Stripe doesn’t calculate GST on sales of imported low-value goods (valued 1,000 AUD or less) to Australian individuals unless you select the option to calculate tax on cross-border sales of goods into Australia.

If you provide services related to admission to events and other venues, Stripe Tax considers them taxable in the country where the venue or event is located.

Cross-border sales of goods into Australia might also be subject to import taxes and customs duties in Australia, which Stripe doesn’t calculate.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. Go to [Registrations](https://dashboard.stripe.com/tax/registrations) to access these reports. Learn more about [the different types of reports](https://docs.stripe.com/tax/reports.md).

Stripe provides reports of your completed tax transactions. Go to [Locations](https://dashboard.stripe.com/tax/locations) to access these reports. Learn more about [the different types of reports](https://docs.stripe.com/tax/reports.md).

You’re responsible for filing and remitting your taxes to Australia. Stripe doesn’t file taxes on your behalf. However, we do have trusted partners who can help manage your filing and remittance.

## Marketplace tax liability

Australia defines electronic distribution platform (EDP) operators as marketplace operators that might have tax collection obligations. To qualify as an EDP, a marketplace operator must set terms or conditions for the sale, process or enable customer payments, or handle ordering or delivery of the product. Businesses that only provides payment processing or maintain the technical infrastructure behind an online marketplace don’t qualify as EDPs. EDP operators must collect GST on:

- Sales of imported low-value goods by remote sellers to private individuals in Australia.
- Sales of digital services by remote sellers to private individuals in Australia.
