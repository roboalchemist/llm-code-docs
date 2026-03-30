# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-plugins/index.md

---

title: rtk-plugins · Cloudflare Realtime docs
description: API reference for rtk-plugins component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-plugins/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-plugins/index.md
---

A component which lists all available plugins from their preset, and ability to enable or disable plugins.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-plugins></rtk-plugins>
```

### With Properties

```html
<rtk-plugins
 size="md">
</rtk-plugins>
```

```html
<script>
  const el = document.querySelector("rtk-plugins");


  el.meeting= meeting
</script>
```
