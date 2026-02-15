# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-setup-screen/index.md

---

title: rtk-setup-screen · Cloudflare Realtime docs
description: API reference for rtk-setup-screen component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-setup-screen/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-setup-screen/index.md
---

A screen shown before joining the meeting, where you can edit your display name, and media settings.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-setup-screen></rtk-setup-screen>
```

### With Properties

```html
<rtk-setup-screen
 size="md">
</rtk-setup-screen>
```

```html
<script>
  const el = document.querySelector("rtk-setup-screen");


  el.meeting= meeting
</script>
```
