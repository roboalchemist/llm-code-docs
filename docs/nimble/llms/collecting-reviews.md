# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api/collecting-reviews.md

# Collecting reviews

There are two ways to collect reviews written for a particular place:

* [x] Using a `nimble_reviews_link` from a previous [search](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api/searching-for-places) or [place](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api/getting-information-about-a-place) request.
* [x] Directly with an existing `place_id` or `data_id`

### Following a `nimble_reviews_link`

Previously, we discussed how to search for places or directly request a place with a `place_id`, both of which produce a relevant `nimble_reviews_link` that can be used to request reviews for the relevant place. For example, for the following reviews link:

{% code overflow="wrap" %}

```
https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&csrf_token=cjHpY_DuJqSr5NoP8P6wuAo&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8
```

{% endcode %}

A request that executes the above reviews link would look like:

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

### Using a `place_id` or `data_id`

If you have a `place_id` or `data_id` from a previous search, place request, or independently from another source, you can use it to directly gather reviews left for that place. For example:

{% tabs %}
{% tab title="cURL" %}

```bash
curl --location --request POST 'https://api.webit.live/api/v1/realtime/serp' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "search_engine": "google_maps_reviews",
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
    "search_engine": "google_maps_reviews",
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
  "search_engine": "google_maps_reviews",
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
  "search_engine": "google_maps_reviews",
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

Nimble's Maps API uses AI to intelligently structure the rich information available through maps engines. For example, a request for the reviews returned by the example on the previous page "Getting Information about a Place" would return:

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
      "Review": [
        {
          "description": "We need to keep these small indie theatres alive! Cinema Village is an amazing venue for premiering your independent films and viewing arthouse cinema. Not only is this theatre a gem in the East Village but the staff, led by Lee, are so friendly and accommodating. I cannot wait for a week of fantastic works as I moderate for the Big Apple Film Festival at this awesome establishment.",
          "entity_type": "Review",
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
          "entity_type": "Review",
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
          "entity_type": "Review",
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
          "entity_type": "Review",
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
          "entity_type": "Review",
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
          "description": "Super cute independent movie theater! The people working there as very nice, theater is clean, and tickets are cheap! Came here for the workers unite film festival and loved it. They also have really good pop corn. Would recommend coming here and supporting a small independent theater.",
          "entity_type": "Review",
          "paging_token_id": "CAESBkVnSUlCZw==",
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
          "entity_type": "Review",
          "paging_token_id": "CAESBkVnSUlCdw==",
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
        },
        {
          "description": "Do get some good indies but bat around .500. Bathroom fixed up nicely.",
          "entity_type": "Review",
          "paging_token_id": "CAESBkVnSUlDQQ==",
          "rating": "3",
          "relative_time": "a month ago",
          "review_like_count": 0,
          "review_maps_link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChZDSUhNMG9nS0VJQ0FnSUNadTltT1JBEAE!2m1!1s0x0:0xbd7ca23deaac9641!3m1!1s2@1:CIHM0ogKEICAgICZu9mORA%7CCgwItImkqAYQiOS7pQI%7C?hl=en-US",
          "review_timestamp": 1695089844615,
          "source_type": "",
          "user_image_link": "https://lh3.googleusercontent.com/a/ACg8ocJj1bfh4-1VjIifJyqIvA3PBCnD1sR2azODONztHeoT=s120-c-rp-mo-ba3-br100",
          "user_link": "https://www.google.com/maps/contrib/114274661823064733648?hl=en-US",
          "user_review_count": 19,
          "user_title": "6 movie theater reviews",
          "username": "Alan M."
        },
        {
          "description": "I really liked this theater! I'm a bigger gal and I fit in the seats just fine.  Plenty of leg room, good popcorn.\n\nVERY NICE STAFF!! I went to see Thrust and I had pre-purchased my tickets and I thought I could just walk in. The clerk was so busy but he stuck his head out the door and very kindly checked on me and then was so nice about directing me back into the line. Talk about multi-tasking!!\n\nI will be back and often! 💗",
          "entity_type": "Review",
          "paging_token_id": "CAESBkVnSUlDUQ==",
          "rating": "5",
          "relative_time": "9 months ago",
          "review_like_count": 1,
          "review_maps_link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSUNoeXJtLTBnRRAB!2m1!1s0x0:0xbd7ca23deaac9641!3m1!1s2@1:CIHM0ogKEICAgIChyrm-0gE%7CCgsIqY6XnwYQwOWcHA%7C?hl=en-US",
          "review_timestamp": 1676003113059,
          "source_type": "",
          "user_image_link": "https://lh3.googleusercontent.com/a-/ALV-UjVdMQgrY8nuieIgzqhmvhVYh0Mf-_SaTlGVZsiGQUYyeHQ=s120-c-rp-mo-ba3-br100",
          "user_link": "https://www.google.com/maps/contrib/117283498811914066922?hl=en-US",
          "user_review_count": 29,
          "user_title": "10 reviews in New York",
          "username": "Kimberly"
        },
        {
          "description": "I'm all for supporting an independent movie theater. It is no frills, so expect smaller theater experience and advise getting there early for seats together. Also be mindful there are stairs to navigate for bathroom. Tickets and snack bar are cheaper, which reflects the experience as it's not the latest modern state of the art comfy theater. Even so, would return to enjoy a film!",
          "entity_type": "Review",
          "paging_token_id": "CAESBkVnSUlDZw==",
          "rating": "3",
          "relative_time": "9 months ago",
          "review_like_count": 1,
          "review_maps_link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSURCODhqQjdnRRAB!2m1!1s0x0:0xbd7ca23deaac9641!3m1!1s2@1:CIHM0ogKEICAgIDB88jB7gE%7CCgwIk_3TngYQ4L6-zQE%7C?hl=en-US",
          "review_timestamp": 1674903187430,
          "source_type": "",
          "user_image_link": "https://lh3.googleusercontent.com/a-/ALV-UjUYbXd2mVzuOZ_n2qn6-Dw2qX9FietkUxL-j3Kq-tJeZC9Z=s120-c-rp-mo-ba5-br100",
          "user_link": "https://www.google.com/maps/contrib/112033236948812333041?hl=en-US",
          "user_review_count": 274,
          "user_title": "Local Guide · 274 reviews",
          "username": "Connie Kwok"
        }
      ]
    },
    "total_entities_count": 10,
    "entities_count": {
      "Review": 10
    },
    "metrics": {}
  },
  "url": "https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=en&ie=UTF-8&sourceid=chrome&oq=undefined&pb=!1m2!1y9926595045733129693!2y13653966557094385217!2m1!2i10!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b0!5m2!1su3vM5w0ner0bHHQNqP0Ha3u!7e81",
  "nimble_links": {
    "next_page": "https://api.webit.live/api/v1/realtime/serp?parse=true&search_engine=google_maps_reviews&place_id=ChIJ3V0TyplZwokRQZas6j2ifL0&domain=com&coordinates=%4040.7123695%2C-74.0357317%2C14z&format=json&render=false&country=ALL&locale=en&paging_token_id=CAESBkVnSUlDZw%3D%3D"
  }
}
```

</details>

### Request options

<table><thead><tr><th width="181">Parameter</th><th width="155">Required</th><th width="211">Type</th><th>Description</th></tr></thead><tbody><tr><td>search_engine</td><td>Required</td><td>Enum: google_maps_search | google_maps_place | google_maps_reviews</td><td>The search engine from which to collect results.</td></tr><tr><td>place_id/data_id</td><td>Required</td><td>String</td><td>A string used by Google to identify a particular place. <code>place_id</code> and <code>data_id</code> cannot both be used in a single request.</td></tr><tr><td>sort</td><td>Optional</td><td><p>Enum:</p><p>relevant |</p><p>newest |</p><p>lowest_rating | highest_rating</p></td><td>Defines the order in which Google Maps reviews are returned.</td></tr><tr><td>domain</td><td>Optional</td><td>String</td><td>Search through a custom top-level domain of Google. eg: "co.uk"</td></tr><tr><td>country</td><td>Optional (default = all)</td><td>String</td><td>Country used to access the target URL, use ISO Alpha-2 Country Codes i.e. US, DE, GB</td></tr><tr><td>locale</td><td>Optional (default = en)</td><td>String</td><td>String | LCID standard locale used for the URL request. Alternatively, user can use <code>auto</code> for automatic locale based on country targeting.</td></tr><tr><td>parse</td><td>Optional (default = true)</td><td>Enum: true | false</td><td>Instructs Nimble whether to structure the results into a JSON format or return the raw HTML.</td></tr></tbody></table>

### Response

**200 - OK**

```json
{
    "status": "success",
    "html_content":"Protobuff output",
    "status_code": 200,
    "headers": {
        ...
    },
    "parsing": {
        "status": "success",
        "entities": {
            "Review": [
                {
                    "description": "Sample review body",
                    "entity_type": "Review",
                    "paging_token_id": "some-token-id",
                    "photos": [
                        {
                            "image_url": "wwww-sample-url.com",
                            "position": 0,
                            "source_type": "photos:gmm_ios_review_post"
                        }
                    ],
                    "rating": "5",
                    "relative_time": "2 months ago",
                    "review_like_count": 0,
                    "review_maps_link": "sample-review-url",
                    "review_timestamp": 1670529025279,
                    "source_type": "",
                    "user_image_link": "sample-image-url",
                    "user_link": "sample-user-url",
                    "user_review_count": 66,
                    "user_title": "Local Guide · 66 reviews",
                    "username": "sample-user"
                },
                {
                    ...
                },
                ...
            ]
        },
        "total_entities_count": 10,
        "entities_count": {
            "Review": 10
        },
        "metrics": {}
    },
    "url": "https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&pb=!1m2!1y9926595081738493951!2y3398227499087174845!2m1!2i10!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b0!5m2!1scjHpY_DuJqSr5NoP8P6wuAo!7e81",
    "nimble_links": {
        "next_page": "https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&csrf_token=cjHpY_DuJqSr5NoP8P6wuAo&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8&paging_token_id=CAESBkVnSUlDZw%3D%3D"
    }
}
```

<details>

<summary>Supported parsing fields</summary>

Below is a list of all the fields supported by Nimble's parsing engine. This list is always growing and subject to change. Additionally, while Nimble supports all of these fields, which fields are available depends on the external search engine as well, and thus different fields will be available at different times.

```
Username
UserLink
UserTitle
UserImageLink
Longitude
Latitude
SourceType
Description
Rating
ReviewMapsLink
UserReviewCount
ReviewLikeCount
ReviewTimestamp
PagingTokenId
Photos
```

</details>

When requesting reviews, the returned HTML will always be a `Google Protobuff output`. This is a result of Google Maps' output. We recommend always using the parsed data for maximum simplicity.

{% hint style="info" %}
The above example is for illustrative purposes only. Review data will vary in accordance with the reviews requested.
{% endhint %}

### Traversing paginated reviews

Some providers automatically paginate reviews so that only a certain number are displayed at once. If surplus reviews exist, an attribute named `next_page` will be present in Nimble's response which can be used to request the next batch of reviews.

In the above response, the `next_page` attribute contains the full address needed to request the next page's batch of reviews:

{% code overflow="wrap" %}

```
https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&csrf_token=cjHpY_DuJqSr5NoP8P6wuAo&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8&paging_token_id=CAESBkVnSUlDZw%3D%3D
```

{% endcode %}

The below example demonstrates how to use the provided `next_page` URL in a request:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl --location --request GET 'https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&csrf_token=cjHpY_DuJqSr5NoP8P6wuAo&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8&paging_token_id=CAESBkVnSUlDZw%3D%3D' \
--header 'Authorization: Basic <credential string>'
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

url = f"https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&csrf_token=cjHpY_DuJqSr5NoP8P6wuAo&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8&paging_token_id=CAESBkVnSUlDZw%3D%3D"
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

const url = `https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&csrf_token=cjHpY_DuJqSr5NoP8P6wuAo&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8&paging_token_id=CAESBkVnSUlDZw%3D%3D`;
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
 url := "https://api.webit.live/api/v1/realtime/serp?search_engine=google_maps_reviews&csrf_token=cjHpY_DuJqSr5NoP8P6wuAo&place_id=ChIJ_58pLKJZwokRvRwO5eftKC8&paging_token_id=CAESBkVnSUlDZw%3D%3D"
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
