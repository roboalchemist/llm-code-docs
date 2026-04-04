# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/javascript-rendering.md

# Javascript Rendering

## What? <a href="#what-and-why" id="what-and-why"></a>

**JS Rendering** feature allow users the ability to control the rendering of the target webpage, configuring the Nimble Browser Driver settings behind the scenes:

* Dynamically select and configure the most appropriate [Browserless Driver](https://docs.nimbleway.io/technologies/browserless-drivers) based on the characteristics of the target domain. This dynamic adjustment ensures optimal performance and accuracy in data retrieval by tailoring the browser's behavior to suit specific website requirements.
* Flexibility to customize how web pages are rendered according to specific needs. Users can adjust settings such as enabling or disabling JavaScript, controlling image loading, or managing CSS interpretation and more.

## &#x20;Why? <a href="#what-and-why" id="what-and-why"></a>

* **Dynamic Content**: Many modern websites use JavaScript to dynamically generate content. If a page is not rendered, important information that loads asynchronously via scripts may not appear in the page source, thus missing from the data collected.
* **Interactivity and User Events**: Websites often modify their content based on user interactions (like clicking or scrolling), which are handled by JavaScript. Rendering the page ensures that the resulting state of these interactions is captured, providing a more accurate representation of the user-experienced content - refer to Render Flow
* **SEO and Visibility**: Rendered pages more accurately mimic what end-users see, including content that might impact SEO analyses or visibility studies. This is important for tasks such as competitive analysis, market research, and monitoring how content appears to users in different locations or under different conditions.
* **Handling Redirects and Ads**: JavaScript is often used to control redirects or to load ads dynamically. Rendering allows you to capture these elements as they would appear to a real user, which can be important for analyzing ad placement and effectiveness or understanding redirection paths.
* **Improved Accuracy**: When a page is rendered, the DOM (Document Object Model) is fully built, allowing your scraping tools to interact with the final structure of the page as a user would. This leads to more accurate and reliable data extraction.

## Additional Information <a href="#how" id="how"></a>

* <mark style="color:green;">Supported</mark> by real-time, asynchronous, and batch requests.
* <mark style="color:green;">Supported</mark> Endpoints: [Web](https://docs.nimbleway.io/nimble-sdk/web-api)
* <mark style="color:red;">Not supported</mark> Endpoints: [Social](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/social-api), [SERP](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api), [Maps](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api) and [eCommerce](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api).

## Request Option <a href="#request-option" id="request-option"></a>

### Enable JS Rendering <a href="#example" id="example"></a>

To run Nimble API request that requires rendering the target URL, the user simply needs to include the parameter `"render": true` in the body of the request. Behind the scenes, the Nimble Browser will dynamically set up the necessary browser drivers to execute the task on the specified domain.

<table><thead><tr><th width="140">Parameter</th><th width="245">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>render</code></td><td>Optional (default = <code>false</code>)</td><td>Enum: <code>true</code> | <code>false</code> - enables or disables Javascript rendering on the target page</td></tr></tbody></table>

{% hint style="info" %}
Subscribed users in ***Enterprise Plan*** can have a direct access to Nimble's [Browserless Drivers](https://docs.nimbleway.io/technologies/browserless-drivers), which also affect the JS rendering:

* When `NMBL-VX6`Driver is being used, the render is automatically set to `false`.
* When `NMBL-VX8/VX10`Driver are being used, the render  is automatically set to `true`.
  {% endhint %}

#### Example Request

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com",
    "method": "GET",
    "parse": false,
    "render": true
}'
```

{% endtab %}
{% endtabs %}

### Advance Rendering Options <a href="#advance-rendering-option" id="advance-rendering-option"></a>

The parameter `render_options` includes several configuration options that allow users to fine-tune how Nimble renders webpages. These options include:

| Parameter         | Required                     | Description                                                                         |
| ----------------- | ---------------------------- | ----------------------------------------------------------------------------------- |
| `include_iframes` | Optional (default = `false`) | Boolean - Instructs Nimble APIs to render or not to render iframes.                 |
| `timeout`         | Optional (default = `false`) | Integer (ms) - Defines how long Nimble APIs will wait for a page to finish loading. |
| `render_type`     | Optional (default = `false`) | Enum - Defines the state that Nimble APIs will consider a page as fully loaded.     |
| `blocked_domains` | Optional                     | A list of domains to be blocked as part of the loaded resources.                    |

{% hint style="info" %}
To use `render_options`, the `render` param must be set to `true`
{% endhint %}

#### Render Type and controlling what is a "fully loaded" page

Because many webpages load additional content after the initial page has finished loading (such as single-page applications), deciding exactly when a webpage has finished loading is often ambiguous. To aid with this, Nimble APIs supports several options of `render_type`:

* **load** - Nimble will consider a page ready after the standard page load event is fired.
* **domready** - Nimble will consider a page ready when the DOMContentLoaded event is fired.
* **idle2** - Nimble will consider a page ready when there are 2 or fewer network connections made during the last 500ms.
* **idle0 -** Nimble will consider a page ready when no new network connections are made during the last 500ms.

#### Example Request

In the below example, `render_type` and `timeout` are combined to illustrate how to simulatenously use rendering options:

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com",
    "method": "GET",
    "parse": true,
    "render": true,
    "render_options": {
        "include_iframes": true,
        "render_type": "idle0",
 "timeout": 35000
    }
}'
```

{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

url = 'https://api.webit.live/api/v1/realtime/web'
headers = {
    'Authorization': 'Basic <credential string>',
    'Content-Type': 'application/json'
}
data = {
    "url": "https://www.example.com",
    "method": "GET",
    "parse": True,
    "render": True,
    "render_options": {
        "include_iframes": True,
        "render_type": "idle0",
        "timeout": 35000,
        "blocked_domains": ["domain2block.com"]
    }
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
```

{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code overflow="wrap" %}

```javascript
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/realtime/web';
const headers = {
  'Authorization': 'Basic <credential string>',
  'Content-Type': 'application/json'
};
const data = {
  "url": "https://www.example.com",
  "method": "GET",
  "parse": true,
  "render": true,
  "render_options": {
    "include_iframes": true,
    "render_type": "idle0",
    "timeout": 35000,
    "blocked_domains": ["domain2block.com"]
  }
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

{% endcode %}
{% endtab %}

{% tab title="Go" %}
{% code overflow="wrap" %}

```go
package main

import (
 "bytes"
 "fmt"
 "net/http"
 "encoding/json"
)

func main() {
 url := "https://api.webit.live/api/v1/realtime/web"
 payload := []byte(`{
  "url": "https://www.example.com",
  "method": "GET",
  "parse": true,
  "render": true,
  "render_options": {
   "include_iframes": true,
   "render_type": "idle0",
   "timeout": 35000,
   "blocked_domains": ["domain2block.com"]
  }
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

{% endcode %}
{% endtab %}
{% endtabs %}

### Controlling resource loading within a webpage

Webpages typically load resources from many external domains, including iframes, images, javascript files, and other resources. In some cases, it may be beneficial to restrict non-essential resources in order to speed up the loading of a page, save bandwidth, and more.

Nimble provides two rendering options that help control what parts of a page are loaded, called `include_iframes` and `blocked_domains`.

* `include_iframes` - controls whether iframes within the target page are loaded or not.
* `blocked_domains` - a list of domains from which external resources are not to be loaded.

#### Example Request

In the below example, we set `include_iframes` to "true" to allow iframes to be loaded, and add "example2.com" and "example3.com" to`blocked_domains` to prevent resources from those domains being loaded:

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com",
    "method": "GET",
    "parse": true,
    "render": true,
    "render_options": {
        "include_iframes": true,
        "blocked_domains": ["example2.com", "example3.com"]
    }
}'
```

{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

url = 'https://api.webit.live/api/v1/realtime/web'
headers = {
    'Authorization': 'Basic <credential string>',
    'Content-Type': 'application/json'
}
data = {
    "url": "https://www.example.com",
    "method": "GET",
    "parse": True,
    "render": True,
    "render_options": {
        "include_iframes": True,
        "blocked_domains": ["example2.com", "example3.com"]
    }
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
```

{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code overflow="wrap" %}

```javascript
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/realtime/web';
const headers = {
  'Authorization': 'Basic <credential string>',
  'Content-Type': 'application/json'
};
const data = {
  "url": "https://www.example.com",
  "method": "GET",
  "parse": true,
  "render": true,
  "render_options": {
    "include_iframes": true,
    "blocked_domains": ["example2.com", "example3.com"]
  }
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

{% endcode %}
{% endtab %}

{% tab title="Go" %}
{% code overflow="wrap" %}

```go
package main

import (
 "bytes"
 "fmt"
 "net/http"
 "encoding/json"
)

func main() {
 url := "https://api.webit.live/api/v1/realtime/web"
 payload := []byte(`{
  "url": "https://www.example.com",
  "method": "GET",
  "parse": true,
  "render": true,
  "render_options": {
   "include_iframes": true,
   "blocked_domains": ["example2.com", "example3.com"]
  }
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

{% endcode %}
{% endtab %}
{% endtabs %}
