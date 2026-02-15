# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-spotlight-indicator/index.md

---

title: rtk-spotlight-indicator · Cloudflare Realtime docs
description: API reference for rtk-spotlight-indicator component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-spotlight-indicator/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-spotlight-indicator/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-spotlight-indicator></rtk-spotlight-indicator>
```

### With Properties

```html
<rtk-spotlight-indicator
 size="md">
</rtk-spotlight-indicator>
```

```html
<script>
  const el = document.querySelector("rtk-spotlight-indicator");


  el.meeting= meeting
</script>
```
