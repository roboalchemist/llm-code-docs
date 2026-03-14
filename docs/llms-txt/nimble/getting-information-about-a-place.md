# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api/getting-information-about-a-place.md

# Getting information about a place

There are two ways to get additional information (address, description, rating, image, and more) about a particular place.

* [x] Using a `nimble_place_link` URL from a previous search request.
* [x] If you have a relevant `place_id` parameter, you can query the Places API directly. The `place_id` is an identifier used by Google, and can either be found externally from Nimble's Places API, or through a [search request](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api/searching-for-places).

### Following a `nimble_place_link`

In the [previous page](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api/searching-for-places), we used `google_maps_search` to search for a list of places with a query string and coordinates. In the response, each place result includes a `nimble_place_link` that, when accessed, returns additional data about that place.

For example, if the place link returned was:

{% code overflow="wrap" %}

```
https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&csrf_token=cjHpY_DuJqSr5NoP8P6wuAo&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8
```

{% endcode %}

Then the link would be accessed with the below example:

{% hint style="info" %}
Nimble APIs requires that a base64 encoded credential string be sent with every request to authenticate your account. For detailed examples, see [Web API Authentication](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/nimble-apis-authentication).
{% endhint %}

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl --location --request GET 'https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&csrf_token=cjHpY_DuJqSr5NoP8P6wuAo&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8' \
--header 'Authorization: Basic <credential string>'
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

url = f"https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&csrf_token=cjHpY_DuJqSr5NoP8P6wuAo&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8"
headers = {
    'Authorization': 'Basic <credential string>'
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())

```

{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code overflow="wrap" %}

```javascript
const axios = require('axios');

const url = `https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&csrf_token=cjHpY_DuJqSr5NoP8P6wuAo&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8`;
const headers = {
  'Authorization': 'Basic <credential string>'
};

axios.get(url, { headers })
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
)

func main() {
 url := "https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&csrf_token=cjHpY_DuJqSr5NoP8P6wuAo&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8"
 headers := map[string]string{
  "Authorization": "Basic <credential string>",
 }

 req, err := http.NewRequest("GET", url, nil)
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

### Using a place\_id

If you already have a `place_id` from a previous Places API search or otherwise, you can directly request information about that place, as in the example below:

{% tabs %}
{% tab title="cURL" %}

```bash
curl --location --request POST 'https://api.webit.live/api/v1/realtime/serp' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "search_engine": "google_maps_place",
    "place_id": "desired-place-id"
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
    "search_engine": "google_maps_place",
    "place_id": "desired-place-id"
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
  "search_engine": "google_maps_place",
  "place_id": "desired-place-id"
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
  "search_engine": "google_maps_place",
  "place_id": "desired-place-id"
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

{% hint style="info" %}
`place_id` and `data_id` are both identifiers used by Google to identify a particular location. Although both can be used to request reviews, their values are not interchangeable, and only one can be used at a time.
{% endhint %}

<details>

<summary>Structured Data Example</summary>

Nimble's Maps API uses AI to intelligently structure the rich information available through maps engines. For example, a request for the first place returned by the example on the previous page "Searching for Places" would return:

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
      "Place": [
        {
          "accessibility": [
            {
              "description": "Has wheelchair-accessible entrance",
              "display_name": "Wheelchair-accessible entrance",
              "full_path_name": "/geo/type/establishment_poi/has_wheelchair_accessible_entrance",
              "is_available": true
            },
            {
              "description": "No wheelchair-accessible car park",
              "display_name": "Wheelchair-accessible car park",
              "full_path_name": "/geo/type/establishment_poi/has_wheelchair_accessible_parking",
              "is_available": false
            }
          ],
          "address": "22 E 12th St, New York, NY 10003, United States",
          "amenities": [
            {
              "description": "Has toilets",
              "display_name": "Toilets",
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
          "csrf_token": "UxlSZcr1JaaKkdUPuduU2A8",
          "data_id": "0x89c25999ca135ddd:0xbd7ca23deaac9641",
          "entity_type": "Place",
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
          "phone_number": "+1 212-924-3364",
          "place_id": "ChIJ3V0TyplZwokRQZas6j2ifL0",
          "place_information": {
            "photos": [
              {
                "image_url": "https://lh5.googleusercontent.com/p/AF1QipO66T4V6dWFaljnukmm1X2X4Tc-P-FzTd2IVZT2=w114-h86-k-no",
                "latitude": "40.7341443",
                "longitude": "-73.9933229",
                "max_height": 3024,
                "max_width": 4032,
                "position": 0,
                "source_type": "photos:gmm_android_review_post"
              },
              {
                "image_url": "https://lh5.googleusercontent.com/p/AF1QipO66T4V6dWFaljnukmm1X2X4Tc-P-FzTd2IVZT2=w408-h306-k-no",
                "latitude": "40.7341443",
                "longitude": "-73.9933229",
                "max_height": 3024,
                "max_width": 4032,
                "position": 1,
                "source_type": "photos:gmm_android_review_post"
              }
            ],
            "reviews_link": "https://search.google.com/local/reviews?placeid=ChIJ3V0TyplZwokRQZas6j2ifL0&authuser=0&hl=en&gl=FR",
            "website_url": "https://www.cinemavillage.com/"
          },
          "place_url": "https://www.google.com/maps/search/?api=1&query=40.7340823%2C-73.9933681&query_place_id=ChIJ3V0TyplZwokRQZas6j2ifL0",
          "plus_code": {
            "compound_code": "P2M4+JM New York, USA",
            "global_code": "87G8P2M4+JM"
          },
          "position": 0,
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
          "top_reviews": [
            {
              "description": "We need to keep these small indie theatres alive! Cinema Village is an amazing venue for premiering your independent films and viewing arthouse cinema. Not only is this theatre a gem in the East Village but the staff, led by Lee, are so friendly and accommodating. I cannot wait for a week of fantastic works as I moderate for the Big Apple Film Festival at this awesome establishment.",
              "paging_token_id": "CAESBkVnSUlBUQ==",
              "photos": [
                {
                  "image_url": "https://lh5.googleusercontent.com/p/AF1QipNEBU61ILcPLvnjcW_TgzOw89jWXAoeX9DGuMHl=w150-h150-k-no-p",
                  "latitude": "40.73408227919416",
                  "longitude": "-73.99336813517314",
                  "position": 0,
                  "source_type": "photos:gmm_android_review_post"
                },
                {
                  "image_url": "https://lh5.googleusercontent.com/p/AF1QipN7AXhbnotnduvNt-av8CzAqzoz-HJ9UskIMHeo=w150-h150-k-no-p",
                  "latitude": "40.73408227919416",
                  "longitude": "-73.99336813517314",
                  "position": 1,
                  "source_type": "photos:gmm_android_review_post"
                },
                {
                  "image_url": "https://lh5.googleusercontent.com/p/AF1QipPQnDGLngWMGwGydsMESaeKPEYPpetK0mRp7evf=w150-h150-k-no-p",
                  "latitude": "40.73408227919416",
                  "longitude": "-73.99336813517314",
                  "position": 2,
                  "source_type": "photos:gmm_android_review_post"
                },
                {
                  "image_url": "https://lh5.googleusercontent.com/p/AF1QipOQWcaLA_xTWe5fA0rZrlSVX4U5g5_BbwkX7gYx=w150-h150-k-no-p",
                  "latitude": "40.73408227919416",
                  "longitude": "-73.99336813517314",
                  "position": 3,
                  "source_type": "photos:gmm_android_review_post"
                }
              ],
              "rating": "5",
              "relative_time": "5 months ago",
              "review_like_count": 2,
              "review_maps_link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChZDSUhNMG9nS0VJQ0FnSUN4cWVUMFpREAE!2m1!1s0x0:0xbd7ca23deaac9641!3m1!1s2@1:CIHM0ogKEICAgICxqeT0ZQ%7CCgwIofCjowYQ8IS0lAM%7C?hl=en-US",
              "review_timestamp": 1684600865848,
              "source_type": "",
              "user_image_link": "https://lh3.googleusercontent.com/a-/ALV-UjVRXxhQ_9fMvjxIIVZYUZ35tasZX8AZzZBCI6pWXbWvuN4y=s120-c-rp-mo-ba4-br100",
              "user_link": "https://www.google.com/maps/contrib/117486298571634574892?hl=en-US",
              "user_review_count": 64,
              "user_title": "Local Guide · 64 reviews",
              "username": "Hahn Films"
            },
            {
              "description": "Excellent theater. Hadn't been there in many years. Friend paid 4 ticket. We're seniors. Believe he said it was $8. Tuesday afternoon, 1pm show. Great price. They always have some movies that aren't mainstream. (We saw \"Beau Is Afraid\"). Highly recommend this theater 4 serious movie buffs.",
              "paging_token_id": "CAESBkVnSUlBZw==",
              "rating": "5",
              "relative_time": "4 months ago",
              "review_like_count": 0,
              "review_maps_link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSUNKdzZQaGhnRRAB!2m1!1s0x0:0xbd7ca23deaac9641!3m1!1s2@1:CIHM0ogKEICAgICJw6PhhgE%7CCgwIxeuMpQYQiPf-1QE%7C?hl=en-US",
              "review_timestamp": 1688417733448,
              "source_type": "",
              "user_image_link": "https://lh3.googleusercontent.com/a/ACg8ocLTggoi7C8fHIOe5u1rZMl673MueiJYmhabik4aNLXD=s120-c-rp-mo-br100",
              "user_link": "https://www.google.com/maps/contrib/106772929563499015372?hl=en-US",
              "user_review_count": 9,
              "user_title": "9 reviews",
              "username": "wayne miller"
            },
            {
              "description": "Nice little independent movie theater with great prices. The screen was on the smaller side but still good. Very, very small seating both in terms of width and legroom. I do not recommend if you're tall and/or heavy. I was so uncomfortable the entire time.",
              "paging_token_id": "CAESBkVnSUlBdw==",
              "rating": "3",
              "relative_time": "5 months ago",
              "review_like_count": 1,
              "review_maps_link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSUN4eHNLcDlnRRAB!2m1!1s0x0:0xbd7ca23deaac9641!3m1!1s2@1:CIHM0ogKEICAgICxxsKp9gE%7CCgwIz9yNowYQsMyinAI%7C?hl=en-US",
              "review_timestamp": 1684237903596,
              "source_type": "",
              "user_image_link": "https://lh3.googleusercontent.com/a-/ALV-UjUcXLgCBu-Fa1KxU1hXwo2xYO-Bau9vF5rxjuMHaNToo6w=s120-c-rp-mo-ba3-br100",
              "user_link": "https://www.google.com/maps/contrib/101939519956340079060?hl=en-US",
              "user_review_count": 11,
              "user_title": "11 reviews in New York",
              "username": "Romario Domi"
            },
            {
              "description": "Such a cute little theater which excellent prices. popcorn was 4 bucks and the ticket was 8. the theaters are small and first come first serve but i didn’t mind at all. saw barbie here and it was a great experience",
              "paging_token_id": "CAESBkVnSUlCQQ==",
              "rating": "5",
              "relative_time": "2 months ago",
              "review_like_count": 0,
              "review_maps_link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSUNwXzZmVjh3RRAB!2m1!1s0x0:0xbd7ca23deaac9641!3m1!1s2@1:CIHM0ogKEICAgICp_6fV8wE%7CCgwIidfkpgYQ2If3mgM%7C?hl=en-US",
              "review_timestamp": 1691954057861,
              "source_type": "",
              "user_image_link": "https://lh3.googleusercontent.com/a-/ALV-UjXGh801RkGhnRkDobIRgjW9BuC-hkPnyrQR7dNIIm0UiUdD=s120-c-rp-mo-br100",
              "user_link": "https://www.google.com/maps/contrib/115366795404356569896?hl=en-US",
              "user_review_count": 19,
              "user_title": "12 reviews in New York",
              "username": "Lydia Birnbaum"
            },
            {
              "description": "Stood in line for 40 mins for the open seating so we can choose the seats we wanted. We were first in line and when we were told to come in there were already about 15-20 people already seated that skipped the line knowingly. So just walk in and don’t waste your time waiting on the line outside.",
              "paging_token_id": "CAESBkVnSUlCUQ==",
              "rating": "1",
              "relative_time": "2 months ago",
              "review_like_count": 0,
              "review_maps_link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSURwZ19fbjJBRRAB!2m1!1s0x0:0xbd7ca23deaac9641!3m1!1s2@1:CIHM0ogKEICAgIDpg__n2AE%7CCgwIqKivpwYQiKH-pAI%7C?hl=en-US",
              "review_timestamp": 1693176872614,
              "source_type": "",
              "user_image_link": "https://lh3.googleusercontent.com/a/ACg8ocKPyxicptpt76D1iCIXeJlswOthPco87Jf4g6f87vNvcA=s120-c-rp-mo-ba3-br100",
              "user_link": "https://www.google.com/maps/contrib/103171436273609879112?hl=en-US",
              "user_review_count": 31,
              "user_title": "20 reviews in New York",
              "username": "Luis Rodriguez"
            },
            {
              "description": "Petit cinéma comprenant 3 salles dont une en sous sol. Contrairement à la France, quelques bandes annonces seulement sont projetées avant le film, pas de publicité. Le prix de la place est de 12$",
              "paging_token_id": "CAESBkVnSUlCZw==",
              "rating": "5",
              "relative_time": "3 months ago",
              "review_like_count": 0,
              "review_maps_link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSUNwMi1PYm5BRRAB!2m1!1s0x0:0xbd7ca23deaac9641!3m1!1s2@1:CIHM0ogKEICAgICp2-ObnAE%7CCgwI8vfWpgYQ4Ozv-gI%7C?hl=en-US",
              "review_timestamp": 1691728882794,
              "source_type": "",
              "user_image_link": "https://lh3.googleusercontent.com/a-/ALV-UjWNdwsdAIE24Fiz1A-RK6coeqazHx3S9GXMpBheaVPFqBs=s120-c-rp-mo-ba7-br100",
              "user_link": "https://www.google.com/maps/contrib/107173693758736440737?hl=en-US",
              "user_review_count": 384,
              "user_title": "8 movie theater reviews",
              "username": "Louis Laugeron"
            },
            {
              "description": "Super cute independent movie theater! The people working there as very nice, theater is clean, and tickets are cheap! Came here for the workers unite film festival and loved it. They also have really good pop corn. Would recommend coming here and supporting a small independent theater.",
              "paging_token_id": "CAESBkVnSUlCdw==",
              "photos": [
                {
                  "image_url": "https://lh5.googleusercontent.com/p/AF1QipOMVpBBDI3tjyCKTNnxLp6m8N1tpGXrV_iamlXY=w150-h150-k-no-p",
                  "latitude": "40.73408227919416",
                  "longitude": "-73.99336813517314",
                  "position": 0,
                  "source_type": "photos:gmm_ios_review_post"
                }
              ],
              "rating": "5",
              "relative_time": "2 years ago",
              "review_like_count": 5,
              "review_maps_link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSUQ2OTR1dHpnRRAB!2m1!1s0x0:0xbd7ca23deaac9641!3m1!1s2@1:CIHM0ogKEICAgID694utzgE%7CCgwIuKuhiwYQkKeywQI%7C?hl=en-US",
              "review_timestamp": 1634227640674,
              "source_type": "",
              "user_image_link": "https://lh3.googleusercontent.com/a-/ALV-UjXv6_U9vO1FoZsDOMvsKJIkU8YKYN-cibseZipVrJcFWARp=s120-c-rp-mo-ba5-br100",
              "user_link": "https://www.google.com/maps/contrib/105455022713764520173?hl=en-US",
              "user_review_count": 308,
              "user_title": "14 reviews in New York",
              "username": "Barbara d'Estaintot"
            },
            {
              "description": "This theatre is so much better than the AMC just a few blocks away. Less crowded and much cheaper.",
              "paging_token_id": "CAESBkVnSUlDQQ==",
              "rating": "5",
              "relative_time": "a month ago",
              "review_like_count": 0,
              "review_maps_link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSUNaN2ZPYnZBRRAB!2m1!1s0x0:0xbd7ca23deaac9641!3m1!1s2@1:CIHM0ogKEICAgICZ7fObvAE%7CCgsIrtaTqAYQuNrFJw%7C?hl=en-US",
              "review_timestamp": 1694821166082,
              "source_type": "",
              "user_image_link": "https://lh3.googleusercontent.com/a-/ALV-UjXE4uwIGsXyRlGcyBQ2f_C-vVwHr7cuB1K_c0JEefaxSzE=s120-c-rp-mo-br100",
              "user_link": "https://www.google.com/maps/contrib/106896244015474780630?hl=en-US",
              "user_review_count": 12,
              "user_title": "12 reviews",
              "username": "Elisa Chen"
            }
          ],
          "zip_code": "10003",
          "nimble_reviews_link": "https://api.webit.live/api/v1/realtime/serp?parse=true&search_engine=google_maps_reviews&place_id=ChIJ3V0TyplZwokRQZas6j2ifL0&domain=com&format=json&render=false&country=ALL&locale=en&csrf_token=UxlSZcr1JaaKkdUPuduU2A8"
        }
      ],
      "SearchResultMetaData": [
        {
          "entity_type": "SearchResultMetaData",
          "latitude": "",
          "longitude": "",
          "zoom": ""
        }
      ]
    },
    "total_entities_count": 2,
    "entities_count": {
      "Place": 1,
      "SearchResultMetaData": 1
    },
    "metrics": {}
  },
  "url": "https://www.google.com/maps/place?hl=en&ie=UTF-8&sourceid=chrome&oq=undefined&q=place_id%3AChIJ3V0TyplZwokRQZas6j2ifL0"
}
```

</details>

### Request options

<table><thead><tr><th width="176">Parameter</th><th width="155">Required</th><th width="211">Type</th><th>Description</th></tr></thead><tbody><tr><td>search_engine</td><td>Required</td><td>Enum: google_maps_search | google_maps_place | google_maps_reviews</td><td>The search engine from which to collect results.</td></tr><tr><td>place_id/data_id</td><td>Required</td><td>String</td><td>A string used by Google to identify a particular place. <code>place_id</code> and <code>data_id</code> cannot both be used in a single request.</td></tr><tr><td>domain</td><td>Optional</td><td>String</td><td>Search through a custom top-level domain of Google. eg: "co.uk"</td></tr><tr><td>country</td><td>Optional (default = all)</td><td>String</td><td>Country used to access the target URL, use ISO Alpha-2 Country Codes i.e. US, DE, GB</td></tr><tr><td>locale</td><td>Optional (default = en)</td><td>String</td><td>String | LCID standard locale used for the URL request. Alternatively, user can use <code>auto</code> for automatic locale based on country targeting.</td></tr><tr><td>parse</td><td>Optional (default = true)</td><td>Enum: true | false</td><td>Instructs Nimble whether to structure the results into a JSON format or return the raw HTML.</td></tr></tbody></table>

### Response

**200 - OK**

{% code overflow="wrap" %}

```json
{
    "status": "success",
    "html_content": "HTML...",
    "status_code": 200,
    "headers": {
        ...
    },
    "parsing": {
        "status": "success",
        "entities": {
            "Place": [
                {
                    ...
                    "nimble_reviews_link": "https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&domain=com&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8&csrf_token=TTfpY8XLE-SUwbkPobi1wAs"
                }
            ]
        },
        "total_entities_count": 1,
        "entities_count": {
            "Place": 1
        },
        "metrics": {}
    },
    "url": "https://www.google.com/maps/place?q=place_id:ChIJ_58pLKJZwokRvRwO5eftKC8"
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

Notice that in the above response, a `nimble_reviews_link` is included that allows for a separate Places API request to collect the reviews written by people about the targeted place. For more information on collecting reviews, see the [collecting-reviews](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api/collecting-reviews "mention") page.

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
