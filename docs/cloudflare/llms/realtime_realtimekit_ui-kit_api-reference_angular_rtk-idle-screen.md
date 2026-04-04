# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-idle-screen/index.md

---

title: rtk-idle-screen · Cloudflare Realtime docs
description: API reference for rtk-idle-screen component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-idle-screen/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-idle-screen/index.md
---

A screen that handles the idle state, i.e; when you are waiting for data about the meeting, specifically the `meeting` object.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-idle-screen></rtk-idle-screen>
```

### With Properties

```html
<!-- component.html -->
<rtk-idle-screen
 [meeting]="meeting">
</rtk-idle-screen>
```
