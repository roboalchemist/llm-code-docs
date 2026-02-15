# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-poll/index.md

---

title: rtk-poll · Cloudflare Realtime docs
description: API reference for rtk-poll component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-poll/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-poll/index.md
---

A poll component. Shows a poll where a user can vote.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `permissions` | `RTKPermissionsPreset` | ✅ | - | Permissions Object |
| `poll` | `Poll` | ✅ | - | Poll |
| `self` | `string` | ✅ | - | Self ID |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-poll></rtk-poll>
```

### With Properties

```html
<!-- component.html -->
<rtk-poll
 [permissions]="rtkpermissionspreset"
 [poll]="poll"
 self="example">
</rtk-poll>
```
