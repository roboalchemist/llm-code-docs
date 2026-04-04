# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-toggle/index.md

---

title: rtk-debugger-toggle · Cloudflare Realtime docs
description: API reference for rtk-debugger-toggle component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-toggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-toggle/index.md
---

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
<rtk-debugger-toggle></rtk-debugger-toggle>
```

### With Properties

```html
<rtk-debugger-toggle
 size="md"
 variant"button">
</rtk-debugger-toggle>
```

```html
<script>
  const el = document.querySelector("rtk-debugger-toggle");


  el.meeting= meeting
</script>
```
