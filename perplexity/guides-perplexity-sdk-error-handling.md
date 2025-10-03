# Source: https://docs.perplexity.ai/guides/perplexity-sdk-error-handling

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling#overview)
Overview
The Perplexity SDKs provide robust error handling with specific exception types for different error scenarios. This guide covers how to catch and handle common API errors gracefully.
## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling#common-error-types)
Common Error Types
The SDKs provide specific exception types for different error scenarios:
  * **APIConnectionError** - Network connection issues
  * **RateLimitError** - API rate limit exceeded
  * **APIStatusError** - HTTP status errors (4xx, 5xx)
  * **AuthenticationError** - Invalid API key or authentication issues
  * **ValidationError** - Invalid request parameters


## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling#basic-error-handling)
Basic Error Handling
Handle common API errors with try-catch blocks:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import perplexity
from perplexity import Perplexity
client = Perplexity()
try:
    search = client.search.create(query="machine learning")
    print(search.results)
except perplexity.APIConnectionError as e:
    print("Network connection failed")
    print(e.__cause__)
except perplexity.RateLimitError as e:
    print("Rate limit exceeded, please retry later")
except perplexity.APIStatusError as e:
    print(f"API error: {e.status_code}")
    print(e.response)

```

Common HTTP status codes: 400 (Bad Request), 401 (Authentication), 403 (Permission Denied), 404 (Not Found), 429 (Rate Limit), 500+ (Server Error).
## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling#advanced-error-handling)
Advanced Error Handling
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling#exponential-backoff-for-rate-limits)
Exponential Backoff for Rate Limits
Implement intelligent retry logic for rate limit errors:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import time
import random
import perplexity
from perplexity import Perplexity
def search_with_retry(client, query, max_retries=3):
    for attempt in range(max_retries):
        try:
            return client.search.create(query=query)
        except perplexity.RateLimitError:
            if attempt == max_retries - 1:
                raise  # Re-raise on final attempt
            # Exponential backoff with jitter
            delay = (2 ** attempt) + random.uniform(0, 1)
            print(f"Rate limited. Retrying in {delay:.2f} seconds...")
            time.sleep(delay)
        except perplexity.APIConnectionError:
            if attempt == max_retries - 1:
                raise
            # Shorter delay for connection errors
            delay = 1 + random.uniform(0, 1)
            print(f"Connection error. Retrying in {delay:.2f} seconds...")
            time.sleep(delay)
# Usage
client = Perplexity()
result = search_with_retry(client, "artificial intelligence")

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling#error-context-and-debugging)
Error Context and Debugging
Extract detailed error information for debugging:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import perplexity
from perplexity import Perplexity
client = Perplexity()
try:
    chat = client.chat.completions.create(
        model="llama-3.1-sonar-small-128k-online",
        messages=[{"role": "user", "content": "What's the weather?"}]
    )
except perplexity.APIStatusError as e:
    print(f"Status Code: {e.status_code}")
    print(f"Error Type: {e.type}")
    print(f"Error Message: {e.message}")
    # Access raw response for detailed debugging
    if hasattr(e, 'response'):
        print(f"Raw Response: {e.response.text}")
        print(f"Request ID: {e.response.headers.get('X-Request-ID')}")
except perplexity.ValidationError as e:
    print(f"Validation Error: {e}")
    # Handle parameter validation errors
except Exception as e:
    print(f"Unexpected error: {type(e).__name__}: {e}")

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling#error-recovery-strategies)
Error Recovery Strategies
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling#graceful-degradation)
Graceful Degradation
Implement fallback mechanisms when API calls fail:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import perplexity
from perplexity import Perplexity
def get_ai_response(query, fallback_response="I'm sorry, I'm temporarily unavailable."):
    client = Perplexity()
    try:
        # Primary: Try online model
        response = client.chat.completions.create(
            model="llama-3.1-sonar-small-128k-online",
            messages=[{"role": "user", "content": query}]
        )
        return response.choices[0].message.content
    except perplexity.RateLimitError:
        try:
            # Fallback: Try offline model if rate limited
            response = client.chat.completions.create(
                model="llama-3.1-8b-instruct",
                messages=[{"role": "user", "content": query}]
            )
            return response.choices[0].message.content
        except Exception:
            return fallback_response
    except perplexity.APIConnectionError:
        # Network issues - return cached response or fallback
        return fallback_response
    except Exception as e:
        print(f"Unexpected error: {e}")
        return fallback_response
# Usage
response = get_ai_response("What is machine learning?")
print(response)

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling#best-practices)
Best Practices
1
Always handle rate limits
Rate limiting is common with API usage. Always implement retry logic with exponential backoff.
Don’t implement aggressive retry loops without delays - this can worsen rate limiting.
2
Log errors for monitoring
Include proper logging to track error patterns and API health.
Python
TypeScript/JavaScript
Copy
Ask AI
```
import logging
import perplexity
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
try:
    result = client.search.create(query="example")
except perplexity.APIStatusError as e:
    logger.error(f"API Error {e.status_code}: {e.message}", 
                extra={'request_id': e.response.headers.get('X-Request-ID')})

```

3
Set appropriate timeouts
Configure timeouts to prevent hanging requests.
Python
TypeScript/JavaScript
Copy
Ask AI
```
import httpx
from perplexity import Perplexity
client = Perplexity(
    timeout=httpx.Timeout(connect=5.0, read=30.0, write=5.0, pool=10.0)
)

```

4
Handle authentication errors
Check for invalid API keys and provide helpful error messages.
Python
TypeScript/JavaScript
Copy
Ask AI
```
try:
    result = client.search.create(query="test")
except perplexity.AuthenticationError:
    print("Invalid API key. Please check your PERPLEXITY_API_KEY environment variable.")

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling#related-resources)
Related Resources
## [Configuration Configure timeouts and retries ](https://docs.perplexity.ai/guides/perplexity-sdk-configuration)## [Best Practices Environment variables and rate limiting ](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices)
