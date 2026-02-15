# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-viewer/index.md

---

title: rtk-image-viewer · Cloudflare Realtime docs
description: API reference for rtk-image-viewer component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-viewer/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-viewer/index.md
---

A component which shows an image sent via chat.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `image` | `ImageMessage` | ✅ | - | Image message |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-image-viewer></rtk-image-viewer>
```

### With Properties

```html
<rtk-image-viewer
 size="md">
</rtk-image-viewer>
```

```html
<script>
  const el = document.querySelector("rtk-image-viewer");


</script>
```
