# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-pinned-message-selector/index.md

---

title: rtk-pinned-message-selector · Cloudflare Realtime docs
description: API reference for rtk-pinned-message-selector component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-pinned-message-selector/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-pinned-message-selector/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-pinned-message-selector></rtk-pinned-message-selector>
```

### With Properties

```html
<!-- component.html -->
<rtk-pinned-message-selector
 [meeting]="meeting">
</rtk-pinned-message-selector>
```
