# Regional Store Configuration

The Element14 Product Search API supports product searches across 40+ regional stores and pricing configurations. Each region uses a unique store ID and may have different product availability, pricing, and currency.

## Store IDs Reference

### Asia-Pacific Region

| Region | Store ID | Platform | Currency |
|--------|----------|----------|----------|
| Japan | 40 | Element14 | JPY |
| Australia | 45 | Element14 | AUD |
| Singapore | 46 | Element14 | SGD |
| Malaysia | 47 | Element14 | MYR |
| China | 53 | Element14 | CNY |
| Hong Kong | 54 | Element14 | HKD |
| Taiwan | 55 | Element14 | TWD |
| Korea | 56 | Element14 | KRW |
| India | 57 | Element14 | INR |
| New Zealand | 59 | Element14 | NZD |

### Europe Region

| Region | Store ID | Platform | Currency |
|--------|----------|----------|----------|
| UK/Europe | 44 | Farnell | GBP/EUR |
| Germany | 48 | Farnell | EUR |
| Netherlands | 49 | Farnell | EUR |
| France | 50 | Farnell | EUR |
| Spain | 51 | Farnell | EUR |
| Italy | 52 | Farnell | EUR |
| Poland | 70 | Farnell | PLN |
| Austria | 75 | Farnell | EUR |
| Belgium | 76 | Farnell | EUR |
| Czech Republic | 77 | Farnell | CZK |
| Hungary | 78 | Element14 | HUF |
| Portugal | 79 | Farnell | EUR |
| Romania | 81 | Farnell | RON |
| Ireland | 84 | Farnell | EUR |
| Greece | 85 | Farnell | EUR |
| Bulgaria | 92 | Element14 | BGN |
| Denmark | 89 | Farnell | DKK |
| Sweden | 91 | Farnell | SEK |
| Finland | 94 | Farnell | EUR |

### Americas Region

| Region | Store ID | Platform | Currency |
|--------|----------|----------|----------|
| USA | 43 | Newark | USD |
| Mexico | 74 | Element14 | MXN |
| Brazil | 72 | Element14 | BRL |

### Middle East & Africa

| Region | Store ID | Platform | Currency |
|--------|----------|----------|----------|
| Israel | 80 | Element14 | ILS |
| Saudi Arabia | 82 | Element14 | SAR |
| Pakistan | 83 | Element14 | PKR |
| Turkey | 97 | Element14 | TRY |
| Russia/CIS | 88 | Element14 | RUB |
| UK (alternate) | 41 | Farnell | GBP |

## Regional Differences

### Product Availability
- Product catalogs vary by region
- Some items may be region-restricted due to export controls
- Availability subject to local supply chains
- Check local regulations for sensitive components

### Pricing and Currencies
- Pricing is region-specific
- Currency automatically returned in response
- Exchange rates are not fixed - prices update regularly
- Contract pricing may have regional variations

### Inventory
- Stock levels are region-specific
- Warehouses are distributed by region
- Lead times and shipping may vary
- Availability can differ significantly between regions

### Language Support
- Element14 sites typically support English
- Farnell sites may support regional languages
- Documentation mostly in English
- Customer support available in regional languages

## Selecting Regional Stores

### For Global Applications

```python
# Map end-user location to store ID
STORE_MAPPING = {
    'US': 43,
    'UK': 41,
    'DE': 48,
    'FR': 50,
    'JP': 40,
    'CN': 53,
    'AU': 45,
    'CA': 43,  # Use US store
}

def search_by_location(search_term, location_code):
    store_id = STORE_MAPPING.get(location_code, 43)  # Default to US
    return search_products(search_term, store_id)
```

### For Multi-Region Searches

```python
def search_all_regions(search_term, target_regions=['US', 'UK', 'DE', 'JP']):
    """Search across multiple regions"""
    results_by_region = {}

    for region in target_regions:
        store_id = STORE_MAPPING[region]
        try:
            result = search_products(search_term, store_id)
            results_by_region[region] = result['response']['products']
        except Exception as e:
            print(f"Error searching {region}: {e}")
            results_by_region[region] = []

    return results_by_region

# Find best pricing across regions
all_results = search_all_regions('resistor 10k', ['US', 'UK', 'JP'])

for region, products in all_results.items():
    if products:
        best_price = min(p['unitPrice'] for p in products)
        print(f"{region}: ${best_price:.4f}")
```

## Platform-Specific Considerations

### Newark (USA)
- Store ID: 43
- Primary US distributor
- Strong inventory of common components
- Fast shipping within USA
- Best for North American projects

### Farnell (Europe & UK)
- Store IDs: 41, 44, 48-52, 70, 75-77, 79, 81, 84-85, 89, 91, 94
- Multiple European warehouses
- Regional pricing in local currencies
- Excellent for European supply chains
- Wide product range

### Element14 (Asia-Pacific & Global)
- Store IDs: 40, 45-47, 53-57, 59, 72, 74, 78, 80, 82-83, 88, 92, 97
- Global distribution network
- Growing inventory in emerging markets
- Regional expertise and support
- Bridge between East and West

## Cross-Regional Best Practices

### Finding Part Number Equivalents

The same part may have different part numbers across regions:

```python
def find_equivalent_parts(mfn, store_ids=[43, 41, 40]):
    """Find equivalent part numbers across regions"""
    equivalents = {}

    for store_id in store_ids:
        result = search_by_mfn(mfn, store_id)
        if result['response']['products']:
            product = result['response']['products'][0]
            equivalents[store_id] = product['partNumber']

    return equivalents

# Find equivalent part numbers
equivalents = find_equivalent_parts('IMXRT1060IEC')
# Result: {43: 'CF14JT10K0', 41: 'CF14JT10K0', 40: 'CF14JT10K0'}
```

### Comparing Pricing Across Regions

```python
def compare_regional_pricing(search_term, store_ids):
    """Compare pricing across multiple regions"""
    pricing = {}

    for store_id in store_ids:
        result = search_products(search_term, store_id=store_id)
        if result['response']['products']:
            product = result['response']['products'][0]
            pricing[store_id] = {
                'price': product['unitPrice'],
                'currency': product['currencyCode'],
                'stock': product['stockLevel']
            }

    return pricing

# Compare across major regions
regions = [43, 41, 40]  # US, UK, Japan
pricing = compare_regional_pricing('capacitor 10uF', regions)
for store_id, info in pricing.items():
    print(f"Store {store_id}: {info['price']} {info['currency']} (Stock: {info['stock']})")
```

### Inventory Tracking by Region

```python
def track_inventory_all_regions(mfn):
    """Track part inventory across all accessible regions"""
    inventory = {}
    major_stores = [43, 41, 40, 44, 48, 50, 53]

    for store_id in major_stores:
        result = search_by_mfn(mfn, store_id)
        if result['response']['products']:
            product = result['response']['products'][0]
            inventory[store_id] = product['stockLevel']

    return inventory

stock = track_inventory_all_regions('LM7805CT')
for store_id, qty in stock.items():
    print(f"Store {store_id}: {qty} units")
```

## Regional API Endpoint

All regions use the same API endpoint:
```
https://api.element14.com/catalog/products
```

The region is controlled by the `storeInfo.id` parameter, not by different endpoints.

## Rate Limiting by Region

Rate limits may vary by region and customer tier. Contact your regional distributor for:
- Regional rate limit policies
- Burst capacity specifications
- Dedicated endpoint availability
- Support for high-volume integrations
