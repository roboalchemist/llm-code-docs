# Code Examples

## Python Examples

### Basic Keyword Search

```python
import requests
import json

API_KEY = "YOUR_24_CHAR_KEY"
BASE_URL = "https://api.element14.com/catalog/products"

def search_products(search_term, store_id=43, page=1):
    """Search for products by keyword"""
    params = {
        'term': f'any:{search_term}',
        'storeInfo.id': store_id,
        'callInfo.apiKey': API_KEY,
        'callInfo.responseDataFormat': 'json',
        'resultsSettings.responseGroup': 'medium',
        'resultsSettings.pageNumber': page,
        'resultsSettings.pageSize': 20
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    return response.json()

# Search for resistors
result = search_products('resistor 10k')
print(f"Found {result['response']['numFound']} products")

for product in result['response']['products']:
    print(f"{product['partNumber']}: {product['description']}")
    print(f"  Price: ${product['unitPrice']}")
    print(f"  Stock: {product['stockLevel']}\n")
```

### Search by Manufacturer Part Number

```python
def search_by_mfn(mfn, store_id=43):
    """Search by manufacturer part number"""
    params = {
        'term': f'manuPartNum:{mfn}',
        'storeInfo.id': store_id,
        'callInfo.apiKey': API_KEY,
        'callInfo.responseDataFormat': 'json',
        'resultsSettings.responseGroup': 'large'
    }

    response = requests.get(BASE_URL, params=params)
    return response.json()

# Find by manufacturer part number
result = search_by_mfn('IMXRT1060IEC')
if result['response']['products']:
    product = result['response']['products'][0]
    print(f"Found: {product['description']}")
    print(f"Element14 Part: {product['partNumber']}")
    print(f"Images: {[img['url'] for img in product.get('images', [])]}")
```

### Search by Element14 Product ID

```python
def get_product_by_id(product_id, store_id=43):
    """Get product details by Element14 product ID"""
    params = {
        'term': f'id:{product_id}',
        'storeInfo.id': store_id,
        'callInfo.apiKey': API_KEY,
        'callInfo.responseDataFormat': 'json',
        'resultsSettings.responseGroup': 'large'
    }

    response = requests.get(BASE_URL, params=params)
    return response.json()

result = get_product_by_id('8947381')
product = result['response']['products'][0]
print(f"{product['description']}")
print(f"Manufacturer: {product['manufacturer']}")
print(f"Category: {product['category']}")
```

### Get Pricing Tiers

```python
def get_pricing_tiers(search_term, store_id=43):
    """Get tiered pricing information"""
    params = {
        'term': f'any:{search_term}',
        'storeInfo.id': store_id,
        'callInfo.apiKey': API_KEY,
        'callInfo.responseDataFormat': 'json',
        'resultsSettings.responseGroup': 'prices'
    }

    response = requests.get(BASE_URL, params=params)
    return response.json()

result = get_pricing_tiers('capacitor 10uF')
for product in result['response']['products'][:1]:
    print(f"{product['partNumber']}:")
    for tier in product.get('pricingTiers', []):
        print(f"  {tier['minQty']:>6} units: ${tier['price']}")
```

### Contract Pricing with Signature

```python
import hmac
import hashlib
from datetime import datetime
from urllib.parse import quote

def search_with_contract_pricing(search_term, contract_id, store_id=43):
    """Search with contract pricing authentication"""

    # Generate timestamp and signature
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    operation = 'searchAPI'
    message = f'{operation}{timestamp}'

    signature = hmac.new(
        API_KEY.encode(),
        message.encode(),
        hashlib.sha1
    ).hexdigest()

    signature_encoded = quote(signature, safe='')

    params = {
        'term': f'any:{search_term}',
        'storeInfo.id': store_id,
        'callInfo.apiKey': API_KEY,
        'userInfo.signature': signature_encoded,
        'userInfo.timestamp': timestamp,
        'userInfo.customerId': contract_id,
        'callInfo.responseDataFormat': 'json',
        'resultsSettings.responseGroup': 'medium'
    }

    response = requests.get(BASE_URL, params=params)
    return response.json()

# Use contract pricing
result = search_with_contract_pricing('resistor', contract_id='CUST12345')
print(result)
```

### Paginate Through All Results

```python
def search_all_pages(search_term, store_id=43):
    """Retrieve all results with pagination"""
    page = 1
    all_products = []

    while True:
        params = {
            'term': f'any:{search_term}',
            'storeInfo.id': store_id,
            'callInfo.apiKey': API_KEY,
            'callInfo.responseDataFormat': 'json',
            'resultsSettings.responseGroup': 'medium',
            'resultsSettings.pageNumber': page,
            'resultsSettings.pageSize': 50
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        all_products.extend(data['response']['products'])

        if page >= data['response']['totalPages']:
            break

        page += 1

    return all_products

products = search_all_pages('microcontroller STM32')
print(f"Retrieved {len(products)} total products")
```

## JavaScript/Node.js Examples

### Basic Fetch Request

```javascript
const API_KEY = "YOUR_24_CHAR_KEY";
const BASE_URL = "https://api.element14.com/catalog/products";

async function searchProducts(searchTerm, storeId = 43) {
  const params = new URLSearchParams({
    'term': `any:${searchTerm}`,
    'storeInfo.id': storeId,
    'callInfo.apiKey': API_KEY,
    'callInfo.responseDataFormat': 'json',
    'resultsSettings.responseGroup': 'medium',
    'resultsSettings.pageSize': 20
  });

  const response = await fetch(`${BASE_URL}?${params}`);
  const data = await response.json();

  return data;
}

// Usage
searchProducts('capacitor 10uF').then(result => {
  console.log(`Found ${result.response.numFound} products`);

  result.response.products.forEach(product => {
    console.log(`${product.partNumber}: ${product.description}`);
    console.log(`  $${product.unitPrice} (Stock: ${product.stockLevel})`);
  });
});
```

### Get Specific Product

```javascript
async function getProductById(productId, storeId = 43) {
  const params = new URLSearchParams({
    'term': `id:${productId}`,
    'storeInfo.id': storeId,
    'callInfo.apiKey': API_KEY,
    'callInfo.responseDataFormat': 'json',
    'resultsSettings.responseGroup': 'large'
  });

  const response = await fetch(`${BASE_URL}?${params}`);
  const data = await response.json();

  return data.response.products[0] || null;
}

// Get product 8947381
const product = await getProductById('8947381');
console.log(product.description);
console.log(product.manufacturer);
```

### With Error Handling

```javascript
async function searchWithErrorHandling(searchTerm) {
  try {
    const params = new URLSearchParams({
      'term': `any:${searchTerm}`,
      'storeInfo.id': 43,
      'callInfo.apiKey': API_KEY,
      'callInfo.responseDataFormat': 'json'
    });

    const response = await fetch(`${BASE_URL}?${params}`);

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    const data = await response.json();

    if (data.response.statusCode !== 200) {
      throw new Error(data.response.statusMessage);
    }

    return data.response.products;

  } catch (error) {
    console.error('Search failed:', error.message);
    return [];
  }
}
```

## cURL Examples

### Simple Keyword Search

```bash
curl "https://api.element14.com/catalog/products?term=any:resistor&storeInfo.id=43&callInfo.apiKey=YOUR_24_CHAR_KEY&callInfo.responseDataFormat=json" | jq
```

### Search by Manufacturer Part Number

```bash
curl -G "https://api.element14.com/catalog/products" \
  --data-urlencode "term=manuPartNum:LM7805CT" \
  --data-urlencode "storeInfo.id=41" \
  --data-urlencode "callInfo.apiKey=YOUR_24_CHAR_KEY" \
  --data-urlencode "callInfo.responseDataFormat=json" | jq
```

### Get Product by ID with Large Response Group

```bash
curl -G "https://api.element14.com/catalog/products" \
  --data-urlencode "term=id:4298467" \
  --data-urlencode "storeInfo.id=45" \
  --data-urlencode "callInfo.apiKey=YOUR_24_CHAR_KEY" \
  --data-urlencode "callInfo.responseDataFormat=json" \
  --data-urlencode "resultsSettings.responseGroup=large" | jq '.response.products[0]'
```

### Paginated Search

```bash
for page in {1..5}; do
  echo "=== Page $page ==="
  curl -G "https://api.element14.com/catalog/products" \
    --data-urlencode "term=any:capacitor" \
    --data-urlencode "storeInfo.id=43" \
    --data-urlencode "callInfo.apiKey=YOUR_24_CHAR_KEY" \
    --data-urlencode "callInfo.responseDataFormat=json" \
    --data-urlencode "resultsSettings.pageNumber=$page" \
    --data-urlencode "resultsSettings.pageSize=10" | jq '.response.products[] | {partNumber, description, unitPrice}'
done
```

## PyFarnell Library (Unofficial)

An unofficial Python wrapper simplifies access to the Farnell variant:

```python
from pyfarnell import FarnellAPI

# Initialize with your API key
api = FarnellAPI(api_key='YOUR_24_CHAR_KEY', region='uk')

# Get part by Farnell part number
part = api.get_part_by_number('9876543')

print(f"Part: {part['partNumber']}")
print(f"Description: {part['description']}")
print(f"Price: {part['unitPrice']}")
print(f"Stock: {part['stockLevel']}")
```

Note: PyFarnell is unofficial and not maintained by Farnell/Element14. Check the GitHub repository for current status and regional support.

## Best Practices

### Rate Limiting
- Implement exponential backoff for retries
- Space requests to avoid hitting rate limits
- Cache results when possible
- Batch multiple searches efficiently

### Error Handling
- Check HTTP status codes
- Validate `statusCode` in response body
- Handle rate limit (429) responses gracefully
- Log failed requests for debugging

### Performance
- Use appropriate `responseGroup` to minimize payload
- Implement pagination for large result sets
- Filter by store ID before making requests
- Consider caching frequently searched terms

### Security
- Never hardcode API keys in source code
- Use environment variables for credentials
- Implement API key rotation policies
- Monitor for unusual API usage patterns
