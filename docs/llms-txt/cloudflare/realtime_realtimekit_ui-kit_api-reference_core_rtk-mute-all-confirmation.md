# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mute-all-confirmation/index.md

---

title: rtk-mute-all-confirmation · Cloudflare Realtime docs
description: API reference for rtk-mute-all-confirmation component (Web
  Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mute-all-confirmation/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mute-all-confirmation/index.md
---

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
<rtk-mute-all-confirmation></rtk-mute-all-confirmation>
```

### With Properties

```html
<rtk-mute-all-confirmation>
</rtk-mute-all-confirmation>
```

```html
<script>
  const el = document.querySelector("rtk-mute-all-confirmation");


  el.meeting= meeting
</script>
```
