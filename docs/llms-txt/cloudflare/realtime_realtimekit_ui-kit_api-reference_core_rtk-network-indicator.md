# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-network-indicator/index.md

---

title: rtk-network-indicator · Cloudflare Realtime docs
description: API reference for rtk-network-indicator component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-network-indicator/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-network-indicator/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `isScreenShare` | `boolean` | ✅ | - | Is for screenshare |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `participant` | `Peer` | ✅ | - | Participant or Self |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-network-indicator></rtk-network-indicator>
```

### With Properties

```html
<rtk-network-indicator>
</rtk-network-indicator>
```

```html
<script>
  const el = document.querySelector("rtk-network-indicator");


  el.isScreenShare= true;
  el.meeting= meeting
  el.participant= participant
</script>
```
