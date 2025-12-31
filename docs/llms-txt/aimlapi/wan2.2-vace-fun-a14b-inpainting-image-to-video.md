# Source: https://docs.aimlapi.com/api-references/video-models/alibaba-cloud/wan2.2-vace-fun-a14b-inpainting-image-to-video.md

# Wan 2.2 VACE Fun Inpainting (Image-to-Video)

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `alibaba/wan2.2-vace-fun-a14b-inpainting`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/alibaba/wan2-2-vace-fun-a14b-inpainting" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

A video generation model that combines a source image, mask, and reference video to produce prompted videos with precise source control.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## How to Make a Call

<details>

<summary>Step-by-Step Instructions</summary>

Generating a video using this model involves sequentially calling two endpoints:

* The first one is for creating and sending a video generation task to the server (returns a generation ID).
* The second one is for requesting the generated video from the server using the generation ID received from the first endpoint.

Below, you can find two corresponding API schemas and examples for both endpoint calls.

</details>

## API Schemas

### Video Generation

This endpoint creates and sends a video generation task to the server — and returns a generation ID.

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["alibaba/wan2.2-vace-fun-a14b-inpainting"]},"prompt":{"type":"string","description":"The text description of the scene, subject, or action to generate in the video."},"video_url":{"type":"string","format":"uri","description":"A HTTPS URL pointing to a video or a data URI containing a video. This video will be used as a reference during generation."},"negative_prompt":{"type":"string","default":"letterboxing, borders, black bars, bright colors, overexposed, static, blurred details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, malformed limbs, fused fingers, still picture, cluttered background, three legs, many people in the background, walking backwards","description":"The description of elements to avoid in the generated video."},"match_input_num_frames":{"type":"boolean"},"num_frames":{"type":"integer","minimum":17,"maximum":241,"default":81,"description":"Number of frames to generate."},"match_input_frames_per_second":{"type":"boolean","description":"Whether to match the input video's frames per second (FPS)."},"frames_per_second":{"type":"integer","minimum":5,"maximum":30,"default":16,"description":"Frames per second of the generated video."},"resolution":{"type":"string","enum":["480p","580p","720p"],"default":"480p","description":"The resolution of the output video, where the number refers to the short side in pixels."},"aspect_ratio":{"type":"string","enum":["auto","16:9","1:1","9:16"],"default":"auto","description":"The aspect ratio of the generated video."},"num_inference_steps":{"type":"integer","default":30,"description":"Number of inference steps for sampling. Higher values give better quality but take longer."},"guidance_scale":{"type":"number","default":5,"description":"Classifier-free guidance scale. Controls prompt adherence / creativity."},"shift":{"type":"number","default":5,"description":"Noise schedule shift parameter. Affects temporal dynamics."},"enable_safety_checker":{"type":"boolean","description":"If set to true, the safety checker will be enabled."},"enable_prompt_expansion":{"type":"boolean","description":"Whether to enable prompt expansion."},"preprocess":{"type":"boolean","description":"Whether to preprocess the input video."},"acceleration":{"type":"string","enum":["none","regular"],"default":"regular","description":"Acceleration to use for inference."},"video_quality":{"type":"string","enum":["low","medium","high","maximum"],"default":"high","description":"The quality of the generated video."},"video_write_mode":{"type":"string","enum":["fast","balanced","small"],"default":"balanced","description":"The method used to write the video."},"num_interpolated_frames":{"type":"integer","description":"Number of frames to interpolate between the original frames."},"temporal_downsample_factor":{"type":"integer","description":"Temporal downsample factor for the video."},"enable_auto_downsample":{"type":"boolean","description":"The minimum frames per second to downsample the video to."},"auto_downsample_min_fps":{"type":"number","default":15,"description":"The minimum frames per second to downsample the video to."},"interpolator_model":{"type":"string","enum":["rife","film"],"default":"film","description":"The model to use for interpolation. Rife, or film are available."},"sync_mode":{"type":"boolean","description":"The synchronization mode for audio and video. Loose or tight are available."},"image_list":{"type":"array","items":{"type":"string","format":"uri"},"description":"Array of image URLs for multi-image-to-video generation."},"mask_video_url":{"type":"string","format":"uri","description":"URL to the source mask file"}},"required":["model","prompt","video_url"],"title":"alibaba/wan2.2-vace-fun-a14b-inpainting"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
```

### Fetch the video

After sending a request for video generation, this task is added to the queue. This endpoint lets you check the status of a video generation task using its `id`, obtained from the endpoint described above.\
If the video generation task status is `complete`, the response will include the final result — with the generated video URL and additional metadata.

## GET /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"get":{"operationId":"VideoControllerV2_pollVideo_v2","parameters":[{"name":"generation_id","required":true,"in":"query","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully generated video","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Video.v2.PollVideoResponseDTO"}}}}},"tags":["Video Models"]}}},"components":{"schemas":{"Video.v2.PollVideoResponseDTO":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."},"duration":{"type":"number","nullable":true,"description":"The duration of the video."}},"required":["url"]},"duration":{"type":"number","nullable":true,"description":"The duration of the video."},"error":{"nullable":true,"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}
```

## Full Example: Generating and Retrieving the Video From the Server

The code below creates a video generation task, then automatically polls the server every **10** seconds until it finally receives the video URL.

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
    url = f"{base_url}/video/generations"
    headers = {
        "Authorization": f"Bearer {api_key}", 
    }

    data = {
        "model": "alibaba/wan2.2-vace-fun-a14b-inpainting",
        "video_url": "https://storage.googleapis.com/falserverless/example_inputs/wan_animate_input_video.mp4",
        "prompt": "A lone woman strides through the neon-drenched streets of Tokyo at night.  Her crimson dress, a vibrant splash of color against the deep blues and blacks of the cityscape, flows slightly with each step. A tailored black jacket, crisp and elegant, contrasts sharply with the dress's rich texture. Medium shot:  The city hums around her, blurred lights creating streaks of color in the background. Close-up:  The fabric of her dress catches the streetlight's glow, revealing a subtle silk sheen and the intricate stitching at the hem. Her black jacket’s subtle texture is visible – a fine wool perhaps, with a matte finish. The overall mood is one of quiet confidence and mystery, a vibrant woman navigating a bustling, nocturnal landscape. High resolution 4k.", 
        "resolution": "720p",
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

    # Trying to retrieve the video from the server every 10 sec
    if gen_id:
        start_time = time.time()

        timeout = 600
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
    model: "alibaba/wan2.2-vace-fun-a14b-inpainting",
    prompt: "A lone woman strides through the neon-drenched streets of Tokyo at night.  Her crimson dress, a vibrant splash of color against the deep blues and blacks of the cityscape, flows slightly with each step. A tailored black jacket, crisp and elegant, contrasts sharply with the dress's rich texture. Medium shot:  The city hums around her, blurred lights creating streaks of color in the background. Close-up:  The fabric of her dress catches the streetlight's glow, revealing a subtle silk sheen and the intricate stitching at the hem. Her black jacket’s subtle texture is visible – a fine wool perhaps, with a matte finish. The overall mood is one of quiet confidence and mystery, a vibrant woman navigating a bustling, nocturnal landscape. High resolution 4k.",
    image_url: "https://s2-111386.kwimgs.com/bs2/mmu-aiplatform-temp/kling/20240620/1.jpeg",
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
Generation ID:   b5592d70-dd31-4e5a-bc5c-5063660c001b:alibaba/wan2.2-vace-fun-a14b-inpainting
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
Processing complete:/n {"id":"b5592d70-dd31-4e5a-bc5c-5063660c001b:alibaba/wan2.2-vace-fun-a14b-inpainting","status":"completed","video":{"url":"https://v3b.fal.media/files/b/rabbit/L3U6CofKB0xe_fgCTKj4G.mp4"}}
```

{% endcode %}

</details>
