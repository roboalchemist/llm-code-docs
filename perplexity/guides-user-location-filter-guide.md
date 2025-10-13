# Source: https://docs.perplexity.ai/guides/user-location-filter-guide

The `user_location` parameter within `web_search_options` allows you to refine search results based on the user’s approximate geographic location. This helps provide more contextually relevant information.
You can specify the location using latitude/longitude coordinates, country code, city, and region. For the most accurate results, we recommend providing as much location information as possible, including `city` and `region` fields. For supported country codes, please refer to the list [here](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
The `city` and `region` fields significantly improve location accuracy. We strongly recommend including them alongside coordinates and country code for the best results.
Latitude and longitude must be provided alongside the country parameter, they cannot be provided on their own.
## 
[​](https://docs.perplexity.ai/guides/user-location-filter-guide#overview)
Overview
The `user_location` filter helps tailor search results by incorporating geographic context. This is particularly useful for queries where location significantly impacts relevance, such as:
  * Finding local businesses or services.
  * Getting information about regional events or news.
  * Understanding location-specific regulations or customs.

To refine search results by location, include the `user_location` object within the `web_search_options` in your request payload. You can provide coordinates, country code, city, region, or combine them for maximum accuracy: **Using All Available Fields (Recommended for Best Accuracy):**
Copy
Ask AI
```
"web_search_options": {
  "user_location": {
    "country": "US",
    "region": "California",
    "city": "San Francisco",
    "latitude": 37.7749,
    "longitude": -122.4194
  }
}

```

**Using City and Region with Country:**
Copy
Ask AI
```
"web_search_options": {
  "user_location": {
    "country": "US",
    "region": "New York",
    "city": "New York City"
  }
}

```

**Using Latitude/Longitude:**
Copy
Ask AI
```
"web_search_options": {
  "user_location": {
    "country":"US",
    "latitude": 37.7749,
    "longitude": -122.4194
  }
}

```

**Using Country Code Only:**
Copy
Ask AI
```
"web_search_options": {
  "user_location": {
    "country": "US"
  }
}

```

These filters work alongside other search parameters like date range or domain filters.
## 
[​](https://docs.perplexity.ai/guides/user-location-filter-guide#examples)
Examples
**1. Refining Results with All Location Fields (Recommended)** This example provides all available location fields for San Francisco to get the most accurate geographically relevant search results. **Request Example**
Python
TypeScript
cURL
Copy
Ask AI
```
from perplexity import Perplexity
client = Perplexity()
completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful local guide."},
        {"role": "user", "content": "What are some good coffee shops nearby?"}
    ],
    model="sonar-pro",
    web_search_options={
        "user_location": {
            "country": "US",
            "region": "California",
            "city": "San Francisco",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
    }
)
print(f"Response: {completion.choices[0].message.content}")

```

**2. Refining Results with Country Code** This example uses a two-letter ISO country code (United States) to provide broader geographic context. **Request Example**
Python
TypeScript
cURL
Copy
Ask AI
```
from perplexity import Perplexity
client = Perplexity()
completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are an expert on international news."},
        {"role": "user", "content": "Summarize political news from today."}
    ],
    model="sonar-pro",
    web_search_options={
        "user_location": {
            "country": "US"
        }
    }
)
print(f"Response: {completion.choices[0].message.content}")

```

**3. Using City and Region for Better Accuracy** This example shows how to use `city` and `region` fields along with coordinates for Paris, France to achieve maximum location accuracy. **Request Example**
Python
TypeScript
cURL
Copy
Ask AI
```
from perplexity import Perplexity
client = Perplexity()
completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are an expert on French news and events."},
        {"role": "user", "content": "What major events are happening in the capital this week?"}
    ],
    model="sonar-pro",
    web_search_options={
        "user_location": {
            "country": "FR",
            "region": "Île-de-France",
            "city": "Paris",
            "latitude": 48.8566,
            "longitude": 2.3522
        }
    }
)
print(f"Response: {completion.choices[0].message.content}")

```

## 
[​](https://docs.perplexity.ai/guides/user-location-filter-guide#best-practices)
Best Practices
**Choosing the Right Specificity**
  * **All Fields (Recommended):** For maximum accuracy, provide country, region, city, latitude, and longitude. This combination gives the best results for location-specific queries.
  * **City and Region:** Use these fields to significantly improve location accuracy without needing exact coordinates. Particularly useful for metropolitan areas and regional searches.
  * **Latitude/Longitude:** Use for high precision when the exact location is known and relevant (e.g., finding nearby points of interest).
  * **Country Code:** Use for broader context when country-level relevance is sufficient (e.g., national news, country-specific regulations).
  * **Combining Fields:** We strongly recommend providing as many location fields as possible. Each additional field improves search accuracy and relevance.

**Data Accuracy**
  * Ensure the provided location data is as accurate as possible. Incorrect data may lead to irrelevant results.
  * Latitude values must be between -90 and 90. Longitude values must be between -180 and 180.
  * Country codes should be valid two-letter ISO 3166-1 alpha-2 codes (e.g., “US”, “GB”, “DE”).
  * City names should match commonly used names (e.g., “New York City” or “NYC” for New York).
  * Region names should match standard administrative divisions (states, provinces, etc.).

**Privacy Considerations**
  * Be mindful of user privacy when collecting and transmitting location data. Only use location when necessary and with user consent where applicable.

**Client-Side Validation**
  * Consider validating location inputs before sending the request: 
    * Check latitude/longitude ranges.
    * Validate country code format (two uppercase letters).
    * Sanitize city and region inputs for special characters.


