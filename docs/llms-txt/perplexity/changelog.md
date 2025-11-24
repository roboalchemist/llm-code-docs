# Source: https://docs.perplexity.ai/changelog/changelog.md

# Changelog

<Tip>
  Looking ahead? Check out our [Feature Roadmap](/feature-roadmap) to see what's coming next.
</Tip>

<Update label="September 2025" tags={["File Attachments", "Documents", "API"]}>
  **New: File Attachments Support**

  You can now upload and analyze documents in multiple formats using Sonar models! This powerful new feature supports PDF, DOC, DOCX, TXT, and RTF files, allowing you to ask questions, extract information, and get summaries from your documents.

  **Key capabilities:**

  * **Document Analysis**: Ask questions about document content and get detailed answers
  * **Content Extraction**: Pull out key information, data points, and insights
  * **Multi-format Support**: Work with PDF, Word documents, text files, and Rich Text Format
  * **Large Document Handling**: Process lengthy documents efficiently
  * **Multi-language Support**: Analyze documents in various languages

  Upload documents either via publicly accessible URLs using the `file_url` content type, similar to our existing image upload functionality.

  **Example:**

  ```python  theme={null}
  from perplexity import Perplexity

  client = Perplexity()
  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Summarize this document"},
                  {"type": "file_url", "file_url": {"url": "https://example.com/document.pdf"}}
              ]
          }
      ]
  )
  ```

  Get started with our comprehensive [File Attachments Guide](/guides/file-attachments).
</Update>

<Update label="September 2025" tags={["Search", "Standalone API", "Features"]}>
  **New: Search-only API**

  Introducing our standalone Search API that provides direct access to search results without LLM processing! This new endpoint gives you raw, ranked search results from Perplexity's continuously refreshed index.

  **Perfect for:**

  * Building custom search experiences
  * Integrating search results into your own applications
  * Creating specialized workflows that need search data without AI responses
  * Applications requiring just the search functionality

  **Key features:**

  * Direct access to Perplexity's search index
  * All existing search filters and controls
  * Faster responses since no LLM processing is involved
  * Same powerful filtering options (domain, date range, academic sources, etc.)

  **Example:**

  ```python  theme={null}
  from perplexity import Perplexity

  client = Perplexity()
  search = client.search.create(
      query="latest AI developments 2024",
      max_results=10
  )

  for result in search.results:
      print(f"{result.title}: {result.url}")
  ```

  This complements our existing chat completions API and gives developers more flexibility in how they use Perplexity's search capabilities.

  Learn more in our [Search API documentation](/guides/search-guide).
</Update>

<Update label="September 2025" tags={["Security", "API Keys", "Key Management"]}>
  **New: API Key Rotation Mechanism**

  We've introduced a comprehensive API key rotation system to enhance security and simplify key management for your applications.

  **Key features:**

  * **Seamless Rotation**: Replace API keys without service interruption
  * **Automated Workflows**: Set up automatic key rotation schedules
  * **Enhanced Security**: Regularly refresh keys to minimize security risks
  * **Audit Trail**: Track key usage and rotation history
  * **Zero Downtime**: Smooth transitions between old and new keys

  **How it works:**

  1. Generate a new API key while keeping the old one active
  2. Update your applications to use the new key
  3. Deactivate the old key once migration is complete

  This is particularly valuable for production environments where continuous availability is critical, and for organizations with strict security compliance requirements.

  **Best practices:**

  * Rotate keys every 30-90 days depending on your security requirements
  * Use environment variables to manage keys in your applications
  * Test key rotation in staging environments first
  * Monitor key usage to ensure successful transitions

  Access key rotation features through your [API Portal](https://perplexity.ai/account/api).
</Update>

<Update label="August 2025" tags={["Models", "Deprecation", "API"]}>
  **API model deprecation notice**

  Please note that as of August 1, 2025, R1-1776 will be removed from the available models.

  R1 has been a popular option for a while, but it hasn't kept pace with recent improvements and lacks support for newer features. To reduce engineering overhead and make room for more capable models, we're retiring it from the API.

  If you liked R1's strengths, we recommend switching to `Sonar Pro Reasoning`. It offers similar behavior with stronger overall performance.
</Update>

<Update label="July 2025" tags={["API", "Cost Tracking", "Usage"]}>
  **New: Detailed Cost Information in API Responses**

  The API response JSON now includes detailed cost information for each request.

  You'll now see a new structure like this in your response:

  ```json  theme={null}
  "usage": {
      "prompt_tokens": 8,
      "completion_tokens": 439,
      "total_tokens": 447,
      "search_context_size": "low",
      "cost": {
       "input_tokens_cost": 2.4e-05,
       "output_tokens_cost": 0.006585,
       "request_cost": 0.006,
       "total_cost": 0.012609
     }
  }
  ```

  **What's included:**

  * **input\_tokens\_cost**: Cost attributed to input tokens
  * **output\_tokens\_cost**: Cost attributed to output tokens
  * **request\_cost**: Fixed cost per request
  * **total\_cost**: The total cost for this API call

  This update enables easier tracking of usage and billing directly from each API response, giving you complete transparency into the costs associated with each request.
</Update>

<Update label="July 2025" tags={["SEC Filings", "Search", "API"]}>
  **New: SEC Filings Filter for Financial Research**

  We're excited to announce the release of our new SEC filings filter feature, allowing you to search specifically within SEC regulatory documents and filings. By setting `search_domain: "sec"` in your API requests, you can now focus your searches on official SEC documents, including 10-K reports, 10-Q quarterly reports, 8-K current reports, and other regulatory filings.

  This feature is particularly valuable for:

  * Financial analysts researching company fundamentals
  * Investment professionals conducting due diligence
  * Compliance officers tracking regulatory changes
  * Anyone requiring authoritative financial information directly from official sources

  The SEC filter works seamlessly with other search parameters like date filters and search context size, giving you precise control over your financial research queries.

  **Example:**

  ```bash  theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header 'accept: application/json' \
    --header 'authorization: Bearer YOUR_API_KEY' \
    --header 'content-type: application/json' \
    --data '{
      "model": "sonar-pro",
      "messages": [{"role": "user", "content": "What was Apple's revenue growth in their latest quarterly report?"}],
      "stream": false,
      "search_domain": "sec",
      "web_search_options": {"search_context_size": "medium"}
  }' | jq
  ```

  For detailed documentation and implementation examples, please see our [SEC Guide](https://docs.perplexity.ai/guides/sec-guide).
</Update>

<Update label="June 2025" tags={["Date Range", "Search", "API"]}>
  **Enhanced: Date Range Filtering with Latest Updated Field**

  We've enhanced our date range filtering capabilities with new fields that give you even more control over search results based on content freshness and updates.

  **New fields available:**

  * `latest_updated`: Filter results based on when the webpage was last modified or updated
  * `published_after`: Filter by original publication date (existing)
  * `published_before`: Filter by original publication date (existing)

  The `latest_updated` field is particularly useful for:

  * Finding the most current version of frequently updated content
  * Ensuring you're working with the latest data from news sites, blogs, and documentation
  * Tracking changes and updates to specific web resources over time

  **Example:**

  ```bash  theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header 'accept: application/json' \
    --header 'authorization: Bearer YOUR_API_KEY' \
    --header 'content-type: application/json' \
    --data '{
      "model": "sonar-pro",
      "messages": [{"role": "user", "content": "What are the latest developments in AI research?"}],
      "stream": false,
      "web_search_options": {
        "latest_updated": "2025-06-01",
        "search_context_size": "medium"
      }
  }'
  ```

  For comprehensive documentation and more examples, please see our [Date Range Filter Guide](https://docs.perplexity.ai/guides/date-range-filter-guide).
</Update>

<Update label="June 2025" tags={["Academic Filter", "Search", "API"]}>
  **New: Academic Filter for Scholarly Research**
  We're excited to announce the release of our new academic filter feature, allowing you to tailor your searches specifically to academic and scholarly sources. By setting `search_mode: "academic"` in your API requests, you can now prioritize results from peer-reviewed papers, journal articles, and research publications.

  This feature is particularly valuable for:

  * Students and researchers working on academic papers
  * Professionals requiring scientifically accurate information
  * Anyone seeking research-based answers instead of general web content

  The academic filter works seamlessly with other search parameters like `search_context_size` and date filters, giving you precise control over your research queries.

  **Example:**

  ```bash  theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header 'accept: application/json' \
    --header 'authorization: Bearer YOUR_API_KEY' \
    --header 'content-type: application/json' \
    --data '{
      "model": "sonar-pro",
      "messages": [{"role": "user", "content": "What is the scientific name of the lions mane mushroom?"}],
      "stream": false,
      "search_mode": "academic",
      "web_search_options": {"search_context_size": "low"}
  }'
  ```

  For detailed documentation and implementation examples, please see our [Academic Filter Guide](https://docs.perplexity.ai/guides/academic-filter-guide).
</Update>

<Update label="May 2025" tags={["Sonar Deep Research", "Reasoning", "API"]}>
  **New: Reasoning Effort Parameter for Sonar Deep Research**

  We're excited to announce our new reasoning effort feature for sonar-deep-research. This lets you control how much computational effort the AI dedicates to each query. You can choose from "low", "medium", or "high" to get faster, simpler answers or deeper, more thorough responses.

  This feature has a direct impact on the amount of reasoning tokens consumed for each query, giving you the ability to control costs while balancing between speed and thoroughness.

  **Options:**

  * `"low"`: Faster, simpler answers with reduced token usage
  * `"medium"`: Balanced approach (default)
  * `"high"`: Deeper, more thorough responses with increased token usage

  **Example:**

  ```bash  theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header 'accept: application/json' \
    --header 'authorization: Bearer ${PPLX_KEY}' \
    --header 'content-type: application/json' \
    --data '{
      "model": "sonar-deep-research",
      "messages": [{"role": "user", "content": "What should I know before markets open today?"}],
      "stream": true,
      "reasoning_effort": "low"
    }'
  ```

  For detailed documentation and implementation examples, please see:
  [Sonar Deep Research Documentation](https://docs.perplexity.ai/models/models/sonar-deep-research)
</Update>

<Update label="May 2025" tags={["Sonar Deep Research", "Async", "API"]}>
  **New: Asynchronous API for Sonar Deep Research**

  We're excited to announce the addition of an asynchronous API for Sonar Deep Research, designed specifically for research-intensive tasks that may take longer to process.

  This new API allows you to submit requests and retrieve results later, making it ideal for complex research queries that require extensive processing time.

  The asynchronous API endpoints include:

  1. `GET https://api.perplexity.ai/async/chat/completions` - Lists all asynchronous chat completion requests for the authenticated user
  2. `POST https://api.perplexity.ai/async/chat/completions` - Creates an asynchronous chat completion job
  3. `GET https://api.perplexity.ai/async/chat/completions/{request_id}` - Retrieves the status and result of a specific asynchronous chat completion job

  **Note:** Async requests have a time-to-live (TTL) of 7 days. After this period, the request and its results will no longer be accessible.

  For detailed documentation and implementation examples, please see:
  [Sonar Deep Research Documentation](https://docs.perplexity.ai/models/models/sonar-deep-research)
</Update>

<Update label="May 2025" tags={["API", "Search Results", "Breaking Change"]}>
  **Enhanced API Responses with Search Results**

  We've improved our API responses to give you more visibility into search data by adding a new `search_results` field to the JSON response object.

  This enhancement provides direct access to the search results used by our models, giving you more transparency and control over the information being used to generate responses.

  The `search_results` field includes:

  * `title`: The title of the search result page
  * `url`: The URL of the search result
  * `date`: The publication date of the content

  **Example:**

  ```json  theme={null}
  "search_results": [
    {
      "title": "Understanding Large Language Models",
      "url": "https://example.com/llm-article",
      "date": "2023-12-25"
    },
    {
      "title": "Advances in AI Research",
      "url": "https://example.com/ai-research",
      "date": "2024-03-15"
    }
  ]
  ```

  This update makes it easier to:

  * Verify the sources used in generating responses
  * Create custom citation formats for your applications
  * Filter or prioritize certain sources based on your needs

  **Update: The `citations` field has been fully deprecated and removed.** All applications should now use the `search_results` field, which provides more detailed information including titles, URLs, and publication dates.

  The `search_results` field is available across all our search-enabled models and offers enhanced source tracking capabilities.
</Update>

<Update label="April 2025" tags={["API Portal", "Organization", "Management"]}>
  **New API Portal for Organization Management**

  We are excited to announce the release of our new API portal, designed to help you better manage your organization and API usage.

  With this portal, you can:

  * Organize and manage your API keys more effectively.
  * Gain insights into your API usage and team activity.
  * Streamline collaboration within your organization.

  Check it out here:\
  [https://www.perplexity.ai/account/api/group](https://www.perplexity.ai/account/api/group)
</Update>

<Update label="April 2025" tags={["Search", "Location", "Filtering"]}>
  **New: Location filtering in search**

  Looking to narrow down your search results based on users' locations?\
  We now support user location filtering, allowing you to retrieve results only from a particular user location.

  Check out the [guide](https://docs.perplexity.ai/guides/user-location-filter-guide).
</Update>

<Update label="April 2025" tags={["Images", "Multimodal", "API"]}>
  **Image uploads now available for all users!**

  You can now upload images to Sonar and use them as part of your multimodal search experience.\
  Give it a try by following our image upload guide:\
  [https://docs.perplexity.ai/guides/image-attachments](https://docs.perplexity.ai/guides/image-attachments)
</Update>

<Update label="April 2025" tags={["Search", "Date Range", "Filtering"]}>
  **New: Date range filtering in search**

  Looking to narrow down your search results to specific dates?\
  We now support date range filtering, allowing you to retrieve results only from a particular timeframe.

  Check out the guide:\
  [https://docs.perplexity.ai/guides/date-range-filter-guide](https://docs.perplexity.ai/guides/date-range-filter-guide)
</Update>

<Update label="April 2025" tags={["Pricing", "Citation Tokens", "API"]}>
  **Clarified: Search context pricing update**

  We've fully transitioned to our new pricing model: citation tokens are no longer charged.\
  If you were already using the `search_context_size` parameter, you've been on this model already.

  This change makes pricing simpler and cheaper for everyone — with no downside.

  View the updated pricing:\
  [https://docs.perplexity.ai/guides/pricing](https://docs.perplexity.ai/guides/pricing)
</Update>

<Update label="April 2025" tags={["Features", "Access", "API"]}>
  **All features now available to everyone**

  We've removed all feature gating based on tiered spending. These were previously only available to users of Tier 3 and above.

  That means **every user now has access to all API capabilities**, regardless of usage volume or spend. Rate limits are still applicable.\
  Whether you're just getting started or scaling up, you get the full power of Sonar out of the box.
</Update>

<Update label="March 2025" tags={["Structured Outputs", "API", "Features"]}>
  **Structured Outputs Available for All Users**

  We're excited to announce that structured outputs are now available to all Perplexity API users, regardless of tier level. Based on valuable feedback from our developer community, we've removed the previous Tier 3 requirement for this feature.

  **What's available now:**

  * JSON structured outputs are supported across all models
  * Both JSON and Regex structured outputs are supported for `sonar` and `sonar-reasoning` models

  **Coming soon:**

  * Full Regex support for all models

  This change allows developers to create more reliable and consistent applications from day one. We believe in empowering our community with the tools they need to succeed, and we're committed to continuing to improve accessibility to our advanced features.

  Thank you for your feedback—it helps us make Perplexity API better for everyone.
</Update>

<Update label="March 2025" tags={["Sonar Models", "Search Modes", "Pricing"]}>
  **Improved Sonar Models: New Search Modes**

  We're excited to announce significant improvements to our Sonar models that deliver superior performance at lower costs. Our latest benchmark testing confirms that Sonar and Sonar Pro now outperform leading competitors while maintaining more affordable pricing.

  Key updates include:

  * **Three new search modes** across most Sonar models:
    * High: Maximum depth for complex queries
    * Medium: Balanced approach for moderate complexity
    * Low: Cost-efficient for straightforward queries (equivalent to current pricing)

  * **Simplified billing structure**:
    * Transparent pricing for input/output tokens
    * No charges for citation tokens in responses (except for Sonar Deep Research)

  The current billing structure will be supported as the default option for 30 days (until April 18, 2025). During this period, the new search modes will be available as opt-in features.

  **Important Note:** After April 18, 2025, Sonar Pro and Sonar Reasoning Pro will not return Citation tokens or number of search results in the usage field in the API response.
</Update>

<Update label="January 2025" tags={["Models", "Deprecation", "API"]}>
  **API model deprecation notice**

  Please note that as of February 22, 2025, several models and model name aliases will no longer be accessible. The following model names will no longer be available via API:

  `llama-3.1-sonar-small-128k-online`

  `llama-3.1-sonar-large-128k-online`

  `llama-3.1-sonar-huge-128k-online`

  We recommend updating your applications to use our recently released Sonar or Sonar Pro models – you can learn more about them here. Thank you for being a Perplexity API user.
</Update>

<Update label="January 2025" tags={["Sonar", "Sonar Pro", "New APIs"]}>
  **Build with Perplexity's new APIs**

  We are expanding API offerings with the most efficient and cost-effective search solutions available:  **Sonar** and **Sonar Pro**.

  **Sonar** gives you fast, straightforward answers

  **Sonar Pro** tackles complex questions that need deeper research and provides more sources

  Both models offer built-in citations, automated scaling of rate limits, and public access to advanced features like structured outputs and search domain filters. And don't worry, we never train on your data. Your information stays yours.

  You can learn more about our new APIs here - [http://sonar.perplexity.ai/](http://sonar.perplexity.ai/)
</Update>

<Update label="November 2024" tags={["Citations", "Rate Limits", "API"]}>
  **Citations Public Release and Increased Default Rate Limits**

  We are excited to announce the public availability of citations in the Perplexity API. In addition, we have also increased our default rate limit for the sonar online models to 50 requests/min for all users.

  Effective immediately, all API users will see citations returned as part of their requests by default. This is not a breaking change. The **return\_citations** parameter will no longer have any effect.

  If you have any questions or need assistance, feel free to reach out to our team at [api@perplexity.ai](mailto:api@perplexity.ai)
</Update>

<Update label="July 2024" tags={["Sonar Models", "Models", "Deprecation"]}>
  **Introducing New and Improved Sonar Models**

  We are excited to announce the launch of our latest Perplexity Sonar models:

  **Online Models** -
  `llama-3.1-sonar-small-128k-online`
  `llama-3.1-sonar-large-128k-online`

  **Chat Models** -
  `llama-3.1-sonar-small-128k-chat`
  `llama-3.1-sonar-large-128k-chat`

  These new additions surpass the performance of the previous iteration. For detailed information on our supported models, please visit our model card documentation.

  **\[Action Required]** Model Deprecation Notice
  Please note that several models will no longer be accessible effective 8/12/2024. We recommend updating your applications to use models in the Llama-3.1 family immediately.

  The following model names will no longer be available via API -
  `llama-3-sonar-small-32k-online`
  `llama-3-sonar-large-32k-online`
  `llama-3-sonar-small-32k-chat`
  `llama-3-sonar-large-32k-chat`
  `llama-3-8b-instruct`
  `llama-3-70b-instruct`
  `mistral-7b-instruct`
  `mixtral-8x7b-instruct`

  We recommend switching to models in the Llama-3.1 family:

  **Online Models** -
  `llama-3.1-sonar-small-128k-online`
  `llama-3.1-sonar-large-128k-online`

  **Chat Models** -
  `llama-3.1-sonar-small-128k-chat`
  `llama-3.1-sonar-large-128k-chat`

  **Instruct Models** -
  `llama-3.1-70b-instruct`
  `llama-3.1-8b-instruct`

  If you have any questions, please email [support@perplexity.ai](mailto:support@perplexity.ai).
  Thank you for being a Perplexity API user.

  Stay curious,

  Team Perplexity
</Update>

***

<Update label="April 2024" tags={["Models", "Deprecation", "API"]}>
  **Model Deprecation Notice**

  Please note that as of May 14, several models and model name aliases will no longer be accessible. We recommend updating your applications to use models in the Llama-3 family immediately. The following model names will no longer be available via API:

  `codellama-70b-instruct`
  `mistral-7b-instruct`
  `mixtral-8x22b-instruct`
  `pplx-7b-chat`
  `pplx-7b-online`
</Update>
