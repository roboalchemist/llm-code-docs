# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-toggle/index.md

---

title: rtk-participants-toggle · Cloudflare Realtime docs
description: API reference for rtk-participants-toggle component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-toggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-toggle/index.md
---

A button which toggles visibility of participants. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeSidebar: boolean; sidebar: 'participants' }
```

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-participants-toggle></rtk-participants-toggle>
```

### With Properties

```html
<rtk-participants-toggle
 size="md"
 variant"button">
</rtk-participants-toggle>
```

```html
<script>
  const el = document.querySelector("rtk-participants-toggle");


  el.meeting= meeting
</script>
```
