# Source: https://docs.perplexity.ai/guides/sec-guide

The `search_mode: "sec"` parameter allows you to tailor your searches specifically to U.S. Securities and Exchange Commission (SEC) filings, prioritizing official financial documents, disclosures, and regulatory filings from public companies.
## 
[​](https://docs.perplexity.ai/guides/sec-guide#overview)
Overview
The SEC filter allows users to target their searches specifically to official SEC filings. This is especially useful for investors, analysts, journalists, and professionals who require authoritative financial documents, such as 10-Ks, 10-Qs, 8-Ks, and other regulatory filings, rather than general web content or news articles. When you activate the SEC filter by setting `search_mode: "sec"`, Perplexity limits results to the SEC’s EDGAR database and other reputable sources of regulatory filings, filtering out non-official or general web sources. This ensures that the answers you receive are grounded in official disclosures and regulatory compliance.
## 
[​](https://docs.perplexity.ai/guides/sec-guide#key-features-and-functionality)
Key Features and Functionality
  * **Source Filtering** : Prioritizes SEC filings such as 10-K, 10-Q, 8-K, S-1, and more
  * **Regulatory Focus** : Returns results based on official financial and regulatory documents
  * **Enhanced Precision** : Provides more accurate and up-to-date information for financial and compliance queries


## 
[​](https://docs.perplexity.ai/guides/sec-guide#usage-examples)
Usage Examples
### 
[​](https://docs.perplexity.ai/guides/sec-guide#basic-sec-filings-search)
Basic SEC Filings Search
This example shows how to perform a basic search using the SEC filter.
cURL
Python
Node.js
Copy
Ask AI
```
curl --request POST \
  --url https://api.perplexity.ai/chat/completions \
  --header "accept: application/json" \
  --header "authorization: Bearer $SONAR_API_KEY" \
  --header "content-type: application/json" \
  --data '{
    "model": "sonar-pro",
    "messages": [{"role": "user", "content": "Prepare me for markets opening."}],
    "search_mode": "sec"
  }' | jq

```

### 
[​](https://docs.perplexity.ai/guides/sec-guide#combining-sec-mode-with-other-parameters)
Combining SEC Mode with Other Parameters
You can combine the SEC filter with other parameters for more refined searches:
cURL
Python
TypeScript
Copy
Ask AI
```
curl --request POST \
  --url https://api.perplexity.ai/chat/completions \
  --header "accept: application/json" \
  --header "authorization: Bearer $SONAR_API_KEY" \
  --header "content-type: application/json" \
  --data '{
    "model": "sonar",
    "messages": [{"role": "user", "content": "Summarize the latest 10-K filings for Apple Inc."}],
    "stream": false,
    "search_mode": "sec",
    "search_after_date_filter": "1/1/2023"
}' | jq

```

## 
[​](https://docs.perplexity.ai/guides/sec-guide#recommended-use-cases)
Recommended Use Cases
The SEC filter is particularly valuable for:
  1. **Financial Analysis** : When you need to review official financial statements and disclosures
  2. **Regulatory Compliance** : For questions requiring up-to-date regulatory filings and compliance information
  3. **Market Research** : When tracking company events, earnings, and risk factors
  4. **Due Diligence** : For investors and analysts evaluating public companies


## 
[​](https://docs.perplexity.ai/guides/sec-guide#best-practices)
Best Practices
### 
[​](https://docs.perplexity.ai/guides/sec-guide#optimizing-sec-filings-searches)
Optimizing SEC Filings Searches
  * **Be Specific** : Reference the type of filing (e.g., 10-K, 8-K) and company name for more precise results
  * **Use Financial Terminology** : Include terms like “earnings,” “risk factors,” or “management discussion” to target relevant sections
  * **Combine with Date Filters** : For the most recent filings, combine with `search_after_date_filter`
  * **Adjust Context Size** : Use higher `search_context_size` values for more comprehensive responses


### 
[​](https://docs.perplexity.ai/guides/sec-guide#limitations)
Limitations
  * Availability is limited to filings made public through the SEC’s EDGAR system
  * Some filings may be delayed or amended after initial publication
  * Only covers U.S. public companies and registered entities

⸻
