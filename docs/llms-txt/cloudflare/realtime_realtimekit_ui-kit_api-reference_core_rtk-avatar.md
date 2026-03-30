# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-avatar/index.md

---

title: rtk-avatar · Cloudflare Realtime docs
description: API reference for rtk-avatar component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-avatar/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-avatar/index.md
---

Avatar component which renders a participant's image or their initials.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `participant` | `Peer \| WaitlistedParticipant \| { name: string; picture: string }` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `AvatarVariant` | ✅ | - | Avatar type |

## Usage Examples

### Basic Usage

```html
<rtk-avatar></rtk-avatar>
```

### With Properties

```html
<rtk-avatar
 participant="example"
 size="md"
 variant="circular">
</rtk-avatar>
```

```html
<script>
  const el = document.querySelector("rtk-avatar");


  el.participant= {};
</script>
```
