# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai/index.md

---

title: rtk-ai · Cloudflare Realtime docs
description: API reference for rtk-ai component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `view` | `AIView` | ✅ | - | View type |

## Usage Examples

### Basic Usage

```html
<rtk-ai></rtk-ai>
```

### With Properties

```html
<rtk-ai
 size="md">
</rtk-ai>
```

```html
<script>
  const el = document.querySelector("rtk-ai");


  el.meeting= meeting
</script>
```
