# Source: https://learn.microsoft.com/en-us/clarity/e-commerce-insights

Title: E-Commerce Insights

URL Source: https://learn.microsoft.com/en-us/clarity/e-commerce-insights

Markdown Content:
If you're an E-commerce site, Clarity is here to help you better understand your Purchases, Abandonments, and Product views. The features include:

1.   [Purchases](https://learn.microsoft.com/en-us/clarity/e-commerce-insights#purchases)
    1.   [Purchases filter](https://learn.microsoft.com/en-us/clarity/e-commerce-insights#purchases-filter)
    2.   [Purchases card](https://learn.microsoft.com/en-us/clarity/e-commerce-insights#purchases-card)

2.   [Checkout Abandonment](https://learn.microsoft.com/en-us/clarity/e-commerce-insights#checkout-abandonment)
    1.   [Checkout Abandonment filter](https://learn.microsoft.com/en-us/clarity/e-commerce-insights#checkout-abandonment-filter)
    2.   [Checkout Abandonment card](https://learn.microsoft.com/en-us/clarity/e-commerce-insights#checkout-abandonment-card)

3.   [Products](https://learn.microsoft.com/en-us/clarity/e-commerce-insights#products)
    1.   [Product Information filters](https://learn.microsoft.com/en-us/clarity/e-commerce-insights#product-information-filters)
    2.   [Most Viewed Products card](https://learn.microsoft.com/en-us/clarity/e-commerce-insights#most-viewed-products-card)

Note

*   The Purchases feature is only available on Clarity projects of Shopify sites.
*   Checkout Abandonment feature is only available on Clarity projects of Shopify Plus sites.
*   Product Information is only available for sites that use Product Json LD.

Clarity Purchases metric shows the percentage of all site sessions resulting in a successful purchase. This metric is available to Shopify sites as both a filter (on all tabs) and a Dashboard card:

The Purchases filter allows you to filter for data from only sessions that did or didn't purchase a product. See [Product filters](https://learn.microsoft.com/en-us/clarity/filters/clarity-filters#filtering-by-product).

The Purchases card appears automatically on the Clarity Dashboard of any Shopify site.

![Image 1: Purchases card in Dashboard.](https://learn.microsoft.com/en-us/clarity/media/purchases-card.png)

You can dig deeper with the widget in two ways:

1.   Filter to sessions with Purchases by selecting on the pie chart.

![Image 2: Select on purchases pie chart.](https://learn.microsoft.com/en-us/clarity/media/purchase-card-pie-chart.png)

The Dashboard now refreshes with the applied Purchase filter data only from sessions, which contained a successful purchase.

![Image 3: Applied Purchases filter data.](https://learn.microsoft.com/en-us/clarity/media/applied-purchases-filter.png)

2.   Select "Recordings" to watch recordings of sessions with Purchase.

![Image 4: Select recordings on purchases.](https://learn.microsoft.com/en-us/clarity/media/purchases-recordings.png)

The Recordings tab displays data only from sessions, which contained a successful purchase.

![Image 5: Recordings with purchases.](https://learn.microsoft.com/en-us/clarity/media/recordings-with-purchases.png)

Clarity's Checkout Abandonment metric shows the percentage of sessions that resulted in abandonment. In other words, how many users abandoned the process before completing the purchase?

Clarity helps you understand where exactly the user dropped during the checkout process for Clarity projects of Shopify Plus users. Once the customer adds a product to the cart, the checkout process is divided into four core steps. These steps are structured by the Shopify e-commerce platforms:

1.   **Contact information**: the customer inputs name, email, and personal info.
2.   **Shipping method**: the customer enters the address or selects the preferred shipping method.
3.   **Payment**: the customer selects the payment method and enters the details.
4.   **Other**: any scenarios not captured by the previous steps. This includes custom steps like "Processing," scenarios where the product was out of stock, and so on.

Abandonment on the payment step indicates it was the last Checkout step that the customer visited before abandoning the process. A Customer could have abandoned by exiting the site or going back to the product page, and so on.

To help you understand where your users are dropping off during Checkout, it's available as both a filter and a Dashboard card.

The Checkout Abandonment filter allows you to filter data from only sessions that abandoned the Checkout process at the selected step. For example, if you're looking to investigate customers who dropped the Checkout process in the payment step, apply the filter as "Checkout Abandonment: at Payment." See [Checkout abandonment filters](https://learn.microsoft.com/en-us/clarity/filters/clarity-filters#filtering-by-product).

The Checkout Abandonment card appears automatically on the Clarity Dashboard of any Shopify Plus site.

![Image 6: Checkout abandonment card.](https://learn.microsoft.com/en-us/clarity/media/checkout-abandonment-card.png)

The top section that is a pie chart, captures the overall Checkout abandonment percentage. This percentage indicates the abandoned percentage out of all sessions that started the checkout. The denominator used in this case (number of sessions that started Checkout) is also listed in the widget.

The bottom bars section breaks down all checkout abandonments by step. These bars indicate dropped percentage on step X out of all the sessions that were abandoned. The [steps](https://learn.microsoft.com/en-us/clarity/e-commerce-insights#checkout-abandonment) used here are the same as mentioned earlier.

For the pie chart section, you can deep dive in two ways:

1.   Filter to sessions with any Checkout abandonment by selecting on the pie chart.

![Image 7: Checkout abandonment pie chart.](https://learn.microsoft.com/en-us/clarity/media/checkout-abandonment-pie-chart.png)

The Dashboard now refreshes with the applied Checkout abandonment filter with the data of the selected step.

![Image 8: Applied checkout abandonment.](https://learn.microsoft.com/en-us/clarity/media/applied-checkout-abandonment.png)

2.   Select "Recordings" to watch Recordings of sessions with any Checkout abandonment.

![Image 9: Select recordings on Checkout abandonment.](https://learn.microsoft.com/en-us/clarity/media/checkout-abandonment-recordings.png)

The Recordings tab appears with the applied Checkout abandonment filter.

![Image 10: Recordings With applied checkout abandonment.](https://learn.microsoft.com/en-us/clarity/media/recordings-with-checkout-abandonment.png)

To explore the bottom section, you can deep dive in three ways:

1.   Filter to sessions that abandoned Checkout at a specific step by selecting the step you're interested in.

![Image 11: Checkout abandonment step.](https://learn.microsoft.com/en-us/clarity/media/checkout-abandonment-step.png)

The Dashboard now refreshes with the applied Checkout abandonment filter. All data is now from the sessions that contained a Checkout abandonment on the selected step.

![Image 12: Applied checkout abandonment step.](https://learn.microsoft.com/en-us/clarity/media/applied-checkout-abandonment-step.png)

2.   Watch Recordings of sessions that abandoned Checkout at a specific step by selecting the "Recordings" icon.

![Image 13: Select recordings on checkout abandonment step.](https://learn.microsoft.com/en-us/clarity/media/checkout-abandonment-recordings-step.png)

The Recordings tab appears with the applied Checkout abandonment filter for your step.

![Image 14: Recordings with applied checkout abandonment step.](https://learn.microsoft.com/en-us/clarity/media/recordings-with-checkout-abandonment-step.png)

3.   Look at a Heatmap for the sessions that abandoned Checkout at a specific step by selecting the "Heatmap" icon.

![Image 15: Select heatmaps on checkout abandonment step.](https://learn.microsoft.com/en-us/clarity/media/checkout-abandonment-heatmap-step.png)

Note

Abandonment at Other step is not available on Heatmap. "Other" is a combination of various scenarios not covered by the previous steps, so there is no single URL for heatmap to display for it. 
The Heatmaps tab appears, with the applied Checkout abandonment filter for your step.

![Image 16: Applied heatmaps on checkout abandonment step.](https://learn.microsoft.com/en-us/clarity/media/applied-checkout-abandonment-heatmap.png)

Clarity's Product Information feature shows data for sites that instrument their products using the Product JSON.LD. This data is available as a set of filters including Name, Price, Brand, Availability, Average Rating, and Number of Ratings and a Dashboard card for your top viewed products.

The Product Information filters allow you to filter data from the sessions of a product that matched with the corresponding criteria. This includes criteria about Product Name, Price, Brand, Availability, Average Rating, and Number of Ratings. See [Product filters](https://learn.microsoft.com/en-us/clarity/filters/clarity-filters#filtering-by-product).

The Products card appears automatically on the Clarity Dashboard. The bars indicate the ordered and ranked most viewed products.

![Image 17: Most viewed products widget.](https://learn.microsoft.com/en-us/clarity/media/most-viewed-products-widget.png)

You can deep dive in three ways:

1.   Filter to sessions to view a specific product by selecting the bar or title area.

![Image 18: Select a product on the most viewed products card.](https://learn.microsoft.com/en-us/clarity/media/most-viewed-product-card.png)

The Dashboard now refreshes with the applied Product Name filter, showing data only from sessions that contained a view of this product.

![Image 19: View results with the applied product filter.](https://learn.microsoft.com/en-us/clarity/media/product-filter-applied.png)

2.   Select the "Recordings" icon to watch recordings of the sessions that contained a view on a specific product.

![Image 20: Select recording icon on most viewed product card.](https://learn.microsoft.com/en-us/clarity/media/most-viewed-product-select-recording.png)

The Recordings tab appears with the applied Product name filter.

![Image 21: View recording with applied product name filter.](https://learn.microsoft.com/en-us/clarity/media/product-name-applied-recording.png)

3.   Look at a Heatmap for the sessions with a specific product by selecting the "Heatmap" icon.

![Image 22: Select heatmap icon on most viewed products card.](https://learn.microsoft.com/en-us/clarity/media/most-viewed-product-select-heatmap.png)

The Heatmaps tab appears with the applied Product name filter.

![Image 23: View heatmap with applied product name filter.](https://learn.microsoft.com/en-us/clarity/media/product-name-applied-heatmap.png)

For more answers, refer to [E-Commerce insights FAQ](https://learn.microsoft.com/en-us/clarity/faq#e-commerce-insights).

:::column-end:::
