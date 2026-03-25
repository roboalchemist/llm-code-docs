# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api/real-time-search-request.md

# Real-time search request

A real-time request allows users to collect data from the search of a single search term. The collected data is returned directly to the user performing the request. The [Nimble SERP API](https://nimbleway.com/nimble-api/serp/) currently supports the following search engines:

* [x] Google Search
* [x] Google AI Overviews (SGE/AIO)
* [x] Bing Search
* [x] Yandex Search

To send a request, use the **/realtime/serp** endpoint with the following syntax:

{% hint style="info" %}
Nimble APIs requires that a base64 encoded credential string be sent with every request to authenticate your account. For detailed examples, see [Web API Authentication](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/nimble-apis-authentication).
{% endhint %}

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/serp' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "search_engine": "google_search",
    "country": "US",
    "query": "Sample search phrase"
}'
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}

```python
import requests

url = 'https://api.webit.live/api/v1/realtime/serp'
headers = {
    'Authorization': 'Basic <credential string>',
    'Content-Type': 'application/json'
}
data = {
    "search_engine": "google_search",
    "country": "FR",
    "locale": "fr",
    "query": "Sample search phrase"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/realtime/serp';
const headers = {
  'Authorization': 'Basic <credential string>',
  'Content-Type': 'application/json'
};
const data = {
  "search_engine": "google_search",
  "country": "FR",
  "locale": "fr",
  "query": "Sample search phrase"
};

axios.post(url, data, { headers })
  .then(response => {
    console.log(response.status);
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });

```

{% endtab %}

{% tab title="Go" %}

```go
package main

import (
 "bytes"
 "fmt"
 "net/http"
 "encoding/json"
)

func main() {
 url := "https://api.webit.live/api/v1/realtime/serp"
 payload := []byte(`{
  "search_engine": "google_search",
  "country": "FR",
  "locale": "fr",
  "query": "Sample search phrase"
 }`)
 headers := map[string]string{
  "Authorization":  "Basic <credential string>",
  "Content-Type":   "application/json",
 }

 req, err := http.NewRequest("POST", url, bytes.NewBuffer(payload))
 if err != nil {
  fmt.Println(err)
  return
 }

 for key, value := range headers {
  req.Header.Set(key, value)
 }

 client := &http.Client{}
 resp, err := client.Do(req)
 if err != nil {
  fmt.Println(err)
  return
 }
 defer resp.Body.Close()

 fmt.Println(resp.StatusCode)
 // Read the response body if needed
 // body, err := ioutil.ReadAll(resp.Body)
 // fmt.Println(string(body))
}

```

{% endtab %}
{% endtabs %}

{% hint style="success" %}
Every request sent through Nimble API is automatically routed through Nimble IP - our premium proxy network!
{% endhint %}

{% hint style="warning" %}
To include Google's AI Overview result, use `google_aio` as search engine

* `google_sge` - supports AI Overview results, limited to first 10 organic SERP results (legacy)
* `google_aio` - supports AI Overview results, support auto pagination with `num_result` (up to 100)
  * **Please Contact Sales** - Using `num_results` greater than 10 may incur additional `VX6` charges per page.
    {% endhint %}

### **Request Options**

<table><thead><tr><th width="183">Parameter</th><th width="155">Required</th><th width="177">Type</th><th>Description</th></tr></thead><tbody><tr><td>query</td><td>Required</td><td>String</td><td>The term or phrase to search for.</td></tr><tr><td>search_engine</td><td>Required</td><td><p>Enum: <br><code>google_search</code> </p><p><code>google_sge</code> <code>google_aio</code> </p><p><code>bing_search</code> </p><p><code>yandex_search</code></p></td><td>The search engine from which to collect results.</td></tr><tr><td>tab</td><td>Optional<br>(default = null)</td><td>Enum:<br><code>news</code></td><td>Select the tab of results to return from <code>google_search</code> engine. Currently, <code>news</code> is supported.</td></tr><tr><td>num_results</td><td>Optional</td><td>Integer</td><td>Set the mount of retuned search results</td></tr><tr><td>domain</td><td>Optional</td><td>String</td><td>Search through a custom top-level domain of Google. eg: "co.uk"</td></tr><tr><td>country</td><td>Optional (default = all)</td><td>String</td><td>Country used to access the target URL, use ISO Alpha-2 Country Codes i.e. US, DE, GB</td></tr><tr><td>state</td><td>Optional</td><td>String</td><td>For targeting US states (does not include regions or territories in other countries). Two-letter state code, e.g. NY, IL, etc.</td></tr><tr><td>city</td><td>Optional</td><td>String</td><td>For targeting large cities and metro areas around the globe. When targeting major US cities, you must include state as well. <a href="../../../../../management-tools/nimble-admin-api/admin-api-reference#location">Click here for a list of available cities.</a></td></tr><tr><td>locale</td><td>Optional (default = en)</td><td>String</td><td>String | LCID standard locale used for the URL request. Alternatively, user can use <code>auto</code> for automatic locale based on country targeting.</td></tr><tr><td>location</td><td>Optional</td><td>String</td><td>Search Google through a custom geolocation, regardless of country or proxy location. eg: "London,Ohio,United States". See <a href="getting-local-data">Getting local data</a> for more information.</td></tr><tr><td>parse</td><td>Optional (default = true)</td><td>Boolean</td><td>Instructs Nimble whether to structure the results into a JSON format or return the raw HTML.</td></tr><tr><td>ads_optimization</td><td>Optional (default = false)</td><td>Boolean</td><td>This flag increases the number of paid ads (sponsored ads) in the results. It works by running the requests in 'incognito' mode (requires JS rendering) </td></tr></tbody></table>

{% hint style="warning" %}
**Jan 25:** Due to latest Google changes, the `ads_optimization` flag requires JS rendering which forces the request to use [VX8 Driver](https://docs.nimbleway.io/technologies/browserless-drivers/api-driver-based-pricing) and hence increase the request's computing costs.
{% endhint %}

### Response

**Headers**

X-Task-ID: string

**Payload examples:**

If parsing is disabled, the resulting data will be the raw HTML of the requested SERP. If parsing is enabled, a JSON object with a parsed version of the SERP will be delivered in addition to the raw HTML, which is contained under the <mark style="color:red;background-color:yellow;">html\_content</mark> property.

**200 OK**

{% code overflow="wrap" %}

```json
{
  "status": "success",
  "html_content": "<html>The SERP's full HTML</html>",
  "parsing": {
    "status": "success",
    "entities": {
      "InlineVideos": [
        {
          "entityType": "InlineVideos",
          "videos": [
            {
              "channel": "FilmsActu",
              "date": "15 nov. 2021",
              "length": "1:52",
              "source": "YouTube",
              "thumbnail": "https://i.ytimg.com/vi/b1r_UR5-0tY/mqdefault.jpg?sqp=-oaymwEECHwQRg&rs=AMzJL3kXJ1udP5Pc4cVSVd0uvOsYe0mTCg",
              "title": "LE TEST Bande Annonce (2021)",
              "url": "https://www.youtube.com/watch?v=b1r_UR5-0tY"
            },
                        ...
          ]
        }
      ],
      "OrganicResult": [
        {
          "displayed_url": "https://fr.wikipedia.org › wiki › Test",
          "entityType": "OrganicResult",
          "position": 1,
          "sitelinks": [
            {
              "title": "Test (méthode) - Wikipédiahttps://fr.wikipedia.org › wiki › Test_(méthode)",
              "url": "https://fr.wikipedia.org/wiki/Test_(m%C3%A9thode)"
            }
          ],
          "snippet": "Le mot test est polysémique en français et issu de deux étymologies latines distinctes : testis (témoin) et testa (récipient rond).",
          "title": "Test - Wikipédia",
          "url": "https://fr.wikipedia.org/wiki/Test"
        },
        ...
            "Pagination": [
        {
          "current_page": 1,
          "entityType": "Pagination",
          "next_page_url": "/search?q=test&hl=fr&ei=6GvmYtLMIYKOlwS3wLTgDA&start=10&sa=N&ved=2ahUKEwjS4LSgh6P5AhUCx4UKHTcgDcwQ8NMDegQIAhBP",
          "other_page_urls": {
            "2": "/search?q=test&hl=fr&ei=6GvmYtLMIYKOlwS3wLTgDA&start=10&sa=N&ved=2ahUKEwjS4LSgh6P5AhUCx4UKHTcgDcwQ8tMDegQIAhA9",
            ...
          }
        }
      ],
        "RelatedSearch": [
        {
          "entityType": "RelatedSearch",
          "query": "test quiz",
          "url": "/search?hl=fr&q=Test+quiz&sa=X&ved=2ahUKEwjS4LSgh6P5AhUCx4UKHTcgDcwQ1QJ6BAglEAE"
        },
            ],
            "SearchInformation": [
        {
          "entityType": "SearchInformation",
          "query_displayed": "Sample search phrase",
          "total_results": "Environ 15 850 000 000 résultats "
        }
      ]
    },
    "total_entities_count": 19,
    "entities_count": {
      "InlineVideos": 1,
      "OrganicResult": 8,
      "Pagination": 1,
      "RelatedSearch": 8,
      "SearchInformation": 1
    },
    "metrics": {}
  },
  "url": "https://www.google.com/search?q=Sample+search+phrase&hl=fr",
  "nimble_links": {
    "next_page": "https://api.webit.live/api/v1/realtime/serp?parse=true&query=test&search_engine=google_search&format=json&render=false&country=FR&locale=fr&ei=vPBQZLakI86ckdUPwOuB6A0&sa=N&ved=2ahUKEwi28uXqwNb-AhVOTqQEHcB1AN0Q8NMDegQIBxAW&start=10",
    "other_pages": [
      "https://api.webit.live/api/v1/realtime/serp?parse=true&query=test&search_engine=google_search&format=json&render=false&country=FR&locale=fr&ei=vPBQZLakI86ckdUPwOuB6A0&sa=N&ved=2ahUKEwi28uXqwNb-AhVOTqQEHcB1AN0Q8tMDegQIBxAE&start=10",
      "https://api.webit.live/api/v1/realtime/serp?parse=true&query=test&search_engine=google_search&format=json&render=false&country=FR&locale=fr&ei=vPBQZLakI86ckdUPwOuB6A0&sa=N&ved=2ahUKEwi28uXqwNb-AhVOTqQEHcB1AN0Q8tMDegQIBxAG&start=20",
      ...
      ]
    }
}
```

{% endcode %}

**500 Error**

{% code overflow="wrap" %}

```json
{
          "status": "error",
        "task_id": "<task_id>",
        "msg": "can't download the query response - please try again"
}
```

{% endcode %}

**400 Input Error**

{% code overflow="wrap" %}

```json
{
        "status": "failed",
        "msg": error
}
```

{% endcode %}

### **Response Codes**

| Status | Description                                    |
| ------ | ---------------------------------------------- |
| 200    | OK.                                            |
| 400    | The requested resource could not be reached.   |
| 401    | Unauthorized/invalid credental string          |
| 500    | Internal service error.                        |
| 501    | An error was encountered by the proxy service. |
