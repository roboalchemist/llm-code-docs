# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/replo-page-builder.md

# Replo Page Builder

Integrating Intelligems with Replo is easy!

### For Price Testing

For a price testing integration, we can add the following selectors to the theme integration:

**Price:** `[data-replo-price]`\
**Compare Price:** `[data-replo-compare-price]`\
**Savings ($):** `[data-replo-compare-difference]`\
**Savings (%):** `[data-replo-compare-percentage]`

Save these tags while [tagging your prices](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices).

{% hint style="warning" %}
When using the Find & Replace feature, take caution to not use any auto-generated classes when generating selectors. If you have questions, reach out to Intelligems support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).
{% endhint %}
