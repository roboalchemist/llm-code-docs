# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-name-tag/index.md

---

title: rtk-name-tag · Cloudflare Realtime docs
description: API reference for rtk-name-tag component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-name-tag/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-name-tag/index.md
---

A component which shows a participant's name.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isScreenShare` | `boolean` | ✅ | - | Whether it is used in a screen share view |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `RtkNameTagVariant` | ✅ | - | Name tag variant |

## Usage Examples

### Basic Usage

```html
<rtk-name-tag></rtk-name-tag>
```

### With Properties

```html
<rtk-name-tag>
</rtk-name-tag>
```

```html
<script>
  const el = document.querySelector("rtk-name-tag");


  el.isScreenShare= true;
  el.meeting= meeting
  el.participant= participant
</script>
```
