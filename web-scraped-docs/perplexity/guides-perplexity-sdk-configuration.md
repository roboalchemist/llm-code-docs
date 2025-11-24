# Source: https://docs.perplexity.ai/guides/perplexity-sdk-configuration

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#overview)
Overview
The Perplexity SDKs provide extensive configuration options to customize client behavior for different environments and use cases. This guide covers retry configuration, timeout settings, and custom HTTP client setup.
## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#retries-and-timeouts)
Retries and Timeouts
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#basic-retry-configuration)
Basic Retry Configuration
Configure how the SDK handles failed requests:
Python
TypeScript/JavaScript
Copy
Ask AI
```
from perplexity import Perplexity
import httpx
client = Perplexity(
    max_retries=3,  # Default is 2
    timeout=httpx.Timeout(30.0, read=10.0, write=5.0, connect=2.0)
)
# Per-request configuration
search = client.with_options(max_retries=5).search.create(
    query="example"
)

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#advanced-timeout-configuration)
Advanced Timeout Configuration
Set granular timeout controls for different phases of the request:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import httpx
from perplexity import Perplexity
# Detailed timeout configuration
timeout_config = httpx.Timeout(
    connect=5.0,    # Time to establish connection
    read=30.0,      # Time to read response
    write=10.0,     # Time to send request
    pool=10.0       # Time to get connection from pool
)
client = Perplexity(timeout=timeout_config)
# For long-running operations
long_timeout = httpx.Timeout(
    connect=5.0,
    read=120.0,  # 2 minutes for complex queries
    write=10.0,
    pool=10.0
)
client_long = Perplexity(timeout=long_timeout)

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#custom-http-client)
Custom HTTP Client
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#proxy-configuration)
Proxy Configuration
Configure the SDK to work with corporate proxies:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import httpx
from perplexity import Perplexity, DefaultHttpxClient
# HTTP Proxy
client = Perplexity(
    http_client=DefaultHttpxClient(
        proxy="http://proxy.company.com:8080"
    )
)
# HTTPS Proxy with authentication
client_auth = Perplexity(
    http_client=DefaultHttpxClient(
        proxy="http://username:password@proxy.company.com:8080"
    )
)
# SOCKS proxy
client_socks = Perplexity(
    http_client=DefaultHttpxClient(
        proxy="socks5://proxy.company.com:1080"
    )
)

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#custom-headers-and-user-agent)
Custom Headers and User Agent
Add custom headers to all requests:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import httpx
from perplexity import Perplexity, DefaultHttpxClient
# Custom headers
headers = {
    "User-Agent": "MyApp/1.0",
    "X-Custom-Header": "custom-value"
}
client = Perplexity(
    http_client=DefaultHttpxClient(
        headers=headers
    )
)
# Advanced HTTP client configuration
transport = httpx.HTTPTransport(
    local_address="0.0.0.0",  # Bind to specific interface
    verify=True,              # SSL verification
    cert=None,                # Client certificate
    http2=True               # Enable HTTP/2
)
client_advanced = Perplexity(
    http_client=DefaultHttpxClient(
        transport=transport,
        headers=headers
    )
)

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#ssl%2Ftls-configuration)
SSL/TLS Configuration
Configure SSL verification and certificates:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import httpx
import ssl
from perplexity import Perplexity, DefaultHttpxClient
# Disable SSL verification (not recommended for production)
client_no_ssl = Perplexity(
    http_client=DefaultHttpxClient(
        verify=False
    )
)
# Custom SSL context
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
client_custom_ssl = Perplexity(
    http_client=DefaultHttpxClient(
        verify=ssl_context
    )
)
# Client certificate authentication
client_cert = Perplexity(
    http_client=DefaultHttpxClient(
        cert=("client.crt", "client.key")
    )
)

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#connection-pooling)
Connection Pooling
Optimize performance with connection pooling:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import httpx
from perplexity import Perplexity, DefaultHttpxClient
# Configure connection limits
limits = httpx.Limits(
    max_keepalive_connections=20,  # Keep-alive connections
    max_connections=100,           # Total connections
    keepalive_expiry=30.0         # Keep-alive timeout
)
client = Perplexity(
    http_client=DefaultHttpxClient(
        limits=limits
    )
)
# For high-throughput applications
high_throughput_limits = httpx.Limits(
    max_keepalive_connections=100,
    max_connections=500,
    keepalive_expiry=60.0
)
client_high_throughput = Perplexity(
    http_client=DefaultHttpxClient(
        limits=high_throughput_limits
    )
)

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#environment-specific-configuration)
Environment-Specific Configuration
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#development-configuration)
Development Configuration
Settings optimized for development and debugging:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import httpx
from perplexity import Perplexity, DefaultHttpxClient
# Development configuration
dev_client = Perplexity(
    max_retries=1,           # Fail fast in development
    timeout=httpx.Timeout(10.0),  # Short timeout
    http_client=DefaultHttpxClient(
        # Enable detailed logging
        event_hooks={
            'request': [lambda request: print(f"Request: {request.method} {request.url}")],
            'response': [lambda response: print(f"Response: {response.status_code}")]
        }
    )
)

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#production-configuration)
Production Configuration
Settings optimized for production environments:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import httpx
from perplexity import Perplexity, DefaultHttpxClient
# Production configuration
prod_limits = httpx.Limits(
    max_keepalive_connections=50,
    max_connections=200,
    keepalive_expiry=60.0
)
prod_timeout = httpx.Timeout(
    connect=5.0,
    read=60.0,
    write=10.0,
    pool=10.0
)
prod_client = Perplexity(
    max_retries=3,
    timeout=prod_timeout,
    http_client=DefaultHttpxClient(
        limits=prod_limits,
        verify=True,  # Always verify SSL in production
        http2=True    # Enable HTTP/2 for better performance
    )
)

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#configuration-patterns)
Configuration Patterns
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#environment-based-configuration)
Environment-Based Configuration
Use environment variables to configure the client:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import os
import httpx
from perplexity import Perplexity, DefaultHttpxClient
def create_client():
    # Base configuration
    timeout = httpx.Timeout(
        connect=float(os.getenv('PERPLEXITY_CONNECT_TIMEOUT', '5.0')),
        read=float(os.getenv('PERPLEXITY_READ_TIMEOUT', '30.0')),
        write=float(os.getenv('PERPLEXITY_WRITE_TIMEOUT', '10.0'))
    )
    max_retries = int(os.getenv('PERPLEXITY_MAX_RETRIES', '3'))
    # Optional proxy configuration
    proxy = os.getenv('PERPLEXITY_PROXY')
    http_client_kwargs = {}
    if proxy:
        http_client_kwargs['proxy'] = proxy
    return Perplexity(
        max_retries=max_retries,
        timeout=timeout,
        http_client=DefaultHttpxClient(**http_client_kwargs)
    )
client = create_client()

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#configuration-factory)
Configuration Factory
Create reusable configuration patterns:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import httpx
from perplexity import Perplexity, DefaultHttpxClient
class PerplexityClientFactory:
    @staticmethod
    def development():
        return Perplexity(
            max_retries=1,
            timeout=httpx.Timeout(10.0)
        )
    @staticmethod
    def production():
        return Perplexity(
            max_retries=3,
            timeout=httpx.Timeout(connect=5.0, read=60.0, write=10.0),
            http_client=DefaultHttpxClient(
                limits=httpx.Limits(
                    max_keepalive_connections=50,
                    max_connections=200
                )
            )
        )
    @staticmethod
    def high_throughput():
        return Perplexity(
            max_retries=2,
            timeout=httpx.Timeout(connect=2.0, read=30.0, write=5.0),
            http_client=DefaultHttpxClient(
                limits=httpx.Limits(
                    max_keepalive_connections=100,
                    max_connections=500
                )
            )
        )
# Usage
client = PerplexityClientFactory.production()

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-configuration#related-resources)
Related Resources
## [Error Handling Handle timeouts and connection errors ](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling)## [Performance Optimize async operations and connection pooling ](https://docs.perplexity.ai/guides/perplexity-sdk-performance)
