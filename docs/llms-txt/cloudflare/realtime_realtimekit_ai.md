# Source: https://developers.cloudflare.com/realtime/realtimekit/ai/index.md

---

title: AI · Cloudflare Realtime docs
description: RealtimeKit provides AI-powered features using Cloudflare's AI
  infrastructure to enhance your meetings with transcription and summarization
  capabilities.
lastUpdated: 2026-01-20T15:20:36.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ai/
  md: https://developers.cloudflare.com/realtime/realtimekit/ai/index.md
---

RealtimeKit provides AI-powered features using Cloudflare's AI infrastructure to enhance your meetings with transcription and summarization capabilities.

* [Transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/)
* [Summary](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/)

## Available features

| Feature | Description |
| - | - |
| [Transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/) | Real-time and post-meeting speech-to-text |
| [Summary](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/) | AI-generated meeting summaries |

## Quick start

Enable AI features when creating a meeting:

```json
{
  "title": "Team Standup",
  "ai_config": {
    "transcription": {
      "language": "en-US"
    },
    "summarization": {
      "summary_type": "team_meeting"
    }
  },
  "summarize_on_end": true
}
```

Ensure participants have `transcription_enabled: true` in their [preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/).

## Storage and retention

* Transcripts and summaries are stored for **7 days** from meeting start
* Files are stored in R2 with presigned URLs for secure access
* Delivered via [webhooks](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/) or REST API
