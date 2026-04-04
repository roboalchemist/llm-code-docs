# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-composer-view/index.md

---

title: rtk-chat-composer-view · Cloudflare Realtime docs
description: API reference for rtk-chat-composer-view component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-composer-view/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-composer-view/index.md
---

A component which renders a chat composer

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `canSendFiles` | `boolean` | ✅ | - | Whether user can send file messages |
| `canSendTextMessage` | `boolean` | ✅ | - | Whether user can send text messages |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `inputTextPlaceholder` | `string` | ✅ | - | Placeholder for text input |
| `isEditing` | `boolean` | ✅ | - | Sets composer to edit mode |
| `maxLength` | `number` | ✅ | - | Max length for text input |
| `message` | `string` | ✅ | - | Message to be pre-populated |
| `quotedMessage` | `string` | ✅ | - | Quote message to be displayed |
| `rateLimits` | `{ period: number; maxInvocations: number; }` | ✅ | - | Rate limits |
| `storageKey` | `string` | ✅ | - | Key for storing message in localStorage |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-chat-composer-view></rtk-chat-composer-view>
```

### With Properties

```html
<rtk-chat-composer-view
 inputTextPlaceholder="example">
</rtk-chat-composer-view>
```

```html
<script>
  const el = document.querySelector("rtk-chat-composer-view");


  el.canSendFiles= true;
  el.canSendTextMessage= true;
</script>
```
