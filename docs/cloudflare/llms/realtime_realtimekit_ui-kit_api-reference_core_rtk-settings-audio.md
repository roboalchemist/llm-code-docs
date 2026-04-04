# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-settings-audio/index.md

---

title: rtk-settings-audio · Cloudflare Realtime docs
description: API reference for rtk-settings-audio component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-settings-audio/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-settings-audio/index.md
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
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-settings-audio></rtk-settings-audio>
```

### With Properties

```html
<rtk-settings-audio
 size="md">
</rtk-settings-audio>
```

```html
<script>
  const el = document.querySelector("rtk-settings-audio");


  el.meeting= meeting
</script>
```
