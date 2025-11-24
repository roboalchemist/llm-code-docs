# Source: https://docs.perplexity.ai/guides/search-control-guide

## 
[​](https://docs.perplexity.ai/guides/search-control-guide#overview)
Overview
Sonar models provide powerful web search capabilities, but there are times when you want to control when and how searches are performed. Perplexity offers two main approaches for search control:
  * **Search Classifier** - Let AI intelligently decide when to search based on the query context
  * **Disable Search** - Turn off web search completely for specific requests


Search control is available across all Sonar models.
Pricing remains the same regardless of whether search is triggered or not. Search control features are designed for performance optimization and user experience, not cost reduction.
## 
[​](https://docs.perplexity.ai/guides/search-control-guide#search-classifier)
Search Classifier
The search classifier is a trained model that automatically determines whether a web search is necessary based on the context and content of your query. This helps optimize performance and costs by only searching when beneficial.
### 
[​](https://docs.perplexity.ai/guides/search-control-guide#how-it-works)
How It Works
The classifier analyzes your query and decides whether:
  * **Search is needed** - For questions requiring current information, facts, or research
  * **Search is unnecessary** - For creative tasks, math problems, or general knowledge that doesn’t require real-time data


### 
[​](https://docs.perplexity.ai/guides/search-control-guide#when-to-use-search-classifier)
When to Use Search Classifier
Use the search classifier when you want to:
  * **Improve response speed** - Skip search for queries that don’t benefit from it
  * **Automatic intelligence** - Let AI decide the best approach for each query
  * **Optimal user experience** - Ensure search is only used when it adds value


  * Python
  * TypeScript
  * cURL


Copy
Ask AI
```
import requests
# API configuration
API_URL = "https://api.perplexity.ai/chat/completions"
API_KEY = "your-api-key-here"
headers = {
    "accept": "application/json",
    "authorization": f"Bearer {API_KEY}",
    "content-type": "application/json"
}
# Query that benefits from search classifier
user_query = "What are the latest developments in quantum computing?"
payload = {
    "model": "sonar-pro",
    "messages": [{"role": "user", "content": user_query}],
    "stream": False,
    "enable_search_classifier": True
}
response = requests.post(API_URL, json=payload, headers=headers)
print(response.json())

```

### 
[​](https://docs.perplexity.ai/guides/search-control-guide#search-classifier-examples)
Search Classifier Examples
Queries that typically trigger search
  * “What happened in the stock market today?”
  * “Latest news about renewable energy”
  * “Current weather in San Francisco”
  * “Recent research on machine learning”


Queries that typically skip search
  * “What is 2 + 2?”
  * “Write a creative story about a dragon”
  * “Explain the concept of recursion”
  * “Generate a business name for a bakery”


## 
[​](https://docs.perplexity.ai/guides/search-control-guide#disabling-search-completely)
Disabling Search Completely
For certain use cases, you may want to disable web search entirely. This is useful when:
  * **Offline-like responses** - Get responses based only on training data
  * **Creative tasks** - Focus on generation without external influence
  * **Deterministic responses** - Ensure consistent outputs based only on training data


### 
[​](https://docs.perplexity.ai/guides/search-control-guide#implementation)
Implementation
To disable search completely, set the `disable_search` parameter to `true`:
  * Python
  * TypeScript
  * cURL


Copy
Ask AI
```
import requests
# API configuration
API_URL = "https://api.perplexity.ai/chat/completions"
API_KEY = "your-api-key-here"
headers = {
    "accept": "application/json",
    "authorization": f"Bearer {API_KEY}",
    "content-type": "application/json"
}
# Query that doesn't need web search
user_query = "What is 2 + 2?"
payload = {
    "model": "sonar-pro",
    "messages": [{"role": "user", "content": user_query}],
    "stream": False,
    "disable_search": True
}
response = requests.post(API_URL, json=payload, headers=headers)
print(response.json())

```

When search is disabled, responses will be based solely on the model’s training data and may not include the most current information.
## 
[​](https://docs.perplexity.ai/guides/search-control-guide#comparison-and-best-practices)
Comparison and Best Practices
### 
[​](https://docs.perplexity.ai/guides/search-control-guide#when-to-use-each-approach)
When to Use Each Approach
## Search Classifier
**Best for:**
  * Mixed workloads with varying query types
  * Performance optimization without manual intervention
  * General-purpose applications
  * Unknown query patterns


## Disabled Search
**Best for:**
  * Creative content generation
  * Mathematical computations
  * Sensitive data processing
  * Offline-like experiences


### 
[​](https://docs.perplexity.ai/guides/search-control-guide#performance-considerations)
Performance Considerations
  * Response Time
  * Information Accuracy


**Search Classifier:** Variable response time depending on whether search is triggered**Disabled Search:** Consistently faster responses since no search operations occur
## 
[​](https://docs.perplexity.ai/guides/search-control-guide#complete-examples)
Complete Examples
### 
[​](https://docs.perplexity.ai/guides/search-control-guide#search-classifier-in-action)
Search Classifier in Action
1
Set up the request with search classifier
Copy
Ask AI
```
payload = {
    "model": "sonar-pro",
    "messages": [{"role": "user", "content": "Explain machine learning"}],
    "enable_search_classifier": True
}

```

The classifier will likely skip search for this general concept explanation.
2
Try with a current events query
Copy
Ask AI
```
payload = {
    "model": "sonar-pro", 
    "messages": [{"role": "user", "content": "Latest AI news this week"}],
    "enable_search_classifier": True
}

```

The classifier will trigger search for this time-sensitive query.
### 
[​](https://docs.perplexity.ai/guides/search-control-guide#creative-task-with-disabled-search)
Creative Task with Disabled Search
Here’s an example of using disabled search for creative content generation:
Copy
Ask AI
```
import requests
payload = {
    "model": "sonar-pro",
    "messages": [
        {
            "role": "user", 
            "content": "Write a short science fiction story about time travel"
        }
    ],
    "disable_search": True,
    "temperature": 0.8
}
response = requests.post(
    "https://api.perplexity.ai/chat/completions",
    headers={
        "authorization": "Bearer your-api-key-here",
        "content-type": "application/json"
    },
    json=payload
)

```

## 
[​](https://docs.perplexity.ai/guides/search-control-guide#troubleshooting)
Troubleshooting
Search classifier not working as expected
**Common causes:**
  * API key doesn’t have access to classifier features
  * Using an unsupported model
  * Incorrect parameter syntax

**Solutions:**
  * Verify your API key permissions
  * Ensure you’re using a Sonar model
  * Check parameter spelling: `enable_search_classifier`


Responses seem outdated with disabled search
This is expected behavior when search is disabled. The model can only use information from its training data.**Solutions:**
  * Re-enable search for queries requiring current information
  * Use search classifier for automatic optimization
  * Clearly document when search is disabled for your users


Start with the search classifier for most applications, then selectively disable search for specific use cases where you want guaranteed offline-like behavior.
