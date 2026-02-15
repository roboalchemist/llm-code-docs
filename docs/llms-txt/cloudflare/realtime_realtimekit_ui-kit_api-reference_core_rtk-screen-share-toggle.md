# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-screen-share-toggle/index.md

---

title: rtk-screen-share-toggle · Cloudflare Realtime docs
description: API reference for rtk-screen-share-toggle component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-screen-share-toggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-screen-share-toggle/index.md
---

A button which toggles your screenshare.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-screen-share-toggle></rtk-screen-share-toggle>
```

### With Properties

```html
<rtk-screen-share-toggle
 size="md"
 variant"button">
</rtk-screen-share-toggle>
```

```html
<script>
  const el = document.querySelector("rtk-screen-share-toggle");


  el.meeting= meeting
</script>
```
