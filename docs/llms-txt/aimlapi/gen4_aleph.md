# Source: https://docs.aimlapi.com/api-references/video-models/runway/gen4_aleph.md

# gen4\_aleph

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `runway/gen4_aleph`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/runway/gen4_aleph" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

This is a video-to-video model capable of either modifying the input video or generating the next shot in a story that begins in the input and continues based on your prompt. You can define camera angles and movements, alter the plot, change character appearances, or adjust the environment.

## How to Make a Call

<details>

<summary>Step-by-Step Instructions</summary>

Generating a video using this model involves sequentially calling two endpoints:

* The first one is for creating and sending a video generation task to the server (returns a generation ID).
* The second one is for requesting the generated video from the server using the generation ID received from the first endpoint.

Below, you can find both corresponding API schemas.

</details>

## API Schemas

{% hint style="success" %}
Now, all of our API schemas for video models use our new universal short URL — `https://api.aimlapi.com/v2/video/generations`. \
However, you can still call this model using the legacy URL that includes the vendor name.
{% endhint %}

### Video Generation

You can generate a video using this API. In the basic setup, you need only a video URL and a prompt.

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["runway/gen4_aleph"]},"prompt":{"type":"string","maxLength":1000,"description":"The text description of the scene, subject, or action to generate in the video."},"video_url":{"type":"string","format":"uri","description":"A HTTPS URL pointing to a video or a data URI containing a video. This video will be used as a reference during generation."},"references":{"type":"array","items":{"type":"object","properties":{"type":{"type":"string","enum":["image"]},"url":{"type":"string","format":"uri"}},"required":["type","url"]},"description":"Passing an image reference allows the model to emulate the style or content of the reference in the output."},"frame_size":{"type":"string","enum":["1280:720","720:1280","1104:832","832:1104","960:960","1584:672","848:480","640:480"],"default":"1280:720","description":"The width and height of the video."},"duration":{"type":"number","enum":[5],"default":5,"description":"The length of the output video in seconds."},"seed":{"type":"integer","minimum":0,"maximum":4294967295,"description":"Varying the seed integer is a way to get different results for the same other request parameters. Using the same value for an identical request will produce similar results. If unspecified, a random number is chosen."}},"required":["model","prompt","video_url"],"title":"runway/gen4_aleph"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
```

### Retrieve the generated video from the server

After sending a request for video generation, this task is added to the queue. This endpoint lets you check the status of a video generation task using its `id`, obtained from the endpoint described above.\
If the video generation task status is `complete`, the response will include the final result — with the generated video URL and additional metadata.

## GET /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"get":{"operationId":"VideoControllerV2_pollVideo_v2","parameters":[{"name":"generation_id","required":true,"in":"query","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully generated video","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Video.v2.PollVideoResponseDTO"}}}}},"tags":["Video Models"]}}},"components":{"schemas":{"Video.v2.PollVideoResponseDTO":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."},"duration":{"type":"number","nullable":true,"description":"The duration of the video."}},"required":["url"]},"duration":{"type":"number","nullable":true,"description":"The duration of the video."},"error":{"nullable":true,"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}
```

## Full Example: Generating and Retrieving the Video From the Server

<details>

<summary>How it works</summary>

Let’s take a video of our running raccoon and ask Aleph to add a small fairy riding on its back. Here’s the prompt we can use:

*`"`*`Add a small fairy as a rider on the raccoon’s back. She must have a black-and-golden face and a cloak in the colors of a dark emerald tropical butterfly with bright blue shimmering spots.`*`"`*

We combine both methods above in one program: first it sends a video generation request to the server, then it checks for results every 10 seconds.

{% hint style="warning" %}
Don’t forget to replace `<YOUR_AIMLAPI_KEY>` with your actual AI/ML API key from your [API Key management page](https://aimlapi.com/app/keys/)!
{% endhint %}

</details>

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests
import time

# replace <YOUR_AIMLAPI_KEY> with your actual AI/ML API key
api_key = "<YOUR_AIMLAPI_KEY>"
base_url = "https://api.aimlapi.com/v2"


# Creating and sending a video generation task to the server
def generate_video():
    url = f"{base_url}/generate/video/runway/generation"
    headers = {
        "Authorization": f"Bearer {api_key}", 
    }

    data = {
        "model": "runway/gen4_aleph",
        "video_url":"https://zovi0.github.io/public_misc/kling-v2-master-t2v-racoon.mp4",
        "prompt":'''
            Add a small fairy as a rider on the raccoon’s back. She must have a black-and-golden face and a cloak in the colors of a dark emerald tropical butterfly with bright blue shimmering spots.
        '''
    }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code >= 400:
        print(f"Error: {response.status_code} - {response.text}")
    else:
        response_data = response.json()
        print(response_data)
        return response_data
    

# Requesting the result of the task from the server using the generation_id
def get_video(gen_id):
    url = f"{base_url}/generate/video/runway/generation"
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

    # Trying to retrieve the video from the server every 10 sec
    if gen_id:
        start_time = time.time()

        timeout = 1800
        while time.time() - start_time < timeout:
            response_data = get_video(gen_id)

            if response_data is None:
                print("Error: No response from API")
                break
        
            status = response_data.get("status")
            print("Status:", status)

            if status == "waiting" or status == "active" or  status == "queued" or status == "generating":
                print("Still waiting... Checking again in 10 seconds.")
                time.sleep(10)
            else:
                print("Processing complete:/n", response_data)
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
{'id': '6d6c768f-702e-4737-a3c9-0c6c6f4fec0a', 'status': 'queued'}
Generation ID:   6d6c768f-702e-4737-a3c9-0c6c6f4fec0a
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: completed
Processing complete:/n {'id': '6d6c768f-702e-4737-a3c9-0c6c6f4fec0a', 'status': 'completed', 'video': ['https://cdn.aimlapi.com/wolf/cbd4bc0a-e4dd-45be-abb4-fa95b014dc46.mp4?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiY2YzNmNmZDVkMDcwZDcxNyIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc1NTA0MzIwMH0.nsiluZQnDhkSr5peYkbNFLeUxn7vJ59C1ablCEm9CSI']}
```

{% endcode %}

</details>

**Processing time**: \~3 min 30 sec.\
**Original**: [1280×720](https://drive.google.com/file/d/1x_AYR09NphtcDpBykCx8u4Kq7AAdgJIt/view?usp=sharing)\
**Low-res GIF preview**:

<table data-full-width="false"><thead><tr><th>Reference Video</th><th>Generated (Edited) Video</th></tr></thead><tbody><tr><td><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-b466370bbb89c643b4a445ebff357982fd4a7f60%2F%D0%B5%D0%BD%D1%82%D0%BE%20%D0%B8%20%D1%81%D0%B5%D0%BA%D0%B2%D0%BE%D0%B9%D0%B8.gif?alt=media" alt=""><figcaption></figcaption></figure></div></td><td><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-38a50b34bc4037e289add78fe4b0b41a0e3ac6a8%2Frunway-aleph-preview.gif?alt=media" alt=""><figcaption></figcaption></figure></div></td></tr></tbody></table>
