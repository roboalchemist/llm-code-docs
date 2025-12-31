# Source: https://docs.intelligems.io/developer-resources/javascript-api/campaigns-object/campaigns.getgwp-options.md

# campaigns.getGWP(options)

Returns all eligible Gift-with-Purchase tiers for the current user's cart.

**Parameters**

**options** *(object, optional)*:

* **achieved** *(boolean, optional)* - When `true`, returns only gift-with-purchase tiers that the user has qualified for based on their current cart. When `false` or omitted, returns all available gift-with-purchase tiers regardless of qualification status.

**Example**

```javascript
console.log(igData.campaigns.getGWP({achieved: true}))
[
  {
    giftWithPurchaseProductId: "7191907565616",
    giftWithPurchaseVariantId: null,
    autoAddGiftWithPurchase: false,
    giftWithPurchaseHandle: "ceramic-risotto-plate",
    id: "0c8f4018-4b42-45ae-9fc4-8f5a9969c32a",
    minimumUnits: 100,
    unitDiscount: 0,
    isFreeShipping: true,
    isGiftWithPurchase: true,
  }
]
```

**Return**

The function returns a list of tiers:

```javascript
[
 {
  autoAddGiftWithPurchase: boolean, //if Intelligems will automatically add the GWP to cart
  giftWithPurchaseProductId: string | null, // Shopify Product ID (i.e. "7191907565616")
  giftWithPurchaseVariantId: string | null, // Shopify Variant ID (i.e. "435713513473145")
  giftWithPurchaseHandle: string | null, // Shopify handle (i.e. /products/<handle>)
  isGiftWithPurchase: boolean,
  isFreeShipping: boolean,
  minimumUnits: integer, // minimum requirement to be eligible, in dollars or items
 }
]
```

### Adding a Gift-with-Purchase to the Cart

When adding your own GWP to the cart, all you need to do is add `{"_igGWP": "true"}` to the item properties.

#### Example

```javascript
fetch("/cart/add.js", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
      },
    body: JSON.stringify({
        items: [{
            id: variantID, 
            quantity: 1, 
            properties: {_igGWP: "true"}
        }])
    }
);
```
