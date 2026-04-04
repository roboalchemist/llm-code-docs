# Source: https://docs.intelligems.io/general-features/targeting/product-targeting/how-to-set-up-collection-card-product-targeting.md

# How to Set Up Collection Card Product Targeting

By default, product card targeting only works on collection pages. To enable product card targeting on **search results**, **home pages**, and **custom pages**, you need to add a small script to your product card templates.

### Step 1: Locate Your Product Card Template

These are the cards that display each product in your collection.

<div align="left"><figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FwB2nhPmGcrHgHQB2l3hI%2FScreenshot%202026-01-22%20at%203.37.39%E2%80%AFPM.png?alt=media&#x26;token=223b8229-6193-4d09-870c-9d0b671538de" alt="" width="563"><figcaption></figcaption></figure></div>

Common locations for product card templates in Shopify themes:

* `snippets/card-product.liquid`
* `snippets/product-card.liquid`
* `snippets/product-grid-item.liquid`
* `sections/featured-product.liquid` (for featured product sections)

#### How to find it

1. In your Shopify admin, go to **Online Store → Themes**
2. Click **Actions → Edit code** on your active theme
3. Look in the `snippets/` or `sections/` folder for files with "product" or "card" in the name

### Step 2: Add the Product Data Script and Update Variable Names

Copy and paste this script at the beginning of your product card template, right after the opening `{%- if product -%}`  or  `{%- if card_product -%}` line:

```liquid
<script>
  window.igProductData = window.igProductData || {};
  window.igProductData["{{ product.id }}"] = {
    productId: {{ product.id | json }},
    handle: {{ product.handle | json }},
    tags: {{ product.tags | json }},
    collectionIds: [{% for col in product.collections %}{{ col.id }}{% unless forloop.last %},{% endunless %}{% endfor %}],
    inventory: {% assign total = 0 %}{% for v in product.variants %}{% assign total = total | plus: v.inventory_quantity %}{% endfor %}{{ total }},
    lowestVariantPrice: {{ product.price_min }}
  };
</script>
```

#### Update the variable names to match your template:

{% hint style="warning" %}
**Important:** The variable name must match what your template uses.
{% endhint %}

| Template Variable            | What to Replace                                   |
| ---------------------------- | ------------------------------------------------- |
| `{{ product }}`              | Keep script as-is                                 |
| `{{ card_product }}`         | Replace all `product` with `card_product`         |
| `{{ featured_product }}`     | Replace all `product` with `featured_product`     |
| `{{ your_custom_variable }}` | Replace all `product` with `your_custom_variable` |

Example for `card_product` variable:

```liquid
<script>
  window.igProductData = window.igProductData || {};
  window.igProductData["{{ card_product.id }}"] = {
    productId: {{ card_product.id | json }},
    handle: {{ card_product.handle | json }},
    tags: {{ card_product.tags | json }},
    collectionIds: [{% for col in card_product.collections %}{{ col.id }}{% unless forloop.last %},{% endunless %}{% endfor %}],
    inventory: {% assign total = 0 %}{% for v in card_product.variants %}{% assign total = total | plus: v.inventory_quantity %}{% endfor %}{{ total }},
    lowestVariantPrice: {{ card_product.price_min }}
  };
</script>
```

{% hint style="info" %}
**How to check:** Look at the top of your template file for lines like:&#x20;

* `{%- if product -%}` → Use  `product`
* `{%- if card_product -%}` → Use  `card_product`&#x20;
  {% endhint %}

### Step 3: Verify Installation

1. Navigate to a search results page or home page with product cards
2. Open your browser's developer console (press `F12` or `Cmd+Option+I`)
3. Type: `console.log(window.igProductData)`
4. Press Enter

**Expected result:** You should see an object with product IDs as keys:

```json
{
  "1234567890": { "productId": 1234567890, "handle": "product-1", "tags": [...] },
  "9876543210": { "productId": 9876543210, "handle": "product-2", "tags": [...] }
}
```
