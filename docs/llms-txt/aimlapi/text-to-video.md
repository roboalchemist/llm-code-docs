# Source: https://docs.aimlapi.com/api-references/video-models/magic/text-to-video.md

# magic/text-to-video

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `magic/text-to-video`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/magic/text-to-video" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

The model allows you to embed your custom text into the selected video template — sound included.

<details>

<summary>Supported Templates</summary>

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2F85fZRUUcfKC81HnmgHtj%2FShanghai%20Drone%20Show.gif?alt=media&#x26;token=b1500fdb-ca90-4082-9a9e-46b899cb2e20" alt=""><figcaption><p><code>"template": "Shanghai Drone Show"</code></p></figcaption></figure></div>

</details>

***

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schemas

Generating a video using this model involves sequentially calling two endpoints:

* The first one is for creating and sending a video generation task to the server (returns a generation ID).
* The second one is for requesting the generated video from the server using the generation ID received from the first endpoint.

Below, you can find two corresponding API schemas and an example with both endpoint calls.

### Create a video generation task and send it to the server

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["magic/text-to-video"]},"prompt":{"type":"string","description":"Text that will appear in the video."},"template":{"type":"string","enum":["Shanghai Drone Show"],"default":"Shanghai Drone Show","description":"Video design template."}},"required":["model","prompt"],"title":"magic/text-to-video"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
```

### Retrieve the generated video from the server

After sending a request for video generation, this task is added to the queue. This endpoint lets you check the status of a video generation task using its `id`, obtained from the endpoint described above.\
If the video generation task status is `completed`, the response will include the final result — with the generated video URL and additional metadata.

## GET /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key","in":"header"}}},"paths":{"/v2/video/generations":{"get":{"operationId":"_v2_video_generations","parameters":[{"name":"generation_id","required":true,"in":"query","schema":{"type":"string"}}],"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
```

## Code Example

The code below creates a video generation task, then automatically polls the server every **15** seconds until it finally receives the video URL.

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests
import time

# Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
api_key = "<YOUR_AIMLAPI_KEY>"
base_url = "https://api.aimlapi.com/v2"

# Creating and sending a video generation task to the server
def generate_video():
    url = f"{base_url}/video/generations"
    headers = {
        "Authorization": f"Bearer {api_key}", 
    }

    data = {
        "model": "magic/text-to-video",
        "prompt": "AI/ML API",
        "template": "Shanghai Drone Show"
    }
 
    response = requests.post(url, json=data, headers=headers)
    if response.status_code >= 400:
        print(f"Error: {response.status_code} - {response.text}")
    else:
        response_data = response.json()
        return response_data
    

# Requesting the result of the task from the server using the generation_id
def get_video(gen_id):
    url = f"{base_url}/video/generations"
    params = {
        "generation_id": gen_id,
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}", 
        "Content-Type": "application/json"
        }

    response = requests.get(url, params=params, headers=headers)
    return response.json()


def main():
     # Running video generation and getting a task id
    gen_response = generate_video()
    gen_id = gen_response.get("id")
    print("Generation ID:  ", gen_id)

    # Trying to retrieve the video from the server every 15 sec
    if gen_id:
        start_time = time.time()

        timeout = 1000
        while time.time() - start_time < timeout:
            response_data = get_video(gen_id)

            if response_data is None:
                print("Error: No response from API")
                break
        
            status = response_data.get("status")
            print("Status:", status)

            if status == "waiting" or status == "active" or  status == "queued" or status == "generating":
                print("Still waiting... Checking again in 15 seconds.")
                time.sleep(15)
            else:
                print("Processing complete:\n", response_data)
                return response_data
   
        print("Timeout reached. Stopping.")
        return None     


if __name__ == "__main__":
    main()
```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Response</summary>

{% code overflow="wrap" %}

```json5
Generation ID:   x6cwiGJM4VSX8msX6VtRX
Status: queued
Still waiting... Checking again in 15 seconds.
Status: generating
Still waiting... Checking again in 15 seconds.
Status: generating
Still waiting... Checking again in 15 seconds.
Status: generating
Still waiting... Checking again in 15 seconds.
Status: generating
Still waiting... Checking again in 15 seconds.
Status: generating
Still waiting... Checking again in 15 seconds.
Status: generating
Still waiting... Checking again in 15 seconds.
Status: generating
Still waiting... Checking again in 15 seconds.
Status: generating
Still waiting... Checking again in 15 seconds.
Status: completed
Processing complete:\n {'id': 'x6cwiGJM4VSX8msX6VtRX', 'status': 'completed', 'video': {'url': 'https://cdn.aimlapi.com/mule/ompr/openmagic/render_tasks/254262/1657f92e15fd427298b5e60e8eedcbce.mp4?response-content-disposition=attachment%3B%20filename%3D1657f92e15fd427298b5e60e8eedcbce.mp4&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=FUQDW4Z92RG9JPURIVP1%2F20251230%2Ffsn1%2Fs3%2Faws4_request&X-Amz-Date=20251230T132555Z&X-Amz-Expires=600&X-Amz-SignedHeaders=host&X-Amz-Signature=c5322a3ec963563674e1ea3447e978bc9d9325a854e30bc2ad8ab2563c2db9df'}}
```

{% endcode %}

</details>

**Processing time**: \~ 2 min 22 sec.

**Generated video** (608x1080, without sound):

{% embed url="<https://drive.google.com/file/d/1k9G9hk3SCdeJAAKOoKeuJQaytDASR2Qf/view>" %}
