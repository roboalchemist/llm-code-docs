# Authentication

The Element14 Product Search API supports two authentication models depending on your pricing tier and requirements.

## Standard Authentication

Standard tier uses a simple API key-based authentication:

### API Key Format
- 24-character alphanumeric string
- Provided by Element14 Partner Portal
- Included in every API request

### How to Obtain

1. Create an account at https://partner.element14.com/
2. Log in to your account dashboard
3. Navigate to API settings or credentials section
4. Generate or retrieve your 24-character API key
5. Store securely (treat like a password)

### Usage in Requests

Include the API key in the `callInfo.apiKey` parameter:

```
https://api.element14.com/catalog/products?callInfo.apiKey=YOUR_24_CHAR_KEY&...
```

## Contract Pricing Authentication

Contract pricing provides negotiated bulk pricing but requires additional authentication mechanisms.

### Required Parameters

Beyond the standard API key, contract pricing requires:

- `userInfo.signature` - HMAC-SHA1 signature of the request
- `userInfo.timestamp` - ISO 8601 formatted timestamp
- `userInfo.customerId` - Your contract customer ID

### Signature Generation

The signature is an HMAC-SHA1 hash of the operation name and timestamp:

**Steps:**
1. Format timestamp in ISO 8601 format (e.g., `2024-01-08T14:30:00Z`)
2. Concatenate operation name with timestamp (e.g., `searchAPI2024-01-08T14:30:00Z`)
3. Generate HMAC-SHA1 hash using your contract API key as the secret
4. URL-encode the resulting signature
5. Include in `userInfo.signature` parameter

**PHP Example:**
```php
$timestamp = date('c');  // ISO 8601 format
$operation = 'searchAPI';
$message = $operation . $timestamp;
$signature = hash_hmac('sha1', $message, $apiKey, false);
$signatureUrlEncoded = rawurlencode($signature);
```

**Python Example:**
```python
import hmac
import hashlib
from datetime import datetime
from urllib.parse import quote

timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
operation = 'searchAPI'
message = f'{operation}{timestamp}'

signature = hmac.new(
    api_key.encode(),
    message.encode(),
    hashlib.sha1
).hexdigest()

signature_encoded = quote(signature, safe='')
```

### Contract Pricing Request Example

```
GET https://api.element14.com/catalog/products
  ?term=any:capacitor
  &storeInfo.id=40
  &callInfo.apiKey=YOUR_24_CHAR_KEY
  &userInfo.signature=HMAC_SIGNATURE
  &userInfo.timestamp=2024-01-08T14:30:00Z
  &userInfo.customerId=YOUR_CONTRACT_ID
  &callInfo.responseDataFormat=json
```

## Security Considerations

- Treat API keys as secrets - never commit to version control
- Use HTTPS for all requests (mandatory)
- Regenerate API keys periodically
- Use environment variables or secure credential stores
- For server-side integrations, restrict API key usage by IP if possible
- Contract pricing signatures include timestamps to prevent replay attacks

## Rate Limiting

The documentation does not publicly specify rate limits. Contact Element14 support for:
- Rate limits on standard tier
- Rate limits on contract tier
- Burst capacity and throttling parameters
- Dedicated endpoint availability for high-volume usage
