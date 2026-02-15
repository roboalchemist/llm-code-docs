# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-controlbar-button/index.md

---

title: rtk-controlbar-button · Cloudflare Realtime docs
description: API reference for rtk-controlbar-button component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-controlbar-button/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-controlbar-button/index.md
---

A skeleton component used for composing custom controlbar buttons.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `brandIcon` | `boolean` | ✅ | - | Whether icon requires brand color |
| `disabled` | `boolean` | ✅ | - | Whether button is disabled |
| `icon` | `string` | ✅ | - | Icon |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isLoading` | `boolean` | ✅ | - | Loading state Ignores current icon and shows a spinner if true |
| `label` | `string` | ✅ | - | Label of button |
| `showWarning` | `boolean` | ✅ | - | Whether to show warning icon |
| `size` | `Size` | ✅ | - | Size |
| `variant` | `ControlBarVariant1` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-controlbar-button></rtk-controlbar-button>
```

### With Properties

```html
<rtk-controlbar-button
 icon="example">
</rtk-controlbar-button>
```

```html
<script>
  const el = document.querySelector("rtk-controlbar-button");


  el.brandIcon= true;
  el.disabled= true;
</script>
```
