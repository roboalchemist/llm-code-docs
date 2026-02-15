# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-emoji-picker-button/index.md

---

title: rtk-emoji-picker-button · Cloudflare Realtime docs
description: API reference for rtk-emoji-picker-button component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-emoji-picker-button/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-emoji-picker-button/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `isActive` | `boolean` | ✅ | - | Active state indicator |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-emoji-picker-button></rtk-emoji-picker-button>
```

### With Properties

```html
<!-- component.html -->
<rtk-emoji-picker-button
 [isActive]="true">
</rtk-emoji-picker-button>
```
