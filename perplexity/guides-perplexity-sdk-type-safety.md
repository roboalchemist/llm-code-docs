# Source: https://docs.perplexity.ai/guides/perplexity-sdk-type-safety

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#overview)
Overview
Both Perplexity SDKs provide comprehensive type definitions to help you catch errors at development time and provide better IDE support. This guide covers type annotations, generic types, and advanced typing patterns.
## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#basic-type-usage)
Basic Type Usage
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#type-imports-and-annotations)
Type Imports and Annotations
Use type imports for better IDE support and type checking:
Python
TypeScript/JavaScript
Copy
Ask AI
```
from perplexity import Perplexity
from perplexity.types import (
    SearchCreateResponse,
    ChatCompletionCreateResponse,
    SearchResult,
    ChatCompletionMessage
)
client = Perplexity()
# Type hints for better IDE support
search_response: SearchCreateResponse = client.search.create(
    query="artificial intelligence"
)
# Access typed properties
result: SearchResult = search_response.results[0]
print(f"Title: {result.title}")
print(f"URL: {result.url}")
print(f"Snippet: {result.snippet}")

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#runtime-type-validation)
Runtime Type Validation
Python SDK uses Pydantic for runtime type validation:
Python
TypeScript/JavaScript
Copy
Ask AI
```
from perplexity import Perplexity
from perplexity.types import SearchCreateResponse
client = Perplexity()
# Runtime validation ensures type safety
try:
    search_response = client.search.create(
        query="machine learning",
        max_results=10
    )
    # Pydantic model methods for serialization
    json_data = search_response.to_json()
    dict_data = search_response.to_dict()
    # Type validation on field access
    first_result = search_response.results[0]
    print(f"Result type: {type(first_result)}")
except ValueError as e:
    print(f"Type validation error: {e}")

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#advanced-type-patterns)
Advanced Type Patterns
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#generic-type-helpers)
Generic Type Helpers
Create reusable typed functions:
Python
TypeScript/JavaScript
Copy
Ask AI
```
from typing import TypeVar, Generic, List, Optional, Callable
from perplexity import Perplexity
from perplexity.types import SearchCreateResponse, ChatCompletionCreateResponse
T = TypeVar('T')
R = TypeVar('R')
class TypedPerplexityClient:
    def __init__(self, client: Perplexity):
        self.client = client
    def search_with_transform(
        self, 
        query: str, 
        transform: Callable[[SearchCreateResponse], T]
    ) -> T:
        """Perform search and transform the result with type safety"""
        response = self.client.search.create(query=query)
        return transform(response)
    def batch_search(
        self, 
        queries: List[str]
    ) -> List[SearchCreateResponse]:
        """Perform multiple searches with proper typing"""
        results = []
        for query in queries:
            response = self.client.search.create(query=query)
            results.append(response)
        return results
# Usage with type safety
client = TypedPerplexityClient(Perplexity())
def extract_titles(response: SearchCreateResponse) -> List[str]:
    return [result.title for result in response.results]
# Typed function call
titles: List[str] = client.search_with_transform("AI research", extract_titles)

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#custom-type-guards)
Custom Type Guards
Create type guards for safer type checking:
Python
TypeScript/JavaScript
Copy
Ask AI
```
from typing import Union, TypeGuard
from perplexity.types import (
    SearchCreateResponse, 
    ChatCompletionCreateResponse,
    SearchResult
)
def is_search_response(
    response: Union[SearchCreateResponse, ChatCompletionCreateResponse]
) -> TypeGuard[SearchCreateResponse]:
    """Type guard to check if response is a search response"""
    return hasattr(response, 'results')
def is_valid_search_result(result: SearchResult) -> TypeGuard[SearchResult]:
    """Type guard to validate search result structure"""
    return (
        hasattr(result, 'title') and
        hasattr(result, 'url') and
        hasattr(result, 'snippet') and
        result.title is not None and
        result.url is not None
    )
# Usage
def process_response(
    response: Union[SearchCreateResponse, ChatCompletionCreateResponse]
) -> None:
    if is_search_response(response):
        # TypeScript now knows this is SearchCreateResponse
        for result in response.results:
            if is_valid_search_result(result):
                print(f"Valid result: {result.title}")
            else:
                print("Invalid result format")

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#response-type-utilities)
Response Type Utilities
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#extracting-nested-types)
Extracting Nested Types
Work with nested response structures safely:
Python
TypeScript/JavaScript
Copy
Ask AI
```
from typing import List, Optional
from perplexity import Perplexity
from perplexity.types import (
    SearchCreateResponse,
    SearchResult,
    ChatCompletionCreateResponse,
    ChatCompletionChoice
)
class ResponseUtils:
    @staticmethod
    def extract_search_titles(response: SearchCreateResponse) -> List[str]:
        """Extract all search result titles with type safety"""
        return [result.title for result in response.results if result.title]
    @staticmethod
    def extract_search_urls(response: SearchCreateResponse) -> List[str]:
        """Extract all search result URLs with type safety"""
        return [result.url for result in response.results if result.url]
    @staticmethod
    def get_first_search_result(
        response: SearchCreateResponse
    ) -> Optional[SearchResult]:
        """Get first search result safely"""
        return response.results[0] if response.results else None
    @staticmethod
    def extract_chat_content(
        response: ChatCompletionCreateResponse
    ) -> Optional[str]:
        """Extract chat completion content safely"""
        if response.choices and response.choices[0].message:
            return response.choices[0].message.content
        return None
# Usage
client = Perplexity()
search_response = client.search.create(query="Python programming")
titles = ResponseUtils.extract_search_titles(search_response)
urls = ResponseUtils.extract_search_urls(search_response)
first_result = ResponseUtils.get_first_search_result(search_response)
print(f"Found {len(titles)} results")
if first_result:
    print(f"First result: {first_result.title}")

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#custom-response-mappers)
Custom Response Mappers
Create typed mappers for domain-specific data structures:
Python
TypeScript/JavaScript
Copy
Ask AI
```
from typing import List, Optional, Dict, Any
from dataclasses import dataclass
from perplexity.types import SearchCreateResponse, SearchResult
@dataclass
class SimplifiedSearchResult:
    title: str
    url: str
    snippet: str
    domain: str
@dataclass
class SearchSummary:
    query: str
    total_results: int
    results: List[SimplifiedSearchResult]
    domains: List[str]
class SearchResponseMapper:
    @staticmethod
    def to_simplified(response: SearchCreateResponse) -> SearchSummary:
        """Convert API response to simplified domain model"""
        simplified_results = []
        domains = set()
        for result in response.results:
            if result.title and result.url and result.snippet:
                # Extract domain from URL
                try:
                    from urllib.parse import urlparse
                    domain = urlparse(result.url).netloc
                    domains.add(domain)
                    simplified_results.append(SimplifiedSearchResult(
                        title=result.title,
                        url=result.url,
                        snippet=result.snippet,
                        domain=domain
                    ))
                except Exception:
                    # Skip invalid URLs
                    continue
        return SearchSummary(
            query=response.query,
            total_results=len(simplified_results),
            results=simplified_results,
            domains=list(domains)
        )
# Usage with type safety
client = Perplexity()
api_response = client.search.create(query="machine learning frameworks")
summary: SearchSummary = SearchResponseMapper.to_simplified(api_response)
print(f"Query: {summary.query}")
print(f"Results: {summary.total_results}")
print(f"Unique domains: {len(summary.domains)}")

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#ide-integration)
IDE Integration
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#enhanced-development-experience)
Enhanced Development Experience
Maximize IDE support with proper type usage:
Python
TypeScript/JavaScript
Copy
Ask AI
```
from perplexity import Perplexity
from perplexity.types import SearchCreateResponse
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # Import types only for type checking (no runtime cost)
    from perplexity.types import ChatCompletionCreateResponse
class EnhancedClient:
    def __init__(self):
        self.client = Perplexity()
    def search(self, query: str, **kwargs) -> SearchCreateResponse:
        """
        Perform search with full type hints
        Args:
            query: Search query string
            **kwargs: Additional search parameters
        Returns:
            SearchCreateResponse: Typed search results
        """
        return self.client.search.create(query=query, **kwargs)
    def chat(self, message: str, model: str = "llama-3.1-sonar-small-128k-online") -> "ChatCompletionCreateResponse":
        """
        Chat completion with type hints
        Args:
            message: User message
            model: Model to use for completion
        Returns:
            ChatCompletionCreateResponse: Typed chat response
        """
        return self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": message}]
        )
# Usage with full IDE support
enhanced_client = EnhancedClient()
# IDE provides full autocomplete and type checking
search_result = enhanced_client.search("Python tutorials")
print(search_result.results[0].title)  # Full intellisense available
chat_result = enhanced_client.chat("Explain decorators")
print(chat_result.choices[0].message.content)  # Type-safe access

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#type-safety-best-practices)
Type Safety Best Practices
1
Always use type imports
Import and use specific types for better IDE support and error catching.
Python
TypeScript/JavaScript
Copy
Ask AI
```
# Good: Specific type imports
from perplexity.types import SearchCreateResponse, SearchResult
def process_search(response: SearchCreateResponse) -> List[str]:
    return [result.title for result in response.results]

```

2
Use type guards for runtime safety
Implement proper type checking for dynamic data.
TypeScript types are compile-time only. Use type guards for runtime validation.
3
Leverage generic types
Create reusable typed functions and classes for common patterns.
Generic types help maintain type safety while providing flexibility.
4
Document with types
Use type annotations as documentation for better code maintainability.
Python
TypeScript/JavaScript
Copy
Ask AI
```
def analyze_search_results(
    response: SearchCreateResponse,
    min_score: float = 0.5
) -> Dict[str, Any]:
    """
    Analyze search results with scoring
    Args:
        response: Search API response
        min_score: Minimum quality score threshold
    Returns:
        Analysis results with scores and recommendations
    """
    # Implementation with type safety

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-type-safety#related-resources)
Related Resources
## [Error Handling Type-safe error handling patterns ](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling)## [Best Practices Type safety in production code ](https://docs.perplexity.ai/guides/perplexity-sdk-best-practices)
