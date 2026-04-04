# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-meeting-title/index.md

---

title: rtk-meeting-title · Cloudflare Realtime docs
description: API reference for rtk-meeting-title component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-meeting-title/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-meeting-title/index.md
---

Displays the title of the meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-meeting-title></rtk-meeting-title>
```

### With Properties

```html
<rtk-meeting-title>
</rtk-meeting-title>
```

```html
<script>
  const el = document.querySelector("rtk-meeting-title");


  el.meeting= meeting
</script>
```
