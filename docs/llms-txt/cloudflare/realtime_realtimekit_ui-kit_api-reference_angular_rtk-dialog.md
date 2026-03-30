# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-dialog/index.md

---

title: rtk-dialog · Cloudflare Realtime docs
description: API reference for rtk-dialog component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-dialog/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-dialog/index.md
---

A dialog component.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `disableEscapeKey` | `boolean` | ✅ | - | Whether Escape key can close the modal |
| `hideCloseButton` | `boolean` | ✅ | - | Whether to show the close button |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `open` | `boolean` | ✅ | - | Whether a dialog is open or not |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-dialog></rtk-dialog>
```

### With Properties

```html
<!-- component.html -->
<rtk-dialog
 [disableEscapeKey]="true"
 [hideCloseButton]="true"
 [meeting]="meeting">
</rtk-dialog>
```
