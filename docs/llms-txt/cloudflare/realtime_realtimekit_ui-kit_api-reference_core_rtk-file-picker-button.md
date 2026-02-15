# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-picker-button/index.md

---

title: rtk-file-picker-button · Cloudflare Realtime docs
description: API reference for rtk-file-picker-button component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-picker-button/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-picker-button/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `filter` | `string` | ✅ | - | File type filter to open file picker with |
| `icon` | `keyof IconPack1` | ✅ | - | Icon |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `label` | `string` | ✅ | - | Label for tooltip |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-file-picker-button></rtk-file-picker-button>
```

### With Properties

```html
<rtk-file-picker-button
 filter="example"
 label="example">
</rtk-file-picker-button>
```

```html
<script>
  const el = document.querySelector("rtk-file-picker-button");


  el.icon= defaultIconPack
</script>
```
