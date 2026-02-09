# Source: https://docs.aimlapi.com/api-references/video-models/kling-ai/video-v2.6-pro-motion-control.md

# v2.6-pro/motion-control

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `klingai/video-v2-6-pro-motion-control`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/?model=klingai/video-v2-6-pro-motion-control" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

A next-generation cinematic video generation model developed by KlingAI. It focuses on transferring motion from reference videos to arbitrary target characters, producing smooth, realistic movement, detailed visuals, and native audio when enabled.

## How to Make a Call

<details>

<summary>Step-by-Step Instructions</summary>

:digit\_one: **Setup You Can’t Skip**

:black\_small\_square: [**Create an Account**](https://aimlapi.com/app/sign-up): Visit the AI/ML API website and create an account (if you don’t have one yet).\
:black\_small\_square: [**Generate an API Key**](https://aimlapi.com/app/keys): After logging in, navigate to your account dashboard and generate your API key. Ensure the key is enabled on the UI.

:digit\_two: **Copy the code example**

At the bottom of this page, you'll find a code example that shows how to structure the request. Choose the code snippet in your preferred programming language and copy it into your development environment.

:digit\_three: **Modify the code example**

:black\_small\_square: Replace `<YOUR_AIMLAPI_KEY>` with your actual AI/ML API key.\
:black\_small\_square: Adjust the input field used by this model (for example, prompt, input text, instructions, media source, or other model-specific input) to match your request.

:digit\_four: <sup><sub><mark style="background-color:yellow;">**(Optional)**<mark style="background-color:yellow;"><sub></sup> **Adjust other optional parameters if needed**

Only the required parameters shown in the example are needed to run the request, but you can include optional parameters to fine-tune behavior. Below, you can find the corresponding **API schema**, which lists all available parameters and usage notes.

:digit\_five: **Run your modified code**

Run your modified code inside your development environment. Response time depends on many factors, but for simple requests it rarely exceeds a few seconds.

{% hint style="success" %}
If you need a more detailed walkthrough for setting up your development environment and making a request step-by-step, feel free to use our [**Quickstart guide.**](https://docs.aimlapi.com/quickstart/setting-up)
{% endhint %}

</details>

## API Schemas

### Create a video generation task and send it to the server

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["klingai/video-v2-6-pro-motion-control"]},"prompt":{"type":"string","description":"Optional instructions that define the background elements, including their appearance, timing in the frame, and behavior, and can also subtly adjust the character’s animation."},"image_url":{"type":"string","format":"uri","description":"A direct link to an online image or a Base64-encoded local image that serves as the character reference for animation. The image must contain exactly one clearly visible character, who will be animated using the motion from the reference video provided in the video_url parameter. For optimal results, be sure the character’s proportions in the image match those in the video."},"video_url":{"type":"string","format":"uri","description":"A HTTPS URL pointing to a video or a data URI containing a video. The character’s movements from this video will be applied to the character from the image provided in the image_url parameter. For best results, use a video with a single clearly visible character. If the video contains two or more characters, the motion of the character occupying the largest portion of the frame will be used for generation."},"character_orientation":{"type":"string","enum":["image","video"],"default":"image","description":"Generate the orientation of the character in the video, which can be selected to match the image or the video:\n- image: has the same orientation as the person in the picture; At this time, the reference video duration should not exceed 10 seconds;\n- video: consistent with the orientation of the characters in the video; At this time, the reference video duration should not exceed 30 seconds;"},"keep_audio":{"type":"boolean","default":true,"description":"Whether to keep the original audio from the video."}},"required":["model","image_url","video_url"],"title":"klingai/video-v2-6-pro-motion-control"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
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

1. Provide the URL of the image containing the character you want to animate.
2. Provide the URL of the video where another character performs the movements you want to transfer to the animated character.
3. If needed, describe minor background details or additional objects in the frame using the `prompt` parameter. Example: `"A brightly colored parrot flies in from the left, briefly circles above the character once, and then hurries off to the right."`
4. Set the `character_orientation` parameter to `image` or `video`, depending on whether you want to use the character’s orientation from the image reference or from the video reference.
5. By default, the model uses the audio track from the reference video. You can disable this behavior by setting the `keep_audio` parameter to `false`.

<details>

<summary> Input Reference Guidelines</summary>

* Ensure the character’s entire body and head are clearly visible and not obstructed in both the image and the motion reference.
* Keep the character’s proportions consistent between the image and the reference video. Avoid pairing a full-body motion reference with a half-body or cropped image.
* Upload a motion reference featuring a single character whenever possible.\
  If the motion reference contains two or more characters, the motion of the character occupying the largest portion of the frame will be used for generation.
* Real human actions are recommended. Certain stylised characters, humanoid animals, and characters with partial humanoid body proportions are supported and can be recognised.
* Avoid cuts, camera movements, and rapid scene changes in the motion reference video.
* Avoid overly fast or complex motions. Steady, moderate movements generally produce better results.
* The short edge of the input media must be at least 300–340 px (depending on the input type), and the long edge must not exceed 3850–65536 px.
* The supported duration of the motion reference video ranges from 3 to 30 seconds.\
  The generated video length will generally match the duration of the uploaded reference video.
* If the motion is too complex or fast-paced, the generated output may be shorter than the original video, as the model can only extract valid continuous action segments.

</details>

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
      "model": "klingai/video-v2-6-pro-motion-control",
      "image_url": "https://cdn.aimlapi.com/flamingo/files/b/0a875302/8NaxQrQxDNHppHtqcchMm.png",
      "video_url": "https://cdn.aimlapi.com/flamingo/files/b/0a8752bc/2xrNS217ngQ3wzXqA7LXr_output.mp4"       
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

        timeout = 1000
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
    model: "klingai/video-v2-6-pro-motion-control",
    image_url: "https://cdn.aimlapi.com/flamingo/files/b/0a875302/8NaxQrQxDNHppHtqcchMm.png",
    video_url: "https://cdn.aimlapi.com/flamingo/files/b/0a8752bc/2xrNS217ngQ3wzXqA7LXr_output.mp4"      
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
        
                if (["waiting", "queued", "generating"].includes(status)) {
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
{'id': 'NVOeetazzu2Xlca6ghTMx', 'status': 'queued'}
Generation ID:   NVOeetazzu2Xlca6ghTMx
Status: queued. Checking again in 15 seconds.
Status: queued. Checking again in 15 seconds.
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
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Status: generating. Checking again in 15 seconds.
Processing complete:
 {'id': 'NVOeetazzu2Xlca6ghTMx', 'status': 'completed', 'video': {'url': 'https://cdn.aimlapi.com/kangaroo/bs2/upload-ylab-stunt-sgp/muse/784256485483880450/VIDEO/20260109/fcf822536e099526fc3cb8e0c72b6d56-34f8180e-d688-4660-85e9-bac5a1bacae2.mp4?cacheKey=ChtzZWN1cml0eS5rbGluZy5tZXRhX2VuY3J5cHQSsAHC22ZHtdl8eKw97-KZAzBvy2RP67q-Vk1qJ97HX6jnXG4aaDLv9nXnEJTxrTer-3ItWMsuf1gHAmAp5-IgNiZH-4Gbzz4Nr6kVKj_lDlZ8iO5qFZc1B-ANepHaG4gMRUmNtr0juZVHxV_1BMzn7wh81dK_TZg7I-UtGfATmByvx2ttbyHG8zBEggZMVqeXVqwO-_Doy2htfyzZFn304rHeGHC4L8DmVoRgJm-5h_LINBoSK9DDR3Zts0AO39BBzVqoebvyIiDSG0tFxUnEmcpQh23QNXer3hT6YcDJEoZRcn8_q3CCPigFMAE&x-kcdn-pid=112781&ksSecret=1ef8bfd0ebad4b4810a97cd91fa51924&ksTime=69884f0c'}}
```

{% endcode %}

</details>

**Processing time**: \~ 5 min 56 sec.

<details>

<summary>Image and Video References</summary>

<table data-header-hidden data-full-width="true"><thead><tr><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top"><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FesPae6lBwTPY4goPJbQy%2Fwoman-in-yellow-dancing.png?alt=media&#x26;token=be46d5ca-1368-431e-8565-5fb778c50f0c" alt=""></td><td valign="top"><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FlaTQUQI1xluVaPfJ5NEi%2Fvideo-reference-motion.gif?alt=media&#x26;token=5e2783e0-0588-4fbf-9e18-c2f668609b5d" alt=""></td></tr></tbody></table>

</details>

**Generated video** (1936x1072, without sound, the character’s orientation matches the orientation from the image reference):

{% embed url="<https://drive.google.com/file/d/1vlalNtBr0tJnEvsS0uQQW1NmyzFH8_0T/view>" %}
`"character_orientation":"image"`
{% endembed %}

**Generated video** (1936x1072, without sound, the character’s orientation matches the orientation from the video reference):

{% embed url="<https://drive.google.com/file/d/1JDUKKGr3Jdm04J9-BOXtsMGo59znot6_/view>" %}
`"character_orientation":"video"`
{% endembed %}
