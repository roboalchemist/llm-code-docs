# Source: https://docs.klarna.com/klarna-search/integrate-klarna-search/detailed-product-data.md

# Detailed product data

| Field | Description |
|-----|-----------|
| AdultContent | Indicate if a product includes sexually suggestive content (yes/no). |
| AgeGroup | The demographic for which your product is intended. |
| Bundled | Indicates a product is a merchant-defined custom group of different products featuring one main product (yes/no). |
| Sale Price | The product sale price including VAT. The currency should be stated. Use a comma or a period as the decimal marker. Keep empty if the product is not on sale. Information in this column will override your original Price column. The length of your sale period. When you specify the sale price effective date (in combination with a sale_price attribute), we can display your sale price and the sale period directly in your listings. The sale price effective date can be specified in several ways, and you can define it with a specific time. * 2024-11-24T13:00-0800/2024-11-29T15:30-0800 (typical) * 2024-11-07T00:00:00+02:00/2024-12-07T23:59:59+01:00 (with a colon in the timezone) * 2024-11-07T00:00:00Z/2024-12-07T23:59:59Z (UTC timezone represented with a Z) * 2024-11-24T13:00:00-0800/2024-11-29T15:30:00-0800 (with seconds) * 2024-11-24/2024-11-29 (Without time and timezone, defaults to 00:00/23:59 UTC) * 2024-11-24T13:00/2024-11-29T15:30 (With time but no timezone, defaults to UTC) If the time is not specified on your product offer, the sale price will start at 00:00 (midnight) on the start date and end at 23:59 on the end date (UTC). |
| Color | Your product’s color(s). |
| EnergyEfficiencyClass | Your product’s energy label. |
| Gender | The gender for which your product is intended. |
| Condition | The condition of your product at time of sale. We support the following values: * New- The item is new, in its original packaging, and has never been opened/used. With full original manufacture warranty and standard return policy. * Used- The item is used. For example, a display model/demo unit or because the packaging is damaged or completely missing. * Refurbished- The item is not new but has been inspected and tested to ensure that it feels like a new product. For example, defective parts have been replaced, but the item may still show signs of use. It may come with or without the original packaging. |
| GroupId | The ID for a group of products that come in different versions (variants). |
| Material | Your product’s fabric or material. |
| Multipack | The number of identical products sold within a merchant-defined multipack (yes/no). |
| Pattern | Your product’s pattern or graphic print. |
| Size | Your product’s size. |
| SizeSystem | The country of the size system used by your product |