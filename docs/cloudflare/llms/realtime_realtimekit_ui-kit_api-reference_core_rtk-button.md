# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-button/index.md

---

title: rtk-button · Cloudflare Realtime docs
description: API reference for rtk-button component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-button/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-button/index.md
---

A button that follows RTK Design System.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `disabled` | `boolean` | ✅ | - | Where the button is disabled or not |
| `kind` | `ButtonKind` | ✅ | - | Button type |
| `reverse` | `boolean` | ✅ | - | Whether to reverse order of children |
| `size` | `Size` | ✅ | - | Size |
| `type` | `HTMLButtonElement['type']` | ✅ | - | Button type |
| `variant` | `ButtonVariant` | ✅ | - | Button variant |

## Usage Examples

### Basic Usage

```html
<rtk-button></rtk-button>
```

### With Properties

```html
<rtk-button>
</rtk-button>
```

```html
<script>
  const el = document.querySelector("rtk-button");


  el.disabled= true;
  el.reverse= true;
</script>
```
