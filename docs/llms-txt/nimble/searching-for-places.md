# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api/searching-for-places.md

# Searching for places

### Basic example

To search for places around a set of geographic coordinates, use the **/realtime/serp** endpoint and set `search_engine` to `google_maps_search`, as in the example below:

{% hint style="info" %}
Nimble APIs requires that a base64 encoded credential string be sent with every request to authenticate your account. For detailed examples, see [Web API Authentication](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/nimble-apis-authentication).
{% endhint %}

{% tabs %}
{% tab title="cURL" %}

```bash
curl --location --request POST 'https://api.webit.live/api/v1/realtime/serp' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "search_engine": "google_maps_search",
    "query": "Cinema",
    "coordinates": {
        "latitude": "40.7123695",
        "longitude": "-74.0357317"
    }
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
    "search_engine": "google_maps_search",
    "query": "Cinema",
    "coordinates": {
        "latitude": "40.7123695",
        "longitude": "-74.0357317"
    }
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
  "search_engine": "google_maps_search",
  "query": "Cinema",
  "coordinates": {
    "latitude": "40.7123695",
    "longitude": "-74.0357317"
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
  "search_engine": "google_maps_search",
  "query": "Cinema",
  "coordinates": {
   "latitude": "40.7123695",
   "longitude": "-74.0357317"
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

{% endtab %}
{% endtabs %}

<details>

<summary>Structured Data Example</summary>

Nimble's Maps API uses AI to intelligently structure the rich information available through maps engines. For example, the above request returns the following data:

```json
{
  "status": "success",
  "query_time": ...,
  "html_content": ...,
  "status_code": 200,
  "headers": {
    ...
  },
  "parsing": {
    "status": "success",
    "entities": {
      "SearchResult": [
        {
          "accessibility": [
            {
              "description": "Has wheelchair accessible entrance",
              "display_name": "Wheelchair accessible entrance",
              "full_path_name": "/geo/type/establishment_poi/has_wheelchair_accessible_entrance",
              "is_available": true
            },
            {
              "description": "No wheelchair accessible parking lot",
              "display_name": "Wheelchair accessible parking lot",
              "full_path_name": "/geo/type/establishment_poi/has_wheelchair_accessible_parking",
              "is_available": false
            }
          ],
          "address": "22 E 12th St, New York, NY 10003",
          "amenities": [
            {
              "description": "Has restroom",
              "display_name": "Restroom",
              "full_path_name": "/geo/type/establishment_poi/has_restroom",
              "is_available": true
            },
            {
              "description": "No restaurant",
              "display_name": "Restaurant",
              "full_path_name": "/geo/type/establishment_poi/has_restaurant",
              "is_available": false
            }
          ],
          "business_category": [
            "Movie theater"
          ],
          "business_description": [
            "Indie-film arthouse",
            "Longtime West Village theater known for showing offbeat & foreign movies, plus documentaries."
          ],
          "cid": "13653966557094385217",
          "city": "New York",
          "country": "US",
          "csrf_token": "LxdSZYbCIcWGptQPt5KHqAI",
          "data_id": "0x89c25999ca135ddd:0xbd7ca23deaac9641",
          "entity_type": "SearchResult",
          "highlights": [
            {
              "description": "Has live performances",
              "display_name": "Live performances",
              "full_path_name": "/geo/type/establishment_poi/has_live_performances",
              "is_available": true
            }
          ],
          "latitude": "40.7340823",
          "longitude": "-73.9933681",
          "number_of_reviews": "399",
          "offerings": [
            {
              "description": "Serves food",
              "display_name": "Food",
              "full_path_name": "/geo/type/establishment_poi/serves_food",
              "is_available": true
            }
          ],
          "page_index": 0,
          "payments": [
            {
              "description": "Accepts credit cards",
              "display_name": "Credit cards",
              "full_path_name": "/geo/type/establishment_poi/pay_credit_card",
              "is_available": true
            },
            {
              "description": "Accepts debit cards",
              "display_name": "Debit cards",
              "full_path_name": "/geo/type/establishment_poi/pay_debit_card",
              "is_available": true
            },
            {
              "description": "Accepts NFC mobile payments",
              "display_name": "NFC mobile payments",
              "full_path_name": "/geo/type/establishment_poi/pay_mobile_nfc",
              "is_available": true
            }
          ],
          "phone_number": "(212) 924-3364",
          "place_id": "ChIJ3V0TyplZwokRQZas6j2ifL0",
          "place_information": {
            "photos": [
              {
                "image_url": "https://lh5.googleusercontent.com/p/AF1QipPcB_h4ltcIsjDvReMUmep7pxEdIdmU_KoSDtB-=w114-h86-k-no",
                "latitude": "40.7341443",
                "longitude": "-73.9933229",
                "max_height": 3024,
                "max_width": 4032,
                "position": 0,
                "source_type": "photos:gmm_android"
              },
              {
                "image_url": "https://lh5.googleusercontent.com/p/AF1QipPcB_h4ltcIsjDvReMUmep7pxEdIdmU_KoSDtB-=w408-h306-k-no",
                "latitude": "40.7341443",
                "longitude": "-73.9933229",
                "max_height": 3024,
                "max_width": 4032,
                "position": 1,
                "source_type": "photos:gmm_android"
              }
            ],
            "reviews_link": "https://search.google.com/local/reviews?placeid=ChIJ3V0TyplZwokRQZas6j2ifL0&q=Cinema&authuser=0&hl=en&gl=US",
            "website_url": "https://www.cinemavillage.com/"
          },
          "place_url": "https://www.google.com/maps/search/?api=1&query=40.7340823%2C-73.9933681&query_place_id=ChIJ3V0TyplZwokRQZas6j2ifL0",
          "position": 1,
          "rating": "4.3 stars",
          "review_summary": {
            "overall_rating": 4.3,
            "ratings_count": {
              "1": 11,
              "2": 11,
              "3": 39,
              "4": 107,
              "5": 231
            },
            "review_count": 399
          },
          "sponsored": false,
          "street_address": "22 E 12th St",
          "title": "Cinema Village",
          "zip_code": "10003",
          "nimble_reviews_link": "https://api.webit.live/api/v1/realtime/serp?parse=true&search_engine=google_maps_reviews&domain=com&format=json&render=false&country=ALL&locale=en&csrf_token=LxdSZYbCIcWGptQPt5KHqAI&place_id=ChIJ3V0TyplZwokRQZas6j2ifL0",
          "nimble_place_link": "https://api.webit.live/api/v1/realtime/serp?parse=true&search_engine=google_maps_place&domain=com&format=json&render=false&country=ALL&locale=en&place_id=ChIJ3V0TyplZwokRQZas6j2ifL0"
        },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... },
  { ... }
      ],
      "SearchResultMetaData": [
        {
          "entity_type": "SearchResultMetaData",
          "latitude": "40.71236584",
          "longitude": "-74.03573171",
          "zoom": "13"
        }
      ]
    },
    "total_entities_count": 21,
    "entities_count": {
      "SearchResult": 20,
      "SearchResultMetaData": 1
    },
    "metrics": {}
  },
  "url": "https://www.google.com/maps/search/Cinema/@40.7123695,-74.0357317,14z?hl=en&ie=UTF-8&sourceid=chrome&oq=Cinema",
  "nimble_links": {
    "next_page": "https://api.webit.live/api/v1/realtime/serp?parse=true&search_engine=google_maps_search&query=Cinema&domain=com&coordinates=%4040.7123695%2C-74.0357317%2C14z&format=json&render=false&country=ALL&locale=en&offset=20"
  }
}
```

</details>

### Request options

<table><thead><tr><th width="168">Parameter</th><th width="155">Required</th><th width="211">Type</th><th>Description</th></tr></thead><tbody><tr><td>query</td><td>Required</td><td>String</td><td>The term or phrase to search for.</td></tr><tr><td>search_engine</td><td>Required</td><td>Enum: google_maps_search | google_maps_place | google_maps_reviews</td><td>The search engine from which to collect results.</td></tr><tr><td>coordinates</td><td>Optional</td><td>String or Object<br>"@{latitude},{longitude},{zoom}z"</td><td>The coordinates to target. When using a string, zoom is required.<br></td></tr><tr><td></td><td></td><td>"coordinates": { "latitude": "40.7590562", "longitude": "-74.0042502", <br>"zoom": "14" }</td><td>When using an object, zoom is optional.</td></tr><tr><td>offset</td><td>Optional</td><td>Integer</td><td>Offset the pagination position by this number of listings (eg: 20).</td></tr><tr><td>domain</td><td>Optional</td><td>String</td><td>Search through a custom top-level domain of Google. eg: "co.uk"</td></tr><tr><td>country</td><td>Optional (default = all)</td><td>String</td><td>Country used to access the target URL, use ISO Alpha-2 Country Codes i.e. US, DE, GB</td></tr><tr><td>locale</td><td>Optional (default = en)</td><td>String</td><td>String | LCID standard locale used for the URL request. Alternatively, user can use <code>auto</code> for automatic locale based on country targeting.</td></tr><tr><td>parse</td><td>Optional (default = true)</td><td>Enum: true | false</td><td>Instructs Nimble whether to structure the results into a JSON format or return the raw HTML.</td></tr></tbody></table>

### Response

**200 - OK**

If the request is executed successfully and parsing is either omitted or set to true, the output will resemble the example below:

{% code overflow="wrap" %}

```json
{
    "status": "success",
    "html_content": "...",
    "status_code": 200,
    "headers": {
        ...
    },
    "parsing": {
        "status": "success",
        "entities": {
            "SearchResult": [
                {
                    ...
                    "nimble_reviews_link": "https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&csrf_token=cjHpY_DuJqSr5NoP8P6wuAo&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8",
                    "nimble_place_link": "https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_place&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8"
                }, 
                {...}
            ]
        },
        "total_entities_count": 20,
        "entities_count": {
            "SearchResult": 20
        },
        "metrics": {}
    },
    "url": "https://www.google.com/maps/search/Cinema/@40.7123695,-74.0357317,14z",
    "nimble_links": {
        "next_page": "https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_search&query=Cinema&coordinates=%4040.7123695%2C-74.0357317%2C14z&offset=20"
    }
}
```

{% endcode %}

<details>

<summary>Supported parsing fields</summary>

Below is a list of all the fields supported by Nimble's parsing engine. This list is always growing and subject to change. Additionally, while Nimble supports all of these fields, which fields are available depends on the external search engine as well, and thus different fields will be available at different times.

```
PlusCode
PageIndex
Position
Title
Address
StreetAddress
ZipCode
City
Country
Floor
Sponsored
PlaceId
DataId
PlaceUrl
BusinessCategory
BusinessDescription
Rating
NumberOfReviews
PhoneNumber
Services*
Accessibility*
Offerings*
Planning*
Recycling*
Payments*
Highlights*
PopularFor*
DiningOptions*
Amenities*
Atmosphere*
Crowd*
PriceLevel
PlaceInformation
Longitude
Latitude
TopReviews
ReviewSummary
CsrfToken
DataIdLatitude
DataIdLongitude
LocatedIn
BusinessStatus
LastConfirmedStatus
```

\*marked fields vary according to the available data, and vary according to the creator of the Place.

</details>

#### Using reviews, place, and next\_page links

A successful result includes a number of follow-up links that can be used to get more information or browse through pagination. These include:

* [x] **`nimble_reviews_link`** - this link will trigger an additional Maps API request that returns the reviews for a particular place. Each place returned by the search will have its own reviews link. For more information, see the [collecting-reviews](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api/collecting-reviews "mention") page.
* [x] **`nimble_place_link`** - this link will trigger an additional Maps API request that returns additional data for a particular place. Each place returned by the search will have its own reviews link. For more information, see the [getting-information-about-a-place](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api/getting-information-about-a-place "mention") page.
* [x] **`next_page`** - Due to pagination, search results are displayed in groups of 20. If more than 20 results are found, the next set can be accessed using the `next_page` link. This triggers an additional Maps API request that fetches the next set of 20 search results, and will include an additional `next_page` link if there are surplus search results, and so on.

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
| 401    | Unauthorized/invalid credental string.         |
| 500    | Internal service error.                        |
| 501    | An error was encountered by the proxy service. |
