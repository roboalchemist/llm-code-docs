# Source: https://docs.aimlapi.com/api-references/video-models/kling-ai/v1-standard-image-to-video.md

# v1-standard/image-to-video

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `kling-video/v1/standard/image-to-video`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/kling-video/v1/standard/image-to-video" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

A model transforms static images into dynamic video clips.

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

### Create a video generation task and send it to the server

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["kling-video/v1/standard/image-to-video"]},"image_url":{"type":"string","format":"uri","description":"A direct link to an online image or a Base64-encoded local image that will serve as the visual base or the first frame for the video."},"prompt":{"type":"string","description":"The text description of the scene, subject, or action to generate in the video."},"tail_image_url":{"type":"string","format":"uri","description":"A direct link to an online image or a Base64-encoded local image to be used as the last frame of the video."},"duration":{"type":"integer","description":"The length of the output video in seconds.","enum":[5,10],"default":"5"},"negative_prompt":{"type":"string","description":"The description of elements to avoid in the generated video."},"cfg_scale":{"type":"number","minimum":0,"maximum":1,"description":"The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt."},"static_mask":{"type":"string","format":"uri","description":"URL of the image for Static Brush Application Area (Mask image created by users using the motion brush)."},"dynamic_masks":{"type":"array","items":{"type":"object","properties":{"mask":{"type":"string"},"trajectories":{"type":"array","items":{"type":"object","properties":{"x":{"type":"integer"},"y":{"type":"integer"}},"required":["x","y"]},"minItems":2,"maxItems":77}},"required":["mask","trajectories"]},"maxItems":6,"description":"List of dynamic masks."},"camera_control":{"type":"object","properties":{"type":{"type":"string","enum":["simple","down_back","forward_up","right_turn_forward","left_turn_forward"]},"config":{"type":"object","properties":{"horizontal":{"type":"number","minimum":-10,"maximum":10},"vertical":{"type":"number","minimum":-10,"maximum":10},"pan":{"type":"number","minimum":-10,"maximum":10},"tilt":{"type":"number","minimum":-10,"maximum":10},"roll":{"type":"number","minimum":-10,"maximum":10},"zoom":{"type":"number","minimum":-10,"maximum":10}}}},"description":"Camera control parameters."}},"required":["model","image_url"],"title":"kling-video/v1/standard/image-to-video"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
```

### Retrieve the generated video from the server

After sending a request for video generation, this task is added to the queue. This endpoint lets you check the status of a video generation task using its `id`, obtained from the endpoint described above.\
If the video generation task status is `completed`, the response will include the final result — with the generated video URL and additional metadata.

## GET /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key","in":"header"}}},"paths":{"/v2/video/generations":{"get":{"operationId":"_v2_video_generations","parameters":[{"name":"generation_id","required":true,"in":"query","schema":{"type":"string"}}],"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
```

## Full Example: Generating and Retrieving the Video From the Server

We have a classic [reproduction](https://s2-111386.kwimgs.com/bs2/mmu-aiplatform-temp/kling/20240620/1.jpeg) of the famous da Vinci painting. Let's ask the model to generate a video where the Mona Lisa puts on glasses. The code below creates a video generation task, then automatically polls the server every **15** seconds until it finally receives the video URL.

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
        "model": "kling-video/v1/standard/image-to-video",
        "prompt": "Mona Lisa puts on glasses with her hands.",
        "image_url": "https://s2-111386.kwimgs.com/bs2/mmu-aiplatform-temp/kling/20240620/1.jpeg",
        "duration": "5",       
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

    # Try to retrieve the video from the server every 15 sec
    if gen_id:
        start_time = time.time()

        timeout = 1000   # 1000 sec = 16 min 40 sec 
        while time.time() - start_time < timeout:
            response_data = get_video(gen_id)

            if response_data is None:
                print("Error: No response from API")
                break

            status = response_data.get("status")
            
            if status in ["queued", "generating"]:
                print(f"Status: {status}. Checking again in 15 seconds.")
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

{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
const https = require("https");
const { URL } = require("url");

// Replace <YOUR_AIMLAPI_KEY> with your actual AI/ML API key
const apiKey = "<YOUR_AIMLAPI_KEY>";
const baseUrl = "https://api.aimlapi.com/v2";

// Creating and sending a video generation task to the server
function generateVideo(callback) {
  const data = JSON.stringify({
    model: "kling-video/v1/standard/image-to-video",
    prompt: "Mona Lisa puts on glasses with her hands.",
    image_url: "https://s2-111386.kwimgs.com/bs2/mmu-aiplatform-temp/kling/20240620/1.jpeg",
    duration: "5",
  });

  const url = new URL(`${baseUrl}/video/generations`);
  const options = {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${apiKey}`,
      "Content-Type": "application/json",
      "Content-Length": Buffer.byteLength(data),
    },
  };

  const req = https.request(url, options, (res) => {
    let body = "";
    res.on("data", (chunk) => body += chunk);
    res.on("end", () => {
      if (res.statusCode >= 400) {
        console.error(`Error: ${res.statusCode} - ${body}`);
        callback(null);
      } else {
        const parsed = JSON.parse(body);
        callback(parsed);
      }
    });
  });

  req.on("error", (err) => console.error("Request error:", err));
  req.write(data);
  req.end();
}

// Requesting the result of the task from the server using the generation_id
function getVideo(genId, callback) {
  const url = new URL(`${baseUrl}/video/generations`);
  url.searchParams.append("generation_id", genId);

  const options = {
    method: "GET",
    headers: {
      "Authorization": `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
  };

  const req = https.request(url, options, (res) => {
    let body = "";
    res.on("data", (chunk) => body += chunk);
    res.on("end", () => {
      const parsed = JSON.parse(body);
      callback(parsed);
    });
  });

  req.on("error", (err) => console.error("Request error:", err));
  req.end();
}

// Initiates video generation and checks the status every 15 seconds until completion or timeout
function main() {
    generateVideo((genResponse) => {
        if (!genResponse || !genResponse.id) {
            console.error("No generation ID received.");
            return;
        }

        const genId = genResponse.id;
        console.log("Generation ID:", genId);

        const timeout = 1000 * 1000; // 1000 sec = 16 min 40 sec
        const interval = 15 * 1000; // 15 sec
        const startTime = Date.now();

        const checkStatus = () => {
            if (Date.now() - startTime >= timeout) {
                console.log("Timeout reached. Stopping.");
                return;
            }

            getVideo(genId, (responseData) => {
                if (!responseData) {
                    console.error("Error: No response from API");
                    return;
                }

                const status = responseData.status;
        
                if (["queued", "generating"].includes(status)) {
                    console.log(`Status: ${status}. Checking again in 15 seconds.`);
                    setTimeout(checkStatus, interval);
                } else {
                    console.log("Processing complete:\n", responseData);
                }
            });
        };
        checkStatus();
    })
}

main();
```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Response</summary>

{% code overflow="wrap" %}

```json5
Generation ID:   nJ8Xcj0YCh8jZL1noqiZH
Status: queued. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Processing complete:
 {'id': 'nJ8Xcj0YCh8jZL1noqiZH', 'status': 'completed', 'video': {'url': 'https://cdn.aimlapi.com/kangaroo/bs2/upload-ylab-stunt-sgp/muse/784256485483880450/VIDEO/20260120/65936dd58d920424e4eb9c63ced58d91-95043990-9089-4f29-964f-bdb9dc8613ef.mp4?cacheKey=ChtzZWN1cml0eS5rbGluZy5tZXRhX2VuY3J5cHQSsAGF3eZphj1FFPB8b_FDXynExDTd0HvbX2EVjv4yP_Gmh8VWD9o5tDZwQTgxGhTON39FMvEafOs-MIqntimFHNbc87q1kSLAvr7i2unqGZPUcOSe1_QHuohz1ziHRpgZS5QJBgyVWcTO1O7rzPEBmcuVq2KAWv1-Hdtf2hsKUWGpM_ND2uqLgtOO3TSOxUW4L0sfxdTBkCzRgtGT8R-PlMk-18wbhrdtdjdDZ9G2KMw1jhoSS2Y9drB8Z4ednHxTIh7XZcnaIiBz78YUdtCCF-Oy9Z_9Dffy3JHkkjqHh7CM6cBjju3sJCgFMAE&x-kcdn-pid=112781&ksSecret=e2572bf52259a55921fce5697719d027&ksTime=6996dc99'}}
```

{% endcode %}

</details>

**Processing time**: \~4 min 9 sec.

**Original**: [832x1216](https://drive.google.com/file/d/1I4yUQanF_g_UppGrN188Zl0unxa5SG8i/view?usp=sharing) (without sound)

**Low-res GIF preview**:

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-31522b1702f0304ce7a4bb9fef1418413a284ec4%2Fkling-video-v1-standard-image-to-video_preview.gif?alt=media" alt=""><figcaption></figcaption></figure></div>
