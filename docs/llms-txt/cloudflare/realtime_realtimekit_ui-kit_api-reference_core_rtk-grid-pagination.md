# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid-pagination/index.md

---

title: rtk-grid-pagination · Cloudflare Realtime docs
description: API reference for rtk-grid-pagination component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid-pagination/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid-pagination/index.md
---

A component which allows you to change current page and view mode of active participants list. This is reflected in the `rtk-grid` component.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size Prop |
| `states` | `States` | ✅ | - | States |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `GridPaginationVariants` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-grid-pagination></rtk-grid-pagination>
```

### With Properties

```html
<rtk-grid-pagination
 size="md">
</rtk-grid-pagination>
```

```html
<script>
  const el = document.querySelector("rtk-grid-pagination");


  el.meeting= meeting
</script>
```
