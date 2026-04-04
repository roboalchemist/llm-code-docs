# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcript/index.md

---

title: rtk-transcript · Cloudflare Realtime docs
description: API reference for rtk-transcript component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcript/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcript/index.md
---

A component which shows a transcript. You need to remove the element after you receive the `rtkTranscriptDismiss` event.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `transcript` | `Transcript & { renderedId?: string }` | ❌ | - | Message |

## Usage Examples

### Basic Usage

```html
<rtk-transcript></rtk-transcript>
```

### With Properties

```html
<rtk-transcript
 transcript="example">
</rtk-transcript>
```

```html
<script>
  const el = document.querySelector("rtk-transcript");


  el.transcript= {};
</script>
```
