# Source: https://docs.aimlapi.com/api-references/video-models/runway/gen3a_turbo.md

# gen3a\_turbo

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `gen3a_turbo`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/gen3a_turbo" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

An advanced AI model designed for converting images into high-quality videos. It allows users to generate dynamic video content with smooth motion and detailed textures from still images or text prompts, significantly enhancing creative workflows in multimedia production.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

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

You can generate a video using this API. In the basic setup, you need only an image URL and the aspect ratio of the desired result. The model can detect and use the aspect ratio from the input image, but for correct operation in this case, the image's width-to-height ratio must be between `0.5` and `2`.

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["gen3a_turbo"]},"prompt":{"type":"string","maxLength":1000,"description":"The text description of the scene, subject, or action to generate in the video."},"image_url":{"type":"string","format":"uri","description":"A HTTPS URL or data URI containing an encoded image to be used as the first frame of the generated video."},"tail_image_url":{"type":"string","format":"uri","description":"A HTTPS URL or data URI containing an encoded image to be used as the last frame of the generated video."},"aspect_ratio":{"type":"string","enum":["16:9","9:16"],"default":"16:9","description":"The aspect ratio of the generated video."},"duration":{"type":"integer","description":"The length of the output video in seconds.","enum":[5,10],"default":"5"},"seed":{"type":"integer","minimum":0,"maximum":4294967295,"description":"Varying the seed integer is a way to get different results for the same other request parameters. Using the same value for an identical request will produce similar results. If unspecified, a random number is chosen."}},"required":["model","image_url"],"title":"gen3a_turbo"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
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

Let’s take a beautiful but somewhat barren mountain landscape:

<figure><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Liebener_Spitze_SW.JPG/1280px-Liebener_Spitze_SW.JPG" alt=""><figcaption><p><a href="https://commons.wikimedia.org/wiki/File:Liebener_Spitze_SW.JPG">commons.wikimedia.org</a></p></figcaption></figure>

Then ask Gen4 Turbo to populate it with an epic reptilian creature using the following prompt:

*<mark style="background-color:blue;">"A menacing evil dragon appears in a distance above the tallest mountain, then rushes toward the camera with its jaws open, revealing massive fangs. We see it's coming"</mark>*

We combine both methods above in one program: first it sends a video generation request to the server, then it checks for results every 10 seconds.

{% hint style="warning" %}
Don’t forget to replace `<YOUR_AIMLAPI_KEY>` with your actual AI/ML API key from your [API Key management page](https://aimlapi.com/app/keys/) — in **both** places in the code!
{% endhint %}

</details>

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import time
import requests

# Creating and sending a video generation task to the server (returns a generation ID)
def generate_video():
    url = "https://api.aimlapi.com/v2/generate/video/runway/generation"
    payload = {
        "model": "gen3a_turbo",
        "prompt": "A menacing evil dragon appears in a distance above the tallest mountain, then rushes toward the camera with its jaws open, revealing massive fangs. We see it's coming",
        "ratio": "16:9",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Liebener_Spitze_SW.JPG/1280px-Liebener_Spitze_SW.JPG",
    }
    # Insert your AI/ML API key instead of <YOUR_AIMLAPI_KEY>:
    headers = {"Authorization": "Bearer <YOUR_AIMLAPI_KEY>", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code >= 400:
        print(f"Error: {response.status_code} - {response.text}")
    else:
        response_data = response.json()
        print("Generation:", response_data)
        return response_data


# Requesting the result of the generation task from the server using the generation_id:
def retrieve_video(gen_id):
    url = "https://api.aimlapi.com/v2/generate/video/runway/generation"
    params = {
        "generation_id": gen_id,
    }
    # Insert your AI/ML API key instead of <YOUR_AIMLAPI_KEY>:
    headers = {"Authorization": "Bearer <YOUR_AIMLAPI_KEY>", "Content-Type": "application/json"}

    response = requests.get(url, params=params, headers=headers)
    return response.json()
    
    
# This is the main function of the program. From here, we sequentially call the video generation and then repeatedly request the result from the server every 10 seconds:
def main():
    generation_response = generate_video()
    gen_id = generation_response.get("id")
        
    if gen_id:
        start_time = time.time()

        timeout = 600
        while time.time() - start_time < timeout:
            response_data = retrieve_video(gen_id)

            if response_data is None:
                print("Error: No response from API")
                break
        
            status = response_data.get("status")

            if status == "generating" or status == "queued" or status == "waiting":
                print("Still waiting... Checking again in 10 seconds.")
                time.sleep(10)
            else:
                print("Generation complete:/n", response_data)
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
Generation: {'id': 'd0cddca1-e382-4625-84c9-0817a6441876', 'status': 'queued'}
Still waiting... Checking again in 10 seconds.
Still waiting... Checking again in 10 seconds.
Still waiting... Checking again in 10 seconds.
Still waiting... Checking again in 10 seconds.
Still waiting... Checking again in 10 seconds.
Still waiting... Checking again in 10 seconds.
Still waiting... Checking again in 10 seconds.
Generation complete:/n {'id': 'd0cddca1-e382-4625-84c9-0817a6441876', 'status': 'completed', 'video': ['https://cdn.aimlapi.com/wolf/704dae4c-2ec9-4390-9625-abb52c359c4f.mp4?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiYjNjYzExNDU1YTJmODNmZCIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc0NDU4ODgwMH0.Jzmu6gPsBTTiZecKxSSwi9qk0-KSaHIgQbIOmCKe0Lk']}
```

{% endcode %}

</details>

The following video was generated by running the code example above. Processing time: \~25 sec.\
You may also check out the [original video in 1280×720 resolution](https://drive.google.com/file/d/1vDMftEwlfspfHPbDIpc2FhuirrsyC9B-/view?usp=sharing).

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-c86f48d97526e4f678e332f99b2aeedfa6d9bf85%2Frun3a_turbo_preview.gif?alt=media" alt=""><figcaption><p>"What... the hell are you?" (c)</p></figcaption></figure></div>
