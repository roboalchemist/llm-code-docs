# Source: https://docs.perplexity.ai/guides/perplexity-sdk-best-practices

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#overview)
Overview
This guide covers essential best practices for using the Perplexity SDKs in production environments. Following these practices will help you build robust, secure, and efficient applications.
## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#security-best-practices)
Security Best Practices
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#environment-variables)
Environment Variables
Always store API keys securely using environment variables:
1
Use environment variables
Store API keys in environment variables, never in source code.
Python
TypeScript/JavaScript
Copy
Ask AI
```
import os
from perplexity import Perplexity
# Good: Use environment variables
client = Perplexity(
    api_key=os.environ.get("PERPLEXITY_API_KEY")
)
# Bad: Never hardcode API keys
# client = Perplexity(api_key="pplx-abc123...")  # DON'T DO THIS

```

Never commit API keys to version control. Use .env files locally and secure environment variable management in production.
2
Use .env files for local development
Create a `.env` file for local development (add it to .gitignore).
.env
Copy
Ask AI
```
PERPLEXITY_API_KEY=your_api_key_here
PERPLEXITY_MAX_RETRIES=3
PERPLEXITY_TIMEOUT=30000

```

Python
TypeScript/JavaScript
Copy
Ask AI
```
from dotenv import load_dotenv
import os
from perplexity import Perplexity
# Load environment variables from .env file
load_dotenv()
client = Perplexity(
    api_key=os.getenv("PERPLEXITY_API_KEY"),
    max_retries=int(os.getenv("PERPLEXITY_MAX_RETRIES", "3"))
)

```

3
Validate environment variables
Check for required environment variables at startup.
Python
TypeScript/JavaScript
Copy
Ask AI
```
import os
import sys
from perplexity import Perplexity
def create_client():
    api_key = os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
        print("Error: PERPLEXITY_API_KEY environment variable is required")
        sys.exit(1)
    return Perplexity(api_key=api_key)
client = create_client()

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#api-key-rotation)
API Key Rotation
Implement secure API key rotation:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import os
import logging
from perplexity import Perplexity
from typing import Optional
class SecurePerplexityClient:
    def __init__(self, primary_key: Optional[str] = None, fallback_key: Optional[str] = None):
        self.primary_key = primary_key or os.getenv("PERPLEXITY_API_KEY")
        self.fallback_key = fallback_key or os.getenv("PERPLEXITY_API_KEY_FALLBACK")
        self.current_client = Perplexity(api_key=self.primary_key)
        self.logger = logging.getLogger(__name__)
    def _switch_to_fallback(self):
        """Switch to fallback API key if available"""
        if self.fallback_key:
            self.logger.warning("Switching to fallback API key")
            self.current_client = Perplexity(api_key=self.fallback_key)
            return True
        return False
    def search(self, query: str, **kwargs):
        try:
            return self.current_client.search.create(query=query, **kwargs)
        except Exception as e:
            if "authentication" in str(e).lower() and self._switch_to_fallback():
                return self.current_client.search.create(query=query, **kwargs)
            raise e
# Usage
client = SecurePerplexityClient()

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#rate-limiting-and-efficiency)
Rate Limiting and Efficiency
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#intelligent-rate-limiting)
Intelligent Rate Limiting
Implement exponential backoff with jitter:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import time
import random
import asyncio
from typing import TypeVar, Callable, Any
import perplexity
from perplexity import Perplexity
T = TypeVar('T')
class RateLimitedClient:
    def __init__(self, client: Perplexity, max_retries: int = 5):
        self.client = client
        self.max_retries = max_retries
    def _calculate_delay(self, attempt: int) -> float:
        """Calculate delay with exponential backoff and jitter"""
        base_delay = 2 ** attempt
        jitter = random.uniform(0.1, 0.5)
        return min(base_delay + jitter, 60.0)  # Cap at 60 seconds
    def with_retry(self, func: Callable[[], T]) -> T:
        """Execute function with intelligent retry logic"""
        last_exception = None
        for attempt in range(self.max_retries):
            try:
                return func()
            except perplexity.RateLimitError as e:
                last_exception = e
                if attempt < self.max_retries - 1:
                    delay = self._calculate_delay(attempt)
                    print(f"Rate limited. Retrying in {delay:.2f}s (attempt {attempt + 1})")
                    time.sleep(delay)
                    continue
                raise e
            except perplexity.APIConnectionError as e:
                last_exception = e
                if attempt < self.max_retries - 1:
                    delay = min(2 ** attempt, 10.0)  # Shorter delay for connection errors
                    print(f"Connection error. Retrying in {delay:.2f}s")
                    time.sleep(delay)
                    continue
                raise e
        raise last_exception
    def search(self, query: str, **kwargs):
        return self.with_retry(
            lambda: self.client.search.create(query=query, **kwargs)
        )
# Usage
client = RateLimitedClient(Perplexity())
result = client.search("artificial intelligence")

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#request-batching)
Request Batching
Efficiently batch multiple requests:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import asyncio
from typing import List, TypeVar, Generic
from perplexity import AsyncPerplexity, DefaultAioHttpClient
T = TypeVar('T')
class BatchProcessor(Generic[T]):
    def __init__(self, batch_size: int = 5, delay_between_batches: float = 1.0):
        self.batch_size = batch_size
        self.delay_between_batches = delay_between_batches
    async def process_batch(
        self, 
        items: List[str], 
        process_func: Callable[[str], Awaitable[T]]
    ) -> List[T]:
        """Process items in batches with rate limiting"""
        results = []
        for i in range(0, len(items), self.batch_size):
            batch = items[i:i + self.batch_size]
            # Process batch concurrently
            tasks = [process_func(item) for item in batch]
            batch_results = await asyncio.gather(*tasks, return_exceptions=True)
            # Filter out exceptions and collect results
            for result in batch_results:
                if not isinstance(result, Exception):
                    results.append(result)
            # Delay between batches
            if i + self.batch_size < len(items):
                await asyncio.sleep(self.delay_between_batches)
        return results
# Usage
async def main():
    processor = BatchProcessor(batch_size=3, delay_between_batches=0.5)
    async with AsyncPerplexity(
        http_client=DefaultAioHttpClient()
    ) as client:
        async def search_query(query: str):
            return await client.search.create(query=query)
        queries = ["AI", "ML", "DL", "NLP", "CV"]
        results = await processor.process_batch(queries, search_query)
        print(f"Processed {len(results)} successful queries")
asyncio.run(main())

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#production-configuration)
Production Configuration
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#configuration-management)
Configuration Management
Use environment-based configuration for different deployment stages:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import os
from dataclasses import dataclass
from typing import Optional
import httpx
from perplexity import Perplexity, DefaultHttpxClient
@dataclass
class PerplexityConfig:
    api_key: str
    max_retries: int = 3
    timeout_seconds: float = 30.0
    max_connections: int = 100
    max_keepalive: int = 20
    environment: str = "production"
    @classmethod
    def from_env(cls) -> "PerplexityConfig":
        """Load configuration from environment variables"""
        api_key = os.getenv("PERPLEXITY_API_KEY")
        if not api_key:
            raise ValueError("PERPLEXITY_API_KEY environment variable is required")
        return cls(
            api_key=api_key,
            max_retries=int(os.getenv("PERPLEXITY_MAX_RETRIES", "3")),
            timeout_seconds=float(os.getenv("PERPLEXITY_TIMEOUT", "30.0")),
            max_connections=int(os.getenv("PERPLEXITY_MAX_CONNECTIONS", "100")),
            max_keepalive=int(os.getenv("PERPLEXITY_MAX_KEEPALIVE", "20")),
            environment=os.getenv("ENVIRONMENT", "production")
        )
    def create_client(self) -> Perplexity:
        """Create optimized client based on configuration"""
        timeout = httpx.Timeout(
            connect=5.0,
            read=self.timeout_seconds,
            write=10.0,
            pool=10.0
        )
        limits = httpx.Limits(
            max_keepalive_connections=self.max_keepalive,
            max_connections=self.max_connections,
            keepalive_expiry=60.0 if self.environment == "production" else 30.0
        )
        return Perplexity(
            api_key=self.api_key,
            max_retries=self.max_retries,
            timeout=timeout,
            http_client=DefaultHttpxClient(limits=limits)
        )
# Usage
config = PerplexityConfig.from_env()
client = config.create_client()

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#monitoring-and-logging)
Monitoring and Logging
Implement comprehensive monitoring:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import logging
import time
import functools
from typing import Any, Callable
from perplexity import Perplexity
import perplexity
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
class MonitoredPerplexityClient:
    def __init__(self, client: Perplexity):
        self.client = client
        self.request_count = 0
        self.error_count = 0
        self.total_response_time = 0.0
    def _log_request(self, method: str, **kwargs):
        """Log request details"""
        self.request_count += 1
        logger.info(f"Making {method} request #{self.request_count}")
        logger.debug(f"Request parameters: {kwargs}")
    def _log_response(self, method: str, duration: float, success: bool = True):
        """Log response details"""
        self.total_response_time += duration
        avg_response_time = self.total_response_time / self.request_count
        if success:
            logger.info(f"{method} completed in {duration:.2f}s (avg: {avg_response_time:.2f}s)")
        else:
            self.error_count += 1
            logger.error(f"{method} failed after {duration:.2f}s (errors: {self.error_count})")
    def search(self, query: str, **kwargs):
        self._log_request("search", query=query, **kwargs)
        start_time = time.time()
        try:
            result = self.client.search.create(query=query, **kwargs)
            duration = time.time() - start_time
            self._log_response("search", duration, success=True)
            return result
        except Exception as e:
            duration = time.time() - start_time
            self._log_response("search", duration, success=False)
            logger.error(f"Search error: {type(e).__name__}: {e}")
            raise
    def get_stats(self):
        """Get client statistics"""
        return {
            "total_requests": self.request_count,
            "error_count": self.error_count,
            "success_rate": (self.request_count - self.error_count) / max(self.request_count, 1),
            "avg_response_time": self.total_response_time / max(self.request_count, 1)
        }
# Usage
client = MonitoredPerplexityClient(Perplexity())
result = client.search("machine learning")
print(client.get_stats())

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#error-handling-best-practices)
Error Handling Best Practices
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#graceful-degradation)
Graceful Degradation
Implement fallback strategies for different error types:
Python
TypeScript/JavaScript
Copy
Ask AI
```
from typing import Optional, Dict, Any
import perplexity
from perplexity import Perplexity
class ResilientPerplexityClient:
    def __init__(self, client: Perplexity):
        self.client = client
        self.circuit_breaker_threshold = 5
        self.circuit_breaker_count = 0
        self.circuit_breaker_open = False
    def _should_circuit_break(self) -> bool:
        """Check if circuit breaker should be triggered"""
        return self.circuit_breaker_count >= self.circuit_breaker_threshold
    def _record_failure(self):
        """Record a failure for circuit breaker"""
        self.circuit_breaker_count += 1
        if self._should_circuit_break():
            self.circuit_breaker_open = True
            print("Circuit breaker activated - temporarily disabling API calls")
    def _record_success(self):
        """Record a success - reset circuit breaker"""
        self.circuit_breaker_count = 0
        self.circuit_breaker_open = False
    def search_with_fallback(
        self, 
        query: str, 
        fallback_response: Optional[Dict[str, Any]] = None
    ):
        """Search with graceful degradation"""
        if self.circuit_breaker_open:
            print("Circuit breaker open - returning fallback response")
            return fallback_response or {
                "query": query,
                "results": [],
                "status": "service_unavailable"
            }
        try:
            result = self.client.search.create(query=query)
            self._record_success()
            return result
        except perplexity.RateLimitError:
            print("Rate limited - implementing backoff strategy")
            # Could implement intelligent backoff here
            raise
        except perplexity.APIConnectionError as e:
            print(f"Connection error: {e}")
            self._record_failure()
            return fallback_response or {
                "query": query,
                "results": [],
                "status": "connection_error"
            }
        except Exception as e:
            print(f"Unexpected error: {e}")
            self._record_failure()
            return fallback_response or {
                "query": query,
                "results": [],
                "status": "error"
            }
# Usage
client = ResilientPerplexityClient(Perplexity())
result = client.search_with_fallback("machine learning")

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#testing-best-practices)
Testing Best Practices
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#unit-testing-with-mocking)
Unit Testing with Mocking
Create testable code with proper mocking:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import unittest
from unittest.mock import Mock, patch
from perplexity import Perplexity
from perplexity.types import SearchCreateResponse, SearchResult
class TestPerplexityIntegration(unittest.TestCase):
    def setUp(self):
        self.mock_client = Mock(spec=Perplexity)
    def test_search_success(self):
        # Mock successful response
        mock_result = SearchResult(
            title="Test Result",
            url="https://example.com",
            snippet="Test snippet"
        )
        mock_response = SearchCreateResponse(
            query="test query",
            results=[mock_result]
        )
        self.mock_client.search.create.return_value = mock_response
        # Test your application logic
        result = self.mock_client.search.create(query="test query")
        self.assertEqual(result.query, "test query")
        self.assertEqual(len(result.results), 1)
        self.assertEqual(result.results[0].title, "Test Result")
    @patch('perplexity.Perplexity')
    def test_rate_limit_handling(self, mock_perplexity_class):
        # Mock rate limit error
        mock_client = Mock()
        mock_perplexity_class.return_value = mock_client
        mock_client.search.create.side_effect = perplexity.RateLimitError("Rate limited")
        # Test your error handling logic here
        with self.assertRaises(perplexity.RateLimitError):
            mock_client.search.create(query="test")
if __name__ == '__main__':
    unittest.main()

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#performance-best-practices-summary)
Performance Best Practices Summary
1
Use environment variables for configuration
Never hardcode API keys or configuration values.
2
Implement intelligent rate limiting
Use exponential backoff with jitter for retry strategies.
3
Configure connection pooling
Optimize HTTP client settings for your use case.
4
Monitor and log appropriately
Track performance metrics and error rates.
5
Implement graceful degradation
Provide fallback responses when APIs are unavailable.
6
Write testable code
Use dependency injection and mocking for unit tests.
## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices#related-resources)
Related Resources
## [Error Handling Comprehensive error handling strategies ](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling)## [Performance Async operations and optimization techniques ](https://docs.perplexity.ai/guides/perplexity-sdk-performance)## [Configuration Production-ready configuration patterns ](https://docs.perplexity.ai/guides/perplexity-sdk-configuration)## [Type Safety Leveraging types for safer code ](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety)
