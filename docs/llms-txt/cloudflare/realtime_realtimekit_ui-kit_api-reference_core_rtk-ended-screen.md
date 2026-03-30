# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ended-screen/index.md

---

title: rtk-ended-screen · Cloudflare Realtime docs
description: API reference for rtk-ended-screen component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ended-screen/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ended-screen/index.md
---

A screen which shows a meeting has ended.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Global states |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | Global states |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-ended-screen></rtk-ended-screen>
```

### With Properties

```html
<rtk-ended-screen
 size="md">
</rtk-ended-screen>
```

```html
<script>
  const el = document.querySelector("rtk-ended-screen");


  el.meeting= meeting
</script>
```
