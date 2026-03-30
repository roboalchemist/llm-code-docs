# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkai/index.md

---

title: RTKAi · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkai/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkai/index.md
---

[]()

This module consists of the `ai` object which is used to interface with product's AI features. You can obtain the live meeting transcript and use other meeting AI features such as summary, and agenda using this object.

* [RTKAi](#module_RTKAi)

  * *instance*

    * [.telemetry](#module_RTKAi+telemetry)
    * [.onTranscript(transcript)](#module_RTKAi+onTranscript)

  * *static*

    * [.parseTranscript(transcriptData, \[isPartialTranscript\])](#module_RTKAi.parseTranscript)
    * [.parseTranscripts(transcriptData)](#module_RTKAi.parseTranscripts)

[]()

### meeting.ai.telemetry

**Kind**: instance property of [`RTKAi`](#module_RTKAi)\
[]()

### meeting.ai.onTranscript(transcript)

**Kind**: instance method of [`RTKAi`](#module_RTKAi)

| Param | Type | Description |
| - | - | - |
| transcript | `TranscriptionData` | Transcript data received for a participant. |

[]()

### meeting.ai.parseTranscript(transcriptData, \[isPartialTranscript])

Parse a single line transcript

**Kind**: static method of [`RTKAi`](#module_RTKAi)

| Param | Type | Default | Description |
| - | - | - | - |
| transcriptData | `string` | | The transcript data to parse |
| \[isPartialTranscript] | `boolean` | `false` | Whether the transcript is partial |

[]()

### meeting.ai.parseTranscripts(transcriptData)

Parse a multi-line transcript

**Kind**: static method of [`RTKAi`](#module_RTKAi)

| Param | Type | Description |
| - | - | - |
| transcriptData | `string` | The transcript data to parse |
