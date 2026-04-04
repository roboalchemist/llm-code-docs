# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-message-view/index.md

---

title: rtk-file-message-view · Cloudflare Realtime docs
description: API reference for rtk-file-message-view component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-message-view/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-message-view/index.md
---

A component which renders a file message.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `name` | `string` | ✅ | - | Name of the file |
| `size` | `number` | ✅ | - | Size of the file |
| `url` | `string` | ✅ | - | Url of the file |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-file-message-view></rtk-file-message-view>
```

### With Properties

```html
<!-- component.html -->
<rtk-file-message-view
 name="example"
 size="42"
 url="example">
</rtk-file-message-view>
```
