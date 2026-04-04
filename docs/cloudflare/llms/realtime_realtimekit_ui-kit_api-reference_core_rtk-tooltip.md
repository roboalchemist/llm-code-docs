# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/index.md

---

title: rtk-tooltip · Cloudflare Realtime docs
description: API reference for rtk-tooltip component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/index.md
---

Tooltip component which follows RTK Design System.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `delay` | `number` | ✅ | - | Delay before showing the tooltip |
| `disabled` | `boolean` | ✅ | - | Disabled |
| `kind` | `TooltipKind` | ✅ | - | Tooltip kind |
| `label` | `string` | ✅ | - | Tooltip label |
| `open` | `boolean` | ✅ | - | Open |
| `placement` | `Placement` | ✅ | - | Placement of menu |
| `size` | `Size` | ✅ | - | Size |
| `variant` | `TooltipVariant` | ✅ | - | Tooltip variant |

## Usage Examples

### Basic Usage

```html
<rtk-tooltip></rtk-tooltip>
```

### With Properties

```html
<rtk-tooltip>
</rtk-tooltip>
```

```html
<script>
  const el = document.querySelector("rtk-tooltip");


  el.delay= 42;
  el.disabled= true;
</script>
```
