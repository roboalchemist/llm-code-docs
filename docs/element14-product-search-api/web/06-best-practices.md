# Best Practices & Advanced Usage

## Performance Optimization

### Minimize Response Payload

Use the smallest appropriate `responseGroup` for your use case:

```python
# Bad: Always fetch everything
result = search_products('resistor', responseGroup='large')

# Good: Fetch only what you need
if just_checking_availability:
    responseGroup = 'small'  # Part number + description only
elif need_pricing:
    responseGroup = 'prices'  # Pricing tiers only
elif need_images:
    responseGroup = 'large'   # Full details with images
else:
    responseGroup = 'medium'  # Balanced (default)
```

### Use Pagination Efficiently

```python
def fetch_first_n_results(search_term, n=100):
    """Efficiently fetch exactly N results without fetching extra pages"""
    page_size = 50
    total_pages = (n + page_size - 1) // page_size

    all_products = []

    for page in range(1, total_pages + 1):
        result = search_products(
            search_term,
            pageSize=page_size,
            pageNumber=page
        )
        all_products.extend(result['response']['products'])

        if len(all_products) >= n:
            return all_products[:n]

    return all_products
```

### Cache Results

```python
import time
from functools import wraps

def cache_with_ttl(ttl_seconds=3600):
    """Cache API results for specified TTL"""
    cache = {}

    def decorator(func):
        def wrapper(*args, **kwargs):
            cache_key = (func.__name__, str(args), str(sorted(kwargs.items())))
            now = time.time()

            if cache_key in cache:
                result, timestamp = cache[cache_key]
                if now - timestamp < ttl_seconds:
                    return result

            result = func(*args, **kwargs)
            cache[cache_key] = (result, now)
            return result

        return wrapper
    return decorator

@cache_with_ttl(ttl_seconds=3600)  # Cache for 1 hour
def search_products_cached(search_term, store_id=43):
    return search_products(search_term, store_id)

# First call hits API
result1 = search_products_cached('resistor')

# Subsequent calls within 1 hour use cache
result2 = search_products_cached('resistor')  # Fast!
```

## Error Handling & Resilience

### Exponential Backoff Retry

```python
import time
import requests
from requests.exceptions import RequestException

def search_with_retry(search_term, max_retries=3):
    """Search with exponential backoff retry"""

    for attempt in range(max_retries):
        try:
            params = {
                'term': f'any:{search_term}',
                'storeInfo.id': 43,
                'callInfo.apiKey': API_KEY,
                'callInfo.responseDataFormat': 'json'
            }

            response = requests.get(BASE_URL, params=params, timeout=10)

            # Check HTTP status
            if response.status_code == 429:  # Rate limited
                wait_time = 2 ** attempt
                print(f"Rate limited. Waiting {wait_time}s...")
                time.sleep(wait_time)
                continue

            response.raise_for_status()

            # Check API status code
            data = response.json()
            if data['response']['statusCode'] != 200:
                if data['response']['statusCode'] == 500 and attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    print(f"Server error. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                else:
                    raise Exception(data['response']['statusMessage'])

            return data

        except RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                print(f"Request failed: {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise

    raise Exception("Max retries exceeded")
```

### Graceful Degradation

```python
def search_with_fallback(search_term, primary_store=43, fallback_store=41):
    """Try primary store, fall back to secondary if unavailable"""

    try:
        return search_products(search_term, store_id=primary_store)
    except Exception as e:
        print(f"Primary store failed: {e}")
        print(f"Falling back to store {fallback_store}")
        try:
            return search_products(search_term, store_id=fallback_store)
        except Exception as e:
            print(f"Both stores failed: {e}")
            return None
```

## Security Best Practices

### API Key Management

```python
import os
from dotenv import load_dotenv

# Load from environment variables
load_dotenv()
API_KEY = os.getenv('ELEMENT14_API_KEY')

if not API_KEY:
    raise ValueError("ELEMENT14_API_KEY environment variable not set")

# For contract pricing
CONTRACT_CUSTOMER_ID = os.getenv('ELEMENT14_CONTRACT_ID')
```

### Secure Signature Generation

```python
import hmac
import hashlib
from datetime import datetime
from urllib.parse import quote

def generate_contract_signature(api_key, operation='searchAPI'):
    """Generate HMAC-SHA1 signature for contract pricing"""

    # Use UTC timestamp
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Create message
    message = f'{operation}{timestamp}'.encode()
    secret = api_key.encode()

    # Generate signature
    signature = hmac.new(secret, message, hashlib.sha1).hexdigest()

    return {
        'timestamp': timestamp,
        'signature': quote(signature, safe=''),
        'message': f'{operation}{timestamp}'  # For verification
    }

# Use it
sig_data = generate_contract_signature(API_KEY)
print(f"Signature: {sig_data['signature']}")
print(f"Timestamp: {sig_data['timestamp']}")
```

### API Usage Monitoring

```python
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_api_usage(search_term, store_id, result):
    """Log API usage for monitoring and auditing"""

    num_results = result['response']['numFound']
    num_returned = len(result['response']['products'])

    logger.info(
        f"Search: term={search_term}, store={store_id}, "
        f"found={num_results}, returned={num_returned}, "
        f"timestamp={datetime.utcnow().isoformat()}"
    )

# Use in search function
result = search_products('resistor', 43)
log_api_usage('resistor', 43, result)
```

## Bulk Operations

### Batch Search Multiple Terms

```python
from concurrent.futures import ThreadPoolExecutor
import requests

def batch_search(search_terms, max_workers=5):
    """Search multiple terms concurrently"""

    results = {}

    def search_term(term):
        try:
            result = search_products(term)
            return term, result
        except Exception as e:
            return term, {'error': str(e)}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(search_term, term) for term in search_terms]

        for future in futures:
            term, result = future.result()
            results[term] = result

    return results

# Search multiple terms concurrently
terms = ['resistor', 'capacitor', 'microcontroller']
results = batch_search(terms)

for term, result in results.items():
    print(f"{term}: {result['response'].get('numFound', 'N/A')}")
```

### Build Component Library

```python
import json
from pathlib import Path

class ComponentLibrary:
    def __init__(self, storage_path='components.json'):
        self.storage_path = Path(storage_path)
        self.components = self._load()

    def _load(self):
        if self.storage_path.exists():
            with open(self.storage_path) as f:
                return json.load(f)
        return {}

    def add_component(self, search_term, store_id=43):
        """Search and add component to library"""
        result = search_products(search_term, store_id)

        if result['response']['products']:
            product = result['response']['products'][0]
            self.components[product['partNumber']] = {
                'description': product['description'],
                'manufacturer': product['manufacturer'],
                'price': product['unitPrice'],
                'currency': product['currencyCode'],
                'store': store_id
            }
            self._save()
            return product

        return None

    def _save(self):
        with open(self.storage_path, 'w') as f:
            json.dump(self.components, f, indent=2)

    def get_component(self, part_number):
        return self.components.get(part_number)

    def list_components(self):
        return list(self.components.keys())

# Usage
library = ComponentLibrary('my_components.json')
library.add_component('resistor 10k')
library.add_component('capacitor 10uF')

print(f"Library has {len(library.list_components())} components")
```

## Data Analysis

### Find Cheapest Components

```python
def find_cheapest(search_term, store_id=43, limit=5):
    """Find cheapest options for a search term"""
    result = search_products(search_term, store_id=store_id)

    products = result['response']['products']
    sorted_products = sorted(products, key=lambda p: p['unitPrice'])

    return sorted_products[:limit]

cheapest = find_cheapest('resistor 10k')
for product in cheapest:
    print(f"{product['partNumber']}: ${product['unitPrice']} ({product['manufacturer']})")
```

### Find High-Stock Items

```python
def find_high_stock(search_term, min_stock=1000):
    """Find items with sufficient stock"""
    result = search_products(search_term)

    high_stock = [
        p for p in result['response']['products']
        if p['stockLevel'] >= min_stock
    ]

    return sorted(high_stock, key=lambda p: p['stockLevel'], reverse=True)

items = find_high_stock('capacitor', min_stock=5000)
for product in items:
    print(f"{product['partNumber']}: {product['stockLevel']} units")
```

### Compare Manufacturers

```python
def analyze_manufacturers(search_term):
    """Analyze available manufacturers for a component type"""
    result = search_products(search_term)

    manufacturers = {}
    for product in result['response']['products']:
        mfg = product['manufacturer']
        if mfg not in manufacturers:
            manufacturers[mfg] = {
                'count': 0,
                'avg_price': 0,
                'products': []
            }

        manufacturers[mfg]['count'] += 1
        manufacturers[mfg]['avg_price'] += product['unitPrice']
        manufacturers[mfg]['products'].append(product['partNumber'])

    # Calculate averages
    for mfg in manufacturers:
        manufacturers[mfg]['avg_price'] /= manufacturers[mfg]['count']

    return manufacturers

analysis = analyze_manufacturers('resistor')
for mfg, stats in analysis.items():
    print(f"{mfg}: {stats['count']} products, avg ${stats['avg_price']:.4f}")
```

## Testing

### Unit Tests for API Integration

```python
import unittest
from unittest.mock import patch, MagicMock

class TestElement14API(unittest.TestCase):

    @patch('requests.get')
    def test_search_products_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'response': {
                'statusCode': 200,
                'numFound': 100,
                'products': [
                    {
                        'partNumber': 'TEST123',
                        'description': 'Test Product',
                        'unitPrice': 10.00
                    }
                ]
            }
        }
        mock_get.return_value = mock_response

        result = search_products('test')

        self.assertEqual(result['response']['statusCode'], 200)
        self.assertEqual(len(result['response']['products']), 1)

    @patch('requests.get')
    def test_api_error_handling(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'response': {
                'statusCode': 401,
                'statusMessage': 'Unauthorized'
            }
        }
        mock_get.return_value = mock_response

        result = search_products('test')

        self.assertEqual(result['response']['statusCode'], 401)

if __name__ == '__main__':
    unittest.main()
```
