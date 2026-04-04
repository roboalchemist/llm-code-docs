# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-message-view/index.md

---

title: rtk-image-message-view · Cloudflare Realtime docs
description: API reference for rtk-image-message-view component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-message-view/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-message-view/index.md
---

A component which renders an image message.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `url` | `string` | ✅ | - | Url of the image |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-image-message-view></rtk-image-message-view>
```

### With Properties

```html
<!-- component.html -->
<rtk-image-message-view
 url="example">
</rtk-image-message-view>
```
