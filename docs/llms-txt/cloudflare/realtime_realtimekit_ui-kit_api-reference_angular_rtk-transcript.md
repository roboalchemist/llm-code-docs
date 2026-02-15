# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-transcript/index.md

---

title: rtk-transcript · Cloudflare Realtime docs
description: API reference for rtk-transcript component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-transcript/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-transcript/index.md
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
<!-- component.html -->
<rtk-transcript></rtk-transcript>
```

### With Properties

```html
<!-- component.html -->
<rtk-transcript
 [t]="rtki18n"
 transcript="example">
</rtk-transcript>
```
