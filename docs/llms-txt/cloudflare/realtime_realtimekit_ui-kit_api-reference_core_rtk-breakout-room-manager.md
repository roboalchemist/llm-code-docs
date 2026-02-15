# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-manager/index.md

---

title: rtk-breakout-room-manager · Cloudflare Realtime docs
description: API reference for rtk-breakout-room-manager component (Web
  Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-manager/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-manager/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `allowDelete` | `boolean` | ✅ | - | allow room delete |
| `assigningParticipants` | `boolean` | ✅ | - | Enable updating participants |
| `defaultExpanded` | `boolean` | ✅ | - | display expanded card by default |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isDragMode` | `boolean` | ✅ | - | Drag mode |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `mode` | `'edit' \| 'create'` | ✅ | - | Mode in which selector is used |
| `room` | `DraftMeeting` | ✅ | - | Connected Room Config Object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-breakout-room-manager></rtk-breakout-room-manager>
```

### With Properties

```html
<rtk-breakout-room-manager>
</rtk-breakout-room-manager>
```

```html
<script>
  const el = document.querySelector("rtk-breakout-room-manager");


  el.allowDelete= true;
  el.assigningParticipants= true;
  el.defaultExpanded= true;
</script>
```
