# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-leave-button/index.md

---

title: rtk-leave-button · Cloudflare Realtime docs
description: API reference for rtk-leave-button component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-leave-button/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-leave-button/index.md
---

A button which toggles visilibility of the leave confirmation dialog.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-leave-button></rtk-leave-button>
```

### With Properties

```html
<rtk-leave-button
 size="md"
 variant"button">
</rtk-leave-button>
```

```html
<script>
  const el = document.querySelector("rtk-leave-button");


</script>
```
