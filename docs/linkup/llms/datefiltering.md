# Source: https://docs.linkup.so/pages/changelog/datefiltering.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Dates Filtering

> _Released: March 19, 2024_

We're excited to introduce date filtering capabilities for your search results. This new feature allows you to narrow down your search results to specific time periods, making it easier to find the most relevant and up-to-date information.

### How to Enable

To filter your search results by date, add the `fromDate` and `toDate` parameters to your API request. You can specify either a start date, end date, or both.

**Example Request**

```shell curl theme={null}
curl --request POST \
  --url https://api.linkup.so/v1/search \
  --header 'Authorization: Bearer {{LINKUP_API_KEY}}' \
  --header 'Content-Type: application/json' \
  --data '{
  "q": "Latest developments in AI",
  "depth": "standard",
  "outputType": "searchResults",
  "fromDate": "2024-01-01",
  "toDate": "2024-03-19"
}'
```

**Example Response**

```json  theme={null}
{
  "results": [
    {
      "type": "text",
      "name": "Recent AI Developments",
      "url": "https://example.com/ai-news",
      "content": "Latest breakthroughs in artificial intelligence...",
      "date": "2024-03-15"
    }
  ]
}
```

The date filtering parameters accept dates in ISO 8601 format (YYYY-MM-DD). You can use either:

* `fromDate`: Filter results from this date onwards
* `toDate`: Filter results up to this date
* Both `fromDate` and `toDate`: Filter results within this date range


Built with [Mintlify](https://mintlify.com).