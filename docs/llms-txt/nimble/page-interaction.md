# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction.md

# Page Interaction

## What? <a href="#what-and-why" id="what-and-why"></a>

Page Interactions allow users to perform operations on a webpage before the web data is collected and returned including clicking, typing, scrolling, and more.

This is useful (and sometimes necessary) in a variety of situations, such as one-page applications that use lazy loading and require scrolling in order to load the desired data. Another example includes E-commerce websites that require button clicks or zip code input to display a product price.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/CCzeFtKzFTSM9ymPqXEZ/Page%20Interactions%202.gif" alt=""><figcaption><p>A visual representation of some of the capabilities of Page Interactions</p></figcaption></figure>

### **Supported Functions**

* [Wait (delay)](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/wait-delay)
* [Wait for Selectors](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/wait-for-selector)
* [Wait and Click (on selector)](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/wait-and-click)
* [Wait and Type](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/wait-and-type)
* [Paste](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/paste)
* [Scroll (position)](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/scroll)
* [Scroll to (selector)](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/scroll-to)
* [Infinite Scroll](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/infinite-scrolling)
* [Capturing Screenshots](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/capturing-screenshots)
* [Collecting Cookies](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/collecting-cookies)
* [Executing HTTP Request](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/executing-http-requests)

## &#x20;Why? <a href="#what-and-why" id="what-and-why"></a>

* **Dynamic Content Access**: Many modern websites load content dynamically based on user interactions. This feature enables your scraping tool to mimic human interactions, such as clicking on dropdowns, navigating through pagination, or filling out forms, to access and retrieve this content. This is particularly useful for scraping data that is not immediately available on the initial page load.
* **Enhanced Data Accuracy**: By interacting with the page as a user would, you can ensure that the data collected is representative of what users actually see. This includes generating and capturing pop-ups, tooltips, and other interactive elements that only appear in response to specific actions.
* **Customized Data Collection**: This feature allows for more targeted and customized data collection strategies. For instance, you can direct the scraping tool to follow specific navigation paths, filter results, or input search terms, tailoring the scraped data to your specific requirements.
* **Automated User Workflows**: Automating complex sequences of actions on a webpage can simulate complete user workflows, providing insights into user experience or functionality testing. This is beneficial for QA testing of web applications, ensuring that all aspects of a site function as intended under various user interactions.
* **Bypass Interactive Barriers**: Some websites use interactive elements as a form of bot management to deter scraping. With the ability to interact with these elements programmatically, your tool can effectively bypass such barriers, allowing you to scrape data from sites that would otherwise be inaccessible.

## Additional Information <a href="#how" id="how"></a>

* <mark style="color:green;">Supported</mark> by real-time, asynchronous, and batch requests.
* <mark style="color:green;">Supported</mark> Endpoints: [Web](https://docs.nimbleway.io/nimble-sdk/web-api)
* <mark style="color:red;">Not supported</mark> Endpoints: [Social](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/social-api), [SERP](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api), [Maps](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api) and [eCommerce](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api).
* Requires page rendering.
* Page Interactions are synchronous, so operations are run sequentially one by one
* The overall sequence is limited to a maximum timeout of **120 seconds**.&#x20;

{% hint style="warning" %}
Page Interactions will not function if rendering is not enabled in the request. Please be sure to set <mark style="color:red;background-color:yellow;">render:true</mark> in order for interactions to function correctly.
{% endhint %}

### Example Request  <a href="#example" id="example"></a>

If you wish to send POST data with your target domain as part of your request, such as when submitting a form, please use the following syntax:

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com",
    "render": true,
    "format": "json",
    "render_flow": [
        {
            "wait": {
                "delay": 500
            }
        }
    ]
}'
```

{% endtab %}
{% endtabs %}

Please note that specifying a content-type header is required when submitting a POST request with data in the body.

### Response

When a request with Page Interactions is completed, an additional property named <mark style="color:red;background-color:yellow;">render:true</mark> is included that contains a log detailing the result of each interaction. For each interaction, the following fields are present:

* **Name** – the interaction type (eg. scroll, wait\_and\_click, wait\_and\_type, etc).
* **Result** – some operations may return information. If there is information to return, <mark style="color:red;background-color:yellow;">result</mark> will contain the returned value, otherwise <mark style="color:red;background-color:yellow;">result</mark> will be true.
* **Error** – this field is only present if an error occurs, and details the type of error encountered.
* **Status** – the status of the interaction. Interactions can have one of four statuses:

| Status      | Description                                                                       |
| ----------- | --------------------------------------------------------------------------------- |
| no-run      | the interaction was not performed.                                                |
| in-progress | The interaction was in progress when the global 120-second timeout was triggered. |
| done        | the interaction finished successfully.                                            |
| error       | the interaction encountered an error.                                             |

The above request would produce the following response:

{% code overflow="wrap" %}

```json
{
    "status": "success",
    "html_content":"...",
    "render_flow": {
        "success": true,
        "results": [
            {
                "name": "wait",
                "status": "done",
                "result": true
            }
        ]
    }
}
```

{% endcode %}

### Optional Steps in Page Interaction Flow

The `required` parameter can be included in each step of the page interaction to mark whether the step must be executed. By default, all steps are considered mandatory (`required: true`). If a step is optional and can be skipped in case it does not occur or fails, set `required` to `false`.

This feature is useful when you have certain interactions that may not always be applicable or are not critical to the overall flow. If a step marked as `required: false` encounters an issue, the interaction chain will proceed to the next step without halting.

Below is an example request using the `required` parameter:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com",
    "render": true,
    "format": "json",
    "country": "US",
    "parse": true,
    "render_flow": [
        {
            "wait_and_type": {
                "selector": "input[type='\''search'\'']",
                "timeout": 2000,
                "value": "eggplant",
                "click_on_element": true
            }
        },
        {
            "wait": {
                "delay": 5000,
                "required":false
            }
        }
    ]
}'
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}

```python
import requests

url = 'https://api.webit.live/api/v1/realtime/web'
headers = {
    'Authorization': 'Basic <credential string>',
    'Content-Type': 'application/json'
}
data = {
    "url": "https://www.example.com",
    "render": True,
    "format": "json",
    "country": "US",
    "parse": True,
    "render_flow": [
        {
            "wait_and_type": {
                "selector": "input[type='search']",
                "timeout": 2000,
                "value": "eggplant",
                "click_on_element": True
            }
        },
        {
            "wait": {
                "delay": 5000,
                "required":False
            }
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/realtime/web';
const headers = {
  'Authorization': 'Basic <credential string>',
  'Content-Type': 'application/json'
};
const data = {
  "url": "https://www.example.com",
  "render": true,
  "format": "json",
  "country": "US",
  "parse": true,
  "render_flow": [
    {
      "wait_and_type": {
        "selector": "input[type='search']",
        "timeout": 2000,
        "value": "eggplant",
        "click_on_element": true
      }
    },
    {
      "wait": {
        "delay": 5000,
        "required":false
      }
    }
  ]
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
 "encoding/base64"
 "fmt"
 "net/http"
)

func main() {
 url := "https://api.webit.live/api/v1/realtime/web"
 payload := []byte(`{
  "url": "https://www.example.com",
  "render": true,
  "format": "json",
  "country": "US",
  "parse": true,
  "render_flow": [
   {
    "wait_and_type": {
     "selector": "input[type='search']",
     "timeout": 2000,
     "value": "eggplant",
     "click_on_element": true
    }
   },
   {
    "wait": {
     "delay": 5000,
     "required":false
    }
   }
  ]
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

### Chaining Page Interactions

Multiple interactions can be chained together and performed sequentially. To do this, simply add additional steps to the <mark style="color:red;background-color:yellow;">render:true</mark> property. When chaining interactions, it’s important to consider the maximum overall execution time of all the requested interactions.

Each request has a maximum timeout of 120 seconds for the overall execution, which includes all render flow interactions such as delays, clicks, scrolls, and timeouts if and when they occur.

Additionally, if any particular interaction encounters an error, interactions that come after it will not be executed. The chain is halted, and the data from the webpage is returned normally.

Below is an example of a request with several interactions chained together in a sequence:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com",
    "render": true,
    "format": "json",
    "country": "US",
    "parse": true,
    "render_flow": [
        {
            "wait_and_type": {
                "selector": "input[type='\''search'\'']",
                "timeout": 2000,
                "value": "eggplant",
                "click_on_element": true
            }
        },
        {
            "wait_and_click": {
                "selector": "#__next > div:nth-child(1) > div > span > header > form > div > button.absolute.bn.br-100.bg-gold.h3.w3 > i",
                "timeout": 2000
            }
        },
        {
            "wait_and_click": {
                "selector": "#maincontent > main > div > div:nth-child(2) section:nth-child(9) > div > h3 > button",
                "timeout": 5000,
                "scroll": true
            }
        },
        {
            "wait_and_click": {
                "selector": "input[name='\''Organic'\'']",
                "timeout": 2000
            }
        },
        {
            "wait": {
                "delay": 5000
            }
        }
    ]
}'
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}

```python
import requests

url = 'https://api.webit.live/api/v1/realtime/web'
headers = {
    'Authorization': 'Basic <credential string>',
    'Content-Type': 'application/json'
}
data = {
    "url": "https://www.example.com",
    "render": True,
    "format": "json",
    "country": "US",
    "parse": True,
    "render_flow": [
        {
            "wait_and_type": {
                "selector": "input[type='search']",
                "timeout": 2000,
                "value": "eggplant",
                "click_on_element": True
            }
        },
        {
            "wait_and_click": {
                "selector": "#__next > div:nth-child(1) > div > span > header > form > div > button.absolute.bn.br-100.bg-gold.h3.w3 > i",
                "timeout": 2000
            }
        },
        {
            "wait_and_click": {
                "selector": "#maincontent > main > div > div:nth-child(2) section:nth-child(9) > div > h3 > button",
                "timeout": 5000,
                "scroll": True
            }
        },
        {
            "wait_and_click": {
                "selector": "input[name='Organic']",
                "timeout": 2000
            }
        },
        {
            "wait": {
                "delay": 5000
            }
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/realtime/web';
const headers = {
  'Authorization': 'Basic <credential string>',
  'Content-Type': 'application/json'
};
const data = {
  "url": "https://www.example.com",
  "render": true,
  "format": "json",
  "country": "US",
  "parse": true,
  "render_flow": [
    {
      "wait_and_type": {
        "selector": "input[type='search']",
        "timeout": 2000,
        "value": "eggplant",
        "click_on_element": true
      }
    },
    {
      "wait_and_click": {
        "selector": "#__next > div:nth-child(1) > div > span > header > form > div > button.absolute.bn.br-100.bg-gold.h3.w3 > i",
        "timeout": 2000
      }
    },
    {
      "wait_and_click": {
        "selector": "#maincontent > main > div > div:nth-child(2) section:nth-child(9) > div > h3 > button",
        "timeout": 5000,
        "scroll": true
      }
    },
    {
      "wait_and_click": {
        "selector": "input[name='Organic']",
        "timeout": 2000
      }
    },
    {
      "wait": {
        "delay": 5000
      }
    }
  ]
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
 "encoding/base64"
 "fmt"
 "net/http"
)

func main() {
 url := "https://api.webit.live/api/v1/realtime/web"
 payload := []byte(`{
  "url": "https://www.example.com",
  "render": true,
  "format": "json",
  "country": "US",
  "parse": true,
  "render_flow": [
   {
    "wait_and_type": {
     "selector": "input[type='search']",
     "timeout": 2000,
     "value": "eggplant",
     "click_on_element": true
    }
   },
   {
    "wait_and_click": {
     "selector": "#__next > div:nth-child(1) > div > span > header > form > div > button.absolute.bn.br-100.bg-gold.h3.w3 > i",
     "timeout": 2000
    }
   },
   {
    "wait_and_click": {
     "selector": "#maincontent > main > div > div:nth-child(2) section:nth-child(9) > div > h3 > button",
     "timeout": 5000,
     "scroll": true
    }
   },
   {
    "wait_and_click": {
     "selector": "input[name='Organic']",
     "timeout": 2000
    }
   },
   {
    "wait": {
     "delay": 5000
    }
   }
  ]
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

When chaining interactions, the response will list a success/failed status for each interaction:

{% code overflow="wrap" %}

```json
{
    "status": "success",
    "html_content":"...",
    "render_flow": {
        "success": true,
        "results": [
            {
                "name": "wait_and_type",
                "status": "done",
                "result": true
            },
            {
                "name": "wait_and_click",
                "status": "done",
                "result": true
            },
            {
                "name": "wait_and_click",
                "status": "done",
                "result": true
            },
            {
                "name": "wait_and_click",
                "status": "done",
                "result": true
            },
            {
                "name": "wait",
                "status": "done",
                "result": true
            }
        ]
    }
}
```

{% endcode %}

### Failure Handling

The most common errors that are likely to occur include execution errors or timeouts. Most interaction functions include an optional timeout property that allows users to cap their execution time.

If an error is encountered in a chain of interactions, interactions that come after the failed interaction will not be executed. The data is collected from the web resource normally, and returned in accordance with the parameters of the associated request.

Additionally, the error encountered is returned to the user for debugging purposes. In the below example, the two initial interactions were executed successfully, followed by a failed interaction, and finally an interaction that was not executed because of the previously failed interaction:

{% code overflow="wrap" %}

```json
{
    "status": "success",
    "html_content":"...",
    "render_flow": {
        "success": false,
        "results": [
            {
                "name": "wait_and_type",
                "status": "done",
                "result": true
            },
            {
                "name": "wait_and_click",
                "status": "done",
                "result": true
            },
            {
                "name": "scroll",
                "status": "error",
                "error": "timeout"
            },
            {
                "name": "wait",
                "status": "no-run"
            }
        ]
    }
}
```

{% endcode %}
