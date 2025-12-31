# Source: https://docs.aimlapi.com/solutions/bagoodex/ai-search-engine/find-links.md

# Find Links

## Overview

This is a description of one of the six use cases for this AI Search Engine—retrieving internet links related to the requested subject.

<details>

<summary>An output example</summary>

Request: *"*&#x73;ite:[www.reddit.com](http://www.reddit.com) A&#x49;*"*

Response:

{% code overflow="wrap" %}

```json
[
  "https://www.reddit.com/r/artificial/",
  "https://www.reddit.com/r/ArtificialInteligence/",
  "https://www.reddit.com/r/artificial/wiki/getting-started/",
  "https://www.reddit.com/r/ChatGPT/comments/1fwt2zf/it_is_officially_over_these_are_all_ai/",
  "https://www.reddit.com/r/ArtificialInteligence/comments/1f8wxe7/whats_the_most_surprising_way_ai_has_become_part/",
  "https://gist.github.com/nndda/a985daed53283a2c7fd399e11a185b11",
  "https://www.reddit.com/r/aivideo/",
  "https://www.reddit.com/r/singularity/",
  "https://www.abc.net.au/",
  "https://www.reddit.com/r/PromptEngineering/"
]
```

{% endcode %}

</details>

{% hint style="info" %}
The output will be the requested information retrieved from the internet—or empty brackets `[]` if nothing was found or if the entered query does not match the selected search type (for example, entering `'owtjtwjtwjtwojo'` instead of a valid subject).
{% endhint %}

## How to make a call

Check how this call is made in the [example ](#example)below.

{% hint style="success" %}
Note that queries can include advanced search syntax:

* **Search for an exact match:** Enter a word or phrase using `\"` before and after it.\
  For example, `\"tallest building\"`.
* **Search for a specific site:** Enter `site:` in front of a site or domain.\
  For example, `site:youtube.com cat videos`.
* **Exclude words from your search:** Enter `-` in front of a word that you want to leave out.\
  For example, `jaguar speed -car`.
  {% endhint %}

## API Schema

## GET /v1/bagoodex/links

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Bagoodex.v1.FetchLinksResponseDTO":{"type":"array","items":{"type":"string","format":"uri"}}}},"paths":{"/v1/bagoodex/links":{"get":{"operationId":"BagoodexControllerV1_fetchLinks_v1","parameters":[{"name":"followup_id","required":true,"in":"query","schema":{"type":"string"}}],"responses":{"default":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Bagoodex.v1.FetchLinksResponseDTO"}}}}},"tags":["Bagoodex"]}}}}
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
                "content": "site:www.reddit.com AI",
            },
        ],
    )
    
    # Extract the ID from the response
    gen_id = response.id  
    print(f"Generated ID: {gen_id}")
    
    # Call the second endpoint with the generated ID
    get_links(gen_id)

def get_links(gen_id):
    params = {'followup_id': gen_id}
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(f'{API_URL}/v1/bagoodex/links', headers=headers, params=params)
    
    print(response.json())

# Run the function
complete_chat()
```

{% endcode %}

**Model Response**:

{% code overflow="wrap" %}

```json
[
  "https://www.reddit.com/r/artificial/",
  "https://www.reddit.com/r/ArtificialInteligence/",
  "https://www.reddit.com/r/artificial/wiki/getting-started/",
  "https://www.reddit.com/r/ChatGPT/comments/1fwt2zf/it_is_officially_over_these_are_all_ai/",
  "https://www.reddit.com/r/ArtificialInteligence/comments/1f8wxe7/whats_the_most_surprising_way_ai_has_become_part/",
  "https://gist.github.com/nndda/a985daed53283a2c7fd399e11a185b11",
  "https://www.reddit.com/r/aivideo/",
  "https://www.reddit.com/r/singularity/",
  "https://www.abc.net.au/",
  "https://www.reddit.com/r/PromptEngineering/"
]
```

{% endcode %}
