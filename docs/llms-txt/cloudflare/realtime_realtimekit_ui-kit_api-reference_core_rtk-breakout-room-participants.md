# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-participants/index.md

---

title: rtk-breakout-room-participants · Cloudflare Realtime docs
description: API reference for rtk-breakout-room-participants component (Web
  Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-participants/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-participants/index.md
---

A component which lists all participants, with ability to run privileged actions on each participant according to your permissions.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participantIds` | `string[]` | ✅ | - | Participant ids |
| `selectedParticipantIds` | `string[]` | ✅ | - | selected participants |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-breakout-room-participants></rtk-breakout-room-participants>
```

### With Properties

```html
<rtk-breakout-room-participants
 participantIds="example"
 selectedParticipantIds="example">
</rtk-breakout-room-participants>
```

```html
<script>
  const el = document.querySelector("rtk-breakout-room-participants");


  el.meeting= meeting
  el.participantIds= [];
  el.selectedParticipantIds= [];
</script>
```
