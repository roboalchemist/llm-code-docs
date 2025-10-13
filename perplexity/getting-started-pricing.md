# Source: https://docs.perplexity.ai/getting-started/pricing

This page shows **pricing information** to help you understand API costs. For **billing setup** , payment methods, and usage monitoring, visit the [Admin section](https://docs.perplexity.ai/getting-started/api-groups).
## 
[​](https://docs.perplexity.ai/getting-started/pricing#search-api-pricing)
Search API Pricing
API | Price per 1K requests | Description  
---|---|---  
**Search API** | $5.00 | Raw web search results with advanced filtering  
**No token costs:** Search API charges per request only, with no additional token-based pricing.
## 
[​](https://docs.perplexity.ai/getting-started/pricing#grounded-llm-pricing)
Grounded LLM Pricing
**Total cost per query** = Token costs + Request fee (varies by search context size, applies to Sonar, Sonar Pro, Sonar Reasoning, and Sonar Reasoning Pro models only)
  * Token Pricing
  * Request Pricing


## 
[​](https://docs.perplexity.ai/getting-started/pricing#token-pricing)
Token Pricing
**Token pricing** is based on the number of tokens in your request and response. Model | Input Tokens ($/1M) | Output Tokens ($/1M) | Citation Tokens ($/1M) | Search Queries ($/1K) | Reasoning Tokens ($/1M)  
---|---|---|---|---|---  
**Sonar** | $1 | $1 | - | - | -  
**Sonar Pro** | $3 | $15 | - | - | -  
**Sonar Reasoning** | $1 | $5 | - | - | -  
**Sonar Reasoning Pro** | $2 | $8 | - | - | -  
**Sonar Deep Research** | $2 | $8 | $2 | $5 | $3  
Token and Cost Glossary
### 
[​](https://docs.perplexity.ai/getting-started/pricing#input-tokens)
Input Tokens
The number of tokens in your prompt or message to the API. This includes:
  * Your question or instruction
  * Any context or examples you provide
  * System messages and formatting

**Example:** “What is the weather in New York?” = ~8 input tokens
### 
[​](https://docs.perplexity.ai/getting-started/pricing#output-tokens)
Output Tokens
The number of tokens in the API’s response. This includes:
  * The generated answer or content
  * Any explanations or additional context
  * Search results and references

**Example:** “The weather in New York is currently sunny with a temperature of 72°F.” = ~15 output tokens
### 
[​](https://docs.perplexity.ai/getting-started/pricing#citation-tokens)
Citation Tokens
Tokens used specifically for generating search results and references in responses. Only applies to **Sonar Deep Research** model.**Example:** Including source links, reference numbers, and bibliographic information
### 
[​](https://docs.perplexity.ai/getting-started/pricing#search-context-size-vs-context-window)
Search Context Size vs Context Window
**Search context size** is _not_ the same as the **context window**.
  * **Search context size** : How much web information is retrieved during search (affects request pricing)
  * **Context window** : Maximum tokens the model can process in one request (affects token limits)


### 
[​](https://docs.perplexity.ai/getting-started/pricing#search-queries)
Search Queries
The number of individual searches conducted by **Sonar Deep Research** during query processing. This is separate from your initial user query.
  * The model automatically determines how many searches are needed
  * You cannot control the exact number of search queries
  * The `reasoning_effort` parameter influences the number of searches performed
  * Only applies to **Sonar Deep Research** model


### 
[​](https://docs.perplexity.ai/getting-started/pricing#reasoning-tokens)
Reasoning Tokens
Tokens used for step-by-step logical reasoning and problem-solving. Only applies to **Sonar Deep Research** model.**Example:** Breaking down a complex math problem into sequential steps with explanations
**Token Calculation:** 1 token ≈ 4 characters in English text. The exact count may vary based on language and content complexity.
## 
[​](https://docs.perplexity.ai/getting-started/pricing#cost-examples)
Cost Examples
## Sonar Web Search Example
**Sonar** • 500 input + 200 output tokens
  * Low
  * Medium
  * High


Component | Cost  
---|---  
Input tokens | $0.0005  
Output tokens | $0.0002  
Request fee | $0.005  
**Total** | **$0.0057**  
## Deep Research Example
**Sonar Deep Research**
  * Low
  * Medium
  * High


Component | Cost  
---|---  
Input tokens (33) | $0.000066  
Output tokens (7163) | $0.057304  
Citation tokens (20016) | $0.040032  
Reasoning tokens (73997) | $0.221991  
Search queries (18) | $0.09  
**Total** | **$0.409393**  
## 
[​](https://docs.perplexity.ai/getting-started/pricing#choosing-the-right-api)
Choosing the Right API
### 
[​](https://docs.perplexity.ai/getting-started/pricing#search-api)
Search API
API | Description | Best For  
---|---|---  
**Search API** | Raw web search results with advanced filtering | Custom search engines, research tools, competitive intelligence, news aggregation  
### 
[​](https://docs.perplexity.ai/getting-started/pricing#sonar-models-chat-completions)
Sonar Models (Chat Completions)
Model | Description | Best For  
---|---|---  
**Sonar** | Lightweight, cost-effective search model | Quick facts, news updates, simple Q&A, high-volume applications  
**Sonar Pro** | Advanced search with deeper content understanding | Complex queries, competitive analysis, detailed research  
**Sonar Reasoning** | Quick problem-solving with step-by-step logic and search | Logic puzzles, math problems, transparent reasoning  
**Sonar Reasoning Pro** | Enhanced multi-step reasoning with web search | Complex problem-solving, research analysis, strategic planning  
**Sonar Deep Research** | Exhaustive research and detailed report generation with search | Academic research, market analysis, comprehensive reports  
**Need help choosing?** Use Search API when you want raw data to process yourself. Use Sonar models when you want AI-generated answers with search grounding.
