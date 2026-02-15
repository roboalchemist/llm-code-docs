# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-text-message-view/index.md

---

title: rtk-text-message-view · Cloudflare Realtime docs
description: API reference for rtk-text-message-view component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-text-message-view/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-text-message-view/index.md
---

A component which renders a text message from chat.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `isMarkdown` | `boolean` | ✅ | - | Renders text as markdown (default = true) |
| `text` | `string` | ✅ | - | Text message |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-text-message-view></rtk-text-message-view>
```

### With Properties

```html
<!-- component.html -->
<rtk-text-message-view
 [isMarkdown]="true"
 text="example">
</rtk-text-message-view>
```
