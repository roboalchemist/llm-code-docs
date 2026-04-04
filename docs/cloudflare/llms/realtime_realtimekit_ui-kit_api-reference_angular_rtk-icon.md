# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-icon/index.md

---

title: rtk-icon · Cloudflare Realtime docs
description: API reference for rtk-icon component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-icon/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-icon/index.md
---

An icon component which accepts an svg string and renders it.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `icon` | `string` | ✅ | - | Icon |
| `size` | `Size1` | ✅ | - | Size |
| `variant` | `IconVariant` | ✅ | - | Icon variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-icon></rtk-icon>
```

### With Properties

```html
<!-- component.html -->
<rtk-icon
 icon="example"
 size="md"
 variant="primary">
</rtk-icon>
```
