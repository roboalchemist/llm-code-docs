# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-clock/index.md

---

title: rtk-clock · Cloudflare Realtime docs
description: API reference for rtk-clock component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-clock/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-clock/index.md
---

Shows the time elapsed in a meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |

## Usage Examples

### Basic Usage

```html
<rtk-clock></rtk-clock>
```

### With Properties

```html
<rtk-clock
 size="md">
</rtk-clock>
```

```html
<script>
  const el = document.querySelector("rtk-clock");


  el.meeting= meeting
</script>
```
