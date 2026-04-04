# Source: https://docs.aimlapi.com/api-references/video-models/alibaba-cloud/wan-2.6-reference-to-video.md

# Wan 2.6 (Reference-to-Video)

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `alibaba/wan-2-6-r2v`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/alibaba/wan-2-6-r2v" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

This model builds videos from reference video material with reliable character consistency, synchronized audio, and cinematic multi-shot storytelling. Compared to earlier versions, Wan 2.6 provides stronger instruction following, higher visual fidelity, and improved sound generation.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## How to Make a Call

<details>

<summary>Step-by-Step Instructions</summary>

Generating a video using this model involves sequentially calling two endpoints:

* The first one is for creating and sending a video generation task to the server (returns a generation ID).
* The second one is for requesting the generated video from the server using the generation ID received from the first endpoint. Below, you can find both corresponding API schemas.

</details>

## API Schemas

### Create a video generation task and send it to the server

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["alibaba/wan-2-6-r2v"]},"prompt":{"type":"string","description":"The text description of the scene, subject, or action to generate in the video."},"video_urls":{"type":"array","items":{"type":"string","format":"uri"},"minItems":1,"maxItems":3,"description":"An array of URLs for the uploaded reference video files. This parameter is used to extract the character's appearance and voice (if any) to generate a video that matches the reference features.\nEach reference video must contain only one character. For example, character1 is a little girl and character2 is an alarm clock."},"aspect_ratio":{"type":"string","enum":["16:9","9:16","1:1","4:3","3:4"],"default":"16:9","description":"The aspect ratio of the generated video."},"resolution":{"type":"string","enum":["720p","1080p"],"default":"1080p","description":"An enumeration where the short side of the video frame determines the resolution."},"duration":{"type":"integer","description":"The length of the output video in seconds.","enum":[5,10,15],"default":"10"},"negative_prompt":{"type":"string","description":"The description of elements to avoid in the generated video."},"shot_type":{"type":"string","enum":["single","multi"],"default":"single","description":"Specifies the shot type of the generated video, that is, whether the video consists of a single continuous shot or multiple switched shots.\nThis parameter takes effect only when \"prompt_extend\" is set to 'true':\n- single: (default) Outputs a single-shot video.\n- multi: Outputs a multi-shot video."},"seed":{"type":"integer","description":"Varying the seed integer is a way to get different results for the same other request parameters. Using the same value for an identical request will produce similar results. If unspecified, a random number is chosen."},"enhance_prompt":{"type":"boolean","default":true,"description":"Whether to enable prompt expansion."}},"required":["model","prompt","video_urls"],"title":"alibaba/wan-2-6-r2v"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
```

### Retrieve the generated video from the server

After sending a request for video generation, this task is added to the queue. This endpoint lets you check the status of a video generation task using its `generation_id`, obtained from the endpoint described above.\
If the video generation task status is `completed`, the response will include the final result — with the generated video URL and additional metadata.

## GET /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key","in":"header"}}},"paths":{"/v2/video/generations":{"get":{"operationId":"_v2_video_generations","parameters":[{"name":"generation_id","required":true,"in":"query","schema":{"type":"string"}}],"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
```

## Code Example

The code below creates a video generation task, then automatically polls the server every **15** seconds until it finally receives the video URL.

Two reference videos are supplied via URLs, and the prompt defines how the model should use them.

{% tabs %}
{% tab title="Python" %}

<pre class="language-python" data-overflow="wrap"><code class="lang-python">import requests
import time

# Insert your AIML API Key instead of &#x3C;YOUR_AIMLAPI_KEY>:
api_key = "&#x3C;YOUR_AIMLAPI_KEY>"
base_url = "https://api.aimlapi.com/v2"

# Creating and sending a video generation task to the server
def generate_video():
    url = f"{base_url}/video/generations"
    headers = {
        "Authorization": f"Bearer {api_key}", 
        "Content-Type": "application/json"
    }

    payload = {
        "model": "alibaba/wan-2-6-r2v",
        "prompt": '''
<strong>Use the woman from the second reference video as Mona Lisa — keep her face, clothing, colors, lighting, camera angle, and background exactly as in the second reference video.
</strong>Do not replace her with a different person and do not change the environment.

Take the raccoon only from the first reference video — keep the same fur pattern, colors, proportions, and appearance.
Do not generate a different raccoon.

Place the raccoon gently in Mona Lisa’s arms, as if he is her pet. She softly pets the raccoon. The raccoon affectionately licks her face, and Mona Lisa reacts with a warm, joyful laugh.

The audio must be in English. Mona Lisa says the short line:
"Oh, you sweet little one!"
Synchronize her lip movement to this line only. Do not generate Chinese speech.

Keep the visual style, motion, framing, and atmosphere realistic and consistent with the second reference video.
''',
        "video_urls":[
            "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/racoon-in-the-forest.mp4",
            "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/monalisa.mp4"
            ],
        # "duration": "5",
    }
 
    response = requests.post(url, json=payload, headers=headers)
    
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
    print(gen_response)
    gen_id = gen_response.get("id")
    print("Generation ID:  ", gen_id)

    # Try to retrieve the video from the server every 15 sec
    if gen_id:
        start_time = time.time()

        timeout = 1000
        while time.time() - start_time &#x3C; timeout:
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
</code></pre>

{% endtab %}

{% tab title="JS" %}
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
    model: "alibaba/wan-2-6-r2v",
    prompt: `Use the woman from the second reference video as Mona Lisa — keep her face, clothing, colors, lighting, camera angle, and background exactly as in the second reference video.
Do not replace her with a different person and do not change the environment.

Take the raccoon only from the first reference video — keep the same fur pattern, colors, proportions, and appearance.
Do not generate a different raccoon.

Place the raccoon gently in Mona Lisa’s arms, as if he is her pet. She softly pets the raccoon. The raccoon affectionately licks her face, and Mona Lisa reacts with a warm, joyful laugh.

The audio must be in English. Mona Lisa says the short line:
"Oh, you sweet little one!"
Synchronize her lip movement to this line only. Do not generate Chinese speech.

Keep the visual style, motion, framing, and atmosphere realistic and consistent with the second reference video.`,
    video_urls: [
      "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/racoon-in-the-forest.mp4",
      "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/monalisa.mp4"
    ]
};

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

        const timeout = 1000 * 1000; // 1000 sec
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
{'id': 'F4ydZjZhuZFinNQMnQleh', 'status': 'queued', 'meta': {'usage': {'credits_used': 3150000}}}
Generation ID:   F4ydZjZhuZFinNQMnQleh
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
 {'id': 'F4ydZjZhuZFinNQMnQleh', 'status': 'completed', 'video': {'url': 'https://cdn.aimlapi.com/alpaca/1d/ef/20260107/69015395/89757270-8987f96a-bdd1-439f-92f6-4ebc4e8a7a4d.mp4?Expires=1767873802&OSSAccessKeyId=LTAI5tRcsWJEymQaTsKbKqGf&Signature=kBywVpc6QoOT0%2BqFhUSAmsw3fqo%3D'}}
```

{% endcode %}

</details>

**Processing time**: \~ 4 min 20 sec.

**Generated video** (1920x1080, with sound):

{% embed url="<https://drive.google.com/file/d/1uqKLmzOZ_MYUTZ1f_DnQ_PoVXhl-DLD0/view>" %}
