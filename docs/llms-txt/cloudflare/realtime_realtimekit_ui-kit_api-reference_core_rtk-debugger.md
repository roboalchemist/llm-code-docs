# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger/index.md

---

title: rtk-debugger · Cloudflare Realtime docs
description: API reference for rtk-debugger component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger/index.md
---

A troubleshooting component to identify and fix any issues in the meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-debugger></rtk-debugger>
```

### With Properties

```html
<rtk-debugger
 size="md">
</rtk-debugger>
```

```html
<script>
  const el = document.querySelector("rtk-debugger");


  el.meeting= meeting
</script>
```
