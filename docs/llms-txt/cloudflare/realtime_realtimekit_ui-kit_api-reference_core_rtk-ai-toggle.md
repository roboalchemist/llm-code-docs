# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai-toggle/index.md

---

title: rtk-ai-toggle · Cloudflare Realtime docs
description: API reference for rtk-ai-toggle component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai-toggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai-toggle/index.md
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
<rtk-ai-toggle></rtk-ai-toggle>
```

### With Properties

```html
<rtk-ai-toggle
 size="md"
 variant"button">
</rtk-ai-toggle>
```

```html
<script>
  const el = document.querySelector("rtk-ai-toggle");


  el.meeting= meeting
</script>
```
