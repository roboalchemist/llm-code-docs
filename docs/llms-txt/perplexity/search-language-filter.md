# Search Language Filter
Source: https://docs.perplexity.ai/docs/search/filters/language-filter



<Note>
  The `search_language_filter` parameter allows you to filter search results by language using ISO 639-1 language codes. Only results in the specified languages will be returned.
</Note>

<Info>
  Language codes must be valid 2-letter ISO 639-1 codes (e.g., "en", "ru", "fr"). You can filter by up to 10 languages per request.
</Info>

## Overview

The language filter for the Search API allows you to control which search results are returned by limiting them to specific languages. This is particularly useful when you need to:

* Search for content in specific languages
* Conduct multilingual research across multiple languages
* Focus on regional content in local languages
* Build language-specific applications or features

The `search_language_filter` parameter accepts an array of ISO 639-1 language codes and returns only results that match those languages.

To filter search results by language:

```bash theme={null}
"search_language_filter": ["en", "fr", "de"]
```

This filter will be applied in addition to any other search parameters.

## Examples

**1. Single Language Filter**

This example limits search results to English language content only.

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search.create(
      query="artificial intelligence",
      max_results=10,
      search_language_filter=["en"]
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search.create({
    query: "artificial intelligence",
    maxResults: 10,
    searchLanguageFilter: ["en"]
  });

  for (const result of response.results) {
    console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "artificial intelligence",
      "max_results": 10,
      "search_language_filter": ["en"]
    }' | jq
  ```
</CodeGroup>

**2. Multiple Language Filter**

Search across multiple languages to gather diverse perspectives or multilingual content:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Search for content in English, French, and German
  response = client.search.create(
      query="renewable energy innovations",
      max_results=15,
      search_language_filter=["en", "fr", "de"]
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Search for content in English, French, and German
  const response = await client.search.create({
    query: "renewable energy innovations",
    maxResults: 15,
    searchLanguageFilter: ["en", "fr", "de"]
  });

  for (const result of response.results) {
    console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "renewable energy innovations",
      "max_results": 15,
      "search_language_filter": ["en", "fr", "de"]
    }' | jq
  ```
</CodeGroup>

**3. Regional Language Search**

Focus on content from specific regions by using their local languages:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Search for Asian market news in Chinese, Japanese, and Korean
  response = client.search.create(
      query="technology market trends",
      max_results=10,
      search_language_filter=["zh", "ja", "ko"]
  )

  # Search for European tech news in multiple European languages
  eu_response = client.search.create(
      query="tech startups",
      max_results=10,
      search_language_filter=["en", "de", "fr", "es", "it"]
  )
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Search for Asian market news in Chinese, Japanese, and Korean
  const response = await client.search.create({
    query: "technology market trends",
    maxResults: 10,
    searchLanguageFilter: ["zh", "ja", "ko"]
  });

  // Search for European tech news in multiple European languages
  const euResponse = await client.search.create({
    query: "tech startups",
    maxResults: 10,
    searchLanguageFilter: ["en", "de", "fr", "es", "it"]
  });
  ```

  ```bash cURL theme={null}
  # Search for Asian market news
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "technology market trends",
      "max_results": 10,
      "search_language_filter": ["zh", "ja", "ko"]
    }' | jq
  ```
</CodeGroup>

**4. Combining with Other Filters**

Language filters work seamlessly with other search parameters for precise control:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Combine language filter with date and domain filters
  response = client.search.create(
      query="climate change research",
      max_results=20,
      search_language_filter=["en", "de"],
      search_domain_filter=["nature.com", "science.org"],
      search_recency_filter="month"
  )

  for result in response.results:
      print(f"{result.title}")
      print(f"URL: {result.url}")
      print(f"Date: {result.date}")
      print("---")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Combine language filter with date and domain filters
  const response = await client.search.create({
    query: "climate change research",
    maxResults: 20,
    searchLanguageFilter: ["en", "de"],
    searchDomainFilter: ["nature.com", "science.org"],
    searchRecencyFilter: "month"
  });

  for (const result of response.results) {
    console.log(`${result.title}`);
    console.log(`URL: ${result.url}`);
    console.log(`Date: ${result.date}`);
    console.log("---");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "climate change research",
      "max_results": 20,
      "search_language_filter": ["en", "de"],
      "search_domain_filter": ["nature.com", "science.org"],
      "search_recency_filter": "month"
    }' | jq
  ```
</CodeGroup>

## Parameter Reference

### `search_language_filter`

* **Type**: Array of strings
* **Format**: ISO 639-1 language codes (2 lowercase letters)
* **Description**: Filters search results to only include content in the specified languages
* **Optional**: Yes
* **Maximum**: 10 language codes per request
* **Example**: `"search_language_filter": ["en", "fr", "de"]`

## Common Language Codes

Here's a comprehensive list of frequently used ISO 639-1 language codes:

| Language   | Code | Language   | Code |
| ---------- | ---- | ---------- | ---- |
| English    | `en` | Portuguese | `pt` |
| Spanish    | `es` | Dutch      | `nl` |
| French     | `fr` | Polish     | `pl` |
| German     | `de` | Swedish    | `sv` |
| Italian    | `it` | Norwegian  | `no` |
| Russian    | `ru` | Danish     | `da` |
| Chinese    | `zh` | Finnish    | `fi` |
| Japanese   | `ja` | Czech      | `cs` |
| Korean     | `ko` | Hungarian  | `hu` |
| Arabic     | `ar` | Greek      | `el` |
| Hindi      | `hi` | Turkish    | `tr` |
| Bengali    | `bn` | Hebrew     | `he` |
| Indonesian | `id` | Thai       | `th` |
| Vietnamese | `vi` | Ukrainian  | `uk` |

<Tip>
  For a complete list of ISO 639-1 language codes, see the [ISO 639-1 standard](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
</Tip>

## Best Practices

### Language Code Validation

* **Use Valid Codes**: Always use valid 2-letter ISO 639-1 codes. Invalid codes will result in an API error.
* **Lowercase Only**: Language codes must be lowercase (e.g., "en" not "EN").
* **Client-Side Validation**: Validate language codes on the client side using a regex pattern:

<CodeGroup>
  ```python Python theme={null}
  import re

  def validate_language_code(code):
      pattern = r'^[a-z]{2}$'
      return bool(re.match(pattern, code))

  def validate_language_filters(codes):
      if len(codes) > 10:
          raise ValueError("Maximum 10 language codes allowed")
      
      for code in codes:
          if not validate_language_code(code):
              raise ValueError(f"Invalid language code: {code}")
      
      return True

  # Usage
  try:
      codes = ["en", "fr", "de"]
      validate_language_filters(codes)
      
      response = client.search.create(
          query="technology news",
          search_language_filter=codes
      )
  except ValueError as e:
      print(f"Validation error: {e}")
  ```

  ```typescript Typescript theme={null}
  function validateLanguageCode(code: string): boolean {
    const pattern = /^[a-z]{2}$/;
    return pattern.test(code);
  }

  function validateLanguageFilters(codes: string[]): void {
    if (codes.length > 10) {
      throw new Error("Maximum 10 language codes allowed");
    }
    
    for (const code of codes) {
      if (!validateLanguageCode(code)) {
        throw new Error(`Invalid language code: ${code}`);
      }
    }
  }

  // Usage
  try {
    const codes = ["en", "fr", "de"];
    validateLanguageFilters(codes);
    
    const response = await client.search.create({
      query: "technology news",
      searchLanguageFilter: codes
    });
  } catch (error) {
    console.error("Validation error:", error.message);
  }
  ```
</CodeGroup>

### Strategic Language Selection

* **Be Specific**: Choose languages that are most relevant to your research or application needs.
* **Consider Your Audience**: Select languages that match your target audience's preferences.
* **Regional Relevance**: Combine language filters with geographic filters (`country` parameter) for better regional targeting.
* **Content Availability**: Some topics may have limited content in certain languages. Start broad and narrow down as needed.

### Performance Considerations

* **Filter Size**: While you can specify up to 10 languages, using fewer languages may improve response times.
* **Result Quality**: More languages mean a broader search scope, which can dilute result relevance. Be strategic about which languages to include.
* **Combination Effects**: Language filters combined with other restrictive filters (domain, date) may significantly reduce the number of results.

## Advanced Usage Patterns

### Multilingual Research

Conduct comprehensive research by searching across multiple languages:

```python theme={null}
from perplexity import Perplexity

client = Perplexity()
