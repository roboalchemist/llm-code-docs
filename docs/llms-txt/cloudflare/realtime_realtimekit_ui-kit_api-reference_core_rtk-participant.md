# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant/index.md

---

title: rtk-participant · Cloudflare Realtime docs
description: API reference for rtk-participant component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant/index.md
---

A participant entry component used inside `rtk-participants` which shows data like: name, picture and media device status. You can perform privileged actions on the participant too.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participant` | `Peer` | ✅ | - | Participant object |
| `states` | `States1` | ✅ | - | States |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `view` | `ParticipantViewMode` | ✅ | - | Show participant summary |

## Usage Examples

### Basic Usage

```html
<rtk-participant></rtk-participant>
```

### With Properties

```html
<rtk-participant>
</rtk-participant>
```

```html
<script>
  const el = document.querySelector("rtk-participant");


  el.meeting= meeting
  el.participant= participant
</script>
```
