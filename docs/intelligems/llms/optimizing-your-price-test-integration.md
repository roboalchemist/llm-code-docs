# Source: https://docs.intelligems.io/performance-optimization/optimizing-your-price-test-integration.md

# Optimizing Your Price-Test Integration

Intelligems uses a product and variant ID lookup algorithm to determine which product/variant each selected price element is associated with. This algorithm will first look for details closest to the selected element before searching outwards throughout the page; therefore, searching becomes less efficient as the search moves outward.

Intelligems highly recommends adding `data-product-id` and `data-variant-id` data attribute tags to relevant elements within your `*.liquid` files to increase performance, as this is the first (and most efficiently gathered) information looked for within the algorithm.

The following optimization mode may help determine the relative cost of each price lookup within your site's page.

### Optimization Mode (Beta)

Optimization mode may be entered by:

1. Entering the price selection mode within our builder widget
2. Adding `ig-opt=true` as a query parameter and refreshing the page.

The relative effectiveness of the product/variant ID lookup will now color all price elements. The best solution, in nearly every scenario, is to add the `data-product-id` and `data-variant-id` data attributes to the selected elements.

Collection pages will likely not have a selected variant ID. In this case, one of the following may be used:

1. If the first variant within the product will always be the lowest-priced, the following liquid variable may be used: `product.selected_or_first_available_variant`
2. If the first variant is not always the lowest-priced, or you are unsure, the following liquid snippet may be used to search for and return it.

```liquid
assign lowest_variant = product.first_available_variant
 for variant in product.variants 
  if variant.available
    if variant.price < lowest_variant.price 
      assign lowest_variant = variant
     endif
  endif
endfor 
```
