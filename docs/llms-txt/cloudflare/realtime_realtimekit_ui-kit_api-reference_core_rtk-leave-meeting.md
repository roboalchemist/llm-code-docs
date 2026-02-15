# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-leave-meeting/index.md

---

title: rtk-leave-meeting · Cloudflare Realtime docs
description: API reference for rtk-leave-meeting component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-leave-meeting/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-leave-meeting/index.md
---

A component which allows you to leave a meeting or end meeting for all, if you have the permission.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-leave-meeting></rtk-leave-meeting>
```

### With Properties

```html
<rtk-leave-meeting>
</rtk-leave-meeting>
```

```html
<script>
  const el = document.querySelector("rtk-leave-meeting");


  el.meeting= meeting
</script>
```
