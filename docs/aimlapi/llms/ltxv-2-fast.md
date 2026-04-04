# Source: https://docs.aimlapi.com/api-references/video-models/ltxv/ltxv-2-fast.md

# ltxv-2-fast

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `ltxv/ltxv-2-fast`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/ltxv/ltxv-2-fast" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

The model generates realistic 6-, 8-, and 10-second videos (up to 4K resolution) with detailed visuals and audio. Runs a little faster while delivering video of somewhat lower quality than [LTXV 2](https://docs.aimlapi.com/api-references/video-models/ltxv/ltxv-2).

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

### Create a video generation task and send it to the server

You can generate a video using this API. In the basic setup, you only need a prompt.\
This endpoint creates and sends a video generation task to the server — and returns a generation ID.

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["ltxv/ltxv-2-fast"]},"prompt":{"type":"string","description":"The text description of the scene, subject, or action to generate in the video."},"image_url":{"type":"string","format":"uri","description":"A direct link to an online image or a Base64-encoded local image that will serve as the visual base or the first frame for the video."},"duration":{"type":"integer","description":"The length of the output video in seconds.","enum":[6,8,10]},"resolution":{"type":"string","enum":["1080p","1440p","2160p"],"default":"1080p","description":"The resolution of the output video, where the number refers to the short side in pixels."},"aspect_ratio":{"type":"string","enum":["16:9"],"default":"16:9","description":"The aspect ratio of the generated video."},"fps":{"type":"integer","description":"Frames per second of the generated video.","enum":[25,50]},"generate_audio":{"type":"boolean","default":true,"description":"Whether to generate audio for the video."}},"required":["model","prompt"],"title":"ltxv/ltxv-2-fast"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
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

The code below creates a video generation task, then automatically polls the server every **15** seconds until it finally receives the video URL.

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests
import time

# Insert your AI/ML API key instead of <YOUR_AIMLAPI_KEY>:
api_key = "<YOUR_AIMLAPI_KEY>"

# Creating and sending a video generation task to the server
def generate_video():
    url = "https://api.aimlapi.com/v2/video/generations"
    headers = {
        "Authorization": f"Bearer {api_key}", 
    }

    data = {
        "model": "ltxv/ltxv-2-fast",
        "prompt": "A menacing evil dragon appears in a distance above the tallest mountain, then rushes toward the camera with its jaws open, revealing massive fangs. We see it's coming. He's roaring: WHERE ARE MY TREASURES?",
        "duration": 6 
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
    url = "https://api.aimlapi.com/v2/video/generations"
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
    # Generate video
    gen_response = generate_video()
    gen_id = gen_response.get("id")
    print("Generation ID:  ", gen_id)

    # Try to retrieve the video from the server every 15 sec
    if gen_id:
        start_time = time.time()

        timeout = 600
        while time.time() - start_time < timeout:
            response_data = get_video(gen_id)

            if response_data is None:
                print("Error: No response from API")
                break

            status = response_data.get("status")
            
            if status in ["waiting", "active", "queued", "generating"]:
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
    model: "ltxv/ltxv-2-fast",
    prompt: "Mona Lisa puts on glasses with her hands.",
    image_url: "https://s2-111386.kwimgs.com/bs2/mmu-aiplatform-temp/kling/20240620/1.jpeg",
    duration: "5",
  });

  const url = new URL(`${baseUrl}/generate/video/google/generation`);
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
  const url = new URL(`${baseUrl}/generate/video/google/generation`);
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

// Initiates video generation and checks the status every 10 seconds until completion or timeout
function main() {
  generateVideo((genResponse) => {
    if (!genResponse || !genResponse.id) {
      console.error("Failed to start generation");
      return;
    }

    const genId = genResponse.id;
    console.log("Gen_ID:", genId);

    const startTime = Date.now();
    const timeout = 600000;

    const checkStatus = () => {
      if (Date.now() - startTime > timeout) {
        console.log("Timeout reached. Stopping.");
        return;
      }

      getVideo(genId, (responseData) => {
        if (!responseData) {
          console.error("Error: No response from API");
          return;
        }

        const status = responseData.status;
        console.log("Status:", status);

        if (["waiting", "active", "queued", "generating"].includes(status)) {
          console.log("Still waiting... Checking again in 10 seconds.");
          setTimeout(checkStatus, 10000);
        } else {
          console.log("Processing complete:\n", responseData);
        }
      });
    };

    checkStatus();
  });
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
{'id': 'fb77b923-55da-4e4d-9519-5c0018088c52:ltxv/ltxv-2-fast', 'status': 'queued', 'meta': {'usage': {'tokens_used': 504000}}}
Generation ID:   fb77b923-55da-4e4d-9519-5c0018088c52:ltxv/ltxv-2-fast
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Processing complete:
 {'id': 'fb77b923-55da-4e4d-9519-5c0018088c52:ltxv/ltxv-2-fast', 'status': 'completed', 'video': {'url': 'https://cdn.aimlapi.com/flamingo/files/b/tiger/qo7CU4MIQp7MqapedpsnK_E4p6CCTs.mp4'}}
```

{% endcode %}

</details>

**Processing time**: 58.9 sec.

**Generated Video** (1920x1080, with sound):

{% embed url="<https://drive.google.com/file/d/1rIHVgEmcPI6ulNLyuqASC-TUYQ89v-U1/view>" %}
