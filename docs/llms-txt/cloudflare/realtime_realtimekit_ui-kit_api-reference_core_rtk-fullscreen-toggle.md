# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-fullscreen-toggle/index.md

---

title: rtk-fullscreen-toggle · Cloudflare Realtime docs
description: API reference for rtk-fullscreen-toggle component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-fullscreen-toggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-fullscreen-toggle/index.md
---

A button which toggles full screen mode for any existing `rtk-meeting` component in the DOM.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `targetElement` | `HTMLElement` | ✅ | - | Target Element to fullscreen |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-fullscreen-toggle></rtk-fullscreen-toggle>
```

### With Properties

```html
<rtk-fullscreen-toggle
 size="md"
 variant"button">
</rtk-fullscreen-toggle>
```

```html
<script>
  const el = document.querySelector("rtk-fullscreen-toggle");


</script>
```
