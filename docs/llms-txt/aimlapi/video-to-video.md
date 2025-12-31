# Source: https://docs.aimlapi.com/api-references/video-models/magic/video-to-video.md

# magic/video-to-video

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `magic/video-to-video`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/magic/video-to-video" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

The model allows you to embed your custom video into the selected video template — sound included.

<details>

<summary>Supported Templates</summary>

<div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FXHUdl5H23M3DqGEFdjNY%2FArt%20Gallery.gif?alt=media&#x26;token=4a51f5b3-53ad-470f-a6d0-fbe87b2ecfa1" alt=""><figcaption><p><code>Art Gallery</code></p></figcaption></figure> <figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FKW5Lbcw5VDbaOjfLZB7l%2FCappadocia%20Balloons.gif?alt=media&#x26;token=df62d421-a773-46f5-9a6b-c34d4321e95e" alt=""><figcaption><p><code>Cappadocia Balloons</code></p></figcaption></figure> <figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Foz8JgHkqkGUFGD7NtHKt%2FDesktop%20Reveal.gif?alt=media&#x26;token=70ab5cc9-236e-4094-8b14-435ab0b8f2ef" alt=""><figcaption><p><code>Desktop Reveal</code></p></figcaption></figure> <figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2F6X78bsIvjs1rXBsyr1ds%2FDubai%20Museum.gif?alt=media&#x26;token=8ad60334-c21b-4447-9bbd-531a101b2849" alt=""><figcaption><p><code>Dubai Museum</code></p></figcaption></figure></div>

<div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FZexbNVdCSjU81mfkAS4b%2FEgypt%20Pyramid.gif?alt=media&#x26;token=1024b517-7050-400b-a35b-3203d15f1f6c" alt=""><figcaption><p><code>Egypt Pyramid</code></p></figcaption></figure> <figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FMN5yGwEkuqz0oBImipDR%2FLas%20Vegas%20LED.gif?alt=media&#x26;token=10480544-fdef-482b-bd51-d1946b6024b8" alt=""><figcaption><p><code>Las Vegas LED</code></p></figcaption></figure> <figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fz2u5a6juM8EXcg9sAzkz%2FNew%20York%20Times%20Square%20().gif?alt=media&#x26;token=1d1e52b0-74d8-48c0-b660-feb3d94d5cc2" alt=""><figcaption><p><code>New York Times Square(66)</code> </p></figcaption></figure> <figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FjyMTiwERbE9hFFOM5niy%2FNew%20York%20Times%20Square.gif?alt=media&#x26;token=d854e186-ee2e-4041-b33f-33ed4dca98d1" alt=""><figcaption><p><code>New York Times Square(77)</code> </p></figcaption></figure></div>

<div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2F3vy7cU9jEYtd82MsrPHB%2FParis%20Eiffel%20Tower.gif?alt=media&#x26;token=8b133e33-674f-44d4-94db-a47e0db5e07c" alt=""><figcaption><p><code>Paris Eiffel Tower</code></p></figcaption></figure> <figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FYXwoudkhLy1n6yAkDCuo%2FPhone%20App.gif?alt=media&#x26;token=4fab10be-7500-46f1-8afd-78b67f06a4f6" alt=""><figcaption><p><code>Phone App</code></p></figcaption></figure> <figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FOoOxDtw8irhmkVUeMoSE%2FPhone%20Social.gif?alt=media&#x26;token=d601954a-056b-4fb8-a647-031c6e191a8c" alt=""><figcaption><p><code>Phone Social</code></p></figcaption></figure> <figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FHbGKrAmitIVkC7NzlljD%2FRotating%20%D0%A1ards.gif?alt=media&#x26;token=71db96c1-90c2-4a2c-ad1d-b6db0e443773" alt=""><figcaption><p><code>Rotating Сards</code></p></figcaption></figure></div>

<div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FSHcQNvgbWUBvOAVZTDVH%2FSan%20Francisco%20Skyscrapers.gif?alt=media&#x26;token=1b6a931e-5ca9-42b1-8abc-90f153b458a7" alt=""><figcaption><p><code>San Francisco Skyscrapers</code></p></figcaption></figure> <figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FzVWKC5MEj5mlwALQfP08%2FStockholm%20Metro.gif?alt=media&#x26;token=501a6a9f-8391-4501-89dd-5802a9502fba" alt=""><figcaption><p><code>Stockholm Metro</code></p></figcaption></figure> <figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2F50kee9hhrD74BuRqldcY%2FThailand%20Street.gif?alt=media&#x26;token=cacad0ed-77ce-4b5c-a564-7089b9ecc4db" alt=""><figcaption><p><code>Thailand Street</code></p></figcaption></figure></div>

<div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FumQ6LZ2B3bHGRUU1gKsT%2FTimes%20Square%20Billboard.gif?alt=media&#x26;token=7d3c2fb0-0bd1-46c1-9a96-71b816dccb5e" alt=""><figcaption><p><code>Times Square Billboard</code></p></figcaption></figure> <figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FQNkZqdYkZL0MFi4wYllB%2FTimes%20Square%20Round%20Screen.gif?alt=media&#x26;token=c7345cd5-bcff-42dd-afa5-c70549636f79" alt=""><figcaption><p><code>Times Square Round Screen</code></p></figcaption></figure> <figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FY9LNIU3q4ZHT8c6NmDy4%2FTokyo%20Billboard.gif?alt=media&#x26;token=d215a63d-3fbf-4e67-88e9-04e7e14d98db" alt=""><figcaption><p><code>Tokyo Billboard</code></p></figcaption></figure></div>

</details>

## API Schemas

Generating a video using this model involves sequentially calling two endpoints:

* The first one is for creating and sending a video generation task to the server (returns a generation ID).
* The second one is for requesting the generated video from the server using the generation ID received from the first endpoint.

Below, you can find two corresponding API schemas and an example with both endpoint calls.

### Create a video generation task and send it to the server

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["magic/video-to-video"]},"video_url":{"type":"string","format":"uri","description":"A video (supplied via URL or Base64) that will be inserted into the selected video template as the embedded ad content."},"template":{"type":"string","enum":["Thailand Street","Times Square Billboard","New York Times Square (78)","Phone Social","Art Gallery","New York Times Square (67)","Dubai Museum","Rotating Cards","Desktop Reveal","Egypt Pyramid","Cappadocia Balloons","Times Square Round Screen","Stockholm Metro","Tokyo Billboard","San Francisco Skyscrapers","Malaysia Shop","Las Vegas LED","Phone App","Paris Eiffel Tower"],"default":"Thailand Street","description":"Video design template."}},"required":["model","video_url"],"title":"magic/video-to-video"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
```

### Retrieve the generated video from the server

After sending a request for video generation, this task is added to the queue. This endpoint lets you check the status of a video generation task using its `generation_id`, obtained from the endpoint described above.\
If the video generation task status is `complete`, the response will include the final result — with the generated video URL and additional metadata.

## GET /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"get":{"operationId":"VideoControllerV2_pollVideo_v2","parameters":[{"name":"generation_id","required":true,"in":"query","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully generated video","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Video.v2.PollVideoResponseDTO"}}}}},"tags":["Video Models"]}}},"components":{"schemas":{"Video.v2.PollVideoResponseDTO":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."},"duration":{"type":"number","nullable":true,"description":"The duration of the video."}},"required":["url"]},"duration":{"type":"number","nullable":true,"description":"The duration of the video."},"error":{"nullable":true,"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}
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
        "model": "magic/video-to-video",
        "video_url": "https://cdn.aimlapi.com/panda/pixverse%2Fmp4%2Fmedia%2Fweb%2Fori%2FSPATnCC6Dp3nA9Sie3fsU_seed186094117.mp4",
        "template": "Thailand Street" 
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
            
            if status in ["waiting", "queued", "generating"]:
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
    model: "magic/video-to-video",
    video_url: "https://cdn.aimlapi.com/panda/pixverse%2Fmp4%2Fmedia%2Fweb%2Fori%2FSPATnCC6Dp3nA9Sie3fsU_seed186094117.mp4",
    template: "Thailand Street" 
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
Generation ID:   expUFhMahEWMCh8vWd-4p
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
Processing complete:
 {'id': 'expUFhMahEWMCh8vWd-4p', 'status': 'completed', 'video': {'url': 'https://cdn.aimlapi.com/mule/ompr/openmagic/render_tasks/255044/e59d3497d6514bb8aaca78f8ac0870a6.mp4?response-content-disposition=attachment%3B%20filename%3De59d3497d6514bb8aaca78f8ac0870a6.mp4&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=FUQDW4Z92RG9JPURIVP1%2F20251231%2Ffsn1%2Fs3%2Faws4_request&X-Amz-Date=20251231T172055Z&X-Amz-Expires=600&X-Amz-SignedHeaders=host&X-Amz-Signature=f9c2d781a10d3e5b23e32eb32476f4c7834862fef6275b6c9d2bcb0ce32111a0'}}
```

{% endcode %}

</details>

**Processing time**: \~ 2 min 37 sec.

**Generated video** (608x1080, with sound):

{% embed url="<https://drive.google.com/file/d/1MY3EWlIT-aR0HNIXqWIP77ueHH_G5KEB/view>" %}
