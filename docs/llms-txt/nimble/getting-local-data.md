# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api/getting-local-data.md

# Getting local data

Accessing localized SERP data is often critical. Two searches performed from different countries or even cities can yield vastly different results. Searches that return business listings, for example, may vary widely according to the businesses close to the search location. Searches from different countries often return results in their local languages, which affects both the contents and ordering of the SERP.

Nimble's [SERP Scraping API](https://nimbleway.com/nimble-api/serp/) offers several methods for targeting and accessing data that is localized to a particular geolocation, including:

* [x] **Proxy location**
* [x] **Google custom location**
* [x] **Search locale**
* [x] **Top-level domains**

### **Proxy location**

Use the country, state, and city parameters to set the geographic location of your desired proxy. Nimble SERP API comes with built-in [premium proxy services](https://nimbleway.com/nimble-ip/), and every request is processed through our premium proxies.&#x20;

* The `country` parameter accepts ISO Alpha-2 Country Codes, such as US, DE, GB.
* the state parameter is for targeting US states (does not include regions or territories in other countries). Two-letter state code, e.g. NY, IL, etc.
* The city parameter is for targeting large cities and metro areas around the globe. When targeting major US cities, you must include state as well. [Click here for a list of available cities.](https://docs.nimbleway.io/management-tools/nimble-admin-api/admin-api-reference#location)

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/serp' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "query": "hello world",
    "search_engine": "google_search",
    "country": "US",
    "state": "NY",
    "city": "brooklyn",
    "parse": true
}'
```

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
    "query": "hello world",
    "search_engine": "google_search",
    "country": "US",
    "parse": True
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
  "query": "hello world",
  "search_engine": "google_search",
  "country": "US",
  "parse": true
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
  "query": "hello world",
  "search_engine": "google_search",
  "country": "US",
  "parse": true
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

### **Google custom location**

Google allows users to perform searches through a location other than their own. This option is currently not available with other search engines, and is independent of any other location settings. To set a custom search location, use the `location` parameter, which accepts either Google's "[canonical names](https://developers.google.com/google-ads/api/reference/data/geotargets)", or a free text location string.

{% hint style="info" %}
When using the location parameter with Google, paid/sponsored ads will not be included in the results. If you need to collect SERP ads data, please use one of the alternative methods of geotargeting.
{% endhint %}

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/serp' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "query": "hello world",
    "search_engine": "google_search",
    "country": "US",
    "location": "London,Ohio,United States",
    "parse": true
}'
```

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
    "query": "hello world",
    "search_engine": "google_search",
    "country": "US",
    "location": "London,Ohio,United States",
    "parse": True
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
  "query": "hello world",
  "search_engine": "google_search",
  "country": "US",
  "location": "London,Ohio,United States",
  "parse": true
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
  "query": "hello world",
   "search_engine": "google_search",
   "country": "US",
   "location": "London,Ohio,United States",
   "parse": true
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

### **Search locale**

Use the `locale` parameter to control the locale passed to the search engine. This parameter accepts an LCID standard locale, such as "en", "fr", "de", etc.

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/serp' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "query": "hello world",
    "search_engine": "google_search",
    "country": "US",
    "location": "London,Ohio,United States",
    "locale": "en",
    "parse": true
}'
```

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
    "query": "hello world",
    "search_engine": "google_search",
    "country": "US",
    "location": "London,Ohio,United States",
    "locale": "en",
    "parse": True
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
  "query": "hello world",
  "search_engine": "google_search",
  "country": "US",
  "location": "London,Ohio,United States",
  "locale": "en",
  "parse": true
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
  "query": "hello world",
    "search_engine": "google_search",
   "country": "US",
    "location": "London,Ohio,United States",
     "locale": "en",
   "parse": true
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

### **Top-level domains**

A top-level domain refers to the portion of a URL that comes immediately after the domain name, such as ".com", ".org", "co.uk", etc. The `domain` parameter enables users to perform searches on a particular top-level domain variant of Google, such as "google.co.uk". This feature is currently only compatible with Google. This parameter accepts only the top-level domain portion, such as "co.uk".

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/serp' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "query": "hello world",
    "search_engine": "google_search",
    "country": "GB",
    "domain": "co.uk",
    "parse": true
}'
```

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
    "query": "hello world",
    "search_engine": "google_search",
    "country": "GB",
    "domain": "co.uk",
    "parse": True
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
  "query": "hello world",
  "search_engine": "google_search",
  "country": "GB",
  "domain": "co.uk",
  "parse": true
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
  "query": "hello world",
   "search_engine": "google_search",
  "country": "GB",
  "domain": "co.uk",
     "parse": true
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
