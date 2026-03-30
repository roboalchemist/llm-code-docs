# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-rooms-manager/index.md

---

title: rtk-breakout-rooms-manager · Cloudflare Realtime docs
description: API reference for rtk-breakout-rooms-manager component (Web
  Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-rooms-manager/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-rooms-manager/index.md
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
<rtk-breakout-rooms-manager></rtk-breakout-rooms-manager>
```

### With Properties

```html
<rtk-breakout-rooms-manager>
</rtk-breakout-rooms-manager>
```

```html
<script>
  const el = document.querySelector("rtk-breakout-rooms-manager");


  el.meeting= meeting
</script>
```
