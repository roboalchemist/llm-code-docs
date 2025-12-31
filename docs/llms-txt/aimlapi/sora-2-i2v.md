# Source: https://docs.aimlapi.com/api-references/video-models/openai/sora-2-i2v.md

# sora-2-i2v

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `openai/sora-2-i2v`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/openai/sora-2-i2v" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

Sora 2 is new powerful media generation model, generating videos with synced audio.

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

You can generate a video using this API. In the basic setup, you only need a reference image and a prompt.\
This endpoint creates and sends a video generation task to the server — and returns a generation ID.

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["openai/sora-2-i2v"]},"prompt":{"type":"string","description":"The text description of the scene, subject, or action to generate in the video."},"image_url":{"type":"string","format":"uri","description":"A URL or a Base64-encoded image file used as the initial frame for video generation.\nThe image dimensions must match the selected video resolution and aspect ratio.\nSupported configurations include:\n720p with aspect ratios:\n- 16:9 — 1280x720\n- 9:16 — 720x1280\n\n1080p with aspect ratios:\n- 16:9 — 1792x1024\n- 9:16 — 1024x1792"},"resolution":{"type":"string","enum":["720p"],"default":"720p","description":"The resolution of the output video, where the number refers to the short side in pixels."},"aspect_ratio":{"type":"string","enum":["16:9","9:16"],"default":"16:9","description":"The aspect ratio of the generated video."},"duration":{"type":"integer","description":"The length of the output video in seconds.","enum":[4,8,12],"default":"4"}},"required":["model","prompt","image_url"],"title":"openai/sora-2-i2v"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
```

### Retrieve the generated video from the server

After sending a request for video generation, this task is added to the queue. This endpoint lets you check the status of a video generation task using its `id`, obtained from the endpoint described above.\
If the video generation task status is `completed`, the response will include the final result — with the generated video URL and additional metadata.

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

# Insert your AI/ML API key instead of <YOUR_AIMLAPI_KEY>:
api_key = "<YOUR_AIMLAPI_KEY>"

# Creating and sending a video generation task to the server
def generate_video():
    url = "https://api.aimlapi.com/v2/video/generations"
    headers = {
        "Authorization": f"Bearer {api_key}", 
    }

    data = {
        "model": "openai/sora-2-i2v",
        "prompt": "She turns around and smiles, then slowly walks out of the frame.",
        "image_url": "https://cdn.openai.com/API/docs/images/sora/woman_skyline_original_720p.jpeg",
        "resolution": "720p",
        "duration": 4
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

    # Try to retrieve the video from the server every 10 sec
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
// Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>
const apiKey = '<YOUR_AIMLAPI_KEY>';

// Creating and sending a video generation task to the server
async function generateVideo() {
  const url = 'https://api.aimlapi.com/v2/video/generations';

  const data = {
    model: 'openai/sora-2-i2v',
    prompt: 'She turns around and smiles, then slowly walks out of the frame.',
    image_url:
      'https://cdn.openai.com/API/docs/images/sora/woman_skyline_original_720p.jpeg',
    resolution: '720p',
    aspect_ratio: '16:9',
    duration: 4,
  };

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error(`Error: ${response.status} - ${errorText}`);
      return null;
    }

    const responseData = await response.json();
    console.log(responseData);
    return responseData;
  } catch (error) {
    console.error('Request failed:', error);
    return null;
  }
}

// Requesting the result of the task from the server using the generation_id
async function getVideo(genId) {
  const url = new URL('https://api.aimlapi.com/v2/video/generations');
  url.searchParams.append('generation_id', genId);

  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
    });

    return await response.json();
  } catch (error) {
    console.error('Error fetching video:', error);
    return null;
  }
}

// Initiates video generation and checks the status every 10 seconds until completion or timeout
async function main() {
  const genResponse = await generateVideo();
  if (!genResponse) return;

  const genId = genResponse.id;
  console.log('Generation ID:', genId);

  if (genId) {
    const timeout = 600 * 1000; // 10 minutes
    const startTime = Date.now();

    while (Date.now() - startTime < timeout) {
      const responseData = await getVideo(genId);

      if (!responseData) {
        console.error('Error: No response from API');
        break;
      }

      const status = responseData.status;
      console.log('Status:', status);

      if (['waiting', 'active', 'queued', 'generating'].includes(status)) {
        console.log('Still waiting... Checking again in 10 seconds.');
        await new Promise((resolve) => setTimeout(resolve, 10000));
      } else {
        console.log('Processing complete:\n', responseData);
        return responseData;
      }
    }

    console.log('Timeout reached. Stopping.');
  }
}

main();

```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Statuses</summary>

<table><thead><tr><th width="169.99993896484375">Status</th><th>Description</th></tr></thead><tbody><tr><td><code>queued</code></td><td>Job is waiting in queue</td></tr><tr><td><code>generating</code></td><td>Video is being generated</td></tr><tr><td><code>completed</code></td><td>Generation successful, video available</td></tr><tr><td><code>error</code></td><td>Generation failed, check <code>error</code> field</td></tr></tbody></table>

</details>

<details>

<summary>Response</summary>

{% code overflow="wrap" %}

```json5
Generation ID: video_68e572c03d08819188f79439891f6f280590a37b858cba30:openai/sora-2-i2v
Status: generating
Still waiting... Checking again in 10 seconds.
Status: queued
Still waiting... Checking again in 10 seconds.
Status: queued
Still waiting... Checking again in 10 seconds.
...
Processing complete:
 {
  id: 'video_68e572c03d08819188f79439891f6f280590a37b858cba30:openai/sora-2-i2v',
  status: 'completed',
  video: {
    url: 'https://cdn.aimlapi.com/generations/hedgehog/1759867684272-d7a19473-8f19-421e-9bde-cf1d206c68e5.mp4'
  }
}
```

{% endcode %}

</details>

**Processing time**: \~1.5 min.

**Low-res GIF preview**:

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-95dc53a51cc0d731d47039a84ab8ce9768028ba0%2Fezgif-1f9deb6add98fd.gif?alt=media" alt=""><figcaption><p><code>"She turns around and smiles, then slowly walks out of the frame."</code></p></figcaption></figure></div>
