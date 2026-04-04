# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-3-update-your-cart.md

# Step 3: Update your cart

Once you have tagged your prices, you should add a product that is in the test to cart while previewing the test. In certain cases, you may notice an issue in the cart when you do this - a few examples of things that may happen include:

* There may be a few visible line item properties in the cart
* The compare-at price will not display correctly in the cart - for example, the compare price may show as the control price, rather than the compare price for the test group you are in

Should any of these happen, follow the below corresponding guidance to correct the issue and complete the integration.

### Remove Hidden Line Item Properties[​](https://docs.intelligems.io/docs/pricing-integration/shopify-plus/update-cart#remove-hidden-line-item-properties)

Most Shopify stores use a convention that states that any line item property with a leading underscore (\_) should not be displayed in the cart. Intelligems uses the line item property `'_igp'`, so as long as this convention is set up for your store, the Intelligems line item property will be automatically hidden.

If this convention is not already set up for your store, You may see something like this in the cart when you test it in preview mode:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-1786d3af7f6635547f08b1b40e4bb3705aadf525%2FScreenshot%202024-03-08%20at%201.17.37%20PM.png?alt=media" alt=""><figcaption></figcaption></figure>

Here is an example of how you can fix this by implementing the below in a liquid cart (i.e. cart-line-items.liquid or a similar file). The key lines are as follows:

```liquid
{% assign first_character_in_key = p.first | truncate: 1, '' %}
{% unless p.last == blank or first_character_in_key == '_' %}

```

This code should be implemented in a loop over each item property. In context, the code block may look something like the below:

```liquid
{% assign property_size = item.properties | size %}
{% if property_size > 0 %}
  {% for p in item.properties %}
    {% assign first_character_in_key = p.first | truncate: 1, '' %}
    {% unless p.last == blank or first_character_in_key == '_' %}
      {{ p.first }}:
      {% if p.last contains '/uploads/' %}
        <a href="{{ p.last }}">{{ p.last | split: '/' | last }}</a>
      {% else %}
        {{ p.last }}
      {% endif %}
    {% endunless %}
  {% endfor %}
{% endif %}
```

You can learn more about this [here](https://community.shopify.com/c/shopify-design/product-pages-get-customization-information-for-products/m-p/616525#toc-hId-287417639) under 'Hide line item properties (optional)'.

### Displaying the Correct Strikethrough Price in the Cart

Typically, you should not tag any prices within your cart while completing "Step 2: Tag your prices". However, if you do display a strikethrough price in the cart, you'll want to tag that to ensure the correct strikethrough price shows up for each group.
