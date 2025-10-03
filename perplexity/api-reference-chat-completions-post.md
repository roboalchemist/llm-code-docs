# Source: https://docs.perplexity.ai/api-reference/chat-completions-post

#### Authorizations
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Body
application/json
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-model)
model
enum<string>
required
The name of the model that will complete your prompt. Choose from our available Sonar models: sonar (lightweight search), sonar-pro (advanced search), sonar-deep-research (exhaustive research), sonar-reasoning (fast reasoning), or sonar-reasoning-pro (premier reasoning).
Available options:
`sonar`,
`sonar-pro`,
`sonar-deep-research`,
`sonar-reasoning`,
`sonar-reasoning-pro`
Example:
`"sonar-deep-research"`
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-messages)
messages
Message · object[]
required
A list of messages comprising the conversation so far.
Show child attributes
Example:
```
[  
  {  
    "role": "system",  
    "content": "Be precise and concise."  
  },  
  {  
    "role": "user",  
    "content": "How many stars are there in our galaxy?"  
  }  
]
```

[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-search-mode)
search_mode
enum<string>
default:web
Controls search mode: 'academic' prioritizes scholarly sources, 'sec' prioritizes SEC filings, 'web' uses general web search. See [academic guide](https://docs.perplexity.ai/guides/academic-filter-guide) and [SEC guide](https://docs.perplexity.ai/guides/sec-guide).
Available options:
`academic`,
`sec`,
`web`
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-reasoning-effort)
reasoning_effort
enum<string>
**Perplexity-Specific** : Controls how much computational effort the AI dedicates to each query for deep research models. 'low' provides faster, simpler answers with reduced token usage, 'medium' offers a balanced approach, and 'high' delivers deeper, more thorough responses with increased token usage. This parameter directly impacts the amount of reasoning tokens consumed. **WARNING: This parameter is ONLY applicable for sonar-deep-research.** Defaults to 'medium' when used with sonar-deep-research.
Available options:
`low`,
`medium`,
`high`
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-max-tokens)
max_tokens
integer
**OpenAI Compatible** : The maximum number of completion tokens returned by the API. Controls the length of the model's response. If the response would exceed this limit, it will be truncated. Higher values allow for longer responses but may increase processing time and costs.
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-temperature)
temperature
number
default:0.2
The amount of randomness in the response, valued between 0 and 2. Lower values (e.g., 0.1) make the output more focused, deterministic, and less creative. Higher values (e.g., 1.5) make the output more random and creative. Use lower values for factual/information retrieval tasks and higher values for creative applications.
Required range: `0 <= x < 2`
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-top-p)
top_p
number
default:0.9
**OpenAI Compatible** : The nucleus sampling threshold, valued between 0 and 1. Controls the diversity of generated text by considering only the tokens whose cumulative probability exceeds the top_p value. Lower values (e.g., 0.5) make the output more focused and deterministic, while higher values (e.g., 0.95) allow for more diverse outputs. Often used as an alternative to temperature.
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-search-domain-filter)
search_domain_filter
any[]
A list of domains to limit search results to. Currently limited to 20 domains for Allowlisting and Denylisting. For Denylisting, add a `-` at the beginning of the domain string. More information about this [here](https://docs.perplexity.ai/guides/search-domain-filters).
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-return-images)
return_images
boolean
default:false
**Perplexity-Specific** : Determines whether search results should include images.
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-return-related-questions)
return_related_questions
boolean
default:false
**Perplexity-Specific** : Determines whether related questions should be returned.
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-search-recency-filter)
search_recency_filter
string
**Perplexity-Specific** : Filters search results based on time (e.g., 'week', 'day').
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-search-after-date-filter)
search_after_date_filter
string
**Perplexity-Specific** : Filters search results to only include content published after this date. Format should be %m/%d/%Y (e.g. 3/1/2025)
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-search-before-date-filter)
search_before_date_filter
string
**Perplexity-Specific** : Filters search results to only include content published before this date. Format should be %m/%d/%Y (e.g. 3/1/2025)
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-last-updated-after-filter)
last_updated_after_filter
string
**Perplexity-Specific** : Filters search results to only include content last updated after this date. Format should be %m/%d/%Y (e.g. 3/1/2025)
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-last-updated-before-filter)
last_updated_before_filter
string
**Perplexity-Specific** : Filters search results to only include content last updated before this date. Format should be %m/%d/%Y (e.g. 3/1/2025)
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-top-k)
top_k
number
default:0
**OpenAI Compatible** : The number of tokens to keep for top-k filtering. Limits the model to consider only the k most likely next tokens at each step. Lower values (e.g., 20) make the output more focused and deterministic, while higher values allow for more diverse outputs. A value of 0 disables this filter. Often used in conjunction with top_p to control output randomness.
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-stream)
stream
boolean
default:false
**OpenAI Compatible** : Determines whether to stream the response incrementally.
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-presence-penalty)
presence_penalty
number
default:0
**OpenAI Compatible** : Positive values increase the likelihood of discussing new topics. Applies a penalty to tokens that have already appeared in the text, encouraging the model to talk about new concepts. Values typically range from 0 (no penalty) to 2.0 (strong penalty). Higher values reduce repetition but may lead to more off-topic text.
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-frequency-penalty)
frequency_penalty
number
default:0
**OpenAI Compatible** : Decreases likelihood of repetition based on prior frequency. Applies a penalty to tokens based on how frequently they've appeared in the text so far. Values typically range from 0 (no penalty) to 2.0 (strong penalty). Higher values (e.g., 1.5) reduce repetition of the same words and phrases. Useful for preventing the model from getting stuck in loops.
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-response-format)
response_format
object
Enables structured JSON output formatting.
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-disable-search)
disable_search
boolean
default:false
**Perplexity-Specific** : When set to true, disables web search completely and the model will only use its training data to respond. This is useful when you want deterministic responses without external information. More information about this [here](https://docs.perplexity.ai/guides/search-control-guide#disabling-search-completely).
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-enable-search-classifier)
enable_search_classifier
boolean
default:false
**Perplexity-Specific** : Enables a classifier that decides if web search is needed based on your query. See more [here](https://docs.perplexity.ai/guides/search-control-guide#search-classifier).
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-web-search-options)
web_search_options
object
**Perplexity-Specific** : Configuration for using web search in model responses.
Show child attributes
Example:
```
{ "search_context_size": "high" }
```

[​](https://docs.perplexity.ai/api-reference/chat-completions-post#body-media-response)
media_response
object
**Perplexity-Specific** : Configuration for controlling media content in responses, such as videos and images. Use the overrides property to enable specific media types.
Show child attributes
Example:
```
{  
  "overrides": {  
    "return_videos": true,  
    "return_images": true  
  }  
}
```

#### Response
200
application/json
OK
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#response-id)
id
string
required
A unique identifier for the chat completion.
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#response-model)
model
string
required
The model that generated the response.
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#response-created)
created
integer
required
The Unix timestamp (in seconds) of when the chat completion was created.
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#response-usage)
usage
object
required
Show child attributes
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#response-object)
object
string
default:chat.completion
required
The type of object, which is always `chat.completion`.
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#response-choices)
choices
ChatCompletionsChoice · object[]
required
A list of chat completion choices. Can be more than one if `n` is greater than 1.
Show child attributes
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#response-search-results)
search_results
ApiPublicSearchResult · object[] | null
A list of search results related to the response.
Show child attributes
[​](https://docs.perplexity.ai/api-reference/chat-completions-post#response-videos)
videos
VideoResult · object[] | null
A list of video results when media_response.overrides.return_videos is enabled. Contains video URLs and metadata.
Show child attributes
