# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-menu/index.md

---

title: rtk-menu · Cloudflare Realtime docs
description: API reference for rtk-menu component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-menu/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-menu/index.md
---

A menu component.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `offset` | `number` | ✅ | - | Offset in px |
| `placement` | `Placement` | ✅ | - | Placement of menu |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-menu></rtk-menu>
```

### With Properties

```html
<rtk-menu
 size="md">
</rtk-menu>
```

```html
<script>
  const el = document.querySelector("rtk-menu");


  el.offset= 42;
</script>
```
