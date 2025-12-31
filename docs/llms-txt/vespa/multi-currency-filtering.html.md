# Source: https://docs.vespa.ai/en/modules/e-commerce/multi-currency-filtering.html.md

# Multi-Currency Pricing

 

Vespa for e-commerce includes multi-currency pricing support for e-commerce applications with global product catalogs where products are priced in different currencies and sold across multiple markets. Multi-currency pricing refers to presenting and working with prices in multiple currencies, enabling applications to query, filter, and rank products using prices expressed in the buyer’s preferred currency. This enables filtering by price range in any currency and using converted prices in ranking, with automatic currency conversion when market-specific pricing is not available.

## Overview

The multi-currency pricing feature supports:

- **Per-market pricing** - Define different prices for different markets on each product.
- **Keeping track of exchange rates** - An N×N tensor mapping of currency-to-currency exchange rates is stored in a "forex" document, and can be updated at any time.
- **Automatic currency conversion** - Fallback to a default market when no other market-specific price exists for the buyer's market.
- **Query-time filtering** - Filter products by price range in any currency.
- **Ranking integration** - Optional exposure of currency rates for use in ranking expressions (ranking on the computed price).

The implementation consists of two key components:

- **MultiCurrencyFilterSearcher** - A custom searcher that intercepts queries and dynamically filters products based on effective prices.
- **CachedForexRateService** - A background service that stores exchange rates from the forex document in-memory for faster look-ups.

## Quick Start
This quick start walks through an end-to-end example of enabling multi-currency pricing in a Vespa application.
### Define Schemas

Create two schemas: one to store the forex rates, and one for products. If you already have an existing product schema, you can reuse it as long as it contains the required fields described below.

#### Forex Schema

The forex schema stores currency exchange rates as a tensor. Add a `forex.sd` schema to your application defined as:

```
```
schema forex {
    document forex {
        field timestamp type long {
            indexing: attribute | summary
        }

        field rates type tensor<double>(from{}, to{}) {
            indexing: attribute | summary
        }
    }
}
```
```

#### Product Schema

The product schema stores products with their seller currency and per-market prices. The `per_market_price` array contains price overrides for specific markets, with a `DEFAULT` market used as fallback. Every product must include a `DEFAULT` entry, and all `per_market_price.price` values are expressed in the document's `seller_currency`.

 **Note:** Every per-market override is stored in the seller's native currency, so the searcher can convert buyer price windows instead of rewriting stored prices.

```
```
schema product {
    document product {

        # Your existing fields above

        field seller_currency type string {
            indexing: summary | attribute
        }

        struct market_price {
            field market type string {}
            field price type double {}
        }

        field per_market_price type array<market_price> {
            indexing: summary
            summary: matched-elements-only
            struct-field market {
                indexing: attribute
            }
            struct-field price {
                indexing: attribute
            }
        }

        # Your existing fields below

    }
}
```
```

### Configure Services

Vespa only applies multi-currency filtering when the searcher and forex cache are wired into the container cluster. Queries must pass through a chain that includes `MultiCurrencyFilterSearcher`, and the `ForexRateRetriever` must read the global forex document via its own search chain. Add both chains and the two components to your container definition in `services.xml`:

Inside your existing `<container>` block, add the multi-currency chains and components:

```
```
<search>
    <chain id="multi-currency-filter" inherits="vespa">
        <searcher id="ai.vespa.ecommerce.multicurrency.MultiCurrencyFilterSearcher"
                  bundle="ecommerce-multi-currency" />
    </chain>
    <chain id="forex-cache" inherits="vespa" />
</search>

<component id="ai.vespa.ecommerce.multicurrency.ForexRateService"
           class="ai.vespa.ecommerce.multicurrency.CachedForexRateService"
           bundle="ecommerce-multi-currency" />

<component id="ai.vespa.ecommerce.multicurrency.ForexRateRetriever"
           bundle="ecommerce-multi-currency" />
```
```

In the `<content>` cluster ensure both document types are declared:

```
```
<documents>
    <document type="forex" mode="index" global="true" />
    <document type="product" mode="index" />
</documents>
```
```

The retriever issues background queries through the `forex-cache` chain. If that chain is missing or restricts the wrong document type, the cache never reaches `READY` and queries fail with “ensure exactly one forex document exists”.

Putting it all together, a minimal `services.xml` might look like this:

```
```
<services version="1.0">
  <container id="default" version="1.0">
    <document-api/>
    <search>
      <chain id="multi-currency-filter" inherits="vespa">
        <searcher id="ai.vespa.ecommerce.multicurrency.MultiCurrencyFilterSearcher"
                  bundle="ecommerce-multi-currency" />
      </chain>
      <chain id="forex-cache" inherits="vespa" />
    </search>
    <component id="ai.vespa.ecommerce.multicurrency.ForexRateService"
               class="ai.vespa.ecommerce.multicurrency.CachedForexRateService"
               bundle="ecommerce-multi-currency" />
    <component id="ai.vespa.ecommerce.multicurrency.ForexRateRetriever"
               bundle="ecommerce-multi-currency" />
  </container>

  <content id="content" version="1.0">
    <documents>
      <document type="forex" mode="index" global="true" />
      <document type="product" mode="index" />
    </documents>
    <nodes count="2" />
  </content>
</services>
```
```

### Feed Data

#### Feed Forex Rates

Feed a single forex document with ID `id:forex:forex::forex` containing all currency-to-currency exchange rates. Include identity rates (e.g., USD→USD = 1.0) to avoid missing-cell lookups. The `timestamp` field is required and must be updated with each rate change to ensure the cache picks up new rates.

 **Warning:** Exactly one global forex document must exist. If multiple documents are present, the retriever reports `INVALID_FOREX_DOCUMENTS` and the searcher returns error hits instructing you to keep a single forex document.

```
```
{
  "put": "id:forex:forex::forex",
  "fields": {
    "timestamp": 1757385600,
    "rates": {
      "cells": [
        {"address": {"from": "USD", "to": "USD"}, "value": 1.0},
        {"address": {"from": "USD", "to": "EUR"}, "value": 0.92},
        {"address": {"from": "USD", "to": "GBP"}, "value": 0.78},
        {"address": {"from": "USD", "to": "NOK"}, "value": 10.50},
        {"address": {"from": "EUR", "to": "USD"}, "value": 1.09},
        {"address": {"from": "EUR", "to": "EUR"}, "value": 1.0},
        {"address": {"from": "EUR", "to": "GBP"}, "value": 0.85}
      ]
    }
  }
}
```
```

#### Feed Products

Feed products with their seller currency and per-market prices. Always include a `DEFAULT` market entry as fallback.

```
```
{
  "put": "id:product:product::sku-100",
  "fields": {
    "seller_currency": "USD",
    "per_market_price": [
      {"market": "DEFAULT", "price": 199.0},
      {"market": "EU", "price": 189.0},
      {"market": "UK", "price": 209.0},
      {"market": "NO", "price": 300.0}
    ]
  }
}
```
```

 **Note:** If your product schema already includes identifiers or descriptive fields (such as `product_id` or `product_name`), include them in the feed as usual. The example keeps only the required currency fields so it works with the minimal schema shown above.

### Query with Price Filtering

Use the following query parameters to filter products by price range in a specific market and currency:

| Parameter | Description | Example |
| --- | --- | --- |
| `ecommerce.multicurrency.market` | Target market code | `NO`, `US`, `EU`, `NO-49`, `27` |
| `ecommerce.multicurrency.currency` | Target currency code | `NOK`, `USD`, `EUR` |
| `ecommerce.multicurrency.price-min` | Minimum price in target currency | `1000` |
| `ecommerce.multicurrency.price-max` | Maximum price in target currency | `1500` |
| `ecommerce.multicurrency.enrich` | Optional: expose forex rates as query tensor for ranking. Defaults to false | `true` or `false` |

#### Example Query

```
```
$ vespa query \
    'yql=select * from product where true' \
    'searchChain=multi-currency-filter' \
    'ecommerce.multicurrency.market=NO' \
    'ecommerce.multicurrency.currency=NOK' \
    'ecommerce.multicurrency.price-min=1000' \
    'ecommerce.multicurrency.price-max=1500'
```
```

This query returns all products whose effective price in NOK (Norwegian Krone) for the Norwegian market is between 1000 and 1500 NOK. The searcher will:

1. Check if the product has a market-specific price for `NO`
2. If yes, use that price directly
3. If no, convert the product's `DEFAULT` market price from the seller currency to NOK using forex rates
4. Keep only products within the specified price range

### Validation Rules

The multi-currency searcher validates query parameters and returns an error if validation fails:

- **Currency codes** must be exactly 3 letters (ISO-4217 format, e.g., `USD`, `EUR`, `NOK`)
- **Market codes** must be alphanumeric (e.g., `US`, `NO`, `EU`, `NO-47`, `13`)
- **Price values** must be valid numbers and non-negative
- **Price range**: `price-max` must be greater than or equal to `price-min`
- **Currency availability**: The requested currency must exist in the forex document

If any parameter is missing or invalid, the searcher will either skip filtering (for format issues) or return an error result (for logical issues like invalid price ranges or unknown currencies).

 **Note:** When filtering is skipped due to malformed inputs, the searcher acts as a no-op and the trace log records the reason (for example, “currency failed ISO-4217 validation; skipping filter”). Use [query tracing](/en/reference/api/query.html#tracing) to confirm whether the multi-currency filter actually ran.

### Updating Forex Rates

Forex rates can be updated at any time by feeding a new version of the forex document with an updated `timestamp` field. The cache will automatically pick up the new rates on its next refresh cycle (typically within seconds).

```
```
$ vespa feed <(echo '{
    "update": "id:forex:forex::forex",
    "fields": {
        "timestamp": {"assign": 1757472000},
        "rates": {
            "assign": {
                "cells": [...]
            }
        }
    }
}')
```
```

## How It Works

### Price Resolution Logic

For each product, the effective price in the target currency is determined as follows:

1. **Market-specific price:** If the product has a price entry for the requested market, use that price directly
2. **Currency conversion:** Otherwise, use the `DEFAULT` market price and convert it from the seller currency to the target currency using forex rates
3. **Price range filter:** Keep only products whose effective price falls within the specified min/max range

### Forex Cache

The `CachedForexRateService` component maintains an in-memory cache of exchange rates and refreshes them periodically from the forex document (`id:forex:forex::forex`). This ensures low-latency access to forex rates during query processing.

#### Automatic Refresh

The `ForexRateRetriever` component automatically refreshes forex rates every 10 seconds using a fixed schedule. This cadence (10s interval, 5s retry window, 1s per attempt) is hard-coded in the provided component and cannot be tuned at deployment time. Each refresh cycle:

- Queries the forex document using the `forex-cache` search chain
- Validates the document has both `rates` (tensor) and `timestamp` (long) fields
- Only applies updates if the timestamp is newer than the cached version
- Retries within a 5-second budget if the first attempt fails

#### Health States

The forex service tracks its operational status with the following health states:

| State | Description | Query Behavior |
| --- | --- | --- |
| `READY` | Forex rates loaded and service is operational | Queries with multi-currency filtering work normally |
| `UNINITIALIZED` | No forex document has been loaded yet | Queries return error: "forex rate service not initialized" |
| `OUTAGE` | Refresh failed but stale data exists (cache stays ready for re-use once the retriever succeeds again) | Queries return error: "forex rate service temporarily unavailable (last refresh failed)" |
| `INVALID_FOREX_DOCUMENTS` | Multiple forex documents detected (expected exactly one) | Queries return error: "ensure exactly one forex document exists" |

#### Error Handling

When the service is not in `READY` state, queries with multi-currency filtering will:

- Return an empty result with an appropriate error message
- Log detailed diagnostic information at appropriate trace levels
- Continue retrying background refresh attempts until successful

### Performance

Multi-currency price filtering is implemented as efficient query-time filter construction, not result-time evaluation. This means Vespa can use its indexes to find matching products without iterating through all documents.

#### How Filtering Works

When a query with multi-currency parameters is received, the searcher:

1. **Pre-computes price ranges:** Converts the buyer's price range (e.g., 1000-1500 NOK) into equivalent ranges for every seller currency using cached forex rates. For example, if the forex cache has USD, EUR, and GBP, it computes what 1000-1500 NOK equals in each currency.
2. **Builds structured query filters:** Creates a query tree using Vespa's efficient query primitives: 
  - `SameElementItem` - Matches documents where market and price appear in the same array element
  - `RangeItem` - Efficiently filters on numeric price ranges using indexes
  - `WordItem` - Matches exact seller currency and market values

3. **Injects filter into query tree:** Combines the price filter with the user's query, allowing Vespa's query execution engine to evaluate it efficiently using indexes.

This approach has several performance benefits:

- **No document iteration:** Vespa uses attribute indexes to quickly identify matching documents without fetching and evaluating all products
- **One-time conversion:** Currency conversion happens once during query construction, not for every product in the result set
- **Index-backed filtering:** Price range and market matching leverage Vespa's fast attribute lookups
- **Query optimization:** Vespa's query optimizer can reorder and optimize the combined query tree for efficient execution

## Advanced Usage

### Custom Field Configuration

By default, the multi-currency components expect specific field names in your product schema. You can customize these field names using the `product-schema-wiring` configuration.

```
```
<container id="default" version="1.0">
    <search>
        <chain id="multi-currency-filter" inherits="vespa">
            <searcher id="ai.vespa.ecommerce.multicurrency.MultiCurrencyFilterSearcher"
                      bundle="ecommerce-multi-currency">
                <config name="ai.vespa.ecommerce.multicurrency.product-schema-wiring">
                    <productFields>
                        <sellerCurrency>seller_currency</sellerCurrency>
                        <perMarketPriceArrayStruct>per_market_price</perMarketPriceArrayStruct>
                        <marketStructField>market</marketStructField>
                        <priceStructField>price</priceStructField>
                    </productFields>
                    <defaults>
                        <market>DEFAULT</market>
                    </defaults>
                    <rankProfileInputs>
                        <forexRates>forexRates</forexRates>
                    </rankProfileInputs>
                </config>
            </searcher>
        </chain>
    </search>
</container>
```
```

Configuration parameters:

- `productFields.sellerCurrency` - Field name for the product's seller currency (default: `seller_currency`)
- `productFields.perMarketPriceArrayStruct` - Array field name containing per-market prices (default: `per_market_price`)
- `productFields.marketStructField` - Struct field name for market code (default: `market`)
- `productFields.priceStructField` - Struct field name for price value (default: `price`)
- `defaults.market` - Default market identifier used as fallback (default: `DEFAULT`)
- `rankProfileInputs.forexRates` - Query tensor name for forex rates in ranking (default: `forexRates`)

### Using Forex Rates in Ranking

When `ecommerce.multicurrency.enrich=true` is set, the searcher exposes the forex rates as a query tensor `query(forexRates)` that can be used in ranking expressions. The ranking profile should implement the same fallback logic as the searcher: check for market-specific prices first, then fall back to the `DEFAULT` market price, and convert to the buyer's currency.

```
```
rank-profile price_ranking {
    inputs {
        query(forexRates) tensor<double>(from{}, to{})
        query(buyer_currency) tensor<double>(to{})
        query(buyer_market) tensor<double>(market{})
    }

    function from_selector() {
        expression: tensorFromLabels(attribute(seller_currency), from)
    }

    function buyer_rate() {
        expression: sum(query(forexRates) * from_selector() * query(buyer_currency), from, to)
    }

    function price_tensor() {
        expression: tensorFromStructs(attribute(per_market_price), market, price, double)
    }

    function market_specific_price() {
        expression: sum(price_tensor() * query(buyer_market), market)
    }

    function default_price() {
        expression: price_tensor(){market:'DEFAULT'}
    }

    function effective_price_in_seller_currency() {
        expression: if(market_specific_price() > 0, market_specific_price(), default_price())
    }

    function effective_price_in_buyer_currency() {
        expression: effective_price_in_seller_currency() * buyer_rate()
    }

    first-phase {
        expression: -effective_price_in_buyer_currency()
    }
}
```
```

This rank profile requires passing one-hot encoded tensors for the buyer's currency and market as query parameters:

```
```
$ vespa query \
    'yql=select * from product where true' \
    'searchChain=multi-currency-filter' \
    'ecommerce.multicurrency.enrich=true' \
    'ranking.features.query(buyer_currency)={{to:NOK}:1}' \
    'ranking.features.query(buyer_market)={{market:NO}:1}'
```
```

Key functions:

- `tensorFromStructs` - Converts the `per_market_price` array to a tensor at ranking time
- `market_specific_price()` - Extracts price for the requested market if it exists
- `default_price()` - Gets the `DEFAULT` market price as fallback
- `effective_price_in_seller_currency()` - Selects market-specific price or falls back to `DEFAULT`
- `effective_price_in_buyer_currency()` - Converts the effective price using forex rates

## Requirements

- **Single global forex document:** Maintain one document with ID `id:forex:forex::forex` and mark it `global="true"`. Additional documents trigger the `INVALID_FOREX_DOCUMENTS` health state and queries fail. 
- **Forex payload completeness:** Every feed/update must include the `rates` tensor for all buyer/seller pairs you filter on, identity rates (USD→USD, etc.), and a monotonically increasing `timestamp` (epoch seconds). 
- **Product schema layout:** Products expose `seller_currency`, encode all `per_market_price.price` values in that seller currency, and include a `DEFAULT` market entry. 
- **Container wiring:** Deploy the `multi-currency-filter` search chain and the `forex-cache` chain in your container cluster, along with the `ForexRateService` and `ForexRateRetriever` components. 
- **Query parameters:** Multi-currency filtering only runs when the query supplies `market`, `currency`, `price-min`, and `price-max`. Missing or malformed parameters cause the searcher to skip filtering. 

## Recommended Practices

- **Structure product ids/names as needed:** Keep your existing product fields (IDs, names, facets) and add the required currency fields alongside them. 
- **Model asymmetric rates:** Store both A→B and B→A conversions explicitly so buyer→seller lookups stay accurate even when FX rates are not perfect inverses. 
- **Plan update cadence:** Choose how often you feed forex data based on market volatility. The retriever polls every 10 seconds, so frequent feeds are reflected quickly. 
- **Default chain selection:** Either set `searchChain=multi-currency-filter` on relevant queries or make it the default chain so multi-currency filtering is always applied when parameters are present. 

## See Also

- [E-commerce tutorial](../../learn/tutorials/e-commerce)
- [Searcher Development](../../applications/searchers.html)
- [Tensor Guide](../../ranking/tensor-user-guide.html)
- [tensorFromStructs - Convert struct arrays to tensors](../../reference/ranking/rank-features.html#tensorFromStructs(attribute,key,value,type))
- [Struct Fields in Schemas](../../reference/schemas/schemas.html#struct-field)
- [Search Chains](../../applications/searchers.html#search-chains)

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Define Schemas](#define-schemas)
- [Configure Services](#configure-services)
- [Feed Data](#feed-data)
- [Query with Price Filtering](#query-with-price-filtering)
- [Validation Rules](#validation-rules)
- [Updating Forex Rates](#updating-forex-rates)
- [How It Works](#how-it-works)
- [Price Resolution Logic](#price-resolution-logic)
- [Forex Cache](#forex-cache)
- [Performance](#performance)
- [Advanced Usage](#advanced-usage)
- [Custom Field Configuration](#custom-field-configuration)
- [Using Forex Rates in Ranking](#using-forex-in-ranking)
- [Requirements](#requirements)
- [Recommended Practices](#recommended-practices)
- [See Also](#see-also)

