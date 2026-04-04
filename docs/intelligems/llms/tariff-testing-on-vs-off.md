# Source: https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/tariff-testing-on-vs-off.md

# Tariff Testing: On vs Off

### About Intelligems Tariff App

Intelligems has created a dedicated [Tariff Support app](https://apps.shopify.com/tariff-support-by-intelligems) to help merchants navigate the complexities of tariff implementation. We recognize that tariffs can be incredibly painful and completely change the viability of brands. We believe in transparent pricing - you can seamlessly break out tariff charges on your products. These are transparent to your customers so they know exactly how much they're paying and why.

#### **Key Features:**

* Choose which products to show a broken out tariff charge
* Configure the percentage of your tariffs
* Use advanced targeting and conditions to manage who sees it

### Introduction

Testing tariffs on versus off allows you to measure the impact of tariff fees on customer behavior and conversion rates. By comparing user experiences with and without tariffs enabled, you can understand how tariff costs affect purchasing decisions, cart abandonment rates, and overall revenue. This A/B testing approach helps you make data-driven decisions about tariff implementation and pricing strategies.

### Setup Instructions

#### Step 1: Install and Configure Tariff App

1. Install the Tariff App [here](https://apps.shopify.com/tariff-support-by-intelligems)
2. Configure tariff settings for your products

#### Step 2: Create an Onsite Edits Test with a Javascript injection

In Intelligems, create a Content Test using the 'Onsite Edits' test type with two test groups. For this example, we'll name the groups 'Tariffs Off' and 'Tariffs On':

**Disabled Group (Control)**

Add this JavaScript snippet as a JS injection to disable tariffs for the control group:

```javascript
void fetch("/cart/update.js", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    attributes: {
      enableTariffs: false,
    },
  }),
});
```

**Enabled Group (Variant)**

Add this JavaScript snippet as a JS injection to enable tariffs for the test group:

```javascript
void fetch("/cart/update.js", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    attributes: {
      enableTariffs: true,
    },
  }),
});
```

{% hint style="success" %}
The only difference between the two code snippets is the `enableTariffs` attribute value:

* **Disabled Group**: `enableTariffs: false`
* **Enabled Group**: `enableTariffs: true`
  {% endhint %}

### Best Practices

* **Run the test for sufficient duration** to gather statistically significant data
* **Monitor key metrics** like conversion rate, average order value, and cart abandonment
* **Consider seasonal factors** that might affect tariff sensitivity
* **Test with different product categories** to understand varying customer responses
* **Document your findings** to inform future pricing and tariff decisions

### Measuring Success

Track these key performance indicators:

* Conversion rate comparison between groups
* Cart abandonment rates
* Average order value
* Revenue per visitor
* Customer feedback and satisfaction scores

Use these insights to optimize your tariff strategy and improve the overall customer experience.
