# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-messages-ui-paginated/index.md

---

title: rtk-chat-messages-ui-paginated · Cloudflare Realtime docs
description: API reference for rtk-chat-messages-ui-paginated component (Web
  Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-messages-ui-paginated/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-messages-ui-paginated/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `privateChatRecipient` | `Participant \| null` | ✅ | - | Selected recipient for private chat; when unset, messages are loaded for public chat (Everyone). |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-chat-messages-ui-paginated></rtk-chat-messages-ui-paginated>
```

### With Properties

```html
<rtk-chat-messages-ui-paginated
 size="md">
</rtk-chat-messages-ui-paginated>
```

```html
<script>
  const el = document.querySelector("rtk-chat-messages-ui-paginated");


  el.meeting= meeting
</script>
```
