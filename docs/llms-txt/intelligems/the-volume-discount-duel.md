# Source: https://docs.intelligems.io/getting-started/common-use-cases/offer-test-common-use-cases/the-volume-discount-duel.md

# The Volume Discount Duel

[Experiences](https://github.com/intelligems-io/docs/blob/main/public-docs/getting-started/common-use-cases/offer-test-common-use-cases/broken-reference/README.md) allow you to serve specific discounts and offers to your site visitors. One of these types of Offers is a Volume Discount. While you can have such an Experience on all the time, Intelligems can also help you test which thresholds and discounts drive the most value.

You can do this by setting up an [Offer Test](https://docs.intelligems.io/offer-personalizations/testing-offer-personalizations).

*What this test design might look like:*

<table data-header-hidden><thead><tr><th width="203"></th><th></th><th width="215"></th><th></th></tr></thead><tbody><tr><td></td><td><strong>Control Discount</strong></td><td><strong>Higher Discount</strong></td><td><strong>Lower Discount</strong></td></tr><tr><td><strong>Product A</strong></td><td><p>15% off $100 or more</p><p>20% off $150 or more</p><p>25% off $200 or more</p></td><td><p>20% off $100 or more</p><p>25% off $150 or more</p><p>30% off $200 or more</p></td><td><p>10% off $100 or more</p><p>15% off $150 or more</p><p>20% off $200 or more</p></td></tr></tbody></table>

{% hint style="info" %}
We recommend taking a look at a histogram of your order values for the last month (or more) when deciding what Volume Discounts to test, especially if Volume Discounts will be a new addition to the site. For example, if a majority of your orders come in around $100, you may not want to provide a discount for orders over $100, but rather start around $150.
{% endhint %}
