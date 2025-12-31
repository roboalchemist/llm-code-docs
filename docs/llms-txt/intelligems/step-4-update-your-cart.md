# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-checkout-scripts/step-4-update-your-cart.md

# Step 4: Update your cart

Once you have published the checkout script, you should add a product to cart while previewing the lowest priced group. In certain cases, you may notice an issue in the cart when you do this. A few examples of things that may happen include:

* There may be a few visible line item properties in the cart
* The Intelligems discount message will occasionally show in the cart
* The compare-at price will not display correctly in the cart. For example, the compare-at price may show as the control group price, rather than the compare-at price for the test group you are in
* The cart will only show the control group prices in preview mode while the test is pending. This is expected; read more in the FAQ [here](https://docs.intelligems.io/price-testing/price-testing-faqs). Starting the test will show the correct prices.

Should any of these happen, follow the below corresponding guidance to correct the issue and complete the integration.

### Remove Hidden Line Item Properties[​](https://docs.intelligems.io/docs/pricing-integration/shopify-plus/update-cart#remove-hidden-line-item-properties)

Most Shopify stores use a convention that any line item with a leading underscore `_` should not be displayed in the cart. The Intelligems line item property (e.g. `_igLineItemDiscount`) in the Checkout Script you've just added begins with an underscore, so we will piggyback on this convention to make sure the Intelligems discount line item property is hidden.

Here is a common example of how this is implemented in a liquid cart (e.g. cart-line-items.liquid or a similar file). Many themes already contain this code, but it may be necessary to add if it is not already present. We recommend searching your theme file with a tool like [EZFY](https://chrome.google.com/webstore/detail/shopify-theme-file-search/mhchmhfecfdpaifljcfebnlaiaphfkmb) first to see if similar code already exists.

The key lines are as follows:

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

### Calculate the Intelligems Discount (per line item and cumulative)

If we're using the Checkout Scripts to apply a "hidden" discount on a product, we don't want to show the user that they're receiving an Intelligems discount. Locate the liquid file that renders each cart item, often called cart-line-items.liquid or something similar. Within that file, locate the beginning of the loop over each item. It will look something like the below:

```liquid
{% for item in cart.items %}

   ...
```

For each cart item, we'll want to check to see if an Intelligems discount was applied, and we'll want to keep track of the running total of Intelligems discounts. The snippet below under 'New', placed inside an existing code block which iterates over each cart item, will create a variable intelligems\_discount per line item which is either 0 or a non-zero number in cents which represents the Intelligems price change. This can also be used to adjust compare-at prices if desired.

***Old***

```liquid
{% for item in cart.items %}
   ...
{% endfor %}

```

***New***

```liquid
{% assign intelligems_total = 0 %}
{% for item in cart.items %}
    {% case item.properties._igp %}
      {% when "0" or nil or blank %}
        {% assign intelligems_discount = 0 %}
      {% else %}
        {% assign intelligems_discount = item.properties._igp | plus: 0 %}
        {% assign intelligems_total = intelligems_total | plus: item.properties._igp | times: item.quantity %}
    {% endcase %} 
   ....
{% endfor %}

```

Note that you'll only need one 'for' loop here (i.e. only one instance of the line\
\&#xNAN;*"for item in cart.items"*)

### Hide the Strikethrough Price in the Cart

Now that we have each item's Intelligems discount, we can prevent certain item properties (i.e. a strikethrough) from being rendered in the cart.

Within the 'for' loop described above, locate the code that renders the strikethrough price. It may look something like the below:

```liquid
{% if item.original_line_price and item.original_line_price != item.line_price %}
<span style="text-decoration:line-through;">{{ item.original_line_price | money }}</span><br>
{% endif %}

```

We might add the condition below to the code rendering the strikethrough:

```liquid
{% if ... and intelligems_discount == 0 %}
...
{% endif %}

```

In context, this will look like something like the below:

```liquid
{% if item.original_line_price and item.original_line_price != item.line_price and intelligems_discount == 0 %}
    <span style="text-decoration:line-through;">{{ item.original_line_price | money  }}</span><br>
{% endif %}

```

### Hide the Discount Message[​](https://docs.intelligems.io/docs/pricing-integration/shopify-plus/update-cart#hide-the-discount-message)

Sometimes discount messages appear to communicate bundle discounts, etc. In this case, we'll want to hide our message. We know from the checkout script in Step 4 that the Intelligems discount has the name "Discount" in most cases, so we'll hide any discount message with this name. Locate the code that renders the discount message, again in the 'for' loop over the cart's items. It will likely look something like the below:

```liquid
{% if item.message and item.message != "" %}
    <br><span>({{ item.message }})</span>
{% endif %}

```

We'll want to add the following condition to prevent "Intelligems" from being rendered as a discount name:

```liquid
{% if ... and item.message != "Discount" %}
    ...
{% endif %}

```

In context, this will look something like the below:

```liquid
{% if item.message and item.message != "" and item.message != "Discount" %}
    <br><span>({{ item.message }})</span>
{% endif %}
```

Note: there may be additional adjustments you want to make (e.g. adjusting a strikethrough on the subtotal). We recommend using the line item and running total discount variables you created above and similar conditional logic to implement these additional adjustment.

### Integrating Using HandleBars[​](https://docs.intelligems.io/docs/pricing-integration/shopify-plus/update-cart#integrating-using-handlebars)

Follow the example below if you use HandleBars in your theme. Add the HandleBar functions to the rest of your HandleBar functions.

<pre class="language-javascript"><code class="lang-javascript"><strong>Handlebars.registerHelper('noIgDiscount', function(arg1, options) {
</strong>    return (arg1.find(discount => discount.discount_application.title === 'intelligems' )) ? options.inverse(this) : options.fn(this) ;
});
Handlebars.registerHelper('hasExtraDiscounts', function(arg1, options) {
    return arg1.some(discount => discount.discount_application.title !== 'intelligems' ) ;
});
</code></pre>

```liquid
{{#if discountsApplied}}
   {{#if (hasExtraDiscounts discounts)}}
      <small class="cart__price--strikethrough">{{{price}}}</small>
      <span class="ajaxcart__price">
          {{{discountedPrice}}}
      </span>
  {{else}}
      <small class="cart__price">{{{price}}}</small>
  {{/if}}
            
  {{else}}
     {{#if shouldShowComparePrice}}                                           
       <small class="cart__price--strikethrough">{{{comparePrice}}}</small>                                                                                    
     {{/if}}     
      <span class="ajaxcart__price {{#if shouldShowComparePrice}}tw-text-red{{/if}} ">
          {{{price}}}
      </span>
{{/if}}

{{#if discountsApplied}}
  <div class="text-right grid__item">
      {{#noIgDiscount discounts}}
          {{#each discounts}}
              <small class="ajaxcart__discount cart__discount">
                  {{this.discount_application.title}}
                  (-{{{this.formattedAmount}}})
              </small>
          {{/each}}
          {{else}}
      {{/noIgDiscount}}
  </div>
{{/if}}
```
