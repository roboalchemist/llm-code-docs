# Source: https://docs.edenai.co/v3/features/image/face-detection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Face Detection

> Face Detection is a computer technology being used in a variety of applications that identifies human faces in digital images with different attributes like landmarks, sentiments and physical attire...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `image/face_detection/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                      |
| ----- | ----------- | -------- | ------------------------------------------------ |
| file  | file\_input | Yes      | Image file ID from /v3/upload or direct file URL |

## Output

| Field                               | Type           | Required | Description |
| ----------------------------------- | -------------- | -------- | ----------- |
| **items**                           | array\[object] | No       |             |
|     confidence                      | float          | Yes      |             |
|     **landmarks**                   | object         | Yes      |             |
|         left\_eye                   | array\[float]  | No       |             |
|         left\_eye\_top              | array\[float]  | No       |             |
|         left\_eye\_right            | array\[float]  | No       |             |
|         left\_eye\_bottom           | array\[float]  | No       |             |
|         left\_eye\_left             | array\[float]  | No       |             |
|         right\_eye                  | array\[float]  | No       |             |
|         right\_eye\_top             | array\[float]  | No       |             |
|         right\_eye\_right           | array\[float]  | No       |             |
|         right\_eye\_bottom          | array\[float]  | No       |             |
|         right\_eye\_left            | array\[float]  | No       |             |
|         left\_eyebrow\_left         | array\[float]  | No       |             |
|         left\_eyebrow\_right        | array\[float]  | No       |             |
|         left\_eyebrow\_top          | array\[float]  | No       |             |
|         right\_eyebrow\_left        | array\[float]  | No       |             |
|         right\_eyebrow\_right       | array\[float]  | No       |             |
|         left\_pupil                 | array\[float]  | No       |             |
|         right\_pupil                | array\[float]  | No       |             |
|         nose\_tip                   | array\[float]  | No       |             |
|         nose\_bottom\_right         | array\[float]  | No       |             |
|         nose\_bottom\_left          | array\[float]  | No       |             |
|         mouth\_left                 | array\[float]  | No       |             |
|         mouth\_right                | array\[float]  | No       |             |
|         right\_eyebrow\_top         | array\[float]  | No       |             |
|         midpoint\_between\_eyes     | array\[float]  | No       |             |
|         nose\_bottom\_center        | array\[float]  | No       |             |
|         nose\_left\_alar\_out\_tip  | array\[float]  | No       |             |
|         nose\_left\_alar\_top       | array\[float]  | No       |             |
|         nose\_right\_alar\_out\_tip | array\[float]  | No       |             |
|         nose\_right\_alar\_top      | array\[float]  | No       |             |
|         nose\_root\_left            | array\[float]  | No       |             |
|         nose\_root\_right           | array\[float]  | No       |             |
|         upper\_lip                  | array\[float]  | No       |             |
|         under\_lip                  | array\[float]  | No       |             |
|         under\_lip\_bottom          | array\[float]  | No       |             |
|         under\_lip\_top             | array\[float]  | No       |             |
|         upper\_lip\_bottom          | array\[float]  | No       |             |
|         upper\_lip\_top             | array\[float]  | No       |             |
|         mouth\_center               | array\[float]  | No       |             |
|         mouth\_top                  | array\[float]  | No       |             |
|         mouth\_bottom               | array\[float]  | No       |             |
|         left\_ear\_tragion          | array\[float]  | No       |             |
|         right\_ear\_tragion         | array\[float]  | No       |             |
|         forehead\_glabella          | array\[float]  | No       |             |
|         chin\_gnathion              | array\[float]  | No       |             |
|         chin\_left\_gonion          | array\[float]  | No       |             |
|         chin\_right\_gonion         | array\[float]  | No       |             |
|         upper\_jawline\_left        | array\[float]  | No       |             |
|         mid\_jawline\_left          | array\[float]  | No       |             |
|         mid\_jawline\_right         | array\[float]  | No       |             |
|         upper\_jawline\_right       | array\[float]  | No       |             |
|         left\_cheek\_center         | array\[float]  | No       |             |
|         right\_cheek\_center        | array\[float]  | No       |             |
|     **emotions**                    | object         | Yes      |             |
|         joy                         | int            | Yes      |             |
|         sorrow                      | int            | Yes      |             |
|         anger                       | int            | Yes      |             |
|         surprise                    | int            | Yes      |             |
|         disgust                     | int            | Yes      |             |
|         fear                        | int            | Yes      |             |
|         confusion                   | int            | Yes      |             |
|         calm                        | int            | Yes      |             |
|         unknown                     | int            | Yes      |             |
|         neutral                     | int            | Yes      |             |
|         contempt                    | int            | Yes      |             |
|     **poses**                       | object         | Yes      |             |
|         pitch                       | float          | Yes      |             |
|         roll                        | float          | Yes      |             |
|         yaw                         | float          | Yes      |             |
|     age                             | float          | Yes      |             |
|     gender                          | string         | Yes      |             |
|     **bounding\_box**               | object         | Yes      |             |
|         x\_min                      | float          | Yes      |             |
|         x\_max                      | float          | Yes      |             |
|         y\_min                      | float          | Yes      |             |
|         y\_max                      | float          | Yes      |             |
|     **hair**                        | object         | Yes      |             |
|         **hair\_color**             | array\[object] | No       |             |
|             color                   | string         | Yes      |             |
|             confidence              | float          | Yes      |             |
|         bald                        | float          | Yes      |             |
|         invisible                   | bool           | Yes      |             |
|     **facial\_hair**                | object         | Yes      |             |
|         moustache                   | float          | Yes      |             |
|         beard                       | float          | Yes      |             |
|         sideburns                   | float          | Yes      |             |
|     **quality**                     | object         | Yes      |             |
|         noise                       | float          | Yes      |             |
|         exposure                    | float          | Yes      |             |
|         blur                        | float          | Yes      |             |
|         brightness                  | float          | Yes      |             |
|         sharpness                   | float          | Yes      |             |
|     **makeup**                      | object         | Yes      |             |
|         eye\_make                   | bool           | Yes      |             |
|         lip\_make                   | bool           | Yes      |             |
|     **accessories**                 | object         | Yes      |             |
|         sunglasses                  | float          | Yes      |             |
|         reading\_glasses            | float          | Yes      |             |
|         swimming\_goggles           | float          | Yes      |             |
|         face\_mask                  | float          | Yes      |             |
|         eyeglasses                  | float          | Yes      |             |
|         headwear                    | float          | Yes      |             |
|     **occlusions**                  | object         | Yes      |             |
|         eye\_occluded               | bool           | Yes      |             |
|         forehead\_occluded          | bool           | Yes      |             |
|         mouth\_occluded             | bool           | Yes      |             |
|     **features**                    | object         | Yes      |             |
|         eyes\_open                  | float          | Yes      |             |
|         smile                       | float          | Yes      |             |
|         mouth\_open                 | float          | Yes      |             |

## Available Providers

| Provider | Model String                    | Price                  |
| -------- | ------------------------------- | ---------------------- |
| amazon   | `image/face_detection/amazon`   | \$1 per 1,000 files    |
| api4ai   | `image/face_detection/api4ai`   | \$0.75 per 1,000 files |
| clarifai | `image/face_detection/clarifai` | \$2 per 1,000 files    |
| google   | `image/face_detection/google`   | \$1.5 per 1,000 files  |

## Quick Start

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "image/face_detection/amazon",
      "input": {
          "file": "YOUR_FILE_UUID_OR_URL"
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  print(response.json())
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/universal-ai \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "image/face_detection/amazon",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).