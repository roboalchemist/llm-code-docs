# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-broadcast-message-modal/index.md

---

title: rtk-broadcast-message-modal · Cloudflare Realtime docs
description: API reference for rtk-broadcast-message-modal component (Web
  Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-broadcast-message-modal/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-broadcast-message-modal/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-broadcast-message-modal></rtk-broadcast-message-modal>
```

### With Properties

```html
<rtk-broadcast-message-modal>
</rtk-broadcast-message-modal>
```

```html
<script>
  const el = document.querySelector("rtk-broadcast-message-modal");


  el.meeting= meeting
</script>
```
