# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-microphone-selector/index.md

---

title: rtk-microphone-selector · Cloudflare Realtime docs
description: API reference for rtk-microphone-selector component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-microphone-selector/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-microphone-selector/index.md
---

A component which lets to manage your audio devices and audio preferences. Emits `rtkStateUpdate` event with data for muting notification sounds:

```ts
{
 prefs: {
   muteNotificationSounds: boolean
 }
}
```

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'full' \| 'inline'` | ✅ | - | variant |

## Usage Examples

### Basic Usage

```html
<rtk-microphone-selector></rtk-microphone-selector>
```

### With Properties

```html
<rtk-microphone-selector
 size="md">
</rtk-microphone-selector>
```

```html
<script>
  const el = document.querySelector("rtk-microphone-selector");


  el.meeting= meeting
</script>
```
