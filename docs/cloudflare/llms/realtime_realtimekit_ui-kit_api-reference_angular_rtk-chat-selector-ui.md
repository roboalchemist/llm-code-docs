# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-selector-ui/index.md

---

title: rtk-chat-selector-ui · Cloudflare Realtime docs
description: API reference for rtk-chat-selector-ui component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-selector-ui/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-selector-ui/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `groups` | `ChatGroup[]` | ✅ | - | Participants |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `selectedGroupId` | `string` | ✅ | - | Selected participant |
| `selfUserId` | `string` | ✅ | - | Self User ID |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `unreadCounts` | `Record<string, number>` | ✅ | - | Unread counts |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-chat-selector-ui></rtk-chat-selector-ui>
```

### With Properties

```html
<!-- component.html -->
<rtk-chat-selector-ui
 [groups]="[]"
 selectedGroupId="example"
 selfUserId="example">
</rtk-chat-selector-ui>
```
