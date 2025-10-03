# Source: https://docs.perplexity.ai/guides/date-range-filter-guide

The `search_after_date_filter` and `search_before_date_filter` parameters allow you to restrict search results to a specific publication date range. Only results with publication dates falling between these dates will be returned.The `last_updated_after_filter` and `last_updated_before_filter` parameters allow you to filter by when content was last modified or updated, rather than when it was originally published.The `search_recency_filter` parameter provides a convenient way to filter results by predefined time periods (e.g., “day”, “week”, “month”, “year”) relative to the current date.
Specific date filters must be provided in the “%m/%d/%Y” format (e.g., “3/1/2025”). Recency filters use predefined values like “day”, “week”, “month”, or “year”. All filters are optional—you may supply either specific dates or recency filters as needed.
## 
[​](https://docs.perplexity.ai/guides/date-range-filter-guide#overview)
Overview
Date and time filters allow you to control which search results are returned by limiting them to specific time periods. There are three types of date and time filters available:
### 
[​](https://docs.perplexity.ai/guides/date-range-filter-guide#publication-date-filters)
Publication Date Filters
The `search_after_date_filter` and `search_before_date_filter` parameters filter results based on when content was **originally created or published**. This is useful when you need to:
  * Find content published within a specific timeframe
  * Exclude outdated or overly recent publications
  * Focus on content from a particular publication period


### 
[​](https://docs.perplexity.ai/guides/date-range-filter-guide#last-updated-date-filters)
Last Updated Date Filters
The `last_updated_after_filter` and `last_updated_before_filter` parameters filter results based on when content was **last modified or updated**. This is useful when you need to:
  * Find recently updated or maintained content
  * Exclude stale content that hasn’t been updated recently
  * Focus on content that has been refreshed within a specific period


### 
[​](https://docs.perplexity.ai/guides/date-range-filter-guide#search-recency-filter)
Search Recency Filter
The `search_recency_filter` parameter provides a simple way to filter results by predefined time periods relative to the current date. This is useful when you need to:
  * Find content from the past day, week, month, or year
  * Get recent results without specifying exact dates
  * Quickly filter for timely information

**Available values:**
  * `"day"` - Content from the past 24 hours
  * `"week"` - Content from the past 7 days
  * `"month"` - Content from the past 30 days
  * `"year"` - Content from the past 365 days

**Important:** These filter types target different dates—publication filters use the original creation/publication date, while last updated filters use the modification date, and recency filters use a relative time period from the current date. To constrain search results by publication date:
Copy
Ask AI
```
"search_after_date_filter": "3/1/2025",
"search_before_date_filter": "3/5/2025"

```

To constrain search results by last updated date:
Copy
Ask AI
```
"last_updated_after_filter": "3/1/2025",
"last_updated_before_filter": "3/5/2025"

```

To constrain search results by recency:
Copy
Ask AI
```
"search_recency_filter": "week"

```

These filters will be applied in addition to any other search parameters (for example, domain filters).
## 
[​](https://docs.perplexity.ai/guides/date-range-filter-guide#examples)
Examples
**1. Limiting Results by Publication Date Range** This example limits search results to content published between March 1, 2025, and March 5, 2025. **Request Example**
Python
TypeScript
cURL
Copy
Ask AI
```
from perplexity import Perplexity
client = Perplexity()
completion = client.chat.completions.create(
    model="sonar",
    messages=[
        {"role": "system", "content": "You are an expert on current events."},
        {"role": "user", "content": "Show me tech news published this week."}
    ],
    search_after_date_filter="3/1/2025",
    search_before_date_filter="3/5/2025"
)
print(completion.choices[0].message.content)

```

**2. Filtering with a Single Publication Date Parameter** If you only wish to restrict the results to those published on or after a specific date, include just the `search_after_date_filter`:
Copy
Ask AI
```
payload = {
    "model": "sonar-pro",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Show me news articles published after March 1, 2025."}
    ],
    "search_after_date_filter": "3/1/2025"
}

```

**3. Filtering by Last Updated Date Range** This example limits search results to content that was last updated between March 1, 2025, and March 5, 2025. This is useful for finding recently maintained or refreshed content. **Request Example**
Python
TypeScript
cURL
Copy
Ask AI
```
from perplexity import Perplexity
client = Perplexity()
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[
        {"role": "system", "content": "You are an expert on current events."},
        {"role": "user", "content": "Show me recently updated tech articles."}
    ],
    last_updated_after_filter="3/1/2025",
    last_updated_before_filter="3/5/2025"
)
print(completion.choices[0].message.content)

```

**4. Combining Publication and Last Updated Filters** You can combine both filter types to find content that was published in one timeframe and updated in another:
Copy
Ask AI
```
payload = {
    "model": "sonar-pro",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Show me articles published last year but updated recently."}
    ],
    "search_after_date_filter": "1/1/2024",
    "search_before_date_filter": "12/31/2024",
    "last_updated_after_filter": "3/1/2025"
}

```

**5. Using Search Recency Filter** The `search_recency_filter` provides a convenient way to filter results by predefined time periods without specifying exact dates:
Python
TypeScript
cURL
Copy
Ask AI
```
from perplexity import Perplexity
client = Perplexity()
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[
        {"role": "system", "content": "You are an expert on current events."},
        {"role": "user", "content": "What are the latest AI developments?"}
    ],
    search_recency_filter="week"
)
print(completion.choices[0].message.content)

```

This example will return only content from the past 7 days, automatically calculated from the current date.
## 
[​](https://docs.perplexity.ai/guides/date-range-filter-guide#best-practices)
Best Practices
**Date Format**
  * Strict Format: Dates must match the “%m/%d/%Y” format exactly. For example, the date “3/1/2025” or “03/01/2025” is acceptable.
  * Consistency: Use one or both filters consistently based on your search needs. Combining both provides a clear range.

**Filter Selection**
  * Choose the Right Filter Type: Use publication date filters (`search_after_date_filter`/`search_before_date_filter`) when you care about when content was originally created. Use last updated filters (`last_updated_after_filter`/`last_updated_before_filter`) when you need recently maintained content. Use recency filters (`search_recency_filter`) for quick, relative time filtering.
  * Recency vs. Exact Dates: Use `search_recency_filter` for convenience when you want recent content (e.g., “past week”). Use specific date filters when you need precise control over the time range.
  * Combining Filters: You can use both publication and last updated filters together to find content that meets both criteria (e.g., published in 2024 but updated recently). Note that `search_recency_filter` cannot be combined with other date filters.

**Client-Side Validation**
  * Regex Check: Validate date strings on the client side (or via the API) using a regex such as:


Copy
Ask AI
```
date_regex='^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/[0-9]{4}$'

```

This ensures that dates conform to the required format before sending the request. **Performance Considerations**
  * Narrowing the Search: Applying date range filters typically reduces the number of results, which may improve response times and result relevance.
  * Avoid Over-Restriction: Ensure that the date range is neither too narrow (limiting useful results) nor too broad (defeating the purpose of the filter).

⸻
## 
[​](https://docs.perplexity.ai/guides/date-range-filter-guide#last-updated-date-filters-2)
Last Updated Date Filters
The `last_updated_after_filter` and `last_updated_before_filter` parameters provide powerful filtering capabilities based on when content was last modified or updated, rather than when it was originally published. This is particularly useful for finding recently maintained, refreshed, or updated content.
### 
[​](https://docs.perplexity.ai/guides/date-range-filter-guide#parameters)
Parameters
**`last_updated_after_filter`**
  * Filters search results to only include content last updated after this date
  * Format should be %m/%d/%Y (e.g. 3/1/2025)
  * Optional parameter

**`last_updated_before_filter`**
  * Filters search results to only include content last updated before this date
  * Format should be %m/%d/%Y (e.g. 3/1/2025)
  * Optional parameter


### 
[​](https://docs.perplexity.ai/guides/date-range-filter-guide#use-cases)
Use Cases
**Content Freshness** : Find articles, documentation, or resources that have been recently updated to ensure you’re getting the most current information. **Maintenance Tracking** : Identify which content has been actively maintained within a specific timeframe. **Quality Assurance** : Focus on content that has been refreshed recently, which often indicates higher quality and relevance.
### 
[​](https://docs.perplexity.ai/guides/date-range-filter-guide#code-examples)
Code Examples
**1. Find Recently Updated Content (After a Specific Date)**
cURL
python
javascript
Copy
Ask AI
```
curl --location 'https://api.perplexity.ai/chat/completions' \
  --header "Authorization: Bearer $SONAR_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "sonar-pro",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant focused on current information."},
      {"role": "user", "content": "Find me documentation that has been updated recently."}
    ],
    "last_updated_after_filter": "1/1/2025"
}' | jq

```

**2. Find Content Updated Within a Specific Window**
cURL
python
Copy
Ask AI
```
curl --location 'https://api.perplexity.ai/chat/completions' \
  --header "Authorization: Bearer $SONAR_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "sonar-pro",
    "messages": [
      {"role": "system", "content": "You are an expert on technology trends."},
      {"role": "user", "content": "Show me tech articles that were updated last week."}
    ],
    "last_updated_after_filter": "2/24/2025",
    "last_updated_before_filter": "3/3/2025"
}' | jq

```

**3. Exclude Recently Updated Content (Before a Date)**
cURL
python
Copy
Ask AI
```
curl --location 'https://api.perplexity.ai/chat/completions' \
  --header "Authorization: Bearer $SONAR_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "sonar-pro",
    "messages": [
      {"role": "system", "content": "You are a research assistant."},
      {"role": "user", "content": "Find historical content that hasn'\''t been updated recently."}
    ],
    "last_updated_before_filter": "1/1/2024"
}' | jq

```

### 
[​](https://docs.perplexity.ai/guides/date-range-filter-guide#advanced-usage-patterns)
Advanced Usage Patterns
**Combining with Domain Filters**
Copy
Ask AI
```
payload = {
    "model": "sonar-pro",
    "messages": [
        {"role": "user", "content": "Latest updates on AI research."}
    ],
    "search_domain_filter": ["arxiv.org", "openai.com"],
    "last_updated_after_filter": "2/1/2025"
}

```

**Finding Maintained vs. Stale Content**
Copy
Ask AI
```
# Find actively maintained content
recent_payload = {
    "model": "sonar-pro",
    "messages": [
        {"role": "user", "content": "Current best practices for React development."}
    ],
    "last_updated_after_filter": "1/1/2025"
}
# Find potentially outdated content
stale_payload = {
    "model": "sonar-pro",
    "messages": [
        {"role": "user", "content": "React development practices."}
    ],
    "last_updated_before_filter": "1/1/2023"
}

```

### 
[​](https://docs.perplexity.ai/guides/date-range-filter-guide#tips-for-last-updated-filters)
Tips for Last Updated Filters
  1. **Content Freshness Strategy** : Use `last_updated_after_filter` when you need the most current information on rapidly evolving topics.
  2. **Quality Indicator** : Recently updated content often indicates active maintenance and higher reliability.
  3. **Research Applications** : Combine with publication date filters to find content published years ago but updated recently, indicating ongoing relevance.
  4. **Performance** : These filters can significantly improve response relevance by focusing on maintained content.
  5. **Date Selection** : Choose update date ranges based on your content type - technical documentation might need monthly updates, while academic papers might be updated annually.


