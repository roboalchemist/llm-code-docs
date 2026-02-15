# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-counter/index.md

---

title: rtk-counter · Cloudflare Realtime docs
description: API reference for rtk-counter component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-counter/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-counter/index.md
---

A number picker with increment and decrement buttons.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `minValue` | `number` | ✅ | - | Minimum value |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `value` | `number` | ✅ | - | Initial value |

## Usage Examples

### Basic Usage

```html
<rtk-counter></rtk-counter>
```

### With Properties

```html
<rtk-counter
 size="md">
</rtk-counter>
```

```html
<script>
  const el = document.querySelector("rtk-counter");


  el.minValue= 42;
  el.value= 42;
</script>
```
