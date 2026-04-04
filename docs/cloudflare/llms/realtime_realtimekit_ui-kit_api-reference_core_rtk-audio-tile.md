# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-tile/index.md

---

title: rtk-audio-tile · Cloudflare Realtime docs
description: API reference for rtk-audio-tile component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-tile/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-tile/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ✅ | - | Config |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-audio-tile></rtk-audio-tile>
```

### With Properties

```html
<rtk-audio-tile>
</rtk-audio-tile>
```

```html
<script>
  const el = document.querySelector("rtk-audio-tile");


  el.config= defaultUiConfig
  el.meeting= meeting
  el.participant= participant
</script>
```
