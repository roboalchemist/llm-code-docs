# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-ui/index.md

---

title: rtk-chat-composer-ui · Cloudflare Realtime docs
description: API reference for rtk-chat-composer-ui component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-ui/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-ui/index.md
---

@deprecated . This component is deprecated, please use rtk-chat-composer-view instead.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `canSendFiles` | `boolean` | ✅ | - | Whether user can send file messages |
| `canSendTextMessage` | `boolean` | ✅ | - | Whether user can send text messages |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `prefill` | `{ suggestedReplies?: string[]; editMessage?: TextMessage; replyMessage?: TextMessage; }` | ❌ | - | prefill the composer |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-chat-composer-ui></rtk-chat-composer-ui>
```

### With Properties

```html
<!-- component.html -->
<rtk-chat-composer-ui
 [canSendFiles]="true"
 [canSendTextMessage]="true"
 size="md">
</rtk-chat-composer-ui>
```
