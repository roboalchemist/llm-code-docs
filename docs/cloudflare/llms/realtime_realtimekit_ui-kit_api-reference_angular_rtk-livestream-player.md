# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-livestream-player/index.md

---

title: rtk-livestream-player · Cloudflare Realtime docs
description: API reference for rtk-livestream-player component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-livestream-player/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-livestream-player/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-livestream-player></rtk-livestream-player>
```

### With Properties

```html
<!-- component.html -->
<rtk-livestream-player
 [meeting]="meeting"
 size="md">
</rtk-livestream-player>
```
