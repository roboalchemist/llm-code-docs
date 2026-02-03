# Source: https://docs.intelligems.io/developer-resources/shopifys-universal-commerce-protocol-ucp-compatibility.md

# Shopify's Universal Commerce Protocol (UCP) Compatibility

## Intelligems and Shopify's Universal Commerce Protocol (UCP)

Shopify recently launched the Universal Commerce Protocol (UCP), an open standard for agentic commerce that enables AI assistants and platforms to interact with merchants through a unified checkout experience. This guide explains how Intelligems works with UCP and what it means for your store.

### What is UCP?

The Universal Commerce Protocol is an open standard co-developed by Shopify and Google that establishes a common language for commerce interactions. UCP standardizes three core capabilities:

* **Product Discovery**: How agents search and discover products across merchants
* **Checkout**: How checkout sessions are created, updated, and completed
* **Order Management**: How orders are tracked, fulfilled, and managed post-purchase

UCP enables AI agents and platforms to initiate purchases on behalf of users while ensuring you remain the Merchant of Record with full control over pricing, discounts, and customer relationships.

### Intelligems Compatibility with UCP

Intelligems operates at the Shopify backend level through Cart Transform Functions, Shopify Functions, and checkout modifications. When a UCP-compliant platform creates a checkout session with your store, Intelligems automatically applies the appropriate experience based on your segmentation rules.

{% hint style="success" %}
All Intelligems features work with UCP-enabled checkout flows when using Shopify Functions integration (the default for new installs). No configuration changes are required.
{% endhint %}

### Feature Compatibility

#### Price Testing

When an AI agent creates a checkout session via UCP, Intelligems identifies which price test group the user belongs to and returns the appropriate price.

**Technical details:**

* Intelligems calculates the correct price using Cart Transform Functions
* Prices are reflected in the checkout session `line_items` and `totals` arrays
* Price testing applies when the checkout session is created (not during product browsing)

**What to know:**

* Agents typically show standard catalog prices during product discovery
* Your price tests activate when purchase intent is clear and checkout begins

#### Offers (Discounts)

Intelligems offers modify cart totals based on user segments and integrate with UCP's discount extension.

**Technical details:**

* Offers appear in the checkout `totals` array with `type: "discount"`
* Progress bars, popups, and messaging components render in your Shopify checkout UI
* Server-side execution through Shopify Functions

**What to know:**

* All offer stacking rules and conditions are respected
* Volume discounts and tiered offers work as configured

#### Shipping Testing

Shipping tests leverage UCP's Fulfillment Extension to present different options to users in different test groups.

**Technical details:**

* Shipping variants appear in the `fulfillment.methods` array
* Each method includes `totals` showing shipping costs
* Shipping progress bars render in your checkout UI

**What to know:**

* Your shipping test logic determines available options per segment
* Free shipping thresholds work as configured

#### Checkout Experiences

Checkout blocks and custom experiences render when users are handed off to your Shopify checkout.

**Technical details:**

* UCP supports `status: requires_escalation` for complex flows
* Checkout blocks appear in the Shopify-hosted checkout UI via `continue_url`
* All Intelligems tracking continues normally

### How UCP Checkout Works with Intelligems

Here's the typical flow:

1. **Discovery**: An AI agent searches products. Standard catalog prices are shown.
2. **Checkout Creation**: The agent creates a checkout session via UCP API.
3. **Segmentation**: Intelligems identifies the user's test group based on your rules.
4. **Dynamic Response**: Your store returns a checkout with appropriate prices, discounts, and shipping.
5. **Updates**: As the user provides information, Intelligems continues applying the correct experience.
6. **Handoff**: The agent hands off to your Shopify checkout via `continue_url` for payment.
7. **Completion**: Order is placed with all modifications tracked correctly.

### What You Need to Do

**Nothing.** Your existing configurations work with UCP:

* Price tests
* Offer experiences
* Shipping tests
* Checkout blocks
* Segmentation rules

The same Shopify Functions that power your Intelligems experiences also power what your store returns to UCP platforms.

### Analytics and Monitoring

All Intelligems analytics continue working normally:

* Conversion rates tracked per test group
* Revenue attribution functions correctly
* Statistical significance includes UCP traffic
* Experiment results reflect all traffic sources

You can segment analytics by traffic source to compare UCP vs. traditional channels.

### Frequently Asked Questions

**Do I need to enable UCP compatibility?**\
No. If you're using Shopify Functions (default for new installs), you're already UCP-compatible.

**Will price tests show during product discovery?**\
During browsing, agents show standard catalog prices. Price tests apply when checkout begins.

**Can agents see my checkout content blocks?**\
Checkout content blocks render in your Shopify checkout when users are handed off via `continue_url`.

**Do stacking rules work with UCP?**\
Yes. All offer stacking rules and exclusions work as configured.

**Will UCP traffic affect my results?**\
No. UCP traffic is randomized into test groups like traditional traffic.

**What if I use Checkout Scripts?**\
Checkout Scripts are being sunset in August 2026. Migrate to Shopify Functions for full UCP compatibility. Contact support for migration help.

### Getting Help

If you have questions about UCP and your Intelligems configuration:

* Open a support ticket in the Intelligems app
* Email <support@intelligems.io>
* Reference this guide when contacting support

### Additional Resources

* [Shopify UCP Documentation](https://shopify.dev/docs/agents)
* [UCP Technical Specification](https://ucp.dev/)
* [Price Testing Integration Guide](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions)
* [Offer Experiences Guide](https://docs.intelligems.io/offer-experiences/offers-getting-started)

***

*Intelligems remains committed to supporting our customers as the e-commerce landscape evolves. UCP represents an exciting opportunity to optimize customer experiences across new surfaces and modalities while maintaining the rigorous testing and experimentation that drives your business forward.*
