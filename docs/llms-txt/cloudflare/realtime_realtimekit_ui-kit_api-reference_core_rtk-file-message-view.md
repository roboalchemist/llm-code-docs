# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-message-view/index.md

---

title: rtk-file-message-view · Cloudflare Realtime docs
description: API reference for rtk-file-message-view component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-message-view/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-message-view/index.md
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
<rtk-file-message-view></rtk-file-message-view>
```

### With Properties

```html
<rtk-file-message-view
 name="example"
 url="example">
</rtk-file-message-view>
```

```html
<script>
  const el = document.querySelector("rtk-file-message-view");


  el.size= 42;
</script>
```
