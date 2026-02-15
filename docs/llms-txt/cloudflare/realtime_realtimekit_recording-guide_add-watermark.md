# Source: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/index.md

---

title: Add Watermark · Cloudflare Realtime docs
description: RealtimeKit's watermark feature enables you to include an image as
  a watermark in your recording. To add watermark, configure the following
  parameters to video_config in the Start Recording API.
lastUpdated: 2025-12-01T15:18:21.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/
  md: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/index.md
---

RealtimeKit's watermark feature enables you to include an image as a watermark in your recording. To add watermark, configure the following parameters to video\_config in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/).

| **Parameter** | **Description** |
| - | - |
| URL | Specify the URL of the watermark image |
| Position | Specify the placement of the watermark, you have the flexibility to choose between left top, right top, left bottom, or right bottom. The default position is set to left top. |
| Size | Specify the height and width of the watermark in pixels. |

```json
{
  "video_config": {
    "watermark": {
      "url": "https://test.io/images/client-logos-6.webp",
      "position": "left top",
      "size": {
        "height": 20,
        "width": 100
      }
    }
  }
}
```
