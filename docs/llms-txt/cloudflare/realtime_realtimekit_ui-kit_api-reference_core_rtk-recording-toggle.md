# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-recording-toggle/index.md

---

title: rtk-recording-toggle · Cloudflare Realtime docs
description: API reference for rtk-recording-toggle component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-recording-toggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-recording-toggle/index.md
---

A button which toggles recording state of a meeting. Only a privileged user can perform this action, thus the button will not be visible for participants who don't have the permission to record a meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `disabled` | `boolean` | ✅ | - | Disable the button |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-recording-toggle></rtk-recording-toggle>
```

### With Properties

```html
<rtk-recording-toggle
 size="md">
</rtk-recording-toggle>
```

```html
<script>
  const el = document.querySelector("rtk-recording-toggle");


  el.disabled= true;
  el.meeting= meeting
</script>
```
