# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai-transcriptions/index.md

---

title: rtk-ai-transcriptions · Cloudflare Realtime docs
description: API reference for rtk-ai-transcriptions component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai-transcriptions/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai-transcriptions/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `initialTranscriptions` | `Transcript[]` | ✅ | - | Initial transcriptions |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-ai-transcriptions></rtk-ai-transcriptions>
```

### With Properties

```html
<rtk-ai-transcriptions>
</rtk-ai-transcriptions>
```

```html
<script>
  const el = document.querySelector("rtk-ai-transcriptions");


  el.initialTranscriptions= [];
  el.meeting= meeting
</script>
```
