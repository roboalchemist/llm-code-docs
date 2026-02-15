# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar/index.md

---

title: rtk-sidebar · Cloudflare Realtime docs
description: API reference for rtk-sidebar component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar/index.md
---

A component which handles the sidebar and you can customize which sections you want, and which section you want as the default.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `defaultSection` | `RtkSidebarSection` | ✅ | - | Default section |
| `enabledSections` | `RtkSidebarTab[]` | ✅ | - | Enabled sections in sidebar |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `view` | `RtkSidebarView` | ✅ | - | View type |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-sidebar></rtk-sidebar>
```

### With Properties

```html
<!-- component.html -->
<rtk-sidebar
 [defaultSection]="rtksidebarsection"
 [enabledSections]="[]"
 [meeting]="meeting">
</rtk-sidebar>
```
