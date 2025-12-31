# Source: https://docs.klarna.com/klarna-search/integrate-klarna-search/basic-product-data.md

# Basic product data

### SKU/ID

Use SKUs as IDs where possible. Since SKUs are unique, they can also help prevent you from accidentally reusing IDs which would result in products being discarded.

- Good SKU: ABC123
- Poor SKU: 1

### Name

Any product variant or model should be clearly stated. Our search engine and filters work using the information in this field. Try to use keywords you want to be found for.

- Good product name: Apple iPhone 12, 256GB, gray
- Poor product name: iPhone 12

Your product name will be used to match your product to our products and customer search. Include the important details that define your product. Put the most important details first— customers will usually see only the first 70 or fewer characters (including spaces) of your title, depending on screen size. Ideally, keep within these character limits for accessibility reasons. Use keywords. These will help connect your product with a customers search and help them recognize what you’re selling. Your keywords could include these types of product details:

- product name.
- brand.
- specific details about the product.

Don't include info about discounts, sales or stock info in the name.

### Price

The product's price should include the VAT. The currency should be stated. Use a comma or a period as the decimal marker.

- Good price: \$25
- Poor price: 25 excluding VAT

### Shipping costs

The product's shipping cost needs to combine all shipping-/order costs for the customer. For example, this can include the environmental, freight, or handling surcharge, as well as the packaging fee, and similar.

- Example: \$5

### Stock status

For starters, there must be a buy/order button so that the customer can buy or order the product. That being said, we allow chain stores to display their offline prices if they’re in stock in their offline stores. However, in these cases, the products has to be tagged as "out of stock" in your product feed with us. If the product can’t be purchased/ordered online or offline at all, it can’t be included in your product feed at all. We don’t distinguish if the product is in local or remote storage by the merchant. Your stock status in the product feed should always be based on your online storage status. It can’t, for example, show the stock status for one of your offline stores. Pre-order products can’t be tagged as "in stock." Use "pre-order" or "out of stock" instead,” alongside "in stock/out of stock," "Yes/No" or the number of products in stock.

- Good stock status: Yes, InStock, 100
- Poor stock status: Few, or N/A

### Delivery time

The promised delivery time is the time of the order in the number of days. It's important that the delivery time in the feed corresponds to the info on your site.

- Good delivery time: 5 working days
- Poor delivery time: Varies

### Manufacturer

The product manufacturer is used in our filters.

- Example: Adidas

### Manufacturer SKU/MPN

The manufacturer's unique article number is used by us for matching products.

- Use the SKU assigned by the manufacturer. Unless you’re the manufacturer, don’t use a value that you’ve created.
- Distinguish between variants and use the correct MPN for each product variant. Typically, each variant of a product (different colors or sizes) has its own manufacturer SKU, so make sure to submit the correct value. An exception is different sizes of apparel products, where all sizes often have the same MPN.
- Example: 1170-0500

### EAN/GTIN

The EAN code is a unique barcode number. It’s used by us to automatically match many product types and make them searchable in the barcode scanner in our app.

- Example: 0021299147573

### Condition

The condition of your product at time of sale. We support the following values:

- **New** - The item is new, in its original packaging, and has never been opened or used. With the full original manufacturer's warranty and standard return policy.
- **Used** - The item is used. For example, a display model/demo unit or because the packaging is damaged or completely missing.
- **Refurbished** - The item is not new but has been inspected and tested to ensure that it feels like a new product. For example, defective parts have been replaced, but the item may still show signs of use. It may come with or without the original packaging.

### URL

The URL to the product in your shop. It can also contain tracking parameters for analysis tools such as Google Analytics.

- Example: <https: product1.html="" www.yourstore.com="">

### Image URL

The URL to the product image. Use a static URL. The one you submit shouldn’t be changed unless the actual image is moved or replaced. For example, don’t use URLs with timestamps, cache values or parts that can be changed each time you generate feed data. A change to the URL will result in download and reprocessing. The CMYK format isn’t supported.

- Example: <https: product1.jpg="" www.yourstore.com="">

### Category

Use the full "breadcrumb trail" flow. Wherever possible, we recommend you include more granular categories as it classifies your product more precisely. 

- Example: Shoes\> Sport Shoes\> Running Shoes

Remember not to mix up different product types within the categories. One example is to avoid adding accessories for a coffee machine to the same category as the machines themselves. Use\> to separate multiple levels in a category. Also, include a space before and after the\> symbol. 

- Example: Clothing\> Women\> Dresses

For gender-specific products (e.g. clothes and perfume), it’s important to divide them up into Women, Men and Children. Our filters are partly based on the category names.

- Good category name: Clothes\> Women\> Pants
- Poor category name: Fashion & Clothes

### Description

The detailed information about the product. Our search engine and filters work using these details in this field. Try to include the keywords you want to be found for.

- Good product description: Red four-legged table with storage underneath. Ideal for living room or bedroom. Dimensions 100 x 50 cm.
- Poor product description: Really attractive and practical!</https:></https:>