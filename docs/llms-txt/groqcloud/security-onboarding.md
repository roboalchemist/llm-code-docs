# Source: https://console.groq.com/docs/production-readiness/security-onboarding

---
description: Learn how to securely configure and use the Groq API in production with best practices for API key management, transport security, input validation, and incident response.
title: Security Onboarding - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Security Onboarding

Welcome to the **Groq Security Onboarding** guide.

This page walks through best practices for protecting your API keys, securing client configurations, and hardening integrations before moving into production. 

## [Overview](#overview)

Security is a shared responsibility between Groq and our customers.

While Groq ensures secure API transport and service isolation, customers are responsible for securing client-side configurations, keys, and data handling. 

All Groq API traffic is encrypted in transit using TLS 1.2+ and authenticated via API keys.

## [Secure API Key Management](#secure-api-key-management)

Never expose or hardcode API keys directly into your source code.

Use environment variables or a secret management system. 

Python

```
# Good: use environment variables
export GROQ_API_KEY="gsk_your_secret_key_here"

# Bad: avoid committing secrets to source
echo 'api_key="gsk_your_secret_key_here"' >> config.py
```

```
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
```

```
import { Groq } from "groq";

const client = new Groq({
apiKey: process.env.GROQ_API_KEY,
});
```

**Warning:** Never embed keys in frontend code or expose them in browser bundles. If you need client-side usage, route through a trusted backend proxy.

## [Key Rotation & Revocation](#key-rotation--revocation)

* Rotate API keys periodically (e.g., quarterly).
* Revoke keys immediately if compromise is suspected.
* Use per-environment keys (dev / staging / prod).
* Log all API key creations and deletions.

Python

```
import os
from groq import Groq

def secure_client():
  key = os.getenv("GROQ_API_KEY")
  if not key:
      raise RuntimeError("Missing GROQ_API_KEY in environment")
  return Groq(api_key=key)

client = secure_client()
print(client.models.list())  # Test call
```

```
import { Groq } from "groq";

function secureClient() {
const key = process.env.GROQ_API_KEY;
if (!key) {
  throw new Error("Missing GROQ_API_KEY in environment");
}
return new Groq({ apiKey: key });
}

const client = secureClient();
console.log(await client.models.list());  // Test call
```

## [Transport Security (TLS)](#transport-security-tls)

Groq APIs enforce HTTPS (TLS 1.2 or higher). You should **never** disable SSL verification.

Python

```
import requests

response = requests.get("https://api.groq.com", verify=True)
```

```
const https = require("https");

https.get("https://api.groq.com", (res) => {
console.log("TLS Verified:", res.socket.authorized);
});
```

## [Input and Prompt Safety](#input-and-prompt-safety)

When integrating Groq into user-facing systems, ensure that user inputs cannot trigger prompt injection or tool misuse.

**Recommendations:**

* Sanitize user input before embedding in prompts.
* Avoid exposing internal system instructions or hidden context.
* Validate model outputs (especially JSON / code / commands).
* Limit model access to safe tools or actions only.

## [Rate Limiting and Retry Logic](#rate-limiting-and-retry-logic)

Implement client-side rate limiting and exponential backoff for 429 / 5xx responses.

Python

```
import time, random
from groq import Groq

client = Groq(api_key="gsk_...")

for attempt in range(5):
  try:
      resp = client.models.list()
      break
  except Exception as e:
      wait = min(2 ** attempt + random.random(), 30)
      time.sleep(wait)
```

```
async function callWithBackoff(fn, maxRetries = 5) {
for (let i = 0; i < maxRetries; i++) {
  try {
    return await fn();
  } catch (err) {
    const delay = Math.min(2 ** i + Math.random(), 30);
    await new Promise((r) => setTimeout(r, delay * 1000));
  }
}
}
```

## [Logging & Monitoring](#logging--monitoring)

Maintain structured logs for all API interactions.

**Include:**

* Timestamp
* Endpoint
* Request latency
* Key / service ID (non-secret)
* Error codes

**Tip:** Avoid logging sensitive data or raw model responses containing user information.

## [Secure Tool Use & Agent Integrations](#secure-tool-use--agent-integrations)

When using Groq's **Tool Use** or external function execution features:

* Expose only vetted, sandboxed tools.
* Restrict external network calls.
* Audit all registered tools and permissions.
* Validate arguments and outputs.

Python

```
import requests
from urllib.parse import quote

class SafeTools:
  @staticmethod
  async def get_weather(city):
      url = f"https://api.weather.com?q={quote(city)}"
      return requests.get(url)

# Export for use
safe_tools = SafeTools()
```

```
const safeTools = {
getWeather: async (city) => fetch(`https://api.weather.com?q=${encodeURIComponent(city)}`),
};

export default safeTools;
```

## [Incident Response](#incident-response)

If you suspect your API key is compromised:

1. Revoke the key immediately from the [Groq Console](https://console.groq.com/keys).
2. Rotate to a new key and redeploy secrets.
3. Review logs for suspicious activity.
4. Notify your security admin.

**Warning:** Never reuse compromised keys, even temporarily.

## [Resources](#resources)

* [Groq API Documentation](https://console.groq.com/docs/api-reference)
* [Prompt Engineering Guide](https://console.groq.com/docs/prompting)
* [Understanding and Optimizing Latency](https://console.groq.com/docs/production-readiness/optimizing-latency)
* [Production-Ready Checklist](https://console.groq.com/docs/production-readiness/production-ready-checklist)
* [Groq Developer Community](https://community.groq.com)
* [OpenBench](https://openbench.dev)
  
---

_This security guide should be customized based on your specific application requirements and updated based on production learnings._