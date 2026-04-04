# LCSC API Authentication Guide

Complete guide to LCSC API authentication with signature generation and implementation examples.

## Overview

LCSC API uses OAuth-like request signing with SHA-1 HMAC. All requests require:
1. API key (from account)
2. API secret (from account)
3. Unique nonce per request
4. Current Unix timestamp
5. SHA-1 signature of combined parameters

## Getting Started

### 1. Register Account

Visit https://lcsc.com and create an account:
- Personal accounts cannot use the API
- Create a **business or agent account**
- Verify email address
- Complete profile information

### 2. Apply for API Access

Go to https://lcsc.com/agent and:
1. Click "API Access" or "Developer Program"
2. Submit application form with:
   - Company name
   - Use case (inventory system, procurement tool, etc.)
   - Expected request volume
   - Data handling practices
3. Submit to support@lcsc.com if form unavailable

### 3. Receive Credentials

LCSC will email you:
- API Key (user ID)
- API Secret (authentication token)
- API documentation link
- Rate limit information

**Important:** Store credentials securely. Never commit to version control.

## Signature Generation

### Formula

```
signature = SHA1("key={key}&nonce={nonce}&secret={secret}&timestamp={timestamp}")
```

This is the exact order. No modifications.

### Step-by-Step

1. **Get timestamp:**
   ```
   timestamp = current_unix_timestamp()
   ```

2. **Generate nonce:**
   - 16 random characters
   - Alphanumeric (a-z, A-Z, 0-9)
   - Different for each request
   ```
   nonce = random_string(16)  # Example: "aBc123DeF456gHiJ"
   ```

3. **Build signature string:**
   ```
   signature_string = f"key={api_key}&nonce={nonce}&secret={api_secret}&timestamp={timestamp}"
   ```
   Example:
   ```
   key=user123&nonce=aBc123DeF456gHiJ&secret=mysecret456&timestamp=1704700800
   ```

4. **Hash with SHA-1:**
   ```
   signature = SHA1(signature_string)
   ```
   Result: 40-character hex string

5. **Add to request:**
   ```
   GET /rest/wmsc2agent/search/product
   ?key=user123
   &timestamp=1704700800
   &nonce=aBc123DeF456gHiJ
   &signature=<40-char-hex-hash>
   &keyword=TL072CP
   ```

## Implementation Examples

### Python

```python
import hashlib
import time
import random
import string

def generate_nonce(length=16):
    """Generate random nonce"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_signature(api_key, api_secret, timestamp, nonce):
    """Generate SHA-1 signature"""
    # Exact order: key, nonce, secret, timestamp
    signature_string = f"key={api_key}&nonce={nonce}&secret={api_secret}&timestamp={timestamp}"
    return hashlib.sha1(signature_string.encode()).hexdigest()

def get_auth_params(api_key, api_secret):
    """Get all authentication parameters for request"""
    timestamp = int(time.time())
    nonce = generate_nonce()
    signature = generate_signature(api_key, api_secret, timestamp, nonce)

    return {
        'key': api_key,
        'timestamp': timestamp,
        'nonce': nonce,
        'signature': signature
    }

# Usage
api_key = 'your_api_key'
api_secret = 'your_api_secret'

auth = get_auth_params(api_key, api_secret)
print(f"key={auth['key']}&timestamp={auth['timestamp']}&nonce={auth['nonce']}&signature={auth['signature']}")
```

### JavaScript/Node.js

```javascript
const crypto = require('crypto');

function generateNonce(length = 16) {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let nonce = '';
  for (let i = 0; i < length; i++) {
    nonce += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return nonce;
}

function generateSignature(apiKey, apiSecret, timestamp, nonce) {
  // Exact order: key, nonce, secret, timestamp
  const signatureString = `key=${apiKey}&nonce=${nonce}&secret=${apiSecret}&timestamp=${timestamp}`;
  return crypto.createHash('sha1').update(signatureString).digest('hex');
}

function getAuthParams(apiKey, apiSecret) {
  const timestamp = Math.floor(Date.now() / 1000);
  const nonce = generateNonce();
  const signature = generateSignature(apiKey, apiSecret, timestamp, nonce);

  return {
    key: apiKey,
    timestamp: timestamp,
    nonce: nonce,
    signature: signature
  };
}

// Usage
const apiKey = 'your_api_key';
const apiSecret = 'your_api_secret';

const auth = getAuthParams(apiKey, apiSecret);
const queryString = `key=${auth.key}&timestamp=${auth.timestamp}&nonce=${auth.nonce}&signature=${auth.signature}`;
console.log(queryString);
```

### PHP

```php
<?php

function generateNonce($length = 16) {
    $chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    $nonce = '';
    for ($i = 0; $i < $length; $i++) {
        $nonce .= $chars[rand(0, strlen($chars) - 1)];
    }
    return $nonce;
}

function generateSignature($apiKey, $apiSecret, $timestamp, $nonce) {
    // Exact order: key, nonce, secret, timestamp
    $signatureString = "key={$apiKey}&nonce={$nonce}&secret={$apiSecret}&timestamp={$timestamp}";
    return sha1($signatureString);
}

function getAuthParams($apiKey, $apiSecret) {
    $timestamp = time();
    $nonce = generateNonce();
    $signature = generateSignature($apiKey, $apiSecret, $timestamp, $nonce);

    return [
        'key' => $apiKey,
        'timestamp' => $timestamp,
        'nonce' => $nonce,
        'signature' => $signature
    ];
}

// Usage
$apiKey = 'your_api_key';
$apiSecret = 'your_api_secret';

$auth = getAuthParams($apiKey, $apiSecret);
$queryString = http_build_query($auth);
echo $queryString;
?>
```

### Go

```go
package main

import (
    "crypto/sha1"
    "fmt"
    "math/rand"
    "time"
)

func generateNonce(length int) string {
    chars := "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    result := make([]byte, length)
    for i := 0; i < length; i++ {
        result[i] = chars[rand.Intn(len(chars))]
    }
    return string(result)
}

func generateSignature(apiKey, apiSecret string, timestamp int64, nonce string) string {
    // Exact order: key, nonce, secret, timestamp
    signatureString := fmt.Sprintf("key=%s&nonce=%s&secret=%s&timestamp=%d",
        apiKey, nonce, apiSecret, timestamp)
    hash := sha1.Sum([]byte(signatureString))
    return fmt.Sprintf("%x", hash)
}

type AuthParams struct {
    Key       string
    Timestamp int64
    Nonce     string
    Signature string
}

func getAuthParams(apiKey, apiSecret string) AuthParams {
    timestamp := time.Now().Unix()
    nonce := generateNonce(16)
    signature := generateSignature(apiKey, apiSecret, timestamp, nonce)

    return AuthParams{
        Key:       apiKey,
        Timestamp: timestamp,
        Nonce:     nonce,
        Signature: signature,
    }
}

func main() {
    apiKey := "your_api_key"
    apiSecret := "your_api_secret"

    auth := getAuthParams(apiKey, apiSecret)
    fmt.Printf("key=%s&timestamp=%d&nonce=%s&signature=%s\n",
        auth.Key, auth.Timestamp, auth.Nonce, auth.Signature)
}
```

## Request Validation

### Client-Side Checks

Before sending request, verify:
```python
# 1. Nonce is 16 characters
assert len(nonce) == 16

# 2. Timestamp is recent (within 60 seconds)
current_time = int(time.time())
assert abs(current_time - timestamp) < 60

# 3. Signature is 40 characters (SHA-1 hex)
assert len(signature) == 40
assert all(c in '0123456789abcdef' for c in signature)
```

### Server Response Errors

If signature fails, LCSC returns:
```json
{
  "success": false,
  "code": 430,
  "message": "Appsecret failed verification",
  "result": null
}
```

Common causes:
- Wrong API secret
- Incorrect parameter order
- Incorrect nonce format
- Timestamp too old (>60 seconds)
- Encoding issues with special characters

## Security Best Practices

### Storing Credentials

**DO:**
- Store in environment variables: `LCSC_API_KEY`, `LCSC_API_SECRET`
- Use secure vaults (AWS Secrets Manager, HashiCorp Vault)
- Load from `.env` file (never commit to git)
- Rotate credentials periodically

**DON'T:**
- Hardcode credentials in source code
- Commit credentials to version control
- Log credentials in application logs
- Expose in client-side code
- Share with unauthorized users

### Environment Variable Example

```bash
# .env file (add to .gitignore)
LCSC_API_KEY=your_api_key_here
LCSC_API_SECRET=your_api_secret_here
```

```python
import os

api_key = os.getenv('LCSC_API_KEY')
api_secret = os.getenv('LCSC_API_SECRET')

if not api_key or not api_secret:
    raise ValueError("Missing LCSC credentials in environment variables")
```

### Request Logging

**Safe logging (remove credentials):**
```python
# Remove sensitive data before logging
safe_params = {
    'key': '***',
    'nonce': nonce,
    'timestamp': timestamp,
    'signature': '***',
    'keyword': 'TL072CP'
}
logger.info(f"LCSC API Request: {safe_params}")
```

**Unsafe logging (avoid):**
```python
# NEVER do this
logger.info(f"Auth params: {auth}")  # Logs API secret!
```

## Nonce Requirements

### Why Nonce Matters

The nonce (number once) serves two purposes:
1. **Prevent replay attacks** - Each request must be unique
2. **Ensure timestamp accuracy** - Different nonce per second

### Nonce Format

- Must be 16 characters
- Must be random alphanumeric (a-z, A-Z, 0-9)
- Must be different for each request
- Must not be predictable

### Good Nonce Generators

```python
# Option 1: Random string
import random
import string
nonce = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))

# Option 2: UUID (take first 16 chars)
import uuid
nonce = str(uuid.uuid4()).replace('-', '')[:16]

# Option 3: Timestamp + random
import time, random
ts = str(int(time.time() * 1000000))[-8:]
rand = ''.join(random.choice(string.ascii_letters) for _ in range(8))
nonce = ts + rand
```

## Timestamp Requirements

### Time Synchronization

LCSC rejects requests older than 60 seconds. Keep server time synchronized:

```bash
# Linux/Mac - Install NTP
brew install ntp    # macOS
sudo apt install ntp # Linux

# Check current time
date -u +%s

# Should match server time within 1 second
curl -v https://ips.lcsc.com 2>&1 | grep -i date
```

### Handling Time Drift

If experiencing time sync issues:

```python
import requests
import time

# Get server time from LCSC
response = requests.get('https://ips.lcsc.com/rest/wmsc2agent/category')
server_time = int(response.headers.get('Date'))  # Approximate
local_time = int(time.time())

time_diff = abs(server_time - local_time)
print(f"Time difference: {time_diff} seconds")

if time_diff > 30:
    print("WARNING: Local time is out of sync with LCSC server!")
    print("Run: ntpdate -u time.nist.gov")
```

## Testing Authentication

### Test Request Template

```bash
#!/bin/bash

API_KEY="your_api_key"
API_SECRET="your_api_secret"
TIMESTAMP=$(date +%s)
NONCE=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 16 | head -n 1)

# Build signature string
SIGNATURE_STRING="key=${API_KEY}&nonce=${NONCE}&secret=${API_SECRET}&timestamp=${TIMESTAMP}"

# Generate SHA-1 signature
SIGNATURE=$(echo -n "${SIGNATURE_STRING}" | sha1sum | awk '{print $1}')

# Make request
curl "https://ips.lcsc.com/rest/wmsc2agent/category?key=${API_KEY}&timestamp=${TIMESTAMP}&nonce=${NONCE}&signature=${SIGNATURE}" | jq .
```

### Verify Signature Locally

```python
import hashlib

api_key = "user123"
api_secret = "mysecret456"
timestamp = "1704700800"
nonce = "aBc123DeF456gHiJ"
expected_signature = "calculated_hash_here"

# Verify
signature_string = f"key={api_key}&nonce={nonce}&secret={api_secret}&timestamp={timestamp}"
calculated = hashlib.sha1(signature_string.encode()).hexdigest()

print(f"Expected:   {expected_signature}")
print(f"Calculated: {calculated}")
print(f"Match: {expected_signature == calculated}")
```

## Troubleshooting

### Error 430: Appsecret failed verification

**Causes:**
1. Wrong API secret
2. Incorrect parameter order (must be: key, nonce, secret, timestamp)
3. Nonce not exactly 16 characters
4. Signature not lowercase hex
5. Encoding issues with special characters

**Fix:**
```python
# Debug: Print each step
print(f"key: '{api_key}'")
print(f"nonce: '{nonce}' (len={len(nonce)})")
print(f"secret: '{api_secret}'")
print(f"timestamp: {timestamp}")

signature_string = f"key={api_key}&nonce={nonce}&secret={api_secret}&timestamp={timestamp}"
print(f"Signature string: '{signature_string}'")

signature = hashlib.sha1(signature_string.encode()).hexdigest()
print(f"Signature: {signature}")
```

### Error 431: No access to information

**Causes:**
1. API key not found
2. API key not approved yet
3. Account type doesn't support API

**Fix:**
- Verify API credentials are correct
- Check LCSC email for approval confirmation
- Ensure business/agent account (not personal)

### Request timeout or slow response

**Causes:**
1. Network latency
2. LCSC server overload
3. Large response payload

**Fix:**
```python
import requests

# Increase timeout
response = requests.get(url, params=params, timeout=30)

# Add retry logic
import time
for attempt in range(3):
    try:
        response = requests.get(url, params=params, timeout=10)
        break
    except requests.Timeout:
        if attempt < 2:
            time.sleep(2 ** attempt)  # Exponential backoff
        else:
            raise
```

## Support

- Official API docs: https://www.lcsc.com/docs/openapi/index.html
- Support email: support@lcsc.com
- FAQ: https://www.lcsc.com/faqs/api
