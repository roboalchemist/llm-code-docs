# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-switch/index.md

---

title: rtk-switch · Cloudflare Realtime docs
description: API reference for rtk-switch component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-switch/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-switch/index.md
---

A switch component which follows RTK Design System.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `checked` | `boolean` | ✅ | - | Whether the switch is enabled/checked |
| `disabled` | `boolean` | ✅ | - | Whether switch is readonly |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `readonly` | `boolean` | ✅ | - | Whether switch is readonly |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-switch></rtk-switch>
```

### With Properties

```html
<rtk-switch>
</rtk-switch>
```

```html
<script>
  const el = document.querySelector("rtk-switch");


  el.checked= true;
  el.disabled= true;
  el.readonly= true;
</script>
```
