# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant-count/index.md

---

title: rtk-participant-count · Cloudflare Realtime docs
description: API reference for rtk-participant-count component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant-count/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant-count/index.md
---

A component which shows count of total joined participants in a meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-participant-count></rtk-participant-count>
```

### With Properties

```html
<rtk-participant-count
 size="md">
</rtk-participant-count>
```

```html
<script>
  const el = document.querySelector("rtk-participant-count");


  el.meeting= meeting
</script>
```
