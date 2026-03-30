# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-picker-button/index.md

---

title: rtk-file-picker-button · Cloudflare Realtime docs
description: API reference for rtk-file-picker-button component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-picker-button/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-picker-button/index.md
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
<!-- component.html -->
<rtk-file-picker-button></rtk-file-picker-button>
```

### With Properties

```html
<!-- component.html -->
<rtk-file-picker-button
 filter="example"
 [icon]="defaultIconPack"
 label="example">
</rtk-file-picker-button>
```
