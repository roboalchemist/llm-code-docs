# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-polls/index.md

---

title: rtk-polls · Cloudflare Realtime docs
description: API reference for rtk-polls component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-polls/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-polls/index.md
---

A component which lists all available plugins a user can access with the ability to enable or disable them as per their permissions.

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
<rtk-polls></rtk-polls>
```

### With Properties

```html
<rtk-polls
 size="md">
</rtk-polls>
```

```html
<script>
  const el = document.querySelector("rtk-polls");


  el.meeting= meeting
</script>
```
