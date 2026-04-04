# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants-waiting-list/index.md

---

title: rtk-participants-waiting-list · Cloudflare Realtime docs
description: API reference for rtk-participants-waiting-list component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants-waiting-list/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants-waiting-list/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-participants-waiting-list></rtk-participants-waiting-list>
```

### With Properties

```html
<!-- component.html -->
<rtk-participants-waiting-list
 [meeting]="meeting"
 size="md"
 [view]="participantsviewmode">
</rtk-participants-waiting-list>
```
