# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-ended-screen/index.md

---

title: rtk-ended-screen · Cloudflare Realtime docs
description: API reference for rtk-ended-screen component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-ended-screen/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-ended-screen/index.md
---

A screen which shows a meeting has ended.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Global states |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | Global states |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-ended-screen></rtk-ended-screen>
```

### With Properties

```html
<!-- component.html -->
<rtk-ended-screen
 [meeting]="meeting"
 size="md">
</rtk-ended-screen>
```
