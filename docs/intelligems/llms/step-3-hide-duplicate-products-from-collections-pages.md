# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-duplicate-products/step-3-hide-duplicate-products-from-collections-pages.md

# Step 3: Hide duplicate products from collections pages

Find the liquid file that renders your collections pages. It may be called something like collection-page.liquid. Find the code block that renders each product in the collection and wrap it in the the following `unless` statement:

```liquid
{% unless product.tags contains "price_test" %}
 ...
{% endunless %}
```

In context, the code should look something like this:

```liquid
{% for product in collection.products %}
   {% unless product.tags contains "price_test" %}
      {%  
         render 'product-thumbnail',
         product: product
       %}
    {% endunless %}
{% endfor %}
```
