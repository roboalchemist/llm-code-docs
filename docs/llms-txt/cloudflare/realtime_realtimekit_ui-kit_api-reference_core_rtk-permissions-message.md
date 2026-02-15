# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-permissions-message/index.md

---

title: rtk-permissions-message · Cloudflare Realtime docs
description: API reference for rtk-permissions-message component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-permissions-message/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-permissions-message/index.md
---

A component which shows permission related troubleshooting information.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-permissions-message></rtk-permissions-message>
```

### With Properties

```html
<rtk-permissions-message>
</rtk-permissions-message>
```

```html
<script>
  const el = document.querySelector("rtk-permissions-message");


  el.meeting= meeting
</script>
```
