# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-messages-ui/index.md

---

title: rtk-chat-messages-ui · Cloudflare Realtime docs
description: API reference for rtk-chat-messages-ui component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-messages-ui/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-messages-ui/index.md
---

@deprecated Use `rtk-chat-messages-ui-paginated` instead.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `canPinMessages` | `boolean` | ✅ | - | Can current user pin/unpin messages |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `messages` | `Chat[]` | ✅ | - | Chat Messages |
| `selectedGroup` | `string` | ✅ | - | Selected group key |
| `selfUserId` | `string` | ✅ | - | User ID of self user |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-chat-messages-ui></rtk-chat-messages-ui>
```

### With Properties

```html
<!-- component.html -->
<rtk-chat-messages-ui
 [canPinMessages]="true"
 [messages]="[]"
 selectedGroup="example">
</rtk-chat-messages-ui>
```
