# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-livestream-toggle/index.md

---

title: rtk-livestream-toggle · Cloudflare Realtime docs
description: API reference for rtk-livestream-toggle component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-livestream-toggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-livestream-toggle/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-livestream-toggle></rtk-livestream-toggle>
```

### With Properties

```html
<!-- component.html -->
<rtk-livestream-toggle
 [meeting]="meeting"
 size="md"
 variant="button">
</rtk-livestream-toggle>
```
