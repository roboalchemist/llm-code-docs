# Source: https://docs.perplexity.ai/api-reference/search-post

#### Authorizations
[​](https://docs.perplexity.ai/api-reference/search-post#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Body
application/json
[​](https://docs.perplexity.ai/api-reference/search-post#body-query)
query
string string[]
required
The search query or queries to execute. A search query. Can be a single query or a list of queries for multi-query search.
Example:
`"latest AI developments 2024"`
[​](https://docs.perplexity.ai/api-reference/search-post#body-max-results)
max_results
integer
default:10
The maximum number of search results to return.
Required range: `1 <= x <= 20`
[​](https://docs.perplexity.ai/api-reference/search-post#body-max-tokens-per-page)
max_tokens_per_page
integer
default:1024
Controls the maximum number of tokens retrieved from each webpage during search processing. Higher values provide more comprehensive content extraction but may increase processing time.
Example:
`1024`
[​](https://docs.perplexity.ai/api-reference/search-post#body-country)
country
string
Country code to filter search results by geographic location (e.g., 'US', 'GB', 'DE').
Example:
`"US"`
#### Response
200 - application/json
Successfully retrieved search results.
[​](https://docs.perplexity.ai/api-reference/search-post#response-results)
results
SearchResult · object[]
required
An array of search results.
Show child attributes
