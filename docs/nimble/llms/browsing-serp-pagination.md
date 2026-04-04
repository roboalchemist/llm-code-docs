# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api/browsing-serp-pagination.md

# Browsing SERP pagination

### Using Nimble pagination

Having received the first page of results for a chosen search term, it is often desirable to access the next page of results, available through pagination. [Nimble's SERP API](https://nimbleway.com/nimble-api/serp/) makes this easy by providing request-ready paginated URLs at the bottom of each request.&#x20;

{% hint style="success" %}
This also applies for all avaiulable search engines (Google, Bing and Yandex)&#x20;
{% endhint %}

For example:

<pre class="language-json" data-overflow="wrap"><code class="lang-json">{
  "status": "success",
  "html_content": "&#x3C;html>The SERP's full HTML&#x3C;/html>",
  "parsing": {...},
  "url": "https://www.google.com/search?q=Sample+search+phrase&#x26;hl=fr",
<strong>  "nimble_links": {
</strong>    "next_page": "https://api.webit.live/api/v1/realtime/serp?parse=true&#x26;query=test&#x26;search_engine=google_search&#x26;format=json&#x26;render=false&#x26;country=FR&#x26;locale=fr&#x26;ei=vPBQZLakI86ckdUPwOuB6A0&#x26;sa=N&#x26;ved=2ahUKEwi28uXqwNb-AhVOTqQEHcB1AN0Q8NMDegQIBxAW&#x26;start=10",
    "other_pages": [
      "https://api.webit.live/api/v1/realtime/serp?parse=true&#x26;query=test&#x26;search_engine=google_search&#x26;format=json&#x26;render=false&#x26;country=FR&#x26;locale=fr&#x26;ei=vPBQZLakI86ckdUPwOuB6A0&#x26;sa=N&#x26;ved=2ahUKEwi28uXqwNb-AhVOTqQEHcB1AN0Q8tMDegQIBxAE&#x26;start=20",
      "https://api.webit.live/api/v1/realtime/serp?parse=true&#x26;query=test&#x26;search_engine=google_search&#x26;format=json&#x26;render=false&#x26;country=FR&#x26;locale=fr&#x26;ei=vPBQZLakI86ckdUPwOuB6A0&#x26;sa=N&#x26;ved=2ahUKEwi28uXqwNb-AhVOTqQEHcB1AN0Q8tMDegQIBxAG&#x26;start=30",
      ...
    ]
  }
}
</code></pre>

Each of the provided URLs contains identical parameters to the original request, as well as an offset to access paginated pages.

In the below example, a request is written to access the next page's results:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl --location --request GET 'https://api.webit.live/api/v1/realtime/serp?parse=true&query=test&search_engine=google_search&format=json&render=false&country=FR&locale=fr&ei=vPBQZLakI86ckdUPwOuB6A0&sa=N&ved=2ahUKEwi28uXqwNb-AhVOTqQEHcB1AN0Q8NMDegQIBxAW&start=10' \
--header 'Authorization: Basic <credential string>'
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

url = 'https://api.webit.live/api/v1/realtime/serp?parse=true&query=test&search_engine=google_search&format=json&render=false&country=FR&locale=fr&ei=vPBQZLakI86ckdUPwOuB6A0&sa=N&ved=2ahUKEwi28uXqwNb-AhVOTqQEHcB1AN0Q8NMDegQIBxAW&start=10'
headers = {
    'Authorization': 'Basic <credential string>'
}
params = {}

response = requests.get(url, headers=headers, params=params)

print(response.status_code)
print(response.json())

```

{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code overflow="wrap" %}

```javascript
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/realtime/serp?parse=true&query=test&search_engine=google_search&format=json&render=false&country=FR&locale=fr&ei=vPBQZLakI86ckdUPwOuB6A0&sa=N&ved=2ahUKEwi28uXqwNb-AhVOTqQEHcB1AN0Q8NMDegQIBxAW&start=10';
const headers = {
  'Authorization': 'Basic <credential string>'
};
const params = {};

axios.get(url, { headers, params })
  .then(response => {
    console.log(response.status);
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });

```

{% endcode %}
{% endtab %}

{% tab title="Go" %}
{% code overflow="wrap" %}

```go
package main

import (
 "fmt"
 "net/http"
 "io/ioutil"
)

func main() {
 url := "https://api.webit.live/api/v1/realtime/serp?parse=true&query=test&search_engine=google_search&format=json&render=false&country=FR&locale=fr&ei=vPBQZLakI86ckdUPwOuB6A0&sa=N&ved=2ahUKEwi28uXqwNb-AhVOTqQEHcB1AN0Q8NMDegQIBxAW&start=10"
 headers := map[string]string{
  "Authorization": "Basic <credential string>",
 }

 resp, err := http.Get(url)
 if err != nil {
  fmt.Println(err)
  return
 }
 defer resp.Body.Close()

 body, err := ioutil.ReadAll(resp.Body)
 if err != nil {
  fmt.Println(err)
  return
 }

 fmt.Println(resp.StatusCode)
 fmt.Println(string(body))
}

```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
All of the original request's parameters are transmitted through the URL automatically, with the exception of your credential string, which needs to be manually reapplied.
{% endhint %}

### Infinite scrolling SERPs

Search engines often alternate between pagination and infinite scrolling methods depending on location, device, search term, and other variables. In cases where the SERP you requested uses infinite scrolling instead of pagination, only a single URL `next_page` will be provided, which leads to the next batch of results, as in the example below:

{% code overflow="wrap" %}

```json
{
  "status": "success",
  "html_content": "<html>The SERP's full HTML</html>",
  "parsing": {...},
  "url": "https://www.google.com/search?q=Sample+search+phrase&hl=fr",
  "nimble_links": {
    "next_page": "https://api.webit.live/api/v1/realtime/serp?parse=true&query=test&search_engine=google_search&format=json&render=false&country=FR&locale=fr&ei=vPBQZLakI86ckdUPwOuB6A0&sa=N&ved=2ahUKEwi28uXqwNb-AhVOTqQEHcB1AN0Q8NMDegQIBxAW&start=10"
  }
}
```

{% endcode %}
