# Source: https://docs.intelligems.io/developer-resources/cart-permalinks.md

# Cart Permalinks

[Cart Permalinks](https://shopify.dev/docs/apps/channels/cart-permalinks) are links that bring a visitor directly to Shopify checkout with specified items and discounts already in the cart. Under the hood, they create a new cart.

Since Intelligems links orders back to visitors for analytics by adding their Intelligems ID to the cart as a note, we need to make sure that ID is on the new cart in order for the resulting order to be tracked.

If the cart permalink is on a page as a normal HTML hyperlink, Intelligems will do this for you automatically. If you're directing the user to the cart permalink using Javascript (e.g., by a button action or redirect), you'll need to make a small edit to the URL in order for Intelligems to track the order.

We need to add a query parameter, `attributes[igId]` , set to the user's Intelligems ID, which is available from the Intelligems window object API. For example:

```
// cart permalink
const href = "https://my-shop-name.myshopify.com/cart/36485954240671:1?discount=mydiscountcode"

// convert to JS URL so that we can add query params
const url = new URL(href);

// get the Intelligems ID
const igId = window.igData?.user?.igId;

// igId might be undefined here if Intelligems is not loaded
if (igId) {
    // add the query param to the URL
    url.searchParams.set("attributes[igId]", igId);
}

// convert the URL object back to its string representation
const newHref = url.toString();
```
