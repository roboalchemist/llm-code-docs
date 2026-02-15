# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-message-list-view/index.md

---

title: rtk-message-list-view · Cloudflare Realtime docs
description: API reference for rtk-message-list-view component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-message-list-view/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-message-list-view/index.md
---

A component which renders list of messages.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `estimateItemSize` | `number` | ✅ | - | Estimated height of an item |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `loadMore` | `(lastMessage: Message)` | ✅ | - | Function to load more messages. Messages returned from this will be preprended |
| `messages` | `Message[]` | ✅ | - | Messages to render |
| `renderer` | `(message: Message, index: number)` | ✅ | - | Render function of the message |
| `visibleItemsCount` | `number` | ✅ | - | Maximum visible messages |

## Usage Examples

### Basic Usage

```html
<rtk-message-list-view></rtk-message-list-view>
```

### With Properties

```html
<rtk-message-list-view>
</rtk-message-list-view>
```

```html
<script>
  const el = document.querySelector("rtk-message-list-view");


  el.estimateItemSize= 42;
  el.messages= [];
</script>
```
