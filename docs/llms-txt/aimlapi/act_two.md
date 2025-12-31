# Source: https://docs.aimlapi.com/api-references/video-models/runway/act_two.md

# act\_two

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `runway/act_two`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/runway/act_two" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

This video-to-video model lets you animate characters using reference performance videos. Simply provide a video of someone acting out a scene along with a character reference (image or video), and Act-Two will transfer the performance to your character — including natural motion, speech, and facial expressions.

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

You can generate a video using this API. In the basic setup, you only need an image or video URL for the character (`character`), and a video URL for body movements and/or facial expressions (`reference`).

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["runway/act_two"]},"character":{"oneOf":[{"type":"object","properties":{"type":{"type":"string","enum":["video"]},"url":{"type":"string","format":"uri"}},"required":["type","url"],"description":"A video of your character. In the output, the character will use the reference video performance in its original animated environment and some of the character's own movements."},{"type":"object","properties":{"type":{"type":"string","enum":["image"]},"url":{"type":"string","format":"uri"}},"required":["type","url"],"description":"An image of your character. In the output, the character will use the reference video performance in its original static environment."}],"description":"The character to control. You can either provide a video or an image. A visually recognizable face must be visible and stay within the frame."},"reference":{"type":"object","properties":{"type":{"type":"string","enum":["video"]},"url":{"type":"string","format":"uri"}},"required":["type","url"],"description":"Passing a video reference allows the model to emulate the style or content of the reference in the output."},"frame_size":{"type":"string","enum":["1280:720","720:1280","1104:832","832:1104","960:960","1584:672","848:480","640:480"],"default":"1280:720","description":"The width and height of the video."},"body_control":{"type":"boolean","description":"A boolean indicating whether to enable body control. When enabled, non-facial movements and gestures will be applied to the character in addition to facial expressions."},"expression_intensity":{"type":"integer","minimum":1,"maximum":5,"default":3,"description":"An integer between 1 and 5 (inclusive). A larger value increases the intensity of the character's expression."},"seed":{"type":"integer","minimum":0,"maximum":4294967295,"description":"Varying the seed integer is a way to get different results for the same other request parameters. Using the same value for an identical request will produce similar results. If unspecified, a random number is chosen."}},"required":["model","character","reference"],"title":"runway/act_two"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
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

As the character reference, we will use a scan of a famous Leonardo da Vinci painting. For the motion reference, we will use a video of a cheerful woman dancing, generated with the [kling-video/v1.6/pro/text-to-video](https://docs.aimlapi.com/api-references/video-models/kling-ai/v1.6-pro-text-to-video) model.

| Character reference image                                                                                                                                                                                                                                                    | Motion reference video                                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-4e97bf7abf2db1d3ac4f07282dafa0d3eeb75f20%2Fmona-lisa.jpeg?alt=media" alt=""><figcaption></figcaption></figure></div> | <div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-bffa63fdb02b677ff567b109dc6cda967d87532c%2Frunway-act-two-preview.gif?alt=media" alt=""><figcaption></figcaption></figure></div> |

We combine both POST and GET methods above in one program: first it sends a video generation request to the server, then it checks for results every 10 seconds.

{% hint style="warning" %}
Don’t forget to replace `<YOUR_AIMLAPI_KEY>` with your actual AI/ML API key from your [API Key management page](https://aimlapi.com/app/keys/) — in **both** places in the code!
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
        "model": "runway/act_two",
        "character":
            {
                "type":"image",
                "url":"https://s2-111386.kwimgs.com/bs2/mmu-aiplatform-temp/kling/20240620/1.jpeg"
            },
        "reference":
            {
                "type":"video",
                "url": "https://zovi0.github.io/public_misc/kling-video-v1.6-pro-text-to-video-dancing-woman-output.mp4"
            },
        "frame_size":"1280:720",
        "body_control":True,
        "expression_intensity":3
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
{'id': 'dbf7a50e-87b2-4ba5-921f-f02fdb8f7cc6', 'status': 'queued'}
Generation ID:   dbf7a50e-87b2-4ba5-921f-f02fdb8f7cc6
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: generating
Still waiting... Checking again in 10 seconds.
Status: completed
Processing complete:/n {'id': 'dbf7a50e-87b2-4ba5-921f-f02fdb8f7cc6', 'status': 'completed', 'video': ['https://cdn.aimlapi.com/wolf/d462f7e3-bdc6-43ac-8c2a-ac2d61dea014.mp4?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNzZmNzY0NDRiZTViYWI2YyIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc1NDc4NDAwMH0._q7rh2fmm7a16k7UHAnDh3aUOIy-fT8NJO3hP-KT4_s']}
```

{% endcode %}

</details>

The following video was generated by running the code example above.\
Processing time: \~45 sec.\
Original: [784×1168](https://drive.google.com/file/d/1QzqNY6tZdyDh1P5mn3_7QsAPOeoUqtYA/view?usp=sharing)

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-41260566923ecd9bd940c4195cb67e637c287a13%2Frunway-act-two-preview.gif?alt=media" alt=""><figcaption><p>Low-resolution GIF preview</p></figcaption></figure></div>
