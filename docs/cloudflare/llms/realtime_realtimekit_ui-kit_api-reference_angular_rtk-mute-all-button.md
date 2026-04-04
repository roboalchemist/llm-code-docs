# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-mute-all-button/index.md

---

title: rtk-mute-all-button · Cloudflare Realtime docs
description: API reference for rtk-mute-all-button component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-mute-all-button/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-mute-all-button/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-mute-all-button></rtk-mute-all-button>
```

### With Properties

```html
<!-- component.html -->
<rtk-mute-all-button
 [meeting]="meeting"
 size="md"
 variant="button">
</rtk-mute-all-button>
```
