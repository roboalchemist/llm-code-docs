# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-screenshare/index.md

---

title: rtk-debugger-screenshare · Cloudflare Realtime docs
description: API reference for rtk-debugger-screenshare component (Web
  Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-screenshare/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-screenshare/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-debugger-screenshare></rtk-debugger-screenshare>
```

### With Properties

```html
<rtk-debugger-screenshare
 size="md">
</rtk-debugger-screenshare>
```

```html
<script>
  const el = document.querySelector("rtk-debugger-screenshare");


  el.meeting= meeting
</script>
```
