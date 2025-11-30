# Source: https://www.electronjs.org/docs/latest/api/structures/product

# Product Object

- `productIdentifier` string - The string that identifies the product to the Apple App Store.
- `localizedDescription` string - A description of the product.
- `localizedTitle` string - The name of the product.
- `price` number - The cost of the product in the local currency.
- `formattedPrice` string - The locale formatted price of the product.
- `currencyCode` string - 3 character code presenting a product\'s currency based on the ISO 4217 standard.
- `introductoryPrice` [ProductDiscount](/docs/latest/api/structures/product-discount) (optional) - The object containing introductory price information for the product. available for the product.
- `discounts` [ProductDiscount](/docs/latest/api/structures/product-discount)\[\] - An array of discount offers
- `subscriptionGroupIdentifier` string - The identifier of the subscription group to which the subscription belongs.
- `subscriptionPeriod` [ProductSubscriptionPeriod](/docs/latest/api/structures/product-subscription-period) (optional) - The period details for products that are subscriptions.
- `isDownloadable` boolean - A boolean value that indicates whether the App Store has downloadable content for this product. `true` if at least one file has been associated with the product.
- `downloadContentVersion` string - A string that identifies the version of the content.
- `downloadContentLengths` number\[\] - The total size of the content, in bytes.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/product.md)