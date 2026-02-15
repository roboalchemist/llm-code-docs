# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-tab-bar/index.md

---

title: rtk-tab-bar · Cloudflare Realtime docs
description: API reference for rtk-tab-bar component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-tab-bar/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-tab-bar/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `activeTab` | `Tab` | ✅ | - | Active tab |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `layout` | `GridLayout1` | ✅ | - | Grid Layout |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `tabs` | `Tab[]` | ✅ | - | Tabs |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-tab-bar></rtk-tab-bar>
```

### With Properties

```html
<!-- component.html -->
<rtk-tab-bar
 [activeTab]="tab"
 [layout]="gridlayout1"
 [meeting]="meeting">
</rtk-tab-bar>
```
