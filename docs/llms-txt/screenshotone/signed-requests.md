# Source: https://screenshotone.com/docs/signed-requests/

# Signed Links

import Alert from "@/components/Alert.astro";

When you share links to the screenshots with your access key in public, there is a problem that everybody can take your API access key and reuse it to take screenshots on their own and exhaust your screenshot quota.

To prevent others from using your API key, you need to:
1. [Sign every request](https://screenshotone.com/docs/signed-requests/#signing-requests) you are going to share publicly.
2. [Require signing](https://screenshotone.com/docs/signed-requests/#require-signing) for every request.

Then even if the potential unscrupulous person sees or steals your access key, they can't reuse it until they also steal your secret key (signing key).

You generally don't need to sign requests if you will not share screenshot links publicly and will use screenshot API only on the server-side.

## Signing requests

<Alert>
Singed links do not work with HTTP "POST" requests. The feature is intended to be used for sharing links in public.
</Alert>

To sign the request, like `https://api.screenshotone.com/take?access_key=0Ij4LFMtFnGUrA&url=https://apple.com`, you need to follow the simple algorithm:

1. Use your secret to hash the query string `access_key=0Ij4LFMtFnGUrA&url=https://apple.com` with the HMAC SHA256 algorithm.
  
2. **Append** the signature parameter with the hash: `https://api.screenshotone.com/?access_key=0Ij4LFMtFnGUrA&url=https://apple.com&signature=70bea3e52efc43834129ecbea236f38bf9bb4a7cd7c2e1951017435defd4dbaf`.

**Do not sort the parameters. Or if you sort them, send them sorted, too.**
  
To hash the query string with your secret key and HMAC SHA256 algorithm in the CLI, you can run the following command:

```bash
$ echo -n "access_key=0Ij4LFMtFnGUrA&url=https://apple.com" | openssl sha256 -hmac "m9ajW9br9hTw2A"                     130 ↵

70bea3e52efc43834129ecbea236f38bf9bb4a7cd7c2e1951017435defd4dbaf
```

## Code examples

You can need to apply the same algorithm in the language of your choice.

### Python

For example, in Python:

```python
import urllib.parse
import hmac
import hashlib

def generate_signature(params: dict, secret_key: str) -> str:
    """
    Generate a signature for the given parameters using HMAC-SHA256.
    
    Args:
        params (dict): Dictionary of parameters to sign
        secret_key (str): Secret key used for signing
        
    Returns:
        str: The hexadecimal signature
    """        
    # convert parameters to URL-encoded query string
    query_string = urllib.parse.urlencode(params, doseq=True)

    signature = hmac.new(
        bytes(secret_key, "utf-8"),
        msg=bytes(query_string, "utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()
    
    return signature

# Example usage
if __name__ == "__main__":
    # options
    params = {
        "access_key": "your_access_key",
        "url": "https://example.com",
        "format": "jpeg",
        "viewport_width": 1920,
        "viewport_height": 1080
    }
    
    secret_key = "your_secret_key"
    
    # generate signature
    signature = generate_signature(params, secret_key)
    
    print("Parameters:", params)
    print("Query string:", urllib.parse.urlencode(params, doseq=True))
    print("Signature:", signature)
    
    query_string = urllib.parse.urlencode(params, doseq=True)
    final_url = f"https://api.screenshotone.com/take?{query_string}&signature={signature}"
    print("\nAPI URL:", final_url)
```

### JavaScript

Or in JavaScript:

```javascript
// npm install @peculiar/webcrypto
import { Crypto } from "@peculiar/webcrypto";

const encoder = new TextEncoder();

export async function signQueryString(queryString: string, secretKey: string) {
    const webCrypto =
        typeof globalThis.crypto !== "undefined"
            ? globalThis.crypto
            : new Crypto();

    let algorithm = { name: "HMAC", hash: "SHA-256" };
    let key = await webCrypto.subtle.importKey(
        "raw",
        encoder.encode(secretKey),
        algorithm,
        false,
        ["sign", "verify"]
    );
    const digest = await webCrypto.subtle.sign(
        algorithm.name,
        key,
        encoder.encode(queryString)
    );

    const signature = Array.from(new Uint8Array(digest))
        .map((b) => b.toString(16).padStart(2, "0"))
        .join("");

    return signature;
}

// example usage
const query = new URLSearchParams({
    access_key: "your_access_key",
    url: "https://example.com"
});
let queryString = query.toString();

const signature = await signQueryString(queryString, "your_secret_key");
queryString += "&signature=" + signature;

console.log(queryString);
```

## Require signing

After you start signing requests and make sure that the API accepts your requests, you can require signing every request.
Go to [the access configuration page](https://dash.screenshotone.com/access) and enforce signing every request.
The change will be applied immediately, but cached screenshots might not be impacted.
That's it. After this step, unsigned requests with your API access key are not accepted.

## Animated screenshots 

[Animated screenshots](/docs/animated-screenshots/) also support signed links. There is no difference in the underlying mechanism besides that the URL prefix should be `/animate`.