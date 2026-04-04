# Source: https://docs.aimlapi.com/solutions/bagoodex/ai-search-engine/find-a-local-map.md

# Find a Local Map

## Overview

This is a description of one of the six use cases for the AI Search Engine—retrieving a Google Maps link, a small picture of the map and coordinates of the requested place based on information from the internet.

**An output example**:

{% code overflow="wrap" %}

```json
{
  "link": "https://www.google.com/maps/place/San+Francisco,+CA/data=!4m2!3m1!1s0x80859a6d00690021:0x4a501367f076adff?sa=X&ved=2ahUKEwjqg7eNz9KLAxVCFFkFHWSPEeIQ8gF6BAgqEAA&hl=en",
  "image": "https://dmwtgq8yidg0m.cloudfront.net/images/TdNFUpcEvvHL-local-map.webp"
}
```

{% endcode %}

{% hint style="info" %}
The output will be the requested information retrieved from the internet—or empty brackets `{}` if nothing was found or if the entered query does not match the selected search type (for example, entering something like "wofujwofifwuowijufi").
{% endhint %}

## How to make a call <a href="#how-to-make-a-call" id="how-to-make-a-call"></a>

Check how this call is made in the [example ](#example)below.

{% hint style="success" %}
Note that queries can include advanced search syntax:

* **Search for an exact match:** Enter a word or phrase using `\"` before and after it.\
  For example, `\"tallest building\"`.
* **Search for a specific site:** Enter `site:` in front of a site or domain. For example, `site:youtube.com cat videos`.
* **Exclude words from your search:** Enter `-` in front of a word that you want to leave out. For example, `jaguar speed -car`.
  {% endhint %}

## API Schema

## GET /v1/bagoodex/local-map

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Bagoodex.v1.FetchLocalMapResponseDTO":{"type":"object","properties":{"link":{"type":"string","nullable":true},"image":{"type":"string","nullable":true,"format":"uri"},"gps_coordinates":{"type":"object","nullable":true,"properties":{"latitude":{"type":"number"},"longitude":{"type":"number"}},"required":["latitude","longitude"]}}}}},"paths":{"/v1/bagoodex/local-map":{"get":{"operationId":"BagoodexControllerV1_fetchLocalMap_v1","parameters":[{"name":"followup_id","required":true,"in":"query","schema":{"type":"string"}}],"responses":{"default":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Bagoodex.v1.FetchLocalMapResponseDTO"}}}}},"tags":["Bagoodex"]}}}}
```

## Example

First, the standard chat completion endpoint with your query is called. It returns an ID, which must then be passed as the sole input parameter `followup_id` to the specific second endpoint:

{% code overflow="wrap" %}

```python
import requests
from openai import OpenAI

# Insert your AIML API Key instead of <YOUR_API_KEY>:
API_KEY = '<YOUR_API_KEY>'
API_URL = 'https://api.aimlapi.com'

# Call the standart chat completion endpoint to get an ID
def complete_chat():
    client = OpenAI(
        base_url=API_URL,
        api_key=API_KEY,
    )    

    response = client.chat.completions.create(
        model="bagoodex/bagoodex-search-v1",
        messages=[
            {
                "role": "user",
                "content": "where is san francisco",
            },
        ],
    )
    
    # Extract the ID from the response
    gen_id = response.id  
    print(f"Generated ID: {gen_id}")
    
    # Call the second endpoint with the generated ID
    get_local_map(gen_id)

def get_local_map(gen_id):
    params = {'followup_id': gen_id}
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(f'{API_URL}/v1/bagoodex/local-map', headers=headers, params=params)
    
    print(response.json())

# Run the function
complete_chat()
```

{% endcode %}

**Model Response**:

{% code overflow="wrap" %}

```json
{
  "link": "https://www.google.com/maps/place/San+Francisco,+CA/data=!4m2!3m1!1s0x80859a6d00690021:0x4a501367f076adff?sa=X&ved=2ahUKEwjqg7eNz9KLAxVCFFkFHWSPEeIQ8gF6BAgqEAA&hl=en",
  "image": "https://dmwtgq8yidg0m.cloudfront.net/images/TdNFUpcEvvHL-local-map.webp"
}
```

{% endcode %}
