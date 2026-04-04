# Source: https://docs.aimlapi.com/solutions/bagoodex/ai-search-engine/get-a-knowledge-structure.md

# Get a Knowledge Structure

## Overview

This is a description of one of the six use cases for the AI Search Engine—retrieving a small structured knowledge base on the requested subject based on information from the internet.

An output example:

{% code overflow="wrap" %}

```json
{
  'title': 'Nikola Tesla', 
  'type': 'Engineer and futurist', 
  'description': None, 
  'born': 'July 10, 1856, Smiljan, Croatia', 
  'died': 'January 7, 1943 (age 86 years), The New Yorker A Wyndham Hotel, New York, NY'
}
```

{% endcode %}

{% hint style="info" %}
The output will be the requested information retrieved from the internet—or empty brackets `{}` if nothing was found or if the entered query does not match the selected search type (for example, querying something like "I love Antarctica" instead of some topic).
{% endhint %}

## How to make a call

Check how this call is made in the [example](#example) below.

{% hint style="success" %}
Note that queries can include advanced search syntax:

* **Search for an exact match:** Enter a word or phrase using `\"` before and after it.\
  For example, `\"tallest building\"`.
* **Search for a specific site:** Enter `site:` in front of a site or domain. For example, `site:youtube.com cat videos`.
* **Exclude words from your search:** Enter `-` in front of a word that you want to leave out. For example, `jaguar speed -car`.
  {% endhint %}

## API Schema

## GET /v1/bagoodex/knowledge

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Bagoodex.v1.FetchKnowledgeResponseDTO":{"type":"object","properties":{"title":{"type":"string","nullable":true},"type":{"type":"string","nullable":true},"description":{"type":"string","nullable":true},"born":{"type":"string","nullable":true},"died":{"type":"string","nullable":true}}}}},"paths":{"/v1/bagoodex/knowledge":{"get":{"operationId":"BagoodexControllerV1_fetchKnowledge_v1","parameters":[{"name":"followup_id","required":true,"in":"query","schema":{"type":"string"}}],"responses":{"default":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Bagoodex.v1.FetchKnowledgeResponseDTO"}}}}},"tags":["Bagoodex"]}}}}
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
                "content": "Who is Nicola Tesla",
            },
        ],
    )
    
    # Extract the ID from the response
    gen_id = response.id  
    print(f"Generated ID: {gen_id}")
    
    # Call the second endpoint with the generated ID
    get_knowledge(gen_id)

def get_knowledge(gen_id):
    params = {'followup_id': gen_id}
    headers = {'Authorization': f'Bearer {API_KEY}'}
    
    response = requests.get(f'{API_URL}/v1/bagoodex/knowledge', headers=headers, params=params)
    print(response.json())

# Run the function
complete_chat()
```

{% endcode %}

**Model Response**:

{% code overflow="wrap" %}

```json
{
  'title': 'Nikola Tesla', 
  'type': 'Engineer and futurist', 
  'description': None, 
  'born': 'July 10, 1856, Smiljan, Croatia', 
  'died': 'January 7, 1943 (age 86 years), The New Yorker A Wyndham Hotel, New York, NY'
}
```

{% endcode %}
