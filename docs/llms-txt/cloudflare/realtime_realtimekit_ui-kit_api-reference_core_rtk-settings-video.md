# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-settings-video/index.md

---

title: rtk-settings-video · Cloudflare Realtime docs
description: API reference for rtk-settings-video component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-settings-video/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-settings-video/index.md
---

A component which lets to manage your camera devices and your video preferences. Emits `rtkStateUpdate` event with data for toggling mirroring of self video:

```ts
{
 prefs: {
   mirrorVideo: boolean
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
<rtk-settings-video></rtk-settings-video>
```

### With Properties

```html
<rtk-settings-video
 size="md">
</rtk-settings-video>
```

```html
<script>
  const el = document.querySelector("rtk-settings-video");


  el.meeting= meeting
</script>
```
